#!/usr/bin/env python3
"""Single source for public origin, URL helper, and the entry routes.

Guide/printable inventories live elsewhere — do not fold them in here.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ORIGIN = "https://mrlifemanager.com"
MAILERLITE_FORM_ID = "00ZwEr"
MAILERLITE_FORM_ATTR = f'data-form="{MAILERLITE_FORM_ID}"'
MAILERLITE_JS_URL = "https://assets.mailerlite.com/js/universal.js"


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


# Entry routes in homepage picker order; the sitemap lists them in this order.
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
        slug="one-room",
        door_title="The room that became storage",
        completion_message=(
            "You reclaimed a usable part of the room. One finished zone is real progress."
        ),
        share_image="one-room.png",
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
        slug="office",
        door_title="The office that got away from you",
        completion_message=(
            "You cleared one surface at work. One finished desk is real progress."
        ),
        share_image="office.png",
    ),
)


# Needles check_entry_pages looks for in the shared entry.js / entry.css.
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

# Sitemap core locs before /guides/{slug}.html. Entry pages follow ENTRY_ROUTES.
SITEMAP_CORE_PATHS: tuple[str, ...] = (
    "/",
    "/index-parents.html",
    "/partners.html",
    *(f"/{route.page}" for route in ENTRY_ROUTES),
    "/first-place.html",
    "/privacy.html",
    "/guides/",
    "/print/",
)


# Built-site and live-site page markers (exact strings used by the checkers).
# Do not invent new copy here.
FIRST_PLACE_BUILT_MARKERS: tuple[str, ...] = (
    "mailto:hello@mrlifemanager.com?subject=First%20Place%20%2439",
    "planned founding price",
    "No charge today",
    "Reserve the $39 founding version",
    "How I found this:",
)
FIRST_PLACE_LIVE_MARKERS: tuple[str, ...] = (
    "First%20Place%20%2439%20founding%20reservation",
    "Reserve the $39 founding version",
    "planned founding price",
)
PARTNERS_BUILT_MARKERS: tuple[str, ...] = (
    "Pilot it with five",
    "data-source-link",
    "Five-person pilot",
    "new URLSearchParams",
    "/first-place.html?from=partner",
)
PARTNERS_LIVE_MARKERS: tuple[str, ...] = (
    "Pilot it with five",
    "data-source-link",
    "Five-person pilot",
    "/print/partner-pilot.pdf",
)
PRIVACY_BUILT_MARKERS: tuple[str, ...] = (
    "The Week",
    "MailerLite stores",
    "just underwater",
    "room that became storage",
    "founding reservation",
)
PRIVACY_LIVE_MARKERS: tuple[str, ...] = (
    "MailerLite stores",
    "The Week",
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


def required_share_images() -> tuple[str, ...]:
    """All share PNG filenames that must exist under assets/share/."""
    names = {"home.png", "first-place.png", "partners.png"}
    names.update(entry_social_images().values())
    return tuple(sorted(names))


def sitemap_core_urls() -> list[str]:
    return [ORIGIN + path for path in SITEMAP_CORE_PATHS]
