# Sequence — "You're just underwater" (Draft 2)

**Entry:** [`/underwater.html`](../underwater.html). Tagged `guide=underwater`.
**Status:** Active in MailerLite per owner 2026-09-22. Reviewed against house style; reader validation remains open.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The Week, plus one named action | one weekly plan |
| 2 | Day 3 | The same thing, smaller | the sink |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

Shrinks unconditionally. Only a reply or a purchase moves anyone out of it.

**This reader is different from the other doors.** Nothing happened to them.
There's no move and no guest arriving — they've just been underwater for a while,
which means shame is closest to the surface here. Nothing in this sequence
references how they got there or how long it's been.

The page resets the house to baseline. Email 1 reinforces that win
in the page's own words.

---

## Email 1 — immediate

**Subject:** Here's the thing worth printing

> The reset checklist covers the kitchen, one main room, your bed, dirty clothes and waiting mail. Here's a weekly sheet to maintain finished areas and plan what still needs doing.
>
> https://mrlifemanager.com/print/the-week.pdf
>
> It's one page, adapted from Dave's weekly schedule. The top is a nightly close-out: empty the sink, wipe the counters and table, and return things to their homes. Below are weekly jobs with space to write your start times. Cross out spaces you don't have, and finish the applicable jobs by Sunday evening.
>
> Print it and stick it inside a cabinet door.
>
> Friday and Sunday have no extra scheduled job. The nightly close-out still applies. Other rooms, sorting the clutter baskets and paying bills remain separate work; write the next job and its time in the reset space.
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
> It does the most work of anything on that page, because a kitchen with an empty sink looks under control even if nothing else has been touched — and walking into that in the morning changes how the day starts.
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

Then it ends. **Silence means stop.**

---

## Still open

1. ~~**No paid offer / $9 product.**~~ **Parked** — under ADR-020 (Accepted) a
   $9–19 guide is offered only after a free win; it is a later idea, not an open ship item and not in
   this sequence.
2. ~~**MailerLite automation.**~~ **Done** 2026-09-22 (Active per owner). Live
   ops spec: [MAILERLITE-SETUP.md](MAILERLITE-SETUP.md). Keep
   resend-to-unopeners off — it violates ADR-016.
