# Pencil.dev WEB-APP Prompt — Batch 3 (MY EN)

> Paste-ready. Self-contained. No local file paths, no MCP, no commission/Beep angles.

---

## HOW TO USE THIS FILE IN PENCIL.DEV

**Option A (recommended)** — Paste **§1 GLOBAL BRIEF** as your project/master brief in Pencil first (sets brand + rules + exclusions), then paste **one concept block from §2** at a time into the design request. This gets the highest-quality variations per concept.

**Option B** — Paste the whole document at once as a mega-brief and ask Pencil to "produce 12 concepts × 3 formats each, one at a time, following the spec verbatim". Lower quality per concept but faster.

**Assets to upload into Pencil's asset library before you start** (so concepts can reference them):
- `StoreHub Logo_Full Orange.png` (use on light backgrounds)
- `StoreHub_Logo_Full Positive Colour Reverse.png` (white version, use on dark/orange)
- D3 Pro hardware front view (MY)
- D3 Mini hardware (MY)
- Falcon Left hardware (MY)
- A reference photo of a mamak/hawker stall at night (for C_006)
- A reference photo of nasi lemak on banana leaf (for C_008)

Everything else Pencil generates with AI imagery.

---

=== BEGIN PROMPT ===

## §1 — GLOBAL BRIEF (paste this first, every session)

### ROLE
You are designing static ad creative for **StoreHub** — an all-in-one POS platform serving 20,000+ F&B and retail merchants across Malaysia, Philippines, and Thailand. The current batch is **Malaysia, English-language only**. You will produce 12 distinct ad concepts, each rendered in 3 formats (1080×1080 square, 1920×1080 landscape, 1080×1920 vertical). Total output: 36 frames.

### THE PRODUCT YOU ARE ADVERTISING
StoreHub POS — a tablet-based point-of-sale system that handles orders, payments, inventory, sales reports, customer loyalty, and multi-location sync, in one screen.
- **MY price anchor (use only this):** From **RM3.40/day** (= From RM3,960/year).
- **Setup:** 24 hours, no training needed.
- **Social proof:** 17,000+ merchants in MY/PH/TH.

