# Side quest: the "are you ready?" step (proposal)

**Status:** Proposal for review, 2026-11-16. **Two decisions made:** no hard lock, and when something is missing the side quest is the suggested path (more taps accepted). Nothing here is on the site. Wording
is draft and follows the plain-speech rule in
[`content/README.md`](../../content/README.md).
**Picture of the flow:** [side-quest-mock.png](side-quest-mock.png) (student look; four screens).

**Decided (Charles, 2026-11-17): no "side quest" on the customer side.**
Marketing wouldn't call it that, and the point is only to get people the stuff so
they can finish the task. The customer-facing words are plain: **"What you'll
need"** for the check and **"Get what's missing first"** for the button. "Side
quest" stays as our own shorthand in this file. Keep it simple: no extra calendar
entry for now.

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
they have everything, nothing changes. If something is missing, we suggest
getting it first (a short errand, with a copy-the-list button and a store-finder
link), then they go back to the plan they already had. Simple version: no second
calendar entry.

## The name (superseded: customer-facing words are plain, see the top)

The table below is the brainstorm. Charles decided on 2026-11-17 against "side quest" on the customer side.

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

**Decided (Charles, 2026-11-16): no hard lock, and a soft push toward the side quest.** "Not really wanting to fight people on this if they want to power through." Nobody is ever stopped from starting. **If someone is missing something, we softly suggest the side quest first, even though it means more taps** (Charles: "even if it's more clicks"). The side quest is the highlighted button and "Start anyway" is one tap below it. The rest of this section is the reasoning.

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

## The screens (draft wording, simplified 2026-11-17)

Drawn in [side-quest-mock.png](side-quest-mock.png). No game words, no second
calendar entry: the page helps people get what they need, then goes back to the
plan they already had.

**1. The page after the scan.** The two buttons stay as they are. Optional, quiet
link under them:
> **What you'll need** (1 minute)
> Vinegar, dish soap, cloths. You'll use them in step 1.

**2. The check** (shows once to everyone who taps Start, and after they pick a time):
> **What you'll need**
> Most of this you probably have. Tap the ones you've got.
> ☐ White vinegar ☐ Dish soap ☐ Two cloths ☐ Trash bags ☐ A basket or box ☐ A spray bottle
> *(all ticked:)* **[ I've got everything. Let's go. ]**
> *(any unticked:)* **[ Get what's missing first ]** (highlighted)
> *(always, below it:)* Start anyway. Nothing is locked.
> Half vinegar, half water in the spray bottle cleans counters, sinks and glass.
> Not on stone like granite or marble. Never mix it with bleach.

**3. Getting what's missing:**
> **Get these first:** a basket or box, a spray bottle.
> About 10 minutes. Any grocery or dollar store has both.
> **[ Copy my shopping list ]**  **[ Find a store near you ]**
> **[ I've got them. Back to my plan. ]**

**4. If they were picking a time:** the usual "That's decided" screen, with one
added line under the time:
> Have these ready by then: a basket or box, a spray bottle.

## A clickable shopping list (idea from Charles, 2026-11-16)

**The idea:** when something is missing, the side quest shows the missing items
as a list the reader can tap to get fast, ideally same-day, through Walmart,
Amazon or a local delivery app. Charles doesn't want affiliate links unless they
get people the items sooner.

**What to build first (after the research, 2026-11-16).**
1. **"Copy my shopping list."** The missing items as plain text the reader pastes
   into Walmart, Amazon or any delivery app. No account, no backend, no affiliate
   deal, and it can't go stale.
2. **One "Find a store near you" link** (Google Maps, which documents its link
   format and needs no key). It opens a search for nearby stores.
3. **Not yet:** retailer search links, cart links, affiliate links. See below.

**Decided (Charles, 2026-11-17):** the Maps "find a store near you" link is fine, and retailer search links are left out for now (his call to me: the goal is that people complete the tasks, and only one of three retailers' search pages even loads reliably). Revisit if people ask for them.

**Correction.** An earlier version of this section proposed retailer search links
as step 2. That conflicts with a rule I didn't flag: the commerce rules say **no
search links in the action path** (link rule 2: a search is a choice, and choice is
what we're removing). Even the Maps link is a search for a place, so it needs
Charles's OK. A retailer search link would need an exception to that rule.

**What I can say now.**
- **Affiliate links don't make anything arrive sooner.** Only a link that fills the
  cart saves taps, and delivery speed depends on the reader's address and the
  store. So affiliate only matters if it's the *only way* to get the cart link.
- **Same-day isn't something we can promise.** It depends on the reader's ZIP and
  the store. Safe wording is "may be available same-day where you live."
- **Rule 10 of the commerce rules still applies:** never invent, infer or repair a
  product link; every link is checked against the real retailer page. Search links
  are easier to check than product links, and they don't go stale as often.
- **A delivery can be slower than the errand.** The side quest is about 10 minutes
  at a store. For tonight's job, a trip may beat a delivery.
- **Same-day in the middle of the side quest is a good fit** for people who can't
  leave the house; the picker for the errand already says "tonight" or "tomorrow."

**What the research found** ([report](../research/growth/same-day-shopping-links.md)):
- **No cart link works without an account on their side.** Amazon's needs an
  Associates tag, Instacart's needs an API key and approval, and no public one
  turned up for Walmart or Target.
- **Retailer search links are unofficial.** Only Target's loaded for the researcher;
  Walmart blocked automated fetching and Amazon was flaky. None are documented,
  so they could break without notice.
- **Affiliate links don't speed anything up.** They add tracking and a commission,
  and they conflict with the rule that basic consumables pay us nothing.
- **A 10-minute drive usually beats delivery.** Non-member delivery fees are about
  $10 with minimums, per the researcher; the Walmart numbers are only partly
  verified because walmart.com blocked the check.
- **Safe wording is "check your address."** Don't promise same-day, free, fast or
  in stock.

## Rules that keep it simple

1. **It never blocks.** "Start anyway" is always one tap.
2. **It's small:** about a minute to check, about 10 minutes to get what's missing.
3. **Nothing is added if they have everything.** One tap.
4. **One list, one job:** it only helps them get the stuff. It doesn't add a second
   plan, a second time to pick or a second reminder.
5. **The existing rules for the main time still apply** (the cap after two moves).
6. **Later, only if people forget the supplies:** a second calendar entry for the
   errand, with the main time after it.

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

- **Small:** the check as a card in the existing flow (ticks kept on the page only),
  the copy-list button, the Maps link, and the optional quiet link under the two buttons.
- **Later, only if needed:** a second calendar entry for the errand. The invite
  file can hold two events and the Google Calendar link would need a second link;
  the main picker would then disable times earlier than the errand.
- **Copy:** one kit list per workflow (the table above), the safety line, and the
  three screens. All of it goes through the copy review first.
- **Not needed:** accounts, a database, or remembering anything between visits.

## Questions for Charles and reviewers

1. **Are "What you'll need" and "Get what's missing first" the right plain words?**
   Say what you'd say to a friend.
2. **Should the third link be on the page from day one, or only after the step 0
   version has been tried?** With Charles's answer that everyone sees the kit
   check once (one tap if they have it all), the step 0 version already reaches
   everyone. My suggestion: build that first, and add the third link only if
   people want to check before choosing.
3. **Should we offer a "Copy my shopping list" button at all,** or just show the
   list? (It's one tap for the reader, a little code for us.)
4. **Is "about 10 minutes to pick up" right?** It's a guess. Please time a real
   trip to a store, or say what you'd expect.
5. **Equal parts vinegar and water:** confirm the mix and the surfaces it's
   fine for before the line goes on a page.
