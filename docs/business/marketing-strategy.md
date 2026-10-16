# Marketing strategy: the moments model

**Status:** Proposal for Charles's decision, 2026-09-30. This page sits above
the messaging strategy in draft PR #56, and copy decisions should follow from
it. Nothing here has been tested with readers. Principle numbers refer to
[principles.md](../vision/principles.md).

## Who we serve, and the problem

We serve adults running a life nobody taught them how to run. That means
keeping a home, doing laundry, living with other people, and later managing
money. They are not failing. The gap hurts at specific moments:
- the first night in a new place
- someone coming over
- the place getting away from them
- a room they avoid
- a conflict with a roommate

For hosting, the state of the house decides for them: it says no before they
can say yes to people. Most clean in bursts, and many have tried chore-chart
apps that left them feeling behind.

## The promise

Mr. Life Manager gives people the practical things nobody showed them, at the
moment they need them. The methods come from Dave, who knew how to run a home,
and they are passed on by someone who had to learn them the hard way. We do not
promise a clean house, and we do not promise to get anyone organized.

## The pattern

1. A person arrives at a moment.
2. The entry page for that moment gives them one free task they can finish
   right away, with no signup or download in the way.
3. After they finish, we offer an email signup for the small weekly routine
   that keeps the moment from happening again.
4. The next moment brings them back. Each paid product handles one bigger
   moment.

## What follows, and what each choice costs

**1. We market moments, not cleaning.** Each moment gets its own entry page
and can get its own flyer.
- **The cost:** we own no single category, and broad searches like "cleaning
  schedule" are weak ground for us.
- **How we compete:** we use flyers where the moment happens, entry pages in
  people's exact phrases, and word of mouth.
- **Principle 11:** "the one thing that matches where the person actually
  is."

**2. The homepage routes people to entry pages. It does not sell.** It already
asks "What's going on right now?" and links the four entry pages, but it also
points to the $39 First Place offer, the pilot page for parents and
institutions, and a request to name a missing moment.
- **The fix:** remove those three. Principle 11's offer filter allows one ask,
  not four.
- **The cost:** the homepage never sells anything directly.

**3. The email list is our main asset.** Keep the first three emails as they
are. Each one asks less than the one before, and none implies the reader fell
short (principle 8). After that, send a useful email about once a month, each
about a moment the reader is likely to face next (principle 3, prevention over
crisis).
- **The risk:** becoming an ignored newsletter, so an email that doesn't help
  with a specific moment is not sent.
- **Needs Charles's decision:** a monthly email conflicts with two rules.
  ADR-016 ends the sequence after email 3 ("silence means stop"), and
  MAILERLITE-SETUP forbids a fourth email. Principle 11 also says to pace
  delivery "behind action," not on a schedule.

**4. Paid products cover bigger moments.** They are sold once, not by
subscription. First Place ($39), for setting up a first home, is the current
example. Price follows the size of the moment.
- **What this settles:** PR #48's $39-versus-$9 conflict. The two prices fit
  moments of different sizes, and ADR-015's 2026-09-25 note already separates
  them.
- **The cost:** revenue is less predictable, and we need enough moments
  covered to have something to sell at each.
- **Principle 11:** someone who finished one task buys the next.
- **Needs Charles's decision:** ADR-015 says the paid step is "smaller and in
  the same domain, never more." A product for a bigger moment contradicts that.

**5. The voice gets simpler because the promise is clear.** Every page, email
and flyer names the moment, says what we will help with, and says what happens
next. PR #56's communication principles still apply (principle 8, dignity).

**6. We choose the next moments deliberately.** A moment earns an entry page
when it is common, happens at a clear time, and can be reached by a flyer. The
known gaps are:
- money
- a first car
- moving out (the free Move-Out Checklist in
  [product-ladder.md](product-ladder.md) is not built yet)
- moving in with a partner (the homepage names it as next, but it has no
  entry page)
- roommate conflict (a free guide exists, the Household Agreement, but no
  entry page does)

Moving in and moving out fit best and should come next (principle 11).

## Who the audience is

The docs disagree. ADR-010 aims the marketing at the overwhelmed adult already
running a household (Dana). [target-audiences.md](../vision/target-audiences.md)
still says to build the MVP for Tyler, who is leaving his parents' home.

This strategy defines the audience by the moment, not a persona: whoever is
spending a first night in a new place is that page's audience, at 23 or 34.

**Needs Charles's decision:** this replaces the persona ranking as the basis
for marketing. ADR-010's decision about who pays still
stands.

## The test for every page, email and flyer

Does it help the reader handle the moment they are in, and say yes to their
life, without making them feel behind? The copy never shames the house or the
person, and it never calls the reader lonely. This serves principles 7
(hospitality) and 8 (dignity).

## What changes next

1. Charles settles the promise.
2. The homepage is restructured so it only routes people to entry pages.
3. Charles decides whether email continues after email 3 (ADR-016, principle
   11).
4. The signup form and email copy are rewritten from the promise, using PR
   #56's principles.
5. The next two moments are chosen. Moving in and moving out are proposed.
