# Business mastery questions and a patronage option

**Status:** Proposal for Charles, 2026-10-04. ADR-010, ADR-015 and ADR-016 are
under review (PR #84), so nothing here relies on them as settled. Web facts were
checked on 2026-10-04 and are linked. Principle numbers refer to
[principles.md](../vision/principles.md).

## Part 1: The three questions

**(a) What business are we in?** Literally, we publish free printable guides and
how-to pages for running a home. There are four entry pages (first night, guests,
one room, underwater), a one-page weekly cleaning plan sent by email, and a
planned $39 product, First Place.

**(b) What business are we really in?** The working answer is "the practical
stuff nobody showed you, at the moment it hurts." The transformation is going
from the house deciding for you to saying yes to your life, without feeling
behind. The docs mostly support this:
- [brand-positioning.md](brand-positioning.md) says competitors sell a feeling
  or a finished result, and we sell competence.
- Saying yes to your life is principle 7: order makes room for people.
- "Without feeling behind" is principle 8, dignity rather than shame.
- The moments model (a moment, a free task, a habit, then the next moment)
  follows principle 11: completion is what converts.

One gap is worth naming. The internal mission in
[mission.md](../vision/mission.md) still names "first-time independent adults."
A moment-based answer serves anyone at the moment, which is wider. Charles
should decide which one governs.

**(c) What business do we need to be in over 3–5 years?** We need to be a
trusted place people come back to at each life moment: a first place, hosting,
moving out, living with a partner, and later money. That requires:
- a free entry page for each of those moments, and most don't exist yet
- a reason to return, such as an email relationship that lasts beyond three
  messages (ADR-016 is open)
- Dave's material captured for money and paperwork, which
  [decisions.md](../../planning/decisions.md) lists as the highest-urgency open
  item
- trust that the free help stays free

**What we really want, measured.** These are candidate metrics. Charles sets the
targets.
1. **Completion rate per moment:** visits to the finished page divided by visits
   to the entry page.
2. **Returning readers:** people who use a second entry page, or who reply to an
   email.
3. **Email signups per completion.**

Why these: principle 11 says to measure completion, not downloads, and the
three-to-five-year goal depends on people coming back.

**Action plan**
1. Ask five real readers what headache the pages relieved, and compare their
   words with our headlines. Use
   [customer-interview-script.md](../research/interviews/customer-interview-script.md)
   and [first-reader-test.md](../research/interviews/first-reader-test.md). No
   file named "week-1 interview pack" exists; these two are the closest match.
2. Confirm which of the three metrics the site can measure today, and set the
   targets.
3. Re-decide ADR-010, ADR-015 and ADR-016 against answer (b).
4. Choose the next two moments.

## Part 2: Patronage (free help plus optional supporter tiers)

**Real examples**

| Creator | Model | Public tier prices |
|---|---|---|
| [How to ADHD](https://www.patreon.com/posts/45678534) | Free videos on YouTube; Patreon | $2, $5, $10, $25, $50, $100 per month |
| [Unf*ck Your Habitat](https://www.patreon.com/posts/updated-cleaning-61731171) | Free advice; Patreon | $1 (downloadables), $3 (Q&A thread), $5 per month; more tiers not shown |
| [A Slob Comes Clean](https://www.aslobcomesclean.com/podcasts/) (Dana K. White) | Free podcast; Patreon | From $9 per month: printables, Facebook group, Zoom calls, work-along sessions |
| [Mercury Stardust](https://www.patreon.com/mercurystardust) | Free how-to videos; Patreon | Page data lists $3, $10, $20, $35 and $50 per month; tier names and perks not checked |

**Perks that fit our principles.** None of these gate the help:
- supporter credit on an "about" page
- early drafts of the next guide, with a request for comments
- a vote on the next moment we build
- a short quarterly note on what is being built and why

These fit principle 9 (simple enough to keep) and principle 8 (dignity). They
also never charge for the help itself, which keeps faith with principle 11's
warning about squeezing people before they finish anything.

**Off-limits perks.** Each of these would gate the help:
- printables or downloads behind a paywall (the $1 tier above)
- private Q&A answers that are never published
- a paid version of the weekly plan
- rewards for sharing or referrals, which Charles has ruled out

**Platforms** (published fees, checked 2026-10-04)

| Platform | Platform fee | Payment processing | Payouts | Fit with our static site and MailerLite |
|---|---|---|---|---|
| [Patreon](https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview) | 10% (new creators since Aug 4, 2025) | 2.9% + $0.30 (US cards) | Payout fee applies | Link out; members live in Patreon, a second list |
| [Buy Me a Coffee](https://help.buymeacoffee.com/en/articles/8105744-how-to-calculate-charges-on-your-payment) | 5% | Stripe 2.9% + $0.30; +0.5% subscriptions; +1% international; 0.5% payout | Weekly via Stripe, after a $10 minimum | Link or button; no monthly cost |
| [Ko-fi](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee) | 0% on one-off tips (Free); 5% on memberships; 0% with Gold ($12/mo) | PayPal or Stripe fees (about 3% + $0.30) | Direct to your PayPal or Stripe | Link or button; no monthly cost |
| [Memberful](https://memberful.com/pricing) | $49/mo + 4.9% | Stripe fees | Your Stripe account | Embeds anywhere; MailerLite not in its listed integrations |
| [Substack paid](https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost) | 10% | Stripe fees | Your Stripe account | Poor: a second email list, split from MailerLite |
| [MailerLite paid newsletters](https://www.mailerlite.com/paid-newsletter-platform) | 0% commission; plan cost scales with subscribers | Stripe fees | Your Stripe account | Same list we already use, but it sells paid email content, which gates help |

**Gift buyers, institutions and First Place.** Patronage is a different motive
from buying. Buyers want a product for themselves or someone else; patrons want
the free help to exist.
- **Gift buyers and institutions:** they buy or license products (the open
  question in ADR-010; licensing in [business-model.md](business-model.md)).
  They should never be routed to patronage.
- **First Place ($39):** it stays the product. Patron tiers should not discount
  or bundle it, so the two asks stay separate.
- **Principle 11:** never put a patron ask on the same page as an entry task or
  the First Place offer.

**Risks**
- **Small audience early.** Only a small share of an audience pays. The one
  published data point found is from music, not our field: top musicians on
  Patreon converted about 1% of their largest social following, and 94% of
  music creators had fewer than 100 patrons
  ([Hypebot, 2024](https://www.hypebot.com/how-many-fans-do-musicians-need-to-be-successful-on-patreon/)).
  The rate for home-help readers is unverified.
- **Perk upkeep.** Calls, groups and monthly posts are recurring work, and they
  compete with building moments (principle 9).
- **The "free help" trust signal.** A visible paywall next to free help makes
  readers wonder what is being held back.

**For Back Office** (questions only, not answered here)
- Is patron income reported differently from First Place sales?
- Who collects sales tax on memberships: the platform or us? And on First
  Place?
- Do we need a business entity or a separate Stripe account first?
- Which MailerLite plan covers paid subscriptions, and at what cost?
- What refund policy applies to patrons?

## Recommendation (Charles's judgment)

Don't launch patron tiers now. The audience is too small for a 1%-scale share to
pay for the upkeep, and the first job is proving completion and return visits.

When a trigger that Charles sets is met, add one quiet support link, Ko-fi
(0% on one-off tips) or Buy Me a Coffee. A suitable trigger would be a list size
or a steady number of returning readers. The link should go on the about
section only, with no monthly cost. Patreon-style tiers make sense later, once
returning readers are steady and someone can keep the perks up without slowing
new moments.
