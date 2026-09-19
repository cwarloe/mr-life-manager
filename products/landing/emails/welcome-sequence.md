# Welcome Sequence — Draft 2

**Rebuilt 2026-09-19 around
[ADR-014](../../../planning/decisions.md#adr-014--completion-is-what-converts).**
Draft 1 delivered three guides on day zero — the same failure the landing page
had, just by email. Handing someone three PDFs produces the feeling of progress
and none of the fact of it.

**One guide. Then ask whether it got done. The next one comes after action, not
after a timer.**

Plain text. No header images, no template chrome. Voice is the apprentice, not
the expert.

---

## Setup in MailerLite

The signup form carries a hidden `guide` field set by the question on the
landing page — `first-apartment`, `household-agreement`, or `how-often`.

Branch the automation on it so day 0 sends **only** the guide they chose. Same
three emails, one attachment each.

---

## Email 1 — Immediate

**Subject:** Here's your [guide name]
**Alt to test:** The one you picked

> Here it is — attached.
>
> **Don't read the whole thing.** Open it, find the first thing you can do today,
> and do that. Twenty minutes is plenty. The rest will still be there.
>
> If you only do one thing from it, do [THE ONE ACTION — varies by guide].
>
> ---
>
> A word on where this comes from. Mr. Life Manager is a real person — Dave, who
> knew how to run a home and taught me over a lot of years. When I told him
> people would pay to learn this, he was baffled. He said it was all obvious, and
> he'd be embarrassed telling people things he assumed they already knew.
>
> Which is exactly why nobody ever told you. The people who know this can't see
> it as knowledge.
>
> I'll check in in a few days. Nothing to buy.
>
> — [name]

**The one action, per guide:**

| Guide | The one thing |
|---|---|
| First Apartment | Photograph every room before you unpack |
| Household Agreement | Sit down together and fill in section 2 — who owns what |
| How Often | Tape it inside a cabinet door and do tonight's ten-minute reset |

---

## Email 2 — Day 3 ★

**Subject:** Did you do the first bit?

> ★ **The pivot of the whole sequence.** Not new content — a nudge, and
> permission to have not done it. Most sequences send more. This one asks.

> Quick one. Did you get to [THE ONE ACTION]?
>
> **If you did** — good. That's genuinely the hard part. The rest of the guide is
> the same move repeated, and it gets easier each time.
>
> **If you didn't** — that's normal, and it isn't a character problem. It's
> usually one of two things:
>
> *It felt too big.* Cut it smaller. Not "photograph the apartment" — photograph
> one room. Not "fill in the agreement" — just the dishes line.
>
> *You forgot.* Which is a system problem, not a you problem. Put it on the
> calendar for a specific evening, with a time attached.
>
> That's it. No new reading. Just the one thing.
>
> — [name]

---

## Email 3 — Day 7 ★

**Subject:** What are you stuck on?

> ★ **The research channel, and still the most valuable email here.** Reply to
> every single response personally — that is where the next product comes from.

> Last one for now.
>
> Everything I sent you is stuff I had to be taught. Which means there are gaps —
> things Dave never thought to mention because they were obvious to him, and
> things I never thought to ask because they were obvious to me.
>
> So: **what's something about running a home or a life that you had to figure
> out on your own, and felt like you should have already known?**
>
> Hit reply and tell me. One line is fine. I read all of them, and I answer.
>
> If you're sitting there thinking your question is too basic to ask — that's the
> exact feeling this whole thing exists to fix. Ask it.
>
> And if you finished the guide and want the next one, just say which problem
> you're on. I'll point you at it.
>
> — [name]

---

## After the sequence

**Do not drip more guides on a schedule.** The next one goes out when they ask,
or when they say they finished. That's the whole principle — material arrives
behind completion, not ahead of it.

Pacing this way also gives the list a job beyond delivery, which is a reason to
stay subscribed rather than a reason to unsubscribe after the dump.

---

## Notes

**Why three and not five.** More emails means more chance of sounding like a
funnel. Three teaches, asks, and stops.

**Nothing to buy in any of them.** There's nothing to buy yet — and when there
is, this sequence stays clean. The free tier's job is earning the right to sell
later, not selling now.

**Dave appears in email 1 and nowhere else.** He's the credibility, not the
gimmick. Introduce him once, properly, and let it sit.

## Before sending

- [ ] Branch the automation on the `guide` field — day 0 sends **one** attachment
- [ ] Fill in the one-action line per guide from the table above
- [ ] Fill in the sign-off name
- [ ] Send the whole sequence to yourself and read it on a phone
- [ ] **Decide who answers the day-7 replies, and commit to it.** An unanswered
      reply is worse than never asking.
- [ ] Set up a way to record who says they finished — that's the completion
      metric, and there's no other instrument at this scale
