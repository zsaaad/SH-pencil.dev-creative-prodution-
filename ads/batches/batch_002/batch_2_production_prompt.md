# Batch 2 — Creative Production Prompt (Pencil.dev)

**Iteration:** 2
**Market:** MY EN (primary) → PH EN (secondary, after MY launch validates concepts)
**Date drafted:** 2026-04-21
**Run window:** launch after production → 14-day test cycle
**Total concepts:** 12 (6 safe + 6 wildcard)
**Total output files:** 36 (each concept × 1080×1080 + 1920×1080 + 1080×1920)
**Control ad that must be beaten:** `S1_EN_Batch 1_competitive contrast - job post_nootp`
**Control benchmark:** CPSQL RM358.92 · SQL% 28.6% · CPL RM89.73 · CPMQL RM102.55

---

## 1 · Why this batch looks the way it does

Batch 1 ran from 1–20 April 2026 at RM5,165 spend across 20 creatives and 8 themes. The results were binary: 3 themes worked, 5 did not.

| Theme | Batch 1 signal | Batch 2 decision |
|---|---|---|
| T5 Competitive Contrast (job post) | **CPSQL RM358.92 · SQL% 28.6%** — best in batch | **Scale + extend** |
| T7 Cultural Pride (kopitiam) | CPL RM53 (best), but 64 clicks / 0 leads — LP gap | **Keep theme, fix LP match** |
| T2 New Chapter (opening expenses) | 19 leads, MQL 84.2% — but SQL% fell 10% → 5.3% at scale | **Evolve into T12 Milestone Math** |
| T1 Pain Amplification | 0 leads across 3 variants | **Retired (unless wrapped in T11)** |
| T4 The Math | 0 leads across 3 variants | **Retired as standalone — survives only inside T12** |
| T6 Social Proof | RM2.74 spend — insufficient runway | **Deferred until asset library wired** |
| T8 Aspirational Self | 1 lead, 0 SQL | **Deprioritised** |
| T10 Value Unlocked | 0 SQL, weak engagement | **Deprioritised** |

**Structural learning:** the Batch 1 winner (`job post`) didn't win because of the competitive-contrast message — it won because it looked like a real artifact, not an ad. Batch 2 isolates that structural insight as a new theme: **T11 Artifact Native** (added to `config/creative_themes.json`).

**Second structural learning:** the `opening expenses` creative pulled volume from the milestone hook but couldn't qualify leads because the math wasn't specific enough. Batch 2 introduces **T12 Milestone Math** — the fusion of emotional milestone + concrete number — to fix that gap.

---

## 2 · Themes in Batch 2

| Theme ID | Theme | Role | Concepts |
|---|---|---|---|
| **T11** | Artifact Native | Primary wildcard test — scale the structural insight | 4 |
| **T5** | Competitive Contrast | Exploit winner — extend beyond job-post with non-artifact executions | 3 |
| **T7** | Cultural Pride | Fix + scale — LP-aligned, volume driver | 3 |
| **T12** | Milestone Math | New fusion theme — test SQL% thesis | 2 |

**Safe/Wildcard split (non-negotiable):** 6 safe + 6 wildcard.

- **T5 (all 3):** safe
- **T7 (all 3):** safe
- **T12 (all 2):** 1 safe + 1 wildcard
- **T11 (all 4):** wildcard (artifact format is structurally unusual by definition)

Result: 7 safe, 5 wildcard → pull one T5 into the wildcard column by rendering it as a metaphor execution to hit 6/6. See concept specs below — **C_005 (Competitive Contrast · Everest) is wildcard category `metaphor`**.

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

**Imagery:** Pan-Asian faces only. No Western faces, no stock-photo expressions. Photo backgrounds must be blurred (40–60). Busy backgrounds get a 70–90% opacity colour panel behind text.

**Logo + CTA:** every frame — even wildcards — must include the StoreHub logo (bottom corner, small) and the CTA button. Default CTA copy: **"BOOK A FREE DEMO NOW"**.

**Anti-patterns to avoid (will fail QA):**
- ❌ Orange split card with POS on pedestal (overused)
- ❌ Centered POS on plain orange background
- ❌ Diagonal CYF split with VS badge (already maxed out)
- ❌ Text in narrow centre column with dead-space margins
- ❌ Small floating "55% Off" corner badges
- ❌ Headlines below minimum font size (looks "about right" → too small)

**Naming convention for exports:**
```
S2_EN_Batch2_[theme_short]_[concept_name]_[format]_nootp
```
Examples:
- `S2_EN_Batch2_artifact_whatsapp-11pm_1x1_nootp`
- `S2_EN_Batch2_compcontrast_google-review_9x16_nootp`

---

## 4 · Concept specs (12 concepts)

> For each concept below: produce **three format variants** (1:1 / 16:9 / 9:16) using the creative brief. Every variant must pass the Visual QA checklist in §5 before moving to the next concept.

---

