# Brand Name Scan — "Mr. Life Manager"

**Status:** Preliminary. One external scan, not independently verified.
**Date:** 2026-09-06
**Input:** [inputs/2026-09-05-brand-name-research-summary.md](inputs/2026-09-05-brand-name-research-summary.md)
**Bottom line:** Keep the name. Spend nothing irreversible on it. Test it in Phase 1.

---

## What this scan is and isn't

**Is:** a preliminary availability check on the name, in the *software and app*
category, via web search.

**Is not:** a trademark search, and not the competitor research this project
actually needs. Phases A–D of [competitor-notes.md](competitor-notes.md) remain
untouched. See [Limitations](#limitations) — they're significant enough to read
before weighting anything below.

---

## Findings

Confidence reflects our assessment, not the source's. Nothing here has been
independently verified.

### 1. No exact-name collision found

No established brand or product uses "Mr. Life Manager" in a comparable
positioning.

**Confidence: Medium.** Consistent with expectations, but the search covered
GitHub, app stores, and social media — not business registries or trademark
databases. Absence of evidence in those channels is weak evidence of absence.

**Action:** none yet. Confirm with a free USPTO search (below).

### 2. "Life manager" is generic and crowded in the software category ★

Multiple apps and repos use "Life Manager," "My Life Manager," "LifeOS," and
similar, all clustered around tasks, notes, finances, and general productivity.

**Confidence: High.** Directly observable, and matches what anyone would expect
of that phrase.

**Why it matters — two distinct consequences:**

- **Trademark distinctiveness.** A descriptive phrase in a crowded field is hard
  to protect. We are unlikely to ever own "Life Manager." "Mr. Life Manager" as a
  whole may be registrable, but the protectable part is the *whole mark*, not the
  words inside it.
- **SEO.** Competing on "life manager" means competing with app-store noise for
  traffic that isn't even looking for us. An app-seeker who lands on a curriculum
  site bounces.

**This is the most useful finding in the scan.**

### 3. Search demand should target the transition, not the brand ★

Optimize around "first apartment checklist," "how to run your first home,"
"household systems for young adults" — not the brand name.

**Confidence: High**, and it's really a strategic inference rather than a finding.

**Why it matters:** it independently confirms what
[target-audiences.md](../vision/target-audiences.md) already concluded — *the
transition is the buying trigger.* Nobody searches for a life-management brand.
They search for the thing that just happened to them.

**Action:** this sharpens the Phase 1 search-demand task in
[roadmap.md](../../planning/roadmap.md). Test transition queries, not brand
queries.

### 4. "Mr. Man: Life Tips & Coaching" is the nearest adjacent product

An app combining a male persona with life advice and coaching.

**Confidence: Medium.** The product appears to exist; whether it's an actual
conflict is a legal question this scan can't answer.

**Why it matters:** it's the closest thing to a conflict surfaced, and it's the
one specific item worth naming to a trademark attorney later. It also shows
"male persona + life advice" isn't novel at the concept level — though it's a
different category (app, coaching) from ours (curriculum, content).

### 5. The "Mr." gender-perception risk

"Mr." implies a male guide, which can read as friendly or as paternalistic
depending on execution — a live tension given the non-shaming ethos.

**Confidence: High that the risk exists. Zero that we know how it lands.**

**This is not new.** [ADR-001](../../planning/decisions.md) and
[brand-positioning.md](../business/brand-positioning.md) already flag it as the
name's top risk. Independent confirmation raises confidence that it's worth
testing; it does not tell us the answer.

**Critically: this is an empirical question, not a preference question.** No
amount of deliberation reveals how a 22-year-old woman reacts to "Mr." Only
asking her does.

### 6. Building software increases collision; staying content-side reduces it ★

**Confidence: High.** Follows directly from finding #2.

**Why it matters:** this is a **new argument for a decision already made.**
[ADR-007](../../planning/decisions.md) commits to digital content products, and
[backlog.md](../../planning/backlog.md) lists "an app as the primary product"
under *Explicitly not doing.* The scan adds a reason we hadn't recorded: an app
would drop us into the crowded, undifferentiated category where the name is
weakest.

### 7. "MR" collides with an unrelated homonym

Much of the "MR life" material online is memes about pharmaceutical **medical
representatives**, unrelated to any brand.

**Confidence: High but low relevance.** Matters only for social hashtag choices
(`#mrlife` is occupied by something else). Not a brand risk.

---

## Limitations

These are substantial. Weight the findings accordingly.

**1. Broken citation apparatus.** The summary's claims about *our own repo* cite
[1] and [3], which resolve to unrelated third-party GitHub projects
(`mzen17/Life-Manager`, `TaylorHuston/local-life-manager`). The repo description
is accurate, but it isn't supported by the sources attached to it. When citations
don't map to claims, individual citations can't be trusted without checking.

**2. No trademark database was searched.** For a trademark question, USPTO is
*the* source. GitHub and Google Play are not. The reasoning about descriptiveness
is sound and standard; the conclusions are not grounded in a trademark search.

**3. Roughly 15 of 41 citations are irrelevant** — Instagram and Facebook reels
about medical representatives. That's a homonym, not a landscape. Their presence
inflates the apparent depth of the research.

**4. It searched the wrong category for our actual business.** The scan covered
software and apps. Mr. Life Manager is a **content and curriculum** business. The
competitive set that matters — adulting books, home-economics content, personal
finance educators, campus life-skills curricula, church young-adult programs — was
not examined. That set is defined in
[competitor-notes.md](competitor-notes.md) and remains **entirely unresearched.**

**5. It confirms more than it discovers.** Findings #1, #5, and most of the
recommendation restate what
[brand-positioning.md](../business/brand-positioning.md) and ADR-001 already say.
Confirmation from an independent pass has real value — it means we weren't
fooling ourselves — but it isn't new information, and shouldn't be counted as
progress against Phase 1.

**6. No audience was consulted.** Zero people in the target market were asked
anything. The gender-perception question — the one that actually matters — is
exactly the question this method cannot answer.

---

## What this changes

| Document | Change | Status |
|---|---|---|
| [ADR-001](../../planning/decisions.md) | Evidence subsection added; decision unchanged | Done |
| [brand-positioning.md](../business/brand-positioning.md) | SEO finding, descriptiveness, nearest adjacent product | Done |
| [competitor-notes.md](competitor-notes.md) | Phase E partially addressed; A–D still open | Done |
| [roadmap.md](../../planning/roadmap.md) | Phase 1 search task sharpened toward transition queries | Pending |

**What does not change:** the name, the beachhead, the product ladder, or the
roadmap sequence. The scan supports the existing plan rather than redirecting it.

---

## Recommended next steps

Prompts for the two research jobs below, plus an acceptance test to apply
before trusting any result, are in
[research-prompts.md](research-prompts.md).

**Do now — free, ~1 hour total**

1. **USPTO search.** tmsearch.uspto.gov, free. Search "life manager," "mr life
   manager," and "Mr. Man." This is the single highest-value missing step, and it
   closes limitation #2 yourself.
2. **Domain and handle check.** `mrlifemanager.com` and the matching social
   handles. Availability is a real input to the naming decision and costs nothing
   to check. Note `#mrlife` is occupied (finding #7).
3. **Record the persona decision** — character or stylistic quirk. It's already an
   open item in [decisions.md](../../planning/decisions.md) and it blocks
   copywriting.

**Do in Phase 1 — the real test**

4. **Test the name with the actual audience**, especially women aged 20–30. Not
   "do you like it?" but: show the name plus one line of positioning, and ask
   what they expect to find and who they think it's for. Watch for *butler*,
   *app*, and *this isn't for me*.
5. **Test transition-query search demand**, not brand queries.
6. **Run competitor research Phases A–D**, which this scan did not touch and which
   remains the larger gap.

**Do later — not now**

7. **Trademark counsel.** Correct step, wrong phase. It costs real money and the
   answer doesn't change anything you'd do before Phase 3. Bring the USPTO
   results and the "Mr. Man" item when you go.
8. **Naming alternatives.** Deliberately deferred — see below.

---

## Why we are not generating naming alternatives yet

The source offered to propose alternatives. **Decline for now.**

- You rename on **data**, not on a list. Testing hasn't happened.
- Generating alternatives before a test turns a decision into shopping, and
  shopping is unbounded.
- The scan found no blocking conflict. There's nothing to route around yet.
- ADR-001 already names the trigger for reopening this: a negative audience
  reaction or a trademark conflict. Neither has occurred.

**The guardrail that does apply now**, and it's a good one from the source: keep
the architecture modular so a future rename is survivable. That's already true —
the frameworks, content, and product ladder carry no dependency on the name.
Nothing in `frameworks/` or `content/` would need rewriting if the brand changed.

**One thing worth internalizing regardless of the name:** the name is not the
differentiator. The manual-for-adulthood narrative, the transition positioning,
and the non-shaming ethos are. A great name would not save weak positioning, and
this positioning would survive a mediocre name.
