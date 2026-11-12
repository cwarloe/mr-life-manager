# Instagram Reels (and the same files on TikTok and Shorts): can faceless video get us clicks and finished checklists?

**Status:** Research and recommendations, retrieved 2026-11-12. Nothing here has met a real reader or a real ad account. Every claim about platform behavior carries a date; the ones most likely to be stale are marked **[stale risk]**.
**Scope set by Charles (2026-11-12):** free-first only (Reel or ad, then the free checklist, then the finish page, then email, then a later paid offer). Replace nothing in the live copy; reuse and improve the existing flier and video lines. Do not mention or imply anyone's mental state, and do not criticize the viewer.
**Builds on, and does not repeat:** [lifecycle 01](../lifecycle/01-acquisition-and-first-win.md) (QR scans, person beats print, message match), [lifecycle 02](../lifecycle/02-emails-and-first-purchase.md) (free-to-paid evidence, pricing, tripwires), [lifecycle 04](../lifecycle/04-lifecycle-plan.md) (measurement and guardrails), [deferred-win.md](../deferred-win.md), [docs/copy/social-launch-kit.md](../../copy/social-launch-kit.md) (static post drafts and the first account plan), [video/README.md](../../../video/README.md), [ADR-020 to ADR-023](../../../planning/decisions.md).
**How sources are graded:** A = official platform documentation, regulator, or peer-reviewed. B = large independent dataset or reputable reporting of a primary event. C = vendor blog or benchmark report. D = anecdote, forum post, or unsourced claim. Full list at the end.

---

## Verdict

1. **Clicks: yes, but few.** Organic Reels from a brand-new account with no followers will reach some people, but the path from a view to a landing visit is long and leaky. My planning guess is 1 to 5 landing visits per 1,000 views from a bare bio link, and 3 to 15 per 10,000 views with a comment-a-word message (guesses, section 9). Paid ads give controllable volume: about 12 link clicks per 1,000 impressions at published cross-industry averages (grade C), roughly $1 per click.
2. **Finished checklists: possible, and that is the realistic win.** At those rates, $140 of ads buys roughly 100 to 120 clicks and about 8 to 12 finished checklists (a guess chain, section 9), so cost per finished checklist lands near $10 to $25 with very wide uncertainty.
3. **Sales from cold Instagram at our scale: no, not plausible.** Even with generous guesses (15% of finishers join the email list, 3% of those buy a $9 guide), 1,000 finished checklists produce about 4 or 5 buyers. Cold social cannot pay for itself on a $9 guide. The honest reason to spend is to learn whether strangers will finish a checklist, and to feed an email list that is worth something later.
4. **Our current videos have two problems Instagram itself names.** Instagram's own 2023 ranking post lists muted reels and majority-text reels among the content it aims to make less visible (grade A, **[stale risk]**). Our three files have no audio track (confirmed with ffprobe) and are almost entirely text. Add audio and some real footage before judging organic reach.
5. **The hooks need work, and the in-app browser needs a test before any traffic.** The hook is a question about who the viewer is, not a problem to fix right now, and the last scene has no "tap" instruction. Separately, the calendar button uses a `data:` download link that I could not confirm works inside Instagram's in-app browser (grade D evidence says it often does not); that is the step our whole "pick a time" idea depends on.
6. **Recommendation:** build the account properly, test the in-app flows on real phones, post organically for two weeks, then run a capped $140 two-campaign ad test (two hook angles, one audience). Judge by finished checklists and cost per finished checklist. Do not expect to settle which hook is better on purchase-like numbers; this budget can only detect large differences in click rate.

---

## 0. Decisions that need Charles

| # | Decision | My recommendation |
|---|---|---|
| 1 | Add audio (a voiceover or a Meta Sound Collection track) and a real-footage first shot, which departs from "no sound needed" in the video README | Yes, test it. Instagram lists muted and majority-text reels as less visible (section 1). Keep a text-only version as the control if you want a clean comparison. |
| 2 | Business or Creator account | Business (section 4). Switching later is free. |
| 3 | Add the Meta pixel to the site for ad optimization | No, not for this test. It conflicts with the privacy-first posture ([operations.md](../../../planning/operations.md)) and the budget is too small to optimize on purchases or finishes anyway. Use Umami and `from` tags. |
| 4 | Tags are lowercase only | The site accepts `^[a-z0-9-]{1,40}$` ([entry.js](../../../products/landing/assets/entry.js) line 25, [audience.js](../../../products/landing/assets/audience.js) line 15). An uppercase letter makes the tag silently drop to empty, so that traffic shows up untagged. |
| 5 | Direct-to-purchase ($9 from Instagram, no free step) | Not tested, per your 2026-11-12 decision. A short note on the evidence is in section 10.5. It would need ADR-020 re-decided, since ADR-020 offers a paid guide only after a finished free win. |

---

## 1. How faceless text-motion video performs on Instagram now

### What Instagram says officially

