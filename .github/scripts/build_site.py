#!/usr/bin/env python3
"""Assemble the public site into _site/ for GitHub Pages."""
from __future__ import annotations
import re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "products" / "landing"
OUT = ROOT / "_site"

GUIDES = [
    ("first-apartment-checklist",
     "products/checklists/first-apartment/first-apartment-checklist.html",
     "The First Apartment Checklist",
     "Everything to do, buy, and find out — in the order you'll need it."),
    ("how-often-should-i",
     "products/checklists/how-often/how-often-should-i.html",
     "How Often Should I…?",
     "Sheets, filters, towels, the dryer vent. Every cadence in one place."),
    ("cleaning-supply-starter-list",
     "products/checklists/cleaning-supplies/cleaning-supply-starter-list.html",
     "Cleaning Supply Starter List",
     "The nine products that do the work — and the ones you can skip."),
    ("what-is-this-room-for",
     "products/checklists/room-for/what-is-this-room-for.html",
     "What Is This Room For?",
     "One room, twenty minutes, three things to do about it."),
    ("the-light-is-the-problem",
     "products/checklists/light/the-light-is-the-problem.html",
     "The Light Is the Problem",
     "Why a room feels wrong when nothing in it is dirty."),
    ("laundry-solved",
     "products/checklists/laundry/laundry-solved.html",
     "Laundry, Solved",
     "Sorting, settings, stains, and the step everyone actually skips."),
    ("ten-meals",
     "products/checklists/ten-meals/ten-meals.html",
     "Ten Meals and a Stocked Kitchen",
     "Enough to stop deciding what's for dinner every single night."),
    ("household-agreement",
     "products/worksheets/household-agreement/household-agreement.html",
     "The Household Agreement",
     "Decide it once, together, before it's a problem."),
]

PDF_TITLES = {
    "cleaning-supply-starter-list.pdf": "Cleaning Supply Starter List",
    "first-apartment-checklist.pdf": "The First Apartment Checklist",
    "household-agreement.pdf": "The Household Agreement",
    "how-often-should-i.pdf": "How Often Should I…?",
    "laundry-solved.pdf": "Laundry, Solved",
    "ten-meals.pdf": "Ten Meals and a Stocked Kitchen",
    "the-light-is-the-problem.pdf": "The Light Is the Problem",
    "the-week.pdf": "The Week",
    "what-is-this-room-for.pdf": "What Is This Room For?",
}

# Copy corrections applied at build so the live guides stay accurate even if
# the large HTML sources have not been rewritten in the same commit.
GUIDE_COPY_FIXES = [
    (
        "It's cheap — a few dollars a month. Get it before you move in.",
        "Usually around fifteen dollars a month. Cheap compared with replacing your stuff. Get it before you move in.",
    ),
    (
        "That covers dishes, counters, most surfaces, glass, scrubbing, and\n    descaling.",
        "That covers dishes, counters, glass, scrubbing, and\n    descaling. Not on stone counters — marble, granite, some quartz. If it looks like stone, use dish soap and water.",
    ),
]


def tokens_from(path: Path) -> str:
    css = path.read_text()
    m = re.search(r"(:root\{.*?)\*\{box-sizing", css, re.S)
    if not m:
        sys.exit(f"could not lift design tokens from {path}")
    return m.group(1).rstrip()


def page(title, heading, sub, extra_css, body):
    return (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<title>{title}</title>"
        "<link rel='preconnect' href='https://fonts.googleapis.com'>"
        "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
        "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap'>"
        "<style>__TOKENS__*{box-sizing:border-box}"
        "body{background:var(--paper);color:var(--ink);font-family:var(--sans);"
        "font-size:16px;line-height:1.55;margin:0}"
        ".wrap{max-width:54rem;margin:0 auto;padding:0 1.5rem}"
        ".bar{border-bottom:1px solid var(--rule)}"
        ".bar .wrap{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem}"
        ".brand{font-weight:700;font-size:.95rem;text-decoration:none;color:inherit}"
        ".brand span{color:var(--blue)}"
        ".bar a.cta{font-size:.85rem;color:var(--blue);text-decoration:none;font-weight:600}"
        "header.hero{padding:3rem 0 1.5rem;border-bottom:3px solid var(--ink)}"
        "h1{font-size:clamp(1.8rem,5vw,2.8rem);font-weight:800;letter-spacing:-.03em;margin:0}"
        ".sub{font-family:var(--serif);color:var(--slate);margin:1rem 0 0;max-width:50ch}"
        "footer{padding:2rem 0 3rem;font-size:.82rem;color:var(--slate)}"
        f"{extra_css}</style></head><body>"
        "<div class='bar'><div class='wrap'>"
        "<a class='brand' href='/'>Mr.&nbsp;<span>Life Manager</span></a>"
        f"{body['nav']}</div></div>"
        "<header class='hero'><div class='wrap'>"
        f"<h1>{heading}</h1><p class='sub'>{sub}</p></div></header>"
        f"{body['main']}"
        "<footer><div class='wrap'><b>Mr. Life Manager</b> — "
        "<a href='mailto:hello@mrlifemanager.com'>hello@mrlifemanager.com</a>"
        " · <a href='/privacy.html'>Privacy</a></div></footer>"
        "</body></html>"
    )


