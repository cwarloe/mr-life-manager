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
                       'property="og:url"', 'name="twitter:card"'):
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
        for marker in ('data-form="00ZwEr"', f"var VALUE = '{tag}'", "Dave's week on one page"):
            if marker not in text:
                problems.append(f"{name}: missing {marker}")

    privacy = (OUT / "privacy.html").read_text(encoding="utf-8")
    for marker in ("The Week", "MailerLite stores", "just underwater", "room that became storage"):
        if marker not in privacy:
            problems.append(f"privacy.html: missing {marker}")

    for name in ("favicon.svg", "site.webmanifest", "robots.txt", "sitemap.xml"):
        if not (OUT / name).is_file():
            problems.append(f"missing generated public file: {name}")

    if problems:
        print("Built-site validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print(f"Validated {len(pages)} generated pages and four entry routes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

