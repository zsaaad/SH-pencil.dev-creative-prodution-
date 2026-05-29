# PH Batch 1 — Creative Production Prompt (Pencil.dev)

**Iteration:** PH-1 (fresh market, no prior PH batch through this pipeline)
**Market:** PH EN
**Date drafted:** 2026-04-28
**Run window:** launch after production → 14-day test cycle
**Total concepts:** 32 (20 safe + 12 wildcard)
**Total output files:** 96 (each concept × 1080×1080 + 1920×1080 + 1080×1920)
**Output .pen file:** `ads/SH PH ads batch 1.pen` (new — do not write into the MY batch file)
**Theme analysis (read first):** `ads/batches/PH-batch_001/theme-analysis.md`
**No prior PH control through this pipeline.** Anchor benchmarks against the PH CSV averages: CPL ₱99 · CPSQL ₱425 · W`on% 7%. Top-tercile PH historical performers hit CPL ₱33–54, CPSQL ₱178–272.

---

## 1 · Why this batch looks the way it does

The PH market dataset (n=18 ads, primary CSV) shows three clear structural reads:

1. **₱63/day price anchor scales.** Six of the top eight PH ads carry it; survives every relaunch.
2. **Holiday-tied promos work *only with* a hard offer.** Independence Day ₱21,000-off promo hit SQL% 43.1%. NationalHeroesDay (no offer) and Halloween (problems hook, no offer) died.
3. **Logos work, talking-head testimonials don't.** Logo-grid ads convert at Won% 5.77%; quote testimonials collapse at Won% 1.02%.

Two further directional signals: (a) "How much is your profit?" cost-question hooks drive the cheapest CPL in the dataset (₱9–₱41) but lower Won% — they fill top of funnel and need sharper qualification copy; (b) Choose Your Fighter / unboxing visual formats drive 4–6% CTR, 5–7× period average.

PH has never been tested through the Pencil pipeline. MY Batch 1's structural insight — *artifact format > polished promo* — has not been validated in PH. PH ad-skepticism is high (heavy GCash / Lazada / Shopee promo saturation), so artifact disguise should outperform standard creative.

**Batch 1 strategy: lock in the proven safe baseline, layer in 3 calculated wildcards.**

---

## 2 · Themes in PH Batch 1

| Theme ID | Theme | Role | Concepts |
|---|---|---|---|
| **T4** | The Math | ₱63/day anchor — proven PH workhorse | 4 (all safe) |
| **T11** | Artifact Native | Highest structural bet — MY winner format never tested in PH | 4 (all wildcard) |
| **T5** | Competitive Contrast | CYF drove top-tercile CTR — extend beyond hardware tiers | 4 (all safe) |
| **T9** | Hidden Cost | Cheapest CPL angle — needs sharper artifact-style execution | 4 (all wildcard) |
| **T2** | New Chapter | Holiday promo + hard offer drove SQL% 43.1% | 4 (all safe) |
| **T12** | Milestone Math | Fuses the two proven PH levers — milestone × price-anchor | 4 (all wildcard) |
| **T7** | Cultural Pride | Halo-halo/sisig/coffee directionally validated; pure-cultural hero untested | 4 (all safe) |
| **T6** | Social Proof (logo-grid only) | Logos win, quotes lose — explicit format constraint | 4 (all safe) |

**Safe / Wildcard split (non-negotiable for this batch):** **20 safe + 12 wildcard.** Argument: PH is fresh market with no in-market Pencil control to beat — overweight safe to set the baseline. MY Batch 2's 6/6 was iterating against a known winner; we don't have that here.

---

## 3 · Global brand + production rules (apply to every concept)

**Colors:** StoreHub Orange `#ff9419`, StoreHub Black `#2f2922`. Accents allowed: Bold Orange `#ff630f`, Pink `#ff546f`, Azure `#2a6ee8`. Gradients: only the 7 approved in `config/brand.json`.

**Typography:**
- Headline: **Barlow Black**, line spacing 1.1–1.25, max 2 lines
- Sub-headline: Open Sans Semibold/Semibold Italic, max 1 line, Sentence case
- Body bullets: Open Sans Regular/Semibold, 1 line per bullet, max 5 bullets, Sentence case
- CTA: Open Sans Bold/Bold Italic, **ALL CAPS**, on orange or pink pill

**Per-format sizing (every concept produced in all 3):**
- **1080×1080:** headline 96–140px · sub 44–60px · body 20–28px · padding max 32px (safe) / 0px (wildcard)
- **1920×1080:** headline 96–130px · sub 44–60px · body 20–28px · padding max 48px (safe) / 0px (wildcard)
- **1080×1920:** headline 130–180px · sub 52–72px · body 28–36px · UI-safe 250px top / 400px bottom

**Imagery:** Pan-Asian faces only, with **PH cultural specificity preferred** — Filipino merchants, jeepney scenes, cafe/palengke/karinderya/lechon contexts. Photo backgrounds blurred 40–60. Busy backgrounds get a 70–90% opacity colour panel behind text.

**Logo + CTA:** every frame — even wildcards — must include the StoreHub logo (bottom corner, small) and the CTA button. Default CTA copy: **"BOOK A FREE DEMO NOW"**. Currency: PHP (₱). All price points in PHP.

