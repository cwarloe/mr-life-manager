#!/usr/bin/env python3
"""Read design tokens from products/landing/assets/tokens.css for code that
can't use CSS variables: share images and the PDF handout drawn by
generate_share_assets.py, and the <meta name="theme-color"> that
build_site.py writes (browsers read it before any CSS).

palette("print") returns the site's base tokens overlaid with the
[data-palette="print"] block, light values only (the @media blocks are
skipped). See products/landing/THEMING.md.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOKENS = ROOT / "products" / "landing" / "assets" / "tokens.css"


def _top_level_rules(css: str):
    """Yield (selector, body) for rules outside any @media/@font-face block."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    i = depth = 0
    start = 0
    while i < len(css):
        c = css[i]
        if c == "{":
            if depth == 0:
                selector, body_start = css[start:i].strip(), i + 1
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                if not selector.startswith("@"):
                    yield selector, css[body_start:i]
                start = i + 1
        i += 1


def palette(name: str | None = None) -> dict[str, str]:
    base: dict[str, str] = {}
    named: dict[str, str] = {}
    for selector, body in _top_level_rules(TOKENS.read_text(encoding="utf-8")):
        values = dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+?)\s*(?:;|$)", body))
        parts = [s.strip() for s in selector.split(",")]
        if ":root" in parts:
            base.update(values)
        elif name and f'[data-palette="{name}"]' in parts:
            named.update(values)
    if name and not named:
        raise SystemExit(f"{TOKENS.relative_to(ROOT)}: no [data-palette=\"{name}\"] block")
    return {**base, **named}


if __name__ == "__main__":
    import sys
    for key, value in sorted(palette(sys.argv[1] if len(sys.argv) > 1 else None).items()):
        print(f"{key}: {value}")
