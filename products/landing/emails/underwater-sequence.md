# Sequence — "You're just underwater" (Draft 2)

**Entry:** [`/underwater.html`](../underwater.html). Tagged `guide=underwater`.
**Status:** Reviewed 2026-09-21 against house style and the first-night / guests sequences. Not sent.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The Week, plus one named action | ten minutes |
| 2 | Day 3 | The same thing, smaller | the sink |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

Shrinks unconditionally. Only a reply or a purchase moves anyone out of it.

**This reader is different from the other doors.** Nothing happened to them.
There's no move and no guest arriving — they've just been underwater for a while,
which means shame is closest to the surface here. Nothing in this sequence
references how they got there or how long it's been.

The page's "floor" is a foundation under the week, not a mopped floor. Email 1
has to say that in the page's own words, or it reads like we think they cleaned.

---

## Email 1 — immediate

**Subject:** Here's the thing worth printing

> You put a floor under the week tonight. Here's the thing that keeps it there.
>
> https://mrlifemanager.com/print/the-week.pdf
>
> It's one page, and it's Dave's whole system. The top of it is ten minutes you do before bed — empty the sink, wipe the counters, walk one lap and put things back. Underneath that there's one job for each day, and two days with nothing on them at all.
>
> Print it and stick it inside a cabinet door.
>
> The two empty days are the important part. This isn't a system that needs you to be different. It's a system that assumes some days you've got nothing left.
>
> — Charles

*Link (not attach): <https://mrlifemanager.com/print/the-week.pdf>*

---

## Email 2 — day 3

**Subject:** The shorter version

> Ten minutes a night is the right answer, and it's also more than most people can start with. That's my fault for leading with it.
>
> So here's the version that fits anywhere.
>
> Just empty the sink before you go to bed. That's it.
>
> It takes about four minutes most nights. Skip the counters, skip the lap around the room. Just the sink.
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

## Not done

1. **No paid offer**, deliberately — the $9 product doesn't exist. Insertion
   point is after email 3.
2. **MailerLite:** group `entry-underwater`, automation keyed on
   `guide=underwater`, 0 / 3 / 7 days, no re-entry, resend-to-unopeners off.