**Anti-patterns to avoid (will fail QA):**
- ❌ Orange split card with POS on pedestal (overused in MY)
- ❌ Centered POS on plain orange background
- ❌ Diagonal CYF split with VS badge (already maxed in PH dataset)
- ❌ Talking-head testimonial quote cards (PH Won% 1.02% — banned this batch)
- ❌ Holiday-tied creative without a hard offer attached (NationalHeroesDay / Halloween failed in PH)
- ❌ Text in narrow centre column with dead-space margins
- ❌ Headlines below minimum font size

**Naming convention for exports:**
```
S1_PH_EN_Batch1_[theme_short]_[concept_name]_[format]_nootp
```
Examples:
- `S1_PH_EN_Batch1_math_jeepney-fare_1x1_nootp`
- `S1_PH_EN_Batch1_artifact_jobstreet-ph_9x16_nootp`

**Frame-naming inside the .pen file:**
```
C_{NNN} | {theme_id} | {concept_short} | {format}
```
Example: `C_001 | T4 | jeepney-fare | 1x1`

---

## 4 · Concept specs (32 concepts)

> For each concept below: produce **three format variants** (1:1 / 16:9 / 9:16) using the creative brief. Every variant must pass the Visual QA checklist in §5 before moving on.

---

### ✅ C_001 — T4 The Math · **₱63 Hero**
**Type:** safe · **Vertical:** F&B + retail
**Hook visual:** Full-bleed orange→white gradient with the StoreHub D3 hardware bundle on a clean surface. Massive typography "₱63/day" dominates.
**Headline:** Run a real POS for the price of one cup of coffee.
**Sub-headline:** StoreHub PH from ₱63/day — hardware, software, and support included.
**Body bullets:** *(none)*
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** ₱63/day is the most repeatedly-validated PH message; baseline must include it as control.
**Success metric:** CPL ≤ ₱45 · SQL% ≥ 20%

### ✅ C_002 — T4 The Math · **Jeepney Fare**
**Type:** safe · **Localisation hero**
**Hook visual:** Clean side-by-side: photo of a ₱25 jeepney coin/bill on the left, "+ ₱38 more" graphic in the middle, StoreHub tablet on the right. Or simpler: stack of ₱63 in coins next to a hardware mockup.
**Headline:** ₱63 is one jeepney ride home. Or one day of running your business.
**Sub-headline:** StoreHub PH from ₱63/day. Hardware included.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** Localised cost-of-living anchor makes the price tangible to PH SMBs in a way the raw number does not.
**Success metric:** CTR ≥ 2.0%

### ✅ C_003 — T4 The Math · **Daily-Coin Stack**
**Type:** safe · **Lifestyle**
**Hook visual:** Overhead photograph of a small pile of ₱1, ₱5, ₱10 coins totalling ₱63, beside a StoreHub tablet on a wooden palengke counter. Soft natural light. Documentary mood.
**Headline:** This much. Per day. Runs your store.
**Sub-headline:** StoreHub from ₱63/day. Used by 17,000+ merchants across SEA.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Overhead photo of small pile of Philippine peso coins totalling about ₱63 next to a tablet POS device on a worn wooden counter, natural daylight, palengke setting, documentary food photography style, 35mm."*
**Hypothesis:** Tactile/physical price proof beats pure typography for sceptical PH audiences.

### ✅ C_004 — T4 The Math · **Year-Math Receipt**
**Type:** safe · **Sets up T9 sibling**
**Hook visual:** Clean cream background with a typed-out math statement, like a receipt. Right-aligned figures.
**Artifact copy:**
```
₱63/day × 365            =  ₱22,995/year
GrabFood 30% commission  =  ~₱400,000/year
─────────────────────────────────────
Same business. Different system.
```
**Headline:** ₱22,995. Or ₱400,000. Your call.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** Annualising the ₱63 anchor against commission losses lifts SQL% by pre-qualifying P&L-aware merchants.

---

### 🛑 C_005 — T11 Artifact Native · **Fake JobStreet PH Posting**
**Type:** wildcard · **Category:** meme-native/artifact
**Hook visual:** Pixel-accurate JobStreet PH job-listing card. White background, grey borders, "Posted 2 hours ago", standard pagination chrome.
**Artifact copy:**
> **HIRING IMMEDIATELY — Operations Cashier-Inventory-Reports Clerk (1 position)**
> Responsibilities: Run POS · track inventory across outlets · reconcile daily sales · file BIR-compliant reports · handle GrabFood/FoodPanda orders
> Salary: ₱28,000/month + SSS + PhilHealth
> Start date: ASAP
>
> **OR — StoreHub PH from ₱63/day does all of it.**
**Headline (inside the job-title field):** One person who does the work of five systems
**Sub-headline (smaller artifact text):** F&B · Retail · Multi-outlet
**CTA (outside the artifact, as a reveal):** BOOK A FREE DEMO NOW
**Pencil notes:** Build the classifieds card as raw rectangles + Pencil text — pixel-sharp. No photo.
**Hypothesis:** PH merchants comparing the cost of a hire will recognise a JobStreet listing before a promo.
**Success metric:** SQL% ≥ 25% · CPSQL ≤ ₱360

