"""Check the public index and local Markdown links; no claim of fact-checking."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PARTS = {'.git', '.local', 'node_modules', '__pycache__'}
MARKERS = re.compile(r'§/?(?:NOTE|CUT|REF)§')
ABSOLUTE_LOCAL = re.compile(r'(?i)\b[A-Z]:[\\/]|file://|/(?:Users|home)/')
LINK = re.compile(r'\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\)')


def public_files(root: Path) -> list[str]:
    config = json.loads((root / 'public-files.json').read_text(encoding='utf-8'))
    if config.get('schema_version') != 1:
        raise ValueError('unsupported public manifest schema')
    files = config.get('files')
    if not isinstance(files, list) or not files or any(not isinstance(s, str) for s in files):
        raise ValueError('manifest files must be a nonempty list of strings')
    if len(files) != len(set(files)):
        raise ValueError('duplicate public file')
    for name in files:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name or str(path) != name:
            raise ValueError(f'unsafe public path: {name}')
        if any(p in PRIVATE_PARTS or p.startswith(('评审', '审计')) for p in path.parts):
            raise ValueError(f'private path in public manifest: {name}')
        if any(s in name for s in ('内部未删节', '内部删节', '工作稿')):
            raise ValueError(f'private file in public manifest: {name}')
        if path.suffix.lower() in {'.docx', '.zip', '.tmp', '.log', '.pyc'}:
            raise ValueError(f'non-public artifact type: {name}')
        resolved = (root / name).resolve()
        if not resolved.is_relative_to(root.resolve()) or resolved != root.resolve().joinpath(*path.parts):
            raise ValueError(f'public path uses a link or escapes the root: {name}')
        if not resolved.is_file():
            raise ValueError(f'missing public file: {name}')
    return files


def validate(root: Path = ROOT, check_index: bool = True) -> dict:
    root = root.resolve()
    errors: list[str] = []
    try:
        files = public_files(root)
    except (ValueError, OSError) as exc:
        return {'ok': False, 'errors': [str(exc)]}
    allowed = set(files)
    tracked: list[str] = []
    if check_index:
        top = subprocess.run(['git', '-C', str(root), 'rev-parse', '--show-toplevel'], capture_output=True)
        if top.returncode or Path(top.stdout.decode('utf-8').strip()).resolve() != root:
            errors.append('public root is not the Git root; use --snapshot only for a history-free export')
        else:
            result = subprocess.run(['git', '-C', str(root), 'ls-files', '-z'], capture_output=True)
            if result.returncode:
                errors.append('cannot inspect Git index')
            else:
                tracked = result.stdout.decode('utf-8').split('\0')[:-1]
                extras = sorted(set(tracked) - allowed)
                if extras:
                    errors.append(f'{len(extras)} tracked paths are not public: ' + ', '.join(extras[:8]))
    links = 0
    for name in files:
        if not name.endswith('.md'):
            continue
        text = (root / name).read_text(encoding='utf-8')
        if MARKERS.search(text):
            errors.append(f'writing markers remain: {name}')
        if ABSOLUTE_LOCAL.search(text):
            errors.append(f'local absolute path remains: {name}')
        # Fenced examples are not actual Markdown links.
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        for match in LINK.finditer(prose):
            raw = match.group(1).strip('<>')
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            links += 1
            target = ((root / name).parent / unquote(url.path)).resolve() if url.path else root / name
            if not target.is_relative_to(root):
                errors.append(f'link escapes root: {name} -> {raw}')
                continue
            relative = target.relative_to(root).as_posix()
            if relative not in allowed:
                errors.append(f'link is outside public file list: {name} -> {raw}')
            elif not target.is_file():
                errors.append(f'broken local file link: {name} -> {raw}')
    return {
        'ok': not errors,
        'public_files': len(files),
        'tracked_files': len(tracked) if check_index else None,
        'local_file_links': links,
        'index_checked': check_index,
        'scope': 'public paths, file existence, writing markers, local paths and linked files; not anchors, remote URLs or semantic validity',
        'errors': errors,
    }


def main() -> int:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:] not in ([], ['--snapshot']):
        print('usage: python tools/check_public.py [--snapshot]', file=sys.stderr)
        return 2
    result = validate(check_index='--snapshot' not in sys.argv)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
