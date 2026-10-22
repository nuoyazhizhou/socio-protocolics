"""Export only public working files to a new folder and ZIP, never Git history."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
import zipfile
from pathlib import Path

from check_public import ROOT, public_files, validate


def main() -> int:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:]:
        print('usage: python tools/export_public.py', file=sys.stderr)
        return 2
    result = validate()
    if not result['ok']:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1
    # Read all listed bytes before creating output. Validation rejects links and traversal.
    payload = {name: (ROOT / name).read_bytes() for name in public_files(ROOT)}
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    parent = ROOT / '.local' / 'exports'
    parent.mkdir(parents=True, exist_ok=True)
    destination = parent / ('public-' + stamp)
    destination.mkdir(exist_ok=False)
    hashes = {}
    for name, data in payload.items():
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        hashes[name] = hashlib.sha256(data).hexdigest()
    # The timestamp contains a dot; append extensions instead of replacing its suffix.
    archive = Path(str(destination) + '.zip')
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as out:
        for name, data in payload.items():
            out.writestr(name, data)
    receipt = Path(str(destination) + '.manifest.json')
    metadata = {
        'created_utc': stamp,
        'source': 'current working files, not necessarily committed contents',
        'git_history_included': False,
        'files': hashes,
        'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
        'validation': result,
    }
    receipt.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'directory': str(destination), 'archive': str(archive), 'receipt': str(receipt), 'files': len(payload)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
