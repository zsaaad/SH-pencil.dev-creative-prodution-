# Batch 3 — Creative Production Brief (Pencil.dev)

**Iteration:** 3
**Market:** MY EN (primary)
**Drafted:** 2026-05-28
**Run window:** launch after production gates clear → 14-day test cycle
**Total concepts:** 12 (6 safe + 6 wildcard)
**Total output files:** 36 (each concept × 1080×1080 + 1920×1080 + 1080×1920)
**Control ad to beat:** `S1_EN_Batch 1_competitive contrast - job post_nootp` — CPSQL RM358.92 · SQL% 28.6% · CPL RM89.73

> Source plan: `data/iterations/3/experiment_plan.json` (v2). The JSON is the source of truth. This brief is the human-readable production wrapper.

---

## 1 · Why this batch looks the way it does

MY Batch 1 (1–12 Apr 2026, RM1,966 spend) returned exactly one decisive winner: **the job-post artifact (CPSQL RM358.92, SQL% 28.6%)**. Every other theme either failed (Pain Amp, social proof, the math standalone, value unlocked, aspirational self) or had a clean diagnostic (opening expenses got volume + MQL but SQL% collapsed to 6.3%; kopitiam got clicks but zero leads — an LP misalignment).

MY Batch 2 (12 concepts, T11 + T12 themes) was designed in late April but **never launched in Meta**. So the only ground-truth performance signal for Batch 3 planning is Batch 1.

**The structural insight from Batch 1** is that job-post didn't win because of the competitive-contrast message — it won because it looked like a real artifact, not an ad. Batch 3 isolates this hypothesis hard: **5 of 12 concepts ride on the T11 Artifact Native format**, each wrapping a different copy angle (hidden cost, social proof, classifieds, government form, native chat). If T11 generalises, the next batch goes all-in on the format. If T11 fails outside the job-post copy, the message was load-bearing — different next move.

The other 7 concepts test secondary research questions:
- **T12 Milestone Math (3 concepts)** — does fusing milestone + concrete number lift SQL% above the 6.3% opening-expenses floor?
- **T7 Cultural Pride (2 concepts)** — does cultural specificity replicate the kopitiam scroll-stop now that the LP is being audited?
- **T9 Hidden Cost (1 wildcard)** — pure visual metaphor; gives T9 its first real RM50+ runway.

---

## 2 · Primary research question

> **Is artifact-native format (T11) the true structural driver of the Batch 1 job-post win — generalising across copy angles (cost, social proof, classifieds, tax form, chat) — at SQL% ≥ 25%?**

Secondary research questions (in priority order):
1. Does milestone+math fusion (T12) lift SQL% above the 6.3% opening-expenses floor to ≥ 15%?
2. Does the cultural-pride creative survive a fixed LP (T7 mamak)?
3. Do untested wildcards (gut-punch, metaphor, absurdist, government-form, entertainment-first) earn enough hook rate to justify next-batch slots?

---

## 3 · Themes in Batch 3

| Theme ID | Theme | Role | Concepts |
|---|---|---|---|
| **T11** | Artifact Native | Load-bearing — 5 concepts wrap 5 distinct copy angles, isolating format from message | 5 (C_001, C_002, C_003, C_007, C_011) |
| **T12** | Milestone Math | Fix the opening-expenses SQL% leak using financial anchor | 3 (C_004, C_005, C_012) |
| **T7** | Cultural Pride | Generalise the kopitiam scroll-stop (mamak, nasi lemak) post-LP fix | 2 (C_006, C_008) |
| **T9** | Hidden Cost | First real wildcard runway for the hidden-cost theme | 1 (C_009) |
| **T1 inside T11** | Pain Amplification + artifact wrapper | First real runway for T1 | 1 (C_010) |

**Hybrid theme labels (`secondary_theme` in JSON):**
- C_001 = T11 wrapper × T9 copy → tests format isolation from competitive-contrast copy
- C_003 = T11 wrapper × T6 social-proof copy → first runway for T6
- C_010 = T11 wrapper × T1 gut-punch → first runway for T1

These hybrids are core to the experiment — when results come in, the next analyst must decompose along the **format axis** (T11 vs not-T11) AND the **message axis** (T9 / T6 / T1 / T5).

**Safe/Wildcard split (non-negotiable):** 6 safe (C_001–C_006) + 6 wildcard (C_007–C_012).

---

## 4 · Global brand + production rules

**Colours:** StoreHub Orange `#ff9419`, StoreHub Black `#2f2922`. Accents allowed: Bold Orange `#ff630f`, Pink `#ff546f`, Azure `#2a6ee8`. Gradients: only the 7 approved in `config/brand.json`.

