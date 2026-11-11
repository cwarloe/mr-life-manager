# Design review: audience looks, color schemes and the Fan Club options

**Date:** 2026-10-31. **Reviewer:** web-designer agent (critique only; no site files changed).
**Inputs:** `products/landing/audiences/*.html`, `assets/looks.css`, `entry.css`,
`site.css`, `audience.js`, `entry.js`; phone screenshots at 390 × 844 of every
audience page and scheme, plus task, doing and finish pages per audience; the
Charles Fan Club site, `public/docs/` design options and event mockups, and its
`notes/`. Screenshots were taken with Google Fonts blocked, so Archivo and
Source Serif show as fallbacks. Pixel positions below are from those
screenshots and will shift a little with the real fonts.

**The test applied throughout:** someone scans a QR code in a coffee shop or
dining hall, or opens a friend's link. Does the design help them feel one
problem, tap it, and then start now or pick a specific time?

---

## 1. Verdict in five lines

1. **The doors are below the fold on every landing page.** On a 390 × 844
   phone the first door's headline lands at about 720–840 px, so a reader sees
   a slogan and three fake buttons, but no problem to tap. Cut the hero down
   until two doors show without scrolling.
2. **Someone holding a flier is usually not at home, so the realistic action is
   "pick a time." Right now that's a ghost button labeled "Not right now."**
   Rename it "Pick a time" and give it equal weight, and make it the filled
   button for QR visitors. This is the change with the best evidence behind it.
3. **The display fonts are carrying text they can't carry.** Bangers and Saira
   Stencil work for headlines and buttons, but not for three-line door titles
   or the small "Ready to start?" line. Keep the look, and put sentences back
   in plain bold sans.
4. **Color has no job yet.** Coral vs. teal (and yellow vs. blue) door stripes
   mean "reset" vs. "setup" internally, and the reader can't tell. The military
   gold headline text renders as olive-brown, which is the least-liked color
   region in the best color-preference study. Use one action color, and use
   gold as a fill or highlight, not as text.
5. **Color schemes are the smallest lever here.** Offer four per audience (in
   section 5), set the default per flier with `?look=`, and judge a scheme by
   the starts and scheduled times that follow it, not by swatch taps.

---

## 2. Audience research that should drive the design

### Who, where, and what they can do in that moment

| | College students | Early-career professionals | Young officers, academy grads, junior enlisted |
|---|---|---|---|
| Age, stage | 18–24; dorm, then first apartment; roommates; dorms often have no kitchen | 22–32; long hours, travel, on call; often living alone ([research](high-intensity-professionals.md)) | Officers 22–28, junior enlisted about 18–24; move every two to three years; used to inspections ([research](service-academy-grads.md)) |
| Where they meet it | Dining hall table tent, campus board, coffee shop, a friend's text | Office or coworking coffee shop, a coworker's Slack or text, an airport | Base coffee shop, gym, a peer's text, an academy or unit group chat |
| Where they are when they scan | **Not at home** for fliers; at home for friend links | Often not home (work, travel); evenings at home for links | Often on base or at work; home for links |
| What they can do right then | Pick a time; start only if it's a friend's link at night | Pick a time (especially "the evening I get back") | Pick a time; "execute now" after duty hours |
| Phone context | Near-universal smartphones (Pew puts ownership at about 96–97% for ages 18–29); one hand, half attention, noisy room | Same, often in dark mode late at night | Same |

**The implication for design (judgment, built on the setting):** for flier
traffic, "Start now" is the less likely action, because the reader isn't
standing in their kitchen. The page should treat picking a time as a full
success.

### Evidence, graded

Grades: **A** peer-reviewed, large or replicated. **B** peer-reviewed but
small or indirect, or a strong observational study. **C** industry or vendor
data, self-selected polls. **D** no real evidence; judgment.

