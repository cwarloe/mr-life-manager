# Products

Packaged deliverables — the things customers download, buy, or are given.

## Products vs. Content

[`content/`](../content/) is the teaching material. `products/` is the packaging.
A product is an *assembly* of content aimed at one audience with one promise.

The same content appears in many products. That's the point: write once at high
quality, package many times. See
[product-ladder.md](../docs/business/product-ladder.md).

## Directories

| Directory | What lives here |
|---|---|
| `checklists/` | One- to four-page printable checklists. Free tier and $9 tier. |
| `worksheets/` | Fill-in templates: agreements, calendars, planners, inventories. |
| `ebooks/` | Multi-chapter guides, starting with the flagship, *First Place* (not yet written). |
| `courses/` | Structured multi-module programs, text or video. |
| `toolkits/` | Bundled systems — several artifacts solving one situation end to end. |
| `landing/` | The public site: router homepage, entry pages, email sequences. See [SETUP.md](landing/SETUP.md). |
| `print/` | One-page printables with no web version (*The Week*). |
| `guides-pdf/` | Rendered PDFs, published at `/print/`. Never edit; regenerate from the HTML. |

## Every product needs a brief

Before building anything, write a `brief.md` in its directory answering:

1. **Who** is this for? Name the persona from
   [target-audiences.md](../docs/vision/target-audiences.md).
2. **What problem** does it solve? Link to
   [customer-problems.md](../docs/research/customer-problems.md).
3. **What outcome** does it produce? Which rung of
   [customer-outcomes.md](../docs/vision/customer-outcomes.md), and which specific
   quote should this make true?
4. **Which domains** does it cover?
   ([life-domains.md](../frameworks/life-domains.md))
5. **Which principles** does it serve?
   ([principles.md](../docs/vision/principles.md))
6. **Where on the ladder** does it sit, and what comes before and after it?
7. **What content** does it draw on, and what's missing?
8. **What's the price**, and why that price?

If you can't answer all eight, the product isn't ready to build.

## Design standards

- **Print-friendly.** Much of this gets taped inside a cabinet door. Design for
  black-and-white at 8.5×11.
- **Clear over pretty.** Instructional design, not lifestyle photography.
- **Standalone.** Assume the reader has seen nothing else.
- **Licensable.** Build every product so it *could* be licensed to an institution:
  modular, brandable, printable.

## Status

As of 2026-09-24. Nothing is for sale, and nothing has been tested with a real
reader. Under [ADR-015](../planning/decisions.md#adr-015--the-win-comes-before-the-email)
the front door is a per-pain entry page; the guides are archive and search
surface, not offers.

- **Entry pages** — four, live: [first night](landing/first-night.html) ·
  [someone's coming over](landing/guests.html) ·
  [just underwater](landing/underwater.html) ·
  [the room that became storage](landing/one-room.html). Each has a completion
  page and its own [sequence](landing/emails/). Routes are in
  [SETUP.md](landing/SETUP.md).
- **Guides** — eight, at `/guides/`: seven [checklists](checklists/) and the
  [Household Agreement](worksheets/household-agreement/) worksheet.
- **Printables** — [`guides-pdf/`](guides-pdf/), at `/print/`: one PDF per guide,
  [*The Week*](print/the-week.html) (what every sequence sends), and the
  partner-pilot handouts.
- **Paid** — none. [`first-place.html`](landing/first-place.html) takes
  no-charge reservations for a planned $39 founding offer.
- **Empty:** [ebooks](ebooks/), [courses](courses/), [toolkits](toolkits/).
