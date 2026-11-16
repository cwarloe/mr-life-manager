# Same-day shopping links for the side quest: what is honest, cheap and possible

**Researched:** 2026-11-16 (every "today" below means that date).
**For:** Charles Warloe. Feeds [`docs/copy/side-quest.md`](../../copy/side-quest.md), screen 3 ("Copy my shopping list").
**Affiliate disclosure:** I have no affiliate relationship with any retailer or program and used no affiliate links. Some sources the search tool surfaced are affiliate or blog sites (Grade C). I used them only to find leads and relied on an official page, or marked the claim unverified.
**Source grades:** A = the retailer's or regulator's own page. B = reputable press. C = blog or affiliate site. D = forum.
**Fixed rules this report is written against:** [`commerce-rules.md`](../../business/commerce-rules.md) (fewest products; no search links in the action path; never invent, infer or repair a URL; no commission on basic consumables; link availability never changes the advice) and the plain-speech rule in [`content/README.md`](../../../content/README.md).

---

## Verdict (6 lines)

1. **No account-free, affiliate-free, multi-item "add these to your cart" link exists** that we can use today. Amazon's needs an Associates tag. Instacart's needs an API key and an approval. I found no public one for Walmart or Target.
2. **Start with "Copy my shopping list"** (plain text the reader pastes into any store app) plus one "find a store near you" Google Maps link. Both work with no account, no backend and no affiliate deal, and neither goes stale on us.
3. **Search links to big retailers are possible but weaker than they look.** Only Target's pattern loaded for me. Walmart blocked my automated fetch, Amazon was flaky, and Instacart blocked a plain fetch. No retailer documents these as stable public links. They also break commerce rule "no search links in the action path," so they need Charles's explicit exception.
4. **Affiliate links do not get anything to the reader sooner.** They add tracking and a commission, nothing else. They also conflict with the commerce rule that basic consumables pay us nothing.
5. **Delivery will usually lose to a 10-minute drive.** Published timing is a one-hour window (Target), "usually within 2 hours" for pickup (Target), and "as fast as 30 minutes" for some convenience orders (Instacart). Typical non-member fees are about $10 on a basket that may cost $15 to $25.
6. **Safe wording is "check your address."** Do not promise same-day, free, fast or in stock.

---

## What I could and could not verify

- **Read directly from the retailer:** Target help pages and search page, Instacart help and developer docs, Amazon Associates policy pages and Amazon's Prime page, Walmart's affiliate FAQ and 2021 press release, Google Maps URL docs, FTC pages.
- **Walmart.com blocked every automated fetch** ("Robot or human?" page, tried on the search page, help center and Walmart+ FAQ). Walmart fee numbers below come from search-result excerpts of walmart.com help pages. They are Grade A sources I could not open in full, so I mark them **partly unverified**.
- I did not try to get around any bot block. A human in a normal browser will see what I could not.
- Not tested: DoorDash and Shipt search or cart URLs. I found fee information for both but no public link documentation.
- Apple Maps: the fetch returned only a page title, so its link format is **unverified**.

---

## 1. Search links

I fetched each URL on 2026-11-16 with the query "distilled white vinegar." None of these retailers publishes its search URL as a stable public interface. What I give is the pattern the site itself uses, with what I saw.

| Retailer | URL pattern | What I saw (2026-11-16) | Logged-out and store/ZIP | Status |
|---|---|---|---|---|
| **Target** | `https://www.target.com/s?searchTerm=distilled+white+vinegar` | Page loaded with results ("204 results," vinegar in 16, 64 and 128 oz sizes, each with "Add to cart" and shipping or pickup notes). Plain curl returned HTTP 200. | Looks usable logged out. I cannot tell which store or ZIP it assumed. | **Worked** (observed, Grade A by observation) |
| **Walmart** | `https://www.walmart.com/search?q=distilled+white+vinegar` | Automated fetch redirected to a `/blocked` page ("Robot or human? Activate and hold the button"). The block page echoed the search path, so the path is a real route. | Unknown. A person may see results; I could not. | **Unverified** |
| **Amazon** | `https://www.amazon.com/s?k=distilled+white+vinegar` | One fetch returned HTTP 503 ("Sorry! Something went wrong!"). A second plain request returned 200, but I did not read the content. | Unknown. | **Unverified, flaky** |
| **Instacart** | `https://www.instacart.com/store/s?k=distilled+white+vinegar` | Plain curl returned 403. The page-reading tool did see results grouped by store (Hy-Vee, Fareway, ALDI) with no login wall and no ZIP prompt. | It chose stores on its own, which suggests it guessed a location. How, I cannot tell. A reader in another city may see different stores or none. | **Unverified for readers** |
| **DoorDash, Shipt** | Not tested | No public link docs found. | | **Unverified** |
| **Google Maps** | `https://www.google.com/maps/search/?api=1&query=grocery+store` | Google's docs: "You don't need a Google API key to use Maps URLs." And: "If no location is specified, Google Maps attempts to find listings nearby your current location." (Grade A, developers.google.com, no date on page.) The link returned HTTP 200. | Uses the reader's device location. | **Documented** |

