#!/usr/bin/env python3
"""Smoke-test the production site without submitting forms or collecting data."""

from __future__ import annotations

import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE = "https://mrlifemanager.com"
PAGES = {
    "/": ("Run your home without carrying all of it in your head",),
    "/first-night.html": ('data-form="00ZwEr"', "var VALUE = 'first-night'", "Dave's week on one page"),
    "/guests.html": ('data-form="00ZwEr"', "var VALUE = 'guests'", "Dave's week on one page"),
    "/underwater.html": ('data-form="00ZwEr"', "var VALUE = 'underwater'", "Dave's week on one page"),
    "/one-room.html": ('data-form="00ZwEr"', "var VALUE = 'one-room'", "Dave's week on one page"),
    "/finished-first-night.html": ('data-form="00ZwEr"', "var VALUE = 'first-night'", "One thing finished"),
    "/finished-guests.html": ('data-form="00ZwEr"', "var VALUE = 'guests'", "One thing finished"),
    "/finished-underwater.html": ('data-form="00ZwEr"', "var VALUE = 'underwater'", "One thing finished"),
    "/finished-one-room.html": ('data-form="00ZwEr"', "var VALUE = 'one-room'", "One thing finished"),
    "/first-place.html": ("First%20Place%20%2439%20founding%20reservation", "Reserve the $39 founding version", "planned founding price"),
    "/partners.html": ("Pilot it with five", "data-source-link", "Five-person pilot", "/print/partner-pilot.pdf"),
    "/privacy.html": ("MailerLite stores", "The Week"),
}
SITEMAP_URLS = (
    f"{BASE}/",
    f"{BASE}/first-night.html",
    f"{BASE}/guests.html",
    f"{BASE}/underwater.html",
    f"{BASE}/one-room.html",
    f"{BASE}/privacy.html",
)


def fetch(url: str) -> tuple[str, str, bytes]:
    request = Request(url, headers={"User-Agent": "mr-life-manager-healthcheck/1.0"})
    with urlopen(request, timeout=20) as response:
        return response.geturl(), response.headers.get_content_type(), response.read()


def run_once() -> list[str]:
    problems: list[str] = []
    for path, markers in PAGES.items():
        url = BASE + path
        try:
            final, content_type, body = fetch(url)
        except (HTTPError, URLError, TimeoutError) as exc:
            problems.append(f"{url}: {exc}")
            continue
        if not final.startswith(BASE):
            problems.append(f"{url}: redirected outside canonical domain to {final}")
        if content_type != "text/html":
            problems.append(f"{url}: content type {content_type}, expected text/html")
        text = body.decode("utf-8", errors="replace")
        for marker in markers:
            if marker not in text:
                problems.append(f"{url}: missing {marker}")
        if 'rel="canonical"' not in text:
            problems.append(f"{url}: missing canonical metadata")
        if path != "/privacy.html" and 'href="/privacy.html"' not in text:
            problems.append(f"{url}: missing privacy link")

    pdf_url = BASE + "/print/the-week.pdf"
    try:
        final, content_type, body = fetch(pdf_url)
        if final != pdf_url:
            problems.append(f"{pdf_url}: unexpected final URL {final}")
        if content_type != "application/pdf" or not body.startswith(b"%PDF-"):
            problems.append(f"{pdf_url}: response is not a PDF")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{pdf_url}: {exc}")

    partner_pdf_url = BASE + "/print/partner-pilot.pdf"
    try:
        final, content_type, body = fetch(partner_pdf_url)
        if final != partner_pdf_url:
            problems.append(f"{partner_pdf_url}: unexpected final URL {final}")
        if content_type != "application/pdf" or not body.startswith(b"%PDF-"):
            problems.append(f"{partner_pdf_url}: response is not a PDF")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{partner_pdf_url}: {exc}")

    share_url = BASE + "/assets/share/home.png"
    try:
        final, content_type, body = fetch(share_url)
        if final != share_url:
            problems.append(f"{share_url}: unexpected final URL {final}")
        if content_type != "image/png" or not body.startswith(b"\x89PNG\r\n\x1a\n"):
            problems.append(f"{share_url}: response is not a PNG")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{share_url}: {exc}")

    sitemap_url = BASE + "/sitemap.xml"
    try:
        final, content_type, body = fetch(sitemap_url)
        if final != sitemap_url:
            problems.append(f"{sitemap_url}: unexpected final URL {final}")
        if content_type not in {"application/xml", "text/xml"}:
            problems.append(f"{sitemap_url}: content type {content_type}, expected XML")
        sitemap = body.decode("utf-8", errors="replace")
        if "finished-" in sitemap:
            problems.append(f"{sitemap_url}: completion pages must stay out of search")
        for loc in SITEMAP_URLS:
            if loc not in sitemap:
                problems.append(f"{sitemap_url}: missing {loc}")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{sitemap_url}: {exc}")

    robots_url = BASE + "/robots.txt"
    try:
        final, _, body = fetch(robots_url)
        robots = body.decode("utf-8", errors="replace")
        if sitemap_url not in robots:
            problems.append(f"{robots_url}: missing Sitemap line for {sitemap_url}")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{robots_url}: {exc}")

    for start in ("http://mrlifemanager.com/", "https://www.mrlifemanager.com/"):
        try:
            final, _, _ = fetch(start)
            if final != BASE + "/":
                problems.append(f"{start}: ended at {final}, expected {BASE}/")
        except (HTTPError, URLError, TimeoutError) as exc:
            problems.append(f"{start}: {exc}")
    return problems


def main() -> int:
    problems: list[str] = []
    for attempt in range(3):
        problems = run_once()
        if not problems:
            print("Production smoke test passed: twelve pages, four routes, one partner path, one founding offer, two PDFs, share images, sitemap, robots and canonical redirects.")
            return 0
        if attempt < 2:
            time.sleep(10)
    print("Production smoke test failed:", file=sys.stderr)
    for problem in problems:
        print(f"- {problem}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