CTA = """
<div class=\"mlm-cta\">
  <p class=\"mlm-cta-body\">Made by <a href=\"/\">Mr. Life Manager</a> — the practical
  systems of running a life, written down. Free to use, copy, and teach from.</p>
</div>
<style>
.mlm-cta{max-width:50rem;margin:0 auto;padding:1.6rem 1.5rem 3rem;border-top:2px solid var(--rule)}
.mlm-cta-body{font-family:var(--serif);font-size:.95rem;line-height:1.55;color:var(--slate);margin:0}
@media print{.mlm-cta{display:none}}
</style>
"""


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "guides").mkdir(parents=True)
    for item in LANDING.iterdir():
        if item.is_dir() or item.name == "SETUP.md":
            continue
        shutil.copy2(item, OUT / item.name)
    tokens = tokens_from(ROOT / GUIDES[0][1])
    cards = []
    for slug, src, title, blurb in GUIDES:
        html = (ROOT / src).read_text()
        if "</body>" not in html:
            sys.exit(f"{src}: no </body>")
        for old, new in GUIDE_COPY_FIXES:
            html = html.replace(old, new)
        html = html.replace("</body>", CTA + "</body>")
        (OUT / "guides" / f"{slug}.html").write_text(html)
        cards.append(
            f"<a class='card' href='/guides/{slug}.html'><h2>{title}</h2>"
            f"<p>{blurb}</p><span class='go'>Read it →</span></a>"
        )
    extra = (
        ".list{display:grid;gap:1rem;margin:2rem 0 3rem}"
        "a.card{border:2px solid var(--rule-strong);border-radius:3px;padding:1.3rem 1.5rem;"
        "background:var(--surface);text-decoration:none;color:inherit;display:grid;gap:.4rem}"
        "a.card:hover{border-color:var(--blue)}"
        "a.card h2{font-size:1.2rem;font-weight:700;margin:0}"
        "a.card p{font-family:var(--serif);font-size:.97rem;color:var(--slate);margin:0}"
        "a.card .go{font-size:.83rem;font-weight:600;color:var(--blue)}"
        ".foot-cta{border-top:3px solid var(--ink);background:var(--surface);padding:2.5rem 0 3rem}"
        ".foot-cta a{display:inline-block;font-weight:600;padding:.8rem 1.4rem;margin:0 .5rem .5rem 0;"
        "border:2px solid var(--ink);border-radius:3px;background:var(--ink);color:var(--paper);text-decoration:none}"
        ".foot-cta a.ghost{background:transparent;color:var(--ink)}"
    )
    guides_index = page(
        "All Guides — Mr. Life Manager",
        "All the guides.",
        "Read them here, print them, or forward them.",
        extra,
        {
            "nav": "<a class='cta' href='/print/'>Printables →</a>",
            "main": (
                "<main class='wrap'><div class='list'>"
                + "".join(cards)
                + "</div></main>"
                "<section class='foot-cta'><div class='wrap'>"
                "<p>Every guide also exists as a PDF.</p>"
                "<a href='/print/'>See the printables</a>"
                "<a class='ghost' href='/'>What's going on right now</a>"
                "</div></section>"
            ),
        },
    ).replace("__TOKENS__", tokens)
    (OUT / "guides" / "index.html").write_text(guides_index)
    pdf_src = ROOT / "products" / "guides-pdf"
    pdfs = sorted(pdf_src.glob("*.pdf"))
    if not pdfs:
        sys.exit("no printables found in products/guides-pdf/")
    (OUT / "print").mkdir(parents=True, exist_ok=True)
    rows = []
    for pdf in pdfs:
        shutil.copy2(pdf, OUT / "print" / pdf.name)
        label = PDF_TITLES.get(pdf.name, pdf.stem.replace("-", " ").title())
        rows.append(f"<li><a class='file' href='/print/{pdf.name}'>{label}<span>PDF</span></a></li>")
    extra_p = (
        "ul{list-style:none;padding:0;margin:1.5rem 0 3rem}"
        "li{border-top:1px solid var(--rule)}"
        "a.file{display:flex;justify-content:space-between;padding:1rem 0;"
        "text-decoration:none;color:inherit;font-weight:600}"
        "a.file:hover{color:var(--blue)}"
        "a.file span{font-weight:500;color:var(--slate);font-size:.85rem}"
    )
    print_index = page(
        "Printables — Mr. Life Manager",
        "Printables.",
        "Same guides, as PDFs. Open one, print it, tape it inside a cabinet door.",
        extra_p,
        {
            "nav": "<a class='cta' href='/guides/'>All guides →</a>",
            "main": "<main class='wrap'><ul>" + "".join(rows) + "</ul></main>",
        },
    ).replace("__TOKENS__", tokens)
    (OUT / "print" / "index.html").write_text(print_index)
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://mrlifemanager.com/sitemap.xml\n"
    )
    urls = [
        "https://mrlifemanager.com/",
        "https://mrlifemanager.com/index-parents.html",
        "https://mrlifemanager.com/first-night.html",
        "https://mrlifemanager.com/one-room.html",
        "https://mrlifemanager.com/guests.html",
        "https://mrlifemanager.com/underwater.html",
        "https://mrlifemanager.com/privacy.html",
        "https://mrlifemanager.com/guides/",
        "https://mrlifemanager.com/print/",
    ]
    urls += [f"https://mrlifemanager.com/guides/{slug}.html" for slug, *_ in GUIDES]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines += [f"  <url><loc>{u}</loc></url>" for u in urls]
    lines.append("</urlset>\n")
    (OUT / "sitemap.xml").write_text("\n".join(lines))
    print(f"Built _site/ — {len(GUIDES)} guides, {len(pdfs)} printables.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
