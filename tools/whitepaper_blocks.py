"""Read bounded whitepaper regions and preview hash-checked replacements (stdlib only)."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / '社会系统协议学白皮书.md'
BLOCK_IDS = tuple(f'chapter-{i:02}' for i in range(1, 9)) + ('appendix',)
CHAPTER_NAMES = dict(zip(BLOCK_IDS, [f'第{x}章' for x in '一二三四五六七八'] + ['附录']))
MARKER = re.compile(rb'<!-- SP:(BEGIN|END) ([a-z][a-z0-9-]*) -->')
FENCE = re.compile(rb' {0,3}(`{3,}|~{3,})(.*)')
ANCHOR = re.compile(rb'<a\s+id="([^"]+)"\s*></a>')


class BlockError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class Block:
    id: str
    start: int
    stop: int
    begin_line: int
    end_line: int
    title: str

    def body(self, data: bytes) -> bytes:
        return data[self.start:self.stop]

    def metadata(self, data: bytes) -> dict:
        body = self.body(data)
        return dict(id=self.id, title=self.title, begin_line=self.begin_line,
                    end_line=self.end_line, lines=len(body.splitlines()),
                    bytes=len(body), sha256=digest(body))


def parse_blocks(data: bytes) -> list[Block]:
    """Ignore fenced examples; require nine ordered, non-overlapping real blocks."""
    data.decode('utf-8')
    blocks = []
    active = None
    fence = None
    headings = []
    offset = 0
    for number, line in enumerate(data.splitlines(keepends=True), 1):
        bare = line.rstrip(b'\r\n')
        fence_match = FENCE.fullmatch(bare)
        if fence is not None:
            if fence_match and fence_match[1][:1] == fence[:1] and len(fence_match[1]) >= len(fence) and not fence_match[2].strip():
                fence = None
        elif fence_match:
            fence = fence_match[1]
        else:
            if bare.startswith(b'## '):
                headings.append((offset, bare.decode('utf-8')[3:]))
            marker = MARKER.fullmatch(bare)
            if not marker and b'<!-- SP:' in bare:
                raise BlockError(f'malformed marker at line {number}')
            if marker:
                kind, block_id = marker[1].decode(), marker[2].decode()
                if block_id not in BLOCK_IDS:
                    raise BlockError(f'unknown block ID: {block_id}')
                if kind == 'BEGIN':
                    if active is not None:
                        raise BlockError(f'nested block at line {number}')
                    if any(b.id == block_id for b in blocks):
                        raise BlockError(f'duplicate block: {block_id}')
                    active = (block_id, offset + len(line), number)
                else:
                    if active is None or active[0] != block_id:
                        raise BlockError(f'unmatched END at line {number}: {block_id}')
                    name, start, begin_line = active
                    titles = [title for position, title in headings if start <= position < offset]
                    if len(titles) != 1 or not titles[0].startswith(CHAPTER_NAMES[name] + '：'):
                        raise BlockError(f'{name}: expected exactly its own level-2 heading')
                    blocks.append(Block(name, start, offset, begin_line, number, titles[0]))
                    active = None
        offset += len(line)
    if fence is not None:
        raise BlockError('unclosed fenced code block')
    if active is not None:
        raise BlockError(f'missing END for {active[0]}')
    if tuple(b.id for b in blocks) != BLOCK_IDS:
        raise BlockError('expected chapter-01 through chapter-08 and appendix, once and in order')
    for block in blocks:
        anchor = (f'chapter-{int(block.id[-2:])}' if block.id != 'appendix' else 'rfc-directory').encode()
        if ANCHOR.findall(block.body(data)).count(anchor) != 1:
            raise BlockError(f'{block.id}: its canonical anchor must remain inside the block')
    for position, title in headings:
        if any(title.startswith(name + '：') for name in CHAPTER_NAMES.values()):
            if sum(b.start <= position < b.stop for b in blocks) != 1:
                raise BlockError(f'chapter/appendix heading outside its block: {title}')
    return blocks


def check_document_blocks(data: bytes) -> list[str]:
    try:
        parse_blocks(data)
        return []
    except (BlockError, UnicodeError) as exc:
        return ['Whitepaper block boundaries: ' + str(exc)]


def find_block(data: bytes, block_id: str) -> Block:
    for block in parse_blocks(data):
        if block.id == block_id:
            return block
    raise BlockError(f'unknown block ID: {block_id}')


@dataclass(frozen=True)
class Edit:
    path: Path
    original: bytes
    proposed: bytes
    diff: str


def plan_replace(path: Path, block_id: str, replacement: bytes, expected_sha256: str) -> Edit:
    if path.is_symlink():
        raise BlockError('refusing to replace a symbolic-link source')
    path = path.resolve()
    original = path.read_bytes()
    block = find_block(original, block_id)
    if not re.fullmatch(r'[a-fA-F0-9]{64}', expected_sha256):
        raise BlockError('expected SHA-256 must contain 64 hexadecimal characters')
    if digest(block.body(original)) != expected_sha256.lower():
        raise BlockError('block changed: read it again and review the new hash')
    replacement.decode('utf-8')
    if not replacement.strip() or replacement.startswith(b'\xef\xbb\xbf') or not replacement.endswith(b'\n'):
        raise BlockError('replacement must be nonempty UTF-8 without BOM, ending with a newline')
    proposed = original[:block.start] + replacement + original[block.stop:]
    parse_blocks(proposed)
    before, after = Counter(ANCHOR.findall(original)), Counter(ANCHOR.findall(proposed))
    if any(after[key] != count for key, count in before.items()) or any(count != 1 for count in after.values()):
        raise BlockError('replacement must preserve existing anchor IDs and must not duplicate anchors')
    diff = ''.join(difflib.unified_diff(
        original.decode('utf-8').splitlines(keepends=True),
        proposed.decode('utf-8').splitlines(keepends=True),
        fromfile=path.name + ' (before)', tofile=path.name + ' (proposed)'))
    return Edit(path, original, proposed, diff)


def apply_edit(edit: Edit, backup_dir: Path | None = None) -> Path | None:
    """Cooperating writers use a lock; also recheck the full source before replace."""
    if edit.original == edit.proposed:
        return None
    lock = edit.path.with_name(edit.path.name + '.sp-block.lock')
    try:
        handle = lock.open('xb')
    except FileExistsError as exc:
        raise BlockError('another block edit holds the lock; inspect it before retrying') from exc
    temporary = None
    try:
        with handle:
            handle.write(str(os.getpid()).encode())
        if edit.path.is_symlink() or edit.path.read_bytes() != edit.original:
            raise BlockError('source changed after preview; no replacement written')
        directory = backup_dir if backup_dir is not None else ROOT / '.local/章节编辑备份'
        directory.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
        backup = directory / (stamp + '_' + edit.path.name)
        with backup.open('xb') as stream:
            stream.write(edit.original)
        with tempfile.NamedTemporaryFile(dir=edit.path.parent, prefix='.sp-block-', suffix='.tmp', delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(edit.proposed)
            stream.flush()
            os.fsync(stream.fileno())
        shutil.copymode(edit.path, temporary)
        if edit.path.is_symlink() or edit.path.read_bytes() != edit.original:
            raise BlockError('source changed during write preparation; no replacement written')
        os.replace(temporary, edit.path)
        temporary = None
        return backup
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', type=Path, default=DEFAULT_FILE, help='UTF-8 source; relative paths resolve against repository root')
    commands = parser.add_subparsers(dest='command', required=True)
    listing = commands.add_parser('list', help='list block IDs, titles, sizes and body hashes')
    listing.add_argument('--json', action='store_true')
    reading = commands.add_parser('read', help='write only the selected body to stdout or a new file')
    reading.add_argument('id', choices=BLOCK_IDS)
    reading.add_argument('--out', type=Path, help='new file only; exact body bytes, no markers')
    replacing = commands.add_parser('replace', help='preview by default; --write explicitly applies it')
    replacing.add_argument('id', choices=BLOCK_IDS)
    replacing.add_argument('--from-file', type=Path, required=True)
    replacing.add_argument('--expect-sha256', required=True)
    replacing.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    try:
        path = resolve_path(args.file)
        if args.command == 'replace':
            edit = plan_replace(path, args.id, resolve_path(args.from_file).read_bytes(), args.expect_sha256)
            sys.stdout.write(edit.diff or 'No changes.\n')
            sys.stdout.flush()
            if args.write:
                backup = apply_edit(edit)
                print(json.dumps({'written': backup is not None, 'backup': str(backup) if backup else None}, ensure_ascii=False), file=sys.stderr)
            else:
                print('PREVIEW ONLY; source unchanged. Add --write after reviewing the diff.', file=sys.stderr)
        else:
            data = path.read_bytes()
            blocks = parse_blocks(data)
            if args.command == 'list':
                if args.json:
                    print(json.dumps({'document_sha256': digest(data), 'blocks': [b.metadata(data) for b in blocks]}, ensure_ascii=False, indent=2))
                else:
                    for block in blocks:
                        meta = block.metadata(data)
                        print(f'{block.id}\t{meta["lines"]} lines\t{meta["bytes"]} bytes\t{meta["sha256"]}\t{block.title}')
            else:
                block = next(b for b in blocks if b.id == args.id)
                body = block.body(data)
                if args.out:
                    output = resolve_path(args.out)
                    output.parent.mkdir(parents=True, exist_ok=True)
                    with output.open('xb') as stream:
                        stream.write(body)
                    print(json.dumps(block.metadata(data), ensure_ascii=False))
                else:
                    sys.stdout.buffer.write(body)
                    print(f'{block.id} SHA256={digest(body)}', file=sys.stderr)
    except (BlockError, OSError, UnicodeError) as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    raise SystemExit(main())
