# Growth research: Instagram video and taking payments

Two reports from 2026-11-12, written to answer Charles's questions: can the
faceless videos get clicks and finished checklists from Instagram, and what is
the cheapest honest way to take payment without getting soaked.

| Report | Question | Short answer |
|---|---|---|
| [instagram-faceless-video.md](instagram-faceless-video.md) | Can faceless Reels get clicks and finished checklists? | Clicks yes, but few. Sales from cold Instagram: not plausible at our scale. The win is finished checklists that feed the email list. Fix the format first (no sound and mostly text is something Instagram itself ranks lower), test the calendar button inside Instagram's browser, then run a capped two-hook test. |
| [payments-options.md](payments-options.md) | Do we need SamCart? | No. It is $79 a month and would have to add about 112 extra $9 sales a year to break even. Start with Stripe at $0 a month, with MailerLite delivering a downloadable guide. The open question is Idaho sales tax on digital guides, a CPA question. |

## What was checked (2026-11-12)

The claims that decide the recommendations were read again on the primary pages:

| Claim | Result |
|---|---|
| Instagram's 2023 ranking post says muted reels and majority-text reels are made "less visible" | Confirmed: [about.instagram.com, May 31, 2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained/). The page says "watermarked" and "low-resolution," not "from other apps" or "blurry." It is three years old, so it may have changed. The Help Center's recommendation guidelines were not read. |
| SamCart: Core $79, Pro $199 a month, 2.9% + 30¢ | Confirmed on [samcart.com/pricing](https://samcart.com/pricing). |
| Stripe: 2.9% + 30¢ domestic cards, no monthly fee, $15 per dispute | Confirmed on [stripe.com/pricing](https://stripe.com/pricing). |
| Idaho: 6% sales tax; digital books, videos, music or games with a permanent right to use are listed among retail sales | Confirmed on the [Idaho Tax Commission basics guide](https://tax.idaho.gov/taxes/sales-use/online-guide/) (updated April 1, 2026). The page lists them as examples; it doesn't say whether a PDF checklist counts. |
| Meta ad standards bar ads that assert or imply a person's mental health | Confirmed on [Meta's personal attributes policy](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/). Its example is "Depression getting you down? Get help now." The phrase "negative self-perception" is in the general ad standards, tied to diet and health products. |

Not checked: vendor pages other than Stripe and SamCart, Instagram's Help Center
and creator pages, and every benchmark figure in the Instagram report (all are
labeled with a grade and several are labeled guesses in the report).

## What needs a decision

- **Sound and real footage** for the videos. This departs from "no sound needed"
  in [video/README.md](../../../video/README.md).
- **Calendar button in Instagram's browser.** The invite is a `data:` download
  that may not work there. Test on a real phone before spending anything.
- **Sales tax on digital guides.** Eight questions for a CPA are at the end of
  section 4 of the payments report. They decide whether a seller's permit is
  needed before the first sale.
- **What the paid product is.** It must be clearly more than the free
  checklists (ADR-020, ADR-022). Neither report picks it.
