# StoreHub Ads — Problems & VPs (Creative Team Brief)

> **For the team starting AI creatives.** This is the working library of merchant **problems** and **value propositions (VPs)** we use to generate ad themes. Pair one **problem** with one **VP** to get a creative angle. Multiple angles can roll up into a **theme** (see `config/creative_themes.json` for the active 12).
>
> **The formula:** `Problem × VP → Angle → Theme → Creative`
>
> **Source files** (read these first if you want to go deeper):
> - `config/audience.json` — segments, fears, frustrations, buying triggers
> - `config/products.json` — products, USPs, pain-points solved
> - `config/creative_themes.json` — the 12 themes (with retired/active status)
> - `ads/claude-design-setup/compliance-and-positioning.md` — hard rules + 4-vertical positioning
> - `ads/claude-design-setup/family-prompts.md` — production-ready creative families

---

## How to use this doc

1. Pick **1 problem** the merchant is feeling acutely.
2. Pick **1 VP** that resolves it.
3. Wrap the pairing in **1 theme** (psychological lever — pain amp, milestone math, artifact native, etc.).
4. Pick **1 format** (1080×1080 / 1920×1080 / 1080×1920).
5. Write copy that names the problem in the merchant's words and the VP in concrete numbers.

A single ad should hit **one** problem + **one** VP cleanly. If you can list more than 2 VPs for an ad, it's too cluttered — split it.

---

## Part 1 · Problems (what merchants feel)

Organised by category. Pull the merchant's exact language — never paraphrase into corporate-speak. Market-specific pains are tagged `[MY only]` / `[PH only]` / `[TH only]`.

### A. Operations & speed
1. **Peak-hour chaos** — orders stacking up, staff yelling, queue out the door, tablets everywhere.
2. **Slow service / low table turnover** — customers walk out before being seated.
3. **Order mistakes** — wrong food to wrong table; angry customer leaves bad review.
4. **Multi-channel chaos** — managing dine-in + takeaway + delivery + walk-in from different systems.
5. **Manual order-taking** — pen-and-paper, verbal mistakes, lost chits.
6. **POS crashes at peak** — old system freezes when you need it most.
7. **WhatsApp order chaos** — customers DM'ing menu photos and voice notes; no POS record, easy to miss, impossible to reconcile.

### B. Inventory & stock
8. **Stock-outs of best-sellers** — running out of what sells; lost revenue, frustrated customers.
9. **Overstock / dead inventory** — cash tied up in items that won't move.
10. **Midnight stock count** — counting boxes after closing, 2-hour task, errors inevitable.
11. **Stock shrinkage (goods missing)** — items gone, no audit trail, no idea where.
12. **Outlet inventory mismatch** — sell at outlet A what's actually only at outlet B.
13. **Online ↔ in-store inventory split** — selling on Instagram / Shopee / TikTok Shop + walk-in, two separate truths, overselling online, disappointing in-store. *(Primarily retail.)*

### C. Money & financial bleed
14. **Delivery-app commissions (30%+)** — half your margin goes to the platform, not you. Year over year you've handed over RM20k+ without anyone showing you the number.
15. **Cashier-level revenue leakage** — wrong change, unofficial discounts, items rung up at wrong price, no audit trail. *Different from stock shrinkage (goods) and order mistakes (kitchen) — this is money walking out the cash drawer.*
16. **Hidden costs you've never totalled** — fees, overtime, manual error costs, "small" subscription stack — never added up.
17. **Cash-flow blind spot** — don't know today's sales until tomorrow.
18. **11pm reconciliation** — counting cash, matching receipts, exhausted, error-prone.
19. **Quietly overpaying old POS** — locked into legacy pricing for a system worse than alternatives.

