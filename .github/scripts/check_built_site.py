#!/usr/bin/env python3
"""Verify generated-site metadata, routing and public offer invariants."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from guide_inventory import LEGACY_GUIDE_SLUGS
from site_catalog import (
    ENTRY_CSS_MARKERS,
    ENTRY_JS_MARKERS,
    ENTRY_ROUTES,
    ORIGIN,
    MAILERLITE_FORM_ATTR,
    public_url as catalog_public_url,
)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_site"


def public_url(path: Path) -> str:
    return catalog_public_url(path, OUT)


def main() -> int:
    problems: list[str] = []
    pages = sorted(OUT.rglob("*.html"))
    if not pages:
        print("_site has no HTML; run build_site.py first", file=sys.stderr)
        return 1

    legacy_pages = {
        OUT / "guides" / f"{old}.html": f"/guides/{new}.html"
        for old, new in LEGACY_GUIDE_SLUGS.items()
    }
    sitemap = (OUT / "sitemap.xml").read_text(encoding="utf-8")
    for path, target in legacy_pages.items():
        rel = path.relative_to(OUT)
        if not path.is_file():
            problems.append(f"missing legacy redirect: {rel} -> {target}")
            continue
        text = path.read_text(encoding="utf-8")
        if not (OUT / target.lstrip("/")).is_file():
            problems.append(f"{rel}: redirect target {target} was not built")
        for marker in ('data-mlm-redirect="1"',
                       f'http-equiv="refresh" content="0; url={target}"',
                       f'<link rel="canonical" href="{ORIGIN}{target}">',
                       'name="robots" content="noindex"'):
            if marker not in text:
                problems.append(f"{rel}: missing {marker}")
        if public_url(path) in sitemap:
            problems.append(f"sitemap.xml: legacy redirect {rel} must stay out of search")
    for old, new in LEGACY_GUIDE_SLUGS.items():
        if (OUT / "print" / f"{new}.pdf").is_file() and not (OUT / "print" / f"{old}.pdf").is_file():
            problems.append(f"missing legacy PDF alias: print/{old}.pdf")

    for path in pages:
        if path in legacy_pages:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(OUT)
        expected = public_url(path)
        canonicals = re.findall(r'<link rel="canonical" href="([^"]+)">', text)
        if canonicals != [expected]:
            problems.append(f"{rel}: canonical {canonicals!r}, expected {expected}")
        if text.count('data-mlm-meta="1"') != 1:
            problems.append(f"{rel}: expected exactly one generated metadata block")
        for marker in ('rel="icon" href="/favicon.svg"', 'rel="manifest" href="/site.webmanifest"',
                       'property="og:title"', 'property="og:description"',
                       'property="og:url"', 'property="og:image"',
                       'name="twitter:card" content="summary_large_image"'):
            if marker not in text:
                problems.append(f"{rel}: missing {marker}")

    if not (OUT / "assets" / "entry.js").is_file():
        problems.append("missing generated public file: assets/entry.js")
    else:
        entry_js = (OUT / "assets" / "entry.js").read_text(encoding="utf-8")
        for label, needle in ENTRY_JS_MARKERS:
            if needle not in entry_js:
                problems.append(f"assets/entry.js: missing {label}")

    if not (OUT / "assets" / "entry.css").is_file():
        problems.append("missing generated public file: assets/entry.css")
    else:
        entry_css = (OUT / "assets" / "entry.css").read_text(encoding="utf-8")
        for label, needle in ENTRY_CSS_MARKERS:
            if needle not in entry_css:
                problems.append(f"assets/entry.css: missing {label}")

    for route in ENTRY_ROUTES:
        name = route.page
        tag = route.slug
        text = (OUT / name).read_text(encoding="utf-8")
        completion = route.completion_page
        for marker in (f'data-guide="{tag}"', f'data-completion-url="/{completion}"',
                       'href="/assets/entry.css"', 'src="/assets/entry.js"', completion):
            if marker not in text:
                problems.append(f"{name}: missing {marker}")

        completion_text = (OUT / completion).read_text(encoding="utf-8")
        for marker in (MAILERLITE_FORM_ATTR, f'data-guide="{tag}"',
                       'src="/assets/entry.js"', "ml-fallback", "One thing finished",
                       'name="robots" content="noindex,nofollow"'):
            if marker not in completion_text:
                problems.append(f"{completion}: missing {marker}")
        # One ask after the win (principle 11): the signup is the only offer.
        for marker in ("/first-place.html", "navigator.share", "Where%20I%20stopped"):
            if marker in completion_text:
                problems.append(f"{completion}: must carry only the signup ask, found {marker}")

    offer = (OUT / "first-place.html").read_text(encoding="utf-8")
    for marker in ('mailto:hello@mrlifemanager.com?subject=First%20Place%20%2439',
                   "planned founding price", "No charge today",
                   "Reserve the $39 founding version", "How I found this:"):
        if marker not in offer:
            problems.append(f"first-place.html: missing {marker}")

    partners = (OUT / "partners.html").read_text(encoding="utf-8")
    for marker in ("Pilot it with five", "data-source-link", "Five-person pilot",
                   "new URLSearchParams", "/first-place.html?from=partner"):
        if marker not in partners:
            problems.append(f"partners.html: missing {marker}")

    privacy = (OUT / "privacy.html").read_text(encoding="utf-8")
    for marker in ("The Week", "MailerLite stores", "just underwater", "room that became storage",
                   "founding reservation"):
        if marker not in privacy:
            problems.append(f"privacy.html: missing {marker}")

    for name in ("favicon.svg", "site.webmanifest", "robots.txt", "sitemap.xml",
                 "assets/share/home.png", "assets/share/partners.png",
                 "print/partner-pilot.pdf"):
        if not (OUT / name).is_file():
            problems.append(f"missing generated public file: {name}")

    if "finished-" in sitemap:
        problems.append("sitemap.xml: completion pages must stay out of search")

    if problems:
        print("Built-site validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print(f"Validated {len(pages) - len(legacy_pages)} generated pages, "
          f"{len(legacy_pages)} legacy redirect(s), four entry routes, "
          "the partner path and the founding offer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