### 🛑 C_006 — T11 Artifact Native · **Fake GCash Receipt**
**Type:** wildcard · **Category:** meme-native/artifact
**Hook visual:** Pixel-accurate GCash transaction receipt UI — blue header, transaction list, amounts right-aligned. Looks like a screenshot taken from a phone.
**Artifact copy:**
```
MONTHLY BUSINESS EXPENSES — MARCH 2026
GrabFood commission (30% of ₱140,000)   ₱42,000.00
FoodPanda commission (20% of ₱75,000)   ₱15,000.00
Manual end-of-day reconciliation
  (46 hours × ₱150/hour)                ₱ 6,900.00
Stock discrepancy write-offs            ₱ 2,400.00
──────────────────────────────────────
TOTAL BLEEDING                          ₱66,300.00

StoreHub PH (monthly)                   ₱ 1,890.00
```
**Headline:** Which line are you cutting?
**Sub-headline:** StoreHub consolidates all of this into one dashboard.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Use Roboto Mono / monospace substitute for receipt body. Reds/orange highlight on the bleeding line, brand orange on StoreHub line.
**Hypothesis:** Forensic cost-breakdown artifact converts vague discomfort into a specific, calculable reason to act.
**Success metric:** CPL ≤ ₱65 · SQL% ≥ 15%

### 🛑 C_007 — T11 Artifact Native · **Fake Viber Boss-Staff Chat**
**Type:** wildcard · **Category:** meme-native/artifact
**Hook visual:** Pixel-accurate Viber chat UI — purple header "Resto Group 🍽️ · 4 members", default Viber chat wallpaper, white incoming bubbles, purple outgoing.
**Chat copy (script as a thread):**
- `[10:42PM · Maria]` boss anong total natin today
- `[10:43PM · Boss]` calculating pa
- `[10:44PM · Maria]` 😭
- `[10:46PM · Maria]` last week ganito din
- `[10:47PM · Boss]` ok ok lipat na tayo sa StoreHub bukas
**Headline (outside chat, below):** When "tomorrow" becomes every night.
**Sub-headline:** StoreHub closes your day automatically. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Solid rectangles + rounded corners. Use Viber purple `#7360F2` for header. Do NOT use the Viber logo. Add a subtle "screenshot crop" shadow.
**Hypothesis:** F&B owners who've had this exact conversation pause on a Viber-native artifact and convert at SQL% ≥ 20%.