Two things follow. First, only Google Maps documents its link format, and it is the one that finds the nearest open store. Second, the retailer search links depend on the page choosing a store for the reader, which none of them documents.

---

## 2. One-tap cart links

| Retailer | Public multi-item cart link without an account or partner deal? | Evidence |
|---|---|---|
| **Amazon** | **No.** The old "Add to Cart form" (`/gp/aws/cart/add.html` with `ASIN.1`, `Quantity.1`) required `AssociateTag` and specific ASINs (product IDs). | The official Product Advertising API page for it now redirects (302, today) to a deprecation notice: "The Amazon Product Advertising API 5.0 (PA-API 5) has been deprecated and is being replaced by the Creators API." Old calls get "HTTP 403 Forbidden." The deprecation page does not mention cart links. I learned the form's fields from a search-result excerpt of the old page (Grade A, not read in full). Whether the URL still works with no tag is **untested and unverified**. |
| **Walmart** | **None found.** | I searched for a Walmart add-to-cart URL and found only seller-catalog docs (for marketplace sellers). Walmart's affiliate FAQ says affiliates can make text links to "anything on Walmart.com" and does not mention cart links. Unverified either way. |
| **Target** | **None found.** | Target's affiliate FAQ page returned only a heading ("Partners"), so I could not read terms. Unverified. |
| **Instacart** | **Yes, but gated.** A shopping list page matches items by name, which suits generic staples. | `POST /idp/v1/products/products_link` needs a bearer API key. `line_items` need a `name`. Docs say "SKU numbers are not a supported method" and "directing users to a specific merchant is not supported." A production key needs a screen recording of the integration and a review ("reach out within 5 business days"). Developer terms 3.7: Instacart "may approve or reject" an application "in its sole discretion." Approved partners also get an invitation to create an Impact.com affiliate account. The link opens a page where the user "selects a store," and if not logged in "they are prompted to log in or create an account." |

**Instacart's brand rules matter for our wording.** The pre-launch checklist says: do not use "Free Delivery," do not describe the relationship as a "Partner" or "Partnership," and "Do not include 'Delivery in as fast as one hour' or any other delivery speed reference." So even if Charles got a key, that button could not sit next to a same-day promise. Also, an API key must stay secret, and our site has no backend. We could make links by hand offline, but the docs say shopping list links have "no default" expiry and allow up to 365 days. How long a hand-made link would actually stay live is **unverified**.

### If we joined an affiliate or partner program anyway

| Program | To join | What it requires of us | Restrictions that bite |
|---|---|---|---|
| **Amazon Associates** | Free sign-up, but Amazon reviews the sites you list. Amazon's own review page: it "require[s] at least three" qualified sales "within the first 180 days"; personal orders do not count; "we aren't able to reassess an application once it's been rejected"; site needs "robust original content," and "You must own your website." (Grade A, Associates Central.) | Disclosure statement from the Operating Agreement, section 5: "As an Amazon Associate I earn from qualifying purchases." (Agreement updated 2025-10-15.) Disclose cookies and tracking technology in a privacy policy or otherwise. | Program Policies (updated 2026-04-14): email links only in solicited, opted-in messages, and "You will not engage in any Promotional Activities in any offline manner," which would cover **our printable PDFs**. Apps "must not host or render Amazon web pages in WebViews." Policy section 6(z) bars using Program Content to promote products sold on non-Amazon sites, which **may clash with a page that also links Walmart and Target** (I have only a summary; a person should read the full text). Prices and availability may only be shown from Amazon's own link feed or API. The Creators API (the replacement data feed) needs "at least 10 qualifying sales within the past 30 days." |
| **Walmart affiliates (Impact)** | "It is absolutely free to join." Walmart reviews each application and decides "at its discretion." Commission "up to 4% on each eligible sale." (Grade A, affiliates.walmart.com/faqs.) | Not stated on that page. | The FAQ does not say whether search links or cart links are supported, and gives no email or print rules. Unverified. |
| **Target Partners (Impact)** | Search-result excerpt of partners.target.com says any family-friendly website owner, blogger or influencer with mainly US viewership may join, free. I could not open the page. | Unknown. | Unknown. Unverified. |
| **Instacart** | See table above: API key plus a demo review. | Brand rules above. | No delivery-speed wording. |

