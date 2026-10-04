# Audience Brief — Having People Over

**Status:** Proposed 2026-09-29. Not adopted; nothing here is live.
**Scope:** Flyers and signup wording for adults already running a home, where
the state of the place is what keeps people from coming over.

Governed by [ADR-010](../../planning/decisions.md#adr-010--beachhead-keep-the-audience-change-the-payer),
[ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email)
and [principles](../vision/principles.md) 7, 8 and 11. Where this page
conflicts with them, they win.

**Parked 2026-09-29:** segment B ("I don't have people over") is parked by
Charles. Work continues on segment A only: people with a visit already
planned sometime this week. Segment B's material below stays for reference
and is not in use.

---

## Who this is

An adult who has run a home for years. They'd have people over, but the place
has gotten ahead of them and they don't know where to start. They are standing
in it, holding their own phone. This is close to Dana in
[target-audiences.md](../vision/target-audiences.md) ("Won't invite people over,
which is now costing her friendships"), and to the loop in
[customer-problems.md](../research/customer-problems.md): "Can't host, so
relationships stay shallow."

**Not:** students, first-timers, parents buying for someone else, or anyone a
helper sends the page to.

The isolation behind this is Charles's observation. Public background: the
U.S. Surgeon General's advisory on social connection,
<https://www.hhs.gov/surgeongeneral/reports-and-publications/connection/index.html>.
No figures from it go into copy.

**A. "Someone's coming."** A visit is set, and the house feels like the
problem. *Where do I start, and is there time?* → `/guests.html`

**B. "I don't have people over."** No visit is planned, and the house is part
of why. *I'd have to fix everything first.* → `/underwater.html`

## Copy rules

- Never call the reader lonely or isolated. The only reference is the good
  outcome: someone at your door.
- Never judge the house (principle 8, *Dignity, not shame*). No urgency or
  scarcity.
- The reader's own next step is the only focus. No sharing or referral ask in
  the flow (Charles's rule).
- One offer per piece: one QR, one page (principle 11).
- The headline matches the page (ADR-015: "The query is the headline").

**On "disaster."** `guests.html` opens "Someone's coming over and your place is
a disaster." On the page, the reader chose that situation. On a flyer, a
stranger is labeling their home. Soften the flyer and keep "Someone's coming
over" as the shared phrase. Whether the page also changes is Charles's call.

## Flyers

The QR goes to the page plus `?from=flyer-<segment>-<spot>`.

| | Headline | Support line |
|---|---|---|
| A | Someone's coming over, and the place isn't ready? | Six things, biggest difference first. It still works with ten minutes. |
| A | Someone's coming over this weekend? | Start with the trash and a window. Stop when they knock. |
| A | Said "come over," then looked around? | Wherever you stop is the right place to have stopped. |
| B | Nothing particular happened. The place just got ahead of you? | Six things that put a floor under it. The first two count on their own. |
| B | Want the place back to where you'd say "come over"? | Start with a fifteen-minute kitchen reset. |
| B | The week won, and the kitchen shows it? | Fifteen minutes on the kitchen. That's the whole first move. |

- **A** (`/guests.html?from=flyer-a-grocery`): grocery-store community board,
  bakery or party-supply counter, apartment package room. All need permission.
- **B** (`/underwater.html?from=flyer-b-laundromat`): laundromat, public library
  board, apartment mailroom. The library usually needs approval; the others
  need permission.

## Signup success line

One fixed view for all eight pages, so it can't name a guide. Baseline: "The
Week is on its way. Tape it up tonight and empty the sink before bed."

1. "Check your inbox. The Week is on its way. Tonight, just empty the sink
   before bed."
2. "The Week is coming by email. If you do one thing from it tonight, empty the
   sink before bed."

[operations.md](../../planning/operations.md) logs the test as "confirm →
correct `entry-*` group → Email 1," which suggests double opt-in. If so, only
option 1 is accurate. Mailer Bot would set it.

## Conflicts / open questions

- [target-audiences.md](../vision/target-audiences.md): "Build the MVP for
  **Tyler**." ADR-010: marketing addresses "The overwhelmed adult already
  running a household." This brief follows ADR-010.
- [brand-positioning.md](brand-positioning.md): "Compete on the transition."
  target-audiences.md: "Nobody buys this on an ordinary Tuesday." Segment B has
  no moment; its page opens "Nothing particular happened."
- Charles's no-referral rule vs. #52 (merged), which put a share QR on The Week
  that email 1 delivers, and #51 (open), which adds "Free to share" to all
  twelve entry emails.

## Gaps

- **Reset to "I invited someone."** Nothing covers the step from a reset home to
  asking someone over. Recorded as a gap only.
- `underwater.html` never mentions company, so B's second headline promises one
  step more than the page delivers.

## Measuring

Entry pages carry `?from=` to the completion page. Visitor analytics were not
installed as of 2026-09-22, so scans can't be counted until Charles approves a
beacon. Until then: signups by group (`entry-guests`, `entry-underwater`) and
replies to email 3. One segment and one spot type at a time (operations.md
growth block), recorded in the [scorecard](../../planning/monthly-scorecard.md).

**Charles approves:** every flyer and spot, each permission request, the
analytics beacon, and the success line.
