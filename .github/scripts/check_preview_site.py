"""Guard preview isolation and internal links without activating draft routes."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

from guide_inventory import ALL_GUIDES
from site_catalog import PAUSED_ENTRY_ROUTES, ORIGIN, UMAMI_SCRIPT_URL


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.cards = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'review-card' in attrs.get('class', '').split():
            self.cards += 1
        if tag in ('a', 'link', 'script'):
            self.urls.append(attrs.get('href', attrs.get('src', '')))


def check_preview_site(out: Path, problems: list[str]) -> None:
    preview = out / 'preview'
    expected = {'index.html', 'reset-your-space.html', 'organizing-ideas.html'}
    expected.update(r.page for r in PAUSED_ENTRY_ROUTES)
    expected.update(r.completion_page for r in PAUSED_ENTRY_ROUTES)
    expected.update(f'guides/{slug}.html' for slug, *_ in ALL_GUIDES)
    actual = {p.relative_to(preview).as_posix() for p in preview.rglob('*.html')}
    if actual != expected:
        problems.append('preview/: draft HTML inventory differs from the retained sources')
    for page in preview.rglob('*.html'):
        text = page.read_text()
        if 'data-mlm-preview="1" name="robots" content="noindex,nofollow"' not in text:
            problems.append(f'{page.relative_to(out)}: missing preview/noindex marker')
        if any(marker in text for marker in ('ml-embedded', 'assets.mailerlite.com', UMAMI_SCRIPT_URL, 'src="/assets/entry.js"')):
            problems.append(f'{page.relative_to(out)}: production signup or tracking wiring in preview')
        links = Links()
        links.feed(text)
        for url in links.urls:
            parsed = urlsplit(url)
            if parsed.scheme in ('mailto', 'tel', 'data') or (parsed.netloc and parsed.netloc != urlsplit(ORIGIN).netloc):
                continue
            path = (out / unquote(parsed.path.lstrip('/'))) if parsed.path.startswith('/') else (page.parent / unquote(parsed.path))
            if path.is_dir():
                path = path / 'index.html'
            if not path.is_file():
                problems.append(f'{page.relative_to(out)}: missing link target {url}')
        if page == preview / 'index.html' and links.cards != 20:
            problems.append('preview/index.html: expected twenty review cards')
    for route in PAUSED_ENTRY_ROUTES:
        path = preview / route.page
        if path.is_file():
            text = path.read_text()
            for marker in (f'data-completion-url="/preview/{route.completion_page}"', 'src="/preview/assets/entry.js"'):
                if marker not in text:
                    problems.append(f'preview/{route.page}: missing isolated task wiring {marker}')
    for page in out.rglob('*.html'):
        if page.is_relative_to(preview):
            continue
        links = Links()
        links.feed(page.read_text())
        if any(urlsplit(url).path.startswith('/preview/') for url in links.urls):
            problems.append(f'{page.relative_to(out)}: preview linked from standard site')
    if '/preview/' in (out / 'sitemap.xml').read_text():
        problems.append('preview/: review pages must stay out of sitemap.xml')
    if 'Disallow: /preview/print/' not in (out / 'robots.txt').read_text():
        problems.append('preview/print/: PDF crawl exclusion missing')
    actual_pdfs = {p.name for p in (preview / 'print').glob('*.pdf')}
    if actual_pdfs != {f'{slug}.pdf' for slug, *_ in ALL_GUIDES}:
        problems.append('preview/print/: saved reference PDF inventory is incomplete')
    root = Path(__file__).resolve().parents[2]
    for slug, *_ in ALL_GUIDES:
        path = preview / 'print' / f'{slug}.pdf'
        if path.is_file() and path.read_bytes() != (root / 'products/guides-pdf' / path.name).read_bytes():
            problems.append(f'preview/print/{slug}.pdf: differs from saved source PDF')
    script = preview / 'assets/entry.js'
    if not script.is_file() or 'function track() {}' not in script.read_text() or 'window.umami' in script.read_text():
        problems.append('preview/assets/entry.js: preview event isolation missing')
