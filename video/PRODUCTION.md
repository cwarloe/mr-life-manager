# Task-focused Instagram production

Four rendered drafts. Sound-off, 1080×1920, 30 fps, H.264/yuv420p. No presenter recording, music license or voiceover needed. Original audience compositions are preserved.

| Composition | Export | Length | Task |
|---|---|---|---|
| Action-company | mlm-company.mp4 | 20s | /guests.html |
| Action-company-alt | mlm-company-alt.mp4 | 20s | /guests.html |
| Action-table | mlm-table.mp4 | 20s | /dinner.html |
| Action-first-night | mlm-first-night.mp4 | 21s | /first-night.html |

## Story

0–3s: one felt problem, illustrated blocked space, immediate profile-link invitation. 3–7s: same space made useful. 7–11s: actual first checklist step, shown as a preview. 11–15s: home-now versus schedule-when-home. 15s–end: task-specific result, profile-link instruction and readable fallback address. Illustration is stylized, not a customer result or testimonial. First-night keeps boxes visible; table moves items into a basket rather than claiming they are sorted.

## Captions and destinations

Company, both hooks:

> Want people over, but your place isn't ready? Get clear seats, a clean bathroom and an empty sink. The free six-step checklist plans about an hour. Home now? Start. Away? Pick the day and time you'll get ready. Open the company checklist through the profile link.

https://mrlifemanager.com/guests.html?from=social-instagram-company

Table:

> Dinner needs somewhere to land. Clear the table, wipe it down and set a place for everyone eating. The free six-step checklist plans about 10 minutes. Home now? Start at the table. Away? Schedule before your next meal. Open the table checklist through the profile link.

https://mrlifemanager.com/dinner.html?from=social-instagram-table

First-night:

> Moving in today? Get your bed and bathroom ready, take move-in photos, check the basics and make somewhere to sit and eat. The free six-step checklist plans about 90 minutes. Start while you're there, or schedule tonight's setup. Open the first-night checklist through the profile link.

https://mrlifemanager.com/first-night.html?from=social-instagram-first-night

These are task planning estimates from the current pages, not guarantees. No email or payment prerequisite. Do not add follow/save/comment requests that compete with doing the task.

## Publication gate and small pilot

Nothing has been posted. Start with company and its alternate hook; they share one destination. The profile link must visibly and reliably open the promised company task. Hold table/first-night until their named tasks are accessible through verified native/profile links; a company-only link cannot serve all three creatives concurrently. Check Instagram's actual in-app browser, calendar save and reminder return before a public pilot. Local browser checks cannot prove a personal calendar saved an event.

Compare the two company hooks while keeping the remaining cut and destination unchanged. Early retention diagnoses attention; task visits, starts, time choices, calendar-link clicks, return loads and self-acknowledged finishes describe later stages. Use existing analytics/scorecard. Calendar clicks do not prove saves; finishes do not independently verify physical work; event totals are not distinct people. No evidence yet that these creatives stop scrolling or increase completion, and no basis to claim lasting habit change.

## Render and asset maintenance

```sh
cd video
npm ci
npm run sync
npx tsc --noEmit
npm run render -- Action-company out/mlm-company.mp4 --codec=h264 --crf=20 --concurrency=2
```

Repeat with the other composition/export names above. Render outputs stay in ignored `out/`; downloadable copies are delivered separately. Site tokens and Archivo come from the existing sync script. `public/tasks/*-step.png` are actual task cards captured from the current built site at a 540px browser viewport, device scale 2, after clicking `.go-do` and waiting for fonts, using a screenshot of `.step.current`. Refresh them after a task or visual update. `public/tasks/sources.json` records capture-source hashes.

## QA and reviewer disposition

Repository HTML/link/theme checks, entry wiring, PDF freshness, built-site checks and TypeScript passed. Local mobile-viewport browser checks passed for immediate start and selected-time ICS/Google links on all three routes. All four exports decoded without ffmpeg errors; ffprobe confirmed codec, dimensions, frame rate and duration. Contact frames at 0/5/9/13/17s and full-size frames were inspected for clipping and readability, not a full uninterrupted human playback or a device/platform test.

The social-action-critic and behavioral-action-reviewer independently reviewed sampled rendered frames and task sources. Both returned conditional ready-for-small-pilot: promises match the routes; one result, real checklist preview and home/away paths are clear; no unsupported habit/brain claims. Their main creative correction—show the action invitation in the opening—was applied before final exports. Their publication condition is the verified matching profile link above. Mild illustrated clutter and actual attention/completion remain test hypotheses.
