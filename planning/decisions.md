# Decision Log

Architecture Decision Record (ADR) style, adapted for a product and business
concept rather than software.

**Why keep this.** Six months from now, the reasoning behind a decision will be
gone but the decision will remain. This file preserves the *why*, so that
revisiting a decision means re-examining an argument rather than re-inventing one.

**Format**

```
## ADR-NNN — Title
Status:   Proposed | Accepted | Superseded by ADR-NNN | Rejected
Date:     YYYY-MM-DD
Context:  What situation forced a decision
Decision: What was decided
Rationale: Why
Consequences: What this makes easier and harder
Revisit when: The condition that should reopen this
```

**Status legend:** *Accepted* means we're acting on it. *Proposed* means it's
written down but not committed. Nothing here is permanent — but changing an
Accepted decision means writing a new ADR that supersedes it, not quietly
editing this one.

---

## ADR-001 — Brand name: "Mr. Life Manager"

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The concept needed a name to organize around before any other work
could proceed.

**Decision.** Use **Mr. Life Manager** as the working brand name.

**Rationale.**
- "Manager" frames life as something that can be *run* — a learnable system with
  methods. That's the entire thesis compressed into one word.
- "Mr." creates a persona: approachable, slightly formal, a bit wry. It reads as a
  character rather than a guru, which lowers the social cost of asking a basic
  question — critical for an audience whose core barrier is embarrassment.
- Distinctive. Doesn't sound like every other organizing or productivity brand.

**Consequences.**
- Easier: memorable identity, a persona voice to write in, clear differentiation.
- Harder: **gender perception risk.** "Mr." may read as *for men* or as *a man
  telling you how to run your house*. Several key personas are women.
- Harder: possible "butler service" read, which pulls toward services and away
  from teaching.
- Requires a trademark and availability check before any real investment.

**Revisit when:** Phase 1 audience testing shows a negative reaction — especially
from women in the target audience — or if a trademark conflict surfaces. Name
changes are cheap now and expensive later.

---

## ADR-002 — Repository name: `mr-life-manager`

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The project needed a home for concept work, frameworks, content, and
planning.

**Decision.** A standalone public repository named `mr-life-manager`, matching the
brand name. Markdown-only, no application code.

**Rationale.**
- Matches the brand; no translation needed between repo and product.
- Markdown is durable, diff-able, portable, and renders everywhere.
- Standalone rather than nested inside an unrelated project — this is its own
  concern with its own lifecycle.