### D. Compliance & admin
20. **e-Invoicing / LHDN deadlines `[MY only]`** — no system that auto-submits to LHDN; risk of penalties.
21. **BIR / OR compliance `[PH only]`** — Bureau of Internal Revenue audit anxiety; Official Receipt requirements; need BIR-Accredited POS.
22. **Manual report generation** — hours every month building reports that finance won't even read.
23. **Tax-season panic** — receipts in a shoebox, missing records, scrambling.
24. **Payroll / timesheet errors** — manual clock-ins, buddy-punching, payroll mistakes.

### E. Staff
25. **Staff training takes forever** — 2 weeks to onboard; they leave a month later.
26. **High turnover** — train them, lose them, train again.
27. **Order-mistake blame game** — who took the order? Nobody knows.
28. **Owner can't leave the shop** — without the boss watching, things fall apart.

### F. Customers & growth
29. **First-time customers never return** — no system to bring them back.
30. **No customer data** — don't know who they are, what they bought, when they last came in.
31. **Manual loyalty (punch cards)** — easy to fake, easy to lose, low engagement.
32. **No way to message customers between visits** — can't run a promo; there's no list.
33. **Customers go to newer cafés / shops** — competitors with apps and loyalty programmes pull them away.

### G. Visibility & control
34. **Anxiety when away** — vacation / family event = guilt and worry.
35. **No real-time view of multiple outlets** — find out about problems hours or days late.
36. **Pricing / ordering by gut** — no data on what's actually selling; menu and stock decisions made blind.
37. **Reports come too late to act on** — by the time you see the dip, it's a week deep.

### H. Life-stage / emotional
38. **Just opened — overwhelmed by setup costs** — RM48k renovation, RM25k kitchen, every line adds up.
39. **First-90-days survival anxiety** — 60% of new F&B closes in year 1; you know it.
40. **No family time** — 11pm closes, no Sundays, missed your kid's recital.
41. **Want to open a second branch but can't run two places at once** — training staff at the new place is killing you; expansion stalls.
42. **"I went into this to cook / serve / sell — not to be a finance team"** — identity strain.

### I. Trust & purchase risk
43. **Burned by previous tech** — "free POS" turned into a nightmare.
44. **Fear of system going down** — what if it crashes on Friday night?
45. **Don't trust the data will be accurate** — old systems gave wrong numbers.
46. **Long-contract lock-in fear** — 2-year contract for software that may not work.
47. **Slow / non-existent support** — when something breaks, nobody answers.

---

## Part 2 · Value Propositions (what StoreHub delivers)

Each VP: the **claim**, **proof**, **features that prove it**, **what NOT to say**.

### VP1 · All-in-one (replaces 6+ tools)
- **Claim:** One system runs everything — POS, payments, inventory, reporting, loyalty, online ordering, e-invoicing. Includes real-time data + insights so you stop running the business on gut.
- **Proof:** "6 tools → 1 system." | "From RM3.40/day."
- **Features:** POS, Payments, Inventory Management, Reporting & Analytics, Loyalty Program, Online Ordering, E-Invoice.
- **NOT:** Don't bury this in a feature list — lead with the breadth, then drill into one feature for proof.

### VP2 · Commission savings (own your delivery)
- **Claim:** Take delivery orders directly. Keep 100% of revenue. Own the customer relationship.
- **Proof:** "Delivery apps take 30%. StoreHub takes 0." | "You're paying how much in delivery fees?"
- **Features:** Online Ordering, Webstore, Integrated Logistics, Takeaway & Pickup.
- **NOT:** Never name GrabFood, FoodPanda, ShopeeFood. Use "delivery apps" / "third-party delivery."

### VP3 · Zero training / ease of use
- **Claim:** Staff can use it on day one. No manual, no week-long onboarding.
- **Proof:** "Open the box, plug it in, sell." | "Train a new staff member in 5 minutes."
- **Features:** POS UI, Employee Management, simplified BackOffice.
- **NOT:** Avoid generic "easy to use" — anchor to a specific time (5 min onboarding, day-one ready).