### 🛑 C_008 — T11 Artifact Native · **Fake BIR Compliance Form**
**Type:** wildcard · **Category:** meme-native/artifact (PH-only — MY can't replicate)
**Hook visual:** Pixel-accurate BIR form chrome — light grey government-form aesthetic, monospace headings, BIR-style numbered sections. Two checkboxes, one ticked.
**Artifact copy:**
```
[ BIR FORM 2303 — RELATED ]

Section 4 · Point-of-Sale Compliance Status

   [ ✓ ]  Is your POS BIR-accredited?
   [   ]  Does it generate compliant ORs in 30 seconds?

If you ticked the wrong box,
your weekend might be gone again.
```
**Headline (below the form):** 30 seconds. Or your Saturday.
**Sub-headline:** StoreHub PH is a BIR-accredited POS. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Use government-form aesthetics — light grey, thin borders, monospace text. Don't lift the actual BIR logo or seal — just the structural feel.
**Hypothesis:** PH-specific compliance artifact addresses a pain MY can't replicate and pre-qualifies established merchants who already deal with BIR.

---

### ✅ C_009 — T5 Competitive Contrast · **CYF Hardware Tier (refreshed)**
**Type:** safe · **Proven control**
**Hook visual:** Three hardware tier cards side-by-side (Falcon / D3 / D3 Pro), labelled with PH-relevant business archetype above each (Cafe / Karinderya / Restaurant). Choose-Your-Fighter game-card aesthetic.
**Headline:** Pick your fighter. We'll handle the rest.
**Sub-headline:** Three hardware tiers from ₱63/day. Built for PH F&B.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** CYF drove top-tercile CTR in PH already; refreshed PH-vertical labelling re-engages the format.

### ✅ C_010 — T5 Competitive Contrast · **30% vs 0%**
**Type:** safe · **Two-number minimal**
**Hook visual:** Hard split: left half pink/red `30%` huge, label "GrabFood commission". Right half orange `0%`, label "Run your own POS · keep your margin."
**Headline:** 30%. Or 0%. Your margin.
**Sub-headline:** StoreHub PH. ₱63/day. No commissions.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** The numerical contrast is the entire ad — punchier than a copy-led comparison. Targets merchants already running on GrabFood/FoodPanda.

### ✅ C_011 — T5 Competitive Contrast · **Midnight vs 6PM**
**Type:** safe · **Operational split**
**Hook visual:** 50/50 horizontal split. Left: photo of a karinderya owner at midnight under a single bulb, clipboard, calculator, exhausted. Right: same owner at 6pm, clean dashboard on a tablet, smiling, going home.
**Headline:** Closing time. Or done at 6pm.
**Sub-headline:** Inventory + reconciliation, automated. StoreHub PH from ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Left `G()` prompt — *"Photo of Filipino karinderya owner at midnight under single bulb, clipboard, calculator, warm tungsten light, documentary, 35mm, exhausted face."* Right `G()` prompt — *"Same Filipino karinderya owner at 6pm, holding a tablet showing a clean POS dashboard, walking out of the karinderya, golden hour light, documentary."*

### ✅ C_012 — T5 Competitive Contrast · **Logbook vs iPad**
**Type:** safe · **Analog→digital**
**Hook visual:** Top: photo of a battered handwritten karinderya logbook with smudged pen ink, water stains, scribbled totals. Bottom: clean StoreHub iPad showing the same kind of data, but tidy.
**Headline:** Same numbers. Different century.
**Sub-headline:** From ₱63/day, your karinderya runs like a chain.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt for top — *"Close-up photo of a handwritten Filipino karinderya logbook, smudged pen, water stains, pesos and item names, documentary, top-down."*

---

### 🛑 C_013 — T9 Hidden Cost · **Annual Commission Audit**
**Type:** wildcard · **Category:** artifact + forensic-cost
**Hook visual:** Receipt-style ledger on a cream background. All figures right-aligned. Italic small footer.
**Artifact copy:**
```
2025 · YOUR COMMISSION AUDIT

GrabFood commissions       ₱478,200
FoodPanda commissions      ₱182,400
Manual reports (240 hrs)   ₱ 36,000
Stock write-offs           ₱ 22,000
──────────────────────────────────
TOTAL COST                 ₱718,600

StoreHub PH (12 months)    ₱ 22,680
```
**Headline:** Your hidden P&L line.
**Sub-headline:** What your delivery apps don't show you. StoreHub from ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** Annual aggregation of the commission leak quantifies the real cost in a way merchants haven't seen before.

### 🛑 C_014 — T9 Hidden Cost · **Sticky-Note on POS Screen**
**Type:** wildcard · **Category:** artifact + observational
**Hook visual:** Photo of a real POS screen (maybe a cash register) with a yellow Post-it stuck on the corner. The Post-it has handwriting in Sharpie:
> *"23 hours doing reports this month. Ask boss why."*
The rest of the screen shows a clutter of receipts and spreadsheets behind it.
**Headline:** Your cashier already knows the answer.
**Sub-headline:** StoreHub automates this. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Close-up photo of an old POS screen in a Filipino restaurant with a handwritten yellow sticky note that reads '23 hours doing reports this month — ask boss why'. Cluttered receipts and small spreadsheets visible. Documentary, 35mm, slight motion."*

### 🛑 C_015 — T9 Hidden Cost · **Coffee Shop P&L Breakdown**
**Type:** wildcard · **Category:** artifact + extends winning hook**
**Hook visual:** Coffee-shop P&L statement on cream paper. Each line item itemised with running totals.
**Artifact copy:**
```
SAMPLE: COFFEE SHOP MONTHLY P&L

Sales (cup price ₱150 × 1,200)   ₱180,000
Beans / milk                     ₱ 36,000
Rent                             ₱ 35,000
Staff (2 baristas)               ₱ 28,000
GrabFood commission              ₱ 24,000
Excel/POS workarounds            ₱  4,500
──────────────────────────────────────
PROFIT                           ₱ 52,500
```
**Headline:** How much is your profit?
**Sub-headline:** StoreHub PH replaces three of these line items with one. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Roboto Mono / monospace body. Highlight the three replaceable lines (commission + workarounds + manual reports buried inside staff cost) in StoreHub orange.
**Hypothesis:** Extends the proven `howmuchisyourprofit_coffee` PH winner with sharper artifact execution to lift Won%.

### 🛑 C_016 — T9 Hidden Cost · **Karinderya Cash-Drawer Leak**
**Type:** wildcard · **Category:** observational artifact**
**Hook visual:** Open cash drawer photographed from above, peso bills laid out, with a transparent overlay showing red "leak" callouts: "₱40 under-rung · ₱85 missed loyalty · ₱200 reconciliation gap · ₱35 voided wrong". Total: "₱360 today · ₱10,800 this month."
**Headline:** Where your cash quietly walks out.
**Sub-headline:** StoreHub catches every one. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt for the cash-drawer base photo — *"Top-down photo of a Filipino karinderya wooden cash drawer open, peso bills and coins, daylight, documentary."* Add red callout overlays as primitives.

---

### ✅ C_017 — T2 New Chapter · **Just Opened? Make POS the Cheapest Item**
**Type:** safe · **Direct New-Chapter execution**
**Hook visual:** Cream paper checklist of opening expenses, POS row highlighted as the smallest line, ₱21,000-off badge in corner.
**Artifact copy:**
```
OPENING WEEK
Renovation             ₱200,000
Kitchen                ₱150,000
Signage                ₱ 25,000
Staff training         ₱ 15,000
─────────────────────
POS (StoreHub)         ₱ 22,995/yr  ← ₱21,000 OFF
```
**Headline:** POS is the last thing on your list. Make it the cheapest.
**Sub-headline:** ₱21,000 off StoreHub hardware bundle. While supplies last.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** PH `Independenceday_P21000_promo` style execution + opening-checklist framing drives SQL%.

### ✅ C_018 — T2 New Chapter · **Renovation Invoice with POS Highlighted**
**Type:** safe · **Artifact-leaning**
**Hook visual:** Photo of a real-looking contractor's invoice/quotation page. POS row circled with red Sharpie.
**Headline:** The line you didn't think to negotiate.
**Sub-headline:** StoreHub from ₱63/day. ₱21,000 off this month.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Close-up photo of a contractor's hand-stamped quotation/invoice for restaurant renovation, peso amounts, with one row circled in red sharpie, documentary, 35mm."*

### ✅ C_019 — T2 New Chapter · **Empty Pre-Opening Restaurant Hero**
**Type:** safe · **Aspirational-but-grounded**
**Hook visual:** Wide photo of a Filipino restaurant interior, just before opening. Owner standing alone at the counter in a clean uniform. Signage installed but lights at half. POS visible on the counter, partially out of focus.
**Headline:** Open with the #1 POS.
**Sub-headline:** 17,000+ SEA merchants. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Wide photo of empty pre-opening Filipino restaurant interior, owner standing alone at counter, signage installed, lights at half intensity, golden hour through window, documentary, 35mm."*

### ✅ C_020 — T2 New Chapter · **Grand-Opening Countdown Checklist**
**Type:** safe · **Checklist artifact + lechon hero**
**Hook visual:** Stylised countdown checklist on a white card. Above it, a small lechon photo. POS marked as final ticked item.
**Artifact copy:**
```
GRAND OPENING — 7 DAYS TO GO
[✓] Lechon supplier confirmed
[✓] Staff hired
[✓] Permits filed
[✓] Signage up
[✓] StoreHub set up
```
**Headline:** Last item. First in importance.
**Sub-headline:** StoreHub PH. From ₱63/day. Set up in 7 days.
**CTA:** BOOK A FREE DEMO NOW

---

### 🛑 C_021 — T12 Milestone Math · **Week-1 Itemised Receipt**
**Type:** wildcard · **Category:** artifact + math**
**Hook visual:** Cream-paper receipt artifact. List of opening-week expenses with pesos right-aligned, POS row highlighted in orange. Caveat handwritten line at the bottom.
**Artifact copy:**
```
WEEK 1 EXPENSES
Renovation                ₱200,000
Kitchen                   ₱150,000
Signage                   ₱ 25,000
Staff training            ₱ 15,000
Insurance                 ₱  4,200
POS (StoreHub)  ₱63/day   ← pays you back
"One of these pays you back."
```
**Headline:** You saved where it counted.
**Sub-headline:** StoreHub PH. From ₱63/day. Set up in 7 days.
**CTA:** BOOK A FREE DEMO NOW

### 🛑 C_022 — T12 Milestone Math · **90-Day Survival Math**
**Type:** wildcard · **Category:** gut-punch + math**
**Hook visual:** Dark cinematic photo — a Filipino restaurant in low light at the end of service, lights dimming, owner sitting at the counter looking at receipts. Text overlay in white.
**Headline:** First 90 days decide the next 10 years.
**Sub-headline:** ₱63/day buys the system. The rest is on you.
**Supporting numbers (small white panel):**
- 90-day setup with StoreHub: 7 days
- 90-day cost: ₱5,670
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Cinematic photo of a Filipino restaurant interior in low light at the end of service, owner sitting at the counter looking at receipts, warm tungsten light, documentary, 35mm, shallow depth of field."*

### 🛑 C_023 — T12 Milestone Math · **Year-2 Anniversary Math**
**Type:** wildcard · **Category:** gut-punch + math**
**Hook visual:** Same cinematic dark Filipino restaurant photo (different angle), but now with the storefront more prominently visible. Owner standing in front, hand on glass.
**Headline:** Year 1: you survived.
**Sub-headline:** Year 2 ran on StoreHub, not commissions. Which one are you closing?
**Supporting numbers (white 90% opacity panel, bottom-right):**
- Year 1 GrabFood commissions: ₱478,200
- Year 2 with StoreHub: ₱22,680
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Cinematic photo of a Filipino restaurant storefront at dusk, owner standing in front looking inside, muted tones, wide lens, documentary."*
**Hypothesis:** Extends MY Batch 2 C_012 cinematic gut-punch into a PH renewal-window context.

### 🛑 C_024 — T12 Milestone Math · **Location #2 Expansion Math**
**Type:** wildcard · **Category:** aspirational math**
**Hook visual:** Two storefront photos side-by-side — same brand, two locations, "Location #1" and "Location #2" labels. Connected by a thin horizontal line with a ₱63/day milestone marker in the middle.
**Headline:** Location 2 in 6 months. Not 14.
**Sub-headline:** Same dashboard. Same StoreHub. Two stores.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Use a single `G()` prompt — *"Two storefront photos of the same Filipino F&B brand, side by side, daylight, documentary, 35mm."*

---

### ✅ C_025 — T7 Cultural Pride · **Lechon Hero**
**Type:** safe · **Cultural specificity**
**Hook visual:** Full-bleed close-up overhead shot of whole lechon on a banana-leaf-lined platter, charred crackling skin, warm light. Bottom 35% gradient overlay for the headline.
**Headline:** Your lechon. Our tech.
**Sub-headline:** The POS built for Filipino F&B. Demo in 15 minutes.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Overhead close-up shot of whole Filipino lechon on a banana-leaf-lined platter, charred crackling skin, natural warm daylight, documentary food photography, 40mm, no text or branding."*

### ✅ C_026 — T7 Cultural Pride · **Jeepney Metaphor**
**Type:** safe · **Cultural metaphor + product**
**Hook visual:** Cinematic photo of a vintage jeepney parked next to a modern restaurant with a tablet POS visible inside. Wide composition.
**Headline:** Old reliable runs the country. Now run yours on something modern.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Cinematic photo of a vintage colourful Filipino jeepney parked next to a modern small restaurant in Manila, tablet POS visible through the window, golden hour, documentary, 35mm."*

### ✅ C_027 — T7 Cultural Pride · **Cafe → Restaurant Ladder**
**Type:** safe · **Three-panel narrative**
**Hook visual:** Three-panel evolution: (1) Filipino cafe counter with espresso machine + barista (2) carinderia kitchen (3) full restaurant dining room. Same StoreHub tablet visible in each. Subtle connecting visual element (e.g. a single line through all three).
**Headline:** From cafe to restaurant. Same dashboard.
**Sub-headline:** StoreHub grows with you. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Three `G()` prompts — *"Documentary photo of a small Filipino cafe counter, espresso machine, pastry display under glass, friendly Pan-Asian Filipino barista in apron, morning daylight, 35mm, candid."* / *"Photo of a Filipino carinderia kitchen, midday rush, documentary."* / *"Photo of a full Filipino restaurant dining room, lunchtime, documentary."*
**Note (2026-04-28 correction):** Previously labelled "Sari-sari → Restaurant Ladder". StoreHub does not support the sari-sari segment, so the first rung is a small Filipino cafe instead. Concept renamed to `cafe-ladder`. Frame names + manifest entries + ad-copy updated accordingly. First panel image regenerated.

### ✅ C_028 — T7 Cultural Pride · **Halo-halo Morning Rush**
**Type:** safe · **Documentary-style**
**Hook visual:** Documentary photo of a halo-halo or palengke food stall during morning rush, customers, vendor mid-action, POS tablet subtly visible on the counter.
**Headline:** Built for the rush.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** `G()` prompt — *"Documentary photo of busy Filipino halo-halo or palengke food stall during morning rush, customers in line, vendor mid-action, small tablet POS visible on the counter, 35mm, candid."*

---

### ✅ C_029 — T6 Social Proof · **Wall of PH F&B Logos**
**Type:** safe · **Logo grid**
**Hook visual:** Tightly packed grid of 30+ real PH F&B merchant logos (real or representative), monochrome treatment. Subtle StoreHub orange accent line at top.
**Headline:** 300+ PH F&B brands run StoreHub.
**Sub-headline:** From ₱63/day. Built locally, scaled regionally.
**CTA:** BOOK A FREE DEMO NOW
**Pencil notes:** Use real merchant logos from `Input Files/Past ads/` if available, otherwise generic representative logos. Confirm permission before final export.

### ✅ C_030 — T6 Social Proof · **Map of Manila / Cebu / Davao**
**Type:** safe · **Geographic proof**
**Hook visual:** Stylised three-city map of the Philippines with merchant pins concentrated in Metro Manila, Cebu, Davao. Pin count ticker in corner.
**Headline:** From Manila to Davao. We're already there.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW

### ✅ C_031 — T6 Social Proof · **Specific Outcome Card (no face, no quote)**
**Type:** safe · **Anonymous-outcome proof**
**Hook visual:** Clean white card on cream background. Bold outcome stat. Brand name only — no face, no quote.
**Artifact copy:**
> **Binq PH cut closing time from 2hrs to 20mins.**
> 6 outlets · F&B · 18 months on StoreHub.
**Headline:** A 2-hour problem. Now 20 minutes.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW
**Hypothesis:** Outcome-as-proof without the failed talking-head format. Specific, anonymous, structurally clean.

### ✅ C_032 — T6 Social Proof · **Scale-as-Proof Minimal**
**Type:** safe · **Numerical proof**
**Hook visual:** Three giant numbers stacked vertically on cream. Minimal — typography is the visual.
**Artifact copy:**
```
17,000  merchants
     3  countries
     1  POS
```
**Headline:** 17,000 merchants. 3 countries. 1 POS.
**Sub-headline:** StoreHub PH. From ₱63/day.
**CTA:** BOOK A FREE DEMO NOW

---

## 5 · Pencil.dev execution checklist

For each of the 32 concepts above:

1. `get_editor_state()` — confirm clean slate
2. `open_document("/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/SH PH ads batch 1.pen")` — create the new file
3. `get_guidelines("web-app")` and `get_style_guide_tags()` — load brand styles
4. For each concept, build **3 frames** (1080×1080, 1920×1080, 1080×1920) using `batch_design()`
5. For wildcards/safe-with-photo concepts that need AI imagery, use the `G()` operation with the prompts written in each concept's "Pencil.dev notes"
6. After each frame: `get_screenshot()` and run the 9-point QA in §6 below. If any check fails, redesign before moving on.
7. Record node ID + status in `data/iterations/PH-1/creative_manifest.json`

**Frame-naming in the .pen file:** `C_{NNN} | {theme_id} | {concept_short} | {format}`

---

## 6 · Visual QA — run after every single frame

**Readability (thumbnail test — 250×250px):**
- [ ] 1. Headline is readable at 250px without zooming
- [ ] 2. Headline is the biggest element on the canvas

**Layout:**
- [ ] 3. < 10% of the canvas is unused empty space without design intent
- [ ] 4. Background covers 100% edge-to-edge — no white borders, no floating centred column

**Brand:**
- [ ] 5. Colours match `config/brand.json` exactly (orange `#ff9419`, black `#2f2922`)
- [ ] 6. Logo present bottom-corner; CTA button present with "BOOK A FREE DEMO NOW" in ALL CAPS

**Typography:**
- [ ] 7. Headline Barlow Black, line spacing 1.1–1.25, ≤ 2 lines
- [ ] 8. Sub-headline + body in Sentence case (never Title Case, never ALL CAPS); CTA in ALL CAPS

**PH-specific:**
- [ ] 9. Currency symbol is ₱ (or "PHP"), never RM or $
- [ ] 10. **Wildcards only:** Could this ad be mistaken for a standard StoreHub promo card? → if YES, redesign

A frame is complete only when all applicable checks return TRUE.

---

## 7 · After production

1. Save the `.pen` file: `ads/SH PH ads batch 1.pen`
2. Export all 96 PNGs into `ads/batches/PH-batch_001/` with the naming convention in §3
3. Write ad-copy markdown: `ads/batches/PH-batch_001/ad-copy.md` — mirror the MY Batch 2 format (Primary Text / Headline / Description per concept)
4. Save `data/iterations/PH-1/creative_manifest.json` with all node IDs and QA statuses
5. Hand off to media buyer for Meta upload
6. Run `python3 scripts/cycle_check.py --mark-launched --market PH` after upload
7. Wait 14 days → results review

---

## 8 · What PH Batch 1 is actually testing (one-line version)

> **Does the proven PH ₱63/day price-anchor scale further when paired with PH-localised cultural cues, and do the two MY structural insights (artifact format + milestone math) generalise into the PH market?**
>
> Answer comes from comparing T4 (control) vs T11 (artifact transplant from MY) head-to-head on CPSQL, plus T7 (PH-localised cultural) vs T6 (logo-only proof) on Won%. The remaining themes (T5, T9, T2, T12) are independent secondary bets judged on their own benchmarks.

---

## 9 · Pre-launch hard gates

- **C_005** uses real "JobStreet" wording — confirm with legal whether the visual treatment risks IP claim. Use generic "Job Listing" chrome if unsure.
- **C_007** uses Viber UI mimicry — confirm Meta won't flag as deceptive content. $5–10 preflight before scaling.
- **C_008** BIR form — confirm StoreHub PH actually holds BIR accreditation before claiming it. Verify pricing claim "₱63/day" reflects current public PH pricing page.
- **C_021–C_024** all reference renewal/year-math numbers — finance team must approve the figures shown (e.g. ₱478,200 GrabFood commission, ₱22,680 StoreHub yearly).
- **C_029** logo grid — every logo must have written use-permission for paid Meta placement.
- **C_031** "Binq PH" outcome — confirm the merchant exists in PH and has signed a testimonial release.

---

## 10 · Concept index (cross-reference)

| ID | Theme | Type | Concept | AI image required |
|---|---|---|---|---|
| C_001 | T4 | safe | ₱63 hero | no (typography + product render) |
| C_002 | T4 | safe | jeepney-fare | optional |
| C_003 | T4 | safe | daily-coin-stack | yes |
| C_004 | T4 | safe | year-math-receipt | no (typography artifact) |
| C_005 | T11 | wildcard | jobstreet-ph | no (primitives) |
| C_006 | T11 | wildcard | gcash-receipt | no (primitives) |
| C_007 | T11 | wildcard | viber-chat | no (primitives) |
| C_008 | T11 | wildcard | bir-form | no (primitives) |
| C_009 | T5 | safe | cyf-hardware-tier | no (hardware library) |
| C_010 | T5 | safe | 30vs0 | no (typography) |
| C_011 | T5 | safe | midnight-vs-6pm | yes (×2) |
| C_012 | T5 | safe | logbook-vs-ipad | yes (×1) |
| C_013 | T9 | wildcard | annual-commission-audit | no (typography artifact) |
| C_014 | T9 | wildcard | sticky-note-pos | yes |
| C_015 | T9 | wildcard | coffee-shop-pl | no (typography artifact) |
| C_016 | T9 | wildcard | cash-drawer-leak | yes (overlays) |
| C_017 | T2 | safe | just-opened-checklist | no (typography artifact) |
| C_018 | T2 | safe | renovation-invoice | yes |
| C_019 | T2 | safe | empty-pre-opening | yes |
| C_020 | T2 | safe | grand-opening-countdown | yes (lechon thumbnail) |
| C_021 | T12 | wildcard | week-1-receipt | no (typography artifact) |
| C_022 | T12 | wildcard | 90-day-survival | yes |
| C_023 | T12 | wildcard | year-2-anniversary | yes |
| C_024 | T12 | wildcard | location-2-math | yes |
| C_025 | T7 | safe | lechon-hero | yes |
| C_026 | T7 | safe | jeepney-metaphor | yes |
| C_027 | T7 | safe | cafe-ladder | yes (×3) |
| C_028 | T7 | safe | halo-halo-rush | yes |
| C_029 | T6 | safe | logo-wall | no (logo library) |
| C_030 | T6 | safe | manila-cebu-davao | no (map illustration) |
| C_031 | T6 | safe | outcome-card | no (typography) |
| C_032 | T6 | safe | scale-numbers | no (typography) |

**Total AI image generations needed:** ~22 unique prompts × 3 ratios variants where reused = budget ~30–40 G() calls. Most concepts (15/32) are typography/primitive-only and require no AI imagery.

---

# 11 · PROMPT FOR PENCIL.DEV LLM (next-session handoff)

> Copy everything between the `=== BEGIN PROMPT ===` and `=== END PROMPT ===` markers into the ad-creative-generator agent in your new Claude Code session (where the Pencil MCP `mcp__pencil__*` tools are loaded).

=== BEGIN PROMPT ===

## ROLE
You are a Pencil.dev ad creative production agent for StoreHub Philippines. You will produce 32 ad concepts × 3 formats = 96 final frames for PH Batch 1. Every frame must pass a 10-point QA gate before you move to the next one. You do not improvise concepts — you execute the brief verbatim.

## INPUTS TO READ FIRST (in this order, do not skip)
1. `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/PH-batch_001/production_prompt.md` — §1–§10 of this brief. All 32 concept specs live in §4.
2. `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/PH-batch_001/theme-analysis.md` — performance rationale per theme.
3. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/brand.json` — colours, typography, logo, imagery rules, asset library paths.
4. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/creative_themes.json` — themes T2, T4, T5, T6, T7, T9, T11, T12 definitions.

Do NOT read any other files until you have read these four.

## OUTPUTS (deliverables)
| Path | What |
|---|---|
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/SH PH ads batch 1.pen` | Pencil.dev document with all 96 frames |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/PH-batch_001/[concept_id]_[format].png` | 96 exported PNGs |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/PH-batch_001/ad-copy.md` | Meta ad copy per concept |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/data/iterations/PH-1/creative_manifest.json` | Manifest |

## THE 32 CONCEPTS (iterate this array in order)
See §10 of the production prompt for the full table. Render in concept order C_001 → C_032 to lock in the safe baseline (T4, T5, T6, T7, T2) before the wildcards (T9, T11, T12).

## NON-NEGOTIABLE RULES
- **Colours (exact):** `#ff9419` orange, `#2f2922` black. Accents only from brand.json approved list.
- **Fonts:** Headline = Barlow Black · Sub = Open Sans Semibold · Body = Open Sans Regular · CTA = Open Sans Bold ALL CAPS.
- **CTA text (verbatim):** `BOOK A FREE DEMO NOW` — in ALL CAPS, on an orange (#ff9419) or pink (#ff546f) pill button.
- **Logo:** present on every frame in bottom corner, small.
- **Faces:** Pan-Asian only, with Filipino specificity preferred.
- **Photo backgrounds:** blur range 40–60. Busy backgrounds get 70–90% opacity colour panel behind text.
- **Three formats per concept:** 1080×1080, 1920×1080, 1080×1920.
- **Currency:** ₱ (peso) only. No RM, no $.
- **Anti-patterns (auto-fail):** orange split card with POS on pedestal · centred POS on plain orange · diagonal CYF split with VS badge · talking-head testimonial quote cards · holiday-themed creative without a hard offer attached.

## EXECUTION LOOP (run once per concept, 32 times total)
For each concept in §10:
1. `get_editor_state()`
2. `open_document("/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/SH PH ads batch 1.pen")` (creates the file on first concept, reopens on subsequent)
3. `get_guidelines("web-app")`
4. Read concept §4.{concept.id}. Extract hook, headline, sub, body, AI prompts.
5. For each format in [1080×1080, 1920×1080, 1080×1920]: build the frame using `batch_design()`. If concept needs AI imagery, call `G(frame_id, "ai", PROMPT)` using the EXACT prompt from §4.
6. After every frame: `get_screenshot()` and run the 10-point QA (§6 of the production prompt). If any check fails → redesign.
7. Record node_id + QA pass state in the in-memory manifest.
8. After all 32 × 3 frames: write ad-copy.md and creative_manifest.json.

## ERROR HANDLING
- If `G()` returns Western faces or off-brief imagery, rerun with sharper noun constraints. Do not accept off-brief.
- If `batch_design()` fails on an artifact concept, fall back to primitive shape composition — C_004, C_005, C_006, C_008, C_013, C_015, C_017, C_021, C_031, C_032 are largely primitive constructions.

## STOP CONDITIONS — surface to user if:
- Any brand file is missing or malformed.
- StoreHub PH BIR-accreditation cannot be verified before C_008 ships.
- Pricing claim (₱63/day) doesn't match current public PH pricing page.
- More than 3 wildcards fail the §6.10 wildcard-novelty QA after two redesigns.

## WHAT SUCCESS LOOKS LIKE
- 96 frames saved to `ads/SH PH ads batch 1.pen`.
- 96 PNGs exported to `ads/batches/PH-batch_001/`.
- `ad-copy.md` mirrors MY Batch 2 ad-copy format with Primary Text / Headline / Description per concept.
- `creative_manifest.json` lists all 96 frames, each with `qa_passed: true`.
- 20 safe / 12 wildcard split confirmed in the manifest counts.

=== END PROMPT ===