**Typography:**
- Headline: **Barlow Black**, line spacing 1.1–1.25, max 2 lines
- Sub-headline: Open Sans Semibold/Semibold Italic, max 1 line, Sentence case
- Body bullets: Open Sans Regular/Semibold, 1 line per bullet, max 5 bullets, Sentence case
- CTA: Open Sans Bold/Bold Italic, **ALL CAPS**, on orange or pink pill — verbatim `BOOK A FREE DEMO NOW`

**Per-format sizing (every concept produced in all 3):**
- **1080×1080:** headline 96–140px · sub 44–60px · body 22–28px (raise from Batch 2 minimum after readiness audit flagged 20px as thumbnail-unsafe) · padding ≤32px (safe) / 0px (wildcard)
- **1920×1080:** headline 96–130px · sub 44–60px · body 22–28px · padding ≤48px (safe) / 0px (wildcard)
- **1080×1920:** headline 130–180px · sub 52–72px · body 28–36px · UI-safe 250px top / 400px bottom

**Imagery:** Pan-Asian faces only. No Western faces, no stock-photo expressions. Photo backgrounds blurred 40–60. Busy backgrounds get a 70–90% opacity colour panel behind text.

**Logo + CTA:** every frame — including wildcards — includes the StoreHub logo (bottom corner, small) and the CTA button. Use the brand PNG, not type-set "StoreHub" Barlow text (Batch 2 audit flagged this).

**Naming convention for exports:**
```
S1_EN_Batch3_[theme_short]_[concept_name]_[format]_nootp
```
Example: `S1_EN_Batch3_artifact_receipt-hidden-cost_1x1_nootp`

**Anti-patterns (auto-fail if used):**
- ❌ Orange split card with POS on pedestal (overused)
- ❌ Centred POS on plain orange background
- ❌ Diagonal CYF split with VS badge
- ❌ Text in narrow centre column with dead-space margins
- ❌ Small floating "55% Off" corner badges
- ❌ Headlines below minimum font size

---

## 5 · Concept specs (12 concepts)

> **Source of truth:** `data/iterations/3/experiment_plan.json` — every concept's `hook_visual`, `headline`, `sub_headline`, `body_or_bullets`, `target_segment`, `hypothesis`, `success_metric`, and `unique_lever` is canonical there. The notes below are production guidance ON TOP of the JSON.

### SAFE (C_001 – C_006)

- **C_001 · artifact-receipt-hidden-cost (T11 × T9)** — Photo-realistic crumpled bank statement / expense sheet. Use Roboto Mono or generic monospace for line items to feel like a real statement. Last-line orange highlight on StoreHub.
- **C_002 · artifact-whatsapp-1am-boss (T11)** — Pixel-accurate WhatsApp UI. Green `#25D366` header, beige `#ECE5DD` wallpaper, white incoming / `#DCF8C6` outgoing bubbles. **Do NOT use the WhatsApp logo** — neutral chat icon. Per-concept QA: a designer reviewer must confirm UI realism at 2-sec glance.
- **C_003 · artifact-google-review-binq (T11 × T6)** — Google review card UI. **Avoid Google's logo/wordmark** — neutral 5-star row. Per-concept QA on UI realism. **Legal/policy gate:** Binq Dessert testimonial release must cover paid Meta usage.
- **C_004 · milestone-opening-week-itemised (T12)** — Cream `#FFF8EA` background, typography-only. Caveat Italic for any handwritten line. No photo. Highlight StoreHub line in orange.
- **C_005 · milestone-year2-time-math (T12)** — Numbers carry the visual. Split BG (black/orange). Time-cost framing: "Year 1: 552 hours counting stock by hand. Year 2 with StoreHub: 0." **Pre-launch gate:** strategist validates the 552h figure (46h/mo × 12) is defensible against MY merchant benchmarks.
- **C_006 · cultural-mamak-night (T7)** — Photo-realistic mamak interior at 2am. D3 POS visible but not hero. **Pre-launch gate:** kopitiam LP audit must complete first — same LP serves this concept and we cannot repeat the Batch 1 clicks-no-leads failure.

### WILDCARD (C_007 – C_012)

