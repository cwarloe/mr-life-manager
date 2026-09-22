#!/usr/bin/env python3
"""Every entry page must be complete before it ships.

An entry page is any file in products/landing/ with a step list. They are easy
to create by copying an older one, and every time that has happened something
was silently missing:

- the underwater page had the "Just the steps" button but none of the script
  behind it, so the button did nothing
- it had a one-line print block, so it printed three pages with the explanatory
  text included while the others printed one page without
- it collected email addresses with no tag and no sequence, so signups landed
  nowhere and received nothing — the exact failure ADR-015 exists to prevent

None of those are visible without opening the page and trying it. This checks
them mechanically instead.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "products" / "landing"
EMAILS = LANDING / "emails"

REQUIRED = [
    ("doing-mode script", "Reading mode persuades"),
    ("mode buttons", 'class="go-do"'),
    ("viewport-locked layout", "body.doing .steps{flex:1"),
    ("step numbering fix", "content:attr(data-n)"),
    ("print hides the reasoning", ".why,.why.open,.whybtn"),
    ("print forces all steps", ".step{display:block !important}"),
    ("Letter page size", "@page{size:Letter"),
    ("print scale", "body{zoom:"),
    ("MailerLite form", 'data-form="00ZwEr"'),
    ("one-PDF promise", "Dave's week on one page"),
]


def main() -> int:
    pages = sorted(p for p in LANDING.glob("*.html")
                   if 'class="steps"' in p.read_text())
    if not pages:
        print("no entry pages found — did the layout change?", file=sys.stderr)
        return 1

    problems = []
    for p in pages:
        s = p.read_text()
        for label, needle in REQUIRED:
            if needle not in s:
                problems.append(f"{p.name}: missing {label}")

        # A page that asks for an email must tag it, and that tag must have a
        # sequence to receive. Otherwise it collects addresses and sends nothing.
        if "ml-embedded" in s:
            m = re.search(r"var VALUE = '([a-z0-9-]+)'", s)
            if not m:
                problems.append(f"{p.name}: has a signup but does not tag it")
            else:
                seq = EMAILS / f"{m.group(1)}-sequence.md"
                if not seq.exists():
                    problems.append(
                        f"{p.name}: tags signups '{m.group(1)}' but "
                        f"{seq.name} does not exist")

    if problems:
        print("Entry pages are incomplete:\n", file=sys.stderr)
        for x in problems:
            print(f"  {x}", file=sys.stderr)
        print("\nSee content/README.md — \"Building a new entry page\".",
              file=sys.stderr)
        return 1

    print(f"{len(pages)} entry pages complete: "
          f"{', '.join(p.stem for p in pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
