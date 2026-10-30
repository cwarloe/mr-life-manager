"""Build an unlisted review area from retained sources, without activating them."""
from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from guide_inventory import ALL_GUIDES
from site_catalog import PAUSED_ENTRY_ROUTES

PREFIX = "/preview/"
VARIANTS = (
    ("junk-drawers", "Every drawer has become a junk drawer."),
    ("cant-find-things", "I put things away. Then I can't find them."),
    ("clear-the-table", "I have to clear the table before we can eat."),
)

CSS = """
.preview-banner{font:14px/1.5 var(--sans,system-ui);padding:.65rem 1.1rem;
 background:var(--blue-soft,#EBF1F7);color:var(--ink,#14181F);border-bottom:1px solid var(--rule,#ddd)}
.preview-banner a{color:var(--blue,#1A446C);font-weight:700}
body.doing .preview-banner{display:none}
.review{max-width:56rem;margin:auto;padding:2.5rem 1.2rem 4rem}
.review h1{font-size:clamp(2rem,6vw,3rem);line-height:1.1;margin:0 0 1rem}
.review h2{font-size:1.35rem;margin:2.5rem 0 1rem}
.review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,20rem),1fr));gap:.8rem}
.review-card{display:block;padding:1rem 1.15rem;border:1px solid var(--rule);border-radius:5px;
 background:var(--surface);color:var(--ink);text-decoration:none}
.review-card:hover{border-color:var(--blue)}
.review-card strong{display:block;line-height:1.35}
.review-card span{display:block;font-size:.85rem;color:var(--slate);margin-top:.4rem}
.review a:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.review-copy{max-width:44rem}.review-copy p,.review-copy li{line-height:1.65}
.review-copy label{display:flex;align-items:flex-start;gap:.7rem}
.review-copy input{flex:none;margin-top:.4rem;width:1rem;height:1rem}
.review-copy .checks{list-style:none;padding:0}.review-copy .checks li{margin:1rem 0}
.review-copy table{width:100%;border-collapse:collapse;margin:1.5rem 0;font-size:.9rem}
.review-copy td,.review-copy th{border:1px solid var(--rule);padding:.6rem;min-width:2rem;height:2.5rem;text-align:left}
.preview-pdf{max-width:50rem;margin:1rem auto;padding:0 1.2rem;font:15px/1.5 var(--sans)}
@media print{.preview-banner,.preview-pdf{display:none!important}.review{padding:0}
 .review-copy h2{break-after:avoid}.review-copy li{break-inside:avoid}}
"""


def shell(title: str, body: str) -> str:
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f"<title>{html.escape(title)} · Mr. Life Manager</title>"
            '<link rel="stylesheet" href="/assets/site.css">'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&amp;family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;display=swap">'
            f"</head><body>{body}</body></html>")


def remove_element(text: str, class_name: str) -> str:
    """Remove a div and its nested divs without leaving signup fragments."""
    match = re.search(r'<div\b[^>]*class="' + re.escape(class_name) + r'"[^>]*>', text)
    if not match:
        return text
    depth = 1
    for tag in re.finditer(r'</?div\b[^>]*>', text[match.end():], re.I):
        depth += -1 if tag.group().startswith("</") else 1
        if depth == 0:
            return text[:match.start()] + text[match.end() + tag.end():]
    raise ValueError(f"Unclosed {class_name} div in preview source")


def markdown_checklist(text: str) -> str:
    """Render this checklist's headings, paragraphs, checkboxes and blank tables.

    Escape source HTML; this deliberately supports only the retained document's
    small Markdown vocabulary rather than adding a build-time package.
    """
    def inline(value: str) -> str:
        value = html.escape(value)
        value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
        return re.sub(r'\[([^]]+)\]\(([^)]+)\)',
                      lambda m: '<a href="https://github.com/cwarloe/mr-life-manager/blob/main/products/checklists/reset-your-space/'
                      + m[2] + '">' + m[1] + '</a>', value)

    lines = text.splitlines()
    rendered, paragraph = [], []
    def flush():
        if paragraph:
            rendered.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|'):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [v.strip() for v in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    tag = 'th' if not rows else 'td'
                    rows.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
                i += 1
            rendered.append('<div style="overflow-x:auto"><table>' + ''.join(rows) + '</table></div>')
            continue
        if line.startswith('- [ ] '):
            flush()
            items = []
            while i < len(lines) and lines[i].startswith('- [ ] '):
                items.append('<li><label><input type="checkbox"><span>' + inline(lines[i][6:]) + '</span></label></li>')
                i += 1
            rendered.append('<ul class="checks">' + ''.join(items) + '</ul>')
            continue
        heading = re.match(r'^(#{1,3}) (.*)$', line)
        if heading:
            flush()
            n = len(heading[1])
            rendered.append(f'<h{n}>{inline(heading[2])}</h{n}>')
        elif line == '---':
            flush()
            rendered.append('<hr>')
        elif not line:
            flush()
        else:
            paragraph.append(line)
        i += 1
    flush()
    return ''.join(rendered)


