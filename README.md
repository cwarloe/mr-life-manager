# Mr. Life Manager

**Practical adult-life systems for people who were never explicitly taught them.**

---

## What this is

Mr. Life Manager teaches the practical systems of adulthood that people were
expected to know but were never actually taught.

Most people learn to run a home and a life by osmosis — by watching a parent,
or by failing repeatedly until something sticks. That works unevenly. Plenty of
capable, intelligent adults have never been shown how to keep a kitchen from
becoming a crisis, how to build a laundry rhythm, how to track a bill, how to
maintain a car, or how to make a home ready for guests without a two-day panic.

This is not a moral failing. Nobody handed them the manual. Mr. Life Manager is
the manual.

The idea began with household cleaning and organization guidance, and cleaning
remains an excellent entry point — it is visible, urgent, and immediately
rewarding. But **this is not a cleaning brand.** Cleaning is the door. The house
is life management: home, food, money, time, work, relationships, digital life,
paperwork, maintenance, hospitality, and transitions.

## Who Mr. Life Manager is

**Mr. Life Manager is Dave Webster — a real person**, not a persona. He is the
one who actually knew how to run a home and taught it. This project is written
by **the apprentice**: the one who learned it, wrote it down, and is passing it
on.

That structure matters more than it sounds. The reader gets the apprentice's
seat — not lectured by an authority, but handed what someone else had to be
taught. Which is the point, since the barrier here is embarrassment.

Dave's own view of the material is worth quoting, because it is the whole thesis:

> He says it's all obvious, and he's embarrassed to tell people things he assumed
> they already knew.

