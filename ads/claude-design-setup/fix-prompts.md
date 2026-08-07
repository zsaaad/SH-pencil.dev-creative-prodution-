# Claude Design — Fix Prompts

Paste-in prompts to retroactively fix already-generated ads for Meta safe-zone compliance, and to set the rule for everything generated after this.

---

## Step 0 — Update "Any other notes?" first

Before fixing anything, update the design system "Any other notes?" field with the safe-zone block from `form-fields.md` (Field 6). Without that, fixes won't stick — Claude Design will regenerate to the same boundaries next time.

---

## Step 1 — One-shot fix prompt (paste into chat for each existing ad file)

For each ad file already created (`everest-metaphor.html`, `midnight-or-30-seconds.html`, `6-tools-or-1-1x1.html`, `6-tools-or-1-16x9.html`, `6-tools-or-1-9x16.html`), run this prompt:

> **Audit this ad against Meta safe zones and reposition any element that violates them.**
>
> **Safe-zone constraints (must be enforced):**
> - **1:1 (1080×1080):** all critical content (headline, sub-headline, CTA pill, logo) inside a 952×952 centered box. 64px padding all sides.
> - **16:9 (1920×1080):** all critical content inside 1720×830 centered (x=100→1820, y=100→930). CTA pill bottom edge at y ≤ 900. 100px top + side padding, 150px bottom.
> - **9:16 (1080×1920):** **headline top at y ≥ 280**, CTA pill bottom at **y ≤ 1400**, top-right logo at y ≥ 250. 64px side padding. The bottom 500px (y=1420 to y=1920) is a DEAD ZONE — runtime UI (Reels caption + like/comment/share + music sticker) covers it. Move all critical content out of the bottom 500px.
>
> **Action:**
> 1. Identify every element currently outside its format's safe zone.
> 2. Reposition by moving inward — never shrink the element to fit if it can be moved instead.
> 3. Preserve visual hierarchy: headline still largest, CTA still prominent, brand colours unchanged.
> 4. For 9:16 specifically: if the CTA pill is currently at the bottom edge, lift it so its bottom is at y=1400. The space between y=1400 and y=1920 should contain only background — no text, no buttons, no logo.
> 5. If recomposition forces a font-size change, prefer reducing background imagery margin over reducing text size.
>
> **Output:** show me the fixed file. Don't change the copy. Don't change the visual concept. Only fix positions.

---

## Step 2 — Verify

After Claude Design applies the fix, eyeball each file for:

- **1:1:** does the rendered preview show ≥64px breathing room on all four sides between critical content and canvas edge?
- **16:9:** does the CTA pill sit clear of the bottom 150px?
- **9:16:** **mentally overlay a 500px dead zone at the bottom.** Is anything critical in there? If yes, fix wasn't applied — re-prompt with: *"The CTA pill is still in the bottom 500px dead zone. Lift it so its bottom edge is at y=1400 maximum."*

For 9:16, the easiest mental check: the bottom 26% of the canvas should contain only background. If you see headline / CTA / logo in the bottom quarter of the screen — that's the dead zone.

---

## Step 3 — Going forward

Every new family prompt in `family-prompts.md` already says "Logo top-right inside safe zone" and "rounded orange CTA pill, ALL CAPS". After updating "Any other notes?", Claude Design will apply the new safe-zone constraints automatically for new generations. Still verify the first few outputs against the checklist below.

---

## Pre-launch checklist (use on every ad before sending to Meta Ads Manager)

- [ ] **1:1** — 952×952 centered; all critical content inside; 64px padding visible
- [ ] **16:9** — 1720×830 centered; CTA bottom at y ≤ 900; clear of in-stream overlay zone
- [ ] **9:16** — headline top at y ≥ 280; CTA bottom at y ≤ 1400; logo at y ≥ 250; bottom 500px contains only background
- [ ] No element clipped at any edge
- [ ] CTA pill fully visible and readable in mental Reels-preview overlay

---

## When Meta's spec changes

Re-verify the safe-zone numbers in `meta-safe-zones.md` every ~6 months. Meta has historically grown the 9:16 bottom safe zone roughly once a year as they add UI. Last verified: 2026-06-04.
