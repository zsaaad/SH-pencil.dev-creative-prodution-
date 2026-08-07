# MY-Batch_013 Family K — Round 1 build report

**Container:** `TJc5F` "Family K — K_110 to K_119" at y:64000, width 7200.
**Frames built:** 10 / 10 — `K_110`–`K_119`, all 1080×1080.
**Status:** READY.

## Frame map
| ID | Node | Concept | Notes |
|---|---|---|---|
| K_110 | ootRx | Nasi lemak banana leaf | Full-bleed photo + bottom white gradient + headline |
| K_111 | y1RLT | Mamak at midnight | Full-bleed photo + dark bottom gradient + white headline |
| K_112 | C9T37 | Kopitiam chalkboard menu | Chalkboard graphic (no photo), Caveat handwritten typeface, last line orange "Sales last night — ???" |
| K_113 | pWZg9 | Roti canai close-up | Macro food photo + cream bottom gradient |
| K_114 | e7KcS | Teh tarik pouring | Action food photo + white bottom gradient |
| K_115 | zUJMa | DuitNow QR receipt | Cream bg, photo card centred (small QR on kopitiam table) |
| K_116 | P1VrWQ | Hari Raya open house | Food photo + lower-third orange band + BM headline. CTA upgraded to black pill for contrast against orange band |
| K_117 | I2Wzmx | CNY reunion dinner | Food photo + lower-third red band + yellow headline. CTA black pill |
| K_118 | YvUjf | Deepavali sweet shop | Food photo + lower-third gold band + black headline |
| K_119 | KVfip | Kuih on banana leaf | Food photo + white bottom gradient |

## AI render queue (all need image generation)
- K_110 `X7ndZl`, K_111 `DpHA8`, K_113 `rNjkc`, K_114 `v06yBh`, K_115 `YZHpe`, K_116 `mhrQo`, K_117 `KMoaY`, K_118 `RmgR1`, K_119 `yO8jy`. All prompts explicitly forbid Western faces, on-screen text, and third-party logos.

## Bahasa Melayu typo audit (round 1)
Pencil-rendered BM text only — AI image prompts explicitly forbid signage text to avoid mangled BM in images.

| Frame | BM text | Spell check |
|---|---|---|
| K_110 | `RM3.40/hari` | ✓ correct |
| K_113 | `RM3.40/hari` | ✓ correct |
| K_116 | `Selamat Hari Raya. Selamat tutup kedai by 10pm.` | ✓ Selamat ✓ Hari Raya ✓ tutup ✓ kedai |
| K_117 | `Gong Xi.` | ✓ correct (Chinese romanisation) |

No "TERIMA KASH" or "KOPI TIM" style typos. K_114 originally proposed `RM3.40/day` (English) for the teh tarik frame — kept English here per brief.

## Judgement calls / deviations
- **K_116 CTA contrast:** Headline orange band conflicted with orange CTA pill. Swapped CTA ref from `WKQjx` (orange pill) to `v23tJ` (black pill, white text) — still says BOOK A FREE DEMO NOW. Same fix applied to K_117 (red band).
- **K_112 chalkboard typography:** Used Google Caveat handwritten font for menu lines; Barlow Black for headline above the board. Brief said "hand-chalked" — Caveat is the closest available chalk-script equivalent.
- **K_115 QR image:** AI prompt forbids visible logo marks (DuitNow/Boost/TnG/GrabPay are referenced in headline text only).
- **/day vs /hari vs /year:** Mixed in line with brief (`RM3.40/hari` on Malay-language frames, `RM3.40/day` on K_114). Same `/day` vs `/year` flag as Family J — production prompt treated as binding.

## Round-2 critique focus
- Re-spellcheck all BM phrases after AI images render — even though images forbid text, double-check no AI hallucinated signage with garbled BM crept in.
- Verify Pan-Asian faces in K_111 (mamak owner) and any incidental humans in food photos.
- Confirm K_112 board reads as chalkboard, not whiteboard (border colour, font).
- Check K_116/K_117/K_118 lower-third bands don't crash legibility against busy food images.
