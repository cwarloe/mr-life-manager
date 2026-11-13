# Sequence — "Someone's coming over" (Draft 4)

**Entry:** [`/guests.html`](../guests.html). Tagged `guide=guests` on the form.
**Status:** Active in MailerLite per owner 2026-09-22. Reader validation remains open.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

**Replaces** the withdrawn site-wide Draft 3 welcome sequence for this entry
only — see [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally).
Per-entry sequences (not one site-wide welcome) per [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The Week (one page), plus one named action | one weekly plan |
| 2 | Day 3 | The same thing, smaller | the sink |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

It shrinks **unconditionally** — nobody is branched on opens, clicks, or any
guess about whether they did it. A **reply** or a **purchase** takes someone out
of the sequence and into a conversation. Nothing else does.

---

## Email 1 — immediate

**Subject:** Here's the thing worth printing

> The guest-area checklist and a weekly routine do different jobs. Here is the sheet for keeping the areas you have finished usable.
>
> Here's the one page I'd print.
>
> https://mrlifemanager.com/print/the-week.pdf
>
> It's one page, adapted from Dave's weekly schedule. The top is a nightly close-out: empty the sink, wipe the counters and table, and return things to their homes. Below are weekly jobs with space to write your start times. Cross out spaces you don't have, and finish the applicable jobs by Sunday evening.
>
> Print it and stick it inside a cabinet door. Your guest area is ready; other areas and the temporary clutter basket may still need work. Use the reset space to name the next job, its finish, and its start time.
>
> — Charles

*Link (not attach): <https://mrlifemanager.com/print/the-week.pdf>*

---

## Email 2 — day 3

**Subject:** The shorter version

> A full nightly close-out can be more than you can take on tonight. Here's one job with a clear finish.
>
> So here's the version that fits anywhere.
>
> Just empty the sink before you go to bed. That's it.
>
> Allow time for the dishes you actually have, including soaking or handwashing. Leave the sink empty; the counters and putting things away are separate jobs tonight.
>
> It's the one that does the most work. A kitchen with an empty sink looks under control even if you haven't touched anything else, and walking into that in the morning changes how the whole day starts.
>
> Some nights it won't happen, and that's fine. This isn't a streak and there's nothing to reset.
>
> — Charles

---

## Email 3 — day 7

**Subject:** One question

> There's nothing attached to this one.
>
> I'm trying to figure out what to write next, and the most useful thing anyone has told me so far came out of a question like this one.
>
> Which room do you avoid?
>
> One word is a complete answer. Just hit reply. It's me reading these, not a system.
>
> — Charles

Then the sequence ends. **Silence means stop.**

---

## The rules this is built on

- **It shrinks unconditionally.** Every email asks less than the last, for
  everyone. We never infer behaviour, so we can never imply we know someone
  failed.
- **No question with a wrong answer.** "Which room do you avoid?" has none.
  Draft 3's *"Done / Started, didn't finish / Haven't yet"* had two.
- **Never reference what they did or didn't do.** Not once in three emails.
- **When something didn't land, it's ours out loud.** Email 2 opens with
  *"that's my fault for leading with it"* rather than asking why they stopped.
- **No streaks, no progress language, no "still haven't…".** Email 2 says so
  explicitly: *"It isn't a streak, and nothing resets."*
- **Silence means stop.** Carried from Draft 3, which got this part right.

## What happens on a reply

A reply is a person, so a person answers — not an autoresponder and not a
sequence. Read it, answer the actual question, and if there's a guide that fits,
send **one**. If there isn't, say so and answer anyway. At this volume this is
genuinely doable and it's the only real research we have.

---

## Still open

1. ~~**The printable.**~~ Done — Email 1 links
   <https://mrlifemanager.com/print/the-week.pdf>. Open it before sending.
2. ~~**No paid offer / $9 maintenance product.**~~ **Parked** — under ADR-020
   (Accepted) a $9–19 guide is offered only after a free win; it is a later idea, not an open ship
   item. These sequences stay free-task only (ADR-015 shrinking rule still
   applies if a same-domain paid step is ever un-parked).
3. ~~**MailerLite automation.**~~ **Done** 2026-09-22 (Active per owner). Live
   ops spec: [MAILERLITE-SETUP.md](MAILERLITE-SETUP.md). Keep
   "resend to unopens" off — it violates ADR-016.

Homepage is the pain router to four entry doors (ADR-016); this file is the
guests door only.
