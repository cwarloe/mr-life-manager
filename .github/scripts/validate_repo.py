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


def validate_share_qr() -> None:
    """Each sheet's inline footer QR must match products/print/share-qr.svg.

    generate_share_assets.py writes both; this catches a hand edit or a sheet
    added to guide_inventory.SHEETS without re-running it.
    """
    sys.path.insert(0, str(ROOT / ".github" / "scripts"))
    from guide_inventory import FLYER_QRS, SHARE_QR_SHEETS, SHEETS  # noqa: E402

    svg_path = ROOT / "products" / "print" / "share-qr.svg"
    if not svg_path.is_file():
        error("products/print/share-qr.svg: missing (run generate_share_assets.py)")
        return
    svg = svg_path.read_text(encoding="utf-8").strip()
    block = re.compile(r"<!-- share-qr:start -->(.*?)<!-- share-qr:end -->", re.DOTALL)
    with_share = {src for src, _stem in SHARE_QR_SHEETS}
    for src, _stem in SHEETS:
        if src not in with_share and block.search((ROOT / src).read_text(encoding="utf-8")):
            error(f"{src}: must not carry a share QR (one QR, one offer)")
    for src, _stem in SHARE_QR_SHEETS:
        found = block.findall((ROOT / src).read_text(encoding="utf-8"))
        if len(found) != 1:
            error(f"{src}: expected one share-qr block, found {len(found)}")
        elif found[0] != svg:
            error(f"{src}: inline share QR differs from products/print/share-qr.svg "
                  "(run generate_share_assets.py)")


def validate_flyer_qrs() -> None:
    """Each flyer carries one QR destination, repeated identically, and names it.

    The QR itself is drawn by generate_share_assets.py (qrcode is not installed
    in CI), so this checks the label it writes rather than decoding the image.
    """
    sys.path.insert(0, str(ROOT / ".github" / "scripts"))
    from guide_inventory import FLYER_QRS  # noqa: E402

    block = re.compile(r"<!-- flyer-qr:start -->(.*?)<!-- flyer-qr:end -->", re.DOTALL)
    for src, url in FLYER_QRS.items():
        found = block.findall((ROOT / src).read_text(encoding="utf-8"))
        if not found:
            error(f"{src}: no flyer-qr block (run generate_share_assets.py)")
            continue
        if len(set(found)) != 1:
            error(f"{src}: flyer QR copies differ (run generate_share_assets.py)")
        if f'aria-label="QR code for {url}"' not in found[0]:
            error(f"{src}: flyer QR is not labeled for {url} (run generate_share_assets.py)")


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

            line = text.count("\n", 0, match.start()) + 1
            error(
                f"{path.relative_to(ROOT)}:{line}: missing local target "
                f"{target}"
            )

    return len(files), checked


def main() -> int:
    html_count = validate_html()
    markdown_count, link_count = validate_markdown_links()
    validate_share_qr()
    validate_flyer_qrs()

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
