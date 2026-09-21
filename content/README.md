# Content

Teaching content, organized by life domain. This is the **raw material** of the
business.

## Content vs. Products

- **`content/`** — reusable teaching material, written once, organized by domain.
  One piece of content can feed several products.
- **[`products/`](../products/)** — that material assembled and packaged into
  something a customer downloads or buys.

A product should rarely contain teaching that doesn't exist here first. Write the
content, then package it.

## Organization

This directory is intentionally **flatter** than the full taxonomy in
[`frameworks/life-domains.md`](../frameworks/life-domains.md) — it groups by
where someone would look, not by conceptual purity.

| Directory | Domains covered |
|---|---|
| `home/cleaning/` | Cleaning routines, supplies, standards, cadences |
| `home/kitchen/` | Food, cooking, pantry, kitchen systems |
| `home/organization/` | Setup, storage, decluttering, where things live |
| `home/hospitality/` | Hosting, guests, gatherings |
| `personal/routines/` | Daily, weekly, seasonal rhythms |
| `personal/time-management/` | Calendar, tasks, planning, review |
| `personal/digital-life/` | Files, email, passwords, backups, photos |
| `personal/personal-admin/` | Paperwork, documents, renewals, vehicles |
| `money/` | Accounts, bills, budgeting, insurance, taxes |
| `work/` | Task systems, boundaries, career admin |
| `relationships/` | Household agreements, friendship, conflict |
| `life-transitions/` | Moving, marriage, starting over |

**Not yet represented:** Health, and Maintenance as a standalone directory.
Both are folded in for now. Don't create a directory until there's content for
it — empty structure is a promise the project hasn't kept.

## Writing standards

Every piece of content should:

1. **Be specific.** Names, numbers, cadences, steps. Not "clean regularly" but
   "weekly, and here's the order."
2. **Explain the why, briefly.** Reasoning transfers; rules don't.
   ([principles.md](../docs/vision/principles.md) §10)
3. **Give the good-enough standard and the ideal**, and say which is fine. This
   builds trust faster than anything else.
4. **Never condescend.** The premise is that nobody taught them. §8.
5. **Trace to a real problem** in
   [customer-problems.md](../docs/research/customer-problems.md).
6. **Be modular.** Assume it will be reused in three products and read out of
   order.

## Email voice: write full sentences

**Emails must sound spoken, not written.** The recurring failure is dropping the
subject and verb to make a clipped fragment. It reads as stylish on a page and as
contrived in an inbox, and it is the single most reliable tell that a machine
wrote it.

| Contrived | Say it like a person |
|---|---|
| Nothing attached to this one. | There's nothing attached to this one. |
| The page you just used, as one sheet you can keep. | Here's a one-page version of the guide you just used. |
| Now tomorrow. | Now, about tomorrow. |
| Four minutes, most nights. | It takes about four minutes most nights. |
| Not "somewhere for now." Its actual place. | Not "somewhere for now." I mean the place it's actually going to live. |

Three habits to watch, all of them mine:

1. **Subjectless fragments.** If a sentence has no subject, say it out loud. If
   you wouldn't say it that way, write it out.
2. **The em-dash appositive.** *"…turn into next month's project — which is the
   only reason tonight was ever necessary."* One per email at most. A plain
   "which" or a new sentence usually reads better.
3. **Eliding the connective.** People say "So," "And," "But," and "Now." Writing
   drops them to sound tighter; speech keeps them.

**This applies to emails, not to the guides.** On a printed checklist a fragment
is a label and it works — *"Bin out. Window open."* is correct there. In an inbox
the same construction sounds like a robot. Different register, different rules.

## US English, throughout

**The beachhead is American. Everything reader-facing is written in US English** —
spelling, vocabulary, currency and units. Decided 2026-09-20 after British idiom
turned up across the free tier.

| Not this | This |
|---|---|
| colour, apologise, grey, realise | color, apologize, gray, realize |
| bin | trash, trash can |
| tap | faucet |
| flat | apartment, place |
| post | mail |
| cupboard | cabinet, pantry |
| boot (of a car) | trunk |
| rubbish | trash, garbage |
| £, pounds | $, dollars |
| hob, cooker | stove, range |
| tidy-up (noun) | cleanup |

**The exception is [`source-material/`](../source-material/), which is never
touched.** Dave's documents are verbatim primary source, including his spelling,
his punctuation and his typos. Americanizing a quotation would be falsifying it.

## Referring to Dave

**He is "Dave." Not "Dave Webster."** The surname adds no credibility and reads
as a claim being made for him. The first name reads as a friend, which is what
he is — and the whole premise of the brand is that this knowledge comes from
someone who'd tell you over a coffee, not from an authority.

**Say "decades," not a number of years.** We happen to hold documents going back
to 2009, but that's the age of our archive, not the age of his practice. "Decades"
is both truer and more interesting than counting.

**Where he appears in a product, he appears after the reader has done something**,
never as onboarding. Provenance is a reward; it is not an introduction. See
[ADR-015](../planning/decisions.md#adr-015--the-win-comes-before-the-email).

## Scope: how deep is too deep

**If someone would have to look it up in a code book or a database, it's not our
content.** We teach what a competent person would just *tell* you — the things
that never got said, not the things that are hard to find.

| Ours | Not ours |
|---|---|
| "Clean the lint trap every load — it's a fire risk" | Fire code citations and replacement intervals |
| "Check your owner's manual for oil changes" | Comparative oil-change interval research |
| "Don't mix bleach and ammonia" | Chemistry |
| "Wipe the counter while the pan's still hot" | — |

The test: **would Dave say this, standing in someone's kitchen?** If it needs
research to state, it's the wrong depth. Nobody is buying technical reference
from us, and pretending otherwise makes the material heavier and less useful.

Simple and effective is the product. Thorough is a different business.

## File conventions

- One topic per file, `kebab-case.md`
- Start with a one-line summary of what the reader will be able to do
- Tag the primary domain and any secondary domains at the top
- Prefer short files over long ones; link rather than repeat

## Status

Empty. Content production begins in Phase 2 of the
[roadmap](../planning/roadmap.md). Priorities are in
[backlog.md](../planning/backlog.md).