- **C_007 · artifact-lhdn-tax-form (T11, meme-native)** — Fake government tax form. **Critical pre-launch gate:** legal + brand review for Meta deceptive-content policy AND LHDN impersonation risk. Microcopy bottom-right: *"illustrative — not a real LHDN document"*. If legal/brand says no, descope.
- **C_008 · absurd-nasi-lemak-pos-stack (T7, absurdist)** — Surreal still life. D3 POS replaces the boiled egg on the banana leaf, perfectly proportioned. Hyperreal food photography lighting. Generate via Pencil `G()` or Nano Banana with sharp noun constraints.
- **C_009 · metaphor-coin-stack-leaking (T9, metaphor)** — Static frame. Coins frozen mid-dissolve into stylised smoke wisps. Dark BG. Single small-text line bottom with the cost breakdown. No product visible.
- **C_010 · gutpunch-2am-empty-stall (T11 × T1, gut-punch)** — **Video-pacing concept**. The 1080×1920 vertical should be the primary asset (treated as a 5–10s reel still + animated reveal). For the static formats (1080×1080, 1920×1080), capture the single most arresting documentary still: owner at folding table, eyes closed, hand on forehead. No StoreHub branding until the bottom-strip CTA bar.
- **C_011 · artifact-jobpost-impossible-human (T11, absurdist)** — JobStreet/Mudah.my classifieds UI. Pure typography + rectangle composition (no AI imagery needed). 12-bullet requirements list with "never sleeps, never gets sick, costs RM900/month" escalating absurdity. Reveal: "OR: StoreHub. From RM3.40/day."
- **C_012 · entertainment-90day-survival-clock (T12, entertainment-first)** — **Video-pacing concept**. For 1080×1920 reel: 2 seconds of locked-off clock ticking, then headline slides in. For 1080×1080 and 1920×1080 statics: capture the still moment — clock + Post-it "Day 47 of 90", half-renovated restaurant slightly out of focus behind. Headline on the still must do the work of the video reveal.

### Video-static handling for C_010 + C_012

Pencil.dev is static-first. For C_010 + C_012:
1. Produce the static frames for all 3 dimensions following the static-friendly description above.
2. **Optionally** generate the reel-format video via Veo 3 / Mosaic (track this as Batch 3.1) — but do not block static launch on it.
3. The 9×16 static must visually justify the headline without the video reveal — if a static reader can't get the joke/punch in 2 seconds, the concept is broken.

---

## 6 · Pre-launch gates

All gates must clear before the ad can spend. Concept stays in `WITH_ISSUES` status until gate clears.

| # | Gate | Owner | Blocks |
|---|---|---|---|
| G1 | Kopitiam LP audit complete — form fires, mobile renders, pixel attributes correctly | performance ops | C_006, C_008 |
| G2 | Lead-form revenue-band qualifier field deployed on milestone-themed LPs | growth eng | C_004, C_005, C_006 |
| G3 | Verify C_005 "552 hours / year on manual reconciliation" figure against MY merchant benchmarks or labour-cost data | strategist | C_005 |
| G4 | Verify C_001 receipt line-items (reconciliation 46h × RM25, stock write-offs RM 680, overtime RM 1,890, missed loyalty RM 220) — defensible in comments | strategist | C_001, C_009 |
| G5 | C_007 LHDN artwork — legal + brand review for Meta deceptive-content + LHDN impersonation risk; disclaimer microcopy present | legal/brand | C_007 |
| G6 | PH RM0 status documented — pause vs delivery break (does not block MY launch) | ops | (none) |

## 7 · Per-concept QA gates (run after creative produced, before upload)

| Concept | QA check |
|---|---|
| C_002 | WhatsApp UI realism — fonts, bubble shape, timestamp format, read receipts, group avatar all native-accurate at 2-sec glance |
| C_003 | Google review chrome realism — star colour, profile placement, verified badge, owner-response styling |
| C_007 | LHDN form realism — letterhead, serial number formatting, checkbox grid, font match real LHDN docs at 2-sec glance without being legally mistakable. Disclaimer present and legible |

## 8 · Visual QA — run on every single frame

**Readability (thumbnail test at 250×250px):**
- [ ] 1. Headline readable at thumbnail without zoom
- [ ] 2. Headline is the biggest element on canvas

**Layout:**
- [ ] 3. < 10% canvas is empty/dead space without design intent
- [ ] 4. Background covers 100% edge-to-edge

**Brand:**
- [ ] 5. Colours match `config/brand.json` exactly
- [ ] 6. Logo present bottom-corner (PNG, not type-set); CTA button present with "BOOK A FREE DEMO NOW" in ALL CAPS

**Typography:**
- [ ] 7. Headline Barlow Black, line spacing 1.1–1.25, ≤ 2 lines
- [ ] 8. Sub + body in Sentence case; CTA in ALL CAPS

