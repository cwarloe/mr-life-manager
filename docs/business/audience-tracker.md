# Audience pages tracker

One row per audience landing page. The goal (Charles, 2026-10-31) is to learn
whether each audience needs **different wording** and **different checklists**,
not just a different look. Update this table when a page, its wording or its
checklists change, when QR codes go up, and when the numbers come in.

**Who the pages are for** ([ADR-023](../../planning/decisions.md#adr-023--target-the-first-stretch-with-nobody-else-running-things)):
people at their first chance to be nearly completely unsupervised. Junior
enlisted in barracks are not a target until they move off base.

How the pages work and how to add one:
[`products/landing/audiences/README.md`](../../products/landing/audiences/README.md).
Numbers come from Umami: filter by the `from` tag. Each QR code gets its own
tag (`?from=qr-<place>`); a visit with no QR tag is counted as the audience
name (`from=career`).

## Pages

| Audience | Page | Look and schemes | Headline | Checklists offered (in order) | QR codes posted | Visits → started → finished | Scheme picks | Status |
|---|---|---|---|---|---|---|---|---|
| Early career: first job, own place, long hours | [/career](https://mrlifemanager.com/career/) | Career: teal and coral (default), navy and amber, plum and green, green and graphite | Too tired to deal with your place tonight? Pick the night you will. | underwater ("full sink and a stack of mail"), dinner ("eating over the sink"), guests ("a date or a friend"), first-night ("moved for the job") | None yet | — | — | Live; copy v2 2026-10-31 |
| Students: first apartment, first place on their own | [/students](https://mrlifemanager.com/students/) | Comic Panel: blue (default), red, green, orange and navy. Campus fliers can open in school-like colors with `?look=` (colors only, no school names) | Nobody's checking your apartment, and you don't know where to start. Start here. | underwater, guests ("friends or your parents"), dinner ("you eat on your bed"), first-night ("first keys"; move to the top in August, January and the first two weeks of a term) | None yet | — | — | Live; copy v2 2026-10-31 |
| Military: first place off base, first assignment | [/military](https://mrlifemanager.com/military/) | Mission Board: scarlet and gold, black and gold, blue and yellow, navy and gold (default), black and silver (the five branches' colors, named by color only) | First place off base, and nobody's checking it. Get it squared away. | first-night ("household goods haven't shown up"), underwater ("no inspection on the calendar"), guests ("people from the unit"), one-room ("spare room full of boxes") | None yet | — | — | Live; copy v2 2026-10-31 |

**Columns.** *Visits → started → finished*: page visits with that page's tags,
then `start-now` plus `time-picked` events, then `finished` events. *Scheme
picks*: `scheme-picked` events by look. Write the date range with the numbers.

## Wording to test

**The flier and workflow wording is under review in
[`docs/copy/`](../copy/README.md)** (2026-11-01). The live pages still carry
the older copy until reviewers sign off.

The live copy and its reasoning: [copy-final](../research/copy-final-2026-10-31.md),
[copy review](../research/copy-review-2026-10-31.md). Design reasoning:
[design review](../research/design-review-2026-10-31.md). Read a test only
after about 100 visits per version, and only for big differences.

| Audience | Live wording | Next to try | Why | Decided |
|---|---|---|---|---|
| Career | "Too tired to deal with your place tonight? Pick the night you will." | "At work, someone's always checking. At home, pick the night you do." | Puts the unsupervised theme in the headline | — |
| Career | (same) | "The trip isn't the problem. Coming back to a mess is." | Only for fliers near travelers ([research](../research/high-intensity-professionals.md)) | — |
| Students | "Nobody's checking your apartment, and you don't know where to start. Start here." | "You don't have to clean everything. Do these six things and stop." | Permission framing lowers the effort they expect | — |
| Military | "First place off base, and nobody's checking it. Get it squared away." | "Nobody inspects your place now. Hold it to your own standard." | True now that barracks residents are out of scope | — |
| All task pages | "Not home yet? Pick a time" (solid button) | For QR visitors, make it the main button and "Start now" the second one | Designer's test 1: most people scanning a flier aren't home | — |

## Checklists to consider

The checklists behind the doors are the same for every audience right now.
These are the gaps and questions each audience raises.

| Audience | Question or gap | Options | Decided |
|---|---|---|---|
| Students, career | The felt need "I moved in a while ago and I'm still living out of boxes" had no checklist. The first-night checklist is for the first night, so it becomes the move-in-season swap on the flier | A "still unpacking" checklist (one room at a time), built from the spare-room and first-night checklists | Drafted 2026-11-01: [workflow 6](../copy/workflows/06-still-unpacking.md), under review |
| Students, career, military | The checklist steps were stiff and full of "it" (2026-11-01) | Plain-speech rewrite proposed inside each file in [`docs/copy/workflows/`](../copy/workflows/); the office and paused checklists get the same pass | Under review |
| Career | No checklist for **before** a trip (leaving the place ready to come back to) | A six-step "leaving for a trip" checklist; the research says preparation is what makes travel go better | — |
| Career | "Back from a trip" points to the general mess checklist | Keep it, or a shorter "first hour home" version | — |
| Students | High school students mostly live at home; first-night doesn't fit them | Separate page for high school, or keep /students for college and first apartments | — |
| Students | Dorms often have no kitchen, and the mess checklist starts with the kitchen | A dorm-room version of the mess checklist | — |
| Students | Roommate conflict is common; the shared-dishes draft is paused | Bring "We keep arguing about the dishes" back for this page | — |
| Military | They move every two to three years | A duty-station version of first-night ("up and running in a week") | — |
| Military | The research idea is "Set your own standard," a worksheet | A checklist that writes the home's standard and weekly routine | — |
| All | Laundry and dinner-planning drafts are paused | Add a door per audience if one fits better than a current one | — |
