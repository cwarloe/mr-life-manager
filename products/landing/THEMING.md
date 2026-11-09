# Theming: one tokens file

**Rule:** every color, font and shadow on the site is a token in
[`assets/tokens.css`](assets/tokens.css). Pages, stylesheets and generators use
`var(--token)` instead of a raw value, so a change in that file reaches every
page, checklist, printable and look at once.

[`check_theme.py`](../../.github/scripts/check_theme.py) enforces it, and
`validate_repo.py` runs it, so CI fails on a hex color, `rgb()`/`hsl()`,
`white`/`black` as a CSS color, an SVG `fill="#…"`, a `%23…` color in a data
URI, or a written-out font family anywhere outside `tokens.css`.

## How it fits together

| File | Job |
|---|---|
| `assets/tokens.css` | The values: the site palette and its dark mode, the paper palette (`@media print`), the named palettes, the audience looks, fonts, shadows, QR ink |
| `assets/site.css`, `entry.css`, `looks.css`, `print/printable.css`, page `<style>` blocks | Layout and components, all `var(--token)` |
| `.github/scripts/theme_tokens.py` | Reads token values for code that can't use CSS: the share images and partner handout (`generate_share_assets.py`) and the `theme-color` meta (`build_site.py`) |

- **Every page links `tokens.css` first,** before its own stylesheet.
  Landing pages use `/assets/tokens.css`. Sheets under `products/checklists/`,
  `products/worksheets/` and `products/print/` use a relative path
  (`../../landing/assets/tokens.css`) so `render_pdf.py` can inline it, and
  `build_site.py` / `preview_site.py` rewrite it for the published copies.
  `check_entry_pages.py` and `check_built_site.py` fail a page that loads a
  shared stylesheet without it. Copying `guests.html` for a new entry page
  carries the link along.
- **Palettes are attributes, so they work on any element.** No attribute is the
  site. `data-palette="print"` (printable sheets, the `/guides/` and `/print/`
  indexes), `"week"` (The Week, light only) and `"feedback"` (light only) set
  their own values. `data-look="<family>-<scheme>"` is an audience look; its
  light values apply to any element, which is how each scheme-picker swatch
  shows its own colors, and its dark variants apply to the page.
- **Semantic names.** Tokens say what the color is for: `--accent`, `--second`,
  `--muted`, `--rule`, `--surface`. A name like `--blue` stops being true the
  day a look makes it gold, which is what the military looks did, so the old
  names were retired.
- **Every fill has an "on" partner.** Text on `--accent` uses `--on-accent`,
  on `--second` uses `--on-second`, on `--dark` uses `--on-dark`, so each
  palette keeps its own contrast.
- **Images can't read CSS variables.** Share images and the handout read the
  print palette through `theme_tokens.py`; re-run `generate_share_assets.py`
  after changing it.
- **Escape hatch.** A literal that has to stay goes on a line with a
  `theme-ok: <reason>` comment, so the exception is visible and explained. The
  inline share QR is skipped automatically: scanners need it black on white.

## Changing the look

| To | Do |
|---|---|
| Recolor the site | Edit the `:root,[data-palette]` block (and its dark block) in `tokens.css` |
| Recolor printables | Edit `[data-palette="print"]`, then re-render PDFs (`render_all_pdfs.py`; `check_pdfs_fresh.py` hashes `tokens.css` because each sheet links it) and share images |
| Add or change an audience scheme | Add a `[data-look="<family>-<scheme>"]` block and the name to `LOOKS` in `site_catalog.py` |
| Need a new kind of color | Add a semantic token (and its "on" partner) to the base block, list it in the header comment, then use it |

## Not covered

- **Email.** The MailerLite sequences (`emails/*.md`) are written in MailerLite;
  email clients need inline styles, so they keep their own.
- **Design prototypes.** `templates/design-options.html` shows options that
  haven't been picked, each with its own palette, so the checker lists it
  instead of failing it. When an option is chosen, move its values into
  `tokens.css` and drop it from `PROTOTYPES` in `check_theme.py`.
- **`favicon.svg`** is the brand mark, drawn in the print palette's ink,
  paper and second color as fixed values (an SVG favicon can't read the page's
  CSS). Redraw it if the brand colors change. `site.webmanifest` needs no
  care: `build_site.py` writes its colors from the tokens.
- `docs/` is thinking, not the site, and isn't scanned.
