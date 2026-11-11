# Lifecycle research 02: from the first win to the follow-up emails to a first purchase

**Status:** Evidence only. No plan, no email copy, no recommendations. For the
lifecycle-strategist.
**Researched:** 2026-10-26. Every web source below was checked on that date
unless noted.
**Read alongside:** [ADR-014](../../../planning/decisions.md#adr-014--completion-is-what-converts),
[ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email) and
[ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
(both **under review**, cited here as the current state, not as settled),
[ADR-020](../../../planning/decisions.md#adr-020--win-before-wallet-retire-the-39-flagship),
[ADR-021](../../../planning/decisions.md#adr-021--when-the-reader-cant-act-yet-ask-for-a-when),
the five sequences in [`products/landing/emails/`](../../../products/landing/emails/),
and the [product ladder](../../business/product-ladder.md).

**Labels used throughout.** *Evidence* is what a source reports. *Inference* is
our reasoning from it. *Opinion* is a practitioner's claim without data.
Confidence is **High** (peer-reviewed or large primary data with stated
methods), **Medium** (credible primary data with limits, or consistent
secondary reports), or **Low** (vendor claims, single anecdotes, unverified).

---

## 1. Question

What is known about the stretch between a reader's first free win and their
first purchase? Specifically: how follow-up email sequences after a free
completion should be shaped (length, spacing, what each asks, replies, one
clear action, when to stop), with open rates treated as unreliable since Apple
Mail Privacy Protection; whether sequences tailored to the reason someone
arrived (first night, guests, whole house, a room that became storage, a work
desk) beat one generic sequence; what drives a first paid purchase of a $9–19
digital guide, including timing relative to the win, low-ticket pricing,
guarantees, pay-what-you-want, and realistic free-to-paid conversion rates for
small creators; whether action-gated offers or completion-based pricing have
any evidence behind them; and what comparable brands (FlyLady, KC Davis,
Clutterbug, Clean My Space, Dana K. White, budgeting and life-skills creators)
actually do.

**Where we start from (repo, not research).** Four live sequences and one
drafted one all follow the same shape: email 1 immediately (The Week plus one
named action), email 2 on day 3 (a smaller action), email 3 on day 7 (one
question answerable in a word), then stop. Nobody is branched on opens or
clicks; a reply or a purchase takes someone out. None of the sequences
contains a paid offer: the $9–19 step is parked under ADR-020
([MAILERLITE-SETUP.md](../../../products/landing/emails/MAILERLITE-SETUP.md)).
The ladder's health check targets **2–5% free-to-paid within 90 days**
([product-ladder.md](../../business/product-ladder.md#ladder-health-checks)).

---

## 2. Findings

### 2a. What email metrics can be trusted

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| Apple Mail Privacy Protection preloads images through a proxy, so an "open" can be recorded with no human reading. Klaviyo's own help center tells customers open rates "will be inflated." | [Klaviyo help: benchmarks](https://help.klaviyo.com/hc/en-us/articles/360050110072-Getting-started-with-benchmarks-reports); [MarTech on iOS 15](https://martech.org/study-finds-ios-15-is-inflating-email-open-rates/) | High that opens are inflated | **Yes, fully.** ADR-016 already refuses to branch on opens. |
| The size of the inflation varies widely by source: SparkPost reported about 12 percentage points of unique-open lift for most senders; SendGrid reported 32% of Apple-domain opens as MPP-influenced; one vendor puts "real" open rates near half of reported ones. No peer-reviewed estimate was found. | [Boomerang 2026 (vendor)](https://www.getboomerang.ai/glossaries/are-email-open-rates-reliable-2026); [MediaPost](https://www.mediapost.com/publications/article/369114/upsetting-the-apple-cart-tips-on-how-to-cope-with.html) | Medium on direction, Low on any single number | Yes. Any benchmark that quotes opens (including the "welcome emails get 50–84% opens" figures below) can't be compared with ours. |
| Vendors and deliverability consultants converge on clicks, replies and purchases as the usable signals. | Same as above; [Suped on replies](https://www.suped.com/knowledge/email-deliverability/sender-reputation/do-email-replies-improve-deliverability-and-sender-reputation) | Medium | Yes, and we have a stronger one: the `/finished-*.html` pages and Umami events ([operations.md](../../../planning/operations.md)) measure completion directly, which no email metric does. |

### 2b. Post-win sequences: length, spacing, asks, replies, one action, stopping

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Welcome and triggered emails outperform regular newsletters** on clicks as well as opens. GetResponse reports click-through of 5.02% for triggered emails vs 3.84% for newsletters; its welcome-email click figure is reported variously as 16.6% and 25.9% in different write-ups. | [GetResponse benchmarks](https://www.getresponse.com/resources/reports/email-marketing-benchmarks); [Stripo report on welcome emails](https://research.stripo.email/welcome-email-open-rates); [MediaPost](https://www.mediapost.com/publications/article/332106/welcome-emails-produce-high-open-rates-worldwide.html) | Medium on direction, Low on exact numbers (vendor data, methods not published) | **Partly.** The direction (the first days after signup are the highest-attention window) is plausible for us. The numbers are mostly e-commerce and newsletter senders. |
| **No credible per-position data exists for how a sequence performs email by email.** The most cited table (orders peaking at email 3 of 5) is a blog's own "synthesis" with no traceable dataset. | [Branvas](https://branvas.com/blogs/news/welcome-email-sequence-benchmarks) (states position-level data "varies by brand size and vertical") | Low | No. See "Don't rely on." |
| **More contacts help, then flatten.** In survey research (the closest field with randomized studies of repeated email asks), reminders raised web-panel response from 49.5% to 65.6% across 38 studies (N = 246,040). A 2020 review summarizes gains up to about three or four reminders, with spamming and fatigue concerns beyond that. | Online-panel meta-analysis ([*Field Methods*, DOI 10.1177/1525822X241286341](https://doi.org/10.1177/1525822X241286341); figures from its abstract as summarized in search, full text not retrieved); review in [Menon & Muraleedharan 2020, *Gen Psychiatry*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7398086/); [Cook, Heath & Thompson 2000](https://www.intotheminds.com/blog/en/online-survey-reminders/) ranks number of contacts first of 15 factors (secondary) | Medium–High that a few reminders help; Medium on "three to four" as a ceiling | **Reasonably.** A survey invite and a "do this small thing" email are both asks for a small action. Our three emails sit inside that range. |
| **One well-timed, specific reminder does most of the work; extra late reminders add little.** | [Karlan et al. 2016, *Management Science*](https://www.nber.org/papers/w16205) (already in [deferred-win.md](../deferred-win.md)) | High | Yes. Supports a short sequence with one concrete action per email. |
| **Academic evidence on marketing-email frequency is thin.** Kumar, Zhang & Luo (2014, *JMR*) model opt-in and opt-out timing and find "marketing intensity" affects how long people stay subscribed, but the public summaries don't give the direction or size usable for a sequence. Practitioner frequency tests are small, single-company and vendor-written. | [Kumar et al. 2014 (dissertation summary)](https://scholarworks.gsu.edu/marketing_diss/32); [Search Engine Land experiment](https://searchengineland.com/extreme-email-experiment-how-much-is-too-much-60755) | Low for any rule about spacing | Inference: our 0/3/7-day spacing is a reasonable choice, not an evidence-backed optimum. Nothing found argues for longer. |
| **Even non-informative personalization raises engagement and cuts unsubscribes.** Randomized field experiments with millions of recipients: adding the recipient's name to the subject raised opens 9.05% to 10.80%, sales leads 0.39% to 0.51%, and cut unsubscribes 1.2% to 1.0%. The authors' mechanism is that it increases effort spent processing the rest of the message. | [Sahni, Wheeler & Chintagunta 2018, *Marketing Science*](https://pubsonline.informs.org/doi/epdf/10.1287/mksc.2017.1066) | High (pre-MPP data, so opens were real) | **Partly.** We don't collect names on the form, and a name in the subject is an old marketing trick. The more useful transfer is the mechanism: something that signals "this is about you" increases attention. Entry-route tailoring (2c) is the honest version. |
| **Plain, simple emails beat designed ones** in HubSpot's own A/B tests: every test was won by the simpler email, and "even a single image reduced the click rate." Other senders have found the opposite for newsletters. | [HubSpot](https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data); [Campaign Creators counter-test](https://www.campaigncreators.com/blog/html-vs-plain-text-emails) | Medium–Low (single-company tests, results vary) | Yes in spirit. Our emails are already plain, personal and signed by Charles. |
| **One call to action tends to beat several**, but the famous "+371% clicks" figure has no traceable source. The best documented case is a Whirlpool test: a single CTA raised clicks 42%. | [Econsultancy case studies](https://econsultancy.com/three-case-studies-to-help-improve-your-email-marketing-conversion-rates/); [Campaign Monitor (repeats 371% unsourced)](https://campaignmonitor.com/resources/knowledge-base/do-ctas-help-to-improve-email-response-rates) | Medium on direction (one case), Low on size | Yes, but our reason for one action is ADR-014 (completion), not click rates. |
| **"Choice overload" is weaker than its reputation.** A meta-analysis of 50 experiments (N = 5,036) found a mean effect "virtually zero," with large variation between studies and no sufficient conditions identified. | [Scheibehenne, Greifeneder & Todd 2010, *JCR*](https://abcwest.cogs.indiana.edu/pmwiki/pdf/scheibehenne.options.2010.pdf) | High | **Important caveat.** The one-action rule should rest on completion data and the shame reasoning in ADR-016, not on the jam study. |
| **Asking for replies is plausibly good for deliverability, but unproven.** Mailbox providers don't publish how they weigh replies; claims come from deliverability vendors. A reply does add the sender to many recipients' address books. | [Suped](https://www.suped.com/knowledge/email-deliverability/sender-reputation/does-asking-for-replies-in-email-marketing-improve-deliverability); [Validity](https://www.validity.com/blog/to-reply-or-no-reply-that-is-the-question) | Low for a measurable inbox effect | Yes for the real reason in our sequences: a reply is the only unambiguous signal we get, and it's research (ADR-016). |
| **Hard stop conditions exist for bulk senders, not for us yet.** Gmail and Yahoo require one-click unsubscribe, SPF/DKIM/DMARC and a spam-complaint rate under 0.3% for senders of 5,000+ messages a day (since February 2024). | [Bounteous summary](https://www.bounteous.com/insights/2024/01/31/2024-gmail-and-yahoo-deliverability-changes/); [Close help](https://help.close.com/docs/requirements-for-bulk-email-senders) | Medium (secondary summaries of Google/Yahoo rules) | Not at our volume, but DMARC is already the open task in MAILERLITE-SETUP.md. Short sequences that end keep complaint rates low (inference). |
| **No study was found on when a follow-up sequence after a free completion should end.** | Searched; nothing with stated methods | n/a | ADR-016's "then stop" is a values decision consistent with the reminder evidence, not something the evidence requires. |

### 2c. Different emails per entry route vs one generic sequence

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Tailored messages change behavior more than generic ones, but the average effect is small.** Meta-analysis of 57 studies (N = 58,454) of tailored print health messages: r = 0.074. Effects vary with what is tailored on, the number of contacts, the behavior and the population. A later meta-analysis of 40 web-delivered tailored interventions (N = 20,180) compared tailored with non-tailored versions directly. | [Noar, Benac & Harris 2007, *Psych Bulletin*](https://pubmed.ncbi.nlm.nih.gov/17592961/); [Lustria et al. 2013, *J Health Commun*](https://scinapse.io/papers/2057902960) (effect size not retrieved) | High that tailoring helps a little; I could not retrieve which moderators help most | **Yes, with a twist.** Our routes tailor on the reader's *situation*, which they chose themselves, not on demographics. The evidence is about behavior change, which is our goal. |
| **Segmented campaigns get more clicks than unsegmented ones from the same sender.** Mailchimp compared about 11,000 segmented campaigns from about 2,000 customers with those customers' own unsegmented sends: opens +14%, clicks +101%, unsubscribes −9%. | [Mailchimp 2017](https://mailchimp.com/resources/effects-of-list-segmentation-on-email-marketing-stats/) | Medium–Low (vendor data, pre-MPP, senders chose when to segment so it isn't randomized) | Partly. Direction is consistent with the tailoring research. |
| **No study was found comparing segmentation by *reason for arriving* with a generic welcome**, for any brand, let alone a small one. | Searched; only vendor advice ("tag-based approach often results in higher conversion") | n/a | We are already segmented by route. What remains open is whether a *paid* offer should differ by route, which no evidence addresses. |
| **A comparable brand segments by self-identified type at the front door.** Clutterbug's free quiz sorts visitors into four organizing styles, each with its own results page. | [clutterbug.me](https://clutterbug.me/) | High that it exists; no data on whether it converts | Yes as a pattern. Note ADR-014 rejected a picker in favor of per-pain entry pages; the quiz is the menu-free version of the same idea. |

### 2d. From free to first purchase

**Drivers and timing**

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Giving first raises reciprocation.** In a field experiment with about 10,000 charity solicitation letters, a small gift raised the *frequency* of donations 17% and a large gift 75% over no gift, and the gifts paid for themselves. | [Falk 2007, *Econometrica*](https://iza.org/publications/dp/1148) | High | **Partly.** Charity giving is not a purchase, and reciprocity is not the motive we want to lean on. It does support ADR-020's order: real value first. |
| **Giving away too much lowers conversion.** In a field experiment with about 300,000 users of a software app, cutting free features raised conversion and sharing but lowered usage; managers had "given away too much for free." | [Runge, Wagner, Claussen & Klapper 2016, ESMT working paper](https://ideas.repec.org/p/esm/wpaper/esmt-16-06.html) | Medium–High (large randomized test; working paper; software, not guides) | **Yes, as a trade-off.** It supports ADR-014's "abundance suppresses conversion" but shows the cost: less free use. For us, use (completion) is the mission, so this cuts both ways. |
| **Progress on a goal can license stopping.** People who feel they've made progress on one goal become more likely to choose things that conflict with it. | [Fishbach & Dhar 2005, *JCR*](https://ideas.repec.org/a/oup/jconrs/v32y2005i3p370-377.html) | High for the effect in lab settings | **Inference, important:** the moment right after a win may be when the reader feels *done*, not when they want the next step. That cuts against the intuition that the moment of success is the best time to sell. |
| **Engagement drops right after a reward, then rebuilds.** In a café loyalty program, purchases sped up toward the free coffee, slowed after it ("post-reward resetting"), then sped up again toward the next. | [Kivetz, Urminsky & Zheng 2006, *JMR*](https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal) | High | Same inference as above. It also supports framing the next step as a new, visible goal rather than "more of the same." |
| **No controlled study was found on whether asking at the moment of success converts better.** Practitioner guides say "after the aha moment"; the best case study found (Memrise) tested how *often* an upgrade screen appeared (every 21st session instead of every 49th: +50% conversion), not *when* relative to success. | [Google Developers blog on Memrise](https://android-developers.googleblog.com/2016/11/learn-tips-from-memrise-to-increase-in-app-conversions-with-pricing-experiments.html?hl=es); [Monetizely (opinion)](https://www.getmonetizely.com/articles/crafting-freemium-to-premium-upgrade-journeys-that-actually-convert) | Low | Open question. The evidence above points both ways: reciprocity favors soon; licensing and post-reward resetting favor later. |
| **Habits take about two months, with wide variation.** Median 66 days to reach automaticity, range 18–254 days (the upper end is projected beyond the 84-day study). Occasional missed days reportedly didn't derail it (secondary reports). | [Lally et al. 2010, *EJSP*, summarized by BPS](https://bps.org.uk/research-digest/how-form-habit) | High for the median and range; Medium for the missed-day claim | **Inference:** if the paid step is maintenance (ADR-015's "the ten minutes a night that means you never do it again"), the reader can't know whether they need it until weeks after the win. |
| **Paying doesn't make people use what they bought, but price does select people who will.** Kenya bed nets: uptake fell 60 points from free to $0.60, and paying did not raise usage. Zambia water treatment: higher prices screened in heavier users, with "no consistent evidence of sunk-cost effects." | [Cohen & Dupas 2010, *QJE*](https://www.povertyactionlab.org/evaluation/free-distribution-or-cost-sharing-evidence-malaria-prevention-experiment-kenya); [Ashraf, Berry & Shapiro 2010, *AER*](https://www.povertyactionlab.org/evaluation/can-higher-prices-stimulate-product-use-evidence-randomized-experiment-zambia) | High | **Yes, directly.** It undercuts "people value what they pay for, so they'll finish it." It supports ADR-020's principle ("we don't sell to people who won't use it") only in the screening sense: buyers are likelier users, but the price doesn't create the use. |

**Pricing a $9–19 guide**

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **The $9–19 band matches what comparable creators charge today.** KC Davis: $4.99–$14.99 digital guides; Dana K. White: $15 mini-course. | [Struggle Care store](https://www.strugglecare.com/); [Dana K. White, 5 Day Clutter Shakedown](https://dana-k-white.teachable.com/courses/258319) (both fetched 2026-10-26) | High (prices seen on the pages) | **Yes.** Adds two current data points to [competitor-notes.md](../competitor-notes.md#verified-price-points). |
| **Prices ending in 9 raised demand in three field experiments**, more for new items, less when "Sale" cues were present. | [Anderson & Simester 2003, *QME*](https://ideas.repec.org/a/kap/qmktec/v1y2003i1p93-110.html) | High for the setting (catalog clothing) | Weakly. Different product and buyer. Not a reason to pick $9 over $10. |
| **Free is a special price.** Moving a cheap option from a low price to zero shifted choices far more than the same price gap elsewhere. | [Shampanier, Mazar & Ariely 2007, *Marketing Science*](https://people.duke.edu/~dandan/webfiles/PapersPI/Zero%20as%20a%20Special%20Price.pdf) | Medium. Not retracted as far as I found, but Ariely is a co-author and another of his papers was retracted in September 2026; I found no replication study either way. | Plausible: the step from free page to $9 guide is the biggest step on the ladder. Treat as a hypothesis. |
| **Pay-what-you-want often draws *fewer* buyers than a fixed low price.** Across three field experiments, people who would pay less than the "appropriate" price felt bad and skipped buying. | [Gneezy, Gneezy, Riener & Nelson 2012, *PNAS*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3358869) | High | **Yes, and it matters for this audience.** Readers whose core wound is shame may be the ones most likely to opt out rather than "underpay." |
| **When PWYW is used, most people pay little or nothing.** Radiohead's *In Rainbows*: comScore estimated 62% of downloaders paid nothing and payers averaged about $6 (Radiohead disputed the figures). One creator's 2014 pre-order with a $1 minimum averaged about $7. | [NBC News on comScore](https://www.nbcnews.com/id/wbna21656525); [Mattermark](https://mattermark.com/results-from-our-pay-what-you-want-experiment-for-the-mattermark-startup-traction-report) | Low–Medium (estimates, disputed, single cases) | Weakly. A review of 97 PWYW datasets exists ([Gerpott 2017](https://doaj.org/article/ee56eaf762974f35ba1ff40e6432b350)) but I couldn't retrieve its conclusions. |
| **More lenient return policies increase purchases and, less strongly, returns.** Meta-analysis of about 21–22 studies; the money dimension of leniency most raises purchases. | [Janakiraman, Syrdal & Freling 2016, *J Retailing*](https://news.utdallas.edu/?p=11491) (press summary; full text not retrieved) | Medium–High | Partly. The studies are physical retail. For digital guides, no rigorous data was found; vendor claims that a guarantee "doubles conversion" are unsourced. Dana K. White offers a 30-day full refund on her $15 course. |

**Free-to-paid conversion rates**

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **"2–5% of free users convert" is a freemium-software figure**, usually attributed to Vineet Kumar's 2014 HBR article. I found only secondary attributions; a 2026 SaaS survey reports a median of 8%. | [AMA (Kannan, Gu & Li)](https://www.ama.org/marketing-news/selecting-and-optimizing-the-freemium-sales-model/); [DBS](https://www.dbs.com/in/sme/businessclass/articles/business-strategy/conversion-rate.page); [Userpilot](https://userpilot.com/blog/freemium-to-premium) | Medium that this is the common SaaS range; Low that it applies to info products | **Poorly.** It's the likely origin of the ladder's 2–5% target, and it measures software users who keep using a free product, not email subscribers who finished one task. |
| **Paid newsletters convert about 3% of free subscribers** by crowd-sourced counts; Substack once promoted 5–10% (and 10% early on) but I found no current official statement. | [Simon Owens](https://simonowens.substack.com/p/whats-a-realistic-conversion-rate); [Steven Scesa](https://stevenscesaon.substack.com/p/substack-paidfree-ratio-analyses) | Low–Medium | Weakly. A subscription to more writing is a different purchase from a one-time guide. |
| **Most small creators sell very little.** Gumroad's 2020 report: about 46,000 creators made at least one cent; the median made **$70** for the year, and the top 1% earned about 60% of the money. A third-party tracker estimates about 2.5% of Gumroad products have any recorded sale. | [Silicon Florist summary of Gumroad's 2020 report](https://siliconflorist.com/2021/01/12/what-happened-in-the-gumroad-creator-community-in-2020/); [profitable.app](https://profitable.app/gumroad/stats) | Medium for the Gumroad median (primary report via secondary summary); Low for the tracker | **Yes, as a base rate.** The typical small seller's revenue is close to zero; outcomes are extremely skewed. |
| **The "1–3% of your list will buy" rule has no traceable source.** Practitioners repeat 1% or 1–2%; none cites data. | [Goodreads notes on *Your First 1000*](https://www.goodreads.com/notes/39679713-your-first-100/51422764-juan-manuel-vera/2c6e6945-d600-4064-ae5d-a1414a20215b); [Derek Murphy](https://derekmurphy.teachable.com/courses/1000-subscribers-in-10-days-or-less/lectures/3441639) | Low | See "Don't rely on." |
| **"Tripwire" offers (a cheap product shown right after a lead-magnet signup) have no independent data.** Even a vendor teaching them says reliable independent data is thin; published "take rates" are hypothetical. | [systeme.io](https://systeme.io/learn/tripwire-funnel/); [aovup (hypothetical, inconsistent numbers)](https://aovup.com/ecommerce/tripwire-funnel/) | Low | **No, and it conflicts with ADR-020.** A tripwire is sold before any use; ours is offered only after a win. |

### 2e. Action-gated offers and completion-based pricing

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **No study was found of an action-gated subscription for consumer guides** (next part unlocks only when the last is done). | Searched; course-platform blogs only | n/a | ADR-020's gate is untested anywhere I could find. |
| **Gated progression improves learning, but can lower completion when self-paced.** A meta-analysis of 108 controlled evaluations of mastery learning (advance only after mastering the unit) found positive effects on exam performance, stronger for weaker students. It also found these programs take more time and, in self-paced college programs, often *lower* completion rates. | [Kulik, Kulik & Bangert-Drowns 1990, *Rev Ed Research*](https://www.academia.edu/81783373/Effectiveness_of_Mastery_Learning_Programs_A_Meta_Analysis) (abstract via Academia.edu; the 0.52 SD effect size is only from a secondary summary) | High for direction; Medium for size | **Yes, as a warning.** The closest evidence to "unlock after doing" says it helps those who keep going and loses some who don't. |
| **Visible progress toward a goal speeds effort; a head start helps.** Goal-gradient: café customers bought faster as the reward neared. Endowed progress: a car-wash card with 2 of 10 stamps pre-filled was completed by 34% vs 19% for a blank 8-stamp card. | [Kivetz et al. 2006](https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal); [Nunes & Drèze 2006, *JCR*](https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-lowdown-on-customer-loyalty-programs-which-are-the-most-effective-and-why/) | High | **Yes.** A reader who finished a free entry page already has real "stamps." Inference: counting the free win as step one of a paid sequence is honest endowed progress, not an illusion. |
| **Commitment devices work for the few who choose them.** A smoking-cessation savings contract was taken up by 11% of smokers offered it and raised verified quitting by about 3 points at 6 and 12 months. A workplace gym study found that offering a self-funded commitment contract produced lasting change where a short incentive alone didn't. | [Giné, Karlan & Zinman 2010, *AEJ Applied*](https://www.povertyactionlab.org/print/pdf/node/1468) (Karlan is president of stickK.com); [Royer, Stehr & Sydnor 2015, *AEJ Applied*](https://www.nber.org/system/files/working_papers/w18580/w18580.pdf) | High | Partly. An action-gated subscription is a mild commitment device. Expect low take-up and a self-selected, motivated minority (inference). |
| **People overestimate their future follow-through when they pay up front.** Gym members forecast 9.5 visits a month and made about 4. | [DellaVigna & Malmendier 2006, *AER*](https://www.aeaweb.org/articles?id=10.1257%2Faer.96.3.694) (already in [underwater-professional.md](../underwater-professional.md)) | High | **Yes.** It is the strongest argument for gating: a time-based subscription profits from non-use, which ADR-020 rules out. |
| **Completion-based pricing has been tried and not reported.** Udacity refunded 50% of tuition to Nanodegree students who finished within 12 months (2015), after an experiment it called an overwhelming success; it quietly dropped the offer by 2018. No completion or uptake data was published. | [EdSurge 2015](https://www.edsurge.com/news/2015-07-10-udacity-offers-50-percent-rebate-as-long-as-you-finish); [I-Programmer 2018](https://www.i-programmer.info/news/150-training-a-education/11721-udacity-withdraws-jobs-guarantee.html) | High that it happened; no evidence on effect | Weakly. Shows the idea is commercially workable for at least a while, not that it raised completion. |
| **Drip release vs all-at-once: only vendor numbers.** One course platform claims 34% completion with drip vs 18% with full access across 1,200+ students; methods aren't given. | [Teachery](https://www.teachery.co/blog/drip-content-online-course-guide) | Low | See "Don't rely on." |

---

## 3. What others do

| Who | Free path | Paid path | What worked or failed | Source |
|---|---|---|---|---|
| **FlyLady** (Marla Cilley) | Daily free emails, "BabySteps" starting with shining the sink, daily missions. Members "graduate" once routines stick. | A store of housewares and organizing tools (sales reportedly $4M in 2007), books, a calendar; FlyLady Premium mentoring groups (2015); a subscription reminder app (2016). | **Worked:** a huge free list (300,000+ subscribers in 2016) built on tiny first actions. **Watch:** revenue came from merchandise, not paid instruction, and the free email volume is the opposite of our "sequences end" rule. Wikipedia reports the housewares business was closing in 2025, from a single footnote I couldn't confirm (Low). | [Wikipedia](https://en.wikipedia.org/wiki/FlyLady); [flylady.net](https://www.flylady.net/); FSB 2007 figure via [search summary](https://money.cnn.com/2007/08/16/smbusiness/Fly_Lady.fsb/index.htm) (page returned 503) |
| **KC Davis** (Struggle Care) | Newsletter signup gives a free decluttering guide; a free therapist guide; large free social presence. | Digital guides $4.99–$14.99 (Depression House cleaning guide $9.99, Declutter Guide $6.99, Family Management Bundle $14.99); an upgrade from the $9.99 guide to a $14.99 guide-plus-course bundle; book (350,000+ copies per [Simon & Schuster](https://www.simonandschuster.com/books/How-to-Keep-House-While-Drowning/KC-Davis/9781668002841)). | **Worked:** the closest match to our ladder: no-shame free content, a classic lead magnet, then single-issue guides in our exact price band. No conversion data is public. | [strugglecare.com](https://www.strugglecare.com/) (fetched 2026-10-26) |
| **Clutterbug** (Cas Aarssen) | Organizing-style quiz (four types); free 30-Day Decluttering Challenge with daily videos, an e-book, daily reminder emails and a checklist. | Courses, books, printables; prices previously verified at $30 bootcamp, $94 method, $99–149 certification ([competitor-notes](../competitor-notes.md#verified-price-points)). | **Worked:** self-segmentation at the door; a free *doing* program, not a free download. The quiz-to-paid link isn't visible on the site. | [clutterbug.me](https://clutterbug.me/) |
| **Dana K. White** (A Slob Comes Clean) | Newsletter signup gives a free "Five Steps" printable; free printable checklists; podcast and blog. | $15 *5 Day Clutter Shakedown* (five short videos, 30-day full refund, lifetime access), kept on sale because the bigger *Take Your House Back* course "enrolls only a few times a year"; $500 coach training plus $39/month certification; several books. | **Worked:** a small, always-available paid step that bridges to a larger course. **Relevant to ADR-009:** a faith-titled book (*Jesus Doesn't Care About Your Messy House*) sits beside her general books rather than inside them. | [Teachable course page](https://dana-k-white.teachable.com/courses/258319); [teachable school](https://dana-k-white.teachable.com/); [aslobcomesclean.com](https://www.aslobcomesclean.com/) |
| **Clean My Space** (Melissa Maker) | Free video content. | Previously recorded: checklists $0.99–$1.99, e-book bundles $7.99–$19.99 (bundle price conflicted between passes). | Couldn't re-verify; the site returned nothing and the shop subdomain didn't resolve. | [competitor-notes](../competitor-notes.md#verified-price-points) (Medium–Low) |
| **Tiny Habits** (BJ Fogg) | Free 5-day email program since 2011; a coach emails each weekday; about 35–40 minutes total. | Coaching and coach certification (fees not published in what I retrieved). A guarantee page invites people who finish the free program and still struggle to personal coaching. | **Worked:** a free, short, *finishable* email program with human check-ins, the nearest analog to our three-email sequences. Couldn't load the guarantee page itself. | [tinyhabits.com](https://www.tinyhabits.com/); [program page](https://tinyhabits.com/program-new/); [coach guidelines](https://tinyhabits.com/coachguidelines/) |
| **YNAB** (budgeting) | 34-day free trial, no card; free live and recorded workshops (about 20 minutes). | About $14.99/month or ~$109/year (sources conflict). | No public data on whether workshops raise conversion. | [YNAB trial page](https://www.ynab.com/our-free-34-day-trial); [CNBC Select](https://www.cnbc.com/select/ynab-budgeting-app-review/) |
| **Ramsey Solutions** (budgeting) | Free EveryDollar with manual entry; Baby Steps framework. | EveryDollar Premium (about $79.99/year, sources conflict); Ramsey+ bundle $59.99–$129.99 including Financial Peace University. | A free tool that's genuinely complete, with paid convenience. Reviewers say Premium mostly makes sense as part of the bundle. | [Tom's Guide](https://tomsguide.com/reviews/everydollar); [College Investor](https://thecollegeinvestor.com/35086/everydollar-review/) |
| **Udacity** (completion-based pricing) | n/a | 50% tuition back for finishing within 12 months. | Launched 2015, dropped by 2018, results never published. | [EdSurge](https://www.edsurge.com/news/2015-07-10-udacity-offers-50-percent-rebate-as-long-as-you-finish) |

**Pattern across the home-care creators (inference):** every one gives away a
*doing* program or a short printable, and the first paid step is $5–15 and
single-issue. None publishes conversion data. The bigger paid step (course,
certification) is where their revenue concentrates, which ADR-020 currently
leaves unpriced.

---

## 4. Don't rely on

| Claim | Why not |
|---|---|
| Ariely & Wertenbroch 2002 on self-imposed deadlines | **Retracted September 2026** ([Retraction Watch](https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/)). |
| "Single-CTA emails get 371% more clicks" | Repeated everywhere, traced to no test. The one documented case found shows +42%. |
| Per-position welcome-series benchmarks (e.g. "email 3 converts best") | A blog's synthesis with no dataset; e-commerce. |
| Any welcome-email open rate (50%, 84%, 91%) | Inflated by MPP and often unsourced. |
| "Welcome emails convert 4–8x better than promotions" | No primary source found. |
| "1–3% of your email list will buy" | No traceable data behind it. |
| "Freemium converts 2–5%" as a target for a guide business | Software-freemium figure, secondary attribution to Kumar 2014; a different kind of user and product. |
| Substack's "5–10% paid conversion" | Not found in a current Substack source; crowd-sourced data points to about 3%. |
| Drip release raising course completion 30–60% | Vendor figures without methods. |
| "A money-back guarantee doubles or triples digital-product conversion" | Vendor claim with no source; the solid research is on physical-retail return policies. |
| Tripwire "take rates" of 30–40% | Hypothetical numbers in vendor posts, internally inconsistent. |
| Gumroad PWYW "+8% sales across 146,271 products" | Third-party analysis with unknown methods. |
| The jam study as proof that fewer options always sell more | Meta-analytic mean effect is about zero. |
| "Commitment framing beats progress framing after a win" (Koo & Fishbach 2008) | Often cited; I could not retrieve or verify the paper's findings, so it isn't used above. |
| "Paying makes people value it, so they'll use it" | Directly tested and not supported (Cohen & Dupas; Ashraf, Berry & Shapiro). |
| FlyLady's store closing in 2025 | One Wikipedia footnote; not confirmed elsewhere. |
| Shampanier, Mazar & Ariely 2007 (zero price) | Not retracted as far as I found, but an Ariely co-authored paper with no replication found; use as a hypothesis only. |

---

## 5. Implications (inference, for the strategist to weigh)

All of this is inference from the findings above. None of it has met a reader.

1. **The current three-email shape is consistent with the evidence and nothing
   argues for longer.** Survey-reminder research flattens after a few
   contacts, and one specific reminder does most of the work. The evidence
   doesn't *require* stopping at three either; ADR-016's "then stop" stands
   on values, which is fine, but should be labeled that way.

2. **Opens are already out. The bigger measurement problem is list size.**
   With completion pages and replies we measure better than most senders.
   But at a few hundred subscribers, a 2% free-to-paid rate is a handful of
   people, which is noise. Counting buyers and reading their replies will say
   more than any rate for a long time. The ladder's 2–5% target is borrowed
   from software freemium; the realistic base rate for small digital sellers
   (Gumroad median of $70 a year) is far lower and highly skewed.

3. **There is no channel for the first purchase yet.** The sequences end on
   day 7, carry no offer, and the only exits are a reply or a purchase. If a
   $9–19 guide is "offered only after a free win" (ADR-020), the strategist
   has to decide *where* that offer lives: on the `/finished-*` page, in one
   of the three emails, in a reply from Charles, or in a separate opt-in. Each
   choice interacts with "every email asks less than the one before."

4. **"Ask at the moment of success" is contested by the evidence.**
   Reciprocity (Falk) favors asking soon after real value. Goal licensing
   (Fishbach & Dhar) and post-reward resetting (Kivetz et al.) suggest the
   moment right after a win is when people feel done. Habit formation (median
   66 days) suggests a reader can't judge a *maintenance* product until weeks
   later. This is a genuine open question to test, not to settle by argument.
   Framing the paid step as a new, visible goal with the free win counted as
   step one has the best support (goal gradient, endowed progress).

5. **Route-specific emails are supported; route-specific offers are untested.**
   Tailoring helps a little on average, and our routes tailor on a situation
   the reader picked. Whether each route needs its own paid guide, or all
   routes lead to one house-in-order step, isn't answered by any evidence
   found. ADR-015's "the paid step is smaller and in the same domain"
   implies the former.

6. **Price: keep it fixed, simple and in the band.** $9–19 matches KC Davis
   and Dana K. White today. Pay-what-you-want is the option most likely to
   backfire with a shame-sensitive reader (fewer buyers, per Gneezy et al.).
   A plain refund promise is cheap and what comparable creators offer; its
   effect on digital sales is unmeasured.

7. **Action-gating has theory behind it and a cost.** Gated progression helps
   people who keep going and loses some who don't (mastery learning).
   Commitment devices attract a motivated minority (about 11% take-up in the
   best-known trial). Paying up front without a gate profits from non-use
   (DellaVigna & Malmendier), which ADR-020 rejects. Since we can't observe
   completion except by self-report on the `/finished-*` pages, any gate is an
   honor system; whether that is a feature (no surveillance, no shame) or a
   flaw is a values call.

8. **Price doesn't create use.** The strongest causal evidence in this file
   (two randomized field experiments) says charging screens in likelier users
   but does not make anyone use what they bought. The paid guide has to be as
   finishable as the free page; the price won't do that work.
