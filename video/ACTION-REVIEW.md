# Instagram action review and next video briefs

**Date:** November 12, 2026 (Boise).
**Reviewed source:** commit f4ea15636f9d8e0fc0372a1269778af29380db08.
**Review performed:** independent marketing and behavioral-science reviews of video source, wording, timing, task pages and routing. No rendered-video viewing or live audience test was performed. Visual quality and observed conversion remain unverified.

## Verdict

**Revise the current three audience-overview videos before using them as the primary Instagram campaign.** They explain how the service works, but do not focus tightly enough on a result worth leaving the feed to achieve. This is a professional judgment supported by concrete source defects, not a measured forecast of audience behavior.

Keep their site-derived colors, sound-off design, source structure and scheduling capability. Build task-specific cuts from them instead of asking the owner to record presenter footage.

The goal is attention that transfers into action: a meaningful household task started and finished, or a specific appointment that leads back to that task. "Engagement" means engagement with the job, not a requirement to like, comment, save, follow or keep watching.

## Ranked findings

| Priority | What is present in source | Why it needs revision | Correction |
|---|---|---|---|
| 1 | Promo.tsx PhoneScene says "Scan the code under yours"; copy.ts says "You scanned this one" | Wrong context for someone already watching a Reel on the same phone | Replace the flyer demonstration with the actual task and a verified native link path |
| 2 | Opening hooks identify students, career or military situations broadly | Membership alone gives little immediate reason to interrupt what the viewer is doing | Open on one current household conflict with a worthwhile payoff |
| 3 | Three problems rotate, then the phone mockup opens the first problem | A viewer attracted by company or the table is taken into a different job | One task per cut; its promise, page and finish line match |
| 4 | Calendar UI is the main demonstration | Scheduling is a bridge; the viewer still needs to want the household result | Show the usable table or welcoming sitting area early |
| 5 | "A free checklist" and audience URL close the video | The container and extra menu are less direct than the promised result | Name the result, show the next action, and use a task-specific destination |
| 6 | Each problem has 100 frames at 30 fps, with entry/exit animation | Some long lines compete with orientation and animation for about 3.3 seconds | Shorten visible text, give it reading time, and inspect actual phone-sized renders |
| 7 | The service tour lasts 800 frames, about 26.7 seconds | More explanation is not automatically more action | Test shorter focused cuts; length serves clarity rather than an assumed algorithm rule |

These are not claims that every demographic hook fails or every shorter video works. The present task mismatch is directly observable; scroll-stopping appeal must be tested.

## Reusable reviewers

- [social-action-critic](../.claude/agents/social-action-critic.md): adversarial marketing, relevance, opening, result, reading burden, native next step and destination.
- [behavioral-action-reviewer](../.claude/agents/behavioral-action-reviewer.md): motivation, opportunity, planning, return, completion, and evidence.

Invoke them before considering a video ready for a small pilot:

> Review the current Mr. Life Manager Instagram draft using social-action-critic and behavioral-action-reviewer. Identify the strongest reason a viewer will keep scrolling or watch without acting. Follow the actual task destination. Give a verdict, three ranked defects, exact replacement text, and the smallest useful comparison. Label source inspection separately from rendered-video review and observed behavior. Optimize completed household results; likes and watch time are intermediate diagnostics.

These are reusable repo agent definitions, not continuously running services or scheduled automations.

## Cut A: company (first production candidate)

**Task:** [guests source](../products/landing/guests.html), public destination https://mrlifemanager.com/guests.html.
**Wanted result:** welcome people into a usable sitting area with a clean bathroom, empty sink, swept walking route and trash outside.
**Competing hooks for the same task:**
- A1: "You want them over. Your place isn't ready."
- A2: "Friends coming over? Get the place ready."

| Proposed time | Picture | On-screen words |
|---|---|---|
| 0–3 seconds | Ordinary sitting area with a blocked seat; immediately show the hook | A1 or A2 |
| 3–7 | Same modest space made usable; short empty-sink and clean-bathroom inserts | "Clear seats. Clean bathroom. Empty sink." |
| 7–11 | Close crop of the real company task; legible first instruction | "Six steps to get ready for company." |
| 11–15 | Keep the useful result visible; briefly show the real start/schedule choice | "Home? Start now. Away? Schedule the work." |
| 15–18 | Hold the result and next action | "Get your place ready. Open the free checklist." |

**Instagram caption:**

> Someone's coming over and your place isn't ready. Follow six steps to handle the sink, sitting area, bathroom, walking route and trash. Set aside about an hour; a backlog of dishes can take longer. Open the profile link to the company checklist. Home now? Start. Away? Choose when you'll get ready and save the calendar event.

**Campaign profile link:** https://mrlifemanager.com/guests.html?from=ig-company-profile

The profile link must actually open the company task before this caption is published. If the account instead supports a verified direct task link at the placement used, change the CTA accordingly. A moving button pictured inside a video is not a clickable link.

The original task is not "clean one mirror." Its benefit is being able to welcome people. Do not create fake urgency, guarantee an hour or substitute a partial task for the full finish.

## Cut B: table (second production candidate)

**Task:** [dinner source](../products/landing/dinner.html), public destination https://mrlifemanager.com/dinner.html.
**Wanted result:** a wiped table, clear needed seats, and places set for the people eating.
**Competing hooks:**
- B1: "Dinner's ready. There's nowhere to eat."
- B2: "Eating on your bed because the table's covered?"

| Proposed time | Picture | On-screen words |
|---|---|---|
| 0–3 seconds | Meal beside a cluttered table, hook visible immediately | B1 or B2 |
| 3–6 | Clear trash, move dishes, contain loose belongings | "Make room for dinner." |
| 6–9 | Same wiped table, clear seats and meal served | "Somewhere to sit. Room to eat." |
| 9–12 | Actual dinner task, legible first step | "Follow the free checklist." |
| 12–16 | Hold usable table and the task-specific next step | "Clear the table. Start now or schedule before dinner." |

