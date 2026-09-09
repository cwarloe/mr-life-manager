# Roadmap

An MVP-first plan. The organizing principle is that **each phase buys information
the next phase needs.** Skipping ahead means building on assumptions.

**Current phase: Phase 0 → Phase 1.**

**Guiding constraint:** solo, part-time, no capital. Everything below assumes
evenings and weekends, and is sequenced so that no phase requires the previous
one to have made money — only to have produced evidence.

---

## Phase 0 — Foundation *(mostly complete)*

**Goal:** get the concept out of your head and into a form you can work with.

- [x] Define the concept and scope
- [x] Draft mission, principles, and audiences
- [x] Draft the core frameworks
- [x] Establish the repository and planning structure
- [x] Draft business model and product ladder
- [ ] **Record Dave — now the critical path.** Every framework here is a
      reconstruction from memory; the primary source is uncaptured. Needs
      *method*, not just time: he will tell you it's all obvious and mean it.
      Guidance in
      [source-material/](../source-material/original-charles-cleanup-notes.md).
- [ ] Import the existing written notes into `source-material/`
- [x] Decide the faith-framing question — settled by
      [ADR-009](decisions.md#adr-009--faith-framing-convictions-inform-the-work-belief-is-never-required-to-use-it):
      belief is never required to use the material; the founder does not hide his
- [x] Preliminary name scan — no exact collision found
      ([brand-name-scan.md](../docs/research/brand-name-scan.md))
- [ ] **Free USPTO search** at tmsearch.uspto.gov for "life manager," "mr life
      manager," "Mr. Man" — **now a prerequisite, not a nice-to-have.** Under
      [ADR-012](decisions.md#adr-012--licensing-permission-is-the-marketing) the
      name is the primary protected asset.
- [x] Dave's participation settled — discussed over years; he'll be compensated
      ([ADR-011](decisions.md#adr-011--mr-life-manager-is-a-real-person-dave-webster)).
      Putting it in writing eventually is worth doing, but it isn't blocking.
- [ ] Domain and social handle availability check

**Exit criteria:** the concept can be explained to a stranger in two minutes, and
the source notes are in the repo.

---

## Phase 1 — Validate audience and problem

**Goal:** find out whether real people have these problems badly enough to want
help — **before writing a product.**

This phase costs nothing but time and is the one most likely to be skipped. Don't.

### Do

- [ ] **15–20 conversations** across the personas in
      [target-audiences.md](../docs/vision/target-audiences.md). Recent movers,
      newlyweds, and recent grads are easiest to reach through existing networks.
- [ ] Lead with: *"What's something about running a home you had to figure out on
      your own and felt like you should have already known?"*
- [ ] Ask what they've **already tried**, and what they've **already paid for**.
      Past spending is the only reliable signal of future spending.
- [ ] Mine Reddit, TikTok comments, and forums for the exact language people use.
      Copy phrasing verbatim — it's the best copy source available.
- [ ] Check real search demand for the top candidate topics. **Test transition
      queries** ("first apartment checklist," "how to run your first home"), not
      brand or category queries — "life manager" is generic and crowded
      ([brand-name-scan.md](../docs/research/brand-name-scan.md)).
- [ ] Validate or correct the problem inventory in
      [customer-problems.md](../docs/research/customer-problems.md); mark
      confirmed items ✅
- [x] **Competitor research Phases A–C — substantially done 2026-09-08.** Three
      independent passes, acceptance test passed, findings synthesized in
      [competitor-notes.md](../docs/research/competitor-notes.md#findings).
      Remaining gaps: church young-adult curriculum (**zero examples**),
      university residence life, Notion sellers, and a systematic archive sweep.
- [ ] **Test the name.** Specifically watch how women in the target audience react
      to "Mr. Life Manager." Show the name plus one line of positioning and ask
      what they expect to find and who it's for; watch for *butler*, *app*, and
      *this isn't for me*. A preliminary scan found no blocking conflict but
      could not answer this — it's empirical
      ([brand-name-scan.md](../docs/research/brand-name-scan.md)).

### Exit criteria

- The top 10 problems are confirmed by real people, not assumed
- At least 3 people have said some version of *"I would pay for that"* unprompted
- You know which persona has the most acute, most reachable pain
- You know whether a comparable product already exists

**If it fails:** the problems are real but nobody prioritizes them. Reconsider the
beachhead or go straight to the institutional channel, where the *buyer* is
different from the *user*.

**Timebox:** 4–6 weeks. Don't let research become a way to avoid shipping.

---

## Phase 2 — Free lead magnet

**Goal:** prove you can reach the audience and that they'll trade an email for
what you make.

### Build

- [x] **First Apartment Checklist — draft 1 written** 2026-09-08
      ([product](../products/checklists/first-apartment/)). Sequenced by time
      rather than by category, with move-in documentation as the hook. **Designed
      2026-09-09; not yet reviewed or tested.**
- [x] **How Often Should I…? — draft 1 written** 2026-09-08
      ([product](../products/checklists/how-often/)). Organized by frequency so
      it converts into a routine. Safety rows
      fact-checked; **designed 2026-09-09.**
- [x] **Cleaning Supply Starter List — draft 1 written** 2026-09-08
      ([product](../products/checklists/cleaning-supplies/)). Leads with what to
      *skip* — the fastest credibility move in a category full of affiliate
      content. **The free tier is drafted and designed. None of it is tested with a
      real reader.**
- [x] **Landing page — draft 1 written and designed** 2026-09-09
      ([product](../products/landing/), [setup](../products/landing/SETUP.md)).
      Static, no dependencies. **Not connected to an email provider** — that is
      the one remaining step, and it's a paste-in URL.
- [ ] **Pick an email provider and paste the endpoint in** — see
      [SETUP.md](../products/landing/SETUP.md)
- [ ] Welcome sequence, 3 emails that teach rather than sell. The day-7 email
      should invite a reply about what they're stuck on — **that is the research
      channel**, and the most valuable email in the sequence.
- [ ] **A parent-facing variant** — "send this with your kid to college."
      Costs one extra landing page and tests the buyer-isn't-the-user hypothesis
      that may unlock the entire student market.

### Distribute

- [ ] Personal network, church, campus contacts
- [ ] Reddit and forums — participate genuinely, don't drop links
- [ ] Short-form video showing one specific useful thing
- [ ] Time it to **August–September** (move-in) and **December–January**
      (new-year reset)

### Exit criteria

- 200+ downloads (any real number beats zero; this is a threshold for *signal*,
  not success)
- Measurable organic sharing
- Replies from real people
- A list you can email

**If it fails:** the constraint is distribution, not product. Solve reach before
building anything else. **This is the most likely failure point in the plan** —
content businesses die of obscurity, not of bad content.

---

## Phase 3 — First paid product

**Goal:** prove someone will pay.

### Build

- [ ] **Two or three $9–$19 guides** — lead with these. They test which topic
      sells before anything long gets written.
- [ ] **Presell or waitlist *First Place*** — do not write it first
      (decided 2026-09-08). Build demand, then produce to it.
- [ ] Payment and delivery (Gumroad, Podia, Lemon Squeezy — pick the boring one)
- [ ] Sales page written from
      [customer-outcomes.md](../docs/vision/customer-outcomes.md)
- [ ] Launch sequence to the Phase 2 list

### Why *First Place* is the right flagship

- **Names the moment.** Not a topic — a life transition. That's the buying
  trigger.
- **The title works twice:** your first place to live, and putting things in
  their place.
- **Comprehensive enough to justify $49** while remaining one clear promise.
- **It's the spine of everything else.** The 30-Day Reset, the couples edition,
  the student edition, and eventually a course are all repackagings of it.
- **It's the licensable asset.** Institutions buy curriculum, not tips.

**Decided 2026-09-08: no book until there is demand.** Build demand first, then
produce to it. A 40-page guide that sells beats a 200-page book that doesn't, and
you find out in a fraction of the time.

Practically, that means Phase 3 leads with the **small paid guides** and a
**presell or waitlist** for *First Place* — not with writing it. If the waitlist
fills, write the book to an audience that already exists. If it doesn't, you
learned that for the cost of a landing page instead of three months.

### Exit criteria

- 20+ sales *(a small number, chosen deliberately — 20 strangers paying is real
  validation; 500 friends downloading a freebie isn't)*
- Refund rate under 5%
- Buyers who report actual outcomes

**If it fails:** distinguish "wrong product" from "wrong price" from "no traffic."
Talk to people who downloaded but didn't buy — that's where the answer is.

---

## Phase 4 — Test with real users

**Goal:** find out whether the product actually *works*, and get proof.

- [ ] Follow up with every buyer at 30 and 90 days
- [ ] Ask specifically about the outcomes in
      [customer-outcomes.md](../docs/vision/customer-outcomes.md)
- [ ] Collect testimonials and permission to use them
- [ ] **Run 5–10 coaching engagements or $99 audit calls** — the fastest,
      highest-fidelity learning available, and it pays
- [ ] Revise the product based on what actually got used and what got ignored
- [ ] Identify the top 3 requested additions

### Exit criteria

- Real customer quotes replacing the invented targets in
  [customer-outcomes.md](../docs/vision/customer-outcomes.md)
- At least a few people describing genuine change
- A clear read on what to build next — **from customers, not from this document**

---

## Phase 5 — Expand into a product family

**Goal:** increase revenue per customer and open the institutional channel.

### Consumer

- [ ] Persona editions of *First Place* (student, couples, starting over) —
      highest ROI available: ~20% new writing for a new market
- [ ] **The 30-Day Life Reset** ($79) — repackage, don't rewrite
- [ ] Toolkits: Household Operating System, Paperwork, Hosting
- [ ] Bundles and a full ladder
- [ ] Group coaching cohort ($299–$499) — better economics and lower cost than a
      video course
- [ ] A video course **only if** text products are clearly selling

### Institutional

- [ ] Package a licensable version: modular, standalone, printable, brandable
- [ ] Facilitator guide and train-the-trainer materials
- [ ] Start with warm networks — a church young-adult program, a campus ministry,
      one friendly housing office
- [ ] Build one case study before approaching anyone cold
- [ ] Then approach universities, military transition programs, and nonprofits

### Exit criteria

- Multiple products selling
- Rising revenue per customer
- At least one institutional pilot

---

## Timeline (rough, part-time)

| Phase | Duration | Cumulative |
|---|---|---|
| 0 — Foundation | 2–4 weeks | Month 1 |
| 1 — Validate | 4–6 weeks | Month 2–3 |
| 2 — Lead magnet | 4–8 weeks | Month 4–5 |
| 3 — First paid product | 8–12 weeks | Month 6–8 |
| 4 — User testing | 8–12 weeks | Month 9–11 |
| 5 — Product family | Ongoing | Year 2 |

**Reality check:** part-time projects take longer than planned, always. Treat this
as sequence, not schedule. The order is the valuable part.

**Seasonality is real and should drive timing.** August–September (move-in) and
December–January (new year) are the two windows when this audience is actively
looking. Aim to have the free asset ready before one of them.

---

## What could kill this

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Can't reach the audience** | **High** | Phase 2 exists to test this first; use warm networks; institutional channel as fallback |
| Audience won't pay individually | Medium-High | Parent-as-buyer; institutional licensing; premium personas |
| Building before validating | **High** | The phase gates; presell before writing |
| Scope creep across 13 domains | High | Ship *First Place* narrow; domains are a map, not a checklist |
| Founder time | High | Small products, real deadlines, no video until text works |
| Perfectionism | **High** | Ship the 80% version. The framework applies to the founder too. |
| Category is crowded / gap is a graveyard | Medium | Phase 1 competitor research, honestly read |

**The two biggest risks are both about the founder, not the market:** building
before validating, and never shipping because it isn't perfect. Guard against
those first.

---

## The next three things

1. Import the original source notes into `source-material/`
2. Line up the first five Phase 1 conversations
3. Draft the First Apartment Checklist — it can be built in parallel with Phase 1,
   and it makes the conversations concrete

Detail lives in [backlog.md](backlog.md); decisions get recorded in
[decisions.md](decisions.md).
