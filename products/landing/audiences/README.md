# Audience landing pages

One page per audience a QR code is aimed at. The main site stays as it is;
each audience gets its own front door in its own look, pointing at the same
checklists. Charles, 2026-10-31: "I don't need a new site for that. I just
need a new landing page."

Each `*.html` file here publishes to `/for/<name>.html`. A QR code points to
`https://mrlifemanager.com/for/<name>.html?from=qr-<place>`, so completions
can be counted by where the code was posted.

## Pages

| Page | Audience | Look | Doors |
|---|---|---|---|
| [`early-career.html`](early-career.html) | Early-career professionals: long hours, travel, on call ([research](../../../docs/research/high-intensity-professionals.md)) | `pro` (teal and coral) | underwater, dinner, guests, first-night |

## Making a new one

1. Copy `early-career.html` to `<audience>.html`.
2. Set `data-look` on `<html>` to a look in `LOOKS` (`site_catalog.py`). For a
   new look, add its name to `LOOKS` and its styles to
   [`assets/looks.css`](../assets/looks.css), scoped to
   `html[data-look="<name>"]` inside `@media screen`. The Comic Panel and
   Mission Board looks on `/preview/design.html` are the starting points for
   students and military.
3. Write the headline, lede and door copy for that audience. Door text can be
   in the audience's words; the checklist behind it stays the same.
4. Each door links to a published checklist with `?look=<name>&from=<audience>`.
   The page's script swaps in the QR code's `from` tag when there is one.
5. Add a row to the table above.

`check_built_site.py` fails the build if a page has an unknown look, links to
a checklist that isn't published, or drops `look=`/`from=` from a door.
`check_live_site.py` checks each page after deploy. Pages here stay out of the
sitemap and the main pickers.

## How the look carries through

A small script in the `<head>` of each published checklist and finish page
sets `data-look` from `?look=`, only for names in `LOOKS`, so there's no flash
of the classic look. `entry.js` adds `look=` to the finish link, the calendar
return link and internal links on the page. Printing ignores the look, so the
printed page stays plain.