### 🛑 C_001 — T11 Artifact Native · **The Hiring Ad v2**
**Creative type:** wildcard · **Category:** meme-native/artifact
**Why we're making this:** the Batch 1 winner's format, evolved. Same artifact (classifieds listing) but with sharper copy and retail vertical added so we're not only addressing F&B.

**Hook visual (second 1):** Looks like a real JobStreet / Mudah.my classifieds card. White background, plain grey borders, pagination UI at the bottom, small "Posted 2 hours ago" timestamp. No StoreHub colours visible until the CTA pill at the bottom.

**Artifact copy (the ad IS this):**
> **HIRING IMMEDIATELY — Retail Operations Manager (1 position)**
> Responsibilities: Manage POS · track inventory across 2 stores · run loyalty programme · reconcile daily sales · handle delivery orders · file monthly reports
> Salary: RM4,800/month + EPF + medical
> Start date: ASAP
>
> **OR — StoreHub POS from RM3.40/day does all of it.**

**Headline on the artifact:** *(inside the "job title" field)* — 'One person who can do the work of five systems'
**Sub-headline (in smaller artifact text):** Retail · F&B · Multi-outlet
**CTA (outside the artifact, as a reveal):** BOOK A FREE DEMO NOW
**Target segment:** MY merchants earning RM30k–200k/month, F&B + retail

**Pencil.dev generation notes:** build the fake classifieds card as a raw rectangle element (not an image) so text is pixel-sharp. Use `G()` AI generation only for optional vendor-logo mockups. Reference image: `ads/batches/batch_001/beep-T5a-competitive-contrast-commission-war.png` for layout mood — but flatter and more document-like.

**Hypothesis:** "We believe MY F&B+retail merchants will recognise a classifieds listing before a promo and will engage at SQL% ≥ 25% because the artifact format pre-qualifies intent — only merchants calculating the cost of a hire will read through."

**Success metric:** SQL% ≥ 25% · CPSQL ≤ RM360 at 1,000+ impressions

---

### 🛑 C_002 — T11 Artifact Native · **The Staff WhatsApp**
**Creative type:** wildcard · **Category:** meme-native/artifact
**Why:** WhatsApp is the most-used app for MY/PH merchants. An ad that looks like a genuine Boss↔Staff chat thread bypasses banner blindness entirely.

**Hook visual (second 1):** Pixel-accurate WhatsApp chat UI — green header "Restaurant Bosses 🍜" (4 members), default WhatsApp wallpaper, green outgoing bubbles on the right, white incoming on the left, 11:47PM timestamp.

**Chat copy (script the ad as a short thread):**
- `[11:42PM · Akmal]` boss still waiting for today's total ah
- `[11:43PM · Boss]` calculating lah
- `[11:44PM · Akmal]` 😭
- `[11:46PM · Akmal]` last month also like this
- `[11:47PM · Boss]` ya ya i'll look at StoreHub tomorrow

**Headline (appears OUTSIDE the chat, below):** When "tomorrow" becomes every night.
**Sub-headline:** StoreHub POS closes your day automatically. From RM3.40/day.
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B owners, 1–3 outlets, doing manual reconciliation

**Pencil.dev notes:** Use solid rectangles, rounded corners, exact WhatsApp green `#25D366` for header (critical for realism). Do not use the WhatsApp logo — use a neutral chat icon. Add a tiny "screenshot" crop shadow on the top-left and bottom-right to sell the screenshot illusion.

**Hypothesis:** "We believe F&B merchants who have had this exact conversation will pause on a WhatsApp-native artifact and convert to SQL at ≥ 20% because they are in the problem-recognition state the artifact depicts."

**Success metric:** CTR ≥ 1.2% · SQL% ≥ 20%

---

### 🛑 C_003 — T11 Artifact Native · **The Google Review Screenshot**
**Creative type:** wildcard · **Category:** artifact + gut-punch
**Why:** isolates the T11 artifact lever using real merchant social proof from the testimonial library (`/Users/zaidsaad/Desktop/Creative/testimonials for CC/`). Tests whether social-proof copy performs better inside a recognised native format (Google review) vs a traditional testimonial layout.

**Hook visual (second 1):** A Google review card — exact Google UI. 5-star rating, real merchant name "Binq Dessert", location pill "Hartamas · SS15 · SS2", "Posted 3 weeks ago", small "Helpful" / "Share" buttons greyed out underneath.

**Review text (copied from Binq testimonial library):**
> "Switched from our old POS 6 months ago. Queue times cut in half. Staff save 2 hours every night on closing. Inventory across 3 outlets finally reconciles. Only regret: we didn't do it sooner."
> — **Binq Dessert** · F&B · Multi-location

**Headline (below the card):** The review you'll leave in 6 months.
**Sub-headline:** 20,000+ merchants. 3 countries. 1 POS.
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B evaluators — in active consideration phase