def build_preview(root: Path, out: Path) -> None:
    target = out / 'preview'
    (target / 'guides').mkdir(parents=True)
    (target / 'assets').mkdir()
    (target / 'print').mkdir()
    (target / 'assets/preview.css').write_text(CSS)

    # Same execution UI, with signup helpers and production events omitted.
    js = (root / 'products/landing/assets/entry.js').read_text()
    js = js[:js.index('  // Event counts')] + '  function track() {}\n' + js[js.index('  // Doing mode:'):]
    (target / 'assets/entry.js').write_text(js)

    replacements = {f'/{r.page}': PREFIX + r.page for r in PAUSED_ENTRY_ROUTES}
    replacements.update({f'/{r.completion_page}': PREFIX + r.completion_page for r in PAUSED_ENTRY_ROUTES})
    replacements['/organizing-ideas.html'] = PREFIX + 'organizing-ideas.html'
    replacements.update({f'/guides/{slug}.html': PREFIX + f'guides/{slug}.html' for slug, *_ in ALL_GUIDES})
    replacements.update({f'/print/{slug}.pdf': PREFIX + f'print/{slug}.pdf' for slug, *_ in ALL_GUIDES})

    def write(relative: str, text: str) -> None:
        text = remove_element(text, 'signup')
        text = re.sub(r'<script\b[^>]*>.*?</script>',
                      lambda m: '' if re.search(r'mailerlite|\bml\(', m[0], re.I) else m[0], text, flags=re.S)
        text = text.replace('src="/assets/entry.js"', 'src="/preview/assets/entry.js"')
        for old, new in replacements.items():
            text = text.replace('"' + old, '"' + new).replace("'" + old, "'" + new)
        text = re.sub(r'<meta\b[^>]*name=["\']robots["\'][^>]*>\s*', '', text, flags=re.I)
        text = text.replace('</head>', '<meta data-mlm-preview="1" name="robots" content="noindex,nofollow">'
                            '<link rel="stylesheet" href="/preview/assets/preview.css"></head>', 1)
        banner = '<aside class="preview-banner">Draft preview · <a href="/preview/">All previews</a> · Not part of the main checklist selection</aside>'
        text = text.replace('<body>', '<body>' + banner, 1)
        (target / relative).write_text(text)

    for route in PAUSED_ENTRY_ROUTES:
        write(route.page, (root / 'products/landing' / route.page).read_text())
        completion = shell('Completion preview', '<main class="review review-copy"><h1>Checklist completion preview</h1>'
                           '<p>This is the end of this draft’s flow. No signup is needed.</p>'
                           f'<p><a href="/preview/{route.page}">Return to this checklist</a> · '
                           '<a href="/preview/">Choose another preview</a></p></main>')
        write(route.completion_page, completion)

    write('organizing-ideas.html', (root / 'products/landing/organizing-ideas.html').read_text())
    write('design.html', (root / 'products/landing/templates/design-options.html').read_text())
    reset = markdown_checklist((root / 'products/checklists/reset-your-space/checklist.md').read_text())
    write('reset-your-space.html', shell('Reset Your Space', '<main class="review review-copy">' + reset + '</main>'))

    for slug, src, title, _ in ALL_GUIDES:
        text = (root / src).read_text().replace('href="../../print/printable.css"', 'href="/print/printable.css"')
        pdf = f'/preview/print/{slug}.pdf'
        text = text.replace('</body>', f'<p class="preview-pdf"><a href="{pdf}" rel="nofollow">Open the saved PDF</a></p></body>')
        write(f'guides/{slug}.html', text)
        shutil.copy2(root / 'products/guides-pdf' / f'{slug}.pdf', target / 'print' / f'{slug}.pdf')

    def card(url: str, title: str, label: str) -> str:
        return f'<a class="review-card" href="{url}"><strong>{html.escape(title)}</strong><span>{html.escape(label)}</span></a>'

    entries = ''.join(card(PREFIX + r.page, r.door_title, 'Six-step draft · start, schedule or print') for r in PAUSED_ENTRY_ROUTES)
    organizing = card(PREFIX + 'reset-your-space.html', 'Reset Your Space', 'Full twelve-step method')
    organizing += ''.join(card(PREFIX + 'organizing-ideas.html#' + slug, title, 'Longer organizing checklist · eight steps') for slug, title in VARIANTS)
    organizing += card(PREFIX + 'organizing-ideas.html', 'Compare the three organizing versions', 'All three on one page · printable')
    guides = ''.join(card(PREFIX + f'guides/{slug}.html', title, 'Reference or worksheet · includes saved PDF') for slug, _, title, _ in ALL_GUIDES)
    content = ('<main class="review"><h1>Draft checklist previews</h1>'
               '<p>The revised drafts, gathered here for review. They remain outside the main site’s five entry points. '
               'Completion times and usefulness still need testing with readers.</p>'
               '<h2>Design options</h2><div class="review-grid">' + card(PREFIX + 'design.html', 'Themes, layouts and colors', 'Home and a checklist page in three looks') + '</div>'
               '<h2>Short task pages</h2><div class="review-grid">' + entries + '</div>'
               '<h2>Longer organizing resets</h2><div class="review-grid">' + organizing + '</div>'
               '<h2>Reference guides and worksheets</h2><div class="review-grid">' + guides + '</div></main>')
    write('index.html', shell('Draft checklist previews', content))
