#!/usr/bin/env python3
"""Single source for public origin, URL helper, and the four entry routes.

Published behavior must stay identical to the prior hardcodes in
build_site / check_built_site / check_live_site. Guide/printable inventories
live elsewhere — do not fold them in here.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ORIGIN = "https://mrlifemanager.com"
MAILERLITE_FORM_ID = "00ZwEr"
MAILERLITE_FORM_ATTR = f'data-form="{MAILERLITE_FORM_ID}"'


@dataclass(frozen=True)
class EntryRoute:
    slug: str
    door_title: str
    completion_message: str
    share_image: str

    @property
    def page(self) -> str:
        return f"{self.slug}.html"

    @property
    def completion_page(self) -> str:
        return f"finished-{self.slug}.html"

    @property
    def back_path(self) -> str:
        return f"/{self.slug}.html"


# Published entry order — keep stable (completion + live-check lists).
ENTRY_ROUTES: tuple[EntryRoute, ...] = (
    EntryRoute(
        slug="first-night",
        door_title="Your first night",
        completion_message=(
            "You handled the things that cost most to miss on a first night."
        ),
        share_image="first-night.png",
    ),
    EntryRoute(
        slug="guests",
        door_title="Someone's coming over",
        completion_message=(
            "The door can open now. Whatever did not get done can wait."
        ),
        share_image="guests.png",
    ),
    EntryRoute(
        slug="underwater",
        door_title="Just underwater",
        completion_message=(
            "You put a floor under the week. That is different from fixing everything."
        ),
        share_image="underwater.png",
    ),
    EntryRoute(
        slug="one-room",
        door_title="The room that became storage",
        completion_message=(
            "You reclaimed a usable part of the room. One finished zone is real progress."
        ),
        share_image="one-room.png",
    ),
)


# Shared entry.js / entry.css body needles for check_entry_pages (source)
# and check_built_site (_site copies). Keep one list so markers cannot drift.
ENTRY_JS_MARKERS: tuple[tuple[str, str], ...] = (
    ("doing-mode", "classList.add('doing')"),
    ("source attribution handoff", "new URLSearchParams(window.location.search).get('from')"),
    ("MailerLite dual-field tag", "fields[guide]"),
    ("MailerLite fallback", "ml-fallback"),
    ("guide VALUE wiring", "var VALUE = guide"),
)

ENTRY_CSS_MARKERS: tuple[tuple[str, str], ...] = (
    ("viewport-locked layout", "body.doing .steps{flex:1"),
    ("step numbering fix", "content:attr(data-n)"),
    ("print hides the reasoning", ".why,.why.open,.whybtn"),
    ("print forces all steps", ".step{display:block !important}"),
    ("Letter page size", "@page{size:Letter"),
    ("text-size-adjust", "-webkit-text-size-adjust"),
    ("prefers-reduced-motion", "prefers-reduced-motion"),
)

# Sitemap core locs before /guides/{slug}.html.
# Entry paths come from ENTRY_ROUTES; order is published/sitemap order — keep stable.
_ENTRY_PAGE_BY_SLUG = {route.slug: f"/{route.page}" for route in ENTRY_ROUTES}
SITEMAP_CORE_PATHS: tuple[str, ...] = (
    "/",
    "/index-parents.html",
    "/partners.html",
    _ENTRY_PAGE_BY_SLUG["first-night"],
    _ENTRY_PAGE_BY_SLUG["one-room"],
    _ENTRY_PAGE_BY_SLUG["guests"],
    _ENTRY_PAGE_BY_SLUG["underwater"],
    "/first-place.html",
    "/privacy.html",
    "/guides/",
    "/print/",
)


def public_url(path: Path, site_root: Path) -> str:
    """Absolute public URL for a file under the built site root (_site)."""
    rel = path.relative_to(site_root)
    if rel.name == "index.html":
        parent = rel.parent.as_posix()
        suffix = "/" if parent == "." else f"/{parent}/"
    else:
        suffix = f"/{rel.as_posix()}"
    return ORIGIN + suffix


def entry_social_images() -> dict[str, str]:
    """Entry + completion page → share PNG filename."""
    images: dict[str, str] = {}
    for route in ENTRY_ROUTES:
        images[route.page] = route.share_image
        images[route.completion_page] = route.share_image
    return images


def completion_pages() -> list[tuple[str, str, str, str, str]]:
    """Tuples matching former COMPLETION_PAGES shape."""
    return [
        (
            route.completion_page,
            route.door_title,
            route.completion_message,
            route.slug,
            route.back_path,
        )
        for route in ENTRY_ROUTES
    ]


def sitemap_core_urls() -> list[str]:
    return [ORIGIN + path for path in SITEMAP_CORE_PATHS]
