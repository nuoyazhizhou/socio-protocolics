"""Regression checks for website-only transforms and the public copy boundary."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

import build_site as site


class ReadingSiteTests(unittest.TestCase):
    def test_windows_table_has_no_spurious_blank_lines(self):
        raw = '| 标题 | 内容 |\r\n|---|---|\r\n| 词表 | $|V|$ |\r\n'
        rendered = site.reading_markdown(raw)
        self.assertEqual(len(rendered.splitlines()), 3)
        self.assertNotIn('\r', rendered)
        self.assertIn(r'$\vert V\vert $', rendered)

    def test_code_examples_remain_verbatim(self):
        raw = '```python\n| not_a_table | "$|x|$" |\n```\n'
        self.assertEqual(site.reading_markdown(raw), raw)
        self.assertEqual(site.chapter_links('```\n[x](docs/item.md)\n```'),
                         '```\n[x](docs/item.md)\n```')

    def test_chapter_links_keep_cross_chapter_anchor_and_external_source(self):
        text = '[其他RFC](#sp-rfc-014) [来源](docs/source.md#fact) [外链](https://example.org/a)'
        actual = site.chapter_links(text)
        self.assertIn('../' + site.WHITEPAPER + '#sp-rfc-014', actual)
        self.assertIn('../docs/source.md#fact', actual)
        self.assertIn('(https://example.org/a)', actual)

    def test_private_and_unlisted_files_are_never_copied(self):
        whitepaper = (site.ROOT / site.WHITEPAPER).read_bytes()
        local = site.ROOT / '.local'
        local.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=local, prefix='site-scope-test-') as tmp:
            root = Path(tmp)
            (root / site.WHITEPAPER).write_bytes(whitepaper)
            (root / 'README.md').write_text('# Public\n', encoding='utf-8')
            (root / '.local').mkdir()
            (root / '.local' / 'private.md').write_text('PRIVATE_SENTINEL_731', encoding='utf-8')
            (root / 'unlisted.md').write_text('UNLISTED_SENTINEL_852', encoding='utf-8')
            names = ['README.md', site.WHITEPAPER]
            source = root / '.local' / 'site-source'
            with patch.object(site, 'ROOT', root), patch.object(site, 'SOURCE', source), \
                 patch.object(site, 'OUTPUT', root / '.local' / 'site-build'), \
                 patch.object(site, 'validate', return_value={'ok': True}), \
                 patch.object(site, 'public_files', return_value=names), \
                 patch.object(site.subprocess, 'run', return_value=SimpleNamespace(returncode=0)), \
                 patch.object(site.sys, 'argv', ['build_site.py']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(site.main(), 0)
            content = b''.join(p.read_bytes() for p in source.rglob('*') if p.is_file())
            self.assertNotIn(b'PRIVATE_SENTINEL_731', content)
            self.assertNotIn(b'UNLISTED_SENTINEL_852', content)
            metadata = json.loads((source / 'release-metadata.json').read_text(encoding='utf-8'))
            self.assertEqual(set(metadata['files']), set(names))


if __name__ == '__main__':
    unittest.main()
