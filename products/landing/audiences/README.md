# Audience landing pages

One page per audience a QR code is aimed at. The main site stays as it is;
each audience gets its own front door in its own look, pointing at the same
checklists. Charles, 2026-10-31: "I don't need a new site for that. I just
need a new landing page."

Each `<name>.html` file here publishes to `/<name>/`, so a QR code points to
`https://mrlifemanager.com/<name>?from=qr-<place>` and completions can be
counted by where the code was posted. What we're learning about each audience,
and the wording and checklist changes to consider, are tracked in the
[audience tracker](../../../docs/business/audience-tracker.md).

## Pages

| File | URL | Audience | Look | Schemes |
|---|---|---|---|---|
| [`career.html`](career.html) | `/career` | First job, own place, long hours, travel ([research](../../../docs/research/high-intensity-professionals.md)) | career: clean, all sans, light and dark | teal, navy, plum, green |
| [`students.html`](students.html) | `/students` | First apartment, first place on their own | students: Comic Panel, light only | blue, red, green, orange |
| [`military.html`](military.html) | `/military` | First place off base, first assignment, academy grads ([research](../../../docs/research/service-academy-grads.md)) | military: Mission Board, light only | scarlet and gold, black and gold, blue and yellow, navy and gold (default), black and silver: the five service branches' colors, named by color only |

## Color schemes

Every page offers **four color schemes (five on military, one per branch's colors)** for now (Charles,
2026-10-31), shown to every visitor as swatches in the top bar. A pick
changes the page, carries into the checklist and finish page, and is counted
in Umami as `scheme-picked`. When the numbers or reader feedback settle on
one, drop the others.

## Who the pages are for

[ADR-023](../../../planning/decisions.md#adr-023--target-the-first-stretch-with-nobody-else-running-things):
people at their first chance to be nearly completely unsupervised, with nobody
telling them what to do or checking on them. Junior enlisted in barracks are
not a target until they move off base.

## School colors on campus fliers

A campus flier's QR code can open `/students` in colors close to the
school's: `mrlifemanager.com/students?look=students-<scheme>&from=qr-<place>`.
If none of the schemes is close, add one named for its colors
(`students-maroon`), never for the school. Colors only: no school names,
mascots, logos or "for X students" copy, so nothing suggests the school
sponsors it (ADR-023).

## Making a new one

1. Copy one of the pages to `<name>.html`. The name becomes the URL, so keep it
   short.
2. Set `data-look` on `<html>` to the default look and list at least three
   `data-look-pick` buttons from the same family. Looks are named
   `<family>-<scheme>` and must be in `LOOKS` (`site_catalog.py`). For a new
   family or scheme, add it to `LOOKS` and to
   [`assets/looks.css`](../assets/looks.css).
3. Write the kicker, headline, lede and door copy for that audience. Door text
   can be in the audience's words; the checklist behind it stays the same.
4. Each door links to a published checklist with `?look=<default>&from=<name>`.
   [`assets/audience.js`](../assets/audience.js) swaps in the picked scheme and
   the QR code's `from` tag.
5. Add a row here and in the audience tracker.

`check_built_site.py` fails the build if a page has an unknown look, fewer
than three schemes, a scheme from another family, a door to a checklist that
isn't published, or a door without `look=` and `from=`. `check_live_site.py`
checks each page after deploy. These pages stay out of the sitemap and the
main pickers.

## How the look carries through

A small script in the `<head>` of each published checklist and finish page
sets `data-look` from `?look=`, only for names in `LOOKS`, so there's no flash
of the classic look. `entry.js` adds `look=` to the finish link, the calendar
return link and internal links on the page. Printing ignores the look, so the
printed page stays plain.
