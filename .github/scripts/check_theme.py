#!/usr/bin/env python3
"""Theme check: every color, font and shadow on the site comes from
products/landing/assets/tokens.css. See products/landing/THEMING.md.

    python3 .github/scripts/check_theme.py     list findings, exit 1 if any

validate_repo.py runs the same scan, so CI fails on a new literal.

Flags, outside tokens.css: hex colors, rgb()/rgba()/hsl()/hsla(), white/black
as a CSS color, colors inside data-URI images (%23abc), SVG fill/stroke hex
colors, and font families written out instead of var(--font-ui) and friends.
Scans the site's sources (HTML, CSS, JS under products/) and the generators
that write CSS or images (.github/scripts/*.py).

A line that truly needs a literal says why in a comment containing
"theme-ok: <reason>". The inline share QR (between the share-qr markers) is
skipped: it is generated, and scanners need it black on white.
PROTOTYPES are design galleries for options not yet picked: their counts are
listed, not failed. When an option is chosen, move its values into tokens.css
and drop the page from PROTOTYPES.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOKENS = "products/landing/assets/tokens.css"
SCAN = (("products", ("*.html", "*.css", "*.js")), (".github/scripts", ("*.py",)))
# Not checked, with the reason:
SKIP = (
    TOKENS,                                    # the one file allowed raw values
    "products/print/fonts/embedded-fonts.css",  # base64 font faces for PDFs (font-family names the faces)
    ".github/scripts/check_theme.py",          # this file's own patterns
)
# Design galleries showing palettes that haven't been picked.
PROTOTYPES = ("products/landing/templates/design-options.html",)

HEX = re.compile(r"(?<=[:\s,(])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?=[;}\s,)!'\"]|$)")
ATTR_HEX = re.compile(r"\b(?:fill|stroke|stop-color|color)=[\"']#[0-9a-fA-F]{3,8}[\"']")
PY_HEX = re.compile(r"[\"']#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})[\"']")
FUNC = re.compile(r"\b(?:rgba?|hsla?)\(\s*[\d.]")
NAMED = re.compile(r"\b(?:color|background(?:-color)?|border(?:-[\w-]+)?|fill|stroke|outline(?:-color)?)\s*:[^;}\"']*?\b(?:white|black)\b", re.I)
URI = re.compile(r"%23[0-9a-fA-F]{3,8}\b")
FONT = re.compile(r"\bfont(?:-family)?\s*:\s*([^;}{\"']*(?:\"[^\"]*\"[^;}{\"']*)*)")
FAMILY = re.compile(r"\"[^\"]+\"|\b(?:serif|sans-serif|monospace|cursive|system-ui|Arial|Helvetica|Impact|Georgia|Verdana|Times)\b")
QR_BLOCK = re.compile(r"<!-- share-qr:start -->.*?<!-- share-qr:end -->", re.S)
THEME_META = re.compile(r"<meta\b[^>]*name=[\"']theme-color[\"'][^>]*>")


def files() -> list[Path]:
    out: list[Path] = []
    for base, patterns in SCAN:
        for pattern in patterns:
            out += (ROOT / base).rglob(pattern)
    return sorted(p for p in set(out) if p.relative_to(ROOT).as_posix() not in SKIP)


def hits_in(line: str, python: bool) -> list[str]:
    line = THEME_META.sub("", line)  # read by the browser before any CSS
    hits = HEX.findall(line) + ATTR_HEX.findall(line) + URI.findall(line)
    if python:
        hits += PY_HEX.findall(line)
    hits += [m.group(0).rstrip(" (0123456789.") + "(…)" for m in FUNC.finditer(line)]
    hits += ["named color: " + m.group(0)[:40] for m in NAMED.finditer(line)]
    for m in FONT.finditer(line):
        if "var(--" not in m.group(1) and FAMILY.search(m.group(1)):
            hits.append("font: " + m.group(1).strip()[:40])
    return hits


def scan() -> tuple[list[str], dict[str, int]]:
    findings: list[str] = []
    prototypes: dict[str, int] = {}
    for path in files():
        rel = path.relative_to(ROOT).as_posix()
        text = QR_BLOCK.sub(lambda m: "\n" * m.group(0).count("\n"), path.read_text(encoding="utf-8"))
        for number, line in enumerate(text.splitlines(), 1):
            if "theme-ok:" in line:
                continue
            hits = hits_in(line, path.suffix == ".py")
            if not hits:
                continue
            if rel in PROTOTYPES:
                prototypes[rel] = prototypes.get(rel, 0) + len(hits)
            else:
                findings.append(f"{rel}:{number}  {', '.join(dict.fromkeys(hits))}")
    return findings, prototypes


def main() -> int:
    findings, prototypes = scan()
    for finding in findings:
        print(finding)
    if findings:
        print(f"\n{len(findings)} line(s) use raw colors or fonts. Use a token from {TOKENS} "
              "(see products/landing/THEMING.md).")
    else:
        print("Theme check: every page uses tokens.")
    if prototypes:
        print("Design prototypes (not checked): "
              + ", ".join(f"{name} {count}" for name, count in prototypes.items()))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
