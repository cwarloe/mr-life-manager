# Side quest: the "are you ready?" step (proposal)

**Status:** Proposal for review, 2026-11-16. Nothing here is on the site. Wording
is draft and follows the plain-speech rule in
[`content/README.md`](../../content/README.md).
**Picture of the flow:** [side-quest-mock.png](side-quest-mock.png) (student look; four screens).

## What Charles said

People can do almost everything around the house with a few staples. If you
have white vinegar and water on hand, you don't need the special product. The
page where we ask "are you home?" needs a quiet third option for people who
aren't ready: a **side quest** to get ready. And if they haven't done it, they
can't really do the main thing anyway. So: ask "do you have the stuff?" before
(or along with) the calendar picker. Find the name and the solution.

## The idea in one paragraph

Every checklist already says "grab these first," but it's a paragraph people
skip, and the calendar picker lets someone commit to a time without checking
they can do the job. We turn the supply list into a **one-tap kit check**. If
they have everything, nothing changes. If something is missing, they get a
**side quest**: a short, time-boxed errand to get it, with its **own calendar
entry** before the main time. Both go on the calendar in one tap.

## The name

| Option | Who it fits | Verdict |
|---|---|---|
| **Side quest** | Students, anyone who games or uses the word | **Recommended.** It's Charles's idea, it says "optional but it unlocks the main thing," and it's how many people in the audience really talk. Always paired with plain words under it ("check you've got the staples") so nobody has to decode it. |
| Pre-flight check | Military, career | Good second skin for those pages. Test it. |
| Staging / load out | Military | Real jargon in some units. Test, don't assume. |
| Kit check | All | Plain and clear. A fine fallback label. |
| Gear up, Stage it, Prep run, Warm-up | | Cute, but less clear about what you do. Skip. |

Rule: the label is "Side quest" and the plain gloss always follows it. If
reviewers say "side quest" sounds like a game to career or military readers,
switch those pages to "Pre-flight check" or "Kit check" with the same screens.

## Where it goes: three options

| | What | For | Against |
|---|---|---|---|
| **A. A gate before the fork** | A kit screen in front of "home or not home" | Simple to explain | Adds a tap for every reader, including the ones who have everything. People scanning a flier are already not home; making them answer first loses the most starts. |
| **B. Inside each branch** | Home: check at step 1. Not home: suggest it after they pick a time | Nothing in the way | Two different pieces of code and wording |
| **C. One kit check with three doors (recommended)** | The same kit check, reachable from (1) a quiet third link under the two buttons, (2) a "step 0" if they tap Start without checking, and (3) a suggestion after they pick a time | One component, nothing blocks anyone, ready people lose no taps | The third link has to be quiet enough not to compete with the two buttons |

**Why not a hard lock.** "You can't start until you've checked the kit" would stop
the people who already have everything and the people who'd rather just try. The
repo's rule is guardrails that keep people moving toward action, not walls that
send them away (ADR-021 says the same about snoozing). So the check is
**honest, not locked**: the page says what step 1 needs, and one tap says "I've
got them all."

## The staples kit

Built on the repo's own rule: the
[commerce rules](../business/commerce-rules.md) name the core low-cost path as
dish soap, baking soda, distilled white vinegar and microfiber cloths. For the
checklists that clean, the kit is these six:

1. White vinegar
2. Dish soap
3. Two cloths
4. Trash bags
5. A basket or box
6. A spray bottle

Each checklist adds only what it truly needs (below). The kit stays the same
size on every page, and the page says "most of this you already have."

| Workflow | The staples apply | This one adds | Notes |
|---|---|---|---|
| 1. Dishes and mess | all six | a laundry hamper | |
| 2. Company | all six | a toilet brush, a clean hand towel, a broom or vacuum | |
| 3. Table | trash bag, cloth, basket or box | nothing | The smallest kit. The check can be one line. |
| 4. First night | none of the cleaning staples | the essentials: phone, key, bedding, toilet paper, soap, a towel, toothbrush and toothpaste | Different kit: personal items, not cleaning. Side quest is "find your essentials box." |
| 5. Spare room | trash bags, basket or box, cloth | boxes, labels or paper and tape, a broom or vacuum | |
| 6. Still unpacking | trash bags, basket or box, cloth | scissors or a box cutter, labels or tape, a broom or vacuum | |

## Where I'd push back: "vinegar and water does almost everything"

It does a lot, and it fits the low-cost path. Two limits are already repo rules
and have to stay on the kit screen:
- **Not on natural stone** (granite, marble) or anything where an acid is wrong
  (commerce rule 7). Point to the manufacturer's care guidance.
