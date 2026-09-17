#!/usr/bin/env python3
"""Validate repository-owned HTML structure and local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def validate_html() -> int:
    files = sorted((ROOT / "products").rglob("*.html"))
    required = {
        "HTML5 doctype": re.compile(r"^\s*<!doctype html>", re.IGNORECASE),
        "language declaration": re.compile(r"<html\b[^>]*\blang=[\"'][^\"']+[\"']", re.IGNORECASE),
        "UTF-8 charset": re.compile(r"<meta\b[^>]*\bcharset=[\"']?utf-8", re.IGNORECASE),
        "mobile viewport": re.compile(r"<meta\b[^>]*\bname=[\"']viewport[\"']", re.IGNORECASE),
        "head element": re.compile(r"<head\b[^>]*>.*?</head>", re.IGNORECASE | re.DOTALL),
        "body element": re.compile(r"<body\b[^>]*>.*?</body>", re.IGNORECASE | re.DOTALL),
        "closing html element": re.compile(r"</html>\s*$", re.IGNORECASE),
    }

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for label, pattern in required.items():
            if not pattern.search(text):
                error(f"{rel}: missing {label}")

    return len(files)


def validate_markdown_links() -> tuple[int, int]:
    files = sorted(ROOT.rglob("*.md"))
    checked = 0
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            raw = match.group(1).strip().strip("<>")
            target = re.split(r"\s+[\"']", raw, maxsplit=1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
                continue

            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            candidate = (path.parent / target).resolve()
            checked += 1

            try:
                candidate.relative_to(ROOT)
            except ValueError:
                error(f"{path.relative_to(ROOT)}: link escapes repository: {raw}")
                continue

            if candidate.exists():
                continue
            if candidate.is_dir() and (candidate / "README.md").exists():
                continue

            line = text.count("\n", 0, match.start()) + 1
            error(
                f"{path.relative_to(ROOT)}:{line}: missing local target "
                f"{target}"
            )

    return len(files), checked


def main() -> int:
    html_count = validate_html()
    markdown_count, link_count = validate_markdown_links()

    if ERRORS:
        print("Repository validation failed:")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print(
        f"Validated {html_count} HTML files, {markdown_count} Markdown files, "
        f"and {link_count} local Markdown links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
