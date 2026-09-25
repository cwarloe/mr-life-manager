# Entry Page Brief — "Someone's coming over"

**Status:** Built 2026-09-20. [Sequence](../emails/guests-sequence.md) active per owner
2026-09-22. Not yet tested with a reader, and no traffic source.
**URL:** `/guests.html`
**Implements:** [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email)
— the first page built to that architecture.

---

### The shape

One pain → one page → one action → one win → then the email. Self-contained: it
does not route to the main page, and it links to no other guide. The only outbound
link is a quiet "What this is" in the footer, for the curious.

### Decisions worth recording

**The action is free and above the fold-ish.** No form, no download, no gate. The
frame at the top says so explicitly — *"Nothing to sign up for. Start at one."*
The email is asked for once, at the bottom, after the work.

**Ordered by visible difference per minute, and the order is the anti-shame
mechanism.** *"Do them in order and stop when they knock."* Because the biggest
wins are first, stopping anywhere still leaves the reader better off than any
other ordering would have. **There is no way to fail this page** — which matters
for an audience whose documented core wound is shame about not knowing.

**Mobile-first.** 17px base, single column, large numerals, no tables, no
horizontal scroll. The reader is standing in a room holding a phone.

**The basket is admitted to be a trick.** Step 3 says so in bold before the reader
finds out for themselves. Concealing it would have bought ten minutes of goodwill
and lost all of it tomorrow morning.

**The basket is also the bridge.** The "About that basket" section turns tomorrow's
annoyance into the actual teaching — *almost everything in it has nowhere to live* —
which is [everything-has-a-place](../../../frameworks/everything-has-a-place.md)
arriving at the one moment the reader has just felt the problem. This is what earns
the maintenance offer instead of asserting it.

**Dave is named here — first name only.** First time in a shipped product. It
sits *after* the win, where it reads as provenance rather than onboarding. This
resolves the open question flagged in the
[What Is This Room For? brief](../../checklists/room-for/brief.md) in favour of
naming him.

**"Dave," not "Dave Webster," and "decades," not a number.** Founder's call,
2026-09-20: the surname adds no credibility and reads as a claim being made;
first name reads as a friend, which is what he is. "Decades" is both more
accurate than counting from the oldest document we happen to hold, and more
interesting than a figure. **Applies everywhere, not just this page** — treat it
as the house style for referring to him in product copy.

**"What just happened" is its own callout.** Dave's crisis-versus-preventative
framing was originally a trailing paragraph in the basket section, where it read
as an afterthought. It's the hinge of the whole page — it names what the reader
just did and why they'll need it again — so it now gets a bordered block of its
own, visually distinct from the amber safety note.

**The offer is smaller, not bigger.** *"Dave's week on one page"* —
[The Week](../../print/the-week.html), led by his ten minutes a night. Per
ADR-015, never a bigger pile of guides.

**One amber safety note**, on mixing bleach with ammonia or vinegar. It clears the
[depth rule](../../../content/README.md) — a competent person would simply tell
you, and someone rushing with two bottles in a small bathroom is the exact
situation where it matters. Rebuilt 2026-09-20 after it read badly on a phone:
the label is now its own element rather than a block-level `<b>` inside the
paragraph, and the body is broken into short lines instead of one dense block.

### Voice

Plain, not commanding — per ADR-015. No "EXECUTE NOW", no congratulation, no
video, no face. The closest it comes to an order is *"That's the whole job."*

The last line of the stop section — *"Don't apologise for the place when they walk
in. They weren't going to notice, and saying it out loud is what makes them look."*
— is doing brand work rather than cleaning work. It's the one moment the page
addresses the shame directly, and it's placed after the labour rather than before.

### Untested assumptions

1. **That the order is right.** Bin/smell first is a judgement call; a reader in a
   panic may expect visible clutter first and bounce when told to take the bin out.
   The most likely thing to be wrong on this page.
2. **That admitting the basket trick builds trust rather than deflating the win.**
3. **That step 6 (lights) lands as a revelation rather than as filler.** It's the
   cheapest, highest-leverage step and the easiest to dismiss.
4. **That thirty-five minutes is the right size.** Someone with ten minutes may
   read "35" and close the tab. Possible fix: lead with "stop whenever" harder, or
   state a ten-minute version up front.

### Not built yet

- **The $9 maintenance product** the section gestures at.
- **Traffic.** There is none. The page is a bet on search intent that has nothing
  pointing at it yet.