**Wildcards only (C_007–C_012):**
- [ ] 9. Could this ad be mistaken for a standard StoreHub promo card at a glance? → if YES, the wildcard failed; redesign.

A frame is complete only when all applicable checks return TRUE.

---

## 9 · After production

1. Save the `.pen` file: `ads/iteration_3.pen`
2. Export all 36 PNGs into `ads/batches/batch_003/` with the naming convention in §4
3. Write ad-copy markdown: `ads/batches/batch_003/ad-copy.md` — mirror Batch 1 format with Primary Text / Headline / Description per concept
4. Save `data/iterations/3/creative_manifest.json` with node IDs and QA pass states
5. Hand off to media buyer for Meta upload
6. Run cycle check after upload; wait 14 days → `/ad-pipeline results 3` → `/ad-pipeline loop 3`

---

## 10 · What Batch 3 is actually testing (one-line version)

> **Did the job-post artifact win because it was an artifact, or because it was a job post?** Batch 3 answers this by running 5 artifact executions across 5 different copy angles (cost, social proof, classifieds, government form, chat) and comparing CPSQL head-to-head. Whichever wins decides whether Batch 4 scales the format or the message.

The other 7 concepts are independent secondary bets that get judged on their own success metrics, not against T11.

---

# 11 · PROMPT FOR PENCIL.DEV LLM

> Copy everything between the `=== BEGIN PROMPT ===` and `=== END PROMPT ===` markers into the ad-creative-generator agent (or any LLM with access to the `mcp__pencil__*` tools).

=== BEGIN PROMPT ===

## ROLE
You are a Pencil.dev ad creative production agent for StoreHub. You will produce 12 ad concepts × 3 formats = 36 final frames for Batch 3 of the creative testing programme. Every frame must pass a 9-point QA gate before you move to the next one. You do not improvise concepts — you execute the brief verbatim.

## INPUTS TO READ FIRST (in this order, do not skip)
1. `/Users/zaidsaad/Desktop/Code/Pencil.dev/data/iterations/3/PENCIL_BRIEF.md` — §1–§10 of this file.
2. `/Users/zaidsaad/Desktop/Code/Pencil.dev/data/iterations/3/experiment_plan.json` — canonical concept specs (use `hook_visual`, `headline`, `sub_headline`, `body_or_bullets` verbatim).
3. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/brand.json` — colours, typography, logo, imagery rules.
4. `/Users/zaidsaad/Desktop/Code/Pencil.dev/config/creative_themes.json` — themes T1, T6, T7, T9, T11, T12.
5. `/Users/zaidsaad/Desktop/Code/Pencil.dev/Input Files/SH Context.md` §13 — Wildcard Creative Framework.

Do NOT read any other files until you have read these five.

## OUTPUTS (deliverables)
| Path | What |
|---|---|
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/iteration_3.pen` | Pencil.dev document with all 36 frames |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/batch_003/[concept_id]_[name]_[format].png` | 36 exported PNGs |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/batches/batch_003/ad-copy.md` | Meta ad copy (Primary Text / Headline / Description) per concept |
| `/Users/zaidsaad/Desktop/Code/Pencil.dev/data/iterations/3/creative_manifest.json` | Manifest with all 36 frames, node IDs, QA pass states |

## THE 12 CONCEPTS (iterate in order — full spec in experiment_plan.json)
- C_001 · T11 (×T9) · safe · artifact-receipt-hidden-cost
- C_002 · T11 · safe · artifact-whatsapp-1am-boss
- C_003 · T11 (×T6) · safe · artifact-google-review-binq
- C_004 · T12 · safe · milestone-opening-week-itemised
- C_005 · T12 · safe · milestone-year2-time-math (GATED on G2 + G3)
- C_006 · T7 · safe · cultural-mamak-night (GATED on G1 + G2)
- C_007 · T11 · wildcard meme-native · artifact-lhdn-tax-form (GATED on G5)
- C_008 · T7 · wildcard absurdist · absurd-nasi-lemak-pos-stack (GATED on G1)
- C_009 · T9 · wildcard metaphor · metaphor-coin-stack-leaking
- C_010 · T11 (×T1) · wildcard gut-punch · gutpunch-2am-empty-stall (video-pacing — see §5)
- C_011 · T11 · wildcard absurdist · artifact-jobpost-impossible-human
- C_012 · T12 · wildcard entertainment-first · entertainment-90day-survival-clock (video-pacing — see §5)

