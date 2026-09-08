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