**Pencil.dev notes:** Reference Google's card UI — white card, 4px rounded corners, small profile avatar top-left, review body in Roboto-style font (substitute Open Sans to stay brand-compliant). The magic is the card chrome — if it doesn't look like a Google card, the concept breaks. Avoid Google's logo/wordmark — use a neutral 5-star row.

**Hypothesis:** "We believe MY F&B owners comparing POS options read Google reviews as authoritative and will engage with a review-formatted ad at higher SQL% than a standard testimonial card, because the format itself signals peer validation."

**Success metric:** SQL% ≥ 20% · CPL ≤ RM80

---

### 🛑 C_004 — T11 Artifact Native · **The Month-End Receipt**
**Creative type:** wildcard · **Category:** artifact + hidden-cost
**Why:** translates T9 Hidden Cost into an artifact rendering. Forensic math delivered through a "fake monthly statement" that quantifies what the merchant is bleeding.

**Hook visual (second 1):** A Maybank / CIMB-style statement page — monospace font, clean header "Monthly Business Expenses — March 2026", line items with RM values right-aligned, a subtotal and a highlight bar at the bottom.

**Artifact copy:**
```
MONTHLY BUSINESS EXPENSES — MARCH 2026
──────────────────────────────────────────────
GrabFood commission (30% of RM14,000)      RM 4,200.00
FoodPanda commission (20% of RM7,500)      RM 1,500.00
Manual end-of-day reconciliation
  (46 hours × RM25/hour)                    RM 1,150.00
Stock discrepancy write-offs                RM   680.00
Missed loyalty redemptions                  RM   220.00
──────────────────────────────────────────────
TOTAL BLEEDING                              RM 7,750.00

StoreHub POS (monthly)                      RM   408.00
──────────────────────────────────────────────
```

**Headline (below or over the statement):** Which line are you cutting?
**Sub-headline:** StoreHub consolidates all of this into one dashboard.
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B merchants doing RM30k+/month with 2+ delivery platforms

**Pencil.dev notes:** Use Roboto Mono or a generic monospace substitute for the statement body to feel like a bank statement. Numbers right-aligned on a virtual column. The "TOTAL BLEEDING" row gets red/orange emphasis. The "StoreHub" row gets orange `#ff9419` highlight. No photo. No illustration.

**Hypothesis:** "We believe forensic cost-breakdown artifacts drive lower CPL than emotional pain ads because they convert vague discomfort into a specific, calculable reason to act — and MY merchants will engage at CPL ≤ RM65."

**Success metric:** CPL ≤ RM65 · SQL% ≥ 15%

---

### ✅ C_005 — T5 Competitive Contrast · **Everest Metaphor**
**Creative type:** wildcard · **Category:** metaphor
**Why:** isolates the competitive-contrast theme from the artifact format — tests whether the comparison logic alone wins, or whether the format was the real driver. If this underperforms T11 artifacts, the hypothesis is confirmed: format > message.

**Hook visual (second 1):** A cinematic photo of a small figure climbing a steep, snow-covered mountain — gradient sky, no brand present. Zero text in the top half.

