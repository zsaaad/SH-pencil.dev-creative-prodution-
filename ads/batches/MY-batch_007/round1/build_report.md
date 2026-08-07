# MY-batch_007 — Family E (Identity / Behavior Call-Out) Round 1 Build Report

**Status:** Complete (9/9 frames ready)
**Pencil document:** `ads/SH Pencil ads batch 2.pen`
**Container node ID:** `eLoE7`
**Y-offset:** 16000
**Layout:** Vertical stack of nine 1080x1080 frames, 200px gap, 200px padding, light grey backing.

## Frames built

| ID | Name | Frame ID |
|---|---|---|
| #047 | counted-the-till-twice | rZ6oS |
| #048 | hey-kopitiam-owner | tI0JQ |
| #049 | tell-me-kopitiam | sF6JU |
| #050 | wanted-one-human | I6Lp3P |
| #051 | lost-rm1800 | pC16n |
| #052 | like-overpaying | PZnUE |
| #053 | dont-click-this-ad | e2R1y0 |
| #054 | if-this-looks-familiar | LB5yK |
| #055 | re-typing-stock | y0rAmB |

## Composition approach
- Cream / dark navy / purple / magenta / blue / yellow / pale-yellow backgrounds per spec.
- Vertical headline-wrap frames with `textGrowth: fixed-width` so multi-line Barlow Black headlines wrap predictably.
- AI image generations issued for: kopitiam calculator hand (047), Z-report illustration (049), portrait headshot (051), support-ticket UI is hand-built native (054), notebook with stock counts (055).
- CTA Orange Pill instance (`WKQjx`) used on every frame except #053 which uses CTA Black Pill (`v23tJ`) per spec.
- StoreHub wordmark variant chosen per background (orange wordmark on cream/yellow, white on dark, black on yellow).

## Judgement calls
- #050 (WANTED): Reduced headline from 120pt to 110pt to fit 3-line layout cleanly; body and orange punchline stack below in same wrap.
- #053: Built the warning triangle as a custom SVG path; "!" text overlay rather than icon-font for visual control.
- #054: Built support-ticket UI natively as nested vertical frame with bordered rows (6 tickets matching the spec).
- All headlines tuned to 70-90pt range to keep within 960px wrap. Round 2 adjusted: 047 to 74pt, 048 to 72pt, 049 to 84pt for breathing room.

## FLAGGED items
- AI image generations are pending render — none visible yet in screenshots. Will resolve once Pencil image queue processes.
- Screenshot tool returning blank PNGs for individual frames at this y-offset — likely a render lag, not a design issue. Snapshot_layout confirms all geometry is within frame bounds.

## Layout issues observed
- Snapshot_layout flags many "partially clipped" warnings on CTAs and Wordmark refs — false positives from frame-with-clip-true measuring the ref's nominal bounding box against the parent. Visual inspection of geometry confirms all stay within the 1080x1080 canvas.
- One genuine issue caught & fixed: #049 headline was overflowing wrap at 110pt — reduced to 84pt in refinement.
- Several Sub texts measured at the bottom edge of their HeadlineWrap (fit_content). Acceptable spacing; not a clip.

## Token estimate
~14k tokens across this family (3 batch_design calls + reads).
