"""Bounded-edit regressions: no out-of-region writes, stale writes or link loss."""
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import whitepaper_blocks as blocks


def book(eol=b'\n'):
    lines = ['# 测试正文', '## 题记', '前言保留。']
    for index, block_id in enumerate(blocks.BLOCK_IDS):
        if block_id == 'appendix':
            lines += ['## 结语：保留', '结语不属于第八章。']
        anchor = f'chapter-{index + 1}' if index < 8 else 'rfc-directory'
        lines += [f'<!-- SP:BEGIN {block_id} -->', f'<a id="{anchor}"></a>',
                  '## ' + blocks.CHAPTER_NAMES[block_id] + '：标题',
                  '原有内容。', f'<!-- SP:END {block_id} -->']
    return eol.join(line.encode() for line in lines) + eol


class BlockTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.path = self.root / '正文.md'
        self.original = book(b'\r\n')
        self.path.write_bytes(self.original)

    def replacement(self):
        block = blocks.find_block(self.original, 'chapter-07')
        body = block.body(self.original)
        return body.replace('原有内容。'.encode(), '新的内容。'.encode()), blocks.digest(body)

    def test_real_public_whitepaper_has_nine_readable_regions(self):
        data = blocks.DEFAULT_FILE.read_bytes()
        self.assertEqual(list(blocks.BLOCK_IDS), [b.id for b in blocks.parse_blocks(data)])
        seventh = blocks.find_block(data, 'chapter-07').body(data)
        self.assertIn('### 7.2 SP-RFC-018'.encode(), seventh)
        self.assertNotIn('## 第八章'.encode(), seventh)

    def test_apply_preserves_all_bytes_outside_region_and_saves_exact_backup(self):
        replacement, expected = self.replacement()
        block = blocks.find_block(self.original, 'chapter-07')
        edit = blocks.plan_replace(self.path, block.id, replacement, expected)
        backup = blocks.apply_edit(edit, self.root / 'backups')
        actual = self.path.read_bytes()
        self.assertEqual(self.original[:block.start] + replacement + self.original[block.stop:], actual)
        self.assertEqual(self.original, backup.read_bytes())
        self.assertFalse(list(self.root.glob('*.lock')))
        self.assertFalse(list(self.root.glob('.sp-block-*')))

    def test_preview_does_not_write_or_create_backup(self):
        payload, expected = self.replacement()
        source = self.root / 'edit.md'
        source.write_bytes(payload)
        with redirect_stdout(StringIO()) as output, redirect_stderr(StringIO()):
            result = blocks.main(['--file', str(self.path), 'replace', 'chapter-07',
                                  '--from-file', str(source), '--expect-sha256', expected])
        self.assertEqual(0, result)
        self.assertIn('proposed', output.getvalue())
        self.assertEqual(self.original, self.path.read_bytes())

    def test_cli_write_is_explicit_and_backed_up(self):
        payload, expected = self.replacement()
        source = self.root / 'edit.md'
        source.write_bytes(payload)
        with patch.object(blocks, 'ROOT', self.root), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            result = blocks.main(['--file', str(self.path), 'replace', 'chapter-07',
                                  '--from-file', str(source), '--expect-sha256', expected, '--write'])
        self.assertEqual(0, result)
        self.assertIn('新的内容。'.encode(), self.path.read_bytes())
        backups = list((self.root / '.local/章节编辑备份').glob('*.md'))
        self.assertEqual(1, len(backups))
        self.assertEqual(self.original, backups[0].read_bytes())

    def test_stale_region_hash_is_rejected_without_write(self):
        payload, expected = self.replacement()
        self.path.write_bytes(self.original.replace('原有内容。'.encode(), '内容已变。'.encode()))
        changed = self.path.read_bytes()
        with self.assertRaisesRegex(blocks.BlockError, 'block changed'):
            blocks.plan_replace(self.path, 'chapter-07', payload, expected)
        self.assertEqual(changed, self.path.read_bytes())

    def test_change_in_another_chapter_after_preview_is_not_overwritten(self):
        payload, expected = self.replacement()
        edit = blocks.plan_replace(self.path, 'chapter-07', payload, expected)
        changed = self.original.replace('前言保留。'.encode(), '前言有新编辑。'.encode())
        self.path.write_bytes(changed)
        with self.assertRaisesRegex(blocks.BlockError, 'source changed'):
            blocks.apply_edit(edit, self.root / 'backups')
        self.assertEqual(changed, self.path.read_bytes())
        self.assertFalse(list(self.root.glob('*.lock')))

    def test_change_during_write_preparation_is_not_overwritten(self):
        payload, expected = self.replacement()
        edit = blocks.plan_replace(self.path, 'chapter-07', payload, expected)
        changed = self.original.replace('前言保留。'.encode(), '外部编辑器的新内容。'.encode())
        with patch.object(blocks.shutil, 'copymode', side_effect=lambda *_: self.path.write_bytes(changed)):
            with self.assertRaisesRegex(blocks.BlockError, 'source changed during'):
                blocks.apply_edit(edit, self.root / 'backups')
        self.assertEqual(changed, self.path.read_bytes())
        self.assertFalse(list(self.root.glob('*.lock')))
        self.assertFalse(list(self.root.glob('.sp-block-*')))

    def test_failed_backup_leaves_source_untouched_and_releases_lock(self):
        payload, expected = self.replacement()
        edit = blocks.plan_replace(self.path, 'chapter-07', payload, expected)
        not_a_directory = self.root / 'not-a-directory'
        not_a_directory.write_bytes(b'keep')
        with self.assertRaises(OSError):
            blocks.apply_edit(edit, not_a_directory)
        self.assertEqual(self.original, self.path.read_bytes())
        self.assertFalse(list(self.root.glob('*.lock')))

    def test_same_body_is_noop(self):
        block = blocks.find_block(self.original, 'chapter-07')
        body = block.body(self.original)
        edit = blocks.plan_replace(self.path, block.id, body, blocks.digest(body))
        self.assertEqual('', edit.diff)
        self.assertIsNone(blocks.apply_edit(edit, self.root / 'backups'))
        self.assertFalse((self.root / 'backups').exists())

    def test_existing_lock_is_not_removed_or_ignored(self):
        payload, expected = self.replacement()
        edit = blocks.plan_replace(self.path, 'chapter-07', payload, expected)
        lock = self.path.with_name(self.path.name + '.sp-block.lock')
        lock.write_bytes(b'other writer')
        with self.assertRaisesRegex(blocks.BlockError, 'holds the lock'):
            blocks.apply_edit(edit, self.root / 'backups')
        self.assertEqual(b'other writer', lock.read_bytes())
        self.assertEqual(self.original, self.path.read_bytes())

    def test_read_to_new_file_is_exact_and_refuses_overwrite(self):
        target = self.root / 'extracted.md'
        args = ['--file', str(self.path), 'read', 'chapter-07', '--out', str(target)]
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertEqual(0, blocks.main(args))
        self.assertEqual(blocks.find_block(self.original, 'chapter-07').body(self.original), target.read_bytes())
        target.write_bytes(b'edited by user')
        with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertEqual(1, blocks.main(args))
        self.assertEqual(b'edited by user', target.read_bytes())

    def test_fenced_marker_examples_are_not_real_boundaries(self):
        example = b'```markdown\n<!-- SP:BEGIN chapter-07 -->\n<!-- SP:END chapter-07 -->\n```\n'
        self.assertEqual(9, len(blocks.parse_blocks(example + book())))
        example = b'   ~~~~\n<!-- SP:END chapter-01 -->\n   ~~~~\n'
        self.assertEqual(9, len(blocks.parse_blocks(example + book())))

    def test_missing_duplicate_nested_crossed_and_malformed_markers_are_rejected(self):
        data = book()
        cases = [
            data.replace(b'<!-- SP:END chapter-07 -->\n', b''),
            data + b'<!-- SP:BEGIN appendix -->\n',
            data.replace(b'<!-- SP:END chapter-01 -->', b'<!-- SP:BEGIN chapter-02 -->'),
            data.replace(b'<!-- SP:END chapter-01 -->', b'<!-- SP:END chapter-02 -->'),
            data.replace(b'SP:BEGIN chapter-01', b'SP:BEGIN  chapter-01'),
            data.replace(b'SP:BEGIN chapter-01', b'SP:BEGIN chapter-99'),
        ]
        for changed in cases:
            with self.subTest(changed=changed[:60]), self.assertRaises(blocks.BlockError):
                blocks.parse_blocks(changed)

    def test_unclosed_code_fence_cannot_hide_end_marker(self):
        changed = book().replace(b'<!-- SP:END chapter-07 -->', b'```\n<!-- SP:END chapter-07 -->')
        with self.assertRaisesRegex(blocks.BlockError, 'unclosed fenced'):
            blocks.parse_blocks(changed)

    def test_wrong_chapter_or_conclusion_inside_region_is_rejected(self):
        for changed in [book().replace('第七章'.encode(), '第五章'.encode()),
                        book().replace(b'<!-- SP:END chapter-08 -->\n', b'').replace(
                            b'<!-- SP:BEGIN appendix -->', b'<!-- SP:END chapter-08 -->\n<!-- SP:BEGIN appendix -->')]:
            with self.subTest(changed=changed[:60]), self.assertRaises(blocks.BlockError):
                blocks.parse_blocks(changed)

    def test_empty_bom_or_unterminated_replacement_is_rejected(self):
        payload, expected = self.replacement()
        for changed in [b'', b'\xef\xbb\xbf' + payload, payload.rstrip(b'\r\n')]:
            with self.subTest(changed=changed[:10]), self.assertRaises(blocks.BlockError):
                blocks.plan_replace(self.path, 'chapter-07', changed, expected)

    def test_missing_legacy_anchor_is_rejected(self):
        self.original = self.original.replace(b'<!-- SP:END chapter-07 -->', b'<a id="legacy-test"></a>\r\n<!-- SP:END chapter-07 -->')
        self.path.write_bytes(self.original)
        payload, expected = self.replacement()
        with self.assertRaisesRegex(blocks.BlockError, 'preserve existing anchor'):
            blocks.plan_replace(self.path, 'chapter-07', payload.replace(b'<a id="legacy-test"></a>\r\n', b''), expected)

    def test_duplicate_or_injected_boundary_cannot_escape_target(self):
        payload, expected = self.replacement()
        for changed in [payload + b'<a id="chapter-1"></a>\n', payload + b'<!-- SP:BEGIN appendix -->\n']:
            with self.subTest(changed=changed[-50:]), self.assertRaises(blocks.BlockError):
                blocks.plan_replace(self.path, 'chapter-07', changed, expected)


if __name__ == '__main__':
    unittest.main()
