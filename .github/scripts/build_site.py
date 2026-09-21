#!/usr/bin/env python3
"""Assemble the public site into _site/ for GitHub Pages.

Single source of truth: the guides stay where they live in products/.
This copies them to /guides/<slug>.html, appends a short credit line,
and generates the guide index. Nothing is duplicated in git.
"""
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

CTA = """
<div class=\"mlm-cta\">
  <p class=\"mlm-cta-body\">Made by <a href=\"/\">Mr. Life Manager</a> — the practical
  systems of running a life, written down. Free to use, copy, and teach from.</p>
</div>
<style>
.mlm-cta{max-width:50rem;margin:0 auto;padding:1.6rem 1.5rem 3rem;border-top:2px solid var(--rule)}
.mlm-cta-body{font-family:var(--serif);font-size:.95rem;line-height:1.55;color:var(--slate);
  margin:0;max-width:52ch}
.mlm-cta-body a{font-weight:600;color:var(--blue);text-decoration:none;
  border-bottom:2px solid var(--blue-soft);padding-bottom:1px}
.mlm-cta-body a:hover{border-bottom-color:var(--blue)}
@media print{.mlm-cta{display:none}}
</style>
"""

INDEX_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>All Guides — Mr. Life Manager</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap\">
<style>
__TOKENS__
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;
  line-height:1.55;margin:0;-webkit-font-smoothing:antialiased}
.wrap{max-width:54rem;margin:0 auto;padding:0 1.5rem}
.bar{border-bottom:1px solid var(--rule)}
.bar .wrap{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem}
.brand{font-weight:700;font-size:.95rem;letter-spacing:-.01em;text-decoration:none;color:inherit}
.brand span{color:var(--blue)}
.bar a.cta{font-size:.85rem;color:var(--blue);text-decoration:none;font-weight:600}
header.hero{padding:3.5rem 0 2.5rem;border-bottom:3px solid var(--ink)}
.kicker{font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--blue);margin:0 0 1rem}
h1{font-size:clamp(2.2rem,6vw,3.2rem);font-weight:800;line-height:1.03;letter-spacing:-.03em;
  margin:0;text-wrap:balance;max-width:18ch}
.sub{font-family:var(--serif);font-size:1.15rem;line-height:1.5;color:var(--slate);
  margin:1.2rem 0 0;max-width:50ch}
.list{display:grid;gap:1rem;margin:2.5rem 0 0;padding:0 0 3rem}
a.card{border:2px solid var(--rule-strong);border-radius:3px;padding:1.3rem 1.5rem;
  background:var(--surface);text-decoration:none;color:inherit;display:grid;gap:.4rem}
a.card:hover{border-color:var(--blue)}
a.card h2{font-size:1.2rem;font-weight:700;margin:0;letter-spacing:-.015em}
a.card p{font-family:var(--serif);font-size:.97rem;line-height:1.5;color:var(--slate);margin:0}
a.card .go{font-size:.83rem;font-weight:600;color:var(--blue);margin-top:.2rem}
.foot-cta{border-top:3px solid var(--ink);background:var(--surface);padding:2.5rem 0 3rem}
.foot-cta h2{font-size:1.5rem;font-weight:700;margin:0 0 .5rem;letter-spacing:-.02em}
.foot-cta p{font-family:var(--serif);font-size:1.03rem;line-height:1.6;color:var(--slate);
  margin:0 0 1.2rem;max-width:52ch}
.foot-cta a{display:inline-block;font-weight:600;padding:.8rem 1.4rem;border:2px solid var(--ink);
  border-radius:3px;background:var(--ink);color:var(--paper);text-decoration:none;margin:0 .5rem .5rem 0}
.foot-cta a:hover{background:var(--blue);border-color:var(--blue)}
.foot-cta a.ghost{background:transparent;color:var(--ink)}
.foot-cta a.ghost:hover{background:var(--blue-soft);border-color:var(--blue);color:var(--blue)}
footer{padding:2rem 0 3rem;font-size:.82rem;color:var(--slate)}
footer .wrap{display:flex;flex-wrap:wrap;gap:.5rem 2rem;justify-content:space-between}
footer b{color:var(--ink);font-weight:600}
</style>
</head>
<body>
<div class=\"bar\"><div class=\"wrap\">
  <a class=\"brand\" href=\"/\">Mr.&nbsp;<span>Life Manager</span></a>
  <a class=\"cta\" href=\"/print/\">Printables →</a>
</div></div>
<header class=\"hero\"><div class=\"wrap\">
  <p class=\"kicker\">Free · Complete · Nothing to buy</p>
  <h1>All the guides.</h1>
  <p class=\"sub\">The practical systems of running a home, written down plainly. Read them here,
  print them, or forward them to someone who just moved out.</p>
</div></header>
<main class=\"wrap\"><div class=\"list\">
__CARDS__
</div></main>
<section class=\"foot-cta\"><div class=\"wrap\">
  <h2>Want a printed copy?</h2>
  <p>Every guide above also exists as a PDF. Grab the file. Or start from
  what's actually going on tonight — that page has the steps in order, and
  an optional printable at the bottom.</p>
  <a href=\"/print/\">See the printables</a>
  <a class=\"ghost\" href=\"/\">What's going on right now</a>
</div></section>
<footer><div class=\"wrap\">
  <span><b>Mr. Life Manager</b> — <a href=\"mailto:hello@mrlifemanager.com\">hello@mrlifemanager.com</a></span>
  <span>Free to use, copy, and teach from — with credit. Not for resale. · <a href=\"/privacy.html\">Privacy</a></span>