**What the FTC requires of us if we use any affiliate link.** The FTC's endorsement Q&A (ftc.gov, undated page) says: "You should disclose your relationship to the retailer clearly and conspicuously on your site," "The closer the disclosure is to your recommendation, the better," and "'Paid link' right next to an affiliate link should be an adequate disclosure of the nature of the link." The FTC's "Disclosures 101 for Social Media Influencers" (November 2019) adds: "Place it so it's hard to miss," and warns that disclosures are "likely to be missed if they appear only on an ABOUT ME or profile page." Our own commerce rule already says the same thing (disclosure "immediately before or beside the links").

**Do affiliate links make delivery faster?** No. Walmart's FAQ says affiliates use Impact "to track sales, impressions, click-throughs, and commissions." Amazon's Associates pages describe tagged links, attribution windows (24 hours to order, cart kept "usually" up to 90 days) and commission. Instacart's checklist says approved partners get an Impact account. None of that mentions any change in stock, speed, fees or priority for the shopper. The only thing an affiliate link changes is who gets paid.

---

## 3. Same-day reality

Fees and rules published today. They change often and vary by address, so treat the numbers as "what a reader may see," not what we promise.

| Retailer | Same-day without a paid membership? | Published fee and minimum | Depends on | Source |
|---|---|---|---|---|
| **Target** | **Pickup:** yes, free. **Delivery:** yes, pay per order. | Order Pickup and Drive Up free; "usually be ready within 2 hours," and "Select stores may take up to 6 hours." Same Day Delivery: "a $9.99 delivery fee for each eligible order"; the page lists a $35 minimum next to the member offer and an EBT exception, which I read as applying to everyone else too. Delivery "can be scheduled for a one-hour window." Extra local fees in California and New York City. Circle 360 is $99 a year or $10.99 a month. | Store (Drive Up is at "select stores"), ZIP, item exclusions (for example items over 40 lbs). Target tells readers to check "by ZIP code or store." | Target help pages, A, read 2026-11-16 |
| **Walmart** | **Pickup and delivery from store:** yes, for a fee. | Via search excerpts of walmart.com help pages: delivery from store $9.95 standard (an older range says $7.95 to $9.95); $35 minimum; a small-order fee quoted as $5.99 on one page and $6.99 on another (the sources conflict); pickup free over $35; Express delivery is "$10 on top of the existing delivery charge" (Walmart press release, 2021-03-01, **stale**). Walmart+ is $98 a year or $12.95 a month per the same excerpts. | Store, ZIP, time slot. "Check your cart." | Walmart, A, **partly unverified** (site blocked automated reading) |
| **Amazon** | **Yes, at a higher fee.** | Same-Day Delivery rates page: Prime "FREE*" over the minimum; Prime under the minimum "Up to $2.99"; non-Prime "Up to $12.99 per order." The Prime page says free "for orders over $25 in most cities." Prime is $14.99 a month or $139 a year. Newer **Amazon Now** (30 minutes or less): non-Prime $13.99 per order plus $3.99 under $15, only in some cities (Digital Commerce 360, 2026-05-12, B). | ZIP and city. Not everywhere. | Amazon, A (the rates page sits on a `digprjsurvey.amazon.com` host, which is unusual; the Prime page is on aboutamazon.com) |
| **Instacart** | **Yes.** | "All orders must be at least $10." Delivery fee "varies based on the retailer, delivery window, and order total." Service fees vary. Instacart+ gives $0 delivery on $10+. Pickup has no service fee. Convenience orders "typically deliver in as fast as 30 minutes." Priority delivery "isn't always available." | Store the reader picks, ZIP, shopper availability. | Instacart help, A |
| **DoorDash** | **Yes, for a fee.** | "Delivery Fee: A fixed fee per order that varies by merchant." Service fee varies, often a percentage of the subtotal in markets not yet on the new structure. I found no grocery-specific schedule. | Merchant, distance, market. | DoorDash help, A (undated) |
| **Shipt** | **Yes, for a fee.** | Help pages (via search excerpt, not read in full): no minimum order; $10 for a one-time delivery without membership; members free over $35. Varies by market. | Market. | Shipt help, A, **partly unverified** |

