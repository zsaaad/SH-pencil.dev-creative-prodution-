# MY-Batch_004 · Family B · Round 3 Final Polish Report

**Status:** COMPLETE. All 5 polish items resolved. 10 of 10 frames READY for export.

Pencil document: `ads/SH MY Adfolio Family B.pen`

---

## Frame-by-frame polish (the 5 items)

### 1. B_013 inbox-to-zero (`Y7zFb`)

**Issue:** BEFORE phone row text at 11pt body + 10pt status badges — borderline at thumbnail.

**Action:** Bumped all 5 row labels from 11pt → 15pt at weight 600. Bumped status badges (MISMATCH / ERROR / FAIL / MISSING) from 10pt/700 → 14pt/800. Title "End-of-Day Reconcile" from 14pt → 18pt. Increased phone screen padding from `[20,16]` → `[22,18]` and row gap from 10 → 12 to give the typography room to breathe.

**Verify:** Screenshot confirmed row labels (Cash drawer, Card terminal, E-wallet 01, Inventory sync, Receipts) and the red status badges all read at thumbnail. Phone now feels populated, not cramped. Brand-compliance preserved: yellow CTA + 2px black border untouched.

**Status:** READY

---

### 2. B_017 one-screen-one-truth (`ZI9jC`)

**Issue:** Spreadsheet column letters (A, B, C, D, E) rendering at 9pt — visual noise without informational value.

**Action:** Dropped the column header row entirely (deleted node `sellz`). Spreadsheet now leads directly with the numeric rows + red `#ERR` cells, which carry the metaphor on their own. The 9 remaining data rows fill the available height more substantially without the header.

**Verify:** Screenshot confirms a cleaner BEFORE → AFTER read. The pink `#ERR` cells are the visual carrier; column letters were taking space without adding meaning. Brand: cream bg, orange-stroke AFTER box preserved.

**Status:** READY

---

### 3. B_020 calendar-consolidated (`r27MX`)

**Issue:** "Calendar block grain on the AFTER side too many small subdivisions. Reduce to 4 clean colour blocks with generous spacing."

**Interpretation:** The AFTER side already had 4 colour blocks (Orders / Stock / Loyalty / Reports). The polish need was visual heft + generous spacing, not block count. Increased internal padding on each block from 12 → 18, container gap 8 → 14, container padding 14 → 20. Bumped block labels from 22pt → 26pt, time stamps from 14pt → 15pt. Corner radius 8 → 12 for a softer, more deliberate read.

**Verify:** Screenshot shows AFTER blocks now read with confidence — labels are the dominant element, time annotations sit cleanly to the right. BEFORE chaos calendar (intentional contrast) left untouched. Dark green `#0E3D32` bg preserved per Round 2 decision.

**Status:** READY

---

### 4. B_022 free-from-tool-stack (`X8qvEY`)

**Issue:** Single StoreHub mark at 280×120 too small against the 96pt headline.

**Action:** Grew the SH Mark frame from 280×120 → 340×140 (~20% larger). Bumped "StoreHub" text inside from 52pt → 62pt. Corner radius 24 → 28 to scale proportionally. Mark is wrapped in a flex container with `alignItems: center` so it stayed centred without manual repositioning.

**Verify:** Screenshot confirms the mark now wins the eye in the bottom half. 12-icon BEFORE grid → 1 dominant orange mark below — the "12 tools collapse into ONE" visual point now lands. Purple bg + drop shadow on the mark preserved.

**Status:** READY

---

### 5. B_021 cafe-full-house (`O1HcRv`)

**Issue:** Round 2 regen made the LEFT side an empty cafe instead of "unhappy customers walking out" (original brief). Round 3 allowed one or two regen attempts with strict no-text constraint.