## NON-NEGOTIABLE RULES
- **Colours (exact):** `#ff9419` orange, `#2f2922` black. Accents only from brand.json approved list.
- **Fonts:** Headline Barlow Black · Sub Open Sans Semibold · Body Open Sans Regular · CTA Open Sans Bold ALL CAPS.
- **CTA text (verbatim):** `BOOK A FREE DEMO NOW`.
- **Logo:** brand PNG, bottom corner, every frame including wildcards.
- **Faces:** Pan-Asian only. No Western faces, no stock expressions.
- **Three formats per concept:** 1080×1080, 1920×1080, 1080×1920.
- **Min body size 1×1:** 22px (raised from Batch 2 after readiness-audit thumbnail-failure findings).
- **Anti-patterns (auto-fail):** orange split with POS on pedestal · centred POS on plain orange · diagonal CYF + VS badge · narrow centre column · tiny "55% Off" badges · any font below minimums.

## EXECUTION LOOP (12 concepts)
```
FOR each concept in C_001..C_012:
  1. get_editor_state()
  2. open_document("ads/iteration_3.pen") (creates on first concept)
  3. get_guidelines("web-app") + get_style_guide_tags() → pick style matching wildcard_category
  4. Read concept from experiment_plan.json. Use hook_visual / headline / sub_headline / body_or_bullets VERBATIM.
  5. FOR each format in [1080x1080, 1920x1080, 1080x1920]:
       a. find_empty_space_on_canvas()
       b. batch_design() the frame
       c. If concept needs AI imagery (C_005 numbers-only is fine, C_006 mamak photo, C_008 surreal still, C_009 coin metaphor, C_010 documentary still), call G() with sharp noun-constrained prompts
       d. Apply brand colours + fonts + CTA + logo
       e. get_screenshot() + run 9-point QA (§8 in PENCIL_BRIEF.md)
       f. If any check fails → redesign, do not advance
       g. Record node_id + QA states in in-memory manifest
  6. Next concept.

7. After all 12 × 3 frames complete:
   - Write ad-copy.md mirroring Batch 1 format
   - Write creative_manifest.json to the path in OUTPUTS
```

## QA GATE (9 checks per frame)
1. Headline readable at 250×250 thumbnail
2. Headline is the biggest element on canvas
3. < 10% dead space without design intent
4. Background full-bleed
5. Colours exactly brand.json
6. Brand PNG logo + CTA "BOOK A FREE DEMO NOW" ALL CAPS
7. Headline Barlow Black, spacing 1.1–1.25, ≤ 2 lines
8. Sub + body Sentence case; CTA ALL CAPS
9. **Wildcards only:** Could this be mistaken for a standard StoreHub promo card? → if YES, fail.

## STOP CONDITIONS
- Brand file missing/malformed → stop and surface.
- LP audit (G1) unresolved → C_006 + C_008 stay in WITH_ISSUES; surface to user.
- C_005 reconciliation-hours gate (G3) unresolved → C_005 stays in WITH_ISSUES.
- C_001 / C_009 receipt-line-items gate (G4) unresolved → both stay in WITH_ISSUES until numbers are defensible.
- C_007 legal/brand gate (G5) rejected → drop C_007 from the batch and replace with a 12th wildcard from the analyst's untested-angle backlog (aspirational self OR value unlocked in artifact wrapper). Re-run for that slot.
- More than 2 concepts fail wildcard-novelty QA after two redesigns → stop and surface.

## OUTPUT SCHEMA — `data/iterations/3/creative_manifest.json`
```json
{
  "iteration": 3,
  "pen_file": "ads/iteration_3.pen",
  "safe_count": 6,
  "wildcard_count": 6,
  "total_created": 36,
  "created_at": "ISO-8601",
  "control_ad_to_beat": "S1_EN_Batch 1_competitive contrast - job post_nootp",
  "control_benchmarks": { "cpsql_rm": 358.92, "sql_pct": 28.6, "cpl_rm": 89.73 },
  "frames": [
    {
      "concept_id": "C_001",
      "theme_id": "T11",
      "secondary_theme": "T9",
      "creative_type": "safe",
      "wildcard_category": null,
      "frame_name": "C_001 | T11 | artifact-receipt-hidden-cost | 1x1",
      "dimensions": "1080x1080",
      "node_id": "<pencil_node_id>",
      "export_path": "ads/batches/batch_003/C_001_artifact-receipt-hidden-cost_1x1.png",
      "qa_passed": true,
      "qa_checks": { "readability_thumb": true, "headline_biggest": true, "no_dead_space": true, "bg_full_bleed": true, "brand_colours_exact": true, "logo_and_cta_present": true, "typography_correct": true, "case_rules_correct": true, "wildcard_novelty": null }
    }
  ]
}
```

=== END PROMPT ===
