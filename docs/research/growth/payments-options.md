# Taking payments: options, costs and traps for Mr. Life Manager

**Researched:** 2026-11-12. Every vendor figure below was read from the vendor's own page on that date unless the table says otherwise. Not legal or tax advice.
**For:** Charles Warloe (sole proprietor, Idaho). EIN, assumed business name and business bank account are still to do.
**Status of the evidence:** vendor pricing and terms are Grade A and current as of the retrieval date; anything marked *unverified* is a number or claim I could not read on an official page. Cost math is arithmetic on those numbers plus stated assumptions, not measured data.
**Affiliate disclosure:** I have no affiliate relationship with any vendor and used no affiliate links. Several comparison blogs I found are written by competitors or affiliates (Grade C). I used them only to find leads, and I checked every number I rely on against an official page, or I marked it unverified.

---

## Verdict (6 lines)

1. **SamCart is not needed and cannot pay for itself at 50 to 100 sales a year.** Core is $79 a month ($948 a year) and its card fee is the same 2.9% + 30¢ you pay Stripe directly, so it never wins on fees. To cover $948 it would have to add about 112 extra $9 sales, 37 extra $27 sales or 27 extra $37 sales a year, on top of your whole first-year goal.
2. **The cheapest honest start is a Stripe Payment Link (or a MailerLite digital product, which runs on Stripe).** $0 a month, 2.9% + 30¢ a sale: $0.56 on a $9 guide (6.2%), $1.08 on $27 (4.0%), $1.37 on $37 (3.7%). You are the seller of record, so you own sales tax, refunds and disputes.
3. **At $9 the fixed fee is the whole story.** Merchant-of-record tools (Lemon Squeezy, Paddle, Polar) charge 5% + 50¢, which is 10.6% on $9. Stripe's own merchant-of-record option adds 3.5% on top of card fees (6.4% + 30¢, 9.7% on $9). Gumroad is about 21.8% on $9 if its help page is right. Don't bother with Gumroad at $9.
4. **A merchant of record does not help with the weekly call.** Stripe's own eligibility page says live coaching and professional services do not qualify for Managed Payments. Calls need ordinary Stripe plus a tax decision.
5. **Tax is the real open question, not the platform.** Idaho's own guide lists "digital books, videos, music, or games with a permanent right to use" as taxable. Whether a PDF checklist counts, and whether a group call does, are CPA questions (section 4).
6. **Biggest uncertainty:** whether Idaho taxes the $9 to $37 guides. It decides whether you need a seller's permit before the first sale, and it is the only reason to pay a 3.5% to 7% premium for a merchant of record. Do not pay that premium until the CPA answers.

---

## 0. What this report assumes (from Charles's answers)

- **Free first.** Instagram leads to the free checklists. Paid offers are sold afterwards, from the finish page, an email, or the weekly call. The buyer has already finished a checklist and joined the email list. The $9 sale is a warm, later purchase.
- **Cases modeled:** one-time $9, $27 and $37 guides, plus the weekly group call (single call, 4-call pack, monthly with pause). A $0 product is covered in section 2.
- **Prices are placeholders.** ADR-022 says price follows cost to deliver and the price is not set. Nothing here picks a product or a price.
- **Buyers open email on phones.** Mobile checkout still matters. The Instagram in-app browser is a short note (section 1C), because few buyers will buy from there.
- **Fixed constraints from the repo:** no auto-renewing charge for people who aren't using it (vision doc, ADR-022), easy refunds, adults only, MailerLite and Umami stay, static GitHub Pages site with no backend, so any checkout is hosted by someone else.

---

## 1. The landscape

How to read the tables: **Seller of record** means you are the legal seller, you collect and remit any sales tax, and you handle refunds and disputes (Stripe, PayPal, Square and most tools). **Merchant of record (MoR)** means the vendor is the legal seller to the buyer, collects and remits the tax, and handles most disputes, and it pays you what is left after its fee. "Not found" means the official page I fetched did not say, not that the feature is missing. Sources are numbered in the Sources section.

### 1A. Price and money

