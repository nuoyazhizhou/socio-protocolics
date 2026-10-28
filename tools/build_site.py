"""Build the reading site from the explicit public manifest, never the workspace tree."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit

from check_public import ROOT, LINK, public_files, validate
from whitepaper_blocks import parse_blocks

SOURCE = ROOT / '.local' / 'site-source'
OUTPUT = ROOT / '.local' / 'site-build'
RELEASE = 'v11.2-r20261028'
WHITEPAPER = '社会系统协议学白皮书.md'


def reading_markdown(text: str) -> str:
    """Protect table math delimiters in derived HTML input; source files stay unchanged."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('../.github/workflows/pages.yml',
                        'https://github.com/nuoyazhizhou/socio-protocolics/blob/codex/public-release/.github/workflows/pages.yml')
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
        if fence is None and line.lstrip().startswith('|'):
            line = re.sub(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$',
                          lambda m: '$' + re.sub(r'(?<!\\)\|', r'\\vert ', m[1]) + '$', line)
        lines.append(line)
    return ''.join(lines)


def chapter_links(text: str) -> str:
    """Chapter views live one level deeper; cross-section links retain the full SSOT target."""
    def replace(match):
        original = match[1]
        raw = original.strip('<>')
        url = urlsplit(raw)
        if url.scheme or url.netloc or raw.startswith('/'):
            return match[0]
        target = '../' + (raw if url.path else WHITEPAPER + raw)
        if original.startswith('<'):
            target = '<' + target + '>'
        return match[0].replace(original, target, 1)
    # Code examples are not links.
    chunks = re.split(r'(```.*?```|~~~.*?~~~)', text, flags=re.S)
    return ''.join(part if i % 2 else LINK.sub(replace, part) for i, part in enumerate(chunks))


def reset_source() -> None:
    expected = ROOT.resolve() / '.local' / 'site-source'
    if SOURCE.resolve() != expected or SOURCE.is_symlink():
        raise ValueError('refusing to replace a source directory outside the named local build path')
    if SOURCE.exists():
        shutil.rmtree(SOURCE)
    SOURCE.mkdir(parents=True)
    if OUTPUT.resolve() != ROOT.resolve() / '.local' / 'site-build' or OUTPUT.is_symlink():
        raise ValueError('unsafe site output path')


def main() -> int:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:]:
        print('usage: python tools/build_site.py', file=sys.stderr)
        return 2
    result = validate()
    if not result['ok']:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    names = public_files(ROOT)
    # Read every permitted byte first; no folder recursion or private material copy.
    payload = {name: (ROOT / name).read_bytes() for name in names}
    reset_source()
    for name, data in payload.items():
        if name.startswith('.') or name in ('public-files.json', 'mkdocs.yml'):
            continue
        path = SOURCE / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if name.endswith('.md'):
            path.write_text(reading_markdown(data.decode('utf-8')), encoding='utf-8')
        else:
            path.write_bytes(data)
    full = payload[WHITEPAPER]
    for block in parse_blocks(full):
        path = SOURCE / 'chapters' / (block.id + '.md')
        path.parent.mkdir(parents=True, exist_ok=True)
        body = chapter_links(block.body(full).decode('utf-8'))
        note = '> 本页由权威正文自动生成，仅供分章阅读；修订请修改[唯一正文](../' + WHITEPAPER + ')。\n\n'
        body = re.sub(r'^## (.+)$', lambda match: '# ' + match[1] + '\n\n' + note,
                      body, count=1, flags=re.M)
        path.write_text(reading_markdown(body), encoding='utf-8')
    metadata = {'release': RELEASE, 'source': 'public-files.json',
                'files': {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}}
    (SOURCE / 'release-metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    completed = subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict', '-f', str(ROOT / 'mkdocs.yml')], cwd=ROOT)
    if completed.returncode:
        return completed.returncode
    print(json.dumps({'release': RELEASE, 'public_files': len(payload), 'chapter_views': 9,
                      'site_directory': str(OUTPUT)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