| Finding | Source | Grade | What it means here |
|---|---|---|---|
| Making a specific plan with a **when** (an implementation intention) raises follow-through; meta-analysis of 94 tests, d ≈ 0.65 | Gollwitzer & Sheeran 2006, *Advances in Experimental Social Psychology* | A | Scheduling is a real conversion, not a consolation prize. Design it as a first-class action. |
| In a field trial (3,272 employees), a mailer asking for a **date and time** raised flu-shot uptake 4.2 points; date alone did not significantly | [Milkman et al. 2011, *PNAS*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3127912) | A | The current picker's line "'Later' isn't a time," plus day-and-time buttons, is right. Make it easier to reach. |
| Students prefer their own university's colors, and the preference grows with school spirit (57 Berkeley and 46 Stanford students) | [Schloss, Poggesi & Palmer 2011, *Psychonomic Bulletin & Review*](https://palmerlab.berkeley.edu/pdf/SchlossPoggesi&Palmer-2011.pdf) | B (small, but it's the age group and the mechanism) | The best student scheme on a campus is likely that campus's colors. The same mechanism (liking an institution carries over to its colors) supports the branch-color military schemes. This is an inference for military; it wasn't studied there. |
| Color preference follows how much people like the objects of that color. Saturated blues and cyans were rated high; dark yellow, olive and brown low (48 US participants) | [Palmer & Schloss 2010, *PNAS*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2889342) | B (small sample; the general blue preference is widely replicated) | Blue and teal are safe defaults. The darkened "gold" text on military (#8A5A00, #755800) sits in the least-liked region. |
| Color-emotion associations are largely shared across 30 nations (4,598 people) | [Jonauskaite et al. 2020, *Psychological Science*](https://biopen.bi.no/bi-xmlui/bitstream/11250/2761614/1/Jonauskaite_etal_2020_PsychScience.pdf) | A for associations | Associations are not behavior. Nothing here says a color makes people tap more. |
| The famous "red impairs achievement" effect doesn't hold up once publication bias is corrected (67 effect sizes) | [Gnambs 2020, *Psychonomic Bulletin & Review*](https://link.springer.com/article/10.3758/s13423-020-01772-1) | A | Discount "color psychology" claims about buttons and moods. Red is fine as a school or branch color. |
| 57% of page-viewing time is above the fold and 74% in the first two screens (120 people, 2018) | [Nielsen Norman Group, "Scrolling and Attention"](https://www.nngroup.com/articles/scrolling-and-attention/) | B for desktop; C applied to phones | People scroll, but attention drops below the first screen. What the reader taps should be on it. |
| In 780 people seen using phones in public, 49% used one hand, mostly the thumb | [Hoober 2013, UXmatters](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php) | B/C (observational, older) | Big tap targets in the lower and middle screen. Doing mode already does this well. |
| Lowercase is more legible than all-caps at the same size; the gap narrows when caps are set larger | Smith, Lott & Cronnell 1969, as reviewed in [Arditi & Cho 2007, *Vision Research*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2016788) | B | All-caps condensed display type is fine for 2–6 word headlines and buttons. It's slow for three-line sentences. |
| QR scanning is common, and 18–29s are the most active group (for example, 45% of US shoppers scanned a marketing QR code in a three-month window, 2021) | Statista via [secondary summaries](https://www.qrcode-tiger.com/qr-code-demographics); a [2011–12 panel](https://rd.springer.com/content/pdf/10.1007/978-3-642-39191-0_18.pdf) found older adults far less likely to scan | C | Scanning isn't the barrier for these groups. What happens in the first screen after the scan is. |
| Most young phone users prefer dark mode | Self-selected polls (for example [Android Authority](https://www.androidauthority.com/dark-mode-survey-results-1090716/)); no rigorous Gen Z data found | C/D | Career already follows the phone's setting. Students and military are light-only, and nothing strong says that costs starts. Leave it alone for now. |
| Gen Z "likes" maximalist, comic or retro visuals; millennials "like" clean minimal ones | Trend reports and agency decks only | D | Treat both looks as hypotheses. Section 7 tests whether a look beats a plain page at all. |

**Where the evidence is weak, plainly:** there is no good evidence that any
particular hue makes a stranger more likely to tap or start. The strong
evidence is about **attention** (what's on the first screen), **planning**
(a specific day and time), **legibility** (case, size, contrast) and
**affiliation** (people like their own institution's colors). The schemes
below are built on those, and the rest is judgment to be tested.

---

## 3. Critique of each Mr. Life Manager look

### Shared landing-page layout (all three audiences)

At 390 × 844, here is where the first door's headline lands:

| Page | Top bar | First door headline | Doors fully visible |
|---|---|---|---|
| /career | 1 row, about 65 px | about 740 px | 0 (one headline) |
| /students | 1 row, about 70 px | about 730 px | 0 (one headline) |
| /military | **2 rows** (five swatches wrap), about 100 px | about 840 px | 0 |
| Classic home | 1 row | about 990 px | 0 |

- **Gets in the way:** the three "1 Pick what's true / 2 Do it now / 3 Done
  means done" pills take about 130 px and look like buttons (white chips with
  shadows on career, hard-shadow boxes on students, dark filled bars on
  military), but they aren't buttons. That's a false affordance at the exact
  point where the reader is looking for something to tap. They explain a
  process the doors make obvious. **Cut them.**
- **Gets in the way:** the lede ("Pick the one that's true today. Six steps on
  your phone, in order. No account, no app.") and the doors intro ("What's
  going on right now? Not home? Pick a time…") say the same thing twice. Keep
  one line: "Not home? Pick one anyway and choose a time." That's the line
  that turns a flier scan into a scheduled time.
- **Helps:** the door card itself is good. It has a problem in the reader's
  words, a time estimate pill, one line of scope, and a verb ("Get it back →").
  The whole card is the link, so it's a large target.
- **Decoration:** door stripes in two colors (blue vs. amber or yellow) with no
  meaning the reader can see.

**The swatch bar, placement and cost.** It's the first interactive thing on
the page, at the top, in the thumb's hardest reach. It costs about 50 px on
career and students and about 100 px on military, where five 44 px swatches
plus the "COLORS" label wrap to a second row. Benefit: picks are counted, and
choosing may make the page feel like theirs, which is plausible but untested.
Cost: on a one-handed phone it pulls the first tap toward play rather than
toward a problem. **Recommendation:** keep it in the top bar (every visitor
still sees it), drop the "COLORS" label (the buttons keep their aria-labels),
and size the swatches at 36 px so all five fit on one row next to the brand.
That's still above the WCAG 2.2 AA 24 px target minimum. Move it below the
doors only if section 7 shows it is drawing taps away from them.

### Career (clean, all sans; teal, navy, plum)

- **Landing.** It's the most legible of the three, and the sans-only type and
  light/dark support suit the audience. The headline ("Your job gets your best
  hours. Here's what to do with what's left.") runs to six lines at phone
  width, which is fine if the pills go. The tinted hero band is quiet and
  effective. Coral "Get it back →" next to teal "Clear the table →" looks
  random. Make every door's stripe and verb `--blue`, and keep `--amber` for
  the one note ("Traveling this week?").
- **Task page.** "I'm there. Start now." lands at about 845 px, just below the
  fold, because the tinted header (1.6 rem extra padding) and the "Grab these
  first" card push it down. The eyebrow pill reads "MR. LIFE MANAGER," which
  wastes the best label slot. The reader tapped "Back from a long week, or a
  trip," and the page now says "Your place is a mess. Again." Carry their words
  into that eyebrow ("Back from a trip") so they know they landed in the right
  place. "Not right now" as an outline button frames scheduling as declining;
  see section 6.
- **Doing mode.** It's good: one step per screen, a large filled "Next step"
  in the thumb zone, a progress strip and "1 of 6." "Not ready? Pick another
  time" is the right escape. Nothing to change.
- **Finish.** "That counts." works. The page then becomes an email card with
  an amber top rule that's heavier than the win itself. A small, quiet check or
  "Done" mark above the headline would let the win land before the ask. Low
  effect on starts, but it helps the reader come back.
- **Contrast:** all pairs pass AA. The amber "time" pills on amber-soft are at
  4.55–4.65:1 in small bold text, which passes with no headroom. Section 5
  darkens amber slightly.

### Students (Comic Panel: Bangers, halftone dots, hard ink shadows)

- **Landing.** It's the most distinctive look, and the yellow-tape headline
  shadow is legible and fun. Problems:
  - Door titles are set in Bangers, all caps, slanted and condensed, at
    1.45 rem across three lines ("MOVE-IN DAY. FIRST NIGHT IN THE NEW PLACE.").
    That's the slowest-reading setting on the site for the most important text
    on the page. Put door titles in bold Archivo, sentence case, and keep
    Bangers for the h1, the verb line ("HANDLE TONIGHT →"), time pills and
    buttons.
  - Every box has the same 3 px border and 5 px hard shadow: the pills, the
    doors and the note. When everything is a panel, nothing is the button.
    Give the hard shadow only to things you can tap (doors, buttons).
  - The "warm" door stripe is yellow, the same as the kicker and pills, so it
    reads as decoration.
- **Task page.** The fork is above the fold (start button at about 717 px),
  which is good. "READY TO START? GIVE IT ABOUT AN HOUR AND A HALF." is set in
  Bangers at about 1 rem and is hard to read. Three type families are on
  screen at once (Bangers, Archivo, Source Serif), which looks busy. Set
  `--serif` to the sans stack like career does. The halftone dots run behind
  the step text. Contrast still passes (slate on a dot is about 6.7:1), but
  it's texture behind reading. Keep the dots in the hero and at the page
  edges, or lower them to about 6% under the steps.
- **Doing mode.** It's good. The blue "NEXT STEP" in Bangers with a hard
  shadow is the best use of the look: big, tappable, on-theme.
- **Finish.** "THAT COUNTS." on yellow tape works. This is the one place a
  comic flourish earns its keep: a small "DONE!" burst would reward the
  finish. Today the page goes straight to the email card.
- **Dignity:** fine. The look is playful, not mocking.

### Military (Mission Board: Saira Stencil, dashed panels, branch colors)

- **Landing.** The dark top bar with the gold rule and the stencil headline
  read immediately as "this is for us," so the audience recognizes itself.
  Problems:
  - The swatch bar wraps to two rows, and the first door starts at the bottom
    edge of the screen.
  - The how-it-works pills are dark filled bars with white bold text, which is
    exactly what the buttons look like on this look. They're the strongest false
    affordance on the site.
  - Gold accent text ("NOW YOU SET THE STANDARD." in #8A5A00, and #755800 on
    black and gold) renders olive-brown. It passes contrast (4.9 and 5.5:1),
    but it reads muddy, and it's the low-preference color region in Palmer &
    Schloss. Set it in ink with a gold highlighter bar behind it (CSS in
    section 6). That keeps the gold and loses the mud.
  - Door titles in Saira Stencil at 1.15 rem: the stencil gaps break up the
    letters at small sizes. Use stencil for h1/h2 and buttons, and bold sans
    caps for door titles.
  - The "~3 hours" one-room door is a big ask from a flier. It's a natural
    "pick a time" door; see section 6.
  - The black and silver scheme's accent is blue (#2E4F8C), so the
    headline reads black and blue. Section 5 fixes it.
- **Task page.** The fork is above the fold (start at about 795 px). The gold
  filled "I'M THERE. START NOW." with a hard offset shadow is the strongest
  start button in the whole system. The dashed inner outline repeats on every
  card, which is busy but on-theme, so keep it.
- **Doing mode.** It's the best of the three: the gold "NEXT STEP" is
  unmissable, with high contrast (7.5–12.5:1 dark on gold).
- **Finish.** Same note as the others: a stamped "COMPLETE" mark is on-theme
  and cheap.
- **Contrast:** gold and silver fills against the paper are only 1.2–1.6:1, so
  those buttons depend on their 2 px dark border to be seen as buttons (WCAG
  1.4.11). Keep the border on every fill. `--blue-deep` on `--blue-soft` is
  1.6–2.2:1. It's only used as a hover fill on military, so keep it out of text.

### Classic main site (fixed; noted for comparison)

The home page has the same fold problem but worse: a five-line headline, a
serif paragraph, and a "Start with what's going on right now →" button that
only scrolls. The first door sits at about 990 px. The door cards with
category badges ("RESET · COMPANY") are clean, though the badges are internal
categories, not the reader's words. The classic task page puts the fork above
the fold (start button at about 730 px). Even keeping the classic look, the
hero could be half as tall.

---

## 4. Critique of the Charles Fan Club

The Fan Club does a different job: a small members' club with families who
come back again and again. **A returning member can afford more decoration than
a stranger who scanned a QR code once.** That's the main reason not to port
its richness wholesale.

**What works**

- **Color with a meaning.** Each club has its own colored header band (Fan
  Club yellow, Run Club blue, Bible Club green). A reader learns the code in
  one glance. Mr. Life Manager's door stripes have no such meaning.
- **The ticket metaphor** (`comic-ticket.html`): a big date stub ("SAT 21
  NOV"), "ADMIT ONE CREW," then punched "USED" afterward. It turns a date into
  an object you hold. That's exactly what a scheduled time needs to feel
  committed (see section 6, item 6).
- **"The plan" as one numbered panel** on the home page. The 1-2-3 sits
  inside a single card, so nothing looks tappable that isn't. That's better
  than Mr. Life Manager's three separate pills.
- **Strong primary buttons:** "SEE THE CALENDAR" is a filled blue with a hard
  shadow, and "VOTE IN THE POLL" is the outlined secondary. The hierarchy is
  clear.
- **The interlace background** is calmer than halftone dots behind text.
- **The comic-orange scheme** (navy ink, orange accent, sky-blue tape) is
  finished and works. It's borrowed below as the fourth student scheme.

**What doesn't**

- The nav wraps to two rows ("DESIGN OPTIONS" alone on row two), so every
  page loses about 180 px of header.
- On the event mockups, the sticky "Members RSVP here / SIGN IN (DEMO)" bar
  covers the title and date at 390 px.
- **Locked states repeat.** Cover, ticket and reel each show three or four
  padlock boxes with "SIGN IN (DEMO)." A public visitor mostly sees what they
  can't have. The dossier's black redaction bars make it worse: clever for
  members, unwelcoming to a parent who's deciding whether to join.
- The "mission" event designs render in the comic theme by default (Bangers
  headlines), so the screenshots don't actually show Mission Board. Review
  them with `#theme=mission`.
- The preview controls take the whole first screen. That's fine for an owner
  review tool, but they're not part of the design.
- **Choice overload in the options page:** two themes, eight color schemes,
  three backgrounds and several layouts. That's useful for Charles to explore
  and too much to show readers. The same instinct is behind three to five
  schemes per Mr. Life Manager page.
- The flyer page in the screenshots shows an empty state ("No event chosen")
  with an active "PRINT FLYER" button.

**What Mr. Life Manager should borrow:** the ticket (as the "That's decided"
card), the comic-orange scheme, one panel for any numbered explanation,
color-with-meaning, and the interlace texture if the dots stay.
**What it shouldn't borrow:** sticky bottom bars that cover content, locked or
redacted blocks, a portrait in the hero (task pages don't introduce Dave, and
a stranger doesn't know Charles), and a nav.

---

## 5. Recommended color schemes

Schema: `--ink --paper --surface --slate --rule --rule-strong --blue
--blue-soft --blue-deep --on-blue --amber --amber-soft --tape` (+ `--dark
--on-dark` for military). `--blue` is the action fill, and `--on-blue` is the
text on it. Ratios are WCAG 2.x contrast, computed from these exact hex values.
Swatch `<i>` colors in the page markup should match `--blue` and the second
color shown.

### Career: four schemes (light and dark)

Changes from today: amber darkened slightly on the three existing schemes so
small amber text has headroom in bright light (today they pass at 4.55–4.81:1),
and a fourth scheme, **Green and graphite**, is added. Career doesn't use
`--tape`; it's set for schema completeness.

```css
/* Teal and coral (default) */
html[data-look="career-teal"]{
  --ink:#0F1D2B; --paper:#F3F7F8; --surface:#FFFFFF; --slate:#4A5A68;
  --rule:#D6E1E5; --rule-strong:#A9BCC4;
  --blue:#0B6E6E; --blue-soft:#E2F1EF; --blue-deep:#08504F; --on-blue:#FFFFFF;
  --amber:#B93C0A; --amber-soft:#FFF0E6; --tape:#FFF0E6;
}
/* Navy and amber */
html[data-look="career-navy"]{
  --ink:#111827; --paper:#F5F6F9; --surface:#FFFFFF; --slate:#4B5563;
  --rule:#DCE1EA; --rule-strong:#AEB7C6;
  --blue:#1E3A8A; --blue-soft:#E6ECFA; --blue-deep:#172C6B; --on-blue:#FFFFFF;
  --amber:#A34A06; --amber-soft:#FEF3E2; --tape:#FEF3E2;
}
/* Plum and green */
html[data-look="career-plum"]{
  --ink:#1C1424; --paper:#F8F5F8; --surface:#FFFFFF; --slate:#57505E;
  --rule:#E4DCE3; --rule-strong:#BBAFBA;
  --blue:#6B2D63; --blue-soft:#F3E8F1; --blue-deep:#52214C; --on-blue:#FFFFFF;
  --amber:#26704B; --amber-soft:#E5F3EB; --tape:#E5F3EB;
}
/* Green and graphite (new) */
html[data-look="career-green"]{
  --ink:#111418; --paper:#F4F5F6; --surface:#FFFFFF; --slate:#4B525C;
  --rule:#DDE0E4; --rule-strong:#AEB4BC;
  --blue:#15703B; --blue-soft:#E3F2E8; --blue-deep:#0F552C; --on-blue:#FFFFFF;
  --amber:#2F3A46; --amber-soft:#E8EBEF; --tape:#E8EBEF;
}
@media (prefers-color-scheme:dark){
  html[data-look^="career-"]{
    --ink:#E6EEF1; --paper:#0D161B; --surface:#14212A; --slate:#9DB0BA;
    --rule:#22343D; --rule-strong:#3A5260; --on-blue:#0D161B;
  }
  html[data-look="career-teal"]{--blue:#4FC2BB; --blue-soft:#12302F; --blue-deep:#7AD6D0; --amber:#FF9A62; --amber-soft:#2E1D13; --tape:#2E1D13}
  html[data-look="career-navy"]{--blue:#8EA8F0; --blue-soft:#18233F; --blue-deep:#B3C4F5; --amber:#F2B45B; --amber-soft:#2D2312; --tape:#2D2312}
  html[data-look="career-plum"]{--blue:#D99BCF; --blue-soft:#311C2E; --blue-deep:#E8BEE1; --amber:#7BD1A4; --amber-soft:#16291F; --tape:#16291F}
  html[data-look="career-green"]{--blue:#5FD08E; --blue-soft:#12301F; --blue-deep:#8EE0AE; --amber:#C3CCD6; --amber-soft:#1E252C; --tape:#1E252C}
}
```

| Scheme | ink/paper | slate/paper | on-blue/blue | amber/paper | blue-deep/blue-soft |
|---|---|---|---|---|---|
| Teal and coral, light | 15.8 | 6.6 | 6.1 | 5.2 | 8.0 |
| Teal and coral, dark | 15.6 | 8.2 | 8.5 | 8.8 | 8.3 |
| Navy and amber, light | 16.4 | 7.0 | 10.4 | 5.5 | 11.0 |
| Navy and amber, dark | 15.6 | 8.2 | 7.9 | 10.0 | 9.0 |
| Plum and green, light | 16.5 | 7.2 | 9.6 | 5.5 | 10.5 |
| Plum and green, dark | 15.6 | 8.2 | 8.3 | 10.0 | 9.6 |
| Green and graphite, light | 16.9 | 7.2 | 6.2 | 10.6 | 7.7 |
| Green and graphite, dark | 15.6 | 8.2 | 9.5 | 11.3 | 9.1 |

Why each suits early-career professionals:

- **Teal and coral (default).** *Evidence:* blues and cyans are among the
  best-liked colors (Palmer & Schloss). *Judgment:* teal stands apart from the
  navy of employer intranets and banking apps, so it reads as "not work" while
  staying calm and credible. Keep it as the default until starts by look say
  otherwise.
- **Navy and amber.** *Judgment:* the most conventional "professional" pair.
  It's the safe option for finance, law and consulting readers who distrust
  anything that looks like a lifestyle brand.
- **Plum and green.** *Judgment:* the one that doesn't look like a work tool.
  It may appeal to people who want home to feel unlike the office. It's the
  first one to cut if it draws few starts.
- **Green and graphite (new).** *Judgment:* a neutral page with a single
  green action color, the pattern of the work apps this group lives in all day,
  and the strongest of the four in dark mode. *Evidence:* none specific; it
  fills the neutral slot so the four picks span cool, conventional, warm and
  neutral, which makes the pick data more informative.

### Students: four schemes (Comic Panel, light)

Changes: blue, red and green are kept as they are. **Orange and navy** is added,
taken from the Fan Club's comic-orange scheme. It overrides ink, paper and
slate, so borders and shadows turn navy.

```css
html[data-look^="students-"]{
  color-scheme:light;
  --ink:#14110F; --paper:#F4EFE1; --surface:#FFFFFF; --slate:#4A443B;
  --rule:#14110F; --rule-strong:#14110F; --on-blue:#FFFFFF;
}
/* Blue and yellow (default) */
html[data-look="students-blue"]{--blue:#1B47A0; --blue-soft:#E6ECF8; --blue-deep:#143679; --amber:#A33A00; --amber-soft:#FFF3C2; --tape:#FFD23F}
/* Red and yellow */
html[data-look="students-red"]{--blue:#C3231A; --blue-soft:#FBE3E1; --blue-deep:#9A1B14; --amber:#1B47A0; --amber-soft:#FFF3C2; --tape:#FFD23F}
/* Green and gold */
html[data-look="students-green"]{--blue:#1A6B3A; --blue-soft:#E5F1E9; --blue-deep:#13522C; --amber:#7A3F12; --amber-soft:#FBECC4; --tape:#F2B632}
/* Orange and navy (new) */
html[data-look="students-orange"]{
  --ink:#12233F; --paper:#F1EEE6; --slate:#3D4A60; --rule:#12233F; --rule-strong:#12233F;
  --blue:#B23C04; --blue-soft:#FBE7DB; --blue-deep:#8F3003; --amber:#1D5A85; --amber-soft:#E2F1FA; --tape:#8FD3F4;
}
```

| Scheme | ink/paper | slate/paper | on-blue/blue | amber/paper | blue-deep/blue-soft | ink/tape |
|---|---|---|---|---|---|---|
| Blue and yellow | 16.4 | 8.4 | 8.6 | 5.8 | 9.7 | 13.0 |
| Red and yellow | 16.4 | 8.4 | 5.9 | 7.4 | 6.8 | 13.0 |
| Green and gold | 16.4 | 8.4 | 6.6 | 7.2 | 8.0 | 10.3 |
| Orange and navy | 13.5 | 7.7 | 5.9 | 6.4 | 6.8 | 9.6 |

Why: *evidence* (Schloss et al. 2011) says students like their own school's
colors more, and more so with school spirit. So the four are chosen to cover
the most common school color families: blue/gold, red, green/gold, and
orange/navy. Which family is most common across US colleges is *judgment*,
not counted. **Default: blue and yellow** for untargeted traffic (blue is the
most broadly liked hue), but **on each campus flier, set the default to the
nearest school colors with `?look=`** in the QR URL. `audience.js` already
honors it. If the first campus is purple-and-gold or maroon-and-gold, swap
the fourth scheme for that pair rather than adding a fifth.

### Military: review of the five schemes

The five color pairs and the navy-and-gold default stay. Three token changes:

1. **`--amber` becomes the scheme's dark color** on black and gold, navy and
   gold, and black and silver, matching what scarlet and blue already do.
   That removes the olive-brown text (#755800, #8A5A00) and the stray blue in
   black and silver (#2E4F8C).
2. The headline accent moves from colored text to **ink on a gold (or silver)
   highlighter bar** (CSS in section 6), so gold stays a fill.
3. No other values change.

```css
html[data-look^="military-"]{color-scheme:light}
/* Scarlet and gold */
html[data-look="military-scarlet"]{
  --ink:#1E1416; --paper:#EFE9E1; --surface:#FAF7F2; --slate:#52464A;
  --rule:#AC9C93; --rule-strong:#8C0B1F; --dark:#8C0B1F; --on-dark:#FFF7E3;
  --blue:#FFC72C; --blue-soft:#F5EDE2; --blue-deep:#E8AE12; --on-blue:#2A0A0F;
  --amber:#A50F25; --amber-soft:#F7E3E3; --tape:#FFD866;
}
/* Black and gold */
html[data-look="military-black"]{
  --ink:#141414; --paper:#ECEAE3; --surface:#F8F7F3; --slate:#4A4A44;
  --rule:#9A968A; --rule-strong:#111111; --dark:#111111; --on-dark:#F8F7F3;
  --blue:#FFCC01; --blue-soft:#F2EFE4; --blue-deep:#E0B400; --on-blue:#111111;
  --amber:#111111; --amber-soft:#F7EFCF; --tape:#FFE07A;
}
/* Blue and yellow */
html[data-look="military-blue"]{
  --ink:#0D1B33; --paper:#E6EBF3; --surface:#F7F9FD; --slate:#43506A;
  --rule:#93A2BD; --rule-strong:#00308F; --dark:#00308F; --on-dark:#F7F9FD;
  --blue:#FFD100; --blue-soft:#EBF0F9; --blue-deep:#E6BC00; --on-blue:#0D1B33;
  --amber:#00308F; --amber-soft:#E1E8F7; --tape:#FFE680;
}
/* Navy and gold (default) */
html[data-look="military-navy"]{
  --ink:#0F1E33; --paper:#E4E9F1; --surface:#F6F8FC; --slate:#44536B;
  --rule:#8FA0BA; --rule-strong:#10294A; --dark:#10294A; --on-dark:#F6F8FC;
  --blue:#F0AE1A; --blue-soft:#E9EDF5; --blue-deep:#D69A10; --on-blue:#10294A;
  --amber:#10294A; --amber-soft:#F9EFD2; --tape:#F4D98A;
}
/* Black and silver */
html[data-look="military-silver"]{
  --ink:#121419; --paper:#E4E6EA; --surface:#F5F6F8; --slate:#4A4F59;
  --rule:#9AA0AA; --rule-strong:#1C1F26; --dark:#1C1F26; --on-dark:#F5F6F8;
  --blue:#B4BAC3; --blue-soft:#ECEEF1; --blue-deep:#9AA1AC; --on-blue:#121419;
  --amber:#1C1F26; --amber-soft:#E3E8F2; --tape:#CDD2DA;
}
```

| Scheme | ink/paper | slate/paper | on-blue/blue | amber/paper | blue-deep/blue-soft* | on-dark/dark |
|---|---|---|---|---|---|---|
| Scarlet and gold | 14.9 | 7.5 | 11.7 | 6.5 | 1.7 | 9.0 |
| Black and gold | 15.3 | 7.4 | 12.5 | 15.7 | 1.7 | 17.6 |
| Blue and yellow | 14.4 | 6.8 | 11.8 | 9.6 | 1.6 | 11.0 |
| Navy and gold | 13.7 | 6.4 | 7.5 | 12.0 | 2.1 | 13.7 |
| Black and silver | 14.7 | 6.6 | 9.4 | 13.2 | 2.2 | 15.3 |

\* On military, `--blue-deep` is the hover fill under dark `--on-blue` text,
not a text color, so this pair fails by design. Keep it out of text. The gold
and silver fills are only 1.2–1.6:1 against the paper, so the 2 px `--dark`
border on every filled button is what makes them visible as buttons. Keep it.

Why: *inference from evidence* (Schloss et al. 2011 found that liking an
institution carries over to its colors): branch colors should feel like "ours"
without a name or logo, which also respects the no-endorsement guardrail.
*Judgment:* dark text on a gold fill is the highest-contrast action color in
the whole system, and it holds up in glare. **Navy and gold as the default**
is reasonable: navy and gold read as "military" broadly rather than as one
branch's identity. For base-specific fliers, the same `?look=` approach as
campuses is available if Charles wants it. The page still won't name a branch.

---

## 6. Other visual changes, ranked by expected effect on starting or scheduling

| # | Change | Why | Effort |
|---|---|---|---|
| 1 | **Compact hero: two doors visible on a 390 × 844 screen.** Delete `.aud-how`; cut the lede to one line ("Not home? Pick one anyway and choose a time."); remove the doors' intro paragraph; hero padding about 1.4 rem; h1 `clamp(1.9rem,7vw,3.2rem)`. Military: swatches on one row (item 8). | Attention falls off below the first screen (NN/g); today no door is fully visible on any page. | Small |
| 2 | **Make scheduling a named, equal action.** Rename "Not right now" to **"Pick a time"**, and style it as a solid secondary button, not an outline. When `from` starts with `qr-`, make "Pick a time" the filled button and "I'm home. Start now." the secondary. | Specific day-and-time plans raise follow-through (Gollwitzer & Sheeran; Milkman). Flier readers are rarely home. | Small (label, CSS); small JS for the QR swap |
| 3 | **Task page: fork above the fold on every look, and carry the door's words.** Career: drop the extra header padding on phones. All: replace the "MR. LIFE MANAGER" eyebrow with the door's phrase (pass `door=` on the door link; entry.js sets the eyebrow from a short allowlist). | The reader confirms "this is my problem" and sees the two choices without scrolling. | Small (padding); medium (eyebrow) |
| 4 | **Type discipline in the themed looks.** Bangers and Saira Stencil for the h1, step numbers, verbs, pills and buttons only. Door titles, `.fork-lead` and `.later h2` in bold Archivo, sentence case. Set `--serif` to the Archivo stack on students and military, as career does. | All-caps condensed sentences read slower; three families on one screen is noise. One fewer font to load. | Small |
| 5 | **One action color on doors.** Every door's stripe and verb in `--blue`; `--amber` only for the single note. Students: give the hard shadow only to tappable things. | The two-color code has no meaning the reader can see; when everything looks like a button, nothing does. | Small |
| 6 | **Turn "That's decided" into a ticket.** After a time is picked, show the day and time large, as an object: a ticket stub on students (borrowed from the Fan Club), "orders" with a stamp on military, a calendar card on career. "Add to my calendar" is the filled button. | It makes the specific time concrete, which is the mechanism behind implementation intentions. *Judgment* that the visual form adds to it. | Medium |
| 7 | **Military token fixes and highlighter headline** (section 5), with this CSS: `html[data-look^="military-"] .aud-hero h1 em{color:var(--ink);background:linear-gradient(transparent 58%,var(--blue) 58%,var(--blue) 92%,transparent 92%);-webkit-box-decoration-break:clone;box-decoration-break:clone}` | Removes the olive-brown text; keeps gold visible. | Small |
| 8 | **Compact swatch bar.** No "COLORS" label; 36 px swatches; one row on all pages. | Saves 50–100 px of the first screen and still shows every visitor the swatches. | Small |
| 9 | **Self-host Archivo** (as Bangers and Saira already are). | Campus and base networks can be slow or filtered; the screenshots show Google Fonts being blocked. | Small–medium |
| 10 | **A small reward mark on the finish page:** a "DONE!" burst on students, a "COMPLETE" stamp on military, a check on career, above "That counts." | Lets the win land before the email card. Little effect on starts; may help return visits. | Small |
| 11 | **Halftone dots off the step text** (keep them in the hero and at page edges, or lower to about 6%). | Texture behind reading; small legibility cost. | Small |
| 12 | **Add `look` to every tracked event** (`data.look = document.documentElement.dataset.look` in `track()`). | Needed for section 7: today `start-now` and `time-picked` don't say which scheme the reader had. | Small |

**What I'd cut outright:** the how-it-works pills, the duplicate intro line,
the "COLORS" label, and the two-color door code. **What I'd keep even though
it's decoration:** the rotated tape kicker, the dashed mission-board outlines
and the hero halftone. They're cheap, they signal "this is for you," and they
don't block a tap.

---

## 7. What to test

Ship items 1, 4, 5, 7 and 8 without testing. They rest on attention and
legibility evidence and have little downside. Test the things that are really
in doubt. Traffic will be small, so read each test only after at least about
100 landing visits per arm (judgment). Treat results as directional, and stop
only for large differences.

**Before any test:** add `look` to tracked events (item 12). Count a scheme by
the **look a reader had when they tapped a door and started or picked a
time**, not by `scheme-picked` taps, which mostly measure curiosity. The
`from` tag is enough to identify each flier, because a QR visitor's
`from=qr-<place>` carries through the doors, and the look family identifies
the audience.

1. **Schedule-first vs. start-first for QR visitors.** For visits with
   `from=qr-*`, randomly show either "Pick a time" or "Start now" as the filled
   button (50/50 in entry.js, variant sent with events). Primary metric:
   (`start-now` + `time-picked`) per task-page visit. Secondary: `finished`
   with `path=appointment` within seven days of the picked time. This tests the
   biggest assumption in this review: that people holding a flier aren't
   home.
2. **Campus colors vs. the house default (students).** On one campus, print
   two batches of the same flier: one QR with `?look=` set to the nearest
   school colors (`from=qr-<place>-school`), one with no look
   (`from=qr-<place>-house`). Metrics: door taps per visit (task-page visits
   carrying the tag ÷ landing visits), then starts plus times picked. Also
   watch `scheme-picked` per visit. If fewer people switch away from the
   school colors, the fit is working.
3. **Does a look beat a plain page at all?** Alternate fliers at one location
   between `/students` (Comic Panel) and a copy of the same page that uses
   the plain career look (for example `/students-plain` with
   `data-look="career-teal"`). It has to be a copy, because any
   `students-*` scheme picks up the comic styling. Same copy, same doors, and
   the only difference is the look. Metric: starts plus times
   picked per visit. If the plain page does as well, stop investing in looks
   and put the effort into copy and checklists. If the look wins, it's earning
   its place.
