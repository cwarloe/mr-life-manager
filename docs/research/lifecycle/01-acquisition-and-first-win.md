# Lifecycle 01: from a QR code to a first finished task

**Status:** Evidence only, 2026-10-26. No plan, no copy, no decisions. The
lifecycle-strategist turns this into proposals.
**Stage:** acquisition and activation, from seeing a flier or link to finishing
one task.
**Builds on:** [deferred-win.md](../deferred-win.md) (intention gap,
implementation intentions, reminders) ·
[deferred-win-architecture.md](../../../planning/deferred-win-architecture.md)
(the live "Start now / Not right now" flow) ·
[niche-strategy.md](../../business/niche-strategy.md) (open a niche only when
there is an insider) · [competitor-notes.md](../competitor-notes.md).
**Governing decisions:** ADR-014 (completion converts), ADR-020 (win before
wallet) and ADR-021 (ask for a when) are Accepted. ADR-010, ADR-015 and ADR-016
are under review and are not treated as settled here.

**How to read the tables.** The *Finding* and *Evidence* columns are
**evidence**: what a named source reports. The *Transfers to us?* column is
**inference**: my judgment about whether it carries over to a tiny,
trust-based brand with five free entry pages, a few hundred fliers and no ad
budget. Anything else that is inference or opinion is labeled where it appears.

**Confidence scale.** High: peer-reviewed, replicated or large and well
designed. Medium: one good study, a credible primary company dataset with stated
methods, or consistent secondary reports. Low: vendor claims, single anecdotes,
or a number I could not trace to its source.

---

## 1. Question

How does someone who sees a Mr. Life Manager flier or QR code in a café,
bookstore, campus board or community board, or who is handed one by a person,
get from that moment to finishing a first real task? Specifically: what makes
people scan a printed code, and how do scan and follow-through rates behave by
placement, copy and location; what the first phone screen after a scan has to
do, and how much the match between flier and page matters, including for people
who scan where they can't act; what research says about activation, time to
first value, small first tasks and one-step-at-a-time formats; whether a
referral from an insider (a coach, a ministry leader, a volunteer) beats an
anonymous flier; and what comparable home, cleaning, organizing and
life-skills brands did to move people from offline to online.

---

## 2. Findings

