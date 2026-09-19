# Commerce Rules

**Status:** Adopted 2026-09-19.
**Scope:** All product recommendations, affiliate links, upsells, and pricing —
site-wide. Written against the Cleaning Supply Starter List; it is the template
for everything that follows.

Governed by [ADR-014](../../planning/decisions.md#adr-014--completion-is-what-converts)
and [principle 11](../vision/principles.md). Where any rule below conflicts with
*completion is what converts*, completion wins.

---

## Purpose

Help a first-time independent adult buy only what they need, at a sensible
price, **with as little decision-making as possible.**

Monetization is secondary to usefulness and trust. The promise: start with a
small, practical kit. Add an upgrade only when it removes a specific recurring
frustration.

> **The decision rule.** If a recommendation makes the reader's life simpler,
> costs them fairly, and is something Mr. Life Manager would recommend with no
> affiliate program attached, it belongs on the page. If it exists mainly to
> create a commission opportunity, it does not.

---

## The freemium ladder

| Tier | What | Why |
|---|---|---|
| **Free — one guide** | Chosen by a question about their situation, not a menu | Extreme value, no overwhelm, immediate action |
| **$9–19 — checklists** | Action-oriented start to finish. They know it's worth it. | They pay, they buy what it says, they're done and moving |
| **Next $9–19** | Same price, next problem, when they want more direction | Repeat purchase at the same trust level |
| **Higher** | Only when they need real help and guidance, and know they do | Never an upsell they didn't ask for |

**One free guide, not six.** Everything stays public at `/guides/` for search
and sharing — *public* and *offered* are different decisions — but the funnel
hands over exactly one.

**A paid product must add organization, instruction, and decision reduction.**
Never a repackaging of links that are already free.

---

## Non-negotiable product rules

1. **Recommend the fewest products that solve the job.** The baseline is the
   existing "nine things, not forty."
2. **Prefer simple, lightly-scented or unscented products.** Don't recommend a
   scented cleaner because it is popular, available, or pays a commission —
   *and don't send anyone hunting for a certified-fragrance-free premium product
   either.* Get something that works, don't buy the heavily-perfumed one, move on.
3. **Avoid** novelty products, specialty cleaners, bundles, "premium natural"
   branding, subscription pressure, and anything whose main feature is fragrance.
4. **No separate product per room or surface** unless a general product has
   demonstrably failed, or the surface manufacturer requires special care.
5. **Disinfecting is not routine cleaning.** Cleaning is the normal job;
   disinfection is situational.
6. **Never recommend mixing cleaning chemicals.** Keep the safety warning
   prominent: one product at a time, rinse between, ventilate.
7. **Never recommend vinegar on natural stone** or other surfaces where an acid
   is inappropriate. Point to the manufacturer's care guidance.
8. **Prefer durable, reusable tools** where they reduce waste or repeat expense
   — microfiber especially.
9. **Don't claim "best"** without current, checkable evidence and stated
   criteria. Prefer "recommended default" or "good basic option."
10. **Never invent, infer, or repair a product URL.** A link must be verified
    against the actual retailer page before publication.

### Link availability never changes the advice

If a product cannot be verified, **the teaching still says buy one.** Only the
*link* is conditional.

A toilet needs cleaning whether or not we found a linkable bowl cleaner. Say so,
and tell the reader to grab the simplest option locally. Never let the
link-checking process quietly edit what we tell people they need.

---

## Link rules

1. **Every affiliate link resolves to the exact product named** — not a search
   result, category page, different size, different scent, marketplace
   substitute, or anything else.
2. **No search links in the action path.** A search is a choice, and choice is
   the thing we are removing. *Click here, done, go.* Sending someone to research
   and select re-creates the paralysis the page exists to prevent.
3. **Record in a source-of-truth file:** product name, retailer, URL, size/count,
   fragrance status, price, date checked, and reason for inclusion.
4. **Re-check before publishing or refreshing**: still available? formula, scent,
   size, or seller changed?
5. **No unverified prices.** "Price varies," or omit the item until verified.
6. **Prices are temporary.** A specific price beside a buy link carries a
   "checked [date]" note. *Approximate ranges used for orientation — "$4–6" — are
   not prices and carry no date*; they are there so someone knows roughly what to
   expect, and they age gracefully.
7. **Prefer retailer-sold or retailer-fulfilled** over unknown third-party
   marketplace listings when a mainstream equivalent exists.
8. **Don't substitute a fancier product to fill a category.** Say it's omitted,
   or tell them to buy the simplest option locally.
9. **Don't use reviews, AI retail summaries, or search snippets as evidence**
   about a formula when the label or manufacturer description can be checked.

---

## Maintenance cadence

Link rot is continuous. A policy with no maintenance schedule is off-brand for a
project built on *preventative beats crisis*.

| Check | Cadence | Who |
|---|---|---|
| **Link availability** — does every URL still resolve? | **Weekly, automated** in CI | Machine |
| **Recommendation review** — is this still the right product? Formula changed? Better option now? | **Quarterly** | Human |

Automated first, deliberately. A person manually checking links every two weeks
is a person doing a machine's job — which is exactly what this brand tells people
not to do.

**When a link breaks: pull it immediately.** Do not wait for a replacement. A
dead link on a page whose credibility is its accuracy costs more than a missing
one.

---

## Basic kit

The basic kit is a **trust product**. It helps the reader begin cheaply and
confidently; it does not maximize commission.

**Core low-cost path** — dish soap · baking soda · distilled white vinegar ·
microfiber cloths

**Standard path adds only** — all-purpose cleaner · non-scratch scrub sponges ·
laundry detergent · a toilet bowl cleaner and brush

Dedicated glass cleaner stays **optional**; a damp microfiber is the default.
Never add a glass-cleaner link just to make the kit feel complete.

**No "full kit" that forces every possible item.** A low-cost starting point, and
a clear checklist for shopping in person.

---

## Retailer strategy

1. Value retailer for basic consumables where it's a clear price/value win.
2. Whichever retailer suits optional tools, where availability, delivery, or
   quality matters on a higher-ticket item.
3. **Retailer choice is decided by shopper value first** — total cost, shipping
   or pickup, availability, ease of buying the whole list.
4. **Commission may break a tie** between equivalent options. It may never
   override a materially worse product or price for the reader.
5. Keep retailer-specific checklists separate where availability differs. **Never
   claim a one-click bundle exists unless the retailer actually supports it.**

---

## Monetization

1. **Trust compounds; a small commission does not.** Never expand a list to
   increase basket size.
2. **Take no commission on basic consumables.** Two dollars on a $30 chemicals
   run is not worth the integrity exposure — and skipping it removes the
   incentive to distort advice on exactly the products the guides are built
   around. *The daily consumables pay nothing, so there is nothing to distort.*
3. **Commission lives on optional durable equipment** — brooms, mops, vacuums,
   organization tools. Higher order value, genuinely useful, and already labeled
   optional.
4. **The real revenue is our own digital products** — checklists, room-by-room
   routines, move-in systems, maintenance calendars, first-apartment packs.
5. **Track** clicks, conversions, refunds, reader questions, recurring problems.
   Remove anything that creates confusion or poor outcomes **even if it converts.**

---

## Upsells

Upsells are optional **friction removers**, never requirements. They sit after
the basic kit, labeled "Make it easier" or equivalent.

Each must answer three questions:

1. What specific problem does it solve?
2. Why is the basic kit insufficient for that problem?
3. Why is this a reasonable default rather than a needless upgrade?

**Approved** — shower squeegee (recurring soap scum; prevention) · flat spray mop
(avoids bucket mopping, hard floors) · handheld vacuum (crumbs, hair, fast
messes) · extendable duster (fans, vents, high corners) · caddy or under-sink
organizer (supplies where they're used) · better vacuum (**only** once they know
their floor type, pet needs, storage, and usage)

**Not approved as defaults** — robot vacuums, steam mops, scented refills,
specialty sprays, bulk cleaner packs, decorative gadgets, duplicates that solve
no named problem.

**Never "buy all upgrades."** The call to action is "See options" or "Consider
this if [specific problem]."

---

## Affiliate disclosure

1. Plain-language disclosure **immediately before or beside** the links.
2. Suggested wording: *"Some links may earn Mr. Life Manager a commission, at no
   extra cost to you. We recommend items because they solve a real problem, not
   because they pay the highest commission."*
3. Amazon links carry the required statement: *"As an Amazon Associate I earn
   from qualifying purchases."*
4. Mark individual links "paid link" or "affiliate link" where the program or law
   requires.
5. **Never hide a disclosure** in a footer, terms page, tooltip, or vague wording.
6. Follow each program's current operating agreement and link-format rules.

---

## Page design

1. **Teach first; sell second.**
2. The free core checklist is visibly complete **without requiring any click.**
3. Page order: basics → purchase path → optional upgrades → safety → storage and
   routines.
4. **No affiliate links inside the safety warning** or the core teaching, and
   never placed so an optional item looks required.
5. No price claims beside affiliate upgrades unless a process keeps them current.
   Use "See options."
6. Label by **use and problem**, not brand alone.

---

## Publication checklist

Before publishing or updating any recommendation:

- [ ] Simple, not heavily scented
- [ ] The URL resolves to the exact product
- [ ] Size, count, scent, seller and price checked
- [ ] Solves a real job or friction point
- [ ] Not a duplicate of something already listed
- [ ] Safety limits stated
- [ ] Disclosure visible and correct
- [ ] **Would remain defensible if no commission existed**
- [ ] **Offers one action, not a menu** ([ADR-014](../../planning/decisions.md#adr-014--completion-is-what-converts))
