# Audience pages tracker

One row per audience landing page. The goal (Charles, 2026-10-31) is to learn
whether each audience needs **different wording** and **different checklists**,
not just a different look. Update this table when a page, its wording or its
checklists change, when QR codes go up, and when the numbers come in.

How the pages work and how to add one:
[`products/landing/audiences/README.md`](../../products/landing/audiences/README.md).
Numbers come from Umami: filter by the `from` tag. Each QR code gets its own
tag (`?from=qr-<place>`); a visit with no QR tag is counted as the audience
name (`from=career`).

## Pages

| Audience | Page | Look and schemes | Headline | Checklists offered (in order) | QR codes posted | Visits → started → finished | Scheme picks | Status |
|---|---|---|---|---|---|---|---|---|
| Early career: long hours, travel, on call | [/career](https://mrlifemanager.com/career/) | Career: teal and coral (default), navy and amber, plum and green | Your job gets your best hours. Here's what to do with what's left. | underwater ("back from a long week, or a trip"), dinner, guests, first-night ("new job, new city") | None yet | — | — | Live 2026-10-31 |
| Students: dorm, apartment, first place | [/students](https://mrlifemanager.com/students/) | Comic Panel: blue (default), red, green | Six steps. Then you're done. | first-night ("move-in day"), underwater, guests, dinner | None yet | — | — | Live 2026-10-31 |
| Military: new assignment, academy grads | [/military](https://mrlifemanager.com/military/) | Mission Board: olive and rust (default), navy and gold, steel and orange | You've passed a hundred inspections. Now you set the standard. | first-night ("new duty station"), underwater, guests, one-room | None yet | — | — | Live 2026-10-31 |

**Columns.** *Visits → started → finished*: page visits with that page's tags,
then `start-now` plus `time-picked` events, then `finished` events. *Scheme
picks*: `scheme-picked` events by look. Write the date range with the numbers.

## Wording to test

| Audience | Current wording | Idea to try | Why | Decided |
|---|---|---|---|---|
| Career | "Your job gets your best hours." | "The trip isn't the problem. Coming back to a mess is." | Travel research: coming home to a pile-up is the stress point ([research](../research/high-intensity-professionals.md)) | — |
| Students | "Six steps. Then you're done." | Something in their words, from a real student | The headline was written without talking to a student | — |
| Military | "Now you set the standard." | "Battle rhythm" for the weekly routine | Their own word for a recurring schedule ([research](../research/service-academy-grads.md)) | — |

## Checklists to consider

The checklists behind the doors are the same for every audience right now.
These are the gaps and questions each audience raises.

| Audience | Question or gap | Options | Decided |
|---|---|---|---|
| Career | No checklist for **before** a trip (leaving the place ready to come back to) | A six-step "leaving for a trip" checklist; the research says preparation is what makes travel go better | — |
| Career | "Back from a trip" points to the general mess checklist | Keep it, or a shorter "first hour home" version | — |
| Students | High school students mostly live at home; first-night doesn't fit them | Separate page for high school, or keep /students for college and first apartments | — |
| Students | Dorms often have no kitchen, and the mess checklist starts with the kitchen | A dorm-room version of the mess checklist | — |
| Students | Roommate conflict is common; the shared-dishes draft is paused | Bring "We keep arguing about the dishes" back for this page | — |
| Military | They move every two to three years | A duty-station version of first-night ("up and running in a week") | — |
| Military | The research idea is "Set your own standard," a worksheet | A checklist that writes the home's standard and weekly routine | — |
| All | Laundry and dinner-planning drafts are paused | Add a door per audience if one fits better than a current one | — |
