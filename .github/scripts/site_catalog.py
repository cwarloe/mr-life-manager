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

# Umami Cloud (privacy-first analytics with custom events; chosen 2026-10-26,
# see planning/operations.md). Leave the ID empty and nothing is loaded or sent.
# To turn tracking on, paste the website ID from the Umami dashboard here.
UMAMI_WEBSITE_ID = "8aaa8b83-1a8f-431b-bd34-aceacf26f3a5"
UMAMI_SCRIPT_URL = "https://cloud.umami.is/script.js"
ANALYTICS_DOMAIN = "mrlifemanager.com"


@dataclass(frozen=True)
class EntryRoute:
    slug: str
    door_title: str
    completion_message: str
    share_image: str
    email_signup: bool = True
    next_url: str = ""
    next_title: str = ""
    next_description: str = ""

    @property
    def collects_email(self) -> bool:
        return self.email_signup

    @property
    def page(self) -> str:
        return f"{self.slug}.html"

    @property
    def completion_page(self) -> str:
        return f"finished-{self.slug}.html"


# Keep drafted routes here even while publication is paused.
ALL_ENTRY_ROUTES: tuple[EntryRoute, ...] = (
    EntryRoute(
        slug="first-night",
        door_title="I just moved in and it's my first night here.",
        completion_message=(
            "You handled the things that cost most to miss on a first night."
        ),
        share_image="first-night.png",
    ),
    EntryRoute(
        slug="one-room",
        door_title="There's a room I stopped using.",
        completion_message=(
            "You cleared one zone of the room, and you can use it again. One finished zone is real progress."
        ),
        share_image="one-room.png",
    ),
    EntryRoute(
        slug="guests",
        door_title="Someone's coming over and the place isn't ready.",
        completion_message=(
            "You're ready for them. Whatever did not get done can wait."
        ),
        share_image="guests.png",
    ),
    EntryRoute(
        slug="underwater",
        door_title="Your place is a mess. Again.",
        completion_message=(
            "The house is livable again. That is different from fixing everything."
        ),
        share_image="underwater.png",
    ),
    EntryRoute(
        slug="dinner",
        door_title="Dinner's ready. There's nowhere to eat.",
        completion_message="You made room to sit down and eat. Enjoy the meal. The basket can wait until after dinner.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="laundry-pile",
        door_title="All my clean clothes are still in a pile.",
        completion_message="One basket is empty, the clothes have homes, and tomorrow's outfit is ready.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="make-dinner",
        door_title="It's dinnertime. I don't know what to make.",
        completion_message="You made and served a meal from beans and tortillas.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="cleaning-start",
        door_title="I don't know what to use to clean this.",
        completion_message="One kitchen work surface is ready to use, and its cleaning supplies have a known home.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="comfortable-room",
        door_title="This room is clean. I still don't want to sit in it.",
        completion_message="One seat has useful light, somewhere reachable to put an item, and room to sit comfortably.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="kitchen-close",
        door_title="I wake up to yesterday's kitchen mess.",
        completion_message="Breakfast dishes and one usable working patch are ready for morning.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="shared-dishes",
        door_title="We keep arguing about the dishes.",
        completion_message="Both people accept a written owner, a clear finish standard, and a first deadline for the dishes.",
        share_image="home.png",
        email_signup=False,
    ),
    EntryRoute(
        slug="office",
        door_title="Clear your desk",
        completion_message=(
            "You cleared one surface at work. One finished desk is real progress."
        ),
        share_image="office.png",
    ),
)


# Charles's active five, in public picker order. Paused source files stay intact.
ACTIVE_ENTRY_SLUGS = ("first-night", "guests", "dinner", "underwater", "one-room")
_ROUTES_BY_SLUG = {route.slug: route for route in ALL_ENTRY_ROUTES}
ENTRY_ROUTES = tuple(_ROUTES_BY_SLUG[slug] for slug in ACTIVE_ENTRY_SLUGS)
PAUSED_ENTRY_ROUTES = tuple(route for route in ALL_ENTRY_ROUTES if route.slug not in ACTIVE_ENTRY_SLUGS)
PAUSED_LANDING_PAGES = (
    *(route.page for route in PAUSED_ENTRY_ROUTES),
    *(route.completion_page for route in PAUSED_ENTRY_ROUTES),
    "organizing-ideas.html",
)

# Needles check_entry_pages looks for in the shared entry.js / entry.css.
ENTRY_JS_MARKERS: tuple[tuple[str, str], ...] = (
    ("doing-mode", "classList.add('doing')"),
    ("source attribution handoff", "new URLSearchParams(window.location.search).get('from')"),
    ("MailerLite dual-field tag", "fields[guide]"),
    ("MailerLite fallback", "ml-fallback"),
    ("guide VALUE wiring", "var VALUE = guide"),
    ("deferred appointment (ADR-021)", "BEGIN:VCALENDAR"),
    ("deferred move cap", "MAX_MOVES"),
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
    "/privacy.html",
    "/guides/",
    "/print/",
)


# Built-site and live-site page markers (exact strings used by the checkers).
# Do not invent new copy here.
PARTNERS_BUILT_MARKERS: tuple[str, ...] = (
    "Pilot it with five",
    "data-source-link",
    "Five-person pilot",
    "new URLSearchParams",
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
    "whole house needing work",
    "room that became storage",
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
    names = {"home.png", "partners.png"}
    names.update(entry_social_images().values())
    return tuple(sorted(names))


def sitemap_core_urls() -> list[str]:
    return [ORIGIN + path for path in SITEMAP_CORE_PATHS]
