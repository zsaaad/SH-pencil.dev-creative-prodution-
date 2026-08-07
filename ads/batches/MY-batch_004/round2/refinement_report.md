# MY-Batch_004 · Family B · Round 2 Refinement Report

**Status:** COMPLETE. All 10 frames audited. 1 frame structurally refined (B_021). 9 frames left untouched — already meet spec.

Pencil document: `ads/SH MY Adfolio Family B.pen`

---

## Decisions on the 3 flagged items

1. **B_013 — yellow `#FFD93A` CTA + 2px black border.** KEPT as-is. At thumbnail, the dark border crisply outlines the yellow pill against the light-purple bg. CTA text "BOOK A FREE DEMO NOW" in black reads cleanly. Yellow gives this frame distinctive personality vs the rest of the orange-CTA set. No change.

2. **B_020 — off-brand dark green `#0E3D32` bg.** KEPT per brief. The dark green makes the BEFORE colourful-block calendar and the AFTER clean block stack pop with high saturation contrast. Swapping to brand black `#2f2922` would dull the calendar swatches. This is a one-off off-palette choice, used only in this single frame, and the brief specified it explicitly. Note for future cycles: if Zaid wants strict brand adherence, swap to `#2f2922` — visual cost is minor.

3. **B_021 — Malay signage typo ("Kafe Kita" / "Terima Kash" — note: AI rendered KASH not KASIH).** FIXED. Regenerated the left cafe image with explicit "NO TEXT anywhere" prompt instruction. Now shows a clean empty cafe interior (warm cream/terracotta palette, hanging lights, plants, wooden counter). Before/after read is now: empty cafe (lost customers) → full cafe (loyal customers). The Malay-typo signage is gone; visual concept preserved.

---

## Frame-by-frame audit table

| Frame | Issue Found | Action |
|---|---|---|
| B_013 inbox-to-zero | None — yellow+black border CTA confirmed legible at thumbnail. Phone screens are dense but the colour story (red errors vs green check) reads in 1 sec. | No change |
| B_014 shoebox-to-sorted | None — receipts photo on left vs clean orange-checkbox list on right is a textbook before/after. Headline wraps cleanly. | No change |
| B_015 growing-your-shop | None — gradient bg orients warmth to orange (after-side), grey to cold (before-side). White wordmark + white CTA both legible. | No change |
| B_016 old-vs-new-car | None — vehicle photos read documentary, not cartoonish. Pill labels on each photo are clear. | No change |
| B_017 one-screen-one-truth | None — spreadsheet grid with red error cells (left) vs clean dashboard list (right) carries the metaphor. Round 1 dropped the hand-rope illustration; the two-panel split is cleaner. | No change |
| B_018 turtle-vs-cheetah | None — AI photos returned editorial, not stock-cheesy. Tortoise on marble / cheetah on savannah. "3 weeks" vs "24 hours" reinforces the speed claim. | No change |
| B_019 one-platform | None — hand crops match in skin tone, lighting, wooden counter surface. Receipts pile vs tablet works at thumbnail. | No change |
| B_020 calendar-consolidated | Dark green is off-palette but works visually. KEPT per brief authority. | No change |
| B_021 cafe-full-house | Left cafe image had Malay signage with a typo ("TERIMA KASH" instead of "KASIH"). AI artifact, would read as broken to Malaysian viewers. | **FIXED — image regenerated, no text in scene, clean empty cafe** |
| B_022 free-from-tool-stack | None — 12-icon Lucide grid (BEFORE) vs single StoreHub orange mark (AFTER) reads instantly. Purple bg gives the headline punch. | No change |

---

## Fixes applied (full detail)

### B_021 — Left cafe image

- Set `SCwUk` (L Img frame) to `layout: "none"` (was inherited horizontal default).
- Generated a replacement image via `Generate("SCwUk", "ai", ...)` with explicit "NO TEXT anywhere in the image. NO signage with words. NO letters or words on any surface" guard rails.
- Result: empty Pan-Asian cafe interior, warm cream-and-terracotta palette, hanging string lights, potted plants, wooden counter, exposed-brick accent. Documentary illustration style matching the right (after) image.
- Removed all sticker-patch experiments — patching the original was worse than the typo because it covered too much of the cafe interior.

The narrative read on B_021 is now:
- **Before:** quiet, empty cafe (no customers, lost connection)
- **After:** full cafe with smiling barista at a StoreHub POS

---

## Items left for Round 3 (polish only)

These are deliberately punted to Round 3. None are structurally broken — all are micro-polish.

- **B_013 phone screens** — the BEFORE phone has 5 row items at 11pt — at sub-150px thumb, individual row text becomes unreadable. The colour story (red badges) still reads, which is what matters. Round 3 could enlarge to 3 rows + bigger type if testing shows weak performance.
- **B_017 spreadsheet thumb** — the BEFORE spreadsheet grid renders the red error cells but the column letters (F G H ...) are small. Visible-on-zoom only; not a thumbnail issue.
- **B_020 BEFORE calendar** — the multi-coloured tiny blocks are deliberately chaotic but the grain is dense. Could simplify to fewer larger blocks if it reads as visual noise.
- **B_022 SH mark size** — at 280×120 against the headline "Free your shop from the tool stack." (96pt), the mark could grow to 340×140 for more after-state emphasis. Not broken; just optimisable.
- **B_021 left image composition** — would be stronger with one visible unhappy customer walking out (the original brief), not a fully empty cafe. The empty version still carries the metaphor (lost customers) but is a softer read than the brief's exact vision. If Round 3 regenerates, prompt should add "one Pan-Asian customer walking toward the door, looking down at phone, slight frown" while keeping the no-text constraint.

---

## Brand variables registered (carried over from Round 1)

All on file: `sh-orange` `#ff9419`, `sh-orange-bold` `#ff630f`, `sh-black` `#2f2922`, `sh-pink` `#ff546f`, `sh-azure` `#2a6ee8`, `sh-cream` `#fff8ea`, `sh-white` `#ffffff`, `sh-yellow` `#FFD93A`, `sh-light-purple` `#E8DCFC`, `sh-light-pink` `#FFE6E6`, `sh-dark-green` `#0E3D32`, `sh-purple` `#7C5BE6`, `font-headline` `Barlow`, `font-body` `Open Sans`.

---

## Final state

- 10 frames built, named, on-canvas
- 1 frame refined (B_021)
- 9 frames untouched
- 0 frames blocked
- 0 frames pending re-render at session close
- Headline copy verbatim per brief on all 10 frames — verified
- CTA "BOOK A FREE DEMO NOW" verbatim on all 10 frames — verified
- Wordmark on all 10 frames — verified
- All 10 frames clipped at 1080×1080 — verified

Ready for Round 3 polish pass and PNG export.
