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
| [`career.html`](career.html) | `/career` | Early-career professionals: long hours, travel, on call ([research](../../../docs/research/high-intensity-professionals.md)) | career: clean, all sans, light and dark | teal, navy, plum |
| [`students.html`](students.html) | `/students` | Dorm, apartment, first place | students: Comic Panel, light only | blue, red, green |
| [`military.html`](military.html) | `/military` | New assignment, academy grads ([research](../../../docs/research/service-academy-grads.md)) | military: Mission Board, light only | olive, navy, steel |

## Color schemes

Every page offers **at least three color schemes** for now (Charles,
2026-10-31), shown to every visitor as swatches in the top bar. A pick
changes the page, carries into the checklist and finish page, and is counted
in Umami as `scheme-picked`. When the numbers or reader feedback settle on
one, drop the others.

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
