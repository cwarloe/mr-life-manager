#!/usr/bin/env python3
"""Fail if outbound HTTPS links in published HTML no longer resolve. Runs weekly."""
from __future__ import annotations
import re, sys, urllib.error, urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[2]
UA = "Mozilla/5.0 (compatible; MrLifeManagerLinkCheck/1.0)"
TIMEOUT = 20
# Hosts that reliably reject automated HEAD/GET but are not broken.
SKIP_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com"}


def links() -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for html in sorted(ROOT.glob("products/**/*.html")):
        for url in re.findall(r'href="(https?://[^"]+)"', html.read_text()):
            if any(h in url for h in SKIP_HOSTS):
                continue
            found.setdefault(url, []).append(str(html.relative_to(ROOT)))
    return found


def check(url: str) -> tuple[str, int | str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return url, r.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except Exception as e:                      # timeout, DNS, TLS
        return url, type(e).__name__


def main() -> int:
    found = links()
    if not found:
        print("No outbound links to check.")
        return 0

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(pool.map(check, found))

    bad = {u: s for u, s in results.items()
           if not (isinstance(s, int) and 200 <= s < 400)}

    print(f"Checked {len(found)} outbound links.")
    for url, status in sorted(bad.items()):
        print(f"  BROKEN [{status}] {url}")
        for where in found[url]:
            print(f"      in {where}")

    if bad:
        print("\nPull these links. Do not wait for a replacement —")
        print("see docs/business/commerce-rules.md, Maintenance cadence.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