**What a reader with no membership can do today.** (1) Drive to the nearest store; that is the baseline. (2) Order pickup at Target (free) or Walmart (free over $35 per the excerpt) and collect it in about two hours. (3) Pay a roughly $10 per-order delivery fee at Target, Walmart, Shipt or Amazon (up to $12.99), plus a minimum basket at some. We will not recommend any membership. Facts a reader should know: Walmart+ $98 a year, Amazon Prime $139 a year, Target Circle 360 $99 a year.

**Basket size reality (my estimate, not a published figure).** The six staples probably cost $15 to $25. Target showed 128 oz distilled white vinegar at $4.59 today. So a $9.99 delivery fee can cost about as much as half the basket, and a $35 minimum can push the reader to buy things they do not need. That conflicts with "recommend the fewest products" if we nudge toward delivery.

---

## 4. What we can honestly say on the page

**The timing problem.** The side quest is a 10-minute errand ([side-quest.md](../../copy/side-quest.md), question 4 already flags that number as a guess). Every published delivery or pickup time is longer than a 10-minute drive: a one-hour window (Target), "usually within 2 hours" and up to 6 (Target pickup), 30 minutes only for some convenience orders (Instacart) or in some cities (Amazon Now). Delivery helps the reader with no car, no time tonight, or a store that is far away. It does not help the typical reader finish sooner. The side quest also adds its own calendar entry before the main time, so a delivery that arrives before that entry still works.

