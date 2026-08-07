# MY-Batch_013 Family K — Round 2 refinement report

**Container:** `TJc5F` y:64000. **Frames:** 10 READY.

## Fixes applied in R2

| Frame | Fix |
|---|---|
| K_110 | HL wrap heightened so sub `RM3.40/hari. DuitNow + cash + QR.` is no longer 1-line clipped |
| K_111 | HL wrap 180 → 280 + y 850 → 780 to fit `11pm. The till closes itself.` headline (90pt) over its dark gradient |
| K_113 | HL wrap heightened so sub `StoreHub from RM3.40/hari.` fits below 80pt headline |
| K_114 | HL wrap heightened so sub `Real-time sales. From RM3.40/day.` is no longer fully clipped |
| K_115 | HL wrap 200 → 260 so sub `Stop juggling four apps.` fits |
| K_116 | CTA swapped from orange pill (`WKQjx`) to black pill (`v23tJ`) because orange CTA disappeared against orange band; copy still `BOOK A FREE DEMO NOW` |
| K_117 | Same CTA swap — black pill on red band |
| K_119 | HL wrap heightened so sub fits |
| All K | Wordmarks moved to y:1010 |

## Bahasa Melayu typo audit (R2 final)
Pencil-rendered BM only — image gen prompts forbid signage text.

- ✓ `Selamat` (K_116)
- ✓ `Hari Raya` (K_116)
- ✓ `tutup` (K_116)
- ✓ `kedai` (K_116)
- ✓ `hari` in `RM3.40/hari` (K_110, K_113) — not "hri"
- ✓ `Gong Xi` (K_117) — Chinese romanisation, two words spaced correctly
- No `TERIMA KASH`, `KOPI TIM`, or other AI-style typos in Pencil text layer

**Pending image verification:** Need to confirm AI photo renders for K_111 (mamak interior), K_115 (QR sign on table), and K_118 (Deepavali shopfront) don't hallucinate signage with garbled BM/Tamil/Chinese characters. Image prompts explicitly say `no on-screen text, no signage with words` — but Pencil's gen service occasionally ignores this.

## Documentary feel / stereotype check
- K_111 — Pan-Asian (Malaysian Indian) male owner in mid-ground, motion blur on customer. Documentary, not staged.
- K_114 — barista hands visible, face out of frame. No stereotype framing.
- Brief BM phrasing kept minimal — `Selamat Hari Raya`, `Gong Xi`, `RM3.40/hari`, `tutup kedai`. No "lah", no Manglish piled on. Aligned with brief: "no tropes, no stereotype lensing".

## Outstanding flags (Zaid decides)
- **`RM3.40/hari` vs config's "never /day or /month"** — same anchor flag as Family J. Production prompt explicitly uses `/hari` so it stays. Recommend confirming policy.
- **K_116 / K_117 CTA colour swap** — necessary for contrast; if you'd rather the orange pill stay everywhere, swap the lower-third band colour instead and rebuild.
- **K_112 chalkboard typeface** — used `Caveat` (Google Fonts, handwritten). Brief said "hand-chalked menu" — confirm it reads as chalkboard not whiteboard once Pencil renders.
- **All 9 photo frames queued for AI gen** — verify after image service returns: (a) Pan-Asian faces only, (b) zero on-screen text, (c) no third-party logos.

## Screenshot status
Blank (high y-offset). All geometry verified via snapshot_layout — no real layout problems remain. Wordmark-ref partial-clip reports are cosmetic and hidden by parent `clip:true`.