### VP4 · Customer retention (bring them back)
- **Claim:** Built-in loyalty + cashback + auto SMS turns first-time customers into repeat regulars with zero manual effort.
- **Proof:** "Customers repeat 8× a month with cashback." | "Loyalty SMS sent automatically while you sleep."
- **Features:** Loyalty Program, Membership, Engage (CRM), CashBack, Customisable Promotions.
- **NOT:** Don't dismiss punch cards — frame this as automation.

### VP5 · Social proof (scale + trust)
- **Claim:** 20,000+ merchants across Malaysia, Philippines, Thailand trust StoreHub.
- **Proof:** "20,000+ merchants across Southeast Asia" | named merchant outcomes.
- **Features:** N/A — brand truth, not a feature.
- **NOT:** Generic "I love StoreHub!" quotes — proven weak. Use specific named merchant + specific number.
- **⚠️ Verify before use:** Named merchant case studies (Binq Dessert, Merchants Lane, Quartet TTDI, The Pinggan, etc.) need confirmed metrics + signed release before they appear in any ad. Check `config/products.json` social_proof fields — anything still marked `FILL IN` is **not approved**.

### VP6 · Growth (scale to multiple outlets)
- **Claim:** Open outlet #2, #5, #50 with one dashboard.
- **Proof:** "One dashboard. Every outlet. Live." | "Open new stores in days, not months."
- **Features:** Multi Location Management, centralised Reporting, Employee Management.
- **NOT:** Don't sell scale to a single-outlet merchant — segment-match.

### VP7 · Time savings
- **Claim:** Get hours back every week — auto reports, auto SMS, auto reconciliation.
- **Proof:** "Close your day in 12 minutes, not 2 hours." | "Save 103 hours a year on payroll."
- **Features:** Reporting & Analytics, Engage automation, AI Face Capture Clock In, auto-close.
- **⚠️ Verify before use:** Any time-savings number used in an ad needs source documentation (which feature, which calculation, finance sign-off). Don't invent hours.
- **NOT:** Vague "save time" claims. Always anchor to a specific number of hours / minutes — and back it up.

### VP8 · Reliability (works at peak)
- **Claim:** Built for the rush — doesn't crash when you need it most.
- **Proof:** "Handles 3 peaks a day." | "Cloud-based — runs even when WiFi drops."
- **Features:** POS hardware (D3 Pro, Falcon 2, D3 Mini), cloud sync, offline mode.
- **NOT:** Don't lead with hardware specs to a merchant whose pain is operational. Specs follow story.

### VP9 · Compliance (e-Invoicing / LHDN / BIR)
- **Claim:** Auto-submits tax records. Zero manual tax work. Market-correct compliance.
- **Proof:** MY: "LHDN-compliant. Auto-submits e-invoices." | PH: "BIR-Accredited. OR-compliant out of the box."
- **Features:** E-Invoice integration, Reporting & Analytics, BIR-compliant receipts (PH).
- **NOT:** Don't run compliance ads outside of active deadline windows — low resonance. Don't mix LHDN (MY) and BIR (PH) framing across markets.

### VP10 · Price anchor
- **Claim:** Industry-leading platform at SME-affordable pricing.
- **Proof:** MY: "From RM3.40/day" / PH: "From ₱22,995/year" + BIR Accredited / TH: "Up to 55% off hardware."
- **Features:** Hardware promo + subscription pricing.
- **NOT:** Never mix market currencies. Never use /day or /month in PH copy — only /year.

### VP11 · Built for SEA (cultural fit)
- **Claim:** Designed for Malaysian / Filipino / Thai F&B and retail — not a Western tool retrofitted.
- **Proof:** Pan-Asian merchant faces, local food, local language (BM, Tagalog, Thai), local payment integrations.
- **Features:** Localised payment methods, multi-language UI, local merchant case studies.
- **NOT:** Generic pan-Asian stock photography. Must be market-specific (MY ≠ PH ≠ TH).

