# Past First Contact — Strategy

**Status:** Proposed 2026-09-28. Not adopted; nothing here is live.
**Scope:** What happens after a reader finishes an entry-page task and gives an
email address, up to the first real sale.

Governed by [ADR-014](../../planning/decisions.md#adr-014--completion-is-what-converts),
[ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email),
[ADR-016](../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [principles](../vision/principles.md). Where this page conflicts with any of
them, they win.

**Evidence status:** none. The [scorecard](../../planning/monthly-scorecard.md)
has no recorded month, and analytics were not installed as of 2026-09-22
([operations.md](../../planning/operations.md)). Every ranking below is
reasoning, not data.

---

## The three moves, ranked

### 1. One ask after the win

Cut the completion page ([`templates/finished.html`](../../products/landing/templates/finished.html))
to the email ask alone. It now carries four: the email form, the *First Place*
founding offer, "Send the task," and "tell me where you stopped."

- **Customer action:** get Dave's week on one page by email.
- **Principle:** 11, *Completion is what converts*. The offer filter says a
  page with more than one thing to act on fails.
- **Why first:** it is the exact moment past first contact, it breaks the
  offer filter today, and it costs nothing. Until it holds one ask, a low
  signup number can't be read.
- **Executes:** Nightly Audit Engineer (template edit). Mailer Bot confirms the
  form still routes to the four `entry-*` groups.
- **Charles approves:** publishing the trimmed page.

### 2. Five-person pilots, one route at a time

Run [validation-launch.md](../../planning/validation-launch.md) as written:
parent, church, or campus, one route at a time.

- **Customer action (the partner's):** propose a five-person pilot.
- **Principle:** 11, *Completion is what converts*, in its "measure completion,
  not downloads" form. The pilot report is a count of who finished.
- **Why second:** the repo names qualified use as the constraint. The
  scorecard rule "No visitors: improve distribution; do not build another
  product" blocks everything after this. It also opens the parent payer
  ([ADR-010](../../planning/decisions.md#adr-010--beachhead-keep-the-audience-change-the-payer)).
- **Executes:** Charles.
- **Charles approves:** every introduction sent (drafts are in
  validation-launch.md), plus the analytics beacon needed to count visitors.

### 3. *First Place* founding presale at $39

Once pilots show completions and reservations exist, turn the no-charge
reservation into a real founding purchase. Charles tells reservers himself, as
[`first-place.html`](../../products/landing/first-place.html) promises. Not by
MailerLite broadcast.

- **Customer action:** buy the $39 founding version.
- **Principle:** 11, *Completion is what converts* (the commercial half), and
  9, *Simple enough to actually keep*: "a sequence, not a pile."
- **Why third:** it is the first durable revenue, but it sits behind the
  "Before the first sale" gate in operations.md, and the scorecard warns that
  "Reservations without purchases" are curiosity, not demand.
- **Executes:** Back Office (checkout terms, refund policy, assumed-name and
  entity check, transaction records, tax and bookkeeping). Charles sends the
  replies.
- **Charles approves:** payment platform signup, terms, entity, price, and
  every message to reservers.

---

## Referrals and incentives

**Make sharing easy. Pay nothing for it.** The referral engine already exists:
[ADR-013](../../planning/decisions.md#adr-013--licensing-revised-free-to-use-never-free-to-sell)
("Free to use. Never free to sell. The brand travels with it"), the parent page
[`index-parents.html`](../../products/landing/index-parents.html), and the
partner pilot. Reject credits, discounts, or rewards for referrals for now.
[commerce-rules.md](commerce-rules.md) says a recommendation must be one that
"Would remain defensible if no commission existed," and a referral reward is a
commission paid to the customer. It would also add a second ask (principle 11)
and put social pressure on the reader (principle 8, *Dignity, not shame*). The
one referral that carries revenue is a parent buying *First Place* as a gift
([revenue-ideas.md](revenue-ideas.md)), and that waits for move 3.

## Patronage and memberships

**Wait. Reject a content membership outright.**
[business-model.md](business-model.md) says membership "fights the brand: the
promise is *you'll need us less over time*." revenue-ideas.md marks content
membership 🔴 and a seasonal reset membership 🟡. operations.md makes any
membership wait on "Proven recurring demand, support-capacity calculation,
cancellation handling and content cadence," and `first-place.html` promises no
"community, or subscription." Pure no-perk patronage doesn't break the "need us
less" promise, but no doc covers it. It would also compete with *First Place*
as a second offer and needs the same Back Office gate. Revisit a seasonal
format after *First Place* has sold. Any "why I do this" note stays in
Charles's own voice, never in a product
([ADR-009](../../planning/decisions.md#adr-009--faith-framing-convictions-inform-the-work-belief-is-never-required-to-use-it)).

---

## Doc conflicts / open questions

1. **Which paid step comes next.** ADR-015 in
   [decisions.md](../../planning/decisions.md): "The paid step is smaller and in
   the same domain, never more." Against that,
   [`templates/finished.html`](../../products/landing/templates/finished.html)
   says: "*First Place* is the paid next step being tested." The ADR-015 $9
   product "does not exist yet"
   ([guests-sequence.md](../../products/landing/emails/guests-sequence.md)) and
   isn't on [product-ladder.md](product-ladder.md).
2. **Emailing subscribers about a launch.**
   [roadmap.md](../../planning/roadmap.md) Phase 3: "Launch sequence to Phase 2
   subscribers." Against that,
   [MAILERLITE-SETUP.md](../../products/landing/emails/MAILERLITE-SETUP.md): "No
   fourth email, promotion, win-back, or behavior-based branch," and ADR-016:
   "Silence means stop."
3. **What year one measures.** [revenue-ideas.md](revenue-ideas.md): "Does the
   free checklist get downloaded and shared without prompting?" Against that,
   [principles.md](../vision/principles.md) #11: "Measure completion, not
   downloads."
4. **Open:** no doc addresses referral incentives or Patreon-style patronage
   directly. The views above rest on neighboring rules.

Next: [product-ladder.md](product-ladder.md) · [commerce-rules.md](commerce-rules.md)
