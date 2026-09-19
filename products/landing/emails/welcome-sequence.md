# Welcome Sequence — Draft 3

**Rebuilt 2026-09-19 around
[ADR-014](../../../planning/decisions.md#adr-014--completion-is-what-converts).**
Draft 1 delivered three guides on day zero — the same failure the landing page
had, just by email. Handing someone three PDFs produces the feeling of progress
and none of the fact of it.

**One guide. Then a conversation.** Day 3 and day 7 ask questions and offer help —
they deliver nothing. The next guide exists only for someone who finished and
asked for it.

Draft 2 still had me talking: it diagnosed why they might be stuck, and it
offered the next guide in the same breath as the research question. Both are
weight on someone who is already carrying too much.

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

> ★ **Ask, don't tell.** Draft 2 diagnosed why they might be stuck. That is still
> me talking, and it hands them a paragraph to read when the problem is that they
> already have too much to read. **One question. Easy to answer. Offer help.**

**Subject:** How's it going?

> Just checking — how did you get on with [THE ONE ACTION]?
>
> Three honest options, pick one and hit reply:
>
> **Done** — and I'd like to hear how it went
> **Started, didn't finish** — tell me where you got stuck
> **Haven't yet** — also completely fine, and worth saying why
>
> One word is a real answer. I read every reply.
>
> If something in the guide didn't make sense, or you hit a bit I didn't cover,
> tell me that too — that's the most useful thing you could send me.
>
> — [name]

**No attachment. No new material. No next guide.** The email is a question.

---

## Email 3 — Day 7 ★

> ★ **The research channel.** Still no offer of anything. Someone who hasn't
> finished should not be handed another thing to not finish.

**Subject:** What are you stuck on?

> Last one from me unless you write back.
>
> Everything I sent you is stuff I had to be taught. Which means there are gaps —
> things Dave never thought to mention because they were obvious to him, and
> things I never thought to ask because they were obvious to me.
>
> So: **what's something about running a home or a life that you had to figure
> out on your own, and felt like you should have already known?**
>
> Hit reply. One line is fine.
>
> If you're sitting there thinking your question is too basic to ask — that's the
> exact feeling this whole thing exists to fix. Ask it.
>
> — [name]

---

## After day 7: branch on what they said

**This is the part that matters.** The sequence stops delivering and starts
responding. Nothing else goes out on a timer.

| They said | Send |
|---|---|
| **Done** | Congratulate them, specifically. *Then* ask what they want next — and only then name a guide. |
| **Stuck on X** | Help with X. A few lines, in the email. **Not a guide.** The answer, or the smallest next step. |
| **Haven't started** | One short note: cut the action smaller, name a specific evening. Nothing else. Then leave them alone. |
| **A question** | Answer it. Personally. That's the whole job. |
| **Silence** | **Nothing.** See below. |

### The rule on offering the next guide

**Only after someone says they finished, and only when they ask for more.**

Offering another guide to someone who hasn't finished the first is exactly the
overload this whole model exists to prevent — the pile builds, the thousand-yard
stare sets in, and they stop opening anything at all. A guide unoffered costs
nothing. A guide offered at the wrong moment costs the relationship.

### The rule on silence

After day 7, someone who hasn't replied gets **nothing further on a schedule.**

They are not a lead to be nurtured. They took a guide, and either it helped or it
didn't. Continuing to email them turns a useful thing they received into a
channel they resent.

Write to them again when there is genuinely something new and worth their
attention — not a drip, and not because it's been a while.

---

## What "help" means right now

Honestly: **it means you replying personally.** There is no paid support tier, no
1:1 offer, nothing to sell them. At this list size that's fine, and it's also the
research channel — every reply is data the repo doesn't have.

**It does not scale**, and it shouldn't be promised as though it will. At a few
hundred subscribers this is the most valuable hour a week in the business. At a
few thousand it becomes something else, and that's a problem worth having later.

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
- [ ] Tag repliers by what they said (done / stuck / not started) so the branch
      table is actually actionable
- [ ] **Turn off any automation after day 7.** No drip. Silence means stop.