### VP12 · Remote control (run from anywhere)
- **Claim:** See every outlet, every sale, every staff clock-in from your phone — anywhere in the world.
- **Proof:** "Check today's sales from your kid's school recital." | "Manage 3 outlets from one screen."
- **Features:** Cloud BackOffice, mobile app, real-time dashboards, Multi Location Management.
- **NOT:** Avoid lifestyle/freedom imagery (beaches, skydiving, hammocks) — proven 0 SQL. Use realistic away-from-shop moments (family, errands, second business).

### VP13 · Done-with-you setup (implementation support)
- **Claim:** We don't drop the system on your doorstep — our team comes in, sets it up, trains your staff, stays on the line.
- **Proof:** "Staff turun kedai — we set up everything." | "Local onboarding team — they speak your language." | "Go-live guaranteed."
- **Features:** Onboarding service, dedicated implementation team, local market support.
- **NOT:** Don't promise "instant setup" — the value is human handholding, not automation. This VP is the close-rate driver for merchants who've been burned before (Problem #43).

---

## Part 3 · Problem → VP → Theme cheat sheet

The fastest way to write a creative: scan the merchant's pain, find the VP that owns it, pick a theme that frames it.

| # | Pain in one line | Primary VP | Secondary VP | Suggested theme(s) |
|---|---|---|---|---|
| 1 | Peak-hour chaos | VP8 | VP3 | T1 / T11 |
| 2 | Slow table turnover | VP8 | VP7 | T9 / T11 |
| 3 | Order mistakes | VP3 | VP8 | T1 / T11 |
| 4 | Multi-channel chaos | VP1 | VP12 | T5 / T11 |
| 5 | Pen-and-paper orders | VP1 | VP3 | T5 / T9 |
| 6 | POS crashes at peak | VP8 | VP1 | T5 / T1 |
| 7 | WhatsApp order chaos | VP1 | VP4 | T11 (WhatsApp artifact) |
| 8 | Stock-outs of best-sellers | VP1 (data) | VP12 | T9 / T11 |
| 9 | Overstock / dead inventory | VP1 (data) | VP6 | T9 / T5 |
| 10 | Midnight stock count | VP7 | VP1 | T11 / T1 |
| 11 | Stock shrinkage (goods) | VP1 | VP8 | T9 / T11 |
| 12 | Outlet inventory mismatch | VP6 | VP12 | T5 / T10 |
| 13 | Online ↔ in-store split | VP1 | VP6 | T5 / T10 |
| 14 | 30% delivery commissions / year-1 bleed | VP2 | VP10 | T9 / T12 |
| 15 | Cashier-level revenue leakage | VP8 | VP1 | T9 (artifact receipt) |
| 16 | Hidden costs untotalled | VP10 | VP2 | T9 / T11 (bank-statement artifact) |
| 17 | Cash-flow blind spot | VP12 | VP7 | T10 / T11 |
| 18 | 11pm reconciliation | VP7 | VP3 | T11 (WhatsApp) / T1 |
| 19 | Overpaying old POS | VP10 | VP1 | T5 / T12 |
| 20 | LHDN deadlines `[MY]` | VP9 | VP3 | T11 (form artifact) / T12 |
| 21 | BIR / OR compliance `[PH]` | VP9 | VP3 | T11 / T12 |
| 22 | Manual reports | VP7 | VP1 | T10 / T9 |
| 23 | Tax-season panic | VP9 | VP7 | T11 / T1 |
| 24 | Payroll errors | VP3 | VP7 | T10 / T9 |
| 25 | Long staff training | VP3 | VP13 | T10 / T6 |
| 26 | High turnover | VP3 | VP8 | T10 / T11 |
| 27 | Order blame game | VP3 | VP1 | T11 (artifact) |
| 28 | Owner can't leave | VP12 | VP7 | T10 / T8 |
| 29 | Customers don't return | VP4 | VP5 | T10 / T6 |
| 30 | No customer data | VP4 | VP1 | T10 / T11 |
| 31 | Manual loyalty cards | VP4 | VP3 | T5 / T10 |
| 32 | Can't message customers | VP4 | VP1 | T10 / T11 |
| 33 | Losing to newer competitors | VP4 | VP6 | T5 / T8 |
| 34 | Anxiety when away | VP12 | VP7 | T10 / T8 |
| 35 | No multi-outlet view | VP6 | VP12 | T5 / T10 |
| 36 | Pricing/ordering by gut | VP1 (data) | VP6 | T10 / T11 |
| 37 | Reports too late | VP7 | VP12 | T10 / T11 |
| 38 | Just opened — overwhelmed | VP10 | VP13 | T2 / T12 |
| 39 | 90-day survival anxiety | VP10 | VP8 | T12 / T2 |
| 40 | No family time | VP7 | VP12 | T11 / T8 |
| 41 | Second branch stuck | VP6 | VP13 | T2 / T10 |
| 42 | "I went in to cook, not finance" | VP1 | VP3 | T10 / T11 |
| 43 | Burned by free / cheap POS | VP8 | VP13 | T5 / T6 |
| 44 | Fear of downtime | VP8 | VP5 | T6 / T5 |
| 45 | Don't trust the data | VP8 | VP5 | T6 / T9 |
| 46 | Long-contract lock-in | VP10 | VP5 | T5 / T6 |
| 47 | Slow support | VP13 | VP11 | T6 / T7 |

---

## Part 4 · Themes (psychological levers)

Once you have `Problem × VP`, choose a theme. Source of truth: `config/creative_themes.json`.

| ID | Theme | Status | Strongest format | Best for |
|---|---|---|---|---|
| T1 | Pain Amplification | **🚫 RETIRED MY EN** (0 leads in Batch 1) | 1080×1920 | Only retest with T11 wrapper or in MS/PH |
| T2 | New Chapter | ✅ Active (volume winner, cap budget) | 1080×1920 | Life-stage moments (just opened, expanding) |
| T3 | Quiet Ambition | ✅ Active (untested in MY) | 1080×1080 | Documentary / low-resistance audiences |
| T4 | The Math | **🚫 RETIRED standalone** (0 leads) | — | Math survives only inside T12 |
| T5 | Competitive Contrast | ⭐ **Proven winner** (CTR 4× benchmark) | 1920×1080 | Comparison shoppers — this way vs that way |
| T6 | Social Proof | ⏳ Active but needs data | 1080×1080 | Late-stage evaluators needing risk reduction |
| T7 | Cultural Pride | ⭐ **Proven winner** (best CPL, scalability) | 1080×1920 | Volume / scroll-stop in SEA feeds |
| T8 | Aspirational Self | ⚠️ Deprioritised (1 lead Batch 1) | 1920×1080 | Already-functional merchants wanting growth |
| T9 | Hidden Cost | ✅ Active (untested but high-potential) | 1080×1080 | Forensic financial pain — receipts, statements |
| T10 | Value Unlocked | ⚠️ Deprioritised (0 SQL Batch 1) | 1080×1920 | Use only as outcome-framing inside other themes |
| T11 | Artifact Native | ⭐⭐ **Top winner** (SQL% 28.6%, CPSQL RM359) | 1080×1080 | Ad mimics non-ad UI (job post, WhatsApp, review, receipt) |
| T12 | Milestone Math | ✅ Active (new — Batch 2 priority) | 1080×1080 | Life-stage moment + specific number |

**Priority order for Batch 2+:** T11 → T5 → T7 → T12 → T9 → T2 → T3 → T6 (avoid T1, T4, T8, T10 unless used as wrappers).

**Rule:** Each theme expects 2–3 creative variations (same angle, different executions) tested head-to-head. Don't mix themes in one ad.

---

## Part 5 · Hard compliance rules (read every time)

Pulled from `compliance-and-positioning.md`. **Zero tolerance:**

1. **Never name competitors.** Not in copy, not in visuals.
   - ❌ GrabFood / FoodPanda / ShopeeFood / Grab / Lalamove / Pickupp / any named POS rival
   - ✅ "delivery apps" / "third-party delivery" / "old POS" / "legacy systems"
2. **Never show competitor logos / app icons / recognisable UI** in any frame.
3. **Market-pricing discipline.** RM stays in MY. ₱ stays in PH. ฿ stays in TH.
   - PH copy uses **/year only** — never /day or /month. Anchor: "From ₱22,995/year" + BIR Accredited.
   - MY anchor: "From RM3.40/day."
   - TH anchor: "Up to 55% off hardware."
4. **Pan-Asian faces only.** Never Western. Market-specific (MY ≠ PH ≠ TH).
5. **Logo always reads "StoreHub"** — one word, mid-cap H. Never ScoreHub / Score Hub / Store Hub.
6. **Brand-colour discipline:** orange `#ff9419` + black `#2f2922` dominant; accents pink `#ff546f`, bold orange `#ff630f`, azure `#2a6ee8`. Never orange + green.
7. **CTA by vertical:**
   - F&B / Retail / Service → "BOOK A FREE DEMO NOW"
   - **Enterprise → "CONTACT US"** (never "Book a demo")
8. **Meta safe zones** must be respected — see `ads/claude-design-setup/meta-safe-zones.md`.

---

## Part 6 · Worked examples

Four end-to-end walkthroughs. The fourth is an anti-pattern + the corrected brief.

### Example A — F&B owner, MY (positive)
- **Problem #18** (11pm reconciliation) × **VP7** (time savings)
- **Theme:** T11 Artifact Native
- **Format:** 1080×1080 (square — matches WhatsApp chrome)
- **Execution:** Fake WhatsApp group chat ("Restaurant Bosses 🍜") with Sarah/Akmal complaining about reconciliation at 11:47pm. One bubble breaks the pattern: "Wait — StoreHub closes the day automatically. From RM3.40/day."
- **Copy hook:** "When 'tomorrow' becomes every night."

### Example B — F&B owner, MY — opening expenses (positive)
- **Problem #38** (just opened — overwhelmed by setup costs) × **VP10** (price anchor)
- **Theme:** T12 Milestone Math
- **Format:** 1080×1080 (square — numbers + milestone copy stack cleanly)
- **Execution:** Cost card on bold orange BG. Line items: Renovation RM48,000 / Kitchen RM25,000 / Signage RM3,500 / Staff training RM1,200. One row highlighted: "POS (StoreHub) — RM102/week." Caveat handwriting: "One of these pays you back."
- **Copy hook:** "You saved where it counted."
- **Why T12 not T2:** T2 "opening expenses" was a Batch 1 volume winner but SQL% collapsed at scale. T12 fixes this by anchoring a specific number inside the milestone so the audience pre-qualifies.

### Example C — F&B owner, PH (positive)
- **Problem #14** (delivery commissions) × **VP2** (commission savings)
- **Theme:** T9 Hidden Cost
- **Format:** 1080×1080 (receipt/statement reads best square)
- **Execution:** Fake month-end statement. Line items: "Delivery app commissions — ₱5,700" / "StoreHub — ₱408." Headline: "Which line are you cutting?"
- **PH-specific:** Anchor "From ₱22,995/year" + "BIR Accredited." No /day or /month language.

### Example D — Anti-pattern → corrected (negative + fix)
**The brief that came in:**
> "Hero ad — Malay merchant smiling at counter. List 7 features: POS, inventory, loyalty, e-invoicing, delivery, reports, support. 55% off + free months + RM3.40/day + 20,000 merchants. Tagline: 'Everything Your Business Needs.' CTA: Book demo."

**Why it fails:**
- ❌ Feature dump (7 features — anti-pattern #1) (Part 7).
- ❌ Promo-stack: 4 different price/proof points piled on (anti-pattern #2).
- ❌ Generic merchant smile — could be any brand (anti-pattern #4).
- ❌ Tagline says nothing — no problem named (anti-pattern #5).
- ❌ No theme. No psychological lever. Reads as a brochure.

**The corrected brief:**
- **Problem #42** ("I went in to cook, not finance") × **VP1** (all-in-one)
- **Theme:** T11 Artifact Native (Google review chrome)
- **Format:** 1080×1080
- **Execution:** Fake Google review card. Reviewer: "Akmal · Mamak Subang." 5 stars. Review body: "Bought StoreHub because I was running 6 different tools and losing my mind. Now I close my day in 15 minutes and actually went home for dinner this week. Wish I'd switched 2 years ago."
- **Copy hook:** "The review you'll leave in 6 months."
- **Single price anchor:** "From RM3.40/day." Drop the 55% / free months / 20k merchants from the same frame — those go in different ads.

---

## Part 7 · Anti-patterns (ads we keep accidentally making)

Ordered by frequency × damage. Stop yourself before any of these:

1. **Feature dump ads** — "POS, inventory, loyalty, reporting, online ordering, e-Invoicing, multi-outlet, payments…" Pick one. Sell one. Drill in.
2. **Promo-stacking** — "55% OFF + free months + zero training + 20,000+ merchants + RM3.40/day" reads as desperation. One anchor per ad.
3. **Generic "save time / save money"** without a number — useless. Anchor every claim to a specific figure.
4. **Stock-photo Pan-Asian merchants** that could be anywhere — must feel like a real MY/PH/TH shop.
5. **Lifestyle/freedom imagery** (beaches, skydiving, hammocks) — proven 0 SQL. Cut it.
6. **Testimonial quote cards** ("I love StoreHub!") — proven weak. Use named merchant + specific number instead.
7. **Polished SaaS aesthetic** — clean dashboards, gradient overlays, abstract icons. Authentic / documentary / artifact-native beats polished in cold acquisition.
8. **Western faces.** Hard fail.
9. **Competitor names anywhere.** Hard fail.
10. **Mixing market currencies in one ad.** Hard fail.
11. **Using retired themes** (T1, T4 standalone, T8, T10) without explicit reason. Default to T11 / T5 / T7 / T12.

---

## Part 8 · The 60-second sanity check (run before submitting any creative)

- [ ] One clear problem named in the merchant's words?
- [ ] One clear VP shown with a specific, defensible number or proof point?
- [ ] One theme — not three smashed together?
- [ ] Theme picked from the **active** list (not T1/T4 standalone/T8/T10)?
- [ ] All 3 formats produced (1080×1080 / 1920×1080 / 1080×1920)?
- [ ] Logo top-right, correct colour for background, inside safe zone?
- [ ] CTA pill — orange `#ff9419`, correct text for vertical (F&B/Retail/Service: **"BOOK A FREE DEMO NOW"**; Enterprise: **"CONTACT US"**), inside safe zone?
- [ ] Market-correct pricing anchor (RM /day | ₱ /year + BIR | ฿ 55% off)?
- [ ] Zero competitor names anywhere (copy + visuals)?
- [ ] Pan-Asian faces only (where humans appear)?
- [ ] Market-specific compliance label correct (LHDN for MY only; BIR for PH only)?
- [ ] StoreHub spelled correctly — one word, mid-cap H?
- [ ] Any named merchant testimonial verified + approved (`config/products.json` confirms — no `FILL IN` fields)?
- [ ] Any time-savings / cost-savings number defensible (finance signed off, calculation documented)?

If any answer is no — fix before submitting.