**Path chosen:** REGENERATED. Used `Generate("SCwUk", "ai", ...)` with prompt explicitly requesting "one or two Pan-Asian customers walking toward the exit door looking dissatisfied" + the same hard no-text guard rails ("ABSOLUTELY NO TEXT anywhere in the image. NO signage with words. NO letters or numbers on any surface. NO menu boards, NO chalkboards with writing, NO labels.")

**Result:** First attempt succeeded. New LEFT image shows the cafe interior with 2 Pan-Asian figures: one walking toward the exit looking down at phone (slight body-language frustration), another in similar pose. Warm cream/terracotta palette matches the AFTER side stylistically. **No text or signage anywhere in the scene.** The narrative read on B_021 is now stronger than Round 2:

- **Before:** dissatisfied customers leaving (lost connection, no loyalty)
- **After:** lively full cafe with barista at StoreHub POS (loyal customers + new ones)

**Why this path:** First regen attempt cleared both constraints (the unhappy-customer brief AND the no-Malay-typo constraint), so no need to fall back to the empty cafe.

**Status:** READY

---

## Untouched frames (per instructions — do NOT touch)

| Frame | Node ID | Status |
|---|---|---|
| B_014 shoebox-to-sorted | `g2Dyk` | READY (approved Round 2) |
| B_015 growing-your-shop | `KHdvY` | READY (approved Round 2) |
| B_016 old-vs-new-car | `S42Ff` | READY (approved Round 2) |
| B_018 turtle-vs-cheetah | `WsOOX` | READY (approved Round 2) |
| B_019 one-platform | (per Round 2 build) | READY (approved Round 2) |

---

## Final approval status

| # | Frame | Node ID | Status |
|---|---|---|---|
| 1 | B_013 inbox-to-zero | `Y7zFb` | READY |
| 2 | B_014 shoebox-to-sorted | `g2Dyk` | READY |
| 3 | B_015 growing-your-shop | `KHdvY` | READY |
| 4 | B_016 old-vs-new-car | `S42Ff` | READY |
| 5 | B_017 one-screen-one-truth | `ZI9jC` | READY |
| 6 | B_018 turtle-vs-cheetah | `WsOOX` | READY |
| 7 | B_019 one-platform | (Round 1) | READY |
| 8 | B_020 calendar-consolidated | `r27MX` | READY |
| 9 | B_021 cafe-full-house | `O1HcRv` | READY |
| 10 | B_022 free-from-tool-stack | `X8qvEY` | READY |

**10 of 10 READY. 0 FLAGGED.**

---

## Export instruction (for Zaid)

```bash
python scripts/export_pen.py "ads/SH MY Adfolio Family B.pen" --out-dir ads/batches/MY-batch_004/round3
```

This will split each of the 10 Family B frames into native-resolution 1080×1080 PNGs into `ads/batches/MY-batch_004/round3/`. Frames T11/T5/T7/T12 in this `.pen` belong to other batches and the script should only pick up the `B_xxx` named frames — verify the output folder contains exactly 10 PNGs before uploading.

---

## Brand variables (unchanged)

All on file: `sh-orange` `#ff9419`, `sh-orange-bold` `#ff630f`, `sh-black` `#2f2922`, `sh-pink` `#ff546f`, `sh-azure` `#2a6ee8`, `sh-cream` `#fff8ea`, `sh-white` `#ffffff`, `sh-yellow` `#FFD93A`, `sh-light-purple` `#E8DCFC`, `sh-light-pink` `#FFE6E6`, `sh-dark-green` `#0E3D32`, `sh-purple` `#7C5BE6`, `font-headline` `Barlow`, `font-body` `Open Sans`.

---

## Round 3 changes summary

- 4 frames edited (B_013, B_017, B_020, B_022) — typography/sizing only
- 1 frame regenerated (B_021) — LEFT image swapped via AI gen
- 5 frames untouched (B_014, B_015, B_016, B_018, B_019)
- 0 headlines / CTAs / wordmarks / core layouts changed
- 0 new components or variables added
- 0 frames blocked
