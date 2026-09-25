#!/usr/bin/env python3
"""Verify generated-site metadata, routing and public offer invariants."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_site"
ORIGIN = "https://mrlifemanager.com"


def public_url(path: Path) -> str:
    rel = path.relative_to(OUT)
    if rel.name == "index.html":
        parent = rel.parent.as_posix()
        suffix = "/" if parent == "." else f"/{parent}/"
    else:
        suffix = f"/{rel.as_posix()}"
    return ORIGIN + suffix


def main() -> int:
    problems: list[str] = []
    pages = sorted(OUT.rglob("*.html"))
    if not pages:
        print("_site has no HTML; run build_site.py first", file=sys.stderr)
        return 1

    for path in pages:
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

    entries = {
        "first-night.html": "first-night",
        "guests.html": "guests",
        "underwater.html": "underwater",
        "one-room.html": "one-room",
    }
    for name, tag in entries.items():
        text = (OUT / name).read_text(encoding="utf-8")
        completion = f"finished-{name}"
        for marker in (f"var VALUE = '{tag}'", completion):
            if marker not in text:
                problems.append(f"{name}: missing {marker}")

        completion_text = (OUT / completion).read_text(encoding="utf-8")
        for marker in ('data-form="00ZwEr"', f"var VALUE = '{tag}'", "One thing finished",
                       "/first-place.html", "navigator.share", f"shared-{tag}",
                       'name="robots" content="noindex,nofollow"'):
            if marker not in completion_text:
                problems.append(f"{completion}: missing {marker}")

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

    sitemap = (OUT / "sitemap.xml").read_text(encoding="utf-8")
    if "finished-" in sitemap:
        problems.append("sitemap.xml: completion pages must stay out of search")

    if problems:
        print("Built-site validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print(f"Validated {len(pages)} generated pages, four entry routes, the partner path and the founding offer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
