# MY-Batch_012 Family J — Round 1 build report

**Container:** `Yscvh` "Family J — J_097 to J_109" at y:56000, width 7200 (widened from 6000 after right-edge frames clipped).
**Frames built:** 13 / 13 — `J_097`–`J_109`, all 1080×1080.
**Status:** READY.

## Frame map
| ID | Node | Concept | Notes |
|---|---|---|---|
| J_097 | VavU6 | 5 stages kopitiam EOD | Mountain silhouette + 5 numbered orange-circle steps below |
| J_098 | b537Wn | 8 ways cut EOD time | Purple bg, yellow Barlow Black headline, 3 floating envelopes |
| J_099 | bPwjt | 17 closing-shift tricks (beanie merchant) | AI photo right-half, BG generation queued |
| J_100 | QA826 | Write epic supplier orders | Purple bg, single orange envelope graphic, yellow headline |
| J_101 | fLiFe | Pillow checklist | Lilac bg, white rounded pillow with 3-tick checklist |
| J_102 | FoiS8 | Choose your shop's system | Navy bg, 3 radio toggles, StoreHub selected (orange row) |
| J_103 | A3EJjB | Cash discrepancies chart | Bar chart rebuilt with absolute positioning after flex chart clipped bars |
| J_104 | A5CZN | What is a great kopitiam (webinar) | Purple, geometric shape confetti |
| J_105 | Gbutg | MY employment compliance | Purple gradient + chat bubble |
| J_106 | y4FWF | Calculator | Purple, full calculator UI with mock display "RM 1,920 saved" |
| J_107 | NWOkf | Daily reporting habit (woman + iPad) | Pink bg, AI illustration queued |
| J_108 | c1kPw | Heat-map menu insight | Cream bg, mock menu UI with BESTSELLER/HOT/DUD tags + heat-coloured rows |
| J_109 | KWW8F | Weak till-pad PINs | Light blue bg, white card listing 4 weak PINs with strikethrough + red X |

## AI render queue
- `J_099` photo `dMG0v` — Pan-Asian merchant in beanie with tablet
- `J_107` photo `ftyBc` — illustration of Pan-Asian woman merchant with iPad

## Judgement calls / deviations
- **`/day` vs `/year`:** Followed brief verbatim — `From RM3.40/day` anchor used on J_099. **FLAGGED** for Zaid: `config/products.json` says "never use /day or /month", brief contradicts. Production prompt was treated as binding.
- **CTA override:** J_103 and J_106 sources said `DOWNLOAD REPORT` / `START CALCULATING`. Brief explicitly overrode to `BOOK A FREE DEMO NOW`. Applied as instructed.
- **J_103 chart bars** initially used horizontal-flex with `alignItems:"end"` but bars+labels overflowed; rebuilt using `layout:"none"` absolute positioning. Year labels now sit at y:400 below baseline.
- **Wordmarks** all repositioned to y:1010 after frame-clip overflow detected from 1020/1000 placements.
- **Container width** widened from 6000 to 7200 after right-edge frame (column index 5, x:5900) reported clipped.

## Snapshot_layout verification
All real layout problems resolved. Remaining `problems` reports are wordmark/CTA reusable refs whose intrinsic bbox slightly exceeds container — visible content stays inside `clip:true` parent frames.

## Round-2 critique focus
- Does each listicle actually deliver value at thumbnail glance? Numbers/labels legible? (J_097, J_101, J_109)
- Is the chart in J_103 readable now? Year labels visible against navy bg?
- J_108 menu rows — colour-coding intuitive without legend?
- J_106 calculator — does mock display read as "savings" not "input"?
- Confirm AI images on J_099 and J_107 land Pan-Asian, not Western.