**Headline (bottom third, large):** Running a restaurant shouldn't feel like climbing Everest.
**Sub-headline:** Trade manual work for one dashboard. StoreHub POS from RM3.40/day.
**Body bullets:** *(none — full-bleed metaphor shouldn't be crowded)*
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B operators in burnout mode — 1–2 outlets, no automation

**Pencil.dev notes:** Use `G()` AI image generation. Prompt: *"Cinematic photo, wide shot, tiny silhouette of a person climbing a steep snow-covered mountain ridge, dramatic grey-blue sky, diffused morning light, shot on Arri Alexa, shallow depth of field, documentary style, no text, no people's faces, no branding."* Apply 40 blur to the lower third only (safe-zone for text readability). Logo bottom-right, small white reversed.

**Hypothesis:** "We believe a metaphor-led comparison ad without artifact chrome will underperform artifact-format versions of the same theme, isolating 'format > message' as the driver of the Batch 1 job-post win."

**Success metric:** SQL% and CPSQL compared directly against C_001/C_002 (same theme, different format). Expected: this loses — which is the point.

---

### ✅ C_006 — T5 Competitive Contrast · **Split Screen (Manual vs StoreHub)**
**Creative type:** safe · **Category:** n/a
**Why:** extends the proven CYF pattern (Batch 1 referenced `CYF hardware split` as the safe champion) into a non-hardware comparison — manual stock count vs StoreHub dashboard. This tests whether the split-screen layout extends into operational-contrast territory.

**Hook visual:** Split 50/50 horizontally. **Left:** photo of a merchant at night with a clipboard, hand-counting stock on a dim storage shelf (warm tungsten light, desaturated). **Right:** StoreHub dashboard screenshot on a tablet — clean UI, stock count numbers, green "All reconciled" badge (bright, cool light).

**Headline (overlaid across both halves, middle):** Midnight. Or 30 seconds.
**Sub-headline:** Inventory reconciliation, automated. StoreHub POS from RM3.40/day.
**Body bullets (right panel only):**
- Real-time stock across all outlets
- Zero manual counts
- Alerts before you run out
**CTA:** BOOK A FREE DEMO NOW

**Pencil.dev notes:** Left side: `G()` prompt *"Photo of Southeast Asian merchant in warehouse at night, clipboard, counting boxes, warm tungsten light, documentary style."* Right side: use the hardware library — `F&B-MY-Merchant-Front.png` or a clean UI mockup. Brand compliance: both halves full-bleed; dividing line is a 2px orange stripe.

**Hypothesis:** "We believe operational split-screen comparisons will extend the proven hardware-CYF pattern into non-hardware territory and drive CTR ≥ 2.5% (vs 1.41% theme average in Batch 1)."

**Success metric:** CTR ≥ 2.5% · CPSQL ≤ RM400

---

### ✅ C_007 — T5 Competitive Contrast · **The Six-vs-One Stack**
**Creative type:** safe · **Category:** n/a
**Why:** directly evolves the proven `6 vs 1` hardware visual (ads/batches/batch_001/beep-T5b-competitive-contrast-6-vs-1.png) into software territory.

**Hook visual:** Left stack: 6 floating phone/tablet mockups labelled GrabFood, FoodPanda, ShopeeFood, manual POS, Excel, WhatsApp — all leaning chaotically, 40% desaturated. Right: a single StoreHub-branded tablet on a clean orange-to-white gradient background, perfectly centred, bright.

**Headline (centred between the stacks):** 6 tools. Or 1.
**Sub-headline:** StoreHub consolidates orders, inventory, delivery, loyalty, and reports.
**Body bullets:** *(none)*
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B merchants juggling ≥ 3 delivery platforms

**Pencil.dev notes:** Use Pencil.dev's stock hardware library for the centre tablet (`d3_pro_front_MY`). For the left stack, use generic phone illustrations from `SH ILLUSTRATIONS` library. Keep the central "6 tools. Or 1." headline at 110–140px Barlow Black so it dominates the canvas.

**Hypothesis:** "We believe a visual consolidation (6 vs 1) will beat the theme average CPSQL because it mirrors the 'Choose Your Fighter' winning pattern applied to software instead of hardware."

**Success metric:** CPSQL ≤ RM400

---

### ✅ C_008 — T7 Cultural Pride · **Kopitiam v2 (LP-Aligned)**
**Creative type:** safe · **Category:** n/a
**Why:** Batch 1 `cultural pride - kopitiam` drove 64 clicks at CPL RM53 — the best CPL in the batch — but 0 leads. That's a landing-page alignment problem, not a creative problem. Batch 2 keeps the winning hook but re-brief the copy so the ad explicitly promises what the LP delivers ("free demo", not an offer-first click).

**Hook visual:** Full-bleed close-up of a classic kopitiam breakfast — half-boiled eggs, kaya toast, kopi-o in a traditional mug — on a marble-top kopitiam table. Natural morning light, shallow depth of field, shot overhead. Zero brand chrome in the top 55%.

**Headline (bottom third, white on blurred edge):** Your kopi. Our tech.
**Sub-headline:** The POS built for Malaysian F&B. Demo in 15 minutes.
**CTA:** BOOK A FREE DEMO NOW

**Pencil.dev notes:** Use `G()` AI prompt: *"Overhead shot of traditional Malaysian kopitiam breakfast — kaya toast, two half-boiled eggs in a saucer, condensed milk coffee in a blue-rimmed porcelain mug, marble table, natural morning light, documentary food photography style, 40mm lens."* Bottom third gets a 70% opacity dark gradient overlay so the white headline reads cleanly.

**Critical:** LP must say "Book your free demo" to match the CTA — confirm with the LP owner before launch.

**Hypothesis:** "We believe CTA alignment between the ad and LP will unlock the proven CPL RM53 hook — converting the clicks into leads at ≥ 50% rate, holding theme CPL below RM70."

**Success metric:** CPL ≤ RM70 · Lead rate ≥ 50% of clicks · SQL% ≥ 15%

---

### ✅ C_009 — T7 Cultural Pride · **Mamak 2am**
**Creative type:** safe · **Category:** n/a
**Why:** extends Cultural Pride into a different Malaysian F&B archetype — mamak night-shift — to test whether the theme wins on cultural specificity broadly, or only on kopitiam specifically.

**Hook visual:** Low-angle shot inside a mamak restaurant at 2am — busy, warm fluorescent tubes overhead, roti canai being flipped in the foreground (motion blur), a line of customers in the background. A subtle StoreHub tablet visible in the corner of frame, unmissable but not hero.

**Headline:** 2am at your mamak.
**Sub-headline:** StoreHub handles the night rush so you can focus on the roti.
**CTA:** BOOK A FREE DEMO NOW

**Pencil.dev notes:** `G()` prompt: *"Low-angle photo inside a busy Malaysian mamak restaurant at 2am, warm fluorescent lighting, roti canai being flipped mid-air with motion blur, crowd of late-night customers in background, candid documentary style, 35mm lens."* Tablet placement: inpaint a small POS tablet on the back counter using Pencil.dev compose tools — must be visible on a close look but not hero.

**Hypothesis:** "We believe cultural specificity (mamak-at-2am) will generalise the T7 win beyond kopitiam and hold CPL below RM70 across Malaysian F&B archetypes."

**Success metric:** CPL ≤ RM70

---

### ✅ C_010 — T7 Cultural Pride · **Pasar Malam Gerai**
**Creative type:** safe · **Category:** n/a
**Why:** tests whether the T7 theme extends into **retail/hawker** verticals, not just sit-down F&B. Pasar malam (night market) gerai is a high-density MY merchant archetype under-served by English POS ads.

**Hook visual:** A single Malaysian pasar malam stall at night — string lights above, grilled satay on a smoking bbq in the foreground, the merchant mid-action serving a customer. The customer's phone is scanning a QR code on a small StoreHub-branded countertop sign. Warm crowd energy.

**Headline:** Your gerai. Our tech.
**Sub-headline:** QR ordering, daily reports, loyalty — all from RM3.40/day.
**CTA:** BOOK A FREE DEMO NOW

**Pencil.dev notes:** `G()` prompt: *"Candid photo of a Malaysian pasar malam satay stall at night, string lights, smoke from the grill, merchant serving a customer, customer scanning a QR code with their phone, warm evening light, documentary, 35mm."* If the inpainting is unreliable, substitute with a hero tablet hardware shot on a neutral background and reserve the pasar malam scene for the supporting illustration.

**Hypothesis:** "We believe extending T7 into retail/hawker archetypes will reveal a lower-CPL audience segment than F&B sit-down, driving overall theme CPL below RM60."

**Success metric:** CPL ≤ RM60

---

### ✅ C_011 — T12 Milestone Math · **Week 1 Expense List**
**Creative type:** safe · **Category:** n/a
**Why:** direct evolution of the Batch 1 `opening expenses` volume driver — keeps the milestone hook but adds the sharper math anchor that T4 was missing. Hypothesis: fusion fixes the SQL% qualification drop we saw at scale.

**Hook visual:** Vertical list on a clean cream background — looks like a real opening checklist taped to a wall. Handwritten-font italic overlays (Caveat font for the "notes"). Each line is a line-item the merchant actually paid for.

**Artifact copy:**
```
OPENING WEEK EXPENSES
─────────────────────
Renovation                 RM 48,000
Kitchen equipment          RM 25,000
Signage + branding         RM  3,500
Staff training             RM  1,200
Insurance                  RM    850
POS system (StoreHub)      RM    102/week
─────────────────────
"One of these pays you back."
```

**Headline (above or below):** You saved where it counted.
**Sub-headline:** StoreHub POS from RM3.40/day. Set up in 7 days.
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B merchants who just opened (0–90 days) or are about to open

**Pencil.dev notes:** cream background `#FFF8EA`. Use Open Sans for the list, Caveat Italic for the handwritten "One of these pays you back." line. No photo, no illustration — just typography as the visual.

**Hypothesis:** "We believe attaching a concrete financial anchor (the RM102/week highlight) to the milestone moment (opening-week list) will lift SQL% above 10% vs the 5.3% floor set by the non-math opening-expenses variant in Batch 1."

**Success metric:** SQL% ≥ 10% · CPSQL ≤ RM700

---

### 🛑 C_012 — T12 Milestone Math · **The Year-2 Math**
**Creative type:** wildcard · **Category:** gut-punch
**Why:** hits an un-addressed milestone (renewal/1-year mark) that existing StoreHub campaigns don't target. Tests whether milestone-math extends into the retention window.

**Hook visual:** A single cinematic shot — a closed restaurant, lights off, "For Lease" sign in the window, shot from across the street in the rain. Muted palette. Single human figure turning away from the door. No brand present in the top 60%.

**Headline (centred on the image, bold):** Year 1: you survived.
**Sub-headline (below, smaller):** Year 2 ran on StoreHub, not commissions. Which one are you closing?
**Supporting numbers (bottom-right, in a discreet white panel):**
- Year 1 GrabFood commissions: **RM 21,900**
- Year 2 with StoreHub POS: **RM 1,240**
**CTA:** BOOK A FREE DEMO NOW
**Target segment:** MY F&B merchants in months 10–18 (renewal-window audience)

**Pencil.dev notes:** `G()` prompt: *"Cinematic rain scene at dusk, closed-down Malaysian shop with 'For Lease' sign in window, single person figure with umbrella walking away, muted blue-grey colour palette, wide lens, shallow depth of field, documentary photography."* Overlay the white number panel bottom-right at 90% opacity so the numbers punch but the scene stays dominant.

**Verify before publishing:** confirm the RM 21,900 vs RM 1,240 math with the finance team. If the exact numbers aren't defensible, replace with a conservative version.

**Hypothesis:** "We believe a milestone-math ad targeting the Year-1 renewal window will reach a higher-intent audience than opening-stage ads (they have P&L data to validate the math) and will drive SQL% ≥ 20% — the highest in Batch 2 at the cost of lower volume."

**Success metric:** SQL% ≥ 20% · lower acceptable volume than C_011

---

## 5 · Pencil.dev execution checklist

For each of the 12 concepts above:

1. `get_editor_state()` — confirm clean slate
2. `open_document("ads/iteration_2.pen")` — create the iteration file
3. `get_guidelines("web-app")` and `get_style_guide_tags()` — load brand styles
4. For each concept, build **3 frames** (1080×1080, 1920×1080, 1080×1920) using `batch_design()`
5. For wildcards that need AI imagery (C_005 Everest, C_008 Kopitiam, C_009 Mamak, C_010 Pasar Malam, C_012 Year-2), use the `G()` operation with the prompts written in each concept's "Pencil.dev notes"
6. After each frame: `get_screenshot()` and run the 9-point QA in §6 below. If any fails, redesign before moving on.
7. Record node ID + status in `data/iterations/2/creative_manifest.json`

**Frame-naming in the .pen file:**
`C_{NNN} | {theme_id} | {concept_short} | {format}`
Example: `C_001 | T11 | hiring-ad-v2 | 1x1`

---

## 6 · Visual QA — run after every single frame

Copy this checklist into the manifest row for each frame. **Do not move on until all 9 pass.**

**Readability (thumbnail test — 250×250px):**
- [ ] 1. Headline is readable at 250px without zooming
- [ ] 2. Headline is the biggest element on the canvas — not the product, not a badge

**Layout:**
- [ ] 3. < 10% of the canvas is unused empty space without design intent
- [ ] 4. Background (colour or image) covers 100% edge-to-edge — no white borders, no floating centred column

**Brand:**
- [ ] 5. Colours match `config/brand.json` exactly (orange `#ff9419`, black `#2f2922`)
- [ ] 6. Logo present bottom-corner; CTA button present with "BOOK A FREE DEMO NOW" in ALL CAPS

**Typography:**
- [ ] 7. Headline Barlow Black, line spacing 1.1–1.25, ≤ 2 lines
- [ ] 8. Sub-headline + body in Sentence case (never Title Case, never ALL CAPS); CTA in ALL CAPS

**Wildcard-specific (run on C_001, C_002, C_003, C_004, C_005, C_012 only):**
- [ ] 9. Could this ad be mistaken for a standard StoreHub promo card at a glance? → if YES, **the wildcard failed** and must be redesigned until the answer is NO

---

## 7 · After production

1. Save the `.pen` file: `ads/iteration_2.pen`
2. Export all 36 PNGs into `ads/batches/batch_002/` with the naming convention in §3
3. Write ad-copy markdown: `ads/batches/batch_002/ad-copy.md` — mirror the Batch 1 format so the upload operator has Primary Text / Headline / Description fields per ad
4. Save `data/iterations/2/creative_manifest.json` with all node IDs and QA statuses
5. Hand off to media buyer for Meta upload
6. Run `python3 scripts/cycle_check.py --mark-launched` after upload
7. Wait 14 days → `/ad-pipeline results 2` → `/ad-pipeline loop 2`

---

## 8 · What Batch 2 is actually testing (one-line version)

> **Is the job-post win a repeatable format (T11 Artifact Native) or a one-off message (T5 Competitive Contrast)?** Batch 2 answers this by running 4 artifact executions across different copy angles and 3 non-artifact competitive-contrast executions, then comparing CPSQL head-to-head. Whichever side wins determines whether Batch 3 scales the format or the message.

The other two themes (T7 Cultural Pride, T12 Milestone Math) are independent secondary bets — they extend or fix known patterns and are judged on their own success metrics, not against T11/T5.

---

# 9 · PROMPT FOR PENCIL.DEV LLM

> Copy everything between the `=== BEGIN PROMPT ===` and `=== END PROMPT ===` markers into the ad-creative-generator agent (or any LLM with access to the `mcp__pencil__*` tools). The prompt is self-contained and references this file + the repo configs by absolute path.

=== BEGIN PROMPT ===

## ROLE
You are a Pencil.dev ad creative production agent for StoreHub. You will produce 12 ad concepts × 3 formats = 36 final frames for Batch 2 of the creative testing programme. Every frame must pass a 9-point QA gate before you move to the next one. You do not improvise concepts — you execute the brief verbatim.

## INPUTS TO READ FIRST (in this order, do not skip)
1. `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/batch_002/batch_2_production_prompt.md` — §1–§8 of this file (the Batch 2 brief). All 12 concept specs live in §4.
2. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/brand.json` — colours, typography, logo, imagery rules, asset library paths.
3. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/creative_themes.json` — themes T5, T7, T11, T12 definitions (T11 + T12 are new, added 2026-04-21).
4. `/Users/zaidsaad/Desktop/Code/Pencil.dev/Input Files/SH Context.md` Section 13 — Wildcard Creative Framework.

Do NOT read any other files until you have read these four.

## OUTPUTS (deliverables)
| Path | What |
|---|---|
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/iteration_2.pen` | Pencil.dev document with all 36 frames |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/batch_002/[concept_id]_[format].png` | 36 exported PNGs |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/batch_002/ad-copy.md` | Meta ad copy (Primary Text / Headline / Description) per concept — mirror the Batch 1 format at `ads/batches/batch_001/ad-copy.md` |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/data/iterations/2/creative_manifest.json` | Manifest — see schema in §OUTPUT SCHEMA below |

## THE 12 CONCEPTS (iterate this array in order)
```
[
  { "id": "C_001", "theme": "T11", "type": "wildcard",  "name": "hiring-ad-v2",        "wildcard_category": "meme-native" },
  { "id": "C_002", "theme": "T11", "type": "wildcard",  "name": "staff-whatsapp",      "wildcard_category": "meme-native" },
  { "id": "C_003", "theme": "T11", "type": "wildcard",  "name": "google-review",       "wildcard_category": "meme-native" },
  { "id": "C_004", "theme": "T11", "type": "wildcard",  "name": "month-end-receipt",   "wildcard_category": "meme-native" },
  { "id": "C_005", "theme": "T5",  "type": "wildcard",  "name": "everest-metaphor",    "wildcard_category": "metaphor" },
  { "id": "C_006", "theme": "T5",  "type": "safe",      "name": "split-screen-manual-vs-storehub" },
  { "id": "C_007", "theme": "T5",  "type": "safe",      "name": "six-vs-one-stack" },
  { "id": "C_008", "theme": "T7",  "type": "safe",      "name": "kopitiam-v2" },
  { "id": "C_009", "theme": "T7",  "type": "safe",      "name": "mamak-2am" },
  { "id": "C_010", "theme": "T7",  "type": "safe",      "name": "pasar-malam-gerai" },
  { "id": "C_011", "theme": "T12", "type": "safe",      "name": "week-1-expense-list" },
  { "id": "C_012", "theme": "T12", "type": "wildcard",  "name": "year-2-math",         "wildcard_category": "gut-punch" }
]
```
Full creative brief for each concept is in §4 of the Batch 2 brief file (read it — do not paraphrase).

## NON-NEGOTIABLE RULES
- **Colours (exact):** `#ff9419` orange, `#2f2922` black. Accents only from brand.json approved list.
- **Fonts:** Headline = Barlow Black · Sub = Open Sans Semibold · Body = Open Sans Regular · CTA = Open Sans Bold ALL CAPS.
- **CTA text (verbatim):** `BOOK A FREE DEMO NOW` — in ALL CAPS, on an orange (#ff9419) or pink (#ff546f) pill button.
- **Logo:** present on every frame (even wildcards) in bottom corner, small. Use `StoreHub Logo_Full Orange.png` on light backgrounds; `StoreHub_Logo_Full Positive Colour Reverse.png` on dark or orange backgrounds.
- **Faces:** Pan-Asian only. No Western faces, no stock expressions, no Western cultural references.
- **Photo backgrounds:** blur range 40–60. On busy backgrounds, apply a 70–90% opacity colour panel behind text.
- **Three formats per concept, no exceptions:** 1080×1080, 1920×1080, 1080×1920. No other dimensions exist.
- **Font sizing per format (from §3 of the brief):**
  - 1:1 · headline 96–140px · sub 44–60px · body 20–28px · padding ≤32px (safe) / 0px (wildcard)
  - 16:9 · headline 96–130px · sub 44–60px · body 20–28px · padding ≤48px (safe) / 0px (wildcard)
  - 9:16 · headline 130–180px · sub 52–72px · body 28–36px · UI-safe 250px top / 400px bottom
- **Headline capitalisation:** Title Case / Sentence case / ALL CAPS (ALL CAPS only for 1–3 word headlines).
- **Sub-headline + body:** Sentence case only. Never Title Case, never ALL CAPS.
- **Anti-patterns (auto-fail if used):** orange split card with POS on pedestal · centred POS on plain orange · diagonal CYF split with VS badge · narrow centre column with empty margins · tiny floating corner badges · any font below the minimums above.

## EXECUTION LOOP (run once per concept, 12 times total)

```
FOR each concept in THE 12 CONCEPTS:

  1. get_editor_state()
  2. open_document("/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/iteration_2.pen")
     (creates the file on first concept, reopens on subsequent ones)
  3. get_guidelines("web-app")
  4. get_style_guide_tags() → pick a style matching mood:
        - safe concepts  → clean / professional
        - wildcard:meme-native → native-feed / documentary
        - wildcard:metaphor → cinematic / minimal
        - wildcard:gut-punch → raw / documentary
  5. Read concept §4.{concept.id} in the brief file. Extract:
        hook_visual, headline, sub_headline, body_copy (or bullets),
        visual_concept (layout / background / mood), ai_generation_notes.
  6. FOR each format in [1080x1080, 1920x1080, 1080x1920]:
        a. find_empty_space_on_canvas()
        b. batch_design() — build the frame using the layout that matches
           the concept's `visual_concept.layout`:
              - product-hero / split / text-dominant / lifestyle →
                standard safe templates
              - absurdist-scene / metaphor / meme-native / cinematic →
                wildcard templates (see ad-creative-generator.md §Rendering Wildcards)
        c. If the concept needs AI imagery, call G(frame_id, "ai", PROMPT)
           using the EXACT prompt from the concept's "Pencil.dev notes" block.
        d. Apply the brand colours + fonts + CTA button + logo per §NON-NEGOTIABLE RULES.
        e. get_screenshot()
        f. Run the 9-point QA (§QA GATE below). If any check fails → redesign, do not proceed.
        g. Record node_id + QA pass state in the in-memory manifest array.
  7. Continue to next concept.

8. When all 12 concepts × 3 formats are complete:
   - Write ad-copy.md mirroring ads/batches/batch_001/ad-copy.md structure.
   - Write creative_manifest.json to the path in §OUTPUTS.
```

## QA GATE (9 checks — run on every frame before moving on)
1. [ ] Headline readable at 250×250px thumbnail without zooming.
2. [ ] Headline is the biggest element on the canvas.
3. [ ] < 10% of canvas is empty/dead space without design intent.
4. [ ] Background covers 100% edge-to-edge (no white borders, no centred narrow column).
5. [ ] Colours exactly match brand.json (`#ff9419` orange, `#2f2922` black).
6. [ ] Logo present in bottom corner; CTA button present with "BOOK A FREE DEMO NOW" in ALL CAPS.
7. [ ] Headline Barlow Black, line spacing 1.1–1.25, ≤ 2 lines.
8. [ ] Sub + body in Sentence case; CTA in ALL CAPS.
9. [ ] **Wildcards only:** Could this ad be mistaken for a standard StoreHub promo card? → if YES, it failed. Redesign.

A frame is complete only when all applicable checks return TRUE.

## OUTPUT SCHEMA — `data/iterations/2/creative_manifest.json`
```json
{
  "iteration": 2,
  "pen_file": "ads/iteration_2.pen",
  "safe_count": 6,
  "wildcard_count": 6,
  "total_created": 36,
  "created_at": "ISO-8601 timestamp",
  "control_ad_to_beat": "S1_EN_Batch 1_competitive contrast - job post_nootp",
  "control_benchmarks": { "cpsql_rm": 358.92, "sql_pct": 28.6, "cpl_rm": 89.73 },
  "frames": [
    {
      "concept_id": "C_001",
      "theme_id": "T11",
      "creative_type": "wildcard",
      "wildcard_category": "meme-native",
      "frame_name": "C_001 | T11 | hiring-ad-v2 | 1x1",
      "dimensions": "1080x1080",
      "node_id": "<pencil_node_id>",
      "export_path": "ads/batches/batch_002/C_001_hiring-ad-v2_1x1.png",
      "qa_passed": true,
      "qa_checks": { "readability_thumb": true, "headline_biggest": true, "no_dead_space": true, "bg_full_bleed": true, "brand_colours_exact": true, "logo_and_cta_present": true, "typography_correct": true, "case_rules_correct": true, "wildcard_novelty": true }
    }
  ]
}
```

## ERROR HANDLING
- If `G()` AI generation returns an image that does not match the prompt's scene or has Western faces, rerun the prompt with sharper noun constraints. Do not accept off-brief imagery.
- If `batch_design()` fails, fall back to primitive shape composition (rectangles + text) for artifact concepts — C_001, C_002, C_003, C_004, C_011 are largely text-and-rectangle constructions and do not require AI imagery.
- If a concept cannot be rendered in one of the 3 formats (extreme aspect-ratio mismatch), produce a keyframe + text annotation and mark `status: "keyframe_only"` in the manifest — but still attempt all 3 formats first.

## STOP CONDITIONS
- Stop and surface the issue to the user if:
  - Any brand file is missing or malformed.
  - The user has not confirmed LP alignment for C_008 (kopitiam v2) — that concept must ship with a corresponding LP CTA match.
  - More than 2 concepts fail the wildcard-novelty QA after two redesigns.

## WHAT SUCCESS LOOKS LIKE
- 36 frames saved to `ads/iteration_2.pen`.
- 36 PNGs exported to `ads/batches/batch_002/`.
- `ad-copy.md` mirrors Batch 1 format with Primary Text / Headline / Description per concept.
- `creative_manifest.json` lists all 36 frames, each with `qa_passed: true`.
- 6 safe / 6 wildcard split confirmed in the manifest counts.

=== END PROMPT ===