- **Never mix it with bleach**, or any other cleaner (commerce rule 6).
- **It cleans; it doesn't disinfect.** Commerce rule 5 already says disinfecting is
  situational. The bathroom step says "cleaners made for those surfaces," so the
  kit shouldn't promise more than that.
"Equal parts vinegar and water" is the usual mix, but the repo doesn't state a
ratio. **Confirm it before it ships.**

## The screens (draft wording)

All screens are drawn in [side-quest-mock.png](side-quest-mock.png).

**1. The page after the scan** (the two buttons stay as they are). Under them, a
quiet third link:
> **Side quest: check you've got the staples**
> Vinegar, dish soap, cloths. 3 minutes, and you'll need them for step 1.

**2. The kit check** (opens from the third link, or as step 0 if they tap Start
without checking):
> **SIDE QUEST**
> **Do you have the staples?**
> You can clean almost everything in your place with these. Tap the ones you've got.
> ☐ White vinegar ☐ Dish soap ☐ Two cloths ☐ Trash bags ☐ A basket or box ☐ A spray bottle
> *(all ticked:)* **[ I've got them all. Let's go. ]**
> *(any unticked:)* **[ I'm missing something. ]**
> Half vinegar, half water in the spray bottle cleans counters, sinks and glass.
> Not on stone like granite or marble. Never mix it with bleach.

**3. The side quest** (when something is missing):
> **SIDE QUEST**
> **Pick up a basket or box, and a spray bottle.** *(the unticked items)*
> About 10 minutes. Any grocery or dollar store has both.
> **[ Copy my shopping list ]**
> **When will you pick them up?** [ Tonight, 6:00 p.m. ] [ Tomorrow, 6:00 p.m. ]
> Then you'll pick the day and time for the main thing, after your side quest.
> **[ Next: pick the main time ]**

**4. Decided** (one tap puts both on the calendar):
> **That's decided:**
> **SIDE QUEST. Friday, 6:00 p.m.** Pick up a basket or box, and a spray bottle.
> **MAIN THING. Saturday, 10:00 a.m.** Wash the dishes and pick up your place.
> **[ Add both to my calendar ]**  **[ Ask a friend to check on you ]**

## Rules that keep it from becoming a way to put things off

1. **The side quest never replaces the main time.** They still pick a day and
   time for the main thing, and it has to come after the side quest.
2. **It's small and time-boxed:** about 3 minutes to check, about 10 to pick up.
3. **One errand per scan.** After they pick a time for the side quest, they go
   straight to picking the main time.
4. **If they already have everything, nothing is added.** One tap.
5. **The calendar file carries both events**, so the reminder for the side quest
   arrives on its own, then the main reminder.
6. **The moved-twice rule still applies to the main time** (the existing cap
   after two moves).

## What we'd measure

New Umami events, tagged like the rest (`from`, `look`): `kit-opened` (and from
which of the three doors), `kit-ready` (all ticked), `kit-missing`,
`sidequest-time-picked`, `list-copied`. The questions it answers:
- Do readers who open the kit start or schedule **less often** than those who don't? (The risk is the extra tap.)
- Do readers who schedule a side quest **finish more often** than those who
  schedule only the main thing? (The theory: they can't do it without the stuff.)
- Which door gets used: the third link, step 0, or the suggestion after picking a time?

If the kit check lowers starts and doesn't raise finishes, cut it back to a
single line above the buttons.

## What it takes (so you can weigh it)

- **Small:** the kit check as a card in the existing flow, ticks kept on the page
  only, and the third link under the two buttons.
- **Medium:** the second calendar event. The invite file can hold two events
  (a standard calendar format feature), and the Google Calendar link needs a second
  link. The main picker has to disable times earlier than the side quest.
- **Copy:** one kit list per workflow (the table above), the safety line, and the
  three screens. All of it goes through the copy review first.
- **Not needed:** accounts, a database, or remembering anything between visits.

## Questions for Charles and reviewers

1. **"Side quest" on all pages, or only students?** (Career and military might
   prefer "Pre-flight check" or "Kit check.")
2. **Should the third link be on the page from day one, or only after the step 0
   version has been tried?** The step 0 version costs nothing for people who tick
   everything, and it needs no new link.
3. **Should we offer a "Copy my shopping list" button at all,** or just show the
   list? (It's one tap for the reader, a little code for us.)
4. **Is "about 10 minutes to pick up" right?** It's a guess. Please time a real
   trip to a store, or say what you'd expect.
5. **Equal parts vinegar and water:** confirm the mix and the surfaces it's
   fine for before the line goes on a page.
