#!/usr/bin/env python3
"""Single source for guide and printable inventories.

Derives GUIDES (publish-as-guide /guides/ pages), SHEETS (Chrome-rendered PDFs),
and PDF_TITLES (print-index labels). LEGACY_GUIDE_SLUGS keeps retired /guides/
and /print/ URLs working after a rename. Keep this out of site_catalog — that module
owns origin/entry routes only.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InventoryItem:
    stem: str
    title: str
    html_src: str = ""
    blurb: str = ""
    publish_as_guide: bool = False
    render_as_pdf: bool = False  # headless Chrome via render_all_pdfs
    share_qr: bool = True  # footer share QR (generate_share_assets.py)
    print_index: bool = True  # listed on /print/; False still publishes the PDF
    qr_url: str = ""  # flyers: the one QR destination, synced between flyer-qr markers


# Order: print-only sheet, then /guides/ publish order, then generated title-only.
INVENTORY: tuple[InventoryItem, ...] = (
    InventoryItem(
        stem="the-week",
        title="The Week",
        html_src="products/print/the-week.html",
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="first-apartment-checklist",
        title="The First Apartment Checklist",
        html_src="products/checklists/first-apartment/first-apartment-checklist.html",
        blurb="Everything to do, buy, and find out — in the order you'll need it.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="how-often-should-i",
        title="How Often Should I…?",
        html_src="products/checklists/how-often/how-often-should-i.html",
        blurb="Sheets, filters, towels, the dryer vent. Every cadence in one place.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="cleaning-supply-starter-list",
        title="Cleaning Supply Starter List",
        html_src="products/checklists/cleaning-supplies/cleaning-supply-starter-list.html",
        blurb="The nine products that do the work — and the ones you can skip.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="what-is-this-room-for",
        title="What Is This Room For?",
        html_src="products/checklists/room-for/what-is-this-room-for.html",
        blurb="One room, twenty minutes, three things to do about it.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="the-light-is-the-problem",
        title="The Light Is the Problem",
        html_src="products/checklists/light/the-light-is-the-problem.html",
        blurb="Why a room feels wrong when nothing in it is dirty.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="laundry-solved",
        title="Laundry, Solved",
        html_src="products/checklists/laundry/laundry-solved.html",
        blurb="Sorting, settings, stains, and the step everyone actually skips.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="six-meals",
        title="Six Meals and a Stocked Kitchen",
        html_src="products/checklists/six-meals/six-meals.html",
        blurb="Enough to stop deciding what's for dinner every single night.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    InventoryItem(
        stem="household-agreement",
        title="The Household Agreement",
        html_src="products/worksheets/household-agreement/household-agreement.html",
        blurb="Decide it once, together, before it's a problem.",
        publish_as_guide=True,
        render_as_pdf=True,
    ),
    # Posted flyer: one QR to one entry page, no footer share QR, not listed
    # on /print/ (it is for posting, not for readers). Draft, pending approval.
    InventoryItem(
        stem="flyer-someones-coming",
        title="Flyer: Having People Over",
        html_src="products/print/flyer-someones-coming.html",
        render_as_pdf=True,
        share_qr=False,
        print_index=False,
        qr_url="https://mrlifemanager.com/guests.html?from=flyer-guests",
    ),
    # Title-only: PDF from generate_share_assets.py, not Chrome / not a /guides/ page.
    InventoryItem(
        stem="partner-pilot",
        title="Five-Person Pilot Handouts",
    ),
)


# Shapes match the former hardcodes in build_site.py / render_all_pdfs.py.
GUIDES: list[tuple[str, str, str, str]] = [
    (item.stem, item.html_src, item.title, item.blurb)
    for item in INVENTORY
    if item.publish_as_guide
]

SHEETS: list[tuple[str, str]] = [
    (item.html_src, item.stem)
    for item in INVENTORY
    if item.render_as_pdf
]

# Sheets that carry the footer share QR. Flyers do not: one QR, one offer.
SHARE_QR_SHEETS: list[tuple[str, str]] = [
    (item.html_src, item.stem)
    for item in INVENTORY
    if item.render_as_pdf and item.share_qr
]

# Flyer source -> its single QR destination.
FLYER_QRS: dict[str, str] = {
    item.html_src: item.qr_url for item in INVENTORY if item.qr_url
}

# Published under /print/ but left off the /print/ index.
UNLISTED_PDFS: set[str] = {
    f"{item.stem}.pdf" for item in INVENTORY if not item.print_index
}

PDF_TITLES: dict[str, str] = {
    f"{item.stem}.pdf": item.title for item in INVENTORY
}


# Retired guide stem -> current stem. build_site.py publishes a static redirect
# at /guides/<old>.html (meta refresh + canonical to the new page, noindex, out
# of the sitemap) and a copy of the current PDF at /print/<old>.pdf, unlisted.
LEGACY_GUIDE_SLUGS: dict[str, str] = {
    # Renamed 2026-09-28: the guide has been six meals since 2026-09-25.
    "ten-meals": "six-meals",
}

_GUIDE_STEMS = {slug for slug, *_ in GUIDES}
for _old, _new in LEGACY_GUIDE_SLUGS.items():
    if _new not in _GUIDE_STEMS:
        raise SystemExit(f"LEGACY_GUIDE_SLUGS: {_old!r} points at unknown guide {_new!r}")
    if _old in _GUIDE_STEMS:
        raise SystemExit(f"LEGACY_GUIDE_SLUGS: {_old!r} is still a live guide")