| Vendor | Model | Monthly fee | Per-transaction fee | Add-ons and gotchas | Payout timing, minimum, holds | Sales tax | Source |
|---|---|---|---|---|---|---|---|
| **Stripe Payment Links / Checkout** | Seller of record; Stripe is processor | $0 | 2.9% + 30¢ domestic card; +1.5% international card; +1% if currency conversion | Custom domain $10/mo (optional). Billing (subscriptions) adds 0.7% of Billing volume. Stripe Tax Basic 0.5% per transaction *where you are registered* (see note). Radar fraud tool is optional, from $0.05 per screened transaction. Instant payout 1.5%, 50¢ minimum. Disputes $15. Invoices after payment 0.4% capped at $2 | First payout typically 7 to 14 days after the first live payment; after that daily payouts, US settlement default 2 business days. Standard payouts free. Minimum payout $0.01 | You. Stripe Tax can calculate and collect, but you register and file | S1, S2, S3 |
| **Stripe Managed Payments** (Stripe's MoR add-on for Checkout and Payment Links) | MoR (Stripe; buyer sees "Sold through Link") | $0 | **3.5% on top of** the 2.9% + 30¢ card fee, so 6.4% + 30¢ | Digital products only. **Excludes** professional services and live 1-to-1 coaching ("human intervention"). Excludes custom domains. Seller must pass an eligibility review. | Same Stripe payouts | Stripe collects and remits in "more than 75" (pricing page) or "more than 80" (docs) countries. US seller supported | S1, S4, S5 |
| **MailerLite digital products** | Seller of record; payments run on Stripe (you connect your own Stripe account) | Free plan: 1 product. Comfort "from $12/mo": 5 products. Power "from $25/mo": unlimited | **0% MailerLite commission**; you pay only Stripe's fee (same as above) | Products made inside MailerLite are **one-time downloads only** (PDF, ePUB, images, or a redirect URL). Subscriptions work only if you create the product in Stripe and sell it through MailerLite. Free plan listed at up to 250 subscribers | Stripe's payouts | You (a "collect tax IDs" option exists; no tax calculation described) | S6, S7, S8 |
| **Lemon Squeezy** | MoR | $0 | 5% + 50¢; +1.5% international; +1.5% PayPal; +0.5% subscriptions | Abandoned-cart recovery +5%, affiliate referrals +3% (opt-in features). **Products under $10 are routed to "contact us" for custom pricing.** Stripe is folding Lemon Squeezy into Managed Payments (Jan 2026 post); no migration steps, dates or fees were given | Payouts on the 1st and 15th, net sales held 13 days; **$50 minimum**; US bank payout free | LS collects and remits | S9, S10, S11 |
| **Paddle** | MoR | $0 | 5% + 50¢ per checkout | "Products under $10 value: contact us for bespoke pricing." Chargebacks covered in the fee; no payout fee stated | Not found on pricing page | Paddle | S12 |
| **Polar** | MoR | Starter $0; Pro $20; Growth $100; Scale $400 | Starter 5% + 50¢; Pro 3.8% + 40¢; Growth 3.6% + 35¢; Scale 3.4% + 30¢; +1.5% non-US cards | Payout fees are Stripe's: $2 per month with active payouts + 0.25% + $0.25 per payout. Disputes $15 regardless of outcome. Rates changed for orgs created on or after 2026-05-27 | Manual withdrawals available | Polar | S13 |
| **Gumroad** | MoR (since 2025-01-01) | $0 | Help page: **10% + 50¢ plus card processing 2.9% + 30¢ plus PayPal fees**, i.e. about 12.9% + 80¢. The pricing page headline shows only "10% + $0.50" and says "no hidden fees"; the two pages disagree. Discover (marketplace) sales: flat 30% | Instant payout 3%. Fee drops to 5% + 50¢ after $20,000 in a month | Weekly, monthly or quarterly payouts need **$100 minimum** and a 7-day hold; new accounts go through a 1 to 3 week review ("typically 3 to 4 sales with a balance over $100") | Gumroad handles it | S14, S15, S16 |
| **Payhip** | Seller of record (not a full MoR); sells through your Stripe and/or PayPal | Free $0 (5% fee); Plus $29 (2% fee); Pro $99 (0% fee) | Platform fee above **plus** Stripe/PayPal at standard rates | All plans have the same features | "Deposited immediately" to your processor account | Payhip says it collects, reports and remits EU/UK VAT and US/Canada sales tax | S17 |
| **SamCart** | Not stated on pricing page whether MoR; uses its own "SamPay" processing | Core $79; Pro $199 (yearly shown as "25% off", price not shown); optional live support $19 | SamPay 2.9% + 30¢ on both plans; "Tax collection" 50 bps (Core) or 35 bps (Pro), basis not explained | 7-day free trial. Core vs Pro feature split is not clear in the text I could read (Pro lists order bumps, upsells, subscription saver, affiliate center) | Not found | "Tax collection" fee above; mechanism not described | S18 |
| **Podia** | Not stated | Mover $42/mo billed yearly ($504) or $49 monthly; Shaker $84 yearly; Earthquaker $150 yearly | Mover adds 5%; Shaker and Earthquaker 0%; Stripe or PayPal still charge 2.9% + 30¢ | No free plan, 14-day trial. Mover limits: 100 email subscribers, 50 products. Upsells and affiliate only on Shaker and up | Not found | "Sales tax in 230 countries" included; whether Podia remits is not stated | S19 |
| **PayPal checkout / links** | Seller of record | $0 | **Unverified.** Official page returned 403. Secondary sources: 3.49% + 49¢ standard, 4.99% + 9¢ "micropayments" (needs enabling; roughly for sales under about $10 to $12) | Not verified | Not verified | You | S20 (Grade B only) |
| **Square Payment Links** | Seller of record | $0 | Square's Payment Links page reportedly lists 3.3% + 30¢ for new customers (read through a search snippet; the page itself was rate-limited). Help center lists 2.9% + 30¢ for Square Online sites | Standard receipt only, per a review | Not verified | You | S21 (partly unverified) |
| **Ko-fi (free plan)** | Seller of record via your Stripe/PayPal | Free; Gold reportedly $12/mo | 5% on shop sales on the free plan, plus Stripe/PayPal processing | Tip jar first, shop second. Official pages returned 403; fee table read through a search snippet of the official help center | Not verified | You | S22 (partly unverified) |
| **Buy Me a Coffee** | Seller of record via Stripe | $0 | 5% + Stripe 2.9% + 30¢ + 0.5% payout fee; +1% outside US; +0.5% subscriptions; fees are not returned on refunds or chargebacks (official help article, read via search snippet) | Whether the 5% covers shop sales is not confirmed on an official page | Not verified | You | S23 (partly unverified) |
| **Shopify Basic** | Seller of record | $29/mo billed yearly, $39 monthly; "Starter" plan not on the pricing page I fetched | Online card 2.9% + 30¢ (Basic); +2% on third-party gateways | 3-day trial then $1/mo for 3 months | Not found | You, with tools | S24 |

**Note on Stripe Tax:** the pricing-page text I fetched showed Tax Basic at 0.5% per transaction (or $0.50 per transaction by API) and Tax Complete from $90 a month on a one-year contract, but the raw page did not show these lines, so treat the Tax numbers as *verify before relying*.

### 1B. Refunds, subscriptions, delivery, lock-in

| Vendor | Refunds and disputes | Buyer cancels a subscription | Delivers the file | One-time, per-session, packs | Coupons, free trial | MailerLite, webhooks, export | Lock-in notes |
|---|---|---|---|---|---|---|---|
| **Stripe Payment Links** | One click in Dashboard (full or partial, bulk full). Fees from the original sale are **not returned**. Disputes: you respond; customers cannot dispute a fully refunded payment | Customer portal; cancel is on by default; **pause** is an option in the redesigned portal | **Does not host files.** After payment: custom message or redirect to your own URL (can carry the session ID) | One-time; quantity can be editable (buyer picks 1 to 4 calls); "customers choose what to pay" with min and max; subscription links | Promotion codes and trial days supported | `checkout.session.completed` webhook; Zapier partner; MailerLite is a Stripe integration | Customers and subscriptions live in **your** Stripe account; CSV exports; low lock-in |
| **MailerLite product** | Refunds go through Stripe ("Begin refund"); MailerLite is not involved | Via Stripe-created products only | **Yes**: PDF/ePUB/images hosted, order confirmation page, confirmation email | One-time only if made in MailerLite | Discount codes: not mentioned | Group add/remove after checkout built in; buyers must tick a marketing box for e-commerce automation triggers | Same Stripe account; your list is already in MailerLite |
| **Stripe Managed Payments** | Stripe handles disputes and evidence; buyer can ask Link support for refunds; Stripe may refund within 60 days and, if you do not answer in 48 hours, may refund without approval. Stripe may keep the original tax on refunds in some places | Buyer can cancel in the Link app | As Payment Links | Subscriptions only through Checkout and Payment Links (not elsewhere) | As Stripe | Buyer data deletion request cancels their subscriptions and deletes the objects | Buyer relationship runs through Link; moving subscriptions out later is not documented (unverified) |
| **Lemon Squeezy** | Refund anytime in dashboard; **platform fee kept**. LS handles chargebacks: refunds the buyer, deducts refund minus fee plus a $15 dispute fee. LS may refund within 60 days even if you promise no refunds | Customer portal ("new" feature) | Yes: signed, throttled download links, license keys | One-time, subscriptions, pay-what-you-want, lead magnets | Discount codes listed | Developer docs and API exist | Migration to Stripe in progress; no steps or dates given |
| **Paddle** | Chargebacks covered under fee; refund terms not on pricing page | Not found | Not found | Not found | Not found | Not found | Not found |
| **Polar** | $15 dispute fee, non-refundable; may suspend accounts approaching ~0.7% chargeback rate | Subscriptions, trials, discounts are features | Not confirmed ("Downloads" appears in site navigation; no pricing-page statement) | Subscriptions, seats, credits | Trials, discounts | Documented API | Not found |
| **Gumroad** | Gumroad handles refunds and disputes in its sole discretion; **you reimburse it**. On refund, Gumroad's own 10% + 50¢ is returned; the processing portion is kept. A buyer who files a dispute loses the right to a Gumroad refund. Refund rate over 15%: 25% of funds reserved for 90 days; over 25%: account may be suspended | Memberships supported | Digital products are its core use (pricing FAQ); hosting details not retrieved | One-time and memberships | Not retrieved | Sales CSV export | Terms bar you from circumventing the fee |
| **Payhip** | Seller-handled; not covered on pricing page | Memberships listed; details not given | Hosted digital products (feature) | Not found | Not found | Not found | Not found |
| **SamCart** | Not on pricing page | "Let customers manage their own subscriptions" | Sells digital products, courses | One-time and subscriptions | Order bumps and upsells (marketing, vendor-claimed conversion lifts) | Not found | Contract: FAQ answer hidden in what I fetched |
| **Podia** | Podia's own refund window for *its* plan: 72 hours | Memberships listed | Yes | Digital products, memberships | Not mentioned | Zapier on Shaker and up | Plan limits on products and subscribers |

### 1C. Mobile checkout from an email or finish page

Charles named these criteria. "Not found" means I found no official statement. **I found no vendor page-speed numbers; measure your own link with a mobile Lighthouse run before you pick.** Tap counts below are inference from how Stripe-style hosted checkout works, not measurements.

| Criterion | Stripe Payment Link | MailerLite native | Stripe Managed Payments | Others |
|---|---|---|---|---|
| Apple Pay and Google Pay | Shown when the buyer's device and browser support them (dynamic payment methods) | Not found for MailerLite's own checkout; Stripe-hosted if the product is a Stripe product | Cards, Apple Pay, Google Pay, Link, Cash App Pay, Klarna, Afterpay (US) | SamCart lists Apple Pay, Google Pay, Link, Venmo (Core vs Pro unclear); others not found |
| Link / saved-card one-tap | Link is on at no extra fee; returning Link users autofill | Not found | Checkout uses Link | Not found |
| Guest checkout, no account | Yes, one-time purchases use a guest customer | Not found | Yes, with a prompt to create a Link account afterward | Not found |
| Taps to pay (inference) | With a wallet: open link, tap the wallet button, confirm with Face ID or Touch ID. With a card: email plus four card fields | Unknown | Same as Stripe | Unknown |
| Instant delivery | Redirect to your thank-you page with the file link, or custom message. Not automatic from Stripe | Yes: download page plus confirmation email | Same as Stripe: you supply the delivery | Gumroad, LS, Payhip host files |
| Receipt and refund | Automatic receipt; refund is one click, buyer sees it in 5 to 10 business days | Receipt can be sent from the order; refund through Stripe | Receipts, invoices, refund notices sent by Stripe from Link | Not verified |
| Name on the card statement | Your Stripe statement descriptor (5 to 22 characters, must reflect your assumed business name). Card payments can use a static prefix plus a per-sale suffix | Same (Stripe) | **`LINK.COM* [your descriptor]`**; buyer sees "Sold through Link", not your brand | MoR vendors: not verified; check a real test charge |
| Instagram in-app browser | See note | See note | See note | Not found |

**Instagram note (short, because the funnel is free-first).** Stripe documents Apple Pay as "supported in iOS webviews, subject to standard Apple Pay eligibility" for its Express Checkout Element, Google Pay in Android webviews only if the host app enables it, and Link, PayPal and Klarna as not supported in in-app webviews (S25, Grade A). A payments vendor's feature request says Apple Pay fails inside the Facebook and Instagram in-app browser on iOS while Stripe and Paddle checkouts reportedly work there (S26, Grade D, single source, no reply). A consultant blog recommends a visible "Open in browser" option and a no-wallet fallback (S27, Grade C). Instagram has no documented global setting to force links open externally (S28, Grade D). Practical conclusion: sell from email and the finish page, test one purchase on a real phone from an Instagram link, and keep card entry working without wallets.

### 1D. Left out, and why

- **Kajabi** (Basic $179/mo or $143 yearly; 2.9% + 30¢) and **Thinkific** ($109/mo monthly, $82 yearly, no free plan) and **Teachable** (Starter $39/mo plus 7.5% fee, or 0% on higher plans with Teachable Payments): course platforms priced for people selling courses. A $9 guide never covers $39 to $179 a month. Official pages: S29, S30, S31.
- **Sellfy** ($29/mo or $22 yearly, 0% fee, $10,000 yearly sales cap with a 2% overage fee): a flat plan that costs $264 to $348 a year, which is 29% to 77% of a $450 to $900 year. S32.
- **Memberful** ($49/mo + 4.9%): built for memberships, which the vision doc says not to lead with. S33.
- **ThriveCart:** I could not read its official pricing page (it returned a sign-in page). Secondary sources report $495 lifetime Standard and $47/mo monthly; unverified, and it is not a merchant of record. Skip.
- **Patreon and Substack:** official pages returned 403, and both are built around recurring subscriptions, which conflicts with "don't bill people who aren't using it."
- **Ko-fi and Buy Me a Coffee** stay in the table because Charles asked, but they are tip jars with a shop attached, and they charge 5% before processing.

---

## 2. The cost math at Charles's scale

### Formulas (so Charles can check)

- Per order: `fee = pct × price + fixed`. Example, Stripe at $9: `0.029 × 9 + 0.30 = $0.561`, which is 6.2% of the price. That is the sticker rate.
- Per year with `N` customers, one order each: `fees = N × fee`.
- Dispute cost: `disputes = 1% × N`; each costs `$15` (Stripe, Lemon Squeezy and Polar publish $15; Paddle says disputes are in its fee, so $0; for Gumroad, Payhip, Square, PayPal, Ko-fi I applied $15 as an *assumption*).
- Refunds: **assumed 5% of orders** (Charles gave no number; this is my placeholder). Fees on refunded orders are not returned on Stripe, Lemon Squeezy, Polar (assumed), Payhip (assumed) and Ko-fi (assumed). Gumroad returns its own 10% + 50¢ on a refunded sale and keeps the processing part (S14).
- Monthly or yearly plan fees are charged every month, with or without sales.
- **All-in effective fee rate** = `(order fees + plan fees + dispute fees + payout fees) ÷ gross sales charged`.
- **Keep per order** = `price × (1 − 5% refunded − 1% disputed) − all fees ÷ N`. It is what Charles keeps per order, after refunds and chargebacks.
- Polar adds payout costs: I assumed four withdrawals a year, so `4 × $2 + 4 × $0.25 + 0.25% of volume`.
- **Sales tax:** not added as a cost. A seller of record collects Idaho tax from buyers and remits it (a pass-through plus paperwork); MoR vendors build their cost into the fee above. See section 4.
- Gumroad is shown twice because its pages disagree: "help page" (12.9% + 80¢) and "headline" (10% + 50¢ only).
- Not modeled: international buyers (+1.5% on Stripe, Polar, Lemon Squeezy), PayPal buyers (+1.5% on Lemon Squeezy), currency conversion (+1% Stripe). Add them if buyers are outside the US.

### One-time purchase, sticker fee per order (no refunds, no plan fee)

| Option | $9 | $27 | $37 |
|---|---|---|---|
| Stripe Payment Link / MailerLite product | $0.56 (6.2%) | $1.08 (4.0%) | $1.37 (3.7%) |
| Stripe + Managed Payments | $0.88 (9.7%) | $2.03 (7.5%) | $2.67 (7.2%) |
| Square Payment Link (3.3% + 30¢) | $0.60 (6.6%) | $1.19 (4.4%) | $1.52 (4.1%) |
| PayPal (3.49% + 49¢, unverified) | $0.80 (8.9%) | $1.43 (5.3%) | $1.78 (4.8%) |
| Lemon Squeezy, Paddle, Polar Starter (5% + 50¢) | $0.95 (10.6%) | $1.85 (6.9%) | $2.35 (6.4%) |
| Payhip Free, Ko-fi Free (5% + Stripe) | $1.01 (11.2%) | $2.43 (9.0%) | $3.22 (8.7%) |
| Gumroad, headline only (10% + 50¢) | $1.40 (15.6%) | $3.20 (11.9%) | $4.20 (11.4%) |
| Gumroad, help page (12.9% + 80¢) | $1.96 (21.8%) | $4.28 (15.9%) | $5.57 (15.1%) |

### One-time purchase, all-in per year (includes 5% refunds, 1% disputes, plan fees)

Each cell: total fees for the year, all-in effective rate, and what Charles keeps per order. Columns are 50, 100 and 300 customers a year.

**$9 guide**

| Option | 50: fees / rate / keep | 100: fees / rate / keep | 300: fees / rate / keep |
|---|---|---|---|
| Stripe Payment Link | $36 / 7.9% / $7.75 | $71 / 7.9% / $7.75 | $213 / 7.9% / $7.75 |
| MailerLite product (Stripe) | $36 / 7.9% / $7.75 | $71 / 7.9% / $7.75 | $213 / 7.9% / $7.75 |
| Square Payment Link | $37 / 8.3% / $7.71 | $75 / 8.3% / $7.71 | $224 / 8.3% / $7.71 |
| PayPal (unverified) | $48 / 10.6% / $7.51 | $95 / 10.6% / $7.51 | $286 / 10.6% / $7.51 |
| Stripe + Managed Payments | $51 / 11.4% / $7.43 | $103 / 11.4% / $7.43 | $308 / 11.4% / $7.43 |
| Paddle (under $10: bespoke pricing, so unverified for $9) | $48 / 10.6% / $7.51 | $95 / 10.6% / $7.51 | $285 / 10.6% / $7.51 |
| Lemon Squeezy (under $10: custom pricing, so unverified for $9) | $55 / 12.2% / $7.36 | $110 / 12.2% / $7.36 | $330 / 12.2% / $7.36 |
| Payhip Free / Ko-fi Free | $58 / 12.9% / $7.30 | $116 / 12.9% / $7.30 | $348 / 12.9% / $7.30 |
| Polar Starter | $65 / 14.5% / $7.16 | $121 / 13.5% / $7.25 | $346 / 12.8% / $7.31 |
| Gumroad (headline) | $74 / 16.4% / $6.98 | $148 / 16.4% / $6.98 | $444 / 16.4% / $6.98 |
| Gumroad (help page) | $102 / 22.7% / $6.42 | $204 / 22.7% / $6.42 | $612 / 22.7% / $6.42 |
| Shopify Basic (yearly billing) | $384 / 85.2% / $0.79 | $419 / 46.6% / $4.27 | $561 / 20.8% / $6.59 |
| Podia Mover (yearly billing) | $562 / 124.9% / -$2.78 | $620 / 68.9% / $2.26 | $852 / 31.6% / $5.62 |
| SamCart Core | $984 / 218.6% / -$11.21 | $1,019 / 113.2% / -$1.73 | $1,161 / 43.0% / $4.59 |

**$27 guide**

| Option | 50: fees / rate / keep | 100: fees / rate / keep | 300: fees / rate / keep |
|---|---|---|---|
| Stripe Payment Link / MailerLite | $62 / 4.6% / $24.15 | $123 / 4.6% / $24.15 | $370 / 4.6% / $24.15 |
| Square Payment Link | $67 / 5.0% / $24.04 | $134 / 5.0% / $24.04 | $402 / 5.0% / $24.04 |
| PayPal (unverified) | $79 / 5.9% / $23.80 | $158 / 5.9% / $23.80 | $475 / 5.9% / $23.80 |
| Paddle | $92 / 6.9% / $23.53 | $185 / 6.9% / $23.53 | $555 / 6.9% / $23.53 |
| Lemon Squeezy | $100 / 7.4% / $23.38 | $200 / 7.4% / $23.38 | $600 / 7.4% / $23.38 |
| Stripe + Managed Payments | $109 / 8.1% / $23.20 | $218 / 8.1% / $23.20 | $653 / 8.1% / $23.20 |
| Polar Starter | $112 / 8.3% / $23.13 | $216 / 8.0% / $23.22 | $629 / 7.8% / $23.28 |
| Payhip Free / Ko-fi Free | $129 / 9.6% / $22.80 | $258 / 9.6% / $22.80 | $775 / 9.6% / $22.80 |
| Gumroad (headline) | $160 / 11.8% / $22.19 | $319 / 11.8% / $22.19 | $957 / 11.8% / $22.19 |
| Gumroad (help page) | $214 / 15.8% / $21.11 | $427 / 15.8% / $21.11 | $1,282 / 15.8% / $21.11 |
| Shopify Basic | $410 / 30.3% / $17.19 | $471 / 17.5% / $20.67 | $718 / 8.9% / $22.99 |
| Podia Mover | $633 / 46.9% / $12.72 | $762 / 28.2% / $17.76 | $1,279 / 15.8% / $21.12 |
| SamCart Core | $1,010 / 74.8% / $5.19 | $1,071 / 39.7% / $14.67 | $1,318 / 16.3% / $20.99 |

**$37 guide**

| Option | 50: fees / rate / keep | 100: fees / rate / keep | 300: fees / rate / keep |
|---|---|---|---|
| Stripe Payment Link / MailerLite | $76 / 4.1% / $33.26 | $152 / 4.1% / $33.26 | $457 / 4.1% / $33.26 |
| Square Payment Link | $84 / 4.5% / $33.11 | $167 / 4.5% / $33.11 | $501 / 4.5% / $33.11 |
| PayPal (unverified) | $97 / 5.2% / $32.85 | $193 / 5.2% / $32.85 | $579 / 5.2% / $32.85 |
| Paddle | $118 / 6.4% / $32.43 | $235 / 6.4% / $32.43 | $705 / 6.4% / $32.43 |
| Lemon Squeezy | $125 / 6.8% / $32.28 | $250 / 6.8% / $32.28 | $750 / 6.8% / $32.28 |
| Stripe + Managed Payments | $141 / 7.6% / $31.96 | $282 / 7.6% / $31.96 | $845 / 7.6% / $31.96 |
| Polar Starter | $139 / 7.5% / $32.01 | $268 / 7.2% / $32.10 | $787 / 7.1% / $32.16 |
| Payhip Free / Ko-fi Free | $169 / 9.1% / $31.41 | $337 / 9.1% / $31.41 | $1,012 / 9.1% / $31.41 |
| Gumroad (headline) | $207 / 11.2% / $30.64 | $414 / 11.2% / $30.64 | $1,242 / 11.2% / $30.64 |
| Gumroad (help page) | $276 / 14.9% / $29.27 | $551 / 14.9% / $29.27 | $1,654 / 14.9% / $29.27 |
| Shopify Basic | $424 / 22.9% / $26.30 | $500 / 13.5% / $29.78 | $805 / 7.3% / $32.10 |
| Podia Mover | $673 / 36.4% / $21.33 | $841 / 22.7% / $26.37 | $1,516 / 13.7% / $29.73 |
| SamCart Core | $1,024 / 55.4% / $14.30 | $1,100 / 29.7% / $23.78 | $1,405 / 12.7% / $30.10 |

What the tables show:

- Without a monthly plan, effective rates barely move with volume. With a plan, they fall with volume but never catch the plan-free options in this range. Even at 300 sales a year, SamCart Core at $9 (43%) is 5 times Stripe's rate (7.9%).
- **At 50 to 100 sales a year** (the vision doc's first-year guess is about $1,000 revenue and 50 to 100 payers), a platform fee of $79 a month is 95% of that revenue.
- **SamCart break-even** over Stripe: its card fee is the same, so it only pays if its features lift sales. Extra sales needed = `$948 ÷ keep per sale`: `948 ÷ 8.44 = 112` extra $9 sales, `948 ÷ 25.92 = 37` extra $27 sales, `948 ÷ 35.63 = 27` extra $37 sales a year. SamCart's own "3X average conversion lift" and "3.15% to 8.91%" are vendor marketing (Grade C), not evidence for a list your size.
- **When a flat-fee platform starts to make sense:** its fee is about 3 to 5% of revenue, which for SamCart Core ($948 a year) is roughly $19,000 to $32,000 of revenue a year. That is 19 to 32 times the vision doc's year-one guess.

### Dispute exposure at tiny volume

A 1% dispute rate means 0.5 disputes a year at 50 customers and 1 a year at 100, so in practice you will see zero or one, and a single one is lumpy. On Stripe, one lost dispute on a $9 sale costs the $9, the $15 dispute fee, and the 56¢ you already paid: $24.56, which is 5.5% of a 50-sale, $450 year. If you counter it yourself, Stripe charges another $15 that you get back only if you win (S1). I found no published win rates for small digital sellers, so I will not give one. Customers cannot dispute a payment you already refunded in full (S34), so quick refunds are the cheapest dispute prevention.

### Weekly group call, three ways

Assumptions: single calls: 6 calls per customer per year at $12 (6 orders). Pack: 2 four-call packs at $40 per customer per year (2 orders). Monthly: 4 paid months per customer per year at $29 (4 orders). Stripe Payment Link subscriptions add Stripe Billing at 0.7% of volume (assumed to apply to Payment Link subscriptions). Lemon Squeezy adds 0.5% for subscriptions. Same refund and dispute assumptions. "MoR" tools may not accept live calls (see section 4).

| Case | Option | 50 customers: fees / rate | 100 customers: fees / rate |
|---|---|---|---|
| **$12 per call** | Stripe Payment Link | $239 / 6.7% | $479 / 6.7% |
| | Square Payment Link | $254 / 7.0% | $508 / 7.0% |
| | Lemon Squeezy | $375 / 10.4% | $750 / 10.4% |
| | Polar Starter | $393 / 10.9% | $777 / 10.8% |
| | Payhip Free | $419 / 11.7% | $839 / 11.7% |
| | Gumroad (help page) | $724 / 20.1% | $1,448 / 20.1% |
| | Podia Mover | $923 / 25.6% | $1,343 / 18.6% |
| | SamCart Core | $1,187 / 33.0% | $1,427 / 19.8% |
| **4-call pack, $40** | Stripe Payment Link | $161 / 4.0% | $322 / 4.0% |
| | Square Payment Link | $177 / 4.4% | $354 / 4.4% |
| | Lemon Squeezy | $265 / 6.6% | $530 / 6.6% |
| | Polar Starter | $284 / 7.1% | $559 / 7.0% |
| | Payhip Free | $361 / 9.0% | $722 / 9.0% |
| | Gumroad (help page) | $588 / 14.7% | $1,177 / 14.7% |
| | Podia Mover | $865 / 21.6% | $1,226 / 15.3% |
| | SamCart Core | $1,109 / 27.7% | $1,270 / 15.9% |
| **$29 a month, pause** | Stripe Payment Link (Billing +0.7%) | $299 / 5.2% | $598 / 5.2% |
| | Square Payment Link | $281 / 4.9% | $563 / 4.9% |
| | Polar Starter | $444 / 7.6% | $878 / 7.6% |
| | Lemon Squeezy | $449 / 7.7% | $898 / 7.7% |
| | Payhip Free | $548 / 9.5% | $1,096 / 9.5% |
| | Gumroad (help page) | $904 / 15.6% | $1,808 / 15.6% |
| | Podia Mover | $1,052 / 18.1% | $1,600 / 13.8% |
| | SamCart Core | $1,206 / 20.8% | $1,464 / 12.6% |

Reading it: selling single $12 calls costs 6.7% on Stripe against 4.0% for a $40 pack, because the 30¢ is paid six times instead of twice per customer. A pack is cheaper for Charles and fits the no-auto-renew rule. If calls are sold as quantity on one Payment Link (the buyer picks 1 to 4 calls), the fixed fee is paid once per checkout.

A pay-up-front call that is then refunded because the call did not happen loses the fee (Stripe keeps its fee on refunds): about 65¢ on $12. Paying after the call (the lifecycle plan's "pay after with a link" option) avoids that loss entirely. A post-call Stripe invoice adds 0.4% (capped at $2) on top of card fees (S1).

### Free product through checkout ($0)

Don't route free products through a checkout. The free checklists already go out through MailerLite forms and stay free forever (ADR-020). I did not find any vendor page stating the fee on a $0 order. A fixed 50¢ would be 100% of nothing, so treat each vendor's $0 behavior as *unverified* and keep free delivery off the payment system. It also keeps the card form out of the free path, which is the honest line between free and paid.

---

## 3. Where people get soaked (with sources)

| Trap | Example from the sources | What it means here |
|---|---|---|
| **Fixed fee per transaction at a low price** | Stripe 30¢ is 3.3% of $9 by itself; Lemon Squeezy, Paddle and Polar 50¢ is 5.6% by itself (S1, S9, S12, S13) | Sticker rate at $9 runs 6.2% to 21.8% (table above) |
| **"Free" platforms with a high cut** | Gumroad 10% + 50¢ (plus processing per its help page); 30% on marketplace sales; Payhip Free 5% plus processing; Ko-fi 5% | Gumroad "Discover" brings a 30% fee on new buyers who find you there (S14, S15). Direct links and email links avoid it |
| **A monthly plan that costs more than the sales** | SamCart Core $948 a year; Podia Mover $504; Shopify Basic $348; Sellfy $264 | 95% to 105% of a $900 to $1,000 year |
| **Fee tiers triggered by volume** | Sellfy: sales above $10,000 a year need an upgrade or a 2% overage; Polar rates change by plan and changed for new orgs from 2026-05-27; Gumroad discounts only above $20,000 a month (S13, S15, S32) | Read the tier rule before volume arrives |
| **Subscription surcharges** | Stripe Billing +0.7%; Lemon Squeezy +0.5%; Buy Me a Coffee +0.5% (S1, S9, S23) | Only matters if you ever sell a monthly plan |
| **Tax tools** | Stripe Tax 0.5% per transaction where registered; SamCart "tax collection" 50 bps; Stripe Managed Payments 3.5% | Pay only after the CPA says you must collect |
| **Fraud tools** | Radar from $10/month or $0.05 per screened payment (S1) | Optional. Don't turn on a paid tool on your own |
| **Currency and international** | Stripe +1.5% international card, +1% conversion; Adaptive Pricing is always on for Payment Links so non-US buyers see their own currency (S1, S3) | A small share of buyers will cost more |
| **Instant payouts** | Stripe 1.5% (50¢ minimum); Gumroad 3% (S1, S16) | Use standard payouts (free) |
| **Chargeback fees** | $15 on Stripe, Lemon Squeezy, Polar and Teachable (S1, S10, S13, S31) | A $9 chargeback costs $24 |
| **Disputes escalating to the card networks** | Visa's monitoring program lists a "non-compliant" tier at a count of 5 and a ratio of 0.5%, "excessive" at 1.5% and 1,500 in the US. Stripe says such programs are "comparatively rare", that issuers count disputes even when you win, and that a business with under about 100 payments a month can see "one or two" disputes distort its rate (S35, S36) | At your volume the count thresholds protect you, but one dispute still moves your percentage. Refund fast and use a clear statement name |
| **Tax reporting (1099-K)** | The IRS says the threshold for payment apps and marketplaces is back to $20,000 and 200 transactions (FS-2025-08, via the One Big Beautiful Bill). **Payment card transactions have no minimum**, and states may set lower thresholds (S37, from a search summary of irs.gov; I did not open the PDF) | Expect a 1099-K from Stripe for card payments at any amount. Tax is due on income whether or not a form arrives. State thresholds: not verified; ask the CPA |
| **Account holds on new small accounts** | Gumroad: 1 to 3 week review, $100 payout minimum, 7-day hold; it may hold funds "in its sole discretion" and reserves 25% for 90 days above a 15% refund rate (S15, S16). Lemon Squeezy: 13-day hold, $50 minimum, twice-monthly payouts (S11). Stripe: first payout typically 7 to 14 days (S2) | A $9 product at a $100 minimum means 12 sales before the first Gumroad payout. Stripe has the shortest wait I could verify |
| **Lock-in** | MoR vendors own the buyer relationship. Stripe Managed Payments: buyers manage orders in Link, a data-deletion request cancels their subscriptions, and subscriptions can be created only through Checkout and Payment Links. Lemon Squeezy's migration to Stripe came with no steps or dates (S4, S5, S10). Gumroad terms bar circumventing the fee (S15) | With plain Stripe, customers and subscriptions are in your account and export as CSV. Customer lists in MailerLite are yours |
| **Refunds that don't return fees** | Stripe: original fees not returned (S3). Lemon Squeezy: platform fee kept (S11). Buy Me a Coffee: not returned. Gumroad returns its own fee (S14) | Each refunded $9 sale costs 56¢ on Stripe |

---

## 4. Sales tax and compliance for an Idaho sole proprietor

**This is not legal or tax advice.** The Idaho Tax Commission pages I found are broad guides, and the AI-generated summaries of them were thin. Where I say "likely" I mean my reading, not a ruling.

### What Idaho's official sources say

- **Digital goods.** The Tax Commission's sales and use tax basics guide lists "Digital books, videos, music, or games with a permanent right for the buyer to use" among taxable sales (S38, Grade A; the page does not name e-books or PDFs).
- **Software.** Idaho Code 63-3616 excludes "computer software that is delivered electronically" from tangible personal property. For digital music, books, videos and games, it treats a **permanent** right of use as taxable and says use "conditioned upon continued payment" is **not** a permanent right (S39, Grade A, read through a page summary).
- **Services.** The guide says tax applies to "every retail sale" of goods and lists taxable services such as admissions, meals and production labor. Group coaching is not on the list I could read (S38). I could not find an official page that says "coaching is not taxable." My confidence that a plain group call is not taxable is **medium to low**. Ask the CPA about "admissions" language, and whether a recording sold afterward is a taxable digital product.
- **Rate.** Sources I found say Idaho's state sales tax is 6% (B-grade). I did not read it on tax.idaho.gov. Verify.
- **Remote sellers.** Idaho requires out-of-state sellers to collect once their Idaho sales exceed **$100,000** in the current or prior year (S40, Grade A). That applies to sellers outside Idaho. **Charles is in Idaho**, so Idaho sales tax on taxable sales to Idaho buyers is a question from the first sale, not the $100,000 mark.
- **Seller's permit.** The Tax Commission's permits pages say who needs one but the details were behind a link I did not retrieve. The repo's checklist already marks "Do we need a seller's permit? (digital guides: ask CPA)."

### What a "merchant of record" really changes

- The MoR is the legal seller to the buyer. It calculates, collects and remits the tax (Stripe Managed Payments "files and remits payments to the relevant tax authorities"; Lemon Squeezy says it "takes on tax collection and calculation liability across all jurisdictions"; Gumroad says it handles "ALL your tax obligations" since 2025-01-01) (S4, S9, S14).
- It also handles buyer support and most disputes, and it can refund buyers itself (Stripe may refund within 60 days; Lemon Squeezy too).
- **What it does not change:** your income tax. You still report your payouts as income. Which form the vendor sends (1099-K, 1099-NEC or none) varies and I did not verify it for each vendor.
- Gumroad's help page says sellers who already file sales tax returns should report their Gumroad sales as "sales to other retailers for purposes of resale" and keep a reseller certificate (S14). In other words, an Idaho permit may still matter. Ask the CPA.
- The catch for Charles: Stripe's MoR **does not cover live coaching or professional services** ("If your service involves human intervention (such as live 1-1 coaching), it doesn't qualify"). For a group call, Charles would still be the seller of record, and Stripe tells you that you are "responsible for any indirect tax liability for the product" if it is found ineligible (S5). Whether group calls count as "human intervention" is not spelled out; the example given is one-to-one, so I would treat it as likely ineligible and ask Stripe.
- Whether Lemon Squeezy, Paddle or Polar accept live calls was not stated on the pages I read. Treat as unverified.

### Other states at our volume

Most states start collection at $100,000 in sales, and some also use a 200-transaction test. Vendor guides disagree on how many states still have the transaction test (one says 15, another says 16 states dropped it), and Illinois and Utah recently removed theirs (S41, Grade C, secondary, conflicting). At 50 to 300 sales a year spread across the country, Charles sits far below every threshold I saw, unless a single state supplies a large share of buyers. At $37 and 300 sales, total gross is $11,100. **What changes at what volume:** if any one state's buyers approach $100,000 (or 200 orders in a transaction-test state), registration is required there. A tax tool or an MoR is worth its fee then, not before.

### Card data and PCI

With a hosted checkout (Payment Links, Checkout, MailerLite on Stripe, any vendor-hosted page), the card number is typed into the processor's page and never touches Charles's site or email. Stripe's guide says Checkout and Elements host card inputs in an iframe from Stripe's domain, which puts a seller on the lightest validation form, **SAQ A**, completed annually in the Stripe Dashboard (S42, Grade A). That guide did not name Payment Links, though the Payment Links page says "PCI compliance handling: Supported" (S3). **The one rule: never handle card numbers yourself.** No card fields on the static site, no card numbers taken in Instagram DMs, email, text or by phone, and nothing typed into a Google Form.

### Questions to take to a CPA

1. Is a downloadable PDF checklist or guide a taxable "digital book" in Idaho, at what rate, and do I need a seller's permit before my first sale?
2. Is a weekly group coaching call over video taxable, including any "admission" language? Is a recorded replay taxable, and does it matter whether access is a one-time purchase or conditioned on a subscription?
3. If I use a merchant of record (Stripe Managed Payments, Gumroad), do I still need an Idaho permit or file zero returns? Does the "sale for resale" treatment apply?
4. Which form will I receive from Stripe and from any MoR (1099-K or other), under my SSN or EIN? Do any states I sell into have lower reporting thresholds?
5. Do I need an assumed business name filing before opening the bank and payment accounts, and how should my legal name and "Mr. Life Manager" appear on each?
6. How much should I set aside from each deposit (the checklist leaves "tax set-aside %" blank), and do I need quarterly estimates yet?
7. At what sales level, or from which state, should I begin collecting tax elsewhere?
8. Do prepaid call packs that expire, or credits, create any sales tax or consumer-protection issue?

---

## 5. The "AI age" question, answered honestly

**Can an LLM-assisted build replace SamCart-style tools with a few lines of code on top of Stripe? For the button and the thank-you page, yes. For everything after the first sale, only if you want to become a small software shop.**

**Genuinely easy (no code, or a few lines):**

- A Payment Link with a button on a page, a QR code, quantity or "choose what to pay," promo codes, and a redirect to a thank-you page that you write (S3, S43). Stripe even ships agent skills and a CLI aimed at AI-assisted setup (S5 page header).
- Receipts are automatic. Refunds are one click. Guest checkout is the default for one-time sales.
- Delivery with no server at all: a redirect to an unlisted page on your static site with the download link, or MailerLite's built-in product delivery (S8).

**Hard or risky (and where LLM code makes it worse, not better):**

| Need | Why it's hard on a static site | What it takes |
|---|---|---|
| **Webhooks** (react to payments) | GitHub Pages has no backend. You need a serverless function that **verifies Stripe's signature** and uses TLS; Stripe says you must verify signatures and allowlist its IPs (S42) | Hosting, secrets, retries, idempotency, monitoring, and someone to fix it when it breaks |
| **Delivering files securely** | A redirect URL on a static site can be shared by anyone who finds it. The session ID in the redirect proves nothing unless a server checks it with Stripe | Signed expiring links (what Lemon Squeezy and Gumroad host for you) or a small server |
| **License or access control** | No accounts, no server | Not worth building at this scale. Free-first makes a shared link a small risk, but it is a real one |
| **Subscriptions and pauses** | Stripe's portal does cancel and pause, but pause starts at the end of the billing period and is only in the redesigned portal (S44). Failed-payment retries are features of Stripe Billing | Configure the portal. The auto-renew conflict with Charles's rule is the larger problem (section 6) |
| **Refunds, receipts, support** | Stripe handles refunds and receipts. Replies and judgment are yours | Charles, or the bot with a written policy |
| **Tax** | Code can't resolve a legal question | CPA first (section 4) |
| **Security and compliance** | Every line of generated code that touches payments is yours to review and patch | A reason to prefer hosted pages with zero custom code |

**Where a vendor earns its fee:** a merchant of record earns 3.5% to 5% + 50¢ when you sell across many states or countries and do not want to register and file in each. A course or membership platform earns its fee when you need gated lessons, member areas, drip content and community, and don't want to build them. A funnel tool like SamCart earns its fee when order bumps, upsells and cart recovery are the thing you are optimizing at volume. None of those describes a $9 checklist sold 50 to 100 times a year.

**"Agentic commerce."** It exists but is not relevant to you now. Stripe offers Shared Payment Tokens (priced at $0.15 per token issued) and an Agentic Commerce Suite for letting AI agents buy from a catalog (S1, S45). OpenAI scaled back its in-chat Instant Checkout in March 2026 and moved toward product discovery, with merchants completing purchases on their own checkout (S46, Grade B, secondary). For a small seller selling guides to people who already joined your list, there is no reader benefit. Don't bother.

**Verdict on SamCart.** Not needed. Its actual price today is **$79 a month (Core) or $199 a month (Pro)**, 7-day free trial, with the same 2.9% + 30¢ card fee as direct Stripe and a tax-collection fee of 50 or 35 basis points whose basis the page doesn't explain (S18). It would be worth it **only if all of these are true:** revenue is above roughly $20,000 to $30,000 a year (so the fee falls to 3 to 5%), you actually use order bumps, one-click upsells and cart recovery, you have several products to bundle, and you do not want to run a payments setup yourself. None applies at 50 to 100 sales. Reconsider when a checkout *experiment* (not a tax or delivery problem) is the thing holding back revenue.

---

## 6. Fit with our rules

| Rule | Options that fit | Options that don't (or only with effort) |
|---|---|---|
| **A single call or a pack, no automatic renewal** | Stripe Payment Link (one-time, quantity picker), MailerLite one-time product (a 4-call pack as a one-time product), Square, PayPal, Payhip, Gumroad one-time | Anything where the subscription is the default (Patreon, Substack, Memberful, most membership tools) |
| **One-click refunds** | Stripe Dashboard (one click, bulk full refunds); Lemon Squeezy; Gumroad (but Gumroad decides disputes "in its sole discretion") | Stripe Managed Payments lets Link support issue refunds without you after 48 hours of silence; that is not a problem for the rule, but you lose control of timing |
| **Free first call** | A booking page with no payment (MailerLite lists bookings on its pricing page; unverified depth), or a 100%-off promotion code on a Stripe link (promo codes supported; whether a $0 Checkout skips card entry is unverified) | Routing a free call through checkout is not needed. Don't collect card details for a free call |
| **Collect only what we need** | Stripe guest checkout: name, email, card. Turn off address and phone fields. MailerLite's native checkout can collect "additional buyer information" and a marketing opt-in box; keep both off unless needed (S8) | MoR checkouts require more buyer data (tax location). Stripe Managed Payments creates a Link account prompt |
| **Forces subscriptions or lock-in** | Memberful, Patreon, Substack; Stripe Managed Payments for buyers who create a Link account; Podia and Kajabi (plan limits and stores on their platform) | |
| **Works from a link in email or a QR-code page with no backend** | Stripe Payment Links (QR code built in), MailerLite product link, Lemon Squeezy, Gumroad, Payhip, Polar | Anything needing an embedded script and a server |
| **"If they're not using it, they don't pay for it"** | One-time sales, packs, or pay-after-the-call. Stripe's portal allows pause, and Stripe can send renewal reminders; pause is a mitigation, not a fix | A monthly plan bills people who forget about it. If you ever run one, require a reminder before every renewal and make cancel one click |
| **No one under 18** | State it on the checkout page and in the terms. Card payments lean adult but are not proof of age | |

The lifecycle plan's $19 "paid start call, charged only if it happened" maps to **pay after the call with a Stripe link** (no fee loss) or **pay up front and refund** (about 65¢ lost per refund at $12).

---

## 7. Three recommended setups

**Ranking: A first, then B only if the CPA says to, then C.** I would pick A this month and cut everything else.

### A. Cheapest and simplest: Stripe, with MailerLite delivering the file

**What it is.** One Stripe account. The one-time guide is sold as a **MailerLite digital product** (MailerLite hosts the PDF, sends the confirmation, and tags the buyer into a group). The weekly call pack is sold as a **Stripe Payment Link**. Links go on the finish page and in emails, not in the Instagram bio.

**Steps, in order.**
1. Get the EIN (free, IRS, online). Then file the Idaho assumed business name (see section 8). Then open the business bank account.
2. Open Stripe as an individual/sole proprietor with the EIN, bank account, and public business name "Mr. Life Manager." Set the statement descriptor (for example "MR LIFE MANAGER") and a support email. Turn on two-factor sign-in.
3. Connect Stripe to MailerLite (Integrations, Stripe). Create the one-time digital product, upload the PDF, set the price.
4. Create the call pack as a Stripe Payment Link with quantity if wanted. Redirect to a thank-you page that says how to join.
5. Test in Stripe's sandbox (no money). Then one live $1 purchase and refund (section 8).
6. Put the links on the finish page and email after the CPA answers the tax question.

**One-time effort.** About half a day once the bank account exists; the EIN and bank account add days of waiting.

**Monthly cost.** $0 platform fee at 0, 50 or 100 customers (if Charles's MailerLite plan already covers one product, which the free plan does; five products need Comfort from $12). Fees only on sales: about $36 and $71 a year on $9 guides (50 and 100 customers, including refunds and disputes), $62 and $123 on $27, $76 and $152 on $37.

**What could go wrong.** A new account's first payout can take 7 to 14 days. Idaho tax might apply and you'd have to register. MailerLite's native checkout page behavior on phones (wallets, load speed, descriptor) was not documented; test it on a real phone. The product limit on the free plan is one. No Stripe MoR protection for tax.

**Switching away.** Customers, receipts and subscriptions live in your Stripe account and export as CSV. Change the link on the finish page to a new tool and keep Stripe for refunds. Your list stays in MailerLite.

### B. Take tax compliance off Charles's plate

**What it is.** Same Stripe account. Turn on **Stripe Managed Payments** for the guide Payment Links only (6.4% + 30¢). Calls stay on ordinary Stripe. Ranked alternatives, only if Managed Payments doesn't accept the account: Polar Starter (5% + 50¢, MoR, aimed at software sellers, payout fees, services unverified), then Gumroad (MoR, hosted storefront, about 21.8% on $9).

**Steps.**
1. Do everything in A first (same accounts).
2. Ask the CPA question 1 and 3 from section 4. Do this step only if the CPA says the guides are taxable and you don't want to collect and file.
3. In Stripe, request Managed Payments (eligibility review, US supported). Set the tax code for each product (`txcd_10302000` for permanent digital books is one of the listed codes; confirm the right one).
4. Create Managed Payments Payment Links for guides. Test with a $1 product.
5. Check what the buyer sees on a test charge: `LINK.COM* ...` and "Sold through Link."

**One-time effort.** Another hour or two after A, plus the eligibility wait (unknown).

**Monthly cost.** $0 platform fee at 0, 50 or 100 customers. Fees on guides: about $51 and $103 a year on $9, $109 and $218 on $27, $141 and $282 on $37.

**What could go wrong.** Stripe may decline the account (eligibility review). The buyer sees Link's name on the card statement, which can raise "I don't recognize this" disputes. Custom domains don't work. Calls and one-to-one coaching are excluded. At $9 the extra 3.5% on top of the fixed fee is 9.7% sticker, and only pays for itself if you'd otherwise hire help with tax.

**Switching away.** Turn Managed Payments off per product and use ordinary Payment Links. Subscriptions sold through Managed Payments can't move easily (unverified), so don't sell any under it.

### C. The one to grow into if the weekly call and a membership take off

**What it is.** Stripe Payment Links and Billing with the customer portal for any recurring plan, MailerLite for email and automation, and one hosted bookings or scheduling tool. Only move to a membership platform (Podia Shaker at $84 a month yearly, Memberful $49 + 4.9%, or Kajabi from $143 yearly) when gated content and member areas are what members ask for and revenue is high enough that the fee is 3 to 5% of it.

**Steps.**
1. Keep A running.
2. Sell packs first (no auto-renew). Add a subscription only after packs show demand.
3. If a subscription is added, turn on the customer portal with cancel and pause, turn on renewal reminders, and add a use-it-or-pause email before each renewal.
4. Write down a trigger for a bigger tool (for example monthly revenue above $2,000 and a repeatable need Stripe can't meet).

**One-time effort.** A day to configure Billing and the portal.

**Monthly cost.** At 0 customers, $0. Per-sale fees on a $29 monthly plan at 50 and 100 customers (4 paid months each): about $299 and $598 a year on Stripe, or $25 and $50 a month. A $84 a month membership platform has to replace that and more.

**What could go wrong.** The gym-membership problem the vision doc rules out. Stripe pause only starts at the end of the billing period, and the redesigned portal is required for it. Failed-payment emails and renewals are yours to monitor.

**Switching away.** Export customers; migrating subscriptions between processors requires moving saved cards, which I did not research and which normally needs help from both processors. Easier: stop selling the subscription and move the call back to packs.

**What I'd cut.** SamCart, Kajabi, Teachable, Thinkific, Podia, Shopify, Sellfy, Memberful, Patreon, Substack, ThriveCart (all section 1D). Gumroad at $9. Lemon Squeezy for new setups (unclear future, $9 is under its "contact us" line). A subscription at launch. Paid fraud and tax tools until a real need shows. The Instagram link-in-bio checkout.

---

## 8. "Before you pick" checklist (plain words)

**Open accounts in this order.**
1. **EIN** from the IRS (free). The repo's checklist says it is in progress.
2. **Idaho assumed business name** for "Mr. Life Manager" if you sell under that name. Idaho's Secretary of State FAQ quotes Idaho Code 53-504: anyone doing business in Idaho under an assumed name must file a certificate before starting (S47). It is a notice filing and does not create a company or protect liability.
3. **Business bank account** in your name (sole proprietor, doing business as Mr. Life Manager). Ask the bank what it needs; many want the EIN and the assumed-name certificate (not verified for your bank).
4. **Stripe**, using the EIN and the business account, public business name "Mr. Life Manager."
5. Connect Stripe to MailerLite. Build the product.
6. Test, then publish links. Don't open an Instagram account for checkout; the paid link lives on the finish page and in email.

**What EIN and the bank account are for.** The EIN keeps your Social Security number off forms and gives the processor a business identity. The bank account keeps business money separate from personal money (the repo's "money wall"), receives Stripe's payouts, and makes tax set-aside simple. Stripe needs a bank account to pay out.

**Names, in one sentence.** Legal name: Charles Warloe. Brand: Mr. Life Manager (assumed business name). Tax forms such as 1099-K go out under your legal name and tax ID; the brand name appears on the checkout page, receipts and card statement. Check how Stripe's tax settings print the two on your forms (not verified).

**Test before you tell anyone.**
- Do the full flow in Stripe's sandbox first. It costs nothing.
- Then one live $1 purchase and refund. Gumroad warns that buying your own product on a live account can look like fraud to processors (S16); I did not find Stripe's rule on this, so keep it to one small purchase, refunded the same day, and ideally by someone else with their own consent and card.
- Check on a phone, from a real email and from an Instagram link: does the wallet button appear, does the page load fast, does the thank-you page open the file, does the receipt arrive, and what name is on the card statement after a day or two?
- Click the refund. Confirm the buyer sees it and the order shows refunded.
- Confirm the unsubscribe path in MailerLite and that the buyer is only marketed to if they ticked the box.

**Say these things on the checkout page** (generic wording; the product and price are Charles's decision):

> **What you get:** [name of the guide or call pack], [format and length], and [what it adds beyond the free checklist].
> **The free checklists stay free.** You do not need to buy this to use them. [One plain sentence on what the paid thing does that the free one doesn't.]
> **One payment, no subscription.** We won't charge you again.
> **Refund:** [Email address] within [N] days and we refund you in full, no questions asked. *(One sentence; Charles sets N.)*
> **Who we are:** Sold by Charles Warloe, doing business as Mr. Life Manager, Idaho, USA. Questions: [email]. For adults 18 and over.
> **On your card statement:** it will read [MR LIFE MANAGER].
> **For a call pack:** Live weekly group call on [day and time] by [tool]. Pack covers [4] calls and is good until [date]. If a call is cancelled we credit or refund it.

**The receipt or delivery email must carry:** what was bought and the amount, the date, the download or join link, the refund sentence and the contact email, and nothing else (no upsell). Stripe's automatic receipt shows your business name and support details; adding your own sentences to it is limited (not verified), so put the refund promise on the checkout page and in your own MailerLite delivery email.

### The "don't resell the free thing" risk

If the paid product repackages what the free checklist already gives, you create a **"product not as described"** dispute and refund exposure: the buyer finds the free version, feels misled, asks for a refund, or disputes the charge. Facts about how the systems treat this:

- Stripe says to "clearly describe the items being sold," to "implement a flexible refund policy," and to reevaluate products with higher dispute rates because "it's possible the items could be defective." It also says to show your full refund policy before payment and that an issuer may reject a link-only checkbox as weak evidence (S34).
- A $9 dispute costs $24 on Stripe, and you can't dispute a payment you already refunded in full. So the cheapest protection is an easy, fast refund.
- Marketplaces and MoR vendors can act without you: Lemon Squeezy may refund within 60 days even if you say no refunds; Stripe Managed Payments may refund within 60 days and after 48 hours of silence; Gumroad decides disputes in its sole discretion, you reimburse it, a refund rate over 15% triggers a 25% reserve for 90 days, and over 25% can end the account (S10, S15, S5).
- Visa and Mastercard monitoring programs count disputes whatever the outcome; at your volume the count thresholds (for example 5 in a month for Visa's lowest tier) keep you well clear, but a single bad month can't be won by arguing "it was free on the site." I found no published win rates for small digital sellers.
- **Therefore:** the paid thing must be clearly more than the free checklist and say so, refunds should be simple and prompt, and the statement name should be one the buyer recognizes.

---

## Sources

All retrieved 2026-11-12. Grades: **A** official vendor or government page; **B** independent comparison or reputable press; **C** vendor marketing or affiliate blog; **D** forum or anecdote. Where a fetch tool returned a summary rather than the raw page, I say so. I checked the key numbers for Stripe, Polar, Gumroad, Lemon Squeezy, MailerLite, SamCart and Podia against the raw page HTML as well.

| # | Source | Grade | Used for | Stale risk |
|---|---|---|---|---|
| S1 | Stripe pricing, https://stripe.com/pricing | A | Card rates, Billing 0.7%, disputes, instant payout, Managed Payments 3.5%, Shared Payment Tokens $0.15 | Medium |
| S2 | Stripe payouts, https://docs.stripe.com/payouts | A | First payout 7 to 14 days, US settlement, minimum payout | Low |
| S3 | Stripe Payment Links, https://docs.stripe.com/payment-links, plus /payment-links/create and /payment-links/post-payment | A | Features, guest checkout, refunds, redirect, QR, quantity, subscriptions | Low |
| S4 | Stripe Managed Payments, https://docs.stripe.com/payments/managed-payments and /how-it-works | A | MoR scope, refunds, disputes, Link, statement descriptor | High (new product) |
| S5 | Stripe Managed Payments eligibility, https://docs.stripe.com/payments/managed-payments/eligibility | A | Excludes live coaching and professional services; supported countries | High |
| S6 | MailerLite sell digital products, https://www.mailerlite.com/features/sell-digital-products | A | Stripe only, 0% commission, plan limits | Medium |
| S7 | MailerLite pricing, https://www.mailerlite.com/pricing | A | Free 250 subscribers; Free, Comfort from $12, Power from $25; plan names changed over time | High |
| S8 | MailerLite help, https://www.mailerlite.com/help/create-a-digital-product and blog https://www.mailerlite.com/blog/sell-digital-products-and-subscriptions-through-mailerlite | A | One-time only, delivery, refunds via Stripe | Medium |
| S9 | Lemon Squeezy pricing, https://www.lemonsqueezy.com/pricing | A | 5% + 50¢, MoR | High |
| S10 | Lemon Squeezy docs, https://docs.lemonsqueezy.com/help/getting-started/fees and /help/payments/refunds-chargebacks (read via search results and a page summary) | A | Surcharges, refund fee kept, $15 dispute | Medium |
| S11 | Lemon Squeezy getting paid, https://docs.lemonsqueezy.com/help/getting-started/getting-paid | A | 13-day hold, $50 minimum, 1st and 15th | Medium |
| S12 | Paddle pricing, https://www.paddle.com/pricing | A | 5% + 50¢, under $10 bespoke pricing, MoR | Medium |
| S13 | Polar pricing, https://polar.sh/resources/pricing | A | Plans, payout fees, $15 disputes, 2026-05-27 change | High |
| S14 | Gumroad fees help, https://gumroad.com/help/article/66-gumroads-fees | A | 10% + 50¢ plus processing, refund treatment, $20,000 discount | Medium |
| S15 | Gumroad terms, https://gumroad.com/terms | A | Disputes, reserve, holds, fee circumvention | Medium |
| S16 | Gumroad payouts help, https://gumroad.com/help/article/13-getting-paid; Gumroad pricing, https://gumroad.com/pricing | A | $100 minimum, 7-day hold, review, 3% instant, MoR, headline fee. The two Gumroad pages disagree on whether processing is included | High |
| S17 | Payhip pricing, https://payhip.com/pricing (page summary; direct fetch returned 403) | A | Plans, tax statement | Medium |
| S18 | SamCart pricing, https://www.samcart.com/pricing | A | $79, $199, SamPay, tax collection 50 and 35 bps, trial. FAQ answers not readable | Medium |
| S19 | Podia pricing, https://www.podia.com/pricing | A | Plans, 5% on Mover, processor fees | Medium |
| S20 | PayPal fees (official page returned 403). Secondary: https://checkoutpage.com/blog/paypal-fees and similar | B/C | 3.49% + 49¢; micropayments 4.99% + 9¢ | **Unverified** |
| S21 | Square Payment Links, https://squareup.com/us/en/online-store/online-checkout (rate-limited; read via search snippet) and help center https://square.com/help/us/en/article/5068 | A (partly unverified) | 3.3% + 30¢ for new customers | **Unverified** |
| S22 | Ko-fi help, https://help.ko-fi.com/hc/en-us/articles/360002506494 (403; read via search snippet) | A (partly unverified) | 5% on shop sales; Gold price conflicts across sources | **Unverified** |
| S23 | Buy Me a Coffee help, https://help.buymeacoffee.com/en/articles/8105744 (via search snippet) | A (partly unverified) | 5% + processing + 0.5% payout | **Unverified** |
| S24 | Shopify pricing, https://www.shopify.com/pricing | A | Basic $29 or $39, 2.9% + 30¢ | Medium |
| S25 | Stripe Express Checkout Element, https://docs.stripe.com/elements/express-checkout-element | A | In-app webview support table | Medium |
| S26 | Dodo Payments feature request, https://dodopayments.featurebase.app/p/apple-pay-support-in-meta-facebook-instagram-in-app-browser | D | Apple Pay fails in Meta in-app browser on iOS for that vendor; competitors reportedly work | Unknown date |
| S27 | AlphonsoLabs in-app browser checklist, https://www.alphonsolabs.com/in-app-browser-checkout-test-checklist/ | C (consultant, sponsored placements) | "Open in browser" fallback advice only | Unknown |
| S28 | Instagram external-browser search results (no official Instagram page found) | D | No documented global setting | Unknown |
| S29 | Kajabi pricing, https://www.kajabi.com/pricing | A | $179, $143, $249 | Medium |
| S30 | Thinkific pricing, https://www.thinkific.com/pricing/ | A | $109 and $82 | Medium |
| S31 | Teachable pricing, https://www.teachable.com/pricing | A | $39, 7.5%, $15 chargeback | Medium |
| S32 | Sellfy pricing, https://sellfy.com/pricing/ | A | $29, $22, $10,000 cap, 2% overage | Medium |
| S33 | Memberful pricing, https://memberful.com/pricing/ | A (page summary) | $49 + 4.9% | Medium |
| S34 | Stripe best practices, https://docs.stripe.com/disputes/prevention/best-practices | A | Fully refunded payments can't be disputed; descriptor, refund policy, unacceptable products | Low |
| S35 | Stripe card monitoring programs, https://docs.stripe.com/disputes/monitoring-programs | A | VAMP thresholds; counted whatever the outcome | Medium |
| S36 | Stripe refunds, https://docs.stripe.com/refunds; statement descriptors, https://docs.stripe.com/get-started/account/statement-descriptors | A | Fees not returned; 5 to 22 characters; reflects your assumed business name | Low |
| S37 | IRS Form 1099-K FAQs and fact sheet FS-2025-08 (https://www.irs.gov/pub/taxpros/fs-2025-08.pdf), read through a search summary; the PDF was not opened | A (via summary) | $20,000 and 200 transactions; card payments no minimum; lower state thresholds | Medium |
| S38 | Idaho State Tax Commission basics guide, https://tax.idaho.gov/taxes/sales-use/online-guide/ | A | Digital books with permanent right taxable; services list | Medium |
| S39 | Idaho Code 63-3616, https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3616/ | A | Electronically delivered software excluded; permanent right of use | Low |
| S40 | Idaho online sellers guide, https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/ | A | $100,000 remote seller threshold | Low |
| S41 | Economic nexus guides (Kintsugi, Taxually, Avalara via search), e.g. https://trykintsugi.com/sales-tax-guides/usa/economic-nexus | C | $100,000 pattern; transaction tests changing; sources disagree | High; verify with each state |
| S42 | Stripe integration security guide, https://docs.stripe.com/security/guide; PCI guide, https://stripe.com/guides/pci-compliance | A | SAQ A, annual attestation, webhook signatures | Low |
| S43 | Stripe Payment Links post-payment and guest customers, https://docs.stripe.com/payments/checkout/guest-customers | A | Guest customer, redirect, receipts | Low |
| S44 | Stripe customer portal configuration, https://docs.stripe.com/customer-management/configure-portal | A | Cancel, pause, promo codes | Low |
| S45 | Stripe agentic commerce, https://docs.stripe.com/agentic-commerce | A | What exists; fees not given except SPT $0.15 on S1 | High |
| S46 | Search results on OpenAI Instant Checkout scale-back (e.g. https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/ and others) | B/C | March 2026 scale-back, single-source details | High |
| S47 | Idaho Secretary of State assumed business name FAQ, https://sos.idaho.gov/CORP/abn_faq.html (quoted in search results; page not opened directly) | A (via snippet) | Idaho Code 53-504 filing duty | Low; confirm citation, since other sites cite a different section |

**Numbers most likely to be stale:** Polar rates (changed 2026-05-27), Lemon Squeezy and everything about its future, Stripe Managed Payments availability and fee, Gumroad's fee (its own pages disagree), MailerLite plan names and limits (the pricing page shows Free, Comfort, Power while older help pages say Growing Business and Advanced), SamCart, Podia and Teachable prices, the 1099-K rule, Idaho tax guidance (check the live Tax Commission pages), state nexus counts.

**Not checked:** PayPal, Square, Ko-fi and Buy Me a Coffee official fee pages (blocked or rate-limited), Patreon and Substack official pages (403), ThriveCart official pricing, Idaho's current state sales tax rate on an official page, Idaho's state-level 1099-K rule, Paddle's refund, payout and services terms, and vendor page-speed numbers.
