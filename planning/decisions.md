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

**Evidence added 2026-09-06** — preliminary external name scan
([brand-name-scan.md](../docs/research/brand-name-scan.md)). Decision unchanged;
confidence raised, with two new constraints recorded:

- **No exact-name collision found.** Medium confidence — the scan covered GitHub,
  app stores, and social media, but **no trademark database.** A free USPTO
  search is now an open Phase 0 item.
- **"Life manager" is generic and crowded** in the productivity-app category.
  Two consequences: weak trademark distinctiveness for the words alone (the
  protectable asset is the whole mark), and "life manager" is a bad SEO target.
  Compete on transition queries instead.
- **Nearest adjacent product:** "Mr. Man: Life Tips & Coaching" — a male-persona
  life-advice app. Different category, but the one specific item to raise with
  counsel later.
- **The gender risk was independently confirmed**, which raises confidence that
  it's worth testing. It does **not** answer it. That question is empirical and
  cannot be resolved by deliberation.

The scan largely confirmed this ADR rather than challenging it. Confirmation from
an independent pass has value, but it is not a substitute for the Phase 1
audience test, which remains the actual revisit trigger.

**Materially updated 2026-09-08 by [ADR-011](#adr-011--mr-life-manager-is-a-real-person-dave-webster).**
"Mr. Life Manager" is **Dave Webster, a real person**, not a persona choice. This
changes the risk profile of this ADR substantially:

- **The gender risk shrinks.** The concern was that "Mr." reads as *a man telling
  you how to run your house*. That lands very differently when "Mr." is a
  specific man who actually taught this, and when the voice reaching the reader
  is **the apprentice's rather than the master's**. The reader is handed what
  someone learned, not lectured by an authority.
- **The "butler service" read weakens.** A named teacher is not a service.
- **The credibility structure strengthens**, matching what the research found in
  every category winner: a real person with a real story.
- **The trademark question sharpens.** Under
  [ADR-012](#adr-012--licensing-permission-is-the-marketing) the name is now the
  primary protected asset, so the USPTO search is a prerequisite rather than
  a nice-to-have.

**Still test it in Phase 1.** Reduced risk is not zero risk, and this remains an
empirical question. But the name is now anchored in something true, which is a
far better position than a naming device would have been.

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

> ### ✅ RESOLVED by [ADR-010](#adr-010--beachhead-keep-the-audience-change-the-payer) — keep the audience, change the payer
>
> ### The evidence that prompted it (added 2026-09-08)
>
> Three independent competitive research passes
> ([findings](../docs/research/competitor-notes.md#findings)) converged on a
> pattern that puts this ADR in question. **The decision has not been changed —
> this needs a human.**
>
> **What the evidence says.** Every commercially successful player in this
> landscape sells to someone **already running a household and overwhelmed by
> it** — not to someone new at it. Every verified commercial attempt at
> *18–25, first-independence, multi-domain* underperformed or died:
>
> - **Society of Grownups** — MassMutual + IDEO, a **$100M** announced
>   investment, 9,000 registrations in 13 months, 10-city expansion plan.
>   **Storefront closed within two years**, staff laid off, brand gone.
>   *(Independently verified.)*
> - **The Adulting School** — this exact positioning, four-domain curriculum,
>   national press, $30 price. Renamed, then no activity found after ~2019.
> - Udemy "Adulting": **361 students.** Outschool: **5 learners.** The newest
>   entrant with near-identical positioning is **free.**
>
> Meanwhile the audience is well served for free by institutions — Casey Life
> Skills, Project LIFE, DoD TAP (~200,000/yr), Extension renter programs,
> university Adulting 101 courses.
>
> **What it does not say.** It does *not* say the need is fake. Society of
> Grownups drew 9,000 signups; the vehicle and unit economics failed, not the
> demand. It also does not say abandon this audience.
>
> **What it does say:** *who has the problem* and *who has the credit card* are
> different people. This repo half-anticipated it —
> [target-audiences.md](../docs/vision/target-audiences.md) already calls Maya
> "the best audience and the worst customer," and
> [revenue-ideas.md](../docs/business/revenue-ideas.md) already flags
> parent-as-buyer as the unlock. The research says that instinct was right and
> **understated**.
>
> **The options, for a human to choose between:**
>
> 1. **Hold.** Keep the beachhead, and treat parent-gift and institutional
>    licensing as the primary revenue path rather than a later channel.
> 2. **Shift the payer, keep the audience.** Same content, sold to the
>    overwhelmed adult already running a household — with first-independence as
>    a gift and institutional channel. (This is what the research recommends.)
> 3. **Shift both.** Aim at the overwhelmed-household persona (Dana) as primary.
>
> Options 2 and 3 are close to what the evidence supports. Option 1 is
> defensible but should be chosen deliberately, knowing the graveyard.
>
> **Chosen: option 2.** See [ADR-010](#adr-010--beachhead-keep-the-audience-change-the-payer).

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

**Supporting argument added 2026-09-06.** The brand name scan
([brand-name-scan.md](../docs/research/brand-name-scan.md)) supplies a reason
this decision is right that we hadn't recorded: "life manager" is generic and
crowded **specifically in the software and app category.** Building an app would
drop the brand into the one category where its name is weakest and least
differentiated. Staying content-side avoids that collision entirely. This
strengthens the existing exclusion of "an app as the primary product" in
[backlog.md](backlog.md).

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

## ADR-009 — Faith framing: convictions inform the work; belief is never required to use it

**Status:** Accepted
**Date:** 2026-09-08

**Context.** The founder's motivation for this work is explicitly Christian —
stewardship of time, money, possessions, and relationships, and hospitality as
the reason order matters. The open question was how visible that should be:
(a) stated openly throughout, (b) held implicitly and expressed as stewardship
and hospitality language, or (c) split into two product lines. This blocked
voice, copywriting, channel strategy, and partnerships.

**Decision.** Option (b), stated precisely:

> **Nobody has to share the founder's faith to use any of this.** The products
> teach practical systems and require no belief, no agreement, and no religious
> vocabulary from the customer. **And the founder does not scrub his faith from
> his own voice.** He talks about Jesus with people; he simply never makes it a
> condition of being helped.

Or, in the founder's words: *it's not like someone has to be born again in order
to clean up their house.*

**The operational line — product vs. person.** The decision is only usable if it
says where the boundary sits:

| | Faith content |
|---|---|
| **Products** (guides, checklists, courses, toolkits) | None by default. No scripture, no assumed shared belief, no conversion framing. Someone who bought laundry advice gets laundry advice. |
| **The founder's own voice** (about page, social, newsletter, conversations, speaking) | His own. Not sanitized, not hidden. If someone asks why he cares about this, he answers honestly. |
| **Ministry-channel editions** (if built) | Explicit and appropriate to the context, because the audience opted into it. A separate product, never a swap-in. |

**Rationale.**

- **It is theologically coherent, not a compromise.** Practical wisdom about
  ordinary life is available to everyone — order, diligence, stewardship, and
  hospitality are goods that work for anyone, and much of the biblical wisdom
  literature is addressed to exactly that. Teaching them without a belief gate
  isn't soft-pedaling; it follows from taking them seriously as *good*.
- **It matches the brand's central commitment.** The premise is that nobody
  taught these people, and the tone is dignity rather than shame
  ([principles.md](../docs/vision/principles.md) §8). A belief requirement would
  add exactly the barrier the brand exists to remove.
- **The vocabulary already works both ways.** *Stewardship* and *hospitality* are
  the honest words for the actual convictions **and** fully intelligible to a
  secular reader. They are not euphemisms or code — they carry the real meaning
  in language everyone can use. No translation layer is needed.
- **It keeps both channels open without dishonesty.** The general market gets a
  genuinely general product. Churches and ministries get a partner whose
  convictions are real rather than retrofitted.
- **It is sustainable.** A position requiring the founder to hide who he is would
  erode; so would one requiring customers to agree with him. This requires
  neither.

**Consequences.**

- Easier: copywriting is unblocked; voice is settled; the church and campus
  ministry channel stays open; the general market is not narrowed.
- Easier: no separate "secular version" has to be maintained — the default
  product *is* the general one.
- Harder: requires discipline in both directions. Not letting faith language
  drift into products, **and** not quietly scrubbing the about page when a large
  secular buyer appears.
- A ministry edition, if built, is a genuine additional product with its own
  cost — not a reskin.

**Pressure tests.** Decisions like this are rarely reversed outright; they erode
under specific pressure. Naming the likely pressures in advance:

1. **A secular institutional buyer asks that the founder's public faith be
   downplayed.** → No. The *product* already contains no faith content, which is
   what they are actually buying. His bio is not part of the purchase.
2. **A church partner asks for scripture in the general product.** → No. Offer a
   ministry edition instead.
3. **Marketing advice says the faith association will limit the market.** → The
   products are already general. The founder's identity is not the product, and
   removing it would buy nothing.
4. **A customer objects to the founder being a Christian.** → The material stands
   on its own merits. Nothing is being asked of them.

**Revisit when:** never, on the substance. Revisit the *mechanics* if a ministry
edition is actually built, since that is where the boundary gets tested in
practice.

---

## ADR-010 — Beachhead: keep the audience, change the payer

**Status:** Accepted
**Date:** 2026-09-08
**Supersedes the open review on** [ADR-003](#adr-003--initial-beachhead-market-first-time-independent-adults)

**Context.** Three independent research passes found that every commercial
success in this landscape sells to people **already running a household and
overwhelmed by it**, while every verified attempt at *18–25, first-independence,
multi-domain* underperformed or died — including Society of Grownups, with a
$100M announced investment, which closed its storefront within two years.

**Decision.** **Keep the audience. Change the payer.**

The content stays aimed at people who were never taught these systems, with
first-time independence as the sharpest expression of that need. What changes is
**who the marketing addresses and who is asked to pay**:

| | Who |
|---|---|
| **Who the content serves** | Unchanged — anyone never taught this, first-timers included |
| **Who the marketing addresses** | The overwhelmed adult already running a household |
| **Who pays** | That same adult · a parent buying a gift · an institution licensing |

**Rationale.**

- **It changes marketing, not content.** Nothing in `frameworks/`, `content/`, or
  the drafted free assets needs rewriting. The cadence reference already serves
  every persona; the First Apartment Checklist already works as a gift.
- The graveyard is specifically at *selling to the 22-year-old*, not at *teaching
  the 22-year-old*. Society of Grownups drew 9,000 registrations — the demand was
  real, the payer was wrong.
- This repo half-anticipated it. [target-audiences.md](../docs/vision/target-audiences.md)
  already called Maya "the best audience and the worst customer."
- It keeps the transition trigger, which is the strongest asset in the
  positioning, while pointing the ask at someone who can act on it.

**Consequences.**
- Easier: the free tier reaches the widest audience; the paid tier addresses
  someone with budget; parent-gift and institutional channels move from "later"
  to primary.
- Harder: two audiences to speak to without the copy becoming mush. The free
  assets skew first-timer; the paid ladder must skew overwhelmed-householder.
- [product-ladder.md](../docs/business/product-ladder.md) pricing should be
  re-examined against this payer, who is less price-sensitive than a student.

**Revisit when:** Phase 4 shows first-time independents buying directly at rates
the research says they won't.

---

## ADR-011 — Mr. Life Manager is a real person: Dave Webster

**Status:** Accepted
**Date:** 2026-09-08
**Resolves** the open persona question and materially changes
[ADR-001](#adr-001--brand-name-mr-life-manager)

**Context.** The open question was whether "Mr. Life Manager" is a first-person
character, or "Mr." is a stylistic quirk on a neutral brand. Neither. **Mr. Life
Manager is Dave Webster, a real person**, and the systems taught here originate
with him.

**Decision.**

> **Dave Webster is Mr. Life Manager.** He is the original — the person who
> actually knew how to do this and taught it. The founder's role is **the
> apprentice**: the one who learned it, wrote it down, and is passing it on.

The brand is a **master-and-apprentice structure**, not an invented persona.
Dave's likeness is available and may be used; recording him is under
consideration.

**Rationale.**

- **It is true**, which no invented persona can be. The credibility structure
  the research found in every winner — Mercury Stardust, KC Davis, How to ADHD —
  is a real person with a real story. This has one.
- **It resolves the gender risk far better than a workaround would.** The concern
  in ADR-001 was that "Mr." reads as *a man telling you how to run your house*.
  That risk shrinks substantially when "Mr." is not a marketing device but a
  specific man who taught specific people — and when the voice reaching the
  reader is **the apprentice's, not the master's**. The reader isn't being
  lectured by an authority; they're being handed what someone else learned. That
  is a fundamentally more welcoming posture, and it is available to any reader
  regardless of gender.
- **It solves the voice problem.** "Here is what Dave taught me" is a natural,
  sustainable register. An invented narrator would have required consistent
  character work forever.
- **It is a proven teaching structure** — the mentor who knows and the narrator
  who learns, as in *The Goal*. It lets the reader occupy the apprentice's seat.

**Consequences.**
- Easier: authentic voice; a real face; a natural answer to "who are you to teach
  this?"; strong story for marketing and for the ministry/institutional channel.
- Easier: the founder never has to pose as the expert, which is both more honest
  and more comfortable.
- **Harder — and this is now the live risk:** the brand rests on a real person
  who is not the founder. Consent, attribution, compensation, and control need to
  be settled explicitly and in writing. See
  [open questions](#open-decisions).
- Content sourcing changes: **Dave is a primary source**, and `source-material/`
  should reflect whose material is whose.

**Revisit when:** Dave's involvement or wishes change. This decision is
contingent on his consent in a way no other ADR here is.

---

## ADR-012 — Licensing: permission is the marketing

**Status:** Accepted
**Date:** 2026-09-08
**Supersedes** [ADR-008](#adr-008--license-deliberately-undecided)

**Context.** ADR-008 deliberately held the licensing decision open. The founder
has now named the model: let people use the material freely or cheaply, ask that
they say where it came from, and charge for **assistance**, not for permission.

**Decision.** **Attribution, not restriction.**

| What | Terms |
|---|---|
| **Frameworks and free content** | Free to use, adapt, and teach — **attribution required** |
| **Paid products** | Bought normally; not freely redistributable |
| **The name "Mr. Life Manager"** | **Protected.** This is the actual asset. |
| **Help, coaching, consultation, facilitation** | Paid. This is the revenue. |

Recommended instrument: **CC BY 4.0** for `frameworks/` and the free tier;
all-rights-reserved for paid products; **trademark** as the real protection.

**Rationale.**

- **Copyright was never the moat.** Anyone can write a first-apartment checklist.
  Nobody else can be Mr. Life Manager. [LICENSING-NOTES.md](../LICENSING-NOTES.md)
  already reached this conclusion; this decision acts on it.
- **Attribution is distribution.** Every church, campus ministry, RA program, and
  transition program that uses the material carries the name with it. That is the
  institutional channel solving its own hardest problem — getting in the door —
  at zero acquisition cost.
- **It removes the friction that kills the institutional channel.** Procurement
  is slow; permission is instant. Let them use it, then sell them help.
- **It fits the convictions.** Withholding practical help that costs nothing to
  copy, in order to charge for permission, would sit badly against
  [ADR-009](#adr-009--faith-framing-convictions-inform-the-work-belief-is-never-required-to-use-it)
  and the stewardship framing. Generosity here is also good strategy, which is a
  comfortable place to be.

**Consequences.**
- Easier: adoption, institutional reach, goodwill, and word of mouth.
- Easier: no permissions administration.
- Harder: **the trademark now matters much more.** If the name is the asset, it
  has to be searched and registered. The free USPTO search moves from
  nice-to-have to prerequisite.
- Harder: someone will eventually use the material commercially with attribution
  and without paying. Under this model that is a **feature**, not a leak — but it
  should be a decision made with open eyes.
- CC BY permits commercial reuse. If that is unacceptable, **CC BY-NC** is the
  fallback — but note that "non-commercial" is vague and hard to enforce, and it
  would block exactly the institutional uses this model wants to encourage.

**Not legal advice.** Before registering a trademark or publishing a license,
talk to an attorney — especially given ADR-011.

**Revisit when:** the trademark position is known, or the first paid product
exists.

---

## Open decisions

Not yet ADRs. These need to be made, and each blocks something.

| Question | Blocks | Urgency |
|---|---|---|
| **Is Dave's participation settled in writing?** Consent to use his name and likeness, how he's credited, whether he's compensated or holds equity, and who decides if you disagree. | Everything. [ADR-011](#adr-011--mr-life-manager-is-a-real-person-dave-webster) rests on it. | **Highest** |
| **Is he "Dave Webster" publicly, or only "Mr. Life Manager"?** | Copy, the about page, how the face is used | **High** |
| **Whose notes are in `source-material/`** — the founder's, Dave's, or the founder's record of Dave's teaching? | Attribution, and the file's name | **High** |
| **Trademark the name.** Now the primary protected asset under [ADR-012](#adr-012--licensing-permission-is-the-marketing). | Licensing model, brand safety | **High** |
| Does CC BY (commercial reuse allowed) go too far, or is CC BY-NC the right fallback? | [ADR-012](#adr-012--licensing-permission-is-the-marketing) mechanics | Medium |
| Is Health in scope, given liability and expertise limits? | Domain taxonomy, content plan | Low |
| Does Transportation earn its own domain, or fold into Maintenance? | Taxonomy | Low |
| Should the public-facing domain list compress from 13 to 5–6? | Marketing, product structure | Low |
| Presell *First Place* or write it first? | Phase 3 sequencing | Medium |

**Closed by evidence, not by decision:** *"What scope of offering — content, app,
or hybrid?"* was raised externally as an open question. It is already answered:
[ADR-007](#adr-007--mvp-prioritizes-practical-tools-over-abstract-coaching)
commits to digital content products, and [backlog.md](backlog.md) lists an app as
explicitly not being pursued. The name scan added a new argument for that
position rather than reopening it.

**Recommended next decision: settle Dave's participation, in writing.**

[ADR-011](#adr-011--mr-life-manager-is-a-real-person-dave-webster) is now the
foundation of the brand, and it is the only ADR here that depends on another
person's ongoing consent. Everything else — the name, the face, the voice, the
story, the trademark — sits on top of it.

This is not a legal formality between strangers. It is the ordinary kindness of
being explicit with someone whose name you are building something on, **before**
there is money or an audience to complicate it. Friendships survive that
conversation early far more reliably than late.
