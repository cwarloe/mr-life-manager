# After the first purchase: retention, upsells and referrals

**Stage:** 3 of 3 (after the first purchase) · **Researched:** 2026-10-26 ·
**Author:** lifecycle-researcher (evidence only; planning belongs to
lifecycle-strategist)

**How to read this file.** Each *Finding* is **evidence**: what a source
reports, with a link and a confidence level. The *Transfers to us?* column and
everything under [Implications](#5-implications-inference) is **inference**,
our reasoning about a small, trust-based brand. Anything that is only
**opinion** is labeled as opinion. Where a source was available only as an
abstract or a press summary, the confidence level reflects that.

**Repo context used:** ADR-013 (free to use, never free to sell), ADR-014
(completion converts), ADR-020 (win before wallet; $9–19 band; subscriptions
only if action-gated), ADR-021 (ask for a when),
[product-ladder.md](../../business/product-ladder.md),
[business-model.md](../../business/business-model.md),
[niche-strategy.md](../../business/niche-strategy.md),
[commerce-rules.md](../../business/commerce-rules.md) and the escalation ladder
in [deferred-win-architecture.md](../../../planning/deferred-win-architecture.md)
(page → appointment → a friend checks → bot check-in → human walkthrough).
ADR-010, ADR-015 and ADR-016 are under review, so nothing below treats them as
settled.

---

## 1. Question

After someone has had a first win and made a first purchase, what keeps them
coming back to a brand whose promise is that they will need it *less* over
time, without a content treadmill or a churn-prone membership? How can more
help be offered so that it feels like help and not selling, especially the
repo's escalation ladder, where more costly help is offered only when the
cheaper step didn't work? Charles thinks referrals from happy customers could be
big: what does the research say about whether referred customers are worth
more, whether to reward referrals at all, who should get the reward, whether
rewards damage trust in a small values-driven brand, and when to ask? What is
known about sharing a commitment with a friend as accountability, and about
word of mouth inside tight communities? Briefly, can parents (buying for adult
children) and institutions (ministries, employers, property managers) be repeat
payers? And what did comparable home, organizing, cleaning and life-skills
brands actually do?

---

## 2. Findings

### 2.1 Retention when the promise is "you'll need us less"

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Self-improvement apps and courses lose almost everyone fast.** Across 93 popular mental-health apps, median 15-day retention was 3.9% and 30-day retention 3.3%. | [Baumel et al. 2019, *JMIR*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6785720) | High | **Yes, as a warning.** Any recurring product built on "keep using us" faces this base rate. Our content is task-shaped, not daily-habit-shaped, so this is about the category's ceiling, not a direct forecast. |
| **Paying doesn't fix completion.** In MIT and Harvard MOOCs, completion among learners who paid for verified certificates fell from 56% (2016–17) to 46% (2017–18); overall completion was 3.13%. Only 7% of 2016–17 first-time learners returned the next year. | [Reich & Ruipérez-Valiente 2019, *Science*](https://webs.um.es/jruiperez/papers/journals/2019_Science_MOOCPivot_postprint.pdf); figures as reported by [Inside Higher Ed](https://www.insidehighered.com/node/7744) | High (paper) / Medium (exact figures via press) | **Yes.** Supports ADR-014: a sale is not a win. Even paying, motivated buyers mostly don't finish long products. |
| **Subscription churn is front-loaded.** Across 115,000+ apps, nearly 30% of annual subscriptions are canceled in the first month. Cheap annual plans keep up to 36% after a year; high-priced monthly plans keep 6.7%. | [RevenueCat, State of Subscription Apps 2025](https://www.revenuecat.com/blog/company/the-state-of-subscription-apps-2025-launch.md) | Medium (vendor data, large sample, not peer-reviewed) | **Partly.** Mobile-app context. Category breakouts weren't in the text. It reinforces business-model.md's view that a content membership fights the brand. |
| **Flat-fee memberships can profit from non-use.** Gym members on flat monthly contracts attended about 4.3 times a month and paid more per visit than a 10-visit pass would have cost (~$600 over membership). Monthly members stayed enrolled longer than annual members. The authors' leading explanation is overconfidence about future self-control. | [DellaVigna & Malmendier 2006, *AER*](https://eml.berkeley.edu/%7Eulrike/Papers/gym.pdf) | High | **Yes, as an ethical boundary.** A subscription that earns most from people who don't use it is the opposite of ADR-020's "we don't sell to people who won't use it." This is the evidence behind the action-gated rule. |
| **Fresh-start moments recur and are predictable.** Searches for "diet," gym visits and goal commitments rise after temporal landmarks: new week, month, year or semester, birthdays, holidays. | [Dai, Milkman & Riis 2014, *Management Science*](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf) | High | **Yes.** Already used for first-win timing (deferred-win.md). The same research supports a small number of seasonal return points instead of a stream. |
| **Home care has its own seasons.** 80% of Americans said they planned to spring clean in 2024 (76% in 2018, 78% in 2020). | [ACI / Wakefield 2024](https://www.businesswire.com/news/home/20240306966220/en/ACI-Survey-80-of-Americans-Now-Spring-Clean-Every-Year); [ACI 2020](https://www.businesswire.com/news/home/20200304005692/en/Tough-on-Grime-2020-National-Cleaning-Survey-Reveals-Why-Americans-Rally-Around-Spring-Cleaning) | Medium (industry survey of stated plans) | **Yes.** A natural yearly touchpoint for a house-in-order brand. |
| **Moves cluster in summer, especially military moves.** About 65% of Department of Defense household-goods moves happen from May 15 to Sept. 30. The often-quoted "~70% of all US moves happen May–September" has no primary source we could find. | [Joint Base Charleston](https://www.jbcharleston.jb.mil/News/Article/233776/peak-move-season-get-ready); [MCB Quantico](https://www.quantico.marines.mil/News/Tag/67188/ipac-orders/) | Medium for military; Low for all US moves | **Yes for the Academy and Guard niches** (niche-strategy.md): PCS season is a dated transition moment. |
| **Customer communities: mixed results.** At eBay Germany, an email invitation raised community participation, but participation *lowered* listings and spending. Participants became more selective. At a US entertainment retailer, joining a firm-run community was followed by about 19% more spending, through more frequent purchases. | [Algesheimer et al. 2010, *Marketing Science*](https://ideas.repec.org/a/inm/ormksc/v29y2010i4p756-769.html); [Manchanda, Packard & Pattabhiramaiah 2015, *Marketing Science*](https://www.informs.org/News-Room/INFORMS-Releases/News-Releases/New-research-finds-double-digit-growth-for-firms-that-create-own-online-communities) | Medium (abstracts and press releases; the two studies disagree) | **Unclear.** Both are large platforms. Neither tests a community whose purpose is to make members need it less. The cost of hosting a community forever (business-model.md) is not in either study. |
| **Progress near a goal speeds people up.** Café customers bought coffee more often as they neared a free one. A 12-stamp card with 2 bonus stamps was finished faster than a plain 10-stamp card ("illusory progress"). Stronger acceleration predicted retention. | [Kivetz, Urminsky & Zheng 2006, *JMR*](https://business.columbia.edu/sites/default/files-efs/pubfiles/1200/goalgradient.pdf) | High | **The real-progress part, yes.** A visible "next win" ladder fits. The bonus-stamp trick is framing manipulation and conflicts with the no-manipulation rule (see [Don't rely on](#4-dont-rely-on)). |

### 2.2 Upsells and the escalation ladder

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **More help works best for people who need it most.** Across 39 trials (9,751 participants), both guided and unguided internet CBT beat controls. Guided was better overall, with the clearest benefit at moderate to severe symptoms and little difference at mild symptoms. | [Karyotaki et al. 2021, *JAMA Psychiatry*](https://www.healio.com/news/psychiatry/20210120/guided-internetbased-cbt-more-effective-for-depression-than-unguided-form) | High (IPD meta-analysis; clinical context) | **Yes, by analogy.** It supports offering human help to people the self-serve page didn't move, not to everyone. Clinical depression is not housekeeping, so this transfers as a principle, not an effect size. |
| **Stepped care (start cheap, step up for non-responders) works moderately well.** 10 trials (4,580 patients): pooled 6-month effect d = 0.34 against care as usual. The authors call the evidence that it beats other models "limited." | [van Straten et al. 2015, *Psychological Medicine*](https://www.cambridge.org/core/journals/psychological-medicine/article/abs/stepped-care-treatment-delivery-for-depression-a-systematic-review-and-metaanalysis/451FCB6B909825F5142A1E845F8651E2) | Medium–High | **Yes.** This is the closest research name for the repo's escalation ladder. It supports the shape; it does not prove stepped beats "everyone gets the same help." |
| **Human support works through accountability to someone trusted.** In the "supportive accountability" model, a coach improves adherence when seen as trustworthy, benevolent and expert; expectations should be clear, process-focused and agreed with the person. More intrinsically motivated people need less support. | [Mohr, Cuijpers & Lehman 2011, *JMIR*](https://pmc.ncbi.nlm.nih.gov/articles/PMC3221353) | Medium (a theoretical model built from adjacent literatures, not a trial) | **Yes.** It describes what Dave did for Charles. It suggests the bot (step 3) works only if it reads as benevolent and specific, and that the human step is for the less self-motivated. |
| **Regular feedback can stand in for peers.** In Chile, self-help savings groups (public goals, peer monitoring) raised deposits 3.7-fold and nearly doubled balances. A follow-up found that weekly feedback texts produced effects of similar size without meetings or peer pressure. | [Kast, Meier & Pomeranz 2018, *J. Development Economics*](https://www.povertyactionlab.org/media/file-research-paper/saving-more-groups-field-experimental-evidence-chile) | High (two RCTs; microcredit clients, so generalize with care) | **Yes.** Supports trying cheap steps (reminder, check-in message) before expensive ones (a person). |
| **A sales pitch after good service can backfire.** In an experiment, suggestive selling at the end of a service encounter lowered intent to buy more, especially when it clashed with the friendly behavior before it. | [Söderlund 2013, *Managing Service Quality*](https://www.emeraldinsight.com/insight/content/doi/10.1108/MSQ-03-2013-0045/full/html) | Medium (single study; abstract) | **Yes.** Supports commerce-rules.md's "never an upsell they didn't ask for." Help offered at the moment of struggle reads differently from a pitch tacked onto a win. |
| **Some cross-buyers lose money for the firm.** Across five companies, 10–35% of customers who cross-bought were unprofitable and accounted for 39–88% of lost profit, mainly through persistent heavy service use or returns. | Secondary write-up of Kumar-led research ([Loyalty360](https://loyalty360.org/Content-Gallery/Daily-News/adverse-cross-buying-customer-behavior-will-decrease-a-companys-profits-sig)); likely Shah, Kumar, Qu & Chen 2012, *Journal of Marketing* (not verified) | Low–Medium | **Weakly.** It matters for human help: a walkthrough sold cheaply to everyone could cost more than it earns. |
| **What higher-touch help costs in the market.** Professional organizers: roughly $50–150 an hour, often with 3-hour minimums. Virtual organizing: roughly $40–80 an hour; single "power hour" sessions around $99–150. ADHD coaches: roughly $75–250 a session. Focusmate (virtual body doubling): 3 free sessions a week, Plus about $8–12 a month. KonMari consultants pay about $3,000 for training plus $500 a year and some charge $100+ an hour. | [Fixr 2025](https://www.fixr.com/costs/professional-organizer); [Ideal Home](https://idealhome.co.uk/house-manual/storage-organisation/how-much-does-a-professional-declutterer-cost); [Neurolaunch](https://neurolaunch.com/how-much-is-an-adhd-coach/); [Lifestack on Focusmate](https://lifestack.ai/blog/focusmate-pricing); [KonMari admissions](https://events.konmari.com/event/upcomingcourses/admission); [Hunker](https://www.hunker.com/13762140/marie-kondo-konmari-consultant-course) | Low–Medium (cost guides and vendor pages, not surveys) | **Context only.** **Any human walkthrough priced like this sits above ADR-020's $9–19 band and contradicts a current decision.** The product ladder's Rung 3 ($299–2,500) predates ADR-020 and has not been re-decided. |

### 2.3 Referrals: are referred customers worth more?

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Referred customers were worth more and stayed longer.** German bank, ~10,000 customers, €25 reward. Referred customers had higher margins at first (the gap closed after about 1,000 days), churned about 18% less (the gap persisted), and were worth 16–25% more over their lifetime. Return on the reward: ~60% over six years. | [Schmitt, Skiera & Van den Bulte 2011, *Journal of Marketing*](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Schmitt-Skiera-vandenBulte-2011-Referral-Programs-Customer-Value.pdf); figures via [Knowledge at Wharton](https://knowledge.wharton.upenn.edu/article/turning-social-capital-into-economic-capital-straight-talk-about-word-of-mouth-marketing/) | High (one firm) | **Directionally.** A bank is a long, repeat relationship; our buyers make a few $9–19 purchases. The retention effect is the transferable part. |
| **Why: better matching and a shared bond.** Referrers send people who fit, and having a friend at the same firm deepens attachment. The authors suggest recruiting referrers among customers who have been with the firm at least six months and are profitable. | [Van den Bulte, Bayer, Skiera & Schmitt 2018, *JMR*](https://faculty.wharton.upenn.edu/wp-content/uploads/2017/07/VdB-et-al.-JMR-2018.pdf) | High | **Yes.** Matching is the point for a niche brand: a friend who knows both the reader and the page sends the right person. |
| **The value edge doesn't always replicate.** A replication with a simpler product found referred customers churned less but had *lower* margins. | [*Journal of Marketing Behavior* 3(4)](https://nowpublishers.com/article/Details/JMB-0054) (abstract via search; page blocked) | Medium | **Yes.** Expect the loyalty effect more reliably than a revenue effect. |
| **Referred customers refer more.** In data on 41.2 million customers of a cashback app, referred customers made more referrals than non-referred ones, after controlling for fit and network effects. Part of the reason: referring feels more socially appropriate if you were referred. Reminding customers they joined through a referral raised referrals 20–27% in a field experiment. | [Gershon & Jiang, *JMR* 2025](https://faculty.wharton.upenn.edu/wp-content/uploads/2020/06/gershon-jiang-2024-express-referral-contagion-downstream-benefits-of-customer-referrals.pdf) | High | **Yes, and this is the strongest support for Charles's hunch.** Referral is self-reinforcing, and the "you came here through a friend" reminder costs nothing. |
| **Referring makes the referrer more loyal.** At a cellular provider, customers who referred defected less over the next year (19% → 7%) and spent 11.4% more per month than a matched control group. The effect was strongest for newer customers. | [Garnefeld, Eggert, Helm & Tax 2013, *Journal of Marketing*](https://csl.wpcarey.asu.edu/growing-existing-customers-revenue-streams-through-customer-referral-programs) | Medium–High (field data plus lab; summary only) | **Yes.** Recommending something is a public commitment to it, which fits a brand built on follow-through. |
| **The best spenders are not the best referrers.** In 9,900 telecom and 6,700 financial-services customers, heavy spenders and good referrers were mostly different people. | [Kumar, Petersen & Leone 2007, *HBR*](https://scinapse.io/papers/121399320); method extended in [Kumar, Petersen & Leone 2010, *JM*](https://pure.psu.edu/en/publications/driving-profitability-by-encouraging-customer-referrals-who-when-/) | Medium (abstract-level) | **Yes.** Someone who only ever used the free pages can still be the best source of new people. Referral asks shouldn't be limited to buyers. |

### 2.4 Referrals: rewards, who gets them, and trust

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Rewards raise referrals most for weak brands and weak ties.** Four experiments: a reward raised referral likelihood by 20+ points for a weaker brand and under 10 for a stronger one. Reward size beyond "some reward" added little. For strong ties and stronger brands, giving at least part of the reward to the friend worked better. | [Ryu & Feick 2007, *Journal of Marketing*](https://biz.korea.ac.kr/news/academic_view?no=84); [Baylor summary](https://kellercenter.hankamer.baylor.edu/news/story/2008/insider-referral-reward-programs-and-referral-likelihood) | High (abstract plus summaries) | **Partly.** We are a weak (unknown) brand, which argues for rewards. But our referrals run through strong ties in tight niches, which argues for rewarding the friend, not the referrer. |
| **Rewards make friends suspect motives.** Receivers infer ulterior motives when the referrer is paid, which weakens their response. The effect is stronger for unsolicited and weak-tie referrals. Rewarding both sides, or using symbolic rewards, removed it. | [Verlegh, Ryu, Tuk & Feick 2013, *JAMS*](https://dare.uva.nl/id/553a0430-0ee6-4f93-bd73-f97db1105ca2) | High (abstract) | **Yes, strongly.** For a trust-based brand, a paid referrer is the risk. |
| **Bigger rewards make recommendations look less sincere.** Larger incentives were more attractive but made the recommendation seem less genuine. Authors advise low face-value rewards aimed at strong ties. | [Wirtz et al. 2013, *J. Service Research*; Orsingher & Wirtz 2018, *J. Services Marketing*](https://emerald.com/insight/content/doi/10.1108/JSM-07-2017-0247/full/html) | Medium–High | **Yes.** |
| **Rewards to the friend recruit more customers than rewards to the sender.** Two field experiments and a lab experiment. In one, 6,364 GiftAMeal customers got one of five offers (none, sender $5, friend $5, $2.50 each, or $5 donated to Feeding America). Friend-benefiting incentives recruited more. **Senders referred at similar rates with or without a personal reward, but much less when anonymous: they want credit for helping.** Sender rewards mattered only when referring was a hassle. Of 351 real programs reviewed, only 2.6% rewarded the friend alone. | [Gershon, Cryder & John 2020, *JMR* 57(1)](https://source.washu.edu/2020/07/research-shows-how-businesses-can-win-more-customers-influence-your-friends/); [Baylor summary](https://kellercenter.hankamer.baylor.edu/news/story/2020/earning-effective-referrals-right-incentives) | High | **Yes, and the best-fitting finding for us.** No payment to the referrer needed; the referrer's motive is looking helpful; make referring easy and make sure the friend knows who sent them. |
| **Cash can be the worst reward.** Consumers prefer cash, but cash carries social cost ("you're profiting off me"), so it produced fewer referrals and less acceptance than in-kind rewards, especially for weak brands, unless large or given to both sides. | [Jin & Huang 2014, *IJRM*](https://ideas.repec.org/a/eee/ijrema/v31y2014i1p107-116.html) | High (abstract) | **Yes.** If anything is given, a free guide beats money. |
| **Public referral rewards can backfire for new or innovative offers.** Rewards lowered referral likelihood under some conditions. Softened by not telling the friend about the referrer's reward, a larger reward, or rewarding both sides. | [Dose, Walsh, Beatty & Elsner 2019, *JAMS*](https://link.springer.com/article/10.1007/s11747-019-00635-z) | Medium–High | **Yes.** A "teach your life" brand is unfamiliar to most people, which is the risky case. Hiding a reward conflicts with our honesty rule, so the practical answer is no referrer reward. |
| **Bigger rewards bring in less profitable customers.** Bank field experiment (160,000+ customers) plus telecom data (~270,000): larger rewards raised acquisition but considerably cut the profitability of referred customers. | [Wolters, Schulze & Gedenk 2020, *Marketing Science*](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2020.1242) | High | **Yes.** People who come for the reward are not the people who come for the fix. |

### 2.5 Referrals: when to ask, and word of mouth in tight communities

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **No controlled study found on asking "right after a win."** Advice to ask at peak satisfaction is practitioner opinion (for example ReferralCandy) with no experimental data. | [ReferralCandy](https://www.referralcandy.com/blog/best-time-to-ask-for-a-referral) | Low (opinion) | **Unproven.** The adjacent evidence (rows below) supports it as inference only. |
| **People share what makes them look good.** Word of mouth is mostly self-serving: impression management, emotion regulation, information, social bonding, persuasion. | [Berger 2014, *J. Consumer Psychology*](https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/WOM-Annual-Rev-of-Psych.pdf) | High | **Yes, with a twist.** "I fixed my place" can be a good look *right after* the win; "I needed help with my mess" is not. The share should let the sender look helpful, not needy. |
| **Self-improvement gifts hurt.** Five experiments (1,340 people): recipients rated self-improvement gifts lower and were likelier to endorse negative reviews, driven by hurt feelings ("you think I'm not good enough"). The effect disappeared when people bought the same product for themselves. 67% had received such a gift. | [Chapman & Reshadi 2025, *Journal of Retailing* 101(3)](https://business.fiu.edu/news/2025/new-fiu-research-some-holiday-gifts-can-backfire-leading-to-hurt-feelings-bad-reviews.html) | High | **Yes, directly.** "Send this to a friend whose place is a mess" and a parent buying a "get your life together" guide both risk this. A competing WPI claim that recipients are more open than givers think is unverified. |
| **Strong ties carry referrals within a group; weak ties carry them between groups.** Strong, similar ties were more likely to be activated and were seen as more influential; weak ties bridged distinct subgroups. | [Brown & Reingen 1987, *J. Consumer Research*](https://academic.oup.com/jcr/article-abstract/14/3/350/1820141) | High | **Yes.** Fits niche-strategy.md: inside a niche, friends spread it; an insider bridges into each new niche. |
| **Loyal fans may add little new word of mouth.** In a restaurant chain field test, already-loyal customers enlisted to spread the word added no sales; the authors argue less loyal customers, talking to acquaintances, drove more incremental sales for a low-awareness product. | [Godes & Mayzlin 2009, *Marketing Science*](https://sloanreview.mit.edu/article/how-companies-turn-buzz-into-sales); replication: [Dost, Sievert & Kassim 2016](https://ideas.repec.org/a/eee/ijrema/v33y2016i1p236-239.html) | Medium | **Partly.** A reminder that the most enthusiastic customer may already have told everyone they know. |
| **Cues in the environment keep word of mouth going.** Interesting products got talked about right away, not over months. Products the environment reminds people of, or that are publicly visible, got more talk both right away and over time. | [Berger & Schwartz 2011, *JMR*](https://faculty.wharton.upenn.edu/wp-content/uploads/2011/10/BzzAgent.pdf) | High (abstract) | **Yes.** A printed sheet on a fridge or a desk with the site's share QR is exactly such a cue (the repo already embeds a share QR on printables). |
| **Big two-sided referral case.** Dropbox credited a two-sided referral program (both sides got storage) with a lasting 60% rise in signups; 35% of daily signups came from referrals as of April 2010. | [Houston, *Startup Lessons Learned* slides 2010](https://www.slideshare.net/slideshow/dropbox-startup-lessons-learned-3836587/3836587) | Medium (founder's self-report) | **Weakly.** The reward cost Dropbox almost nothing and was the product itself. The analog for us would be a free guide to both sides. |

### 2.6 Sharing a commitment with a friend

Relevant to step 2 of the escalation ladder ("send it to someone who'll check
on you") and to referrals, since the friend who checks on you also sees the page.

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Monitoring progress helps, more so when reported to others.** 138 randomized studies (N = 19,951): prompting people to monitor progress improved goal attainment (d = 0.40). Effects were larger when progress was reported or made public and when it was physically recorded. One bias-adjusted estimate is lower (d ≈ 0.19, via secondary source). | [Harkin et al. 2016, *Psychological Bulletin*](https://www.apa.org/news/press/releases/2015/10/progress-goals.aspx); [White Rose eprint](https://eprints.whiterose.ac.uk/id/eprint/91437/) | High | **Yes.** Directly supports the "a friend checks" step and a printed sheet you tick. |
| **Who you tell matters.** Telling a goal to someone you see as higher in status (someone you respect) raised commitment and performance. Telling a lower-status person, or no one, did not. | [Klein et al. 2019, *J. Applied Psychology*, via Ohio State](https://news.osu.edu/share-your-goals--but-be-careful-whom-you-tell/) | Medium (press coverage; paper not read) | **Yes.** Suggests "someone whose opinion you care about" beats "anyone." This is how Dave worked for Charles. |
| **Announcing an identity goal can backfire.** When others noticed an identity-related intention ("I'm going to be a lawyer"), people worked on it less, but only those strongly committed to the identity, and apparently because being noticed felt like already having it. | [Gollwitzer et al. 2009, *Psychological Science*](https://stafforini.com/works/gollwitzer-2009-when-intentions-go/) | Medium (no replication found either way) | **A narrow caution.** Sharing a dated *task* with a checker differs from announcing *who you are becoming*. Keep shares task- and time-specific. |
| **A referee raises self-reported success on stickK.** stickK reports that contracts with no stakes succeed 29% of the time and 59% with a referee (about 125,000 contracts). | [Yale Daily News quoting Ian Ayres](https://yaledailynews.com/?p=24449); [HBS case material](https://courses.edx.org/c4x/HarvardX/BUS5.1x/asset/8-page.html) | Low (self-selected users, self-reported, unaudited) | **Suggestive only.** People who choose a referee differ from those who don't. |
| **Partner-based plans have some trial support.** A UK trial tested collaborative implementation intentions (planning with a partner) for physical activity; a sister trial on diet found partner-based interventions had "some positive benefits." | [Prestwich et al. 2012, *Health Psychology*](https://eprints.whiterose.ac.uk/10346) | Low–Medium (results not retrieved) | **Possibly.** Points toward the friend helping set the time, not only receiving it. Needs the full paper before relying on it. |

### 2.7 Gift buyers and institutions as repeat payers

| Finding | Evidence | Confidence | Transfers to us? |
|---|---|---|---|
| **Parents already pay for adult children's households.** 59% of parents of 18–34-year-olds gave financial help in the past year; 28% of young adults got help with household expenses. 36% of helping parents said it hurt their own finances. | [Pew Research Center 2024](https://www.pewresearch.org/social-trends/2024/01/25/financial-help-and-independence-in-young-adulthood/) | High | **Yes, as a market fact.** Parents are a willing payer (ADR-010's idea, now under review). Nothing found on parents *repeat*-buying life-skills products. Expect one purchase per transition. |
| **Gifts are judged on use, not the moment of giving.** Givers over-weight the unwrapping moment; recipients value usefulness over time. | [Galak, Givi & Williams 2016, *Current Directions in Psychological Science*](https://www.cmu.edu/piper/news/archives/2016/december/gifting-errors.html) | Medium–High (review) | **Yes.** Combined with Chapman & Reshadi (2.5), a parent gift must not read as "you can't cope." |
| **Churches buy the same curriculum cohort after cohort.** Financial Peace University reports 4.5 million+ participants and use in about 50,000 churches. Churches run it in successive semesters, charging a kit fee per household each time (historically ~$93–119; some subsidize to $25–30). Ramsey sells to churches partly on increased giving. | [Baptist Press 2026](https://www.baptistpress.com/resource-library/news/dave-ramseys-love-for-pastors-fuels-mission/); [Ramsey 20-year release (2014)](https://www.ramseysolutions.com/company/newsroom/releases/financial-peace-university-celebrates-20-years-of-changing-lives); [Spokesman-Review 2012](https://www.spokesman.com/stories/2012/jan/05/fiscal-spiritual-advice-offered/); [Christ Fellowship](https://christfellowship.church:443/articles/financial-peace-university); [Ramsey church page](https://ramseysolutions.com/ramseyplus/organization/fpu-tithely/fpu-tithely-free-study) | Medium (company figures, local church listings) | **Partly.** The repeat comes from new people arriving every term, not from the same people buying again. Under ADR-013 a ministry can teach our material free; payment would come for things outside the license (printed kits, branded editions). FPU is explicitly faith-based; ADR-009 keeps faith content out of general products. |
| **Employers pay per head for practical-life benefits.** YNAB sells a workplace version at about $109 per employee per year (prorated), with an enterprise tier from 100 employees. | [YNAB for Organizations](https://ynab.com/wellness); [YNAB enterprise sign-up](https://www.youneedabudget.com/wellness/sign-up-enterprise) | Medium (vendor page; the plan the price applies to is unclear) | **Later.** Shows the shape of an employer offer; our material would need to be a product an HR buyer can evaluate. |
| **Property managers have a turnover cost to save.** Industry estimates put one move-out at $1,000–5,000 (one example averages $1,800; a vendor says ~$4,000). | [NAA](https://naahq.org/news/crunching-numbers-turnover-costs); [Grace Hill (vendor)](https://gracehill.com/resident-turnover-cost-calculator) | Low–Medium | **Unclear.** No evidence found that welcome kits or tenant education reduce turnover or damage. Alignment is plausible, unproven. |

---

## 3. What others do

| Who | What they did | What worked or failed | Source |
|---|---|---|---|
| **FlyLady** (home cleaning) | Free daily emails and "baby steps"; members "graduate" once routines stick. Revenue from a store of tools and housewares (~$4M in 2007), a book, and later FlyLady Premium (paid small-group mentoring, 2015) and the FlyLadyPlus app (2016). | Free method plus a paid store and a paid human-support tier is a long-lived model (300,000+ subscribers in 2016). The daily email stream breaks our no-nagging rule. | [Wikipedia](https://en.wikipedia.org/wiki/FlyLady); [CNN Money 2007](https://money.cnn.com/2007/08/16/smbusiness/Fly_Lady.fsb/index.htm) |
| **Dana K White** (A Slob Comes Clean) | Free blog, podcast, YouTube and printables; several books; a course; **certified decluttering coaches**; speaking. Her faith-labeled book is a separate title. | Free method feeds books, a course and a certification tier. The separate faith title mirrors ADR-009's split. Her business started from an ebook after 2.5 years of blogging. | [aslobcomesclean.com](https://www.aslobcomesclean.com/); [Simple Pin podcast](https://www.simplepinmedia.com/a-slob-comes-clean-summer-stories/) |
| **Clutterbug, KonMari, Go Clean Co** | Consumer tier cheap; certification is the high-end tier (Clutterbug $99–149; KonMari ~$3,000 plus $500 a year). | Upsell goes to people who want to *teach* it, not more product for the struggling user. | [competitor-notes.md](../competitor-notes.md#verified-price-points); [KonMari admissions](https://events.konmari.com/event/upcomingcourses/admission) |
| **WW (Weight Watchers) Lifetime** | Members who reach and hold a goal weight become Lifetime members: free (in the US) as long as they weigh in once each billing cycle within 2 lbs of goal; charged again if not. | A built-in "graduate but check in" model: the brand stays in touch through a periodic check, not content. Terms vary by country. | [WW Lifetime page](https://weightwatchers.com/us/blog/weight-loss/lifetime-membership) |
| **Hinge** ("designed to be deleted") | Positions success as leaving. The CEO says referrals from existing users are the top acquisition channel; the team counts deletion-survey answers and wedding invites as success. | A brand built on "you'll need us less" grew through word of mouth from people it worked for. Big-app context, self-reported. | [Global Dating Insights](https://www.globaldatinginsights.com/news/hinge-ceo-discusses-designed-to-be-deleted-redesign/); [The Drum 2024](https://www.thedrum.com/news/2024/10/03/hinge-s-cmo-her-unconventional-kpi-dates-so-great-people-delete-the-app) |
| **YNAB** | Two-sided referral: friend gets an extra free month; referrer gets a free month once the friend pays. Workplace version sold per employee. | Rewards both sides in product, not cash, matching the research above. Subscription business, unlike ours. | [YNAB referral help](https://support.ynab.com/en_us/referral-program-an-overview-BJWpA9Rc.md); [YNAB for Organizations](https://ynab.com/wellness) |
| **Tiny Habits** (BJ Fogg) | Free 5-day program by email (about 35 minutes total) that ends; book; certified coaches. | A short, finite free program that ends, feeding a book and coach tier. | [Tiny Habits](https://tinyhabits.com/quickstart/) |
| **Financial Peace University** (Ramsey) | Church-hosted cohorts, repeated each term; per-household kits; free access for pastors; discounted leader kits through denominations. | The institution supplies new people every term. Built on an explicit faith frame. | See 2.7 |
| **Morning Brew** | Tiered referral rewards (swag) for newsletter subscribers. | Credits referrals with about 30% of subscribers (up to 80% early on); figures vary by source and are self-reported. Rewarded referrers in a free-content setting; quality of referred subscribers not reported. | [GrowSurf](https://growsurf.com/blog/how-morning-brew-grew-its-subscribers/); [ReferralRock](https://referralrock.com/blog/wp-json/wp/v2/posts/30914) |
| **Society of Grownups** | MassMutual-funded adulting brand ($100M announced) aimed at 18–25-year-olds. | Closed within two years; 9,000 registrations showed demand, but the payer was wrong. | [competitor-notes.md](../competitor-notes.md) |

---

## 4. Don't rely on

- **"Acquiring a customer costs 5–25x more than keeping one" and "a 5% rise in
  retention raises profit 25–95%."** These trace to Reichheld & Sasser (*HBR*,
  1990) and later Bain analyses of service firms, mostly financial services.
  They are widely quoted as general laws. Not checked against our model; don't
  cite.
- **Dropbox "grew 3,900% through referrals."** Secondary blogs combine total
  user growth (100,000 to 4 million in 15 months) with the referral program.
  Houston's own slides credit referrals with a 60% lift and 35% of daily
  signups, not the whole growth. Several blogs also misstate the 2.8 million
  invites as an 18-month total; the slides give it as one month.
- **stickK's 29% vs. 59% referee figures.** Self-selected, self-reported,
  unaudited. Fine as a story, not as an effect size.
- **"Telling people your goals makes you less likely to achieve them."** The
  2009 study (Gollwitzer et al.) applies only to identity goals and to people
  strongly committed to them, and Klein et al. (2019) found the opposite when
  goals were shared with someone respected. No replication found either way.
- **Illusory progress (bonus stamps).** Real effect (Kivetz et al. 2006), but
  it works by making progress look bigger than it is. It conflicts with the
  no-manipulation rule.
- **Morning Brew's referral percentages.** 30%, 35% and 80% all circulate,
  from different dates, all self-reported.
- **"Ask for the referral at peak satisfaction."** Practitioner advice with no
  controlled study behind it (see 2.5).
- **Unprofitable cross-buying figures (10–35% of cross-buyers).** Found only in
  a secondary write-up; not matched to the original paper.
- **Fishbach & Dhar (2005), "Goals as excuses or guides."** Often cited to say
  that a win can license people to stop. Only the citation was confirmed, not
  the findings. Don't use it until the paper is read.
- **"~70% of US moves happen May–September."** No primary source found. The
  military figure (~65% of DoD moves in summer peak season) is sourced.
- **Self-imposed deadlines (Ariely & Wertenbroch 2002)** — relevant to any
  "commit to a friend" design; **retracted in September 2026** (see
  [deferred-win.md](../deferred-win.md#dont-cite)).

---

## 5. Implications (inference)

All of this is inference for the strategist to weigh. None of it is a decision.

1. **The best-supported referral design for us is the opposite of the common
   one.** Most programs pay the referrer (Gershon et al.: 40.5% sender-only,
   2.6% friend-only). For a trust-based brand with strong-tie referrals, the
   evidence points to **no reward to the referrer** (Verlegh et al.; Jin &
   Huang; Orsingher & Wirtz), **any benefit going to the friend or to both in
   kind** (Gershon et al.; Ryu & Feick), **the friend knowing who sent it**
   (Gershon et al.: senders want credit), and **referring being effortless.**
   This fits ADR-013 and the free-forever tier: the free page is already a
   gift to the friend.
2. **Referral looks self-reinforcing, and the cost to amplify it is near
   zero.** Referred customers refer more (Gershon & Jiang), referring makes
   the referrer more loyal (Garnefeld et al.), and referred customers churn
   less (Schmitt et al.). Telling someone they came through a friend raised
   referrals 20–27% in one field test. This supports Charles's hunch better
   than any single statistic about referral volume.
3. **Wording carries the main risk.** Self-improvement gifts produce hurt
   feelings and negative word of mouth (Chapman & Reshadi 2025), and people
   share what makes them look good (Berger). A share that implies "your place
   is a mess" could hurt both friend and brand. A share framed around the
   *task and time* ("I'm doing my desk Saturday at 10") or around *what worked
   for me* looks safer, but has not been tested.
4. **The two existing share moments do different jobs.** The deferred-win
   "send it to someone who'll check on you" is accountability (Harkin; Klein),
   and it is also the first referral, because the checker sees the page.
   Sharing after a win is word of mouth. The evidence suggests not merging
   them: the checker works best as someone respected; the post-win share works
   best as the sender helping someone.
5. **The escalation ladder matches stepped care and supportive
   accountability.** Cheap feedback can do much of what peers or people do
   (Kast et al.), and human help pays off most for people the self-serve
   version didn't move (Karyotaki et al.). Offering the next step at the point
   of struggle ("Not ready? Pick another time" → a check-in) reads as help.
   The same offer attached to a win reads as a pitch (Söderlund). **Steps 3
   and 4 priced at market rates for human help ($40–250 an hour) would
   contradict ADR-020's $9–19 band and need a decision.**
6. **Retention without a treadmill most likely looks like scheduled return
   points, not a stream.** Fresh-start dates, spring cleaning, move-in and
   PCS season, and a "check in" like WW Lifetime's are the evidence-backed
   moments. A flat-fee subscription that earns from non-use is ruled out by
   ADR-020 and by DellaVigna & Malmendier. **No evidence was found on churn
   for seasonal or action-gated memberships specifically;** that is a gap.
7. **Repeat institutional revenue comes from new people each term, not from
   repeat buyers.** FPU's model is a church running cohort after cohort. Under
   ADR-013 a ministry teaches our material for free; paid offers would be
   things outside the license (printed kits, editions, facilitator help).
   Parents look like one purchase per transition, and the gift-insult research
   applies to them too.
8. **Comparable brands make money from the people who want more, not from
   charging the struggling more.** The pattern across FlyLady, Dana K White,
   Clutterbug, KonMari and Tiny Habits: a free method that ends or graduates
   people, then books, a store, a small paid support tier, and a certification
   tier for people who want to teach it. A certification or facilitator tier
   is still missing from our ladder (as competitor-notes.md already flagged).