### 2.1 QR codes and print in physical places

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Scan rates from posters are low in absolute terms.** On a German research campus of about 25,000 people, posters in ten public spots for two weeks drew **37 unique scanners** in total. The authors put participation at under 1% of potential passers-by. | Geisler, Pöhn & Hommel 2024, ["Hooked: A Real-World Study on QR Code Phishing"](https://arxiv.org/html/2407.16230v1) (arXiv preprint, not peer-reviewed) | Medium | **Yes, as a base rate.** A campus board is our exact setting. Expect scans per flier per week in single digits, not dozens. |
| **A designed poster with a concrete benefit drew about three times the scans of a plain one.** Variant 2 (professional design, an Amazon voucher) had 25 unique scanners against 12 for the plain variant. Respondents who preferred it named the voucher (47%) and professionalism (44%). | [Hooked 2024](https://arxiv.org/html/2407.16230v1) | Low–Medium (tiny counts; two things changed at once) | **Partly.** We can't offer vouchers. The transferable part is that a stated, concrete payoff plus a credible look moved scans. A specific benefit ("Your spare room back in two hours") is the closest honest equivalent. That is inference. |
| **Distrust is the main reason people don't scan.** Of survey respondents who would scan neither poster, 77% gave lack of trust as the reason; 26% said they were not interested. | [Hooked 2024](https://arxiv.org/html/2407.16230v1); the FTC warned in Dec 2023 that scammers hide harmful links in QR codes ([CNBC](https://www.cnbc.com/2023/12/07/qr-codes-may-be-a-gateway-to-identity-theft-ftc-warns.html)) | Medium | **Yes, strongly.** An unknown brand on a board is exactly the low-trust case. A visible plain domain (mrlifemanager.com) next to the code, a human name, or a known place or person vouching for it all speak to this. That is inference; I found no study testing those fixes. |
| **People who do scan are mostly curious, and most who scan follow through to the page.** Across 139 flier locations in Pittsburgh over four weeks, 225 people visited the linked site; curiosity was the main stated reason for scanning. In a separate observed experiment, 85% of people who scanned a code went on to visit its URL. | Vidas et al. 2013, ["QRishing"](https://www.andrew.cmu.edu/user/nicolasc/publications/Vidas-USEC13.pdf), Financial Cryptography workshops | Medium (pre-pandemic) | **Yes.** The drop-off happens before the scan, not between scan and page. The flier's job is to earn the scan; the page's job is to hold the curious person who arrives. |
| **Curiosity interacts with design.** Highly curious people scan more from visually complex ads; less curious people are put off by complexity unless the code clearly fits the brand and message. | Okazaki et al. 2019, ["The curious versus the overwhelmed"](https://ideas.repec.org/a/eee/jbrese/v99y2019icp498-506.html), *J. Business Research* 99 | Medium (scan **intention**, lab, Coca-Cola posters) | **Partly.** Our reader is often the overwhelmed one by definition. Inference: a sparse flier where the code obviously belongs to the one stated problem is the safer design. |
| **Handing a QR flier to someone works, but far less often than asking them in person; it may reach people who wouldn't speak up.** In a women's health clinic, 17% of patients given a QR-code flier by staff took part (64/377), against 91% of those approached in person (57/63). The two arms enrolled similar numbers. Flier recruits were about twice as likely to disclose alcohol risk (38% vs 19%) and drug risk (31% vs 16%). | Beatty et al. 2024, [*JMIR Formative Research* 8:e48823](https://formative.jmir.org/2024/1/e48823) | Medium | **Yes, and it matters for shame.** A flier handed over by a trusted person converts at a fraction of a direct ask, but it reached people who disclosed more privately. Inference: for an audience whose core wound is shame, a self-serve page after a personal hand-off may suit some readers better than a conversation. |
| **QR familiarity rose after the pandemic, and codes now help slightly where they once didn't.** Gallup found a QR code in a mailed survey invitation had no effect in 2015 but a small, significant lift in 2022. A statewide US experiment found QR plus URL beat URL alone; a German panel found +3 points; a Swedish panel found no change in response but more smartphone completions. | Marlar & Schreiner 2024, *JSSAM* ([EBSCO record](https://www.ebsco.com/articles/history/80704703-d01e-5451-8a27-dcd3702e24e0/the-use-of-qr-codes-to-encourage-participation-in-mail-push-to-web-surveys-an-evaluation-of-experiments-from-2015-and-2022)); Endres et al. 2023 ([Boise State record](https://experts.boisestate.edu/en/publications/experimenting-with-qr-codes-and-envelope-size-in-push-to-web-surv/)); [Lundmark et al. 2023](https://www.gu.se/sites/default/files/2023-09/Lundmark%20et%20al%20%282023%29%20GOR.pdf) | Medium–High | **Yes, with a caveat.** These are mailed letters, where the person already intends to respond. A code adds convenience, not motivation. Always print the short URL as well. |
| **On a museum label, almost nobody scans.** Brooklyn Museum: 1.77% of visitors scanned entrance tags and about 0.06% scanned object labels. A Brazilian museum: 2.29% of visitors used any code over three months. Cambridge museums in 2021: QR drew nine times the page views of NFC. | [Brooklyn Museum tech blog](https://techblog.brooklynmuseum.org/tag/qrcode/feed/index.html); [Câmara Cascudo study](https://bell.unochapeco.edu.br/revistas/index.php/rcc/article/view/6656/3602); [Cambridge museums blog 2022](https://www.museums.cam.ac.uk/blog/2022/01/06/to-qr-or-nfc-that-is-the-question/) | Low–Medium (single sites, mostly pre-2020) | **As a floor, not a forecast.** It shows how low passive scanning can go when the code is secondary to what people came for, as at a café table. |
| **Per-location comparison needs a unique code per location; a shared code makes places impossible to compare.** Transport for London ran about 400 poster sites at roughly 5,000 scans a month (about 12 per site per month, my arithmetic) but used one code, so sites could not be compared. A Southampton trial gave each bus stop its own code and found use varied by area, not by weekday or peak hours. | [Terence Eden, TfL follow-up 2012](https://shkspr.mobi/blog/2012/04/tfl-qr-followup-5000-scans-per-month/) (blog, FOI data); [Univ. of Southampton record](https://eprints.soton.ac.uk/348567) (full text blocked; abstract via search) | Medium | **Yes, and we already do it.** The `qr-<place>-<page>` tag scheme in the architecture doc is the Southampton design. The open risk is volume: at single-digit scans per spot, differences between places will mostly be noise for months. That is inference. |
| **A prompt at the point of action works.** Signs at the stair-elevator decision point raised stair use by a median 2.4 percentage points, about 50% relative (11 studies). The review notes that signs naming a specific benefit, or speaking to a specific group, may work better. | [Community Preventive Services Task Force](https://www.thecommunityguide.org/findings/physical-activity-point-decision-prompts-encourage-use-stairs); Soler et al. 2010, *AJPM* | High | **Yes, for placement.** The strongest version of a flier sits where the task happens: a laundry room, a dorm hall, a mailroom, a move-in table. A café is the opposite, which is the deferred-win problem. That is inference. |
| **Tailoring a printed message to the reader helps, but only a little.** Across 57 studies (N = 58,454), tailored print beat generic print with a mean effect of r = .074. | Noar, Benac & Harris 2007, [*Psychological Bulletin*](https://pubmed.ncbi.nlm.nih.gov/17592961/) | High | **Yes, modestly.** A niche headline ("for new lieutenants") should help, but not dramatically. Don't expect wording alone to rescue a bad placement. |
| **Vendor data links designed codes and logos to more scans, but the comparison is confounded.** Bitly's QR Code Generator reports codes with logos averaged 232 scans vs 152 without, and dotted designs 239 vs 65 for plain, across about 2 billion scans in 2025. It gives no count of codes and no controls. | [QRCG by Bitly 2026 report](https://www.qr-code-generator.com/blog/how-to-create-high-performing-qr-codes/) | Low | **No, not as a causal claim.** Businesses that bother to brand codes also run bigger campaigns. It says nothing about whether a logo would change our scans. |
| **On call-to-action wording next to the code ("Scan to…"), I found no published controlled test.** Vendors claim 30–80% lifts without naming the tests. | [Linkbreakers](https://linkbreakers.com/help/article/qr-code-ab-testing-benchmarks-variables-that-affect-scan-rates); [QRCG CTA guide](https://www.qr-code-generator.com/blog/call-to-action-qr-codes/) | Low | **Unknown.** It is plausible and cheap to test ourselves with two `from=` tags. |
| **Scale of the habit.** Forecasts put US smartphone users scanning QR codes at roughly 99.5 million in 2025. | eMarketer figure via [NFCW](https://www.nfcw.com/technology/engagement/) (secondary; original not reached) | Low–Medium | **Background only.** Most adults know how to scan. Knowing how is not the barrier; trust and relevance are. |

**On specific benefit vs. brand.** I found no field experiment that isolates a
specific-benefit headline against a brand-name flier. What exists points the
same way without proving it: the Hooked voucher variant (a concrete payoff),
the Community Guide's note on benefit-specific signs, the curiosity-and-fit
result, and the small but real tailoring effect. *Inference:* an unknown brand
name carries no information to a stranger, so the problem statement has to do
the work. That matches the repo's existing rule that the headline is the
reader's own situation.

### 2.2 Landing on the page from a QR code

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Most attention goes to the first screen.** In NN/g's 2018 eyetracking study, 57% of page-viewing time went above the fold and 74% to the first two screenfuls (120 participants, desktop). | [NN/g, "Scrolling and Attention"](https://www.nngroup.com/articles/scrolling-and-attention/) | High for desktop; Medium for phones | **Yes.** On a phone the first screen is smaller, so it has to carry recognition (this is my problem) and the fork (now or a time). The pages already do this; this supports keeping the fork high. |
| **When the page matches the ad, more people convert.** Two nonprofit tests from Facebook ads: Hoover Institution's page made to match its ad image converted 34.8% vs 25.0% (3,687 visitors). Dallas Theological Seminary matched ad and page image: 0.73% vs 0.49% (about 240,000 impressions). | NextAfter experiments [#314 (Hoover)](https://www.nextafter.com/experiments/increasing-landing-page-congruence-affects-cost-subscriber/) and [DTS](https://www.nextafter.com/experiments/how-congruence-between-ad-and-landing-page-affects-conversion/) | Medium (single tests, practitioner-run, stated significance) | **Yes.** Small, values-driven organizations, and the effect is visual as well as verbal. Inference: the flier and the page should share the same headline words and the same look, so a scanner knows in one glance they are in the right place. |
| **Match can backfire if the page promises something it doesn't deliver.** NN/g found that when a strongly scented page lacked the expected content, users concluded the whole site lacked it and left. | Nielsen, "Deceivingly Strong Information Scent Costs Sales," summarized by [CXL](https://cxl.com/blog/high-user-engagement/); [NN/g on information foraging](https://www.nngroup.com/articles/information-foraging-leave-site/) | Medium | **Yes.** A flier that says "two hours" must land on a page that says two hours, not on a general home page. Our entry pages are already self-contained. |
| **Plain words correlate with higher conversion.** Unbounce's 2024 data (41,000+ landing pages, 57 million conversions) found pages written at a 5th–7th grade level had an 11.1% median conversion rate vs 5.3% at college level. | [Unbounce benchmark methodology](https://unbounce.com/conversion-benchmark-report/methodology/); figures via [MarketingProfs](https://marketingprofs.com/charts/2024/52374/landing-page-conversion-benchmarks) | Medium (large, correlational; mostly commercial pages) | **Yes.** Consistent with content/README.md. Reading level is cheap to check. |
| **Faster mobile pages convert better.** Across 37 brands and about 30 million sessions, a 0.1-second improvement on every page in the journey went with 8.4% more retail conversions. | Deloitte for Google, ["Milliseconds Make Millions"](https://web.dev/case-studies/milliseconds-make-millions) (2020) | Medium (Google-commissioned, observational) | **Low priority.** Our pages are static and small. Keep them that way: no heavy scripts or video on the first screen. |
| **Some people who scan can't act there, and planning for later can lower doing it now.** In four studies, progress toward a goal licensed people to pursue opposing goals, and **merely planning to make progress later led to present choices against the goal.** | Fishbach & Dhar 2005, [*J. Consumer Research* 32(3)](https://academic.oup.com/jcr/article-abstract/32/3/370/1787396) | Medium–High | **Yes, and it's a caution for ADR-021.** A "Not right now" button can draw readers who could have started now. Inference: the "Start now" path should stay the default and the visually primary choice, and the measure is completions by path, which the Umami `path=now` / `path=appointment` tags already capture. |
| **Simple plan-making helps one-off actions, not repeated ones.** 877 gym members who picked days and times to exercise attended no more than controls, with a tightly estimated null. The authors contrast it with positive results for one-time acts (vaccination, voting). | Carrera et al. 2018, [*J. Health Economics* 62](https://www.nber.org/papers/w24959) | High | **Yes, for scope.** Our first task is a one-off ("one zone, two hours"), which is where planning prompts work. Don't extend the appointment logic to habits (the nightly ten minutes) and expect the same effect. |
| **A distinctive physical cue at the place of action helps people remember.** Linking an intention to a distinctive cue that will be seen when the action is possible raised follow-through in six lab and field studies; people undervalue the method. | Rogers & Milkman 2016, ["Reminders Through Association,"](https://scholar.harvard.edu/files/todd_rogers/files/reminders_through_association_2016.pdf) *Psychological Science* 27(7) | Medium–High | **Plausibly.** The printed action sheet, or the flier itself, could be the cue if the reader puts it where the task is. That is untested for us and is inference. |
| **Asking someone whether they'll do something slightly raises the chance they do it.** Across 116 tests, intention or self-prediction questions had a small effect (d = 0.24), larger for easy, desirable behaviors. Later reviews flag bias risk and heterogeneity. | Wood et al. 2016 ([eScholarship](https://escholarship.org/uc/item/4r7461w6)); Miles et al. 2020 ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7308800/)) | Medium | **Small, possibly useful.** The fork ("Are you where this happens?") is a question with no wrong answer, which keeps it on the right side of ADR-016's rule even though that ADR is under review. |

**Building on deferred-win.md, not repeating it.** That file covers the
intention gap, date-and-time plans, reminders, the "reserved for you" framing
and fresh starts. What this pass adds: (1) the Fishbach & Dhar licensing
risk, meaning a later option can pull people away from now; (2) the Carrera
boundary, meaning plans help one-off tasks, not habits; (3) the Rogers &
Milkman cue result, an offline reminder that needs no data from us; and (4) the
point-of-decision result, meaning the cheapest fix for "can't act here" may be
putting fliers where people can act.

### 2.3 Getting to a first win

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Self-guided programs mostly don't get finished.** MOOC completion stayed low and flat over six years on edX (HarvardX and MITx); most learners never return after year one. Health-app interventions lose a pooled 43% of users (17 studies, very high heterogeneity). | Reich & Ruipérez-Valiente 2019, ["The MOOC Pivot,"](https://tsl.mit.edu/research/the-mooc-pivot/) *Science* 363; Meyerowitz-Katz et al. 2020, [*JMIR* 22(9)](https://www.jmir.org/2020/9/e20283/) | High | **Yes.** It's the base rate behind ADR-014. The deferred-win doc's "expect about half not to do it" is consistent. |
| **A little human guidance raises completion.** Guided internet interventions show more completed modules and more completers than unguided ones; a 2021 meta-analysis of 22 studies found a significant but small effect. The guide's profession didn't seem to matter. | Baumeister et al. 2014, *Internet Interventions* 1(4); Musiat et al. 2021, [*Psychological Medicine*](https://www.cambridge.org/core/journals/psychological-medicine/article/abs/impact-of-guidance-on-intervention-adherence-in-computerised-interventions-for-mental-health-problems-a-metaanalysis/02990B48E8FEB565569640C54BF8E9F1) | Medium–High (mental health context) | **Yes, for the escalation ladder.** Supports "a friend checks on you" (step 2) and, later, a person (step 4). That the guide's profession didn't matter fits a friend or volunteer as checker. That is inference. |
| **Being shown progress at the start raises completion.** A car-wash card needing 8 washes, printed as 10 spaces with 2 already stamped, was completed by 34% of customers vs 19% for a blank 8-space card. | Nunes & Drèze 2006, *J. Consumer Research* 32(4) (summary via [Wharton](https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-lowdown-on-customer-loyalty-programs-which-are-the-most-effective-and-why/)) | High (field experiment, widely replicated concept) | **Yes, honestly applied.** A reader who did the portable steps in the café has real progress. Showing it on return ("you've already done the first two") is accurate, not a trick. Fake head starts would break our honesty rule. |
| **Effort rises as the finish gets closer.** Café customers bought faster as they neared a free drink, and an illusory head start sped them up too. | Kivetz, Urminsky & Zheng 2006, [*J. Marketing Research* 43](https://business.columbia.edu/insights/chazen-global-insights/goal-gradient-hypothesis-resurrected-purchase-acceleration) | High | **Yes.** Short tasks with a visible end benefit from this. It favors "one zone" over "the whole room". |
| **Progress bars only help if early progress feels fast.** Across 32 experiments, a constant-speed progress indicator did not reduce drop-off; fast-then-slow reduced it; slow-then-fast increased it. | Villar, Callegaro & Yang 2013, [*Social Science Computer Review* 31(6)](https://research.google/pubs/where-am-i-a-meta-analysis-of-experiments-on-the-effects-of-progress-indicators-for-web-surveys/) | High (surveys, not physical tasks) | **Yes, for step order.** Inference: put a quick, sure step first (several pages already start with a short decide or prepare step). A "step 1 of 9" counter on a page whose first step takes 45 minutes would show slow early progress, the pattern that raised drop-off. |
| **One-question-per-screen vs scrolling: mixed evidence.** In a mobile survey experiment (2,100 completes), scrolling was faster and had slightly lower, not significantly different, breakoff than paging. GOV.UK's "one thing per page" pattern is backed by its own user research with low-confidence users and on mobile, but that research is unpublished. | Mavletova & Couper 2014 ([chapter](https://www.ubiquitypress.com/site/chapters/10.5334/bar.f)); [GDS, "One thing per page"](https://designnotes.blog.gov.uk/2015/07/03/one-thing-per-page/) | Medium (surveys) / Low–Medium (GDS) | **Partly.** No one has tested step-per-screen for a *physical* task. Our doing mode exists so "Next" stays on screen while the reader's hands are busy, a different job from answering questions. The evidence neither supports nor undermines it. Don't cite surveys as proof either way. |
| **Simple planning doesn't reliably change repeated behavior, and experts can't predict which nudge will work.** In a 61,293-person gym megastudy, 45% of 54 programs raised visits by 9–27% during the four weeks, but only 8% had effects that lasted after. Forecasters failed to predict the winners. | Milkman et al. 2021, [*Nature* 600](https://mathematica.org/publications/megastudies-improve-the-impact-of-applied-behavioural-science) | High | **Yes, as humility.** Untested design choices should be called untested, and our own completion data should outrank anyone's intuition, including this file's. |
| **Small wins go with higher motivation.** In about 12,000 daily diary entries from 238 professionals, people reported their best motivation and mood on days they made progress, even small progress; setbacks weighed more. | Amabile & Kramer, *The Progress Principle* (2011), summarized by [HBS Working Knowledge](https://hbswk.hbs.edu/item/6685.html) | Medium (correlational, workplace) | **Directionally.** It supports ending the first task on a clear, visible "done". |
| **Trying the product before signing up reportedly raised engagement at Duolingo.** Moving sign-up after a first lesson is reported as a roughly 20% gain, but secondary sources disagree on whether it was next-day retention or daily active users. | [Taplytics write-up](https://taplytics.com/blog/duolingo-ab-test-onboarding); [ReallyGoodUX](https://www.reallygoodux.io/blog/duolingo-user-onboarding) | Low (no primary source) | **Directionally, yes.** Consistent with the win-first pattern, but don't quote the 20%. |
| **"Time to first value" is mostly industry measurement, not research.** Userpilot's vendor data puts median SaaS time-to-value at 1.5 days and activation at 37.5%, from only 62 companies. | [Userpilot 2025 benchmarks](https://userpilot.com/saas-product-metrics/) | Low–Medium | **No.** Software onboarding with accounts and teams. The useful idea, measuring the time from first visit to first completion, is ours to measure: `start-now` to `finished` in Umami. |
| **A small first request makes a later, bigger one slightly more likely, under conditions.** Foot-in-the-door effects are real but small and depend on conditions such as the first act being freely chosen and self-relevant. | Burger 1999, *Personality and Social Psychology Review* 3(4) ([record](https://cbsm.com/articles/32623-the-foot-in-the-door-compliance-procedure-a-multiple-process-analysis-and-review)) | Medium | **Weakly.** It supports a free first task leading to a $9–19 guide (ADR-020) only if the first task was the reader's own choice and finished. It is not a lever to push. |

### 2.4 Niche communities and trusted messengers

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Personal contact beats print by a wide margin in rigorous field experiments.** Across 51 canvassing experiments, a face-to-face contact raised turnout by 4.3 percentage points per contact. In the original New Haven experiment, canvassing raised turnout 8.7 points, each mailing about 0.5, and commercial phone calls had no detectable effect. | Green & Gerber, summarized in [SSIR](https://ssir.org/articles/entry/getting_out_the_vote_is_tougher_than_you_think); [J-PAL evaluation summary](https://www.povertyactionlab.org/evaluation/effects-canvassing-phone-calls-and-direct-mail-voter-turnout-united-states) | High | **Yes, in direction.** The gap between a person asking and a piece of paper is large and well replicated. A flier is the weakest channel we have; a person handing over the link is the strongest. |
| **Influence travels through close ties.** In a 61-million-person Facebook experiment, a get-out-the-vote message showing friends who had voted spread to friends and friends of friends. The spread to others had a bigger effect on real voting than the message itself, and nearly all of it ran between close friends likely to know each other face to face. | Bond et al. 2012, [*Nature* 489](https://sparq.stanford.edu/sites/g/files/sbiybj19021/files/media/file/bond_et_al._2012_-_a_61-million-person_experiment_in_social_influence_political_mobilization.pdf) | High | **Yes.** Supports niche-strategy.md's rule: open a niche only when there's an insider. A volunteer who personally knows cadets is a close tie; a board in the student union is not. |
| **Referred customers stay longer and are worth more.** At a German bank (about 10,000 customers, nearly three years), referred customers were at least 16% more valuable and churned about 18% more slowly than similar non-referred customers. | Schmitt, Skiera & Van den Bulte 2011, [*J. Marketing* 75(1)](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Schmitt-Skiera-vandenBulte-2011-Referral-Programs-Customer-Value.pdf); churn figure from the authors' [GfK MIR summary](https://reference-global.com/download/article/10.2478/gfkmir-2014-0020.pdf) | High | **Yes, in direction.** It is a bank with a paid referral program. Paying referrers is not on the table for us, and the effect may differ without a reward. |
| **Word of mouth outlasts and outweighs traditional marketing for sign-ups.** On a social network, member invitations had a long-run sign-up elasticity of about 0.53, roughly 20 times that of marketing events and 30 times that of media appearances, and the effect lasted longer. | Trusov, Bucklin & Pauwels 2009, *J. Marketing* 73(5) ([summary](https://marketingandmetrics.com/effects-of-word-of-mouth-versus-traditional-marketing-findings-for-an-internet-social-networking-site/)) | Medium–High (observational time series) | **Partly.** It's a social network, where inviting is the product. It agrees with everything else here. |
| **In recruitment studies, referrals produce more people, more cheaply, than fliers.** Adolescent study: word of mouth brought 52% of 200 enrollees at $7 each; fliers 7.5% at $10; Facebook ads 23% at $150. Young-adult weight trial (599 people): fliers, events and print ads each brought under 10%. Young cancer survivors: brochures produced zero contacts. | Rait et al. 2015, [*Transl. Behav. Med.* 5(3)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4537465); Tate et al. 2014, [*Trials*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4150977/); Rabin et al. 2013, [*J. Clin. Psych. Med. Settings*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3541434) | Medium (different populations and measures) | **Yes.** Cheap fliers are cheap per person, but they bring few people. Fliers support an insider; they don't replace one. That is inference. |
| **Credible local opinion leaders shift practice modestly.** Across 18 studies, local opinion leaders improved professionals' compliance with desired practice by a median 9 percentage points (moderate certainty; the range includes a small negative effect). | Flodgren et al. 2019, [Cochrane CD000125](https://www.cochrane.org/evidence/CD000125) | Medium–High | **Yes, by analogy.** A ministry leader or coach is an opinion leader in a small network. Expect a real but modest effect, not a flood. |
| **Recruited "popular opinion leaders" added nothing over an intensive comparison in a five-country trial.** Self-reported risk fell about a third in both arms; opinion leaders gave no extra benefit. The comparison arm was itself intensive, so the leaders' effect alone is unknown. | NIMH Collaborative HIV/STD Prevention Trial Group 2010, [*JAIDS* 54(2)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2904551); [aidsmap summary](https://www.aidsmap.com/news/apr-2010/popular-opinion-leaders-add-no-benefit-intensive-hiv-prevention) | High | **Caution.** Recruiting and training "influencers" is not the same as a person who already cares passing a link along. The positive evidence is for natural ties (Bond) and real credibility (Cochrane). |
| **Credentialed messengers in paid ads had small, inconsistent effects.** Doctors' and nurses' Facebook videos reduced holiday travel slightly in a county-randomized trial; a follow-up with similar videos for vaccination found no detectable effect despite reaching 29 million users. | Breza et al. 2021, [*Nature Medicine* 27](https://www.hks.harvard.edu/publications/effects-large-scale-social-media-advertising-campaign-holiday-travel-and-covid-19); [J-PAL case study](https://www.povertyactionlab.org/case-study/communicating-covid-19-messages-scale-social-media) | High | **Yes, as a distinction.** "Trusted messenger" works through a relationship, not a job title. A stranger with credentials in an ad is closer to a flier than to a friend. That is inference. |
| **A trusted setting plus real help can produce large effects.** Pharmacists working in Black-owned barbershops cut systolic blood pressure by 27.0 mmHg vs 9.3 in controls at six months (319 men, 52 shops). | Victor et al. 2018, *NEJM* ([Healio summary](https://www.healio.com/news/cardiology/20180328/hypertension-intervention-in-barbershops-cuts-bp-levels)) | High | **Partly.** The barber's role was trust and access; the pharmacist did the clinical work. Analogy: an insider makes the introduction, the page does the work. The clinical context is very different. |
| **Church-based programs reach people and can change behavior**, especially when built with the congregation; reviews lack pooled effect sizes. | Campbell et al. 2007, [*Annual Review of Public Health* 28](https://drum.lib.umd.edu/items/9218dee7-a079-4512-b684-f6a517ea0880) | Medium | **With ADR-009 limits.** A ministry can refer; the general product carries no faith content. The evidence is about programs built *with* churches, which is more than the referral-only role in our notes. |
| **People say they trust recommendations from people they know above any advertising.** 83% of respondents in 60 countries said they completely or somewhat trust friends' and family's recommendations. | [Nielsen Global Trust in Advertising 2015](https://www.nielsen.com/insights/2015/global-trust-in-advertising/) (online survey, about 30,000 respondents) | Medium (self-report) | **Background only.** Stated trust, not behavior. The field experiments above are stronger evidence for the same point. |

---

## 3. What others do

None of the five named brands has a documented **print or QR** acquisition
channel. Every one grew online first, then moved to books or TV. That gap is
itself a finding: I found no sourced example of a home, cleaning or organizing
brand that grew through fliers.

| Who | What they did | What worked or failed | Source and confidence |
|---|---|---|---|
| **FlyLady** (Marla Cilley) | Started in 1999 on a web forum for disorganized people; a member asked her to start an email group to mentor others. Moved to e-Groups, then Yahoo Groups; website in 2001. New members ("FlyBabies") start with **"Go shine your sink"** and 31 one-a-day baby steps, then "graduate" off the emails. | Over 300,000 email subscribers by 2016; store sales of $4 million in 2007. Email volume was heavy: up to 20 messages a day in 2002. A 2025 notice says the store business was closing. Lesson: a tiny, concrete first step and peer mentoring worked; the volume breaks our no-nagging rule. | [Wikipedia](https://en.wikipedia.org/wiki/FlyLady) (citing USA Today, CSM, Fortune Small Business); [CSM 2002](https://m.csmonitor.com/2002/0710/p18s02-lihc.html). Medium |
| **KC Davis** (Struggle Care, @domesticblisters) | A licensed therapist on TikTok. Self-published a **68-page** guide in Oct 2020; Simon & Schuster republished it in 2022. | The short self-published guide reportedly sold about 27,900 copies before the deal (agency claim); our earlier research verified 350,000+ copies overall. TikTok following about 1.8M (third-party ranking, 2026). Lesson: a professional credential plus no-shame framing, and a *short* first product. | [Mohrbooks rights listing](https://www.rightsdesk.com/works/how-to-keep-house-while-drowning-1) (self-reported); [competitor-notes.md](../competitor-notes.md); [infludata](https://infludata.com/rankings/top-20-influencer-united-states-of-america-minneapolis-tiktok). Medium for the arc, Low for the numbers |
| **Clutterbug** (Cas Aarssen) | YouTube channel started at her husband's suggestion; signature **quiz** sorts people into four organizing styles; later books and HGTV's *Hot Mess House*. | About 420,000 YouTube subscribers by 2020. The quiz is a front door that asks about the person rather than offering a menu of products, the same move as ADR-014's "a question, not a menu." I found no data on quiz completions or email capture. | [Sarnia News Today 2020](https://sarnianewstoday.ca/chatham/news/2020/06/10/local-woman-star-new-hgtv-show); [Apartment Therapy](https://www.apartmenttherapy.com/clutterbug-organizing-style-37411897). Medium |
| **Unf\*ck Your Habitat** (Rachel Hoffman) | A Tumblr blog of daily, weekly and mini **challenges**; the **20/10** rule (20 minutes cleaning, 10 off, no marathons); book in 2016 for people "left behind by traditional aspirational systems." | Time-boxed small tasks and a challenge format. Growth numbers not found. | [Pan Macmillan](https://www.panmacmillan.com/authors/rachel-hoffman/unfck-your-habitat/9781509830206). Medium for format, no data on reach |
| **Library "Adulting 101" programs** | North Bend (Ore.) Public Library: a flier with six months of topics on bulletin boards, the website, Facebook and local media. | A reporter found the flier and coverage went viral ("tens of thousands" of hits), but sessions drew **12 and 13** people, mostly teens and parents rather than the 16–25 target. Forsyth County (Ga.): most popular topics were health insurance, résumés and car buying; the meal-planning session drew least. Lesson: buzz is not attendance, and the people who come are not always the target. | [Programming Librarian](https://programminglibrarian.org/programs/adulting-101); [American Libraries 2018](https://americanlibrariesmagazine.org/2018/05/01/adulting-101-library-programming/). Medium |
| **University adulting programs** | MSU's Adulting 101 reports 50–1,000 attendees per session since 2019 (format not stated; most popular topics are financial). Kennesaw State and UC Riverside run series tied to student success; Waterloo runs a communications campaign. | No published outcome evaluation found for any of them. These are possible partners or referrers, not proof of a channel. | [Newsweek 2025](https://www.newsweek.com/gen-z-adulting-life-skills-classes-2078070); [Kennesaw State](https://www.kennesaw.edu/student-affairs/adulting-101.php). Low–Medium |
| **Financial Peace University** (Ramsey) | Grew a life-skills course through **churches hosting it**: DVD lessons plus small groups, run by local volunteers. | Ramsey-sourced figures: 50,000 churches have taught it; participant claims rose from 750,000 families (2009) to about 2.5 million (recent). The clearest example in a life-skills category of distribution through trusted institutions. It is a paid, multi-week course with explicit faith alignment, which differs from our product and ADR-009. | [Baptist Press](https://www.baptistpress.com/resource-library/news/dave-ramsey-urges-pastors-to-lead-people-out-of-debt/); [Christianity Today](https://christianitytoday.com/?p=196351). Low–Medium (company-reported) |

A lead, not a finding: a search snippet said Boise Public Library runs an
adulting series with a monthly badge. I could not open the source, so it is
unverified. If true, it is a local referral partner in the founder's city.

---

## 4. Don't rely on

- **"53% of mobile visitors leave if a page takes over 3 seconds."** Google
  2016. The method is thin, Google's own posts word it as "likely," and it is
  not a causal estimate ([DoubleClick blog](https://doubleclick-publishers.googleblog.com/2016/09/)).
- **Facebook's "7 friends in 10 days" and similar "aha moment" numbers.** A
  correlation repeated as a cause; no primary source; wording varies
  ([Geckoboard](https://www.geckoboard.com/blog/how-facebooks-7-friends-in-10-days-got-everyone-confused-about-correlation-and-causation/)).
- **Duolingo's "20% from delayed sign-up."** No primary source, and secondary
  sources disagree on what metric moved.
- **Vendor QR statistics** ("branded codes get 3.8x scans," "CTAs lift scans
  30–80%," "1–5% scan rate on posters"). No stated method, or confounded.
- **"QR scan reluctance is 40%"** and similar quishing-survey figures. Security
  vendors and QR vendors report opposite numbers, each without independent
  method.
- **Recruited popular-opinion-leader programs as proof that "influencers"
  work.** The large NIMH trial found no added benefit.
- **Physician or credentialed faces in ads as "trusted messengers."** Small
  effects for travel, null for vaccination (Breza et al.).
- **Ariely & Wertenbroch 2002 (self-imposed deadlines).** Retracted September
  2026 ([Retraction Watch](https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/)).
  Not used here.
- **The "Zeigarnik effect" as a reason starting makes people finish.** Already
  flagged in deferred-win.md; I found nothing new to rescue it.
- **"Tiny habits" claims of specific success rates.** Not peer-reviewed; not
  used here.
- **The "seven words on a billboard" rule** and other print-copy rules of
  thumb. I found no study behind them.
- **Specific benefit vs. brand, as settled.** It is consistent with the
  evidence but untested in a field experiment. Say "likely," not "proven."

---

## 5. Implications (inference, for the strategist to weigh)

All of this is inference from the findings above. None of it is a decision.

1. **The flier is the weakest link, and the person is the strongest.** Every
   comparison that pits a human ask against print (canvassing, recruitment,
   close-tie spread) favors the human by a wide margin. Fliers look most useful
   as something an insider hands over, or as a reminder at the place of action,
   not as the main way strangers find us. This is consistent with
   niche-strategy.md's "open a niche only when there is an insider."
2. **Placement may matter more than copy.** Point-of-decision prompts work
   because they sit where the action happens. A laundry room, dorm hallway,
   apartment mailroom or move-in table puts the reader in the room; a café puts
   them in the deferred-win problem. If both are tried, the `from=` tags can
   compare them, but expect small numbers.
3. **Trust is the scan barrier, and relevance is the scan driver.** Evidence
   points to a plain, visible web address, a specific problem in the reader's
   words, and an uncluttered layout. No study tests these exact fixes for a
   small brand.
4. **Expect very small counts and be patient with location data.** At the scan
   rates found (dozens per campus per fortnight; about a dozen per poster per
   month on the London Underground), per-location comparisons will be mostly
   noise for a long time. A handful of completions from a spot is a signal worth
   recording; a difference of three scans is not.
5. **Message match is cheap and has decent evidence.** Same headline words,
   same look, flier to page. The live pages already land on the reader's
   problem, so the work is on the flier side.
6. **Watch the "Not right now" path for cannibalization.** Planning to act later
   can license not acting now (Fishbach & Dhar). The Umami `path=now` and
   `path=appointment` split, read against `start-now` and `not-right-now`, is
   the test. If appointment-takers finish less often than people who would
   otherwise have started, that is a design signal. The base rate is about half
   of intentions not acted on.
7. **Keep the appointment logic for one-off tasks.** Plans help one-time acts and
   not repeated ones (Carrera). The first win qualifies; a nightly routine does
   not.
8. **Order steps so early progress feels fast, and show only real progress.**
   Supported by the progress-indicator meta-analysis, endowed progress and goal
   gradient. Credit what the reader really did at the café when they return.
9. **A little human checking raises completion.** Guidance research supports the
   "send to someone who'll check on you" step and suggests the checker doesn't
   need credentials. That fits Dave's "have someone check you."
10. **Comparable brands won online, through a person with a story, a tiny first
    step and a no-shame frame.** None shows a print path. If print is tried, it
    is new ground for this category. Treat it as an experiment, and say so.
