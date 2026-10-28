"""Check generated HTML file links and fragments using the configured Pages prefix."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '.local' / 'site-build'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])


def main() -> int:
    configured = re.search(r'^site_url:\s*(\S+)', (ROOT / 'mkdocs.yml').read_text(encoding='utf-8'), re.M)
    if not configured or not (SITE / 'index.html').is_file():
        raise ValueError('build the configured site before checking links')
    canonical = urlsplit(configured[1])
    pages = {}
    for path in SITE.rglob('*.html'):
        page = Page()
        page.feed(path.read_text(encoding='utf-8'))
        pages[path.resolve()] = page
    errors = []
    checked = 0
    for path, page in pages.items():
        for raw in page.links:
            url = urlsplit(raw)
            if raw == '#' or (url.scheme or url.netloc) and url.netloc != canonical.netloc:
                continue
            decoded = unquote(url.path)
            if decoded.startswith('/'):
                if not decoded.startswith(canonical.path):
                    errors.append([str(path.relative_to(SITE)), raw, 'outside project URL'])
                    continue
                target = SITE / decoded[len(canonical.path):]
            else:
                target = path.parent / decoded if decoded else path
            target = target.resolve()
            if target.is_dir():
                target = target / 'index.html'
            checked += 1
            reason = None
            if not target.is_relative_to(SITE.resolve()) or not target.is_file():
                reason = 'missing or outside file'
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                reason = 'missing anchor'
            if reason:
                errors.append([str(path.relative_to(SITE)), raw, reason])
    print(json.dumps({'ok': not errors, 'html_pages': len(pages), 'local_links': checked,
                      'errors': errors, 'scope': 'generated HTML hyperlinks and anchors; not external URLs or browser rendering'},
                     ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