</div></footer>
</body>
</html>
"""

PRINT_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Printables — Mr. Life Manager</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap\">
<style>
__TOKENS__
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.55;margin:0}
.wrap{max-width:40rem;margin:0 auto;padding:0 1.5rem}
.bar{border-bottom:1px solid var(--rule)}
.bar .wrap{display:flex;justify-content:space-between;align-items:center;padding:1rem 1.5rem}
.brand{font-weight:700;font-size:.95rem;text-decoration:none;color:inherit}
.brand span{color:var(--blue)}
.bar a.cta{font-size:.85rem;color:var(--blue);text-decoration:none;font-weight:600}
header{padding:3rem 0 1.5rem}
h1{font-size:clamp(1.8rem,5vw,2.6rem);font-weight:800;letter-spacing:-.03em;margin:0}
.sub{font-family:var(--serif);color:var(--slate);margin:1rem 0 0;max-width:42ch}
ul{list-style:none;padding:0;margin:1.5rem 0 3rem}
li{border-top:1px solid var(--rule)}
a.file{display:flex;justify-content:space-between;gap:1rem;padding:1rem 0;text-decoration:none;color:inherit;font-weight:600}
a.file:hover{color:var(--blue)}
a.file span{font-weight:500;color:var(--slate);font-size:.85rem}
footer{padding:2rem 0 3rem;font-size:.82rem;color:var(--slate);border-top:1px solid var(--rule)}
</style>
</head>
<body>
<div class=\"bar\"><div class=\"wrap\">
  <a class=\"brand\" href=\"/\">Mr.&nbsp;<span>Life Manager</span></a>
  <a class=\"cta\" href=\"/guides/\">All guides →</a>
</div></div>
<header class=\"wrap\">
  <h1>Printables.</h1>
  <p class=\"sub\">Same guides, as PDFs. Open one, print it, tape it inside a cabinet door.</p>
</header>
<main class=\"wrap\"><ul>
__FILES__
</ul></main>
<footer><div class=\"wrap\">
  <b>Mr. Life Manager</b> — <a href=\"mailto:hello@mrlifemanager.com\">hello@mrlifemanager.com</a>
  · <a href=\"/privacy.html\">Privacy</a>
</div></footer>
</body>
</html>
"""


def tokens_from(path: Path) -> str:
    css = path.read_text()
    m = re.search(r\"(:root\\{.*?)\\*\\{box-sizing\", css, re.S)
    if not m:
        sys.exit(f\"could not lift design tokens from {path}\")
    return m.group(1).rstrip()


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / \"guides\").mkdir(parents=True)

    for item in LANDING.iterdir():
        if item.is_dir() or item.name == \"SETUP.md\":
            continue
        shutil.copy2(item, OUT / item.name)

    tokens = tokens_from(ROOT / GUIDES[0][1])
    cards = []
    for slug, src, title, blurb in GUIDES:
        html = (ROOT / src).read_text()
        if \"</body>\" not in html:
            sys.exit(f\"{src}: no </body>\")
        html = html.replace(\"</body>\", CTA + \"</body>\")
        (OUT / \"guides\" / f\"{slug}.html\").write_text(html)
        cards.append(
            f'  <a class=\"card\" href=\"/guides/{slug}.html\">\\n'
            f'    <h2>{title}</h2>\\n'
            f'    <p>{blurb}</p>\\n'
            f'    <span class=\"go\">Read it →</span>\\n'
            f'  </a>'
        )

    index = (INDEX_TEMPLATE.replace(\"__TOKENS__\", tokens).replace(\"__CARDS__\", \"\\n\".join(cards)))
    (OUT / \"guides\" / \"index.html\").write_text(index)

    pdf_src = ROOT / \"products\" / \"guides-pdf\"
    pdfs = sorted(pdf_src.glob(\"*.pdf\"))
    if not pdfs:
        sys.exit(\"no printables found in products/guides-pdf/\")
    (OUT / \"print\").mkdir(parents=True, exist_ok=True)
    file_rows = []
    for pdf in pdfs:
        shutil.copy2(pdf, OUT / \"print\" / pdf.name)
        label = PDF_TITLES.get(pdf.name, pdf.stem.replace(\"-\", \" \").title())
        file_rows.append(
            f'  <li><a class=\"file\" href=\"/print/{pdf.name}\">{label}'
            f'<span>PDF</span></a></li>'
        )
    print_index = (PRINT_TEMPLATE.replace(\"__TOKENS__\", tokens).replace(\"__FILES__\", \"\\n\".join(file_rows)))
    (OUT / \"print\" / \"index.html\").write_text(print_index)

    (OUT / \"robots.txt\").write_text(
        \"User-agent: *\\nAllow: /\\n\\nSitemap: https://mrlifemanager.com/sitemap.xml\\n\"
    )
    urls = [
        \"https://mrlifemanager.com/\",
        \"https://mrlifemanager.com/index-parents.html\",
        \"https://mrlifemanager.com/first-night.html\",
        \"https://mrlifemanager.com/guests.html\",
        \"https://mrlifemanager.com/privacy.html\",
        \"https://mrlifemanager.com/guides/\",
        \"https://mrlifemanager.com/print/\",
    ]
    urls += [f\"https://mrlifemanager.com/guides/{slug}.html\" for slug, *_ in GUIDES]
    body = [
        '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>''',
        '<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">',
    ]
    body += [f\"  <url><loc>{u}</loc></url>\" for u in urls]
    body.append(\"</urlset>\\n\")
    (OUT / \"sitemap.xml\").write_text(\"\\n\".join(body))

    print(f\"Built _site/ — {len(GUIDES)} guides, {len(pdfs)} printables.\")
    return 0


if __name__ == \"__main__\":
    raise SystemExit(main())
