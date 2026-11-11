# Drive import, 9 November 2026

This note covers the 9 November Drive import from commit f44f6e0, except the BEC 2026 files, which I skipped as asked. The files I read are [idaho-formation-tax-checklist.md](../../business/idaho-formation-tax-checklist.md), [interview-pack-week1.md](../../research/interviews/interview-pack-week1.md), [research-chores-2026-09-16.md](../../research/research-chores-2026-09-16.md), and the updated [docs/README.md](../../README.md).

What already works well: the Idaho checklist has no EIN, bank, or permit numbers in the repo, and it says plainly that it is not legal or tax advice. The USPTO scan is dated, careful, and also not legal advice. The week-1 interview pack asks about the past, not about whether someone "would buy," and it has a clear consent line.

## 1. The research-chores file still points at a machine path that is not in this repo

[research-chores-2026-09-16.md](../../research/research-chores-2026-09-16.md), lines 126 to 128, lists this deliverable:

> `/workspace/mr-life-manager-bd/research-chores-2026-09-16.md` | This report (TLDR + full notes).

That path was true on the machine that first wrote the scan. It is not a path in this repository. A later reader will go looking for a folder that is not here.

Suggested rewrite of that row:

> `docs/research/research-chores-2026-09-16.md` | This report (TLDR and full notes), imported from Drive on 2026-11-09.

## 2. The interview pack still points parents at the old GitHub Pages URL

[interview-pack-week1.md](../../research/interviews/interview-pack-week1.md), lines 11 to 13:

> **Parent landing (once live):** https://cwarloe.github.io/mr-life-manager/index-parents.html
> *(May already be published via GitHub Pages — useful for parents-as-buyers follow-up after the call, not during.)*

The live site is mrlifemanager.com, and the parents page lives there. "Once live" and "may already be published" are out of date.

Suggested rewrite:

> Parent landing, for follow-up after a call, not during it: https://mrlifemanager.com/index-parents.html

## 3. The Idaho checklist is a 16 September snapshot imported in November, without a status refresh

[idaho-formation-tax-checklist.md](../../business/idaho-formation-tax-checklist.md) says Drive remains the live editable copy, which is the right warning. The body still shows the EIN application as in progress, the assumed business name as not filed, and the log ending on 16 September 2026. The import was 9 November. A reader of the repo can think those steps are still mid-flight.

Suggested addition directly under the Drive-is-live warning:

> This Git copy is a snapshot from 2026-09-16, imported on 2026-11-09. Check the Drive doc before treating any checkbox as current.

Whether the assumed business name should be filed is an ops step, not a wording fix. I have not turned it into a strategy question.

## 4. This import and the 5 November interview plan still disagree

The week-1 pack wants five conversations this week, toward 15 to 20, across five persona groups, including newlyweds and overwhelmed householders. The 5 November willingness-to-pay plan wants 3 to 5 recent movers aged 18 to 25 and 3 to 5 parents. That conflict is already in [needs-charles.md](needs-charles.md), question 6. I am not rewriting either plan.

The pack also says, on line 20, that this week's work "runs in parallel with recording Dave." If that recording is no longer the current parallel track, the sentence should be cut or dated. I do not know whether it is still underway, so I am flagging it rather than inventing a replacement.

## 5. The docs index was updated for this import, and it still omits several current files

[docs/README.md](../../README.md) now lists the Idaho checklist, the USPTO scan, the BEC folder, and the week-1 interview pack, which is good. It still does not list the November Bronco files (customer profile, competitor scan, willingness-to-pay plan), the audience tracker, or anything in `docs/copy/`. The suggested reading order on lines 15 to 16 is still "mission, principles, target audiences, product ladder, roadmap." It does not mention the customer profile or the business model, which are the documents a new reader would use to understand who pays and how the work makes money.

Suggested additions to the business row: customer profile, competitor scan, willingness-to-pay plan, and audience tracker. Suggested addition of a `copy/` row pointing at the copy review folder. Suggested reading order, once the first-area notes are accepted as a guide:

> mission, principles, target audiences, customer profile, business model, product ladder, then the roadmap.

## 6. The USPTO scan and the closed name-clearance note now sit in the same repo

This is the same conflict already described in the brand note and in [needs-charles.md](needs-charles.md), question 10. The imported scan is the document that makes that conflict visible. I checked the live-registration claim for LIFE MANAGER, Registration 3544555, on 11 November 2026. I am not offering a legal conclusion.
