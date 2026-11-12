# Mr. Life Manager social videos

Vertical (9:16, 1080x1920, 30 fps, about 27 seconds) videos for phones: Reels,
Shorts and TikTok. Built with [Remotion](https://www.remotion.dev/). One video
per audience, all from the same template:

| Composition | Look (colors, fonts) | Ends on |
|---|---|---|
| `Promo-students` | `students-blue`, Comic Panel | mrlifemanager.com/students |
| `Promo-career` | `career-teal`, clean | mrlifemanager.com/career |
| `Promo-military` | `military-navy`, Mission Board | mrlifemanager.com/military |

## The story (about 27 seconds, no sound needed)

1. **Hook (3 s):** the flier's first line, e.g. "Living on your own for the first time?"
2. **Three problems (10 s):** the flier's three problem lines, one at a time, in the reader's words.
3. **Scan page (about 5 s):** a phone shows what they see after scanning: the problem first, then "I'm home now. Let's start." and "I'm not home yet. Let me pick a day and time."
4. **Pick a day and time (about 4 s):** "When will you wash the dishes and pick up your place?", Saturday at 10:00 a.m., "Add to my calendar."
5. **Finish (4 s):** "A free checklist. No app to download. No email needed." and the address.

The order follows the site: feel the problem, see it repeated, pick a time to do
that exact thing. Text stays out of the top 230 px and the bottom 430 px, where
the apps put their buttons and captions.

## Words

All wording is in [`src/copy.ts`](src/copy.ts) and nowhere else. **It is draft
wording:** the lines come from the fliers under review in
[`docs/copy/`](../docs/copy/README.md). When reviewers change a line there,
change it in `copy.ts` too, then re-render. It follows the copy rules in
[`content/README.md`](../content/README.md): plain speech, every verb gets its
object, about right now.

## Colors and fonts

Read from the site's [`tokens.css`](../products/landing/assets/tokens.css) and
its self-hosted fonts by `scripts/sync.mjs`, so a change to the site's look
changes the videos. The generated files (`src/generated/`, `public/fonts/`) are
not committed. To make a video in another look, add an audience to `copy.ts`
with any look name from `LOOKS` in `.github/scripts/site_catalog.py`.

## Run it

```
cd video
npm install
npm run studio                    # preview in the browser
npm run render -- Promo-students out/mlm-students.mp4 --crf=26
npm run still -- Promo-students out/frame.png --frame=480
```

Needs Node 20 or newer. Rendered files go to `out/` (not committed).

## Not done yet

- **No sound.** The video reads with the sound off. Voiceover and music are open.
- **No captions track** (the text is part of the picture).
- **Wording is under review** (see Words).
- **Tags for tracking.** Each post should link to its audience page with a place tag, for example `mrlifemanager.com/students?from=social-<platform>`, so Umami can tell social visits from fliers.