**Consequences.**
- Easier: version-controlled thinking, visible evolution, easy to share.
- Harder: **business planning and product material are publicly visible.** That's
  acceptable now (ideas aren't the moat, execution is) but needs revisiting.
- If products are ever built here, a private repo will likely be required.

**Revisit when:** the first real product is being built, or if anything genuinely
sensitive needs to live here. See ADR-008.

---

## ADR-003 — Initial beachhead market: first-time independent adults

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The problem space touches nearly everyone, which is a trap. Broad
targeting produces content that resonates with no one.

**Decision.** Focus initially on **first-time independent adults** — college
students moving to apartments, young adults leaving home, newlyweds, and anyone
setting up a household for the first time.

**Rationale.**
- **Acute, time-bound pain.** The need spikes at a specific, identifiable moment.
- **A clear trigger.** The transition itself creates the search and the purchase.
- **They know they don't know.** No convincing required — the hardest part of most
  marketing is already done.
- **Reachable.** Concentrated in identifiable places: campuses, churches, moving
  services, wedding channels.
- **Institutional buyers exist** for exactly this population.

**Consequences.**
- Easier: sharper copy, obvious first product, clear channel choices.
- Harder: this is not the highest-willingness-to-pay segment. Students especially
  are the best audience and the worst customer.
- Requires a plan for reaching them where the *buyer* differs from the *user* —
  parents, universities, churches.
- Risks building a brand so youth-oriented that the higher-paying overwhelmed
  professional feels condescended to. Guard the tone.

**Revisit when:** Phase 4 data shows a different persona buying more readily, or
if the overwhelmed-professional segment proves easier to reach.

---

## ADR-004 — Broader scope: practical adult-life management

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The concept could be scoped narrowly (household management) or
broadly (all of adult life). Both have real advantages.

**Decision.** Scope the business as **practical adult-life management** across
the thirteen domains in
[life-domains.md](../frameworks/life-domains.md) — home, food, money, time,
health, work, digital life, relationships, transportation, maintenance,
paperwork, hospitality, and transitions.

**Rationale.**
- The underlying problem is identical across domains: nobody taught them, nothing
  has a place, everything is reactive.
- The frameworks generalize. *Everything has a place* applies equally to socks,
  files, dollars, and responsibilities — that transferability is the real
  intellectual asset.
- A single-domain brand caps out. A life-management brand can grow with the
  customer.
- Justifies a higher price: comprehensive guidance is worth more than a topic.

**Consequences.**
- Easier: room to grow, higher-value products, a defensible position nobody else
  occupies.
- Harder: **serious scope-creep risk.** Thirteen domains is a lot of surface area
  for a solo founder.
- Requires discipline: the MVP must ship narrow even though the vision is broad.
- Some domains (health, legal, financial) carry real liability boundaries.

**Mitigation.** Treat the domain map as a *map*, not a checklist. *First Place*
covers seven domains at practical depth; the rest wait.

**Revisit when:** scope creep is visibly slowing delivery, or a single domain
proves to carry the whole business.

---

## ADR-005 — Cleaning is an entry point, not the brand

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The concept originated in household cleaning and organization
guidance. Cleaning content is also the easiest to make and the easiest to
distribute — which makes it tempting to become a cleaning brand by default.

**Decision.** Cleaning is the **top-of-funnel entry point**, not the identity.
Cleaning content is produced deliberately for discovery and trust, and always
connects to the larger system.

**Rationale.**
- Cleaning is the most *visible* symptom, so it's how people find us.
- It's also the most *crowded* category, with the weakest economics — an enormous
  field of free content.
- Positioning as a cleaning brand caps the business at one of thirteen domains
  and forecloses the higher-value products.
- The founding insight was never about cleanliness. It was about **systems** and
  about **hospitality** — a clean home nobody enters misses the point entirely.

**Consequences.**
- Easier: a credible path to higher-value products; differentiation from a
  crowded field.
- Harder: must actively resist being categorized as a cleaning brand. Requires
  discipline in copy, imagery, and partnership choices.
- Cleaning content must always *bridge* to the broader system rather than
  standing alone.

**Test.** If a product could only appear in a cleaning company's catalog, it's
under-scoped.

**Revisit when:** cleaning content vastly outperforms everything else in
distribution *and* the broader content demonstrably fails to convert. That would
be market feedback worth listening to — but it should be a deliberate, recorded
pivot, not a drift.

---

## ADR-006 — Preventative management is a core framework

**Status:** Accepted
**Date:** 2026-09-05

**Context.** Several candidate ideas could serve as the organizing framework.
One had to be primary.

**Decision. Preventative vs. crisis management** is the central framework of the
curriculum. See
[preventative-vs-crisis.md](../frameworks/preventative-vs-crisis.md).

**Rationale.**
- It explains **why** the systems matter, which nothing else does as clearly.
- It applies to every one of the thirteen domains without strain.
- The economics are dramatic and easy to demonstrate — 10× to 100× cost
  differences that people recognize instantly from their own lives.
- It reframes the customer's situation compassionately: *you're not lazy, you're
  in crisis mode, and crisis mode consumes the capacity prevention requires.*
  That reframe is emotionally powerful and true.
- It naturally generates products: calendars, cadence references, checklists.

**Consequences.**
- Easier: a unifying thread across all content; a compelling sales argument;
  obvious product formats.
- Harder: prevention is intrinsically unrewarding to *feel*, so it must always be
  taught as something scheduled, never as something willed.
- Requires an honest account of how to *transition* from crisis mode, since that's
  where most of the audience starts.

**Revisit when:** never, probably. This one is load-bearing.

---

## ADR-007 — MVP prioritizes practical tools over abstract coaching

**Status:** Accepted
**Date:** 2026-09-05

**Context.** The business could lead with high-touch coaching (immediate revenue,
no leverage) or with digital tools (delayed revenue, full leverage).

**Decision.** The MVP is **practical, concrete, digital tools**: checklists,
guides, calendars, and templates. Coaching is used deliberately and in limited
quantity as **paid customer research**, not as the primary offer.

**Rationale.**
- Practical tools *are* the differentiation. Mindset coaching without systems is
  the category we're explicitly positioned against
  ([brand-positioning.md](../docs/business/brand-positioning.md)).
- Digital products scale; a solo founder's hours don't.
- Concrete artifacts are far easier to validate — either someone downloads and
  uses a checklist or they don't.
- Coaching that becomes the business quietly strangles product development.
- **But:** ten coaching conversations teach more about real problems than a
  hundred survey responses, and they pay while doing it. That's worth doing on
  purpose, capped.

**Consequences.**
- Easier: leverage, scalability, and a clear MVP.
- Harder: slower initial revenue; requires writing before earning.
- Requires deliberately *capping* coaching so it doesn't consume the calendar.
- Premium tiers stay available later, anchored on proven material.

**Revisit when:** Phase 4 shows coaching converting dramatically better than
products, or if cash flow requires a service pivot.

---

## ADR-008 — License: deliberately undecided

**Status:** Proposed
**Date:** 2026-09-05

**Context.** A public repository with no license is "all rights reserved" by
default. That's a defensible position, but it should be chosen rather than
stumbled into.

**Decision.** **Do not choose a license yet.** Document the options and their
implications in [LICENSING-NOTES.md](../LICENSING-NOTES.md) and decide once the
first real product exists.

**Rationale.**
- The repo mixes three kinds of material — spreadable frameworks, commercial
  product content, and internal business planning — which probably deserve
  different treatment.
- The most consequential upstream question (does `products/` belong in a public
  repo at all?) is unanswered, and licensing shouldn't be decided ahead of it.
- Choosing a permissive license is easy to do and effectively impossible to undo.

**Consequences.**
- Easier: nothing is foreclosed; maximum flexibility retained.
- Harder: the public repo is legally inert — readable, not reusable. Blocks
  contributors and quotation.
- Ambiguity for anyone who wants to use the material.

**Revisit when:** the first real product is complete, or someone asks to use the
material. Whichever comes first.

---

## Open decisions

Not yet ADRs. These need to be made, and each blocks something.

| Question | Blocks | Urgency |
|---|---|---|
| **How explicit is the Christian stewardship framing?** Options: (a) stated openly, (b) held implicitly and expressed as stewardship/hospitality language, (c) two product lines. | Voice, copywriting, channel, partnerships | **High** |
| Does the brand need a visible human face, and must it be the founder? | Marketing approach, content format | Medium |
| Is "Mr. Life Manager" a first-person persona or a brand name? | Voice in all copy | Medium |
| Should `products/` live in a public repo at all? | ADR-008, repo structure | Medium |
| Is Health in scope, given liability and expertise limits? | Domain taxonomy, content plan | Low |
| Does Transportation earn its own domain, or fold into Maintenance? | Taxonomy | Low |
| Should the public-facing domain list compress from 13 to 5–6? | Marketing, product structure | Low |
| Presell *First Place* or write it first? | Phase 3 sequencing | Medium |

**Recommended next decision:** the faith-framing question. It's the highest-urgency
item, it blocks copywriting, and it's the one most likely to be decided by drift
rather than by intent if left open. Everything downstream — voice, channel,
partnerships — depends on it.
