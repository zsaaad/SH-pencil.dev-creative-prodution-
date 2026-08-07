# Meta Ad Safe Zones — for Claude Design

Every ad Claude Design produces must keep critical elements inside the safe zones below. Otherwise Meta's runtime UI (profile bar, caption sticker, like/comment/share, music attribution, in-stream CTA bar) covers them at delivery — invisible in Ads Manager preview.

---

## The three formats — exact safe-zone boundaries

### 1:1 Square (1080×1080) — Feed

| Dimension | Value |
|---|---|
| Canvas | 1080 × 1080 |
| Top buffer | 64px (y=0 to y=64) |
| Bottom buffer | 64px (y=1016 to y=1080) |
| Side buffer | 64px each (x=0 to x=64, x=1016 to x=1080) |
| **Safe zone** | **952 × 952 centered (x=64→1016, y=64→1016)** |

All headlines, sub-headlines, body copy, CTA pills, logos, and other critical visual elements must fit inside the 952×952 safe zone. Background imagery and decorative gradients may extend full-bleed.

---

### 16:9 Landscape (1920×1080) — In-stream + Feed video

| Dimension | Value |
|---|---|
| Canvas | 1920 × 1080 |
| Top buffer | 100px (y=0 to y=100) |
| Bottom buffer | 150px (y=930 to y=1080) — accommodates in-stream CTA bar overlay |
| Side buffer | 100px each (x=0 to x=100, x=1820 to x=1920) |
| **Safe zone** | **1720 × 830 centered (x=100→1820, y=100→930)** |

CTA pill must end at y ≤ 900. Bottom 150px is dead — Meta's in-stream "Learn more" bar lands there.

---

### 9:16 Vertical (1080×1920) — Stories + Reels — CRITICAL

| Dimension | Value |
|---|---|
| Canvas | 1080 × 1920 |
| Top buffer | **250px** (y=0 to y=250) — profile bar, "Sponsored" tag, story timer |
| Bottom buffer | **500px** (y=1420 to y=1920) — caption + like/comment/share + music sticker chrome |
| Side buffer | 64px each |
| **Safe zone** | **952 × 1170 centered (x=64→1016, y=250→1420)** |

**Hard rules for 9:16:**
- Headline starts at `y ≥ 280` (28px buffer below top safe zone)
- CTA pill bottom edge at `y ≤ 1400` (20px buffer above bottom safe zone)
- Top-right logo starts at `y ≥ 250` (just below profile bar overlay)
- Bottom 500px is DEAD ZONE — no critical content, no CTA, no key copy

**Why we use the Reels spec (500px) and not Stories (250px) for the bottom:** Reels has more aggressive UI chrome (caption + like/comment/share buttons + music sticker). Designing to Reels passes Stories automatically. Designing to Stories breaks on Reels.

---

## Visual reference (ASCII)

```
1:1 Square                16:9 Landscape              9:16 Vertical
1080×1080                 1920×1080                   1080×1920

┌────────────────┐        ┌──────────────────────┐   ┌────────────┐
│■■■■■■■■■■■■■■■■│ 64     │■■■■■■■■■■■■■■■■■■■■■■│   │■■■■■■■■■■■■│
│■┌────────────┐■│        │■■■■■■■■■■■■■■■■■■■■■■│   │■■■■■■■■■■■■│ 250
│■│            │■│        │■┌──────────────────┐■│   │■■■■■■■■■■■■│
│■│  SAFE ZONE │■│        │■│   SAFE ZONE      │■│   │■┌────────┐■│
│■│  952×952   │■│        │■│   1720×830       │■│   │■│        │■│
│■│            │■│        │■└──────────────────┘■│   │■│  SAFE  │■│
│■│            │■│        │■■■■■■■■■■■■■■■■■■■■■■│ 150│■│  ZONE  │■│
│■└────────────┘■│        └──────────────────────┘   │■│952×1170│■│
│■■■■■■■■■■■■■■■■│ 64                                │■│        │■│
└────────────────┘                                   │■└────────┘■│
                                                     │■■■■■■■■■■■■│
                                                     │■■■■■■■■■■■■│ 500
                                                     │■■■■■■■■■■■■│
                                                     └────────────┘
```

`■` = unsafe zone (covered by UI / cropped / risk area)

---

## How Claude Design should apply this

When generating each ad layout:

1. **Build a CSS safe-zone container** inside the canvas with the padding values above. All critical content (text, CTA, logo) sits inside that container. Background imagery is the only thing allowed full-bleed.

2. **For 9:16 specifically:** put a non-visible 250px "header gutter" at top and a 500px "footer gutter" at bottom. Nothing critical crosses those lines.

3. **CTA pill placement on 9:16:** the pill's bottom edge must be at or above y=1400. If the design needs the CTA "at the bottom" visually, that means the BOTTOM of the pill is at y=1400, not the canvas edge.

4. **Logo position:** for 9:16, top-right logo starts at y ≥ 250. For 1:1 and 16:9, top-right logo respects the side + top buffer.

---

## Production checklist

- [ ] 1:1 — all critical content inside 952×952 centered
- [ ] 16:9 — all critical content inside 1720×830, CTA pill bottom at y ≤ 900
- [ ] 9:16 — headline top at y ≥ 280, CTA pill bottom at y ≤ 1400, logo top at y ≥ 250
- [ ] No content in bottom 500px of 9:16 (caption + UI dead zone)
- [ ] No content in bottom 150px of 16:9 (CTA bar dead zone)
- [ ] Preview the 9:16 against a Reels safe-zone overlay before exporting
