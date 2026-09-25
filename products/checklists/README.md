# Checklists

Printable checklists. The **free tier** and the **$9 tier** of the
[product ladder](../../docs/business/product-ladder.md).

## Why checklists matter more than their price suggests

- **Cheapest possible validation.** A checklist takes a day to make. If nobody
  wants it, you learned that for a day instead of three months.
- **The best lead magnets available.** Complete, immediately useful, and easy to
  share.
- **Highly shareable.** People forward a good checklist. They don't forward an
  ebook.
- **They're what people search for.** "First apartment checklist" is a real,
  high-volume query.

## Planned

**Free**
- ★ ✓ **First Apartment Checklist** — the flagship lead magnet
- ✓ **What Is This Room For?** — one room: its job, what fights it, three things
- ✓ **The Light Is the Problem** — why a room feels wrong when nothing is dirty
- ✓ **Cleaning Supply Starter List**
- The 20-Minute Reset
- ✓ **How Often Should I…?** — the cadence reference
- Move-Out Checklist

**Paid ($9)**
- Room-by-room setup checklists
- Seasonal maintenance checklists
- Hosting checklist
- Moving checklist (complete)

## Standards

**The design standard, per [ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email):
one action, roughly a dozen decisions at most, and "done" reachable in a single
sitting.** A guide that presents a menu has moved the analysis paralysis inside
the product instead of removing it. *What Is This Room For?* shipped with 76 tick
boxes and is the worked example of getting this wrong; it was cut to 13 on
2026-09-20.


- **Genuinely complete.** A checklist with gaps is worse than none — it produces
  false confidence.
- **Printable, black-and-white, 8.5×11.** Much of this gets taped inside a
  cabinet door.
- **No upsell in the body.** A free asset that's really a sales pitch poisons the
  whole ladder, especially for an audience whose core wound is being talked down
  to.
- **Checkable items.** Every line is a discrete, completable action.
- **Ordered.** Sequence is most of the value.

Write a `brief.md` before building — see [../README.md](../README.md).

## Status

**Seven designed, none reviewed or reader-tested.** Each printable `.html` is the
source of truth; its `brief.md` holds intent and open questions.
Per [ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email)
they are archive and search surface at `/guides/`, not offers.

| Guide | State | Next step |
|---|---|---|
| [First Apartment Checklist](first-apartment/) | Draft 1, designed | Read by someone who moved recently |
| [How Often Should I…?](how-often/) | Draft 1, designed, safety rows checked | Second pass on the non-safety rows |
| [Cleaning Supply Starter List](cleaning-supplies/) | Draft 1, designed | Price-check the ranges |
| [What Is This Room For?](room-for/) | Designed 2026-09-20 | See its brief |
| [The Light Is the Problem](light/) | Designed 2026-09-20 | See its brief |
| [Laundry, Solved](laundry/) | Designed 2026-09-18 | See its brief |
| [Ten Meals and a Stocked Kitchen](ten-meals/) | Designed 2026-09-18 | See its brief |

They share one system: Archivo for mechanics, Source Serif for the teaching
voice, blueprint blue for structure, amber spent only where money or safety is
at stake. Each footer carries the
[ADR-013](../../planning/decisions.md#adr-013--licensing-revised-free-to-use-never-free-to-sell)
permission line, so the licensing decision travels on the asset.

They are **source material for `content/`**, not the reverse — sections should
be extracted back into it once proven.