| Safe (we can back it) | Not safe (we cannot back it) |
|---|---|
| "Many stores will bring these to you or hold them for pickup. Fees and minimums apply, and it depends on your address." | "Same-day delivery." "Free delivery." "Delivered in an hour." (We cannot know any reader's address, stock or fee.) |
| "Check your address in the store's app." | "Available near you." "In stock." "Walmart/Target/Amazon has all of these." |
| "Any grocery or dollar store has these." (Already in draft screen 3.) | A price, a total, or "cheaper at X." |
| "Copy the list and paste it into any store's app or search box." | "No account needed." (Instacart's docs say a logged-out user is "prompted to log in or create an account." I did not verify guest checkout at Walmart, Target or Amazon.) |
| "Some stores charge for delivery. Pickup can be cheaper." (Supported by Target's page.) | Any Instacart-style speed claim next to an Instacart link. Instacart's partner rules forbid it. |

Plain-speech draft for screen 3 (not final; goes through copy review):
> **Can't get to a store? Many stores will bring these to you or hold them for pickup.** It depends on your address, and some charge a fee. Copy your list and paste it into any store's app.

---

## 5. Our options, ranked

| Rank | Option | Effort | What could break | Commerce-rules fit | Gets items sooner? |
|---|---|---|---|---|---|
| **1** | **(a) "Copy my shopping list"** (plain text, six generic items, unticked ones only) plus an optional "Find a store near you" Google Maps link | Small: one button, clipboard code, one documented link | Almost nothing. The clipboard needs a secure page (GitHub Pages is HTTPS) and a tap; add a "select the list" fallback. The Maps URL is documented. | **Fits.** No product URL, no affiliate, no brand, no claim about stock. Matches rule "tell them to grab the simplest option locally." | Yes for readers who drive: Maps shows the nearest open store. For delivery readers it saves retyping six items in an app. |
| **2** | **(b) Search links, three retailers** (Target, Walmart, Amazon), non-affiliate | Small to build; ongoing checks | Each pattern is undocumented. Walmart and Amazon could not be verified by me. Results depend on a store or ZIP the reader may not have set. | **Needs an exception.** Link rule 2 says "No search links in the action path." Rule 10 says never "infer" a URL, and a search URL is inferred from the site's behavior. Also "Never claim a one-click bundle exists." Fine as a labeled "search for it" helper, not as "click here, done." | Only if the reader already has the store app or a saved address, and then only for pickup or delivery, which is slower than driving. |
| **3** | **(c) One-tap cart link per retailer** | Large, and mostly blocked | Amazon form needs a tag and product IDs and the old doc is gone. Instacart needs a key, a review, and a backend or offline generation. Walmart and Target: none found. | **Conflicts.** Needs exact product URLs (rule 10), exact-product verification, brand picks (rules 3, 10), and "never claim a one-click bundle exists unless the retailer actually supports it." | Slightly, if it worked. No evidence it does for the six generic items without picking brands. |
| **4** | **(d) Affiliate versions of (b) or (c)** | Largest: applications, disclosure, tracking, ongoing policy compliance | Amazon account can be refused with no appeal; policies bar offline use (printables) and may bar mixed-retailer pages; Walmart and Target terms unverified. | **Conflicts.** "Take no commission on basic consumables" (Monetization rule 2). Search or category affiliate links break link rule 1 ("exact product named"). Commission "may never override" shopper value. | **No.** The programs provide tracking and commission only. |

**Recommended first step: option 1 only.** Ship "Copy my shopping list" and the Maps link. It answers Charles's ask ("click to get the staples fast") in the way that actually is fastest and works for everyone, and it needs no promise we cannot keep.

**What I would add second, only if Charles wants a clickable store.** A small "search on" row for Target, then Walmart and Amazon after a human confirms each in a normal browser, labeled as a convenience and not an action-path button, with Charles recording an exception to link rule 2 in the commerce rules. Wording stays "check your address."

**What I would cut.** Cart links (nothing usable without an account, key or tag). Affiliate links of any kind (they do not speed anything, and they violate our own consumables rule). Any price, fee, speed or "free" wording. Any membership mention beyond neutral facts if the page ever carries them.

**Note on Instacart.** It is the only one where a link can carry a generic list with no brands, which is exactly our need. The gates (API key, review, no speed wording, backend) put it out of reach for now. If Charles later wants a fast revisit, the first step would be to ask Instacart about developer access, not to build anything.

---

## 6. Stale-link maintenance

**How fast these change.** I cannot give a measured rate. Evidence of drift, all seen today: Amazon's official add-to-cart doc now redirects to a deprecation notice; Instacart's developer terms show two different dates ("Last Updated: July 3, 2024" and "Last updated on Oct 14, 2026"); Walmart's help pages quote delivery fees that disagree with each other (small-order fee $5.99 on one page, $6.99 on another); Amazon's 503 then 200 on the same URL. So expect search-URL patterns to hold for a long time but fees, minimums and programs to move without notice. Keeping fee numbers off the page removes most of the maintenance.

**Re-check plan** (matches the cadence already in commerce rules: weekly automated, quarterly human):
1. **Weekly, in CI:** run the script below against the list of links. A plain 200 check is not enough, because Walmart answered 200 with a bot-wall page, so the script also looks for wall text and treats 403, 429 and 503 as UNKNOWN (a warning for a human), not as dead.
2. **Quarterly, by a person in a normal browser:** open each link on a phone and a laptop. Does it show results? Does it ask for a store or ZIP? Does the wording on our page ("check your address") still match what the retailer shows? Re-read the fee pages and retire any claim that changed.
3. **When a link breaks, pull it** (commerce rule) and keep the list and the Maps link, which do not depend on it.
4. Record each link with retailer, URL, date checked and how it was checked, in the same source-of-truth file the commerce rules already require.

**Script** (tested today on four URLs, standard library only, honest user agent, does not try to evade bot walls). Today's run: Target OK; Walmart UNKNOWN (bot wall); Amazon OK (200, content not inspected); Google Maps OK.

```python
#!/usr/bin/env python3
"""Re-check shopping links. Usage: python3 check_shop_links.py links.txt
links.txt: one URL per line. Exit 1 if any link is BROKEN. UNKNOWN (bot wall) needs a human look."""
import sys, urllib.request, urllib.error

UA = "MrLifeManagerLinkCheck/1.0 (+https://mrlifemanager.com)"
WALL = ("robot or human", "captcha", "/blocked", "access denied", "something went wrong")

def check(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(200000).decode("utf-8", "ignore").lower()
            final = r.geturl().lower()
            if any(w in final or w in body[:5000] for w in WALL):
                return "UNKNOWN", f"{r.status} but looks like a bot wall at {r.geturl()}"
            return "OK", str(r.status)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429, 503):
            return "UNKNOWN", f"HTTP {e.code} (often a bot block, not a dead link)"
        return "BROKEN", f"HTTP {e.code}"
    except Exception as e:
        return "BROKEN", repr(e)

bad = 0
for line in open(sys.argv[1]):
    url = line.strip()
    if not url or url.startswith("#"):
        continue
    status, note = check(url)
    bad += status == "BROKEN"
    print(f"{status:8} {url}  {note}")
sys.exit(1 if bad else 0)
```

**Limit of the script.** It proves a page loads, not that it shows search results for our item or the reader's store. Only the quarterly human check proves that. Retailers may also block GitHub's runner addresses more often than my session's; I did not test that, so expect some UNKNOWN results.

---

## Open questions for Charles

1. **Is a Maps link to "grocery store" or "dollar store" acceptable as the clickable part,** given link rule 2 (no search links in the action path)? It searches for a place, not a product, but it is still a search.
2. **Do you want to write an exception to link rule 2** before any retailer search link ships?
3. **Printable PDFs:** if affiliate links are ever added, Amazon's policy bars offline promotion. The printables would need to stay link-free. Unverified beyond the policy excerpt; a person should read the full text before any application.

---

## Sources (retrieved 2026-11-16 unless noted)

**A, retailer or regulator pages read directly**
- Target, Same Day Delivery help: https://www.target.com/help/articles/delivery-options/same-day-delivery
- Target, Drive Up and Order Pickup help: https://www.target.com/help/articles/delivery-options/drive-up-order-pickup
- Target search page (observed): https://www.target.com/s?searchTerm=distilled+white+vinegar
- Instacart help, fees: https://www.instacart.com/help/section/360007902791/360039164252
- Instacart developer docs: shopping list concept https://docs.instacart.com/developer_platform_api/guide/concepts/shopping_list ; create endpoint https://docs.instacart.com/developer_platform_api/api/products/create_shopping_list_page ; API keys https://docs.instacart.com/developer_platform_api/get_started/api-keys ; FAQ https://docs.instacart.com/developer_platform_api/faq ; pre-launch checklist https://docs.instacart.com/developer_platform_api/guide/concepts/launch_activities/pre-launch_checklist ; developer terms https://docs.instacart.com/developer_platform_api/guide/terms_and_policies/developer_terms
- Amazon Associates: application review https://affiliate-program.amazon.com/help/node/topic/G8TW5AE9XL2VX9VM ; Operating Agreement https://affiliate-program.amazon.com/help/operating/agreement ; Program Policies https://affiliate-program.amazon.com/help/operating/policies ; Creators API intro https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction ; PA-API deprecation https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation
- Amazon, Prime cost and benefits: https://www.aboutamazon.com/md/news/retail/prime-membership-cost-benefits
- Amazon, Same-Day Delivery rates (odd host): https://digprjsurvey.amazon.com/csad/help/node/GTFUTRQF459U3H3Y
- Walmart affiliates FAQ: https://affiliates.walmart.com/faqs
- Walmart press release, 2021-03-01 (stale): https://corporate.walmart.com/news/2021/03/01/walmart-drops-35-minimum-for-express-delivery
- DoorDash, fees: https://help.doordash.com/consumers/s/article/What-fees-do-I-pay?language=en_US
- Google Maps URLs: https://developers.google.com/maps/documentation/urls/get-started
- FTC, endorsement Q&A: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- FTC, Disclosures 101 for Social Media Influencers (Nov 2019): https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers

**A, but only seen in search excerpts (site blocked automated reading, or fetch failed)**
- Walmart help: https://www.walmart.com/help/article/walmart-benefits-free-shipping-and-free-delivery-from-your-store/d1738a201207485c99fd53ccdbc49699 ; https://www.walmart.com/plus ; Walmart+ FAQ https://www.walmart.com/plus/faq/free-unlimited-delivery
- Shipt help: https://help.shipt.com/is-there-a-minimum-order
- Target Partners FAQ: https://partners.target.com/faqs
- Amazon PA-API Add to Cart form (now redirects): https://webservices.amazon.com/paapi5/documentation/add-to-cart-form.html

**B**
- Digital Commerce 360, Amazon Now (2026-05-12): https://www.digitalcommerce360.com/2026/05/12/amazon-now-us-30-minute-delivery/amp/

**C and D:** affiliate and blog guides to the Walmart, Target and Amazon programs appeared in search results; used for leads only, no claim above rests on them.