### HARD EXCLUSIONS — DO NOT PRODUCE ANY CREATIVE THAT
- ❌ Mentions or implies **delivery commission** savings (no "GrabFood takes 30%", no "FoodPanda commission", no "0% commission" claims, no delivery-platform comparison).
- ❌ Mentions or features **Beep** (StoreHub's QR-ordering product). This batch is POS-only.
- ❌ Uses Western faces, stock-photo expressions, or non-Asian models.
- ❌ Mentions competitor brand names (no GrabFood, FoodPanda, Square, Loyverse, etc.).
- ❌ Promises uptime, security certifications, or any unverified statistic.

### THE CONTROL TO BEAT (context only — do not copy)
A previous winning ad mimicked a real **job-posting classifieds card** (no product shot, no brand chrome until the bottom). It returned SQL% 28.6% at CPSQL RM358. The hypothesis being tested in this batch: the format (looks-like-a-real-document) was the structural driver — not the message. Five of the twelve concepts below are "artifact-native": they look like real documents (receipts, WhatsApp screenshots, Google reviews, tax forms, classifieds), not like ads.

### BRAND SYSTEM (use these values exactly)
**Colours**
- StoreHub Orange `#ff9419` — primary, CTA button, accents
- StoreHub Black `#2f2922` — text on light bg, dark bg blocks
- Bold Orange `#ff630f` — secondary accent
- Pink `#ff546f` — accent only
- Azure Blue `#2a6ee8` — secondary accent
- Cream `#fff8ea` — for typography-led concepts
- White `#ffffff`

**Approved gradients (use only these)**
- Orange Warm: `#ff630f` → `#ff9419` at 135°
- Orange to Pink: `#ff630f` → `#ff546f` at 135°
- Orange Tint: `#ff9419` → `#ffce95` at 135°

**Forbidden combinations**
- ❌ Do NOT mix orange with green or blue in a gradient.
- ❌ No drop shadows on icons or hardware.

**Typography (English)**
| Use | Font | Weight | Case |
|---|---|---|---|
| Headline | **Barlow** | **Black (900)** | Title case or Sentence case (or ALL CAPS only if ≤4 words) |
| Sub-headline | Open Sans | Semibold (600) | Sentence case |
| Body / bullets | Open Sans | Regular (400) | Sentence case |
| CTA | Open Sans | **Bold ALL CAPS** | ALL CAPS verbatim |

**Sizing per format (minimums — bigger is fine)**
| Format | Headline | Sub-head | Body | Padding |
|---|---|---|---|---|
| 1080×1080 | 96–140 px | 44–60 px | **22–28 px (min 22)** | ≤32 px |
| 1920×1080 | 96–130 px | 44–60 px | 22–28 px | ≤48 px |
| 1080×1920 | 130–180 px | 52–72 px | 28–36 px | 250 px top / 400 px bottom (UI-safe zones) |

**Type rules**
- Headline must be the LARGEST element on canvas — at least 30% bigger than the sub-headline.
- Never bold every text level — bold is reserved for emphasis.
- Headline max 2 lines; sub-head max 1 line; body bullets max 5 bullets, 1 line each.
- Line spacing on headline: 1.1–1.25.

### CTA (VERBATIM, EVERY FRAME)
`BOOK A FREE DEMO NOW` — Open Sans Bold, ALL CAPS, on a **rounded pill** in StoreHub Orange `#ff9419` with white text. The pill must be visible above the fold of the visible safe-zone.

### LOGO RULES (EVERY FRAME — INCLUDING WILDCARDS)
- **Light backgrounds** → full-color orange wordmark.
- **Dark or orange backgrounds** → white wordmark.
- **Position:** bottom-left or bottom-right corner, small but readable.
- **Never** type-set "StoreHub" in Barlow — always use the brand PNG/SVG asset.
- **Never** place the logo on a busy photo without a clear-space background.

### VISUAL STYLE
- **Aesthetic:** bold, modern, practical, authentic.
- **Imagery:** Pan-Asian merchants only. Real-looking shops, hawker stalls, F&B counters. Documentary-style preferred over staged.
- **Background photos:** blur 40–60 if behind text. Place a 70–90% opacity colour panel behind text on busy backgrounds for readability.
- **Hardware photography:** never on plain white. Always show in a real environment context.

### ANTI-PATTERNS (auto-fail — redesign if any appear)
- ❌ Orange split-card with POS sitting on a pedestal (overused in Batch 1).
- ❌ Centred POS hardware on plain orange background.
- ❌ Diagonal "Choose Your Fighter" split with a VS badge.
- ❌ Text crammed into a narrow centre column with dead-space margins.
- ❌ Tiny floating "55% off" corner badges (too small to read in thumbnail).
- ❌ Any text below the minimum font sizes above.
- ❌ Multiple competing CTAs in one frame.

### 9-POINT QA CHECKLIST (Pencil — run this on every frame before declaring done)
1. Headline is readable at 250×250 px thumbnail size.
2. Headline is the biggest element on canvas.
3. <10% of canvas is empty / dead space without design intent.
4. Background is full-bleed edge-to-edge.
5. Colours match the hex codes above exactly.
6. StoreHub logo present (brand asset, not type-set) AND CTA "BOOK A FREE DEMO NOW" in ALL CAPS present.
7. Headline is Barlow Black, line spacing 1.1–1.25, ≤2 lines.
8. Sub and body in Sentence case; CTA in ALL CAPS.
9. **Wildcards only:** Could this be mistaken for a standard StoreHub promo card at a glance? If YES — the wildcard failed; redesign.

---

## §2 — THE 12 CONCEPTS (paste one block per design request)

> Each concept must be produced in **3 formats**: 1080×1080, 1920×1080, 1080×1920. Use the headline / sub-headline / body / CTA copy **verbatim**. The hook_visual is the design direction — interpret faithfully.

---

### C_001 · SAFE · Artifact-Native (Receipt)
**Concept name:** `artifact-receipt-hidden-cost`

**Visual direction (verbatim):**
Full-bleed photo of a crumpled month-end expense statement lying on a coffee-stained table. Line items must be legible at thumbnail size, styled like a monospace bank statement (Roboto Mono or similar):
- Manual reconciliation (46h × RM25/h) ………… RM 1,150
- Stock write-offs ………………………………… RM 680
- Staff overtime (3 staff) ………………………… RM 1,890
- Missed loyalty redemptions …………………… RM 220
- **StoreHub POS …………………………………… RM 408** ← circled in red pen
Coffee ring stain on one corner. Slight paper texture. No product visible. StoreHub logo + CTA pill anchor the bottom strip only.

**Copy (verbatim):**
- Headline: `Which one are you cutting?`
- Sub-headline: `Your month, itemised. The cheapest line is the one that quietly fixes the other four.`
- Body: `From RM3.40/day · 17,000+ merchants · Setup in 24h`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_002 · SAFE · Artifact-Native (WhatsApp screenshot)
**Concept name:** `artifact-whatsapp-1am-boss`

**Visual direction:**
Pixel-accurate WhatsApp group chat screenshot. Group name **"Restaurant Ops"** with a generic neutral group avatar (do NOT use WhatsApp's logo or wordmark — replace with a generic chat icon to avoid trademark issues). Header bar in green `#25D366`, wallpaper beige `#ECE5DD`. Outgoing bubbles `#DCF8C6`, incoming white. Timestamps **00:47–01:12**. Realistic read-receipt double-blue ticks.
- Boss: "Stock count off again?" (00:47)
- Staff: "Three tablets all showing different numbers" (00:51)
- Boss: "Tomorrow we look at StoreHub lah" (01:12)
Bottom strip outside the "screenshot" frame holds the StoreHub logo + CTA pill. The chat must look like a real screenshot first; the ad reveal happens only at the bottom.

**Copy:**
- Headline: `When the group chat starts at midnight, it's time.`
- Sub-headline: `One POS. One inventory. One source of truth across every location.`
- Body: `Real-time stock · Auto-reconciled sales · From RM3.40/day`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_003 · SAFE · Artifact-Native (Google review card)
**Concept name:** `artifact-google-review-binq`

**Visual direction:**
A Google review card UI, full canvas. Reviewer name: **"Binq Dessert (4 locations)"**, verified-merchant badge, neutral profile photo placeholder. 5 orange stars (not Google's exact yellow — use StoreHub orange `#ff9419` to differentiate). Posted "3 weeks ago" timestamp.
Review body: *"Cut closing time from 2 hours to 20 minutes. Manpower down by 2 staff per shift. Switched in 2024, never looked back."*
Below: a small "Owner response · StoreHub" reply with 👍👍 reaction icons.
**Avoid Google's logo and exact font** (use Open Sans + Open Sans Semibold, not Google Sans). Bottom strip: StoreHub logo + CTA pill.

**Copy:**
- Headline: `Real merchant. Real numbers. Real switch.`
- Sub-headline: `Binq cut closing time by 83%. From RM3.40/day. Book a demo and we'll show you the maths.`
- Body: `F&B specific · Multi-location dashboard · 17,000+ merchants`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_004 · SAFE · Milestone Math (typography-led)
**Concept name:** `milestone-opening-week-itemised`

**Visual direction:**
Cream `#fff8ea` background. Typography-only — no full photo. Centre column shows an architect's-budget-sheet itemised list, left-aligned, monospaced numerals on the right:
- Renovation ……………………………… RM 48,000
- Kitchen equipment …………………… RM 25,000
- Signage ………………………………… RM 3,500
- Staff training ………………………… RM 4,000
- **POS — from RM3.40/day** ← this line highlighted in StoreHub Orange `#ff9419`
Bottom-right: a small floating D3 Pro hardware cutout at ~25% scale (uploaded asset). Bottom strip: orange CTA pill + StoreHub wordmark.

**Copy:**
- Headline: `You saved where it counts.`
- Sub-headline: `Opening week is the most expensive week of your career. The POS shouldn't be the line that breaks you.`
- Body: `RM3.40/day · 24h setup · F&B + retail ready`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_005 · SAFE · Milestone Math (Year 2 split)
**Concept name:** `milestone-year2-time-math`

**Visual direction:**
Split canvas exactly down the middle.
- **Left half** — black background `#2f2922`, white Barlow Black type: **"Year 1: 552 hours counting stock by hand."**
- **Right half** — orange background `#ff9419`, black Barlow Black type: **"Year 2 with StoreHub: 0."**
- A 4px white vertical divider separates the two halves.
No product shot. Numbers + the gap between them is the visual. Bottom strip: thin neutral grey bar with the StoreHub white wordmark on the left and the orange CTA pill on the right (or vice-versa for layout balance per format).

**Copy:**
- Headline: `Which year are you closing?`
- Sub-headline: `You can't get the hours back. But you can stop bleeding them.`
- Body: `Auto-reconciled sales · Daily report at close · From RM3.40/day`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_006 · SAFE · Cultural Pride (mamak at night)
**Concept name:** `cultural-mamak-night`

**Visual direction:**
Full-bleed authentic photo of a Malaysian mamak stall after midnight. Fluorescent overhead lighting, plates of roti canai stacked, owner standing at the till in the mid-ground, a customer walking past with slight motion blur. A D3 POS terminal visible on the counter but **not the hero** — eye should land on the scene first. Warm ambient light bleeding from the kitchen behind. Apply a 40–60 blur strength to the background regions where text will overlay, plus a 70–80% opacity dark panel behind the headline for readability.

**Copy:**
- Headline: `Your stall. Our tech.`
- Sub-headline: `Built for the way Malaysian F&B actually runs — 11pm rushes, cash + QR, every payment in one screen.`
- Body: `DuitNow · Boost · TnG · Cash · One POS`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_007 · WILDCARD · Artifact-Native (fake government form) · meme-native
**Concept name:** `artifact-lhdn-tax-form`

**Visual direction:**
A document that looks at first glance like a Malaysian government / tax form. **Avoid using the real LHDN logo, real serial-number format, or exact LHDN typography**. Use a generic "Inland Revenue"-style letterhead, a fake serial number, checkbox grid, a neutral coat-of-arms-style mark.
Highlight one line of the form:
> **Item 14**: Annual hours your team spent on manual end-of-day reconciliation (hrs): _____________
A pen hovers over the blank field. Subtle paper grain.
**Required microcopy bottom-right, small but legible:** *"illustrative — not a real government document"*
Bottom strip: StoreHub logo + CTA pill.

**Copy:**
- Headline: `If anyone audited your time, you'd cry.`
- Sub-headline: `StoreHub closes your day in 12 minutes. The hours you actually want back.`
- Body: `Auto-reconciled sales · Daily report at close · Setup in 24h`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_008 · WILDCARD · Cultural Pride (absurdist nasi lemak)
**Concept name:** `absurd-nasi-lemak-pos-stack`

**Visual direction:**
Surreal hyperreal food photography. A single banana leaf with nasi lemak — sambal, peanuts, ikan bilis, cucumber slices, and **one boiled egg replaced by a tiny D3 POS terminal**, perfectly proportioned to the egg's size, steam rising faintly from it. Studio food-photography lighting. Banana leaf occupies most of the frame. Plate visible at the edge. Background a dark wood table.
Bottom strip: StoreHub logo + CTA pill.

**Copy:**
- Headline: `Standard issue. Malaysian F&B.`
- Sub-headline: `The five things every stall needs. We're the one nobody told you about.`
- Body: `From RM3.40/day · DuitNow + QR · Built for Malaysian F&B`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_009 · WILDCARD · Visual Metaphor (coins dissolving)
**Concept name:** `metaphor-coin-stack-leaking`

**Visual direction:**
Macro photography, dark background `#1a1614`. A tall stack of Malaysian RM coins centred in the frame. The bottom 5 coins frozen mid-dissolve into stylised smoke wisps — captured at peak visual tension (not motion-blurred — a single crisp still). No product visible.
Single small line of text bottom-left, Open Sans Regular, white at 80% opacity:
*"Manual reconciliation: 46 hrs · Stock write-offs: untracked · Overtime pay: untracked."*
Bottom strip: StoreHub H-mark logo (small, not the full wordmark) + CTA pill.

**Copy:**
- Headline: `Where your month goes.`
- Sub-headline: `The costs you don't see are the ones that close businesses. StoreHub closes the leaks.`
- Body: `Auto-reconciled sales · Real-time stock · RM3.40/day`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_010 · WILDCARD · Gut-Punch documentary (2am)
**Concept name:** `gutpunch-2am-empty-stall`

**Visual direction:**
Quiet documentary still. A small F&B stall at **2:14 AM** (timestamp burnt-in lower corner in a small mono font, like a security camera). Owner alone at a folding table under a single fluorescent tube, paper receipts spread out, a basic calculator, head in one hand, eyes closed. Cool fluorescent lighting, slightly desaturated. No product visible anywhere in the frame. No StoreHub branding in the upper two-thirds. The only StoreHub presence is the bottom strip: small white logo + orange CTA pill.
This frame must feel like recognition, not dramatisation. No theatrical chaos. A quiet image.

**Copy:**
- Headline: `Tomorrow you do it again.`
- Sub-headline: `Or you don't. StoreHub closes your day in 12 minutes, not 2 hours.`
- Body: `Auto-reconciled sales · Daily report at close · From RM3.40/day`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_011 · WILDCARD · Artifact-Native (absurd job classifieds)
**Concept name:** `artifact-jobpost-impossible-human`

**Visual direction:**
A classifieds-card UI mimicking a Malaysian job-listings site (JobStreet or Mudah.my **style only — do not use their logos or trademarks**). Pure typography + rectangle composition. No AI imagery needed.
- Title line: **"HIRING: One Human (must be four humans)"**
- Posted "2 days ago · Klang Valley · Full-time"
- Requirements (12 bullets — escalate absurdity through the list):
  - Manages POS + payments
  - Tracks inventory across 3 locations
  - Runs loyalty programme
  - Sends daily sales reports
  - Schedules staff shifts
  - Sends customer SMS campaigns
  - Processes refunds and exchanges
  - Syncs stock across all branches
  - Closes end-of-day reconciliation
  - Conducts shift handovers
  - **Never sleeps**
  - **Never gets sick**
- Salary line: ~~RM 900 / month~~ (struck through)
- Final line (bold, orange): **"OR: StoreHub. From RM3.40/day."**
Bottom strip: StoreHub logo + CTA pill.

**Copy:**
- Headline: `Hiring: one human (must be four humans).`
- Sub-headline: `The job description nobody can fill. The system that already does it.`
- Body: `POS + inventory + loyalty + reports + reconciliation · One screen · RM3.40/day`
- CTA: `BOOK A FREE DEMO NOW`

---

### C_012 · WILDCARD · Entertainment-First (90-day clock)
**Concept name:** `entertainment-90day-survival-clock`

**Visual direction:**
Single locked-off composition. A round analog wall clock fills the centre. A yellow Post-it note is stuck on the clock face — handwritten in marker, says **"Day 47 of 90"**. Behind the clock, slightly out of focus, a half-renovated restaurant space — tools, plastic sheeting, an unfinished counter. Warm late-afternoon light through a single window. Subtle film grain.
No StoreHub branding in the upper two-thirds. Bottom strip: small StoreHub logo + orange CTA pill.

**Copy:**
- Headline: `The first 90 days decide the next 10 years.`
- Sub-headline: `Your POS is the cheapest line on the rescue list. From RM3.40/day.`
- Body: `24h setup · F&B + retail · 17,000+ merchants`
- CTA: `BOOK A FREE DEMO NOW`

---

## §3 — FORMAT-SPECIFIC NOTES (apply when producing the 3 sizes)

**1080×1080 (square — feed)**
- Headline takes ~⅓ of canvas height.
- Visual takes ~⅔ height.
- CTA pill spans roughly 60–70% width, centred or anchored to the bottom strip.
- Body bullets sit between sub-head and CTA.

**1920×1080 (landscape — desktop / Audience Network)**
- Headline left-aligned takes ~50% of width on the left; visual on the right (or vice versa).
- For artifact concepts: the artifact takes ~70% of the canvas, headline + CTA sit in a bottom or side strip.

**1080×1920 (vertical — Reels / Stories)**
- **Top safe zone:** 250 px reserved (do not put critical text there — Instagram username overlays this region).
- **Bottom safe zone:** 400 px reserved (Instagram CTA + caption overlay this region).
- Headline lives in the middle 1280-px band.
- For C_002 (WhatsApp): this format is the strongest — long-form chat looks native here.
- For C_010 + C_012: this format is the primary — these were designed video-pacing-first; a still must justify the headline without animation.

---

## §4 — FILE NAMING ON EXPORT

Format your exports as:
```
S1_EN_Batch3_[concept_name]_[format]_nootp.png
```
Examples:
- `S1_EN_Batch3_artifact-receipt-hidden-cost_1x1_nootp.png`
- `S1_EN_Batch3_artifact-whatsapp-1am-boss_9x16_nootp.png`
- `S1_EN_Batch3_milestone-year2-time-math_16x9_nootp.png`

Total expected output: **36 PNGs** (12 concepts × 3 formats).

---

## §5 — IF YOU GET STUCK

- If a concept's hook_visual cannot be rendered faithfully (e.g. you cannot generate a believable WhatsApp UI): produce the closest possible interpretation and flag it in your response so the human can substitute the artifact manually.
- If any frame triggers an anti-pattern in the QA check: redesign before exporting.
- If the wildcard check (#9) returns "yes, this looks like a normal promo card": the wildcard is broken. Push it further into the artifact / metaphor / documentary direction.

=== END PROMPT ===

---

## Local-only notes (do not paste into Pencil)

- Master file of record: `data/iterations/3/experiment_plan.json` and `data/iterations/3/PENCIL_BRIEF.md`.
- Gates G1 (kopitiam LP audit), G3 (552h figure), G4 (receipt line items), G5 (LHDN legal review) must still clear before launch. C_006, C_008 sit in WITH_ISSUES until G1 clears. C_007 (LHDN) is high legal risk — verify the disclaimer is on-frame before upload.
- C_010 and C_012 are video-pacing concepts; the static versions must stand alone but the reel version is the canonical asset (produce statically here; treat the video as a separate Batch 3.1).
- Once Pencil generates the 36 frames, export to `ads/batches/batch_003/` and run the 9-point QA in §1 again manually before media upload.