**Instagram caption:**

> Your table is covered and you need somewhere to eat. The free checklist walks you through clearing the table and the seats you need, wiping the surface and setting places. The rest of the house can wait. Open the profile link to the table checklist. If you're away, schedule the task before your next meal at home.

**Campaign profile link:** https://mrlifemanager.com/dinner.html?from=ig-table-profile

Run this as its own campaign block or verified placement with the correct link. Do not rotate company and table feed posts while silently treating one generic profile link as if it opens both tasks. For a necessary multi-topic profile menu, label the exact choice and account for the extra decision.

The basket is temporary containment, not a completed organization project. Show the full table outcome without implying the whole room is sorted.

## Cut C: first night (use when a move-in audience is reachable)

**Task:** [first-night source](../products/landing/first-night.html), public destination https://mrlifemanager.com/first-night.html.
**Wanted result:** tonight's essentials working, condition documented and essential checks handled.
**Competing hooks:**
- C1: "First night in your own place?"
- C2: "Moving in today? Make tonight work first."

| Proposed time | Picture | On-screen words |
|---|---|---|
| 0–3 seconds | New place, accessible boxes, bed not yet made | C1 or C2 |
| 3–7 | Made bed, bathroom essentials out | "Make tonight work before unpacking everything." |
| 7–11 | Condition photos, lock check, clear eating surface | "Bed ready. Essentials out. Important checks done." |
| 11–15 | Actual first-night checklist, not the audience menu | "Six steps for your first night." |
| 15–19 | Calm usable space and clear next step | "Open the free checklist. Start or schedule tonight's setup." |

**Instagram caption:**

> Tonight is your first night in the new place. Get the bed and bathroom ready, document the condition, handle the important checks and clear somewhere to sit and eat. The full task allows about an hour and a half, longer if essentials are missing. Open the profile link to the first-night checklist and choose when you'll start.

**Campaign profile link:** https://mrlifemanager.com/first-night.html?from=ig-first-night-profile

Target someone moving in now. Do not use this as a promise to solve still-unpacked boxes weeks later; that is a different draft workflow.

## Production constraints

Timings, hooks and ranking above are design hypotheses. They are not a universal three-second rule or a tested optimal runtime.

Use existing site tokens and available illustrations, staged scenes, or clearly illustrative animation. No presenter required. A before/after is a staged depiction unless supported by a real, consented case; it is not a customer testimonial. Depict the same ordinary space rather than imply a renovation or purchase is required. Audit the actual rendered phone-size words, scene timing and platform overlays. Keep essential text within the project's safe areas, while checking actual placement because app overlays vary.

The visible first step is a demonstration, not completion. Do not make the ad itself into a second long checklist. Offer the existing task experience.

## Behavioral rationale and limits

| Verified research lead | What it supports | What it does not establish here |
|---|---|---|
| [Milkman et al., 2011, original vaccination study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3127912/), also [Harvard author publication record](https://www.hks.harvard.edu/publications/using-implementation-intentions-prompts-enhance-influenza-vaccination-rates) | Specifying date and time helped enact a one-off health action in a randomized workplace study | The effect size for household tasks or Instagram viewers; a calendar choice is not completion |
| [Carrera et al., 2018, randomized exercise planning study](https://www.nber.org/papers/w24959) | A simple planning prompt did not improve repeated gym attendance in this study | Scheduling is a sufficient mechanism for every repeated behavior |
| [Lally et al., 2010, original habit-formation study](https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674) | Repetition in a consistent context was associated with developing automaticity over time, with substantial variation | One finished household task creates a habit, ends a scrolling habit, or makes later action generally more likely |

Primary records/abstracts were checked through retrieval; some full-text endpoints blocked direct access. No effect size from these studies is used to forecast this campaign.

The practical inference is to combine a result the person wants, an available opportunity, a concrete next step and a useful return path. Scheduling addresses opportunity; it cannot make an unimportant chore compelling. The owner's longer-term hope, that a first success supports further action, is worth exploring after the first outcome is established.

## Small pilot and decision rules

Begin with the company cut and an alternative hook for the same cut, keeping destination and remaining scenes constant. Inspect both renders for legibility and truthful scope. Then use the table cut as a separate meaningful-outcome experiment. This is not a requirement to launch paid advertising or a large field study.

Use the existing [audience tracker](../docs/business/audience-tracker.md) and [monthly scorecard](../planning/monthly-scorecard.md). Record the creative/placement, available reach and retention, task visits, immediate starts, time choices, calendar-link clicks, returns, starts from reminders and acknowledged finishes. Keep their denominators distinct.

Current limitations:
- A profile link attributes the campaign, not the exact feed post.
- A calendar-added event is a link click, not proof of an event saved.
- A came-back event is a return-URL load, not proof a notification caused it.
- A finished event is a reader's acknowledgment, not independent observation of physical work.
- Event totals can include repeat actions; they are not automatically distinct people.
- Self-selected now/appointment groups differ; their rates do not establish scheduling's causal effect.
- Low counts and sequential posting do not support statistically proven winners.

A higher-view video with fewer completed tasks is not automatically the better creative. Ask where the useful action stops. Do not make comments or reporting back a condition of help. Later voluntary feedback can test whether the household result occurred and whether the person independently repeated useful action; it is not needed to receive the free task.

## Next production handoff

Use these briefs for task-specific revisions to the existing Remotion project. Keep the original audience overview compositions as reference; do not confuse this review document with revised code or rendered exports. Match current live pages, verified link placement and approved workflow promises before publishing. No MailerLite or live-account change is required by this review.