**That is why nobody was taught this.** Not indifference — invisibility. The
people who know it can't see it as knowledge. See
[ADR-011](planning/decisions.md#adr-011--mr-life-manager-is-a-real-person-dave-webster).

## Who it is for

**Anyone who was never explicitly taught how to run a home and a life.**
First-time independence is the sharpest expression of that need — students
leaving dorms, young adults on their own, newlyweds — but it is not the whole of
it. Plenty of people have been running a household for a decade and never had
these systems either.

**Who the marketing addresses and who pays is a separate question**, settled in
[ADR-010](planning/decisions.md#adr-010--beachhead-keep-the-audience-change-the-payer):
competitive research found that every commercial success in this space sells to
the adult already running a household and overwhelmed by it, while every attempt
to sell to the 22-year-old directly underperformed or failed. So the content
serves first-timers; the *ask* goes to the overwhelmed householder, a parent
buying a gift, or an institution licensing.

See [`docs/vision/target-audiences.md`](docs/vision/target-audiences.md) for the
personas, and
[`docs/research/competitor-notes.md`](docs/research/competitor-notes.md) for the
evidence.

## The problem it solves

People without systems live in **reaction**. Everything is urgent because
nothing was handled early. The dishes become a project. The bills become a
scramble. The car becomes a repair bill. The apartment becomes a place you
apologize for instead of a place you invite people into.

The cost isn't just mess. It's decision fatigue, low-grade shame, wasted money,
strained relationships, and attention that never gets spent on anything that
matters.

Mr. Life Manager replaces reaction with **light, repeatable systems** — so that
the right action is the easy action, and the crisis mostly never arrives.

## Initial product direction

The first flagship product is planned as:

> **First Place: The Practical Guide to Running Your First Home**

A structured, room-by-room, domain-by-domain guide for someone setting up and
running their own place for the first time — supplies, setup, routines,
maintenance calendar, money basics, and hosting.

Ahead of it: a free lead magnet (**First Apartment Checklist**) to validate the
audience and build a list. Behind it: a product family of checklists, toolkits,
courses, and eventually coaching or consultation.

See [`planning/roadmap.md`](planning/roadmap.md).

## The major life domains

Home · Food · Money · Time · Health · Work · Digital Life · Relationships ·
Transportation · Maintenance · Paperwork & Admin · Hospitality · Life Transitions

Defined in [`frameworks/life-domains.md`](frameworks/life-domains.md).

## Core frameworks

| Framework | Idea |
|---|---|
| [Everything Has a Place](frameworks/everything-has-a-place.md) | Every object, task, document, dollar, and responsibility has one defined home. |
| [Do It Now](frameworks/do-it-now.md) | A decision rule — do, schedule, delegate, or discard — not a command to do everything immediately. |
| [Preventative vs. Crisis](frameworks/preventative-vs-crisis.md) | Small scheduled effort beats large forced effort, across every domain. |
| [Remove the Excuse](frameworks/remove-the-excuse.md) | A prep list's job is closing off the reasons a person will stop, not gathering supplies. |
| [Life Domains](frameworks/life-domains.md) | The taxonomy that organizes all content and products. |

## Repository structure

```
mr-life-manager/
├── README.md
├── LICENSING-NOTES.md       Licensing: free to use, never free to sell
├── PERMISSIONS.md           Plain-language "what you can do with this"
├── docs/
│   ├── vision/              Mission, principles, outcomes, audiences
│   ├── business/            Model, product ladder, positioning, revenue
│   └── research/            Customer problems, competitor research plan
├── content/                 Teaching content, organized by life domain
│   ├── home/                cleaning · kitchen · organization · hospitality
│   ├── personal/            routines · time-management · digital-life · personal-admin
│   ├── money/  work/  relationships/  life-transitions/
├── products/                Packaged deliverables
│   ├── ebooks/ checklists/ worksheets/ courses/ toolkits/
├── frameworks/              The durable conceptual models
├── source-material/         Original, unedited source notes
└── planning/                Roadmap, backlog, decision log
```

**`content/` vs `products/`** — `content/` is the raw teaching material,
organized by life domain and written to be reusable. `products/` is where that
material gets assembled into something a customer buys or downloads. One piece
of content may appear in several products; a product should rarely contain
teaching that doesn't exist in `content/`.

**`frameworks/` vs `docs/vision/principles.md`** — `principles.md` states what
we believe. `frameworks/` explains how to actually apply a belief. Principles
are short; frameworks are working models.

**`source-material/`** holds original notes verbatim. Derived work never
overwrites it. See
[`source-material/original-charles-cleanup-notes.md`](source-material/original-charles-cleanup-notes.md).

## Current status

**Pre-launch validation stage.** The free funnel exists; the next job is to
verify it and learn from real people.

- ✅ Concept, audiences, principles, and frameworks drafted
- ✅ Competitive research done — three independent passes, acceptance test passed
      ([findings](docs/research/competitor-notes.md#findings))
- ✅ Foundational decisions settled: faith framing, beachhead and payer, the
      person behind the brand, and the intended licensing model
      ([decision log](planning/decisions.md))
- ✅ Eight free-tier guides drafted and designed — see
      [`products/checklists/`](products/checklists/). They are now **archive and
      search surface, not offers** ([ADR-015](planning/decisions.md#adr-015--the-win-comes-before-the-email))
- ✅ **Dave's original documents recovered** — four guides he wrote in 2009–2010,
      plus the 2023 re-send and the 2019 thread where the name was coined. The
      frameworks are documented rather than reconstructed
      ([`source-material/`](source-material/INVENTORY.md))
- ✅ **Funnel rebuilt around the win, not the email** — the main page routes to
      per-pain entry pages; the action is free and ungated; signup comes after
      ([ADR-015](planning/decisions.md#adr-015--the-win-comes-before-the-email),
      [ADR-016](planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally))
- ✅ Four entry pages live, each with its own sequence drafted —
      [first night](products/landing/first-night.html) ·
      [someone's coming over](products/landing/guests.html) ·
      [just underwater](products/landing/underwater.html) ·
      [the room that became storage](products/landing/one-room.html).
      Completeness is enforced by
      [`check_entry_pages.py`](.github/scripts/check_entry_pages.py)
- ✅ Public contact (`hello@mrlifemanager.com`) and [privacy page](products/landing/privacy.html)
- ✅ Custom domain live at https://mrlifemanager.com (HTTPS)
- ✅ Customer-interview script and Dave recording guide ready
- ✅ **Four MailerLite automations are active**, per owner confirmation on
      2026-09-22. Each entry page routes to its own three-email sequence; email
      1 links only `The Week`. The private account state is not machine-verifiable
      from this public repository, so the last controlled delivery-test result
      is tracked in [`planning/operations.md`](planning/operations.md)
- ⬜ **Record Dave.** The recovered documents cover cleaning, organizing and
      hospitality only. Money, food, paperwork, maintenance and transitions are
      still entirely unsourced, and he is still the critical path for them
- ⬜ Complete the USPTO/name check and domain/social availability check
- ⬜ No completed audience validation, customers, or revenue yet

**Two honest caveats.** The products are designed prototypes, not validated
products. And the frameworks are the apprentice's reconstruction, not the
primary source — that gets fixed by recording Dave, not by more writing.

## Next steps

Start at [`planning/roadmap.md`](planning/roadmap.md), then
[`planning/backlog.md`](planning/backlog.md). Run the business from
[`planning/operations.md`](planning/operations.md) and record evidence in
[`planning/monthly-scorecard.md`](planning/monthly-scorecard.md). Decisions get
recorded in [`planning/decisions.md`](planning/decisions.md).