| Statement | Source, date | Grade | Meaning for us |
|---|---|---|---|
| "Start with a compelling hook in the first 3 seconds that compels people to stick around." Instagram also points creators to View Rate in Insights, the share of viewers who keep watching after the first 3 seconds. | [Creators blog, Feb 26, 2025](https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through) | A | Our hook scene lasts 3.3 seconds (100 frames). The hook has to deliver its point inside that window. |
| A reel is "initially recommended and shown to a small audience" of non-followers; reels that do well reach wider audiences; distribution is "based on its engagement, not just the creator's follower count." | Same post | A | A zero-follower account can be shown to strangers. The first small audience decides everything. |
| Trial reels: "post a reel just to accounts that do not follow you," then decide whether to share with followers. | Same post | A | A free way to test hooks on strangers before they go on the main grid. Check that the feature is available to our account type. |
| Reels up to 3 minutes can reach non-followers; the original-content post says the most effective growth is "post original content consistently." | [Creators blog, Jan 21, 2025](https://creators.instagram.com/blog/the-latest-with-instagram) | A | Our 27 seconds is fine on length. |
| The most important Reels predictions are "how likely you are to reshare a reel, watch a reel all the way through, like it, and go to the audio page." | [Mosseri, Instagram Ranking Explained, May 31, 2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained) | A, **[stale risk]** | Watch-through and sharing matter more than likes. A 27-second video that people watch to the end is in our favor. |
| Instagram "aims to make certain reels less visible," including reels that are "low-resolution or watermarked," "muted or contain borders," "majority text," or "already posted on Instagram." | Same post | A, **[stale risk]** (2023) | **Our videos are muted and majority text.** The only reason to doubt this is its age. It is the single most relevant official sentence for our format. |
| "Don't post reels that contain watermarks." Reels over 3 minutes are not recommended; only public accounts are recommended. | [Creators blog, Aug 30, 2022, updated Apr 25, 2023](https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators) | A | Render from Remotion (no watermark). Never re-upload a file saved from TikTok, which carries a TikTok watermark. |
| Top three ranking signals: watch time, likes and sends. | Mosseri video series, January 2025, as reported by [Social Media Today](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/) | B (reporting of an official statement) | "Sends" (a viewer sending a Reel to a friend) is why a "send this to someone who is cleaning up tonight" line is worth testing (section 11). |

### What changed about originality (April 30, 2026)

Instagram's [Rewarding original creators](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram) post (grade A) extends the original-content test to photos, carousels and reels: accounts that primarily post unoriginal content "will no longer be shown in places where we recommend content." It does not affect followers' feeds. Original means "wholly created or reflects your unique perspective." The post gives no numeric threshold ("a significant percentage" over a rolling 30 days) and says nothing about AI-generated content. It also reports "75% of recommendations in the US now coming from original posts" (Instagram's own figure, not independently checked).

Implication: our videos are our own, so this helps us. The risk is indirect. If we cross-post the same file with only the audience name changed, Instagram's duplicate detection could treat the second and third as repeats. I found no official statement on how it treats three similar files from one account. Treat that as untested and vary the first scene.

### What the independent data says

| Finding | Source | Grade | Notes |
|---|---|---|---|
| Business Reels from accounts with 1,000 to 5,000 followers reached 9.78% of followers on average, January to June 2026, about 140,000 Reels. | [Socialinsider](https://www.socialinsider.io/blog/instagram-reels-benchmarks/) | C (vendor, large sample) | Reach as a share of followers. It says nothing about zero-follower accounts or non-follower reach. |
| Average Reels engagement rate 0.48% to 0.52% in 2026; Rival IQ median Instagram engagement about 0.30%. | Socialinsider (same page); [Quid/Rival IQ](https://www.quid.com/knowledge-hub/resource-library/blog/2026-social-media-industry-benchmark-report) | C | Different denominators, so not comparable between vendors. |
| "The first 1.4 seconds" or "65% of viewers watch three seconds" style numbers. | Vendor and creator blogs | D | No primary source found. I do not use them. |
| Text-on-screen hooks and caption pacing "outperform." | Vendor blogs | D | No published methodology and no peer-reviewed study found. Evidence for faceless text-motion video as a format is thin; there is no good dataset, and I will not pretend otherwise. |
| Sound-off viewing as a rule of thumb ("85% watch without sound"). | Old Facebook-era claim, no current source | D | Not used. Instagram's own post says muted reels are shown less, which cuts the other way for Reels. |

**Bottom line on format.** Nothing I found proves text-motion beats other formats. What exists is one official warning against muted majority-text reels, one official instruction to hook in 3 seconds, and watch-through and sends as stated priorities. Plan for text-motion to be the weak format on Instagram unless we add sound and some visual proof of a real sink, table or room.

---

## 2. How a Reel turns into a click

### Mechanics that exist today

| Route | Allowed? | Restrictions and risks | Grade |
|---|---|---|---|
| **Link in bio** | Yes | One profile link works for everyone; the profile can hold several links. Best for a single stable destination. Per-post attribution is impossible, since every post shares one link. | A (help center, not fully retrievable), C |
| **Link sticker in Stories** | Yes, for most accounts | The 2021 announcement says "Accounts that are new, or that repeatedly share content violating Community Guidelines" do not get the link sticker, and Stories with link stickers cannot be boosted ([Instagram, Oct 2021](https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone), read through a search summary). **[stale risk]** A brand-new account may not have this sticker at first. | A, **[stale risk]** |
| **Clickable link in a Reel caption or comment** | No for ordinary accounts | Caption and comment URLs are not clickable. I found no official page stating this plainly; it comes from many third-party guides (grade D) and is consistent with my understanding. | D |
| **Clickable links in Reels or posts for paid plans** | Reported | Meta's September 2026 Meta One announcement is reported to say paid plans can add links to posts and Reels, starting at $14.99 a month (search summaries of [Meta's announcement](https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/); I did not retrieve the page itself and sources disagree on tiers and caps). | B/C, **[stale risk]** |
| **Ads with a call-to-action button** | Yes | Ads must comply with the Advertising Standards (section 3). The CTA button (for example "Learn more") is the cleanest route from a Reel placement to a landing page. | A |
| **Comment a word, receive the link by direct message** | Yes, via Meta's own API | Meta's [Private Replies](https://developers.facebook.com/documentation/instagram-platform/private-replies) allows one message per commenter, within a time window measured from the comment (reported as 7 days; verify). Follow-ups need the user to reply within 24 hours. Third-party tools use this API. | A (API docs), C |
| **"Send this to someone" (a share)** | Yes | A share is a ranking signal and a free referral. | A |

### Policy risks

- **Engagement bait.** Instagram's [Recommendation Guidelines](https://help.instagram.com/313829416281232) list engagement bait among content people dislike, and the creator site says repeated violations can make an account ineligible for recommendation. Social Media Today reports Instagram saying the test is intent (an attempt to hack reach versus connecting with an audience). "Comment CHECKLIST and I'll send it" asks for a comment in exchange for something, which sits near the line. I rate it a medium-low risk and a real one. Mitigation: ask for the comment only when it is the only way to get the link, say what you will send, and do not ask for likes or follows.
- **Automation flags on new accounts.** Third-party guides (D) claim new accounts hit action blocks faster and give inconsistent numbers. Do not use follow, like or comment bots. Use only API-based tools for DM replies, and keep volume low.
- **Link shorteners and look-alike domains.** I found no official rule. Using our own domain is both safer and more trustworthy; lifecycle 01 found distrust is the main reason people do not scan or tap an unknown link.

### Benchmarks, graded

| Step | Figure | Source, date | Grade | Notes |
|---|---|---|---|---|
| Profile visit to bio-link tap | "About 3%"; vendors claim 2% to 6% | [CreatorFlow](https://creatorflow.so/blog/bio-link-vs-dm-automation-affiliate-clicks/), 2025; [Brandwatch](https://www.brandwatch.com/social-media-glossary/link-in-bio/) defines the metric | D | No reliable cross-tool benchmark exists. Instagram's own analytics do not itemize bio-link clicks. Measure it ourselves. |
| DM-delivered link click | "12% to 18%" | Same CreatorFlow post (vendor, affiliate context, unclear source) | D | Plausible that it is higher than a bio link. Unverified. |
| Paid link click-through (CTR) | Cross-industry median link CTR 1.18% (Databox, July 2026). Education category: 1.45% (traffic) and 1.86% (lead gen), all-clicks CTR, WordStream, April 2024 to June 2025 | [Superscale roundup](https://superscale.ai/learn/meta-ads-benchmarks-by-industry/) | C | All-clicks CTR counts reactions and profile taps; link CTR counts destination clicks only. Do not mix them. |
| Cost per click | Home and lifestyle under $50 order value: $0.51 median CPC; services: $0.61 | [Lebesgue, Sept 2026](https://lebesgue.io/facebook-ads/meta-ads-benchmarks-by-industry-and-aov) (period and sample not stated; ecommerce) | C | Ecommerce brands with pixels and purchase optimization. Our traffic campaign has no pixel optimization. |
| Instagram Reels vs Stories | Reels $1.28 CPC, 2.08% CTR; Stories $1.15 CPC, 1.87% CTR; Instagram average CPC reported $1.42 in 2025 | [AdManage](https://admanage.ai/blog/how-much-do-instagram-ads-cost) | C | Sources disagree widely (Stories from $0.35 to $1.83 across vendors). I plan with about $1.00 per link click and a range of $0.60 to $1.50. |
| Small audiences | Narrow audiences usually cost more per click and tire faster | General practice, no published figure found | D | Say plainly: I found no reliable number for a small 18-to-24 audience. |

All US dollars. Meta's CPMs and CPCs vary by season; November to December costs more because of holiday advertisers (general knowledge, no source retrieved).

---

## 3. Paid versus organic at near-zero budget

### What a $5 to $10 per day test can and cannot tell you

Meta says an ad set is "learning limited" when it is unlikely to reach about 50 optimization events in the week after its last significant edit, and recommends raising the budget, broadening the audience, or choosing a more frequent event ([Meta Business Help](https://en-gb.facebook.com/business/help/269269737396981), grade A; Meta notes this is a signal, not a penalty).

For us this means: at $10 per day with about $1 per click we get about 10 clicks a day, about 70 per week. We cannot optimize for finished checklists (rare events) and cannot even reach 50 landing visits a week per ad set if we split the budget. So we pick the cheapest honest objective, **Traffic (link clicks)**, accept that Meta cannot learn much at this size, and judge on our own Umami counts.

Do not choose Engagement (it buys reactions) or Leads (it asks for an email form we do not run in the ad). Sales is not an objective for this test.

### What each budget can prove

All numbers use a $1.19 planning cost per click, derived from a $14 CPM and a 1.18% link CTR (both grade C). Treat them as a planning guess.

| Total spend | Clicks (approx.) | What it can prove | What it cannot |
|---|---|---|---|
| $0 (organic only) | Unknown, likely 0 to 30 | Whether any stranger taps and finishes; whether the in-app flow works | Anything about rates; the sample is too small |
| $140 (14 days at $10) | about 118 | Ads get approved; real CPC and CTR; that landing visits arrive and are counted; whether anyone finishes at all; a 2x or larger gap in click rate between two creatives | Which hook wins on starts or finishes; any purchase rate |
| $500 | about 420 | A start rate to within about plus or minus 6 points; a gap like 10% versus 20% in start rate (needs about 200 clicks per arm) | A 2% versus 5% purchase-type difference (needs about 590 clicks per arm) |
| $1,500 or more | about 1,260 | Two-arm comparison of small purchase-type rates | Anything about lifetime value; we still would not have enough buyers |

### Targeting (ages 18 to 24 and 22 to 32)

- Meta's age settings changed in 2025. With Advantage+ audience on, an age range is treated as a suggestion; a minimum age (settable between 18 and 25) is a hard limit ([Jon Loomer](https://www.jonloomer.com/meta-ads-targeting-guide/), grade C, summarizing Meta's behavior; no primary Meta page retrieved). **[stale risk]** Set the minimum age to 18 as the hard control and treat the upper age as soft.
- Interests are thin for this audience ("first apartment" is not a clean interest). Start broad inside the age limit and use creative to select, since the hook tells people whether it is for them.
- Military: do not use branch names, logos or ranks in targeting copy or visuals; ADR-023's rule (colors only) applies to ads too.

### Under-18s

We do not target minors. What Meta enforces, as far as I could confirm: since early 2023, advertisers can reach teens only by age and location, with gender and activity-based targeting removed ([Search Engine Land](https://searchengineland.com/meta-introduces-new-ad-targeting-limits-for-teens-391259), grade B/C reporting). Instagram also places under-18 accounts in Teen Accounts with a 13+ content setting (reported 2025). Those rules limit targeting; they do not stop a teen from seeing an ad or a Reel, which is why age 18 as the hard minimum, and copy that is clearly about an adult first apartment, matter. I did not find Meta's own page to cite for these; verify in Ads Manager.

### Meta Advertising Standards: guardrails for what we avoid

Charles's remark that the emotional context is about people "stuck" was an explanation of why people act, not copy. The policy check is therefore a list of things to keep out. Quotes are from the Meta Transparency Center, retrieved 2026-11-12 (grade A).

**Personal attributes** ([Privacy Violations and Personal Attributes](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/)):

- "ads must not contain content that asserts or implies personal attributes. This includes direct or indirect assertions or implications about a person's race, ethnicity, religion, beliefs, age, sexual orientation or practices, gender identity, disability, physical or mental health (including medical conditions), vulnerable financial status, voting status, membership in a trade union, criminal record, or name."
- "Instead, ads should focus on the benefits of the product or service being advertised."
- Allowed: "Use 'you/your' language without a personal attribute." Not allowed: "Using the word 'you/your/other' to reference a personal attribute."
- Meta's own examples include a disallowed "Depression getting you down? Get help now." and "Do you have diabetes?", and an allowed "Depression counseling." Also disallowed: "Are you 18 years old?"

What this means for us:

| Do | Do not |
|---|---|
| Describe the situation and the object: "Your sink is full." "People are coming over tonight." | Name a feeling or condition of the viewer: sad, depressed, anxious, overwhelmed, lazy, stuck, unmotivated, failing |
| Use "you/your" for the home and the task | "Are you ___?" about the person (age, money, health, military status); "Do you struggle with ___?" |
| "Living off base for the first time?" is a situation question and is probably fine, but see the risk below | Any line that says or implies the viewer is a certain kind of person |

**Risk to flag:** our current hooks ("Living on your own for the first time?", "Working long hours and living on your own for the first time?") ask the viewer to confirm who they are. Meta's list does not include "lives alone" or "works long hours," so I rate the risk low, but "first time" can read as an age proxy and an automated review could misclassify it. Moving the hook to the situation ("People are coming over tonight") removes the question rather than relying on a favorable review.

**Negative self-perception and before/after.** Meta's [Health and Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/) standard says "Ads must not imply or attempt to generate negative self-perception" and bars weight-loss and wrinkle side-by-side comparisons. The page shows different versions: the Jul 22, 2026 and Dec 26, 2024 versions include the negative self-perception language, and the "Today" version I fetched omits it. This rule is written for health and appearance products, so it does not govern cleaning checklists directly, but the principle matches our rule that copy names the situation, never the person. **A before/after photo of a messy and a clean room is not mentioned in this standard.** I found no rule against it. Our brand voice should still avoid shaming "before" images of a person's home.

**Misleading content.** [Prohibited Commercial Practices](https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/) names "deceptive pricing, unauthorized endorsements, and guaranteed investment returns." Our "free checklist, no app, no email needed" lines are true and are our strongest compliance asset. Keep them true: the landing page must keep delivering the checklist without an email.

**Home and personal-organization content.** I found no Advertising Standards category that restricts cleaning or home-organization ads. Inference: automated review might mistake a "first apartment" or "moving into a new place" ad for the Housing special ad category (rentals and listings), which restricts targeting. I found no evidence of this happening, so treat it as a watch item if an ad is rejected.

**AI-generated content in ads.** Our videos are not AI-generated. If a future version uses an AI voiceover or generated images: Meta says it adds an "AI info" label when people disclose AI content or when industry-standard indicators are detected, and advertisers must disclose in "certain cases" for political or social issue ads ([Meta, updated Oct 23, 2025](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/), grade A). Trade press in 2026 reports broader ad disclosure and "AI info" labels for ads made with Meta's own generative tools; reports conflict on whether disclosure is now mandatory for all ads (grade C/D). **[stale risk]** Disclose when in doubt.

**Selling digital products.** I found no Meta standard that restricts advertising a digital checklist. The standards do restrict health, finance and gambling categories, none of which we are in.

---

## 4. Opening the brand account properly

There is no Instagram account yet. The [social launch kit](../../copy/social-launch-kit.md) already sets the display name, bio and a Facebook Page plan; this section adds what to decide and check. Per CLAUDE.md, account creation and publishing belong to the downstream operator.

1. **Claim the handle everywhere at once.** The launch kit prefers `@mrlifemanager`; the roadmap lists a social-handle availability check as open ([roadmap.md](../../../planning/roadmap.md) line 32). Check Instagram, TikTok and YouTube for the same handle before creating any account, and avoid underscores and extra characters people will mistype.
2. **Create it on a phone with a brand email** (the contact address in the launch kit), turn on two-step authentication, and use one steady device and location. Unusual sign-ins are a reported trigger for challenges (grade D).
3. **Switch to a professional account.** Instagram's help center says both types unlock insights, ads and message tools; Creator suits "public figures, content producers, artists and influencers," Business suits "retailers, local businesses, brands, organizations and service providers" ([help center](https://help.instagram.com/138925576505882), summarized through search; the page body did not load for me). Pick Business: we are a brand. Two things to know. Instagram says licensed music can be unavailable "for your account type," with the Sound Collection as the fallback (section 6), and professional accounts cannot be private. You can switch back at any time.
4. **Connect a Facebook Page.** The launch kit already plans one. Meta's ad and DM-automation tools expect an Instagram account linked to a Page (my understanding; not confirmed on an official page).
5. **Profile.** Display name "Mr. Life Manager," the launch kit bio, a brand mark (no face needed), contact email, and one link: the audience page or the task page, with a tag such as `?from=ig-stu-bio` (section 5). The bio should say what the link opens. Keep the link stable.
6. **What to post first.** Eight to ten original posts before any ad runs, so a person who taps the profile sees substance: the three videos, three static images from the launch kit, and two or three of the "one useful thing" posts (a single step with an image). Never reuse someone else's content; Instagram's originality rules apply.
7. **How long until reach.** I found no official statement of a new-account penalty. Instagram says reels go first to a small audience of non-followers and expand if they do well (section 1), and a vendor study found 1,000-to-5,000-follower accounts reach 9.78% of followers (C). There is no published figure for a zero-follower account. My planning assumption is two to four weeks of consistent posting before any pattern is readable (guess).
8. **What gets new accounts flagged.** All grade D, from third-party guides with inconsistent numbers: bulk follows or likes, automated commenting, engagement pods, buying followers, repeated identical comments, logging in from many places. The official signals are Community Guidelines violations and unoriginal content (Account Status shows eligibility; check it weekly). One official item to expect: new accounts may not get the Story link sticker at first (section 2).
9. **Ad account.** Create it in Meta Business Suite with a payment method. Expect an identity or business verification step before ads run, and possible delays; I found no official timeline.

---

## 5. Tracking it in our stack

### What the site already does

- `entry.js` reads `?from=` and keeps it only if it matches `^[a-z0-9-]{1,40}$` (lowercase letters, digits, hyphens). It attaches it as `from` to every Umami event (`start-now`, `not-right-now`, `time-picked`, `calendar-added`, `started-from-reminder`, `finished`) and carries it to the finish page ([entry.js](../../../products/landing/assets/entry.js) lines 24 to 41, 145 to 149, 228).
- `audience.js` carries `from` from an audience page to the door links (lines 14 to 28).
- Umami Cloud (Hobby plan) is on; its UTM insight reads `utm_source`, `utm_medium`, `utm_campaign`, `utm_term` and `utm_content` ([Umami docs](https://docs.umami.is/docs/utm), grade A). The docs do not say that other parameters such as `from` appear in a built-in report; the site sends `from` explicitly with events, which is why we use it.

### `from` tag versus UTM

Use `from` as the one tag that drives our funnel events. Optionally add `utm_source=instagram&utm_medium=paid` (or `organic`) to ad URLs so Umami's UTM view and Meta's own reports line up. Do not rely on UTM alone: the entry script does not read UTM, so the tag would not reach `start-now` or `finished`. Meta also appends its own parameters (such as `fbclid`) to ad clicks, and those pass through harmlessly because the code reads only the `from` value. The referrer is unreliable for Instagram (many apps strip it or route through a link shim), which is the other reason the tag matters.

### Naming scheme (40 characters, lowercase)

`<platform>-<audience>-<source>-<post>`

| Part | Values |
|---|---|
| platform | `ig`, `tt`, `yt` |
| audience | `stu`, `car`, `mil` |
| source | `bio` (profile link), `dm` (keyword reply), `story`, `reel` (organic, via a per-post link), `ad` |
| post | short id: `tonight1`, `table1`, `dishes1`, `night1`, `boxes1`, `static1` |

Examples: `ig-stu-bio-main`, `ig-stu-dm-tonight1`, `ig-stu-ad-tonight1`, `ig-car-ad-dishes1`, `tt-mil-bio-main`. The longest example is under 25 characters. This extends the launch kit's `ig-company-profile` and `fb-company-c1` pattern; keep those as they are or rename them to match. Never use uppercase, spaces, underscores or dots.

A shared bio link cannot say which post sent someone. For per-post attribution, use the comment-a-word DM link (each post gets its own tag) or a Story link sticker with a post tag. Everything else is "bio, main."

### In-app browser: what it does to us

| Question | What I found | Grade |
|---|---|---|
| Does Instagram open links in its own browser? | Yes, on iOS and Android. Felix Krause's August 2022 research reported Instagram injects its own JavaScript into pages shown there and that opening in the default browser is available from the menu ([MacRumors, 2022](https://www.macrumors.com/2022/08/10/instagram-tracking-users-in-app-browser)). I did not confirm current behavior. | B, **[stale risk]** |
| Does Umami still count visits? | Probably yes. Umami records through its own script; I found no source saying otherwise. Test it. Visits can still be lost to ad blockers and tracking prevention in the webview (inference). | inference |
| Does a `data:` "Add to my calendar" download work? | **Unknown, and the evidence leans no.** Our checklist builds the invite as `data:text/calendar` with the `download` attribute ([entry.js](../../../products/landing/assets/entry.js) line 331). Reports: a ManyChat forum thread says that in the Instagram browser "the download does not start" for a calendar entry and recommends a redirect ([forum](https://community.manychat.com/general-q-a-43/dm-automation-event-calendar-entry-download-not-possible-8066), D); an older Stack Overflow question reports `data:text/calendar` failing on iPhone ([thread](https://kiwix.lema.org/stackoverflow.com_en_all_2023-11/questions/15439922/data-uri-for-ical-does-not-work-on-android-or-iphone), D); Apple developer forums say deep links and app handoffs often fail in Instagram's browser (D). No official Meta or Apple statement found. | D |
| Does the Google Calendar link work? | Unknown. It is a normal `https` link, so it likely opens, but whether it hands off to the Calendar app or asks for a login inside the webview is untested. | untested |
| Does Apple Pay or Google Pay show up? | Reports say Apple Pay often does not in Meta's iOS in-app browser, while Stripe and Paddle hosted checkouts work ([Dodo feature thread](https://dodopayments.featurebase.app/p/apple-pay-support-in-meta-facebook-instagram-in-app-browser), [Square community](https://community.squareup.com/t5/Community-Corner/No-Apple-Pay-on-checkout-links/m-p/213239/highlight/true)). Not relevant for the free flow; matters later when a paid offer exists. | D |
| Does print work? | Untested. `window.print()` is often unsupported in webviews (inference). | untested |

**What to do before any traffic.** Have the bot (or a person) run the whole flow on a real iPhone and a real Android phone, opening the link from Instagram (bio, Story, ad preview): landing, start now, pick a time, add to calendar (both buttons), print, finish. If the calendar fails, the fix is cheap: detect "Instagram" in the user agent and show one line, "For the calendar button, tap the three dots and choose Open in browser," before the pick-a-time screen. This is an engineering suggestion from me, not something I could test here.

**How the data will reveal the problem anyway.** Compare `calendar-added` ÷ `time-picked` for `ig-*` tags against `qr-*` tags. A big gap means the in-app browser is eating the step. Note this is exactly the step the deferred-win design (ADR-021) rests on, and Instagram is a "not home yet" audience: people scroll while commuting, in class or in bed. Expect more `not-right-now` than from fliers.

### What Umami can and cannot see

Can: landing page views by `from` tag, events by tag, `finished` by tag and by `path` (now or appointment). Cannot: people (we keep no profiles; a repeat finisher counts twice, as lifecycle 04 notes), impressions, views, profile visits, or ad spend. Those live in Instagram Insights and Meta Ads Manager. Hobby plan keeps six months of history; write the monthly scorecard before data ages out ([operations.md](../../../planning/operations.md)).

### Minimal measurement table

| Step | Where to read it | Read as |
|---|---|---|
| Impressions or reach | Instagram Insights, Ads Manager | Count |
| 3-second views and View Rate | Instagram Insights (View Rate is the share who keep watching after 3 seconds, per Instagram) | Percent per post |
| Profile visits | Instagram Insights | Count |
| Link taps | Ads Manager (link clicks) for ads; DM tool for keyword links; none per link for the bio | Count; the bio link is read from Umami |
| Landing visits | Umami, page views by `from` tag | Count. Compare with Ads Manager link clicks; the gap shows webview losses. |
| `start-now` | Umami | Count and share of landing visits |
| `time-picked` | Umami | Count; check `calendar-added` against it |
| `finished` | Umami, by `from` and `path` | **North star** |
| Cost per finished checklist | Ads Manager spend ÷ Umami `finished` for the ad tags | Dollars |
| Email signups from the finish page | MailerLite, by route | Count (second measure) |

---

## 6. Compliance and trust

| Topic | What applies | Source | Grade |
|---|---|---|---|
| **AI disclosure** | Meta adds an "AI info" label when people disclose AI-generated content or when industry-standard indicators are detected; content only edited by AI gets a less prominent label. On Aug 31, 2026 Instagram renamed "AI creator" to "AI-generated profile" and said undisclosed AI-generated people can lose reach; the label is not required for editing photos, polishing captions or making graphics. Our Remotion videos need neither. If we later add an AI voiceover, disclose it in the post settings and keep it out of anything that implies a real person is speaking. | [Meta, Apr 5, 2024, updated Oct 23, 2025](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/); [TechCrunch, Aug 31, 2026](https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/) | A / B, **[stale risk]** |
| **Music** | Instagram's help center says licensed music may be unavailable for some business accounts and for some account types or regions, and points to the Meta Sound Collection as the fallback; a Meta business page covers access to the licensed library. The page bodies did not load for me, so this comes from search summaries. Safest: a voiceover we record or license, or a Sound Collection track. Do not use trending audio on a business account. Check in-app, and check again for ads (ads use royalty-free audio from the Sound Collection). | [Meta Business Help](https://www.facebook.com/business/help/402084904469945); [Instagram Help](https://help.instagram.com/1612770602842742) | A (not fully read), **[stale risk]** |
| **FTC endorsements and testimonials** | The Consumer Reviews and Testimonials Rule has been in effect since October 21, 2024 and allows civil penalties for knowing violations. The FTC says it "has no blanket prohibition on the use of AI-generated avatars," but fake or false testimonials are prohibited, and using actors to portray testimonialists "could still be deceptive." Testimonials can appear "in social media." We have none and will not invent any. | [FTC Q&A](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers) | A |
| **Disclosure of paid endorsement** | Not applicable yet: we pay no one and receive no affiliate commission in these videos. If a creator shares us for pay or for a commission, Instagram's paid-partnership label and the FTC disclosure apply. [commerce-rules.md](../../business/commerce-rules.md) already requires disclosure beside affiliate links. | [Instagram branded content help](https://help.instagram.com/616901995832907) (via search) | A (not fully read) |
| **What we never claim in these videos** | No fake users or fake messages ("Sam did this in 30 minutes"). No invented numbers: do not say "thousands of people," "most people finish," or a completion rate. Time claims must match the checklist behind them; the workflow files flag several time estimates as unverified, so time one checklist before showing "about an hour" in an ad. No countdowns or scarcity: nothing here is scarce. No implied sponsorship: colors only, no school or branch names, logos or ranks (ADR-023). No claims about outcomes beyond the task ("a clear table to eat at"). The ad and the page must say the checklist is free and needs no email, and that has to stay true on the page. | Repo rules; Meta Ad Standards | n/a |
| **Dignity** | Name the situation, never the person. No mention of feelings or conditions. Nothing aimed at under 18. | [content/README.md](../../../content/README.md); Meta personal attributes policy | n/a |

---

## 7. What comparable free-resource brands do on short video

Evidence here is thin and mostly anecdotal. I found no published conversion rate from any home or life-skills creator.

| Case | What is reported | Grade |
|---|---|---|
| **KC Davis (Struggle Care)** | Built a large no-shame presence, mostly on TikTok; sells $4.99 to $14.99 guides, plus a book. Details in [lifecycle 02](../lifecycle/02-emails-and-first-purchase.md). No conversion data is public. | C/D |
| **Clean That Up** (cleaning creator) | One trade article reports 4 million followers across platforms and $300,000 in sales and 70 million views for a spring-cleaning product in 2025. I could not retrieve the article (503), so I cannot confirm the source or what share came from Reels. | D |
| **A cleaning coach reporting 20 paid members from one Instagram Story ad** | Steady newsletter post, first-hand and anecdotal; about 11,000 followers. | D |
| **The Organized by Nadine** | A ManyChat case study of a professional organizer using comment-to-DM automation. The page returned 403, so no figures retrieved; it is vendor material. | D |
| **Kajabi seller data** | Across 600,000 digital products sold on Kajabi, products under $25 are 14.8% of the catalog and produce 3.5% of seller earnings; the median under-$25 product earns $96 over its lifetime. Experts whose catalog never exceeds $50 have a median lifetime earnings of $178. Kajabi says this is correlation and that it has a commercial interest. | [Kajabi](https://www.kajabi.com/blog/what-experts-actually-charge), C |
| **Gumroad creator income** | Median creator earned $70 in 2020; top 1% earned about 60% of money (summarized in lifecycle 02). | C |

**Typical path to a purchase when the product is free first** (from lifecycle 02, not repeated here): a free doing-program or printable, an email signup, a $5 to $15 single-issue guide, then a larger course. Every home-care creator in that research follows this shape; none publishes conversion. Social is the top of that path, not the payment step. The honest read: the creators who sell a lot have large audiences built over years, and their money concentrates in books and courses.

---

## 8. Our existing hooks and video text: critique and improved variants

### Critique of what we have (from [copy.ts](../../../video/src/copy.ts), [Promo.tsx](../../../video/src/Promo.tsx), and the rendered files)

Reading time uses the 238 words-per-minute average for adult silent reading of non-fiction in English ([Brysbaert 2019 meta-analysis of 190 studies, summarized by the BPS](https://www.bps.org.uk/research-digest/most-comprehensive-review-date-finds-average-persons-reading-speed-slower), grade A). Cold viewers scrolling at speed read slower than people reading for comprehension, so these are minimums.

| What | Problem | Evidence or reasoning | Fix |
|---|---|---|---|
| **Hook is a question about who you are** ("Living on your own for the first time?") | The viewer has to decide whether it applies to them, then wait to learn what we want. It does not name a problem they have right now. It also fails our own act-now filter (question 2: is it about now). | Instagram asks for a hook that "compels people to stick around"; a specific situation does that better than an identity (inference; no controlled test found). Meta's personal-attributes policy discourages "you" questions about who someone is. | Open with the situation and a command. |
| **Career hook is 12 words** (3.0 seconds of reading) | The hook scene lasts 3.3 seconds, and words arrive one at a time starting at frame 6 and every 4 frames. The last of 12 words lands at about 1.7 seconds; the viewer finishes reading at the end of the scene. | Calculation. | Keep hooks under 8 words. |
| **Frame 0 shows no hook text** | The hook begins at frame 6 and builds word by word; the first frame (and any thumbnail) is a background and a small label. | [Promo.tsx](../../../video/src/Promo.tsx) line 203. | Show the full hook at frame 0, then animate the next beat. |
| **Student problem 1 is 18 words** (4.5 seconds) | Each problem scene lasts 3.3 seconds. The three-in-one sentence (dishes, floor, mail) cannot be read in time. | Calculation. | One problem per scene, 8 words or fewer. |
| **"Sound like your place?"** | It asks the viewer to agree, not to act. The act-now filter (question 3) says a nod without an action is a hook without a result. | [content/README.md](../../../content/README.md). | Replace with a next step and a time. |
| **The end card shows only the address** | Nothing says what to tap or where; the link is in the bio or an ad button, not on screen. The address appears at about 1.7 seconds into a 4-second scene. | Promo.tsx lines 386 to 420. | Add a verb and the place: "Tap the link in my bio." |
| **No audio, and nearly all text** | Instagram lists muted and majority-text reels as less visible (2023). | [Mosseri, 2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained) | Add audio and one real-footage shot. |
| **The phone mock shows "Saturday at 10:00 a.m."** | Fine as an example, but it reads as a promise. | Honesty rule. | Label it "Example" or show the real picker. |
| **Dishes and mail line mixes problems** | The student, career and military problem lines sound true and kind; the military box 2 ("Nobody inspects your place anymore") is flagged by reviewers as possibly blunt ([workflow-wording.md](../../copy/workflow-wording.md)). | Review notes. | Test it, do not assume it. |

What the existing copy gets right: the tone is plain, no shaming, and "A free checklist. No app to download. No email needed." is true and specific.

### Evidence for what makes people stop and act (strength labeled)

| Idea | Evidence | Strength |
|---|---|---|
| Hook inside 3 seconds and hold watch-through | Instagram's own guidance | A |
| A command with a concrete object and a time ("Clear your table in about 10 minutes") | Specific, small first steps and visible progress raise follow-through: endowed progress (34% vs 19% completion) and the goal gradient, covered in [lifecycle 01](../lifecycle/01-acquisition-and-first-win.md); date-and-time plans (Milkman 2011), in [deferred-win.md](../deferred-win.md) | A, but from other settings; inference for video |
| Assertive commands work when the person already cares about the issue and backfire when they do not | [Kronrod, Grinstein & Wathieu 2012, *Journal of Marketing* 76(1)](https://research.vu.nl/en/publications/go-green-should-environmental-messages-be-so-assertive/): assertive messages persuaded more when the issue felt important and less when it did not (abstract; full text not retrieved). A companion paper in the *Journal of Consumer Research* found assertive wording works better for pleasure-oriented products. | A (peer-reviewed), but for environmental messages and ad text, not video |
| "Pattern interrupt" and curiosity-gap hooks | Vendor and creator blogs only; no peer-reviewed or platform data found | D |
| Time-bound "tonight" prompts | Plausible given implementation intentions research; no direct short-video test found | inference |
| Our own tag data | The only evidence that will matter | n/a |

Implication for our voice: commands are fine when the viewer is already in the situation ("People are coming over tonight"), which is why the "tonight" lines are the best test. The directive voice does not need "get off your ass" language; the brand's own signature, a plain command with an object, is both on-brand and supported better.

### Improved variants (3 to 4 per audience)

Rules applied: plain speech, every verb with its object, about right now, nothing about feelings or the viewer's character, no unverified numbers (times come from the workflow files, flagged for timing). Format per variant: **first 3 seconds** (shown at frame 0), then **second beat**, then **end card**. The end card for organic is "Free checklist. Tap the link in my bio." For ads, "Free checklist. Tap Learn more." These are drafts for the copy review, not final wording.

**Students**

| # | First 3 seconds | Second beat | Task page |
|---|---|---|---|
| S1 | People are coming over tonight. | Do these six things first. It takes about an hour. | Company ([workflow 2](../../copy/workflows/02-guests.md)) |
| S2 | Clear your table in about 10 minutes. | Six steps. Step one: throw away the trash on the table. | Table ([workflow 3](../../copy/workflows/03-dinner.md)) |
| S3 | Wash the dishes first. | Then pick up your main room. Then make your bed. Six steps, about an hour and a half. | Dishes and mess ([workflow 1](../../copy/workflows/01-underwater.md)) |
| S4 (August, January, first two weeks of a term) | Tonight is your first night in your new place. | Take photos of every room before you unpack more. | First night ([workflow 4](../../copy/workflows/04-first-night.md)) |

**Career**

| # | First 3 seconds | Second beat | Task page |
|---|---|---|---|
| C1 | It's late, and the dishes are still in the sink. | Wash them and wipe the kitchen. That is step one of six. About an hour and a half in all. | Dishes and mess |
| C2 | Someone's coming over tonight. | Six things, about an hour. Start with the kitchen trash and open a window. | Company |
| C3 | Eat at your table tonight. | Clear it in about 10 minutes. Six steps. | Table |
| C4 (moved for a job) | Tonight is your first night in your new place. | Take photos of every room before you unpack more. | First night |

**Military**

| # | First 3 seconds | Second beat | Task page |
|---|---|---|---|
| M1 | Your household goods aren't here yet. | Do these six things tonight. About an hour and a half. | First night |
| M2 | People from your unit are coming over tonight. | Get your place ready in about an hour. Six steps. | Company |
| M3 | Your spare room is full of boxes. | Start with one shelf or one box. Set aside about three hours. | Spare room ([workflow 5](../../copy/workflows/05-one-room.md)) |
| M4 (flagged for reviewers) | Nobody inspects your place anymore. | Get it squared away in about an hour and a half. | Dishes and mess |

**Notes.** The times are the workflow files' estimates. [workflow-wording.md](../../copy/workflow-wording.md) says they should be timed by a reviewer; do that before paying to show "about an hour." The table task (10 minutes) is the smallest ask and the best candidate for a first tap from someone scrolling at home. M4 is deliberately the line reviewers questioned; test it only if reviewers approve it. All variants avoid asking "Are you...?" and avoid feelings.

---

## 9. Funnel math

All figures are planning assumptions. Where a rate has a source it is cited; otherwise it is a **guess**. They will be wrong; the point is the order of magnitude.

### Assumptions

| Step | Rate | Source |
|---|---|---|
| Organic: view to profile visit | 1% (range 0.3% to 2%) | Guess. No reliable benchmark found. |
| Organic: profile visit to link tap | 3% (range 2% to 6%) | Vendor claim, D |
| Organic via comment-a-word: comment rate, then DM link click | 0.2% of views comment (guess); 15% click the DM link | Comment rate guess; click rate vendor claim, D |
| Paid: link CTR | 1.18% | Databox median via [Superscale](https://superscale.ai/learn/meta-ads-benchmarks-by-industry/), C |
| Paid: cost per 1,000 impressions | $14 | Roundup, C (implies $1.19 per click) |
| Link click to landing visit | 80% | Guess (in-app browser and slow loads lose some) |
| Landing visit to start-now or time-picked | 30% | Guess. No baseline in Umami yet. |
| Started to finished | 37% | Guess, anchored on "about half of intentions never become action" ([deferred-win.md](../deferred-win.md)) and low completion of self-guided programs ([lifecycle 01](../lifecycle/01-acquisition-and-first-win.md)) |
| Finisher to email signup | 15% | Guess |
| Email subscriber to $9 guide buyer | 3% | Software-freemium 2% to 5%, weak transfer ([lifecycle 02](../lifecycle/02-emails-and-first-purchase.md)) |

### Organic (bare bio link)

| Views | Profile visits | Link taps | Landing visits | Starts | Finished | Emails |
|---|---|---|---|---|---|---|
| 100 | 1 | 0.03 | 0.02 | 0 | 0 | 0 |
| 1,000 | 10 | 0.3 | 0.2 | 0.07 | 0.03 | 0 |
| 10,000 | 100 | 3 | 2.4 | 0.7 | 0.3 | 0.04 |

With a comment-a-word DM link, 10,000 views gives about 20 comments and about 3 DM link clicks, so roughly 2 landing visits, about 0.3 finished. In both cases 10,000 views is about one finished checklist or fewer. If the true rates are twice as good it is still two. That is the honest picture of organic from a bare account: it can show whether people react, not move a business.

### Paid (per impressions)

| Impressions | Cost at $14 CPM | Link clicks | Landing visits | Starts | Finished | Cost per finished |
|---|---|---|---|---|---|---|
| 1,000 | $14 | 11.8 | 9.4 | 2.8 | 1.0 | about $13 |
| 10,000 | $140 | 118 | 94 | 28 | 10 | about $13 |
| 100,000 | $1,400 | 1,180 | 944 | 283 | 105 | about $13 |

The plausible range is a factor of 2 either way, so $7 to $27 per finished checklist. The sensitive inputs are the 30% start rate and 37% finish rate, which have no data behind them yet. Our first Umami numbers replace them.

### What it earns

1,000 finished checklists, 150 email signups, about 4 or 5 $9-guide buyers, about $40 of revenue. At $13 per finish, that traffic costs about $13,000. **Cold paid social cannot pay for itself on a $9 guide at these rates.** Even at 10% of subscribers buying, revenue is about $135. This is a values-and-learning spend, not an ROI spend.

### Sample size: how many do we need?

Sample sizes per arm for a two-sided test at 5% significance and 80% power (my own calculation, standard two-proportion formula):

| Comparison | Per arm | Both arms |
|---|---|---|
| 2% vs 5% | 588 | 1,176 |
| 1% vs 3% | 769 | 1,538 |
| 2% vs 4% | 1,141 | 2,282 |
| 10% vs 20% | 199 | 398 |
| 10% vs 30% | 62 | 124 |
| 20% vs 40% | 82 | 164 |
| 15% vs 30% | 121 | 242 |

Single-arm uncertainty (95% Wilson interval): 5 of 100 is 2.2% to 11.2%; 15 of 300 is 3.1% to 8.1%; 25 of 500 is 3.4% to 7.3%. If zero of 100 click through, the rate could still be as high as about 3.7% (the "rule of three" gives 3/n). So at about 60 to 120 clicks per campaign, we can see only large differences, and we should read counts, not rates, as lifecycle 04 says.

---

## 10. Four-week test plan, two campaigns

### 10.1 What the two campaigns are

**One question, one variable.** Both campaigns use the improved existing videos, the same audience, the same budget and the same landing flow. They differ only in **the hook angle**:

- **Campaign A, "Tonight":** a time-bound, specific event. Hooks S1 and S2 (or C2 and C3, or M2). Opens the company or table checklist.
- **Campaign B, "The mess":** the sink, the boxes, the first night. Hooks S3 and S4 (or C1 and C4, or M1 and M3). Opens the dishes, first-night or spare-room checklist.

Why this pair: it is the most informative thing we can learn and reuses existing copy. The alternative, video versus a static image (the launch kit's default), is a good second test once a hook angle is working, because format effects are smaller than topic effects and this budget cannot separate them. Pick **one audience** for the paid weeks; run the other two audiences organically. Default: students (18 to 24), since the launch kit and the audience tracker put them first, unless weeks 1 and 2 clearly favor career.

### 10.2 Schedule

| Week | What | Cost |
|---|---|---|
| **0 (before day 1, 3 to 5 days)** | Open the account (section 4). Time one checklist. Render the improved videos with audio and a first real-footage shot. Run the in-app browser tests on a real iPhone and Android phone (section 5). Post six to eight starter items. | $0 |
| **1** | Organic: 4 Reels (one per audience plus one extra for the lead audience), 3 static posts, 3 Stories with link stickers if available. Link-in-bio tag `ig-<aud>-bio-main`. Trial reels to test hooks on non-followers if available. | $0 |
| **2** | Organic: 4 more Reels, same cadence. Add the comment-a-word DM on one post per audience, with a per-post tag. Read Account Status. Read first Umami numbers. | $0 |
| **3 and 4** | Paid: $10 per day for 14 days, split $5 per day per campaign, **Traffic objective, link clicks, Reels and Stories placements, one audience, minimum age 18 hard**. Keep posting organically (about 3 per week). Do not edit the ads mid-flight except to stop a failing one (edits reset learning). | $140; hard cap $200 |

**Cadence.** Three to five organic posts a week (launch kit suggests two per week as a start; my suggestion is slightly higher for Reels because reach is initial-audience driven). This is an operating choice, not a claim about the best frequency.

### 10.3 Measurement

Read weekly: the table in section 5. Primary success measure is **`finished` events by tag** (north star), then **cost per finished checklist** for paid, then email signups from the finish page. Sales are measured separately and later. Guardrails (from lifecycle 04): unsubscribes and complaints at or below the sequence baseline; the `start-now` share among fork choices does not fall; Account Status stays clean.

### 10.4 Decision rules

Thresholds are our own planning numbers, not benchmarks. Revisit them with real data.

| When | Observation | Decision |
|---|---|---|
| **Before week 3** | In-app browser test fails (calendar, start, or counting) | Fix first; do not spend. |
| | Account Status shows an issue, or first ads are rejected twice | Stop; read the policy page for the cited reason; do not appeal by rewording the same hook. |
| **After about $50 of spend** (about 3,500 impressions) | Link CTR below 0.4% (about a third of the 1.18% median) | The creative or hook is the problem. Replace the weaker campaign's hook with the next variant from section 8. |
| | Link CTR 0.8% or higher in either campaign | Continue. |
| **After $140** | 10 or more total finishes, and cost per finish $25 or less | Continue for four more weeks; move the budget toward the campaign with higher CTR *and* any finishes. |
| | 3 to 9 finishes | Do not scale. Fix the landing flow (check the in-app calendar gap, start rate, finish rate) before more spend. |
| | Fewer than 3 finishes, with 100 or more landing visits | Stop paid. The ad is attracting taps but not finishers (the lifecycle 04 guardrail); go back to organic and fix the page promise. |
| | Fewer than 40 landing visits | The test could not run; the ad or the page is not working. Fix delivery first. |
| **Comparing A and B** | One campaign has at least twice the other's link CTR over 3,000 or more impressions each | Call it for click rate. |
| | Differences smaller than that | Call it a tie. Do not read finish rates; with about 10 finishes in total they are noise (section 9). |
| **Organic, end of week 2** | Fewer than about 3 landing visits from Instagram in total | Expected for a new account; do not conclude the format failed. Look at View Rate and sends per post instead. |
| | View Rate under about 30% on most Reels (a guess) | Hooks are not holding; test variants with trial reels. |
| **Sales** | None expected | Do not judge this test on sales. Note email signups per finish as the bridge to the later paid offer. |

### 10.5 A short note on direct sales ($9 from Instagram)

Not designed or recommended for this test, per Charles's decision. For the record, what the evidence says: there is no reliable public conversion rate for a $9 impulse purchase from a cold Instagram tap. Vendor figures for cold social traffic run 1.2% to 2.0% for stores and 2% to 3% for digital products (grade D, from search summaries). The $9, $27, $37 pattern: Kajabi reports that its expert sellers' prices cluster on 7 and 9 endings ($27, $47, $97), covering more than 600,000 digital products ([Kajabi](https://www.kajabi.com/blog/what-experts-actually-charge), C). That describes what sellers charge, not what converts; I found no test tying those price points to conversion. The only controlled evidence nearby is Anderson and Simester's field experiments, where a $9 ending raised demand, more for new items and less with "Sale" cues ([2003](https://ideas.repec.org/a/kap/qmktec/v1y2003i1p93-110.html), grade A, catalog clothing). I found no reliable refund rate for low-price digital guides; the numbers online are unsourced. Mobile checkout in Instagram's browser has reported friction with Apple Pay (section 5). Two repo issues: ADR-020 offers a paid guide only after a finished free win, and a paid product must be genuinely more than the free checklist, so any positioning must not suggest the free checklist is lesser or incomplete. If Charles later reconsiders, that is a separate decision.

### 10.6 Realistic expectations

- **Likely result:** the organic weeks bring a few dozen views per Reel to a few hundred, a handful of profile visits, and zero to a few landing visits. Paid brings about 120 clicks and about 10 finished checklists, with a cost per finish somewhere from $7 to $27 or worse.
- **A good outcome** is not volume. It is learning that the in-app flow works, that strangers do finish a checklist, and which hook angle gets taps.
- **Sales from cold social at our scale:** unlikely. The realistic win is clicks and finished checklists that feed the email list, with the bigger lever staying the person-to-person channels that lifecycle 01 found stronger than any feed.

### 10.7 The three biggest risks

1. **Attention is the bottleneck, and our format starts at a disadvantage.** A zero-follower account, muted, majority-text videos, and a hook that asks who you are. Mitigation: audio, a real-footage first shot, situation hooks, trial reels.
2. **Friction and intent mismatch after the tap.** The in-app browser may break the calendar step, the viewer is scrolling and often not at home (so more "not right now"), and our funnel assumes a calendar button works. Mitigation: test on real phones, add an "open in browser" line, read `calendar-added` ÷ `time-picked` by tag.
3. **Small-number misreading and policy flags.** About 10 finishes cannot rank hooks, and a rejected ad or a flagged account can end the test. Mitigation: read counts not rates, decide only on large differences, keep copy to the situation and the object, never the person.

---

## 11. Cross-posting and reuse

| Topic | Instagram Reels | TikTok | YouTube Shorts |
|---|---|---|---|
| Same file | Yes. Render from Remotion with no watermark; do not re-upload a file saved from another app. | Yes | Yes |
| Links | Bio, Story sticker, ad button, DM. No clickable caption or comment links (D). | A website link needs 1,000 followers or a registered business account, and rules vary by region ([Buffer](https://buffer.com/library/how-to-put-a-link-in-tiktok-bio/), C) | Links in Shorts comments and descriptions stopped being clickable around August 31, 2023; a channel page link is the route ([Malwarebytes, Aug 2023](https://www.malwarebytes.com/blog/news/2023/08/youtube-makes-sweeping-changes-to-tackle-spam-on-shorts-videos), B/C) |
| Safe zones | Our files keep text out of the top 230 px and bottom 430 px ([video/README.md](../../../video/README.md)). I have not verified current UI overlays for any app; preview each in-app. | Same caution | Same caution |
| Ads | Meta Ads Manager (section 3) | TikTok ads exist; I did not research them | Google Ads video; I did not research them |
| Music | Meta Sound Collection or our own audio | TikTok has its own commercial music rules; I did not retrieve them | YouTube has its own audio library; not researched |
| Our priority | First, to use one ad system and one account | Second, only after Instagram data | Third, low effort: same file |

Staggering the posts a few days apart and varying the first scene is a cheap guard against duplicate detection (my suggestion, untested).

---

## 12. Ideas beyond what we have, ranked

| Rank | Idea | Cost | Expected effect | Evidence |
|---|---|---|---|---|
| 1 | Fix the in-app calendar step (user-agent detection, "open in browser") and test on phones | Low (engineering) | Protects the whole funnel | D that it breaks; testing is cheap |
| 2 | Show the full hook at frame 0, shorten problem lines, add a "tap" end card | Low | Better hold and more taps | Instagram's 3-second guidance (A); the rest is inference |
| 3 | Add audio and one real-footage shot (a sink, a table) | Low to medium | Avoids the "muted, majority text" disadvantage | A (2023, stale risk) |
| 4 | A "send this to someone coming over tonight" line on the end card | Low | More sends, which Instagram names as a top signal | A for the signal; no test for the prompt |
| 5 | Comment-a-word keyword with a per-post DM link | Low | Per-post attribution and likely higher click rate than a bare bio link | Vendor claim only (D); engagement-bait risk is medium-low |
| 6 | A pinned comment saying what the free checklist is and where the link lives | Low | Reduces "where is the link?" friction | D |
| 7 | A visible address on screen the whole time, in large type | Low | Helps the viewer who types it; fits lifecycle 01's trust finding | Distrust is the main scan barrier (grade B in lifecycle 01), inference for video |
| 8 | Trial reels to test hooks on non-followers first | Low | Free hook testing | Instagram says the feature exists (A) |
| 9 | Static carousel or image of the same task (launch kit style) | Low | A format comparison later | Launch kit default |
| 10 | A creator or local partner shares the checklist (a person with a close tie) | Medium | Strongest by the research in lifecycle 01 | A, from other settings |
| 11 | Meta One paid plan for in-Reel links | $14.99 a month and up (reported) | Unknown | Reported only (B/C) |

**What I would cut:** paid ads before the account has real posts and the in-app tests pass; paid to all three audiences at once; a $9-direct campaign (not in scope); the Meta pixel; Meta One; trending audio on a business account; a long list of hashtags (Instagram asks for keywords in captions, bio and content instead: [Creators blog, May 31, 2023](https://creators.instagram.com/blog/tips-for-improving-your-reach), grade A); TikTok and Shorts ads. Also cut any copy that says or implies how someone feels.

---

## Where evidence is thin (plain list)

- Faceless text-motion performance on Instagram: no good dataset.
- Zero-follower account reach: no published figure.
- Profile-visit to link-tap rate: only vendor claims.
- Reels versus Stories cost per link click: vendors disagree widely.
- Whether Instagram's in-app browser handles our `data:` calendar download: no official source, anecdotes lean no.
- Refund rates and impulse conversion for $9 digital guides: none found.
- Whether Instagram's 2023 "muted and majority text" rule still holds: no newer statement found.
- Whether imperative hooks beat other hooks in short video: no controlled study found.

## Sources

Retrieved 2026-11-12 unless noted. Pages marked "search summary" did not load as full text for me.

**A: official or peer-reviewed**

- Instagram, [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained), May 31, 2023.
- Instagram Creators, [Recommendations on Instagram](https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators), Aug 30, 2022, updated Apr 25, 2023.
- Instagram Creators, [Tips for improving your reach](https://creators.instagram.com/blog/tips-for-improving-your-reach), May 31, 2023.
- Instagram Creators, [Finding success on reels in 2025](https://creators.instagram.com/blog/the-latest-with-instagram), Jan 21, 2025.
- Instagram Creators, [Helping creators of all sizes break through](https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through), Feb 26, 2025.
- Instagram Creators, [Rewarding original creators on Instagram](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram), Apr 30, 2026; blog index at [creators.instagram.com/blog](https://creators.instagram.com/blog) (lists Aug 31, 2026 AI-profile post and Sep 15, 2026 Meta One post, whose pages I could not retrieve).
- Instagram, [Share links in Stories to everyone](https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone) (search summary; about 2021).
- Instagram Help, [About professional accounts](https://help.instagram.com/138925576505882), [Recommendations Guidelines](https://help.instagram.com/313829416281232), [Problems with audio](https://help.instagram.com/1612770602842742), [branded content](https://help.instagram.com/616901995832907) (all search summaries).
- Meta Business Help, [Access to the licensed music library](https://www.facebook.com/business/help/402084904469945) (search summary); [About learning limited](https://en-gb.facebook.com/business/help/269269737396981) (search summary).
- Meta for Developers, [Private Replies](https://developers.facebook.com/documentation/instagram-platform/private-replies) (search summary).
- Meta Transparency Center, [Privacy Violations and Personal Attributes](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/), [Health and Wellness](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/), [Prohibited Commercial Practices](https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/).
- Meta, [Our approach to labeling AI-generated content and manipulated media](https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/), Apr 5, 2024, updated Oct 23, 2025.
- FTC, [Consumer Reviews and Testimonials Rule: Questions and Answers](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers); [final rule announcement, Aug 14, 2024](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) (search summary).
- Umami, [UTM documentation](https://docs.umami.is/docs/utm).
- Brysbaert 2019, "How many words do we read per minute?", *Journal of Memory and Language*, via [BPS Research Digest](https://www.bps.org.uk/research-digest/most-comprehensive-review-date-finds-average-persons-reading-speed-slower).
- Kronrod, Grinstein & Wathieu 2012, ["Go green! Should environmental messages be so assertive?"](https://research.vu.nl/en/publications/go-green-should-environmental-messages-be-so-assertive/), *Journal of Marketing* 76(1) (abstract only).
- Anderson & Simester 2003, ["Effects of $9 price endings on retail sales"](https://ideas.repec.org/a/kap/qmktec/v1y2003i1p93-110.html), *Quantitative Marketing and Economics* 1 (abstract only).

**B: large dataset or reputable reporting of a primary event**

- Social Media Today, [Instagram shares algorithm insights, Jan 2025](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/).
- TechCrunch, [Instagram puts new limits on undisclosed AI profiles](https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/), Aug 31, 2026; Tubefilter, [Apr 30, 2026](https://tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator).
- MacRumors, [Instagram in-app browser tracking, Aug 2022](https://www.macrumors.com/2022/08/10/instagram-tracking-users-in-app-browser) (reports Felix Krause's research).
- Search Engine Land, [Meta ad targeting limits for teens](https://searchengineland.com/meta-introduces-new-ad-targeting-limits-for-teens-391259).
- Malwarebytes, [YouTube Shorts link changes, Aug 2023](https://www.malwarebytes.com/blog/news/2023/08/youtube-makes-sweeping-changes-to-tackle-spam-on-shorts-videos).

**C: vendor blog or benchmark report**

- Socialinsider, [2026 Instagram Reels benchmarks](https://www.socialinsider.io/blog/instagram-reels-benchmarks/); Quid/Rival IQ, [2026 social media benchmark report](https://www.quid.com/knowledge-hub/resource-library/blog/2026-social-media-industry-benchmark-report).
- Superscale, [Meta ads benchmarks by industry, Jul 23, 2026](https://superscale.ai/learn/meta-ads-benchmarks-by-industry/) (cites WordStream 2025, Databox July 2026, Triple Whale 2025).
- Lebesgue, [Meta ads benchmarks by industry and AOV, Sep 7, 2026](https://lebesgue.io/facebook-ads/meta-ads-benchmarks-by-industry-and-aov) (period and sample not disclosed; its CVR and CAC do not reconcile with CPC).
- AdManage, [Instagram ads cost](https://admanage.ai/blog/how-much-do-instagram-ads-cost).
- Kajabi, [What experts actually charge](https://www.kajabi.com/blog/what-experts-actually-charge) (600,000+ products, 2022 onward; commercial interest).
- Jon Loomer, [Meta ads targeting guide](https://www.jonloomer.com/meta-ads-targeting-guide/).
- Buffer, [TikTok link in bio](https://buffer.com/library/how-to-put-a-link-in-tiktok-bio/); Brandwatch, [link in bio](https://www.brandwatch.com/social-media-glossary/link-in-bio/).
- Meta One announcement as reported by [Meta (search summary)](https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/), Metricool and Net Influencer (tier prices conflict).

**D: anecdote, forum or unsourced**

- [CreatorFlow](https://creatorflow.so/blog/bio-link-vs-dm-automation-affiliate-clicks/) (link-in-bio and DM click rates).
- [ManyChat forum, calendar download in Instagram browser](https://community.manychat.com/general-q-a-43/dm-automation-event-calendar-entry-download-not-possible-8066); [Stack Overflow, data URI iCal on iPhone](https://kiwix.lema.org/stackoverflow.com_en_all_2023-11/questions/15439922/data-uri-for-ical-does-not-work-on-android-or-iphone); [Dodo Payments thread](https://dodopayments.featurebase.app/p/apple-pay-support-in-meta-facebook-instagram-in-app-browser); [Square community](https://community.squareup.com/t5/Community-Corner/No-Apple-Pay-on-checkout-links/m-p/213239/highlight/true).
- Action-block guides, e.g. [Chatplace](https://blog.chatplace.io/en/instagram-limits/).
- Creator case posts (Clean That Up, Steady newsletter, ManyChat case study): could not be retrieved or verified.
- Hook-timing blogs (1.4-second and 65% figures): no primary source; not used.

**Repo documents cited:** CLAUDE.md; content/README.md; planning/decisions.md ADR-020 to ADR-023; planning/operations.md; planning/roadmap.md; docs/business/audience-tracker.md, commerce-rules.md, product-ladder.md, willingness-to-pay-plan.md; docs/research/deferred-win.md; docs/research/lifecycle/01, 02, 04; docs/copy/README.md, social-launch-kit.md, workflow-wording.md, workflows/01 to 06; video/README.md, video/src/copy.ts, video/src/Promo.tsx; products/landing/assets/entry.js, audience.js.
