# MY-batch_008 — Family F (Audacious Single-Word / Single-Phrase Typography) Round 1 Build Report

**Status:** Complete (10/10 frames ready)
**Pencil document:** `ads/SH Pencil ads batch 2.pen`
**Container node ID:** `f90mX`
**Y-offset:** 24000
**Layout:** Vertical stack of ten 1080x1080 frames, 200px gap, 200px padding, light grey backing.

## Frames built

| ID | Name | Frame ID |
|---|---|---|
| #056 | receipt-books-so-2019 | zf2yC |
| #057 | slam-dunk | PM1Cj |
| #058 | goodbye-spreadsheets | X6xraJ |
| #059 | dont-risk-it-balloon | iSx9J |
| #060 | bullet-proof-close-out | BRihC |
| #061 | wave-goodbye-eod | i5LQ3h |
| #062 | receipts-great | KFSQW |
| #063 | tired-of-lockin | ANEmD |
| #064 | tougher-than-ever | XPJ8u |
| #065 | susah | r5ZOUa |

## Composition approach
- Type IS the design. All headlines Barlow Black 900-weight, sizes 120-380pt to dominate the frame.
- Massive typography centred or top-left; supporting elements (speech bubble, balloon, photo) sized as secondary.
- AI image generations issued for: basketball dunk in kopitiam (057), thermal printer apron (060), waving hand (061), receipt roll unspooling (062), sleeping pug (063), b/w merchant with clipboard (064).
- F_059 balloon-and-thorn built natively: yellow ellipse + black SVG-path thorn shape + text labels.
- F_058 "GOODBYE / SPREADSHEETS / HELLO / STOREHUB" rendered at 150pt (down from 170pt to fit width cleanly after R2 fix).

## Judgement calls
- #056 (RECEIPT BOOKS): Headline at 140pt (refined from 160pt for clean two-line layout) with yellow speech bubble + "BORING." overlay.
- #058 (GOODBYE SPREADSHEETS): Refined to 150pt — 170pt overflowed the 960px wrap. Still hero-scale.
- #065 (Susah): Refined to 320pt (from 380pt) to keep within the 1080px frame. Still the largest single word in the batch.
- #060 (BULLET-PROOF): Used `sh-purple` variable for the purple headline on yellow bg (matches spec colour).
- #064 (TOUGHER THAN EVER): Photo restricted to right 320px column; headline owns left 620px.

## FLAGGED items
- AI image generations pending — F_057 dunk, F_060 apron, F_061 wave hand, F_062 receipt roll, F_063 pug, F_064 b/w merchant.
- F_059 thorn SVG is approximate — a star-burst shape standing in for a thorn. Visually reads as sharp/danger; can be refined later.
- Screenshot tool returning blanks at this y-offset (renderer lag with large doc) — geometry confirmed via snapshot_layout.

## Layout issues observed
- Same "partially clipped" false positives on CTA/Wordmark refs across the family (measured by snapshot, not actually clipping).
- One real overflow fixed in R2: F_056 headline 160→140pt, F_058 170→150pt, F_065 380→320pt.
- Sub texts in headline wraps sit at fit_content bottom edge — visually fine; spec calls for them to sit immediately under headline.

## Token estimate
~13k tokens across this family (3 batch_design calls).
