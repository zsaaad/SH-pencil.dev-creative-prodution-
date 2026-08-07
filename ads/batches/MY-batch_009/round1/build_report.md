# MY-batch_009 — Family G (Photo as Hero / Documentary) Round 1 Build Report

**Status:** Complete (10/10 frames ready)
**Pencil document:** `ads/SH Pencil ads batch 2.pen`
**Container node ID:** `D24xE`
**Y-offset:** 32000
**Layout:** Vertical stack of ten 1080x1080 frames, 200px gap, 200px padding, light grey backing.

## Frames built

| ID | Name | Frame ID |
|---|---|---|
| #066 | glitched-face | mMt8v |
| #067 | webcam-selfie | CWnaS |
| #068 | confused-merchant | KkolF |
| #069 | person-in-clouds | wsAFU |
| #070 | owner-overloaded | DDaV5 |
| #071 | mid-laugh-kopitiam | PBMEm |
| #072 | crumpled-receipt | TmI2w |
| #073 | buried-under-receipts | FdTQs |
| #074 | sleeping-cat | vbIkr |
| #075 | long-dachshund | endDG |

## Composition approach
- Photo dominates each frame — 1080x1080 full-bleed where the photo is the hero (066, 067, 069, 071, 073, 074), or 800x600 / 320x680 photo on a coloured background where the spec calls for context.
- Strong contrast scrims (semi-transparent panels, ~90% opacity in hex alpha) placed behind headlines that sit on busy photo areas. Approach matches the global brief's text-on-image rule.
- Pan-Asian merchant photography only. All AI image prompts explicitly request: "Pan-Asian Malaysian merchant," "no text," "no signage," "documentary editorial."
- G_069 (person in clouds): built 3 small floating "Sales / Stock / Loyalty" cards as nested frames over the cloud image.

## Judgement calls
- #066 (glitched face): Used a 80% black scrim (`#1B2434CC`) over the bottom 400px for headline contrast. Stylised glitch described in prompt — not horror, just digital distortion.
- #067 (webcam): Cream-coloured solid bottom strip (no transparency) for the headline — matches the spec's "lower strip cream" cue.
- #069 (clouds): Cards positioned at fixed coords across the frame width with vertical text inside.
- #071 (mid-laugh kopitiam): 90% white scrim over bottom 360px for the Manglish headline. Manglish copy verbatim per spec.
- #073 (buried receipts): Top 380px purple scrim at 80% opacity over the photo for headline legibility.
- All headlines kept 72-100pt — readable against busy photographic backgrounds.

## FLAGGED items
- AI image generations pending for all 10 frames. Documentary feel hinges on prompt quality — manual review post-render recommended.
- #066 glitch effect depends on AI interpretation — may need re-roll if too aggressive/horror.
- #069 surreal "person reclined on clouds" — high risk for AI prompt to look staged/stock. Flag for review.
- Screenshot tool returning blanks at this y-offset.

## Layout issues observed
- Same false-positive clip warnings on refs.
- All sub texts sit immediately under headlines inside fit_content wraps — visually fine.
- One real concern: G_068 right-column photo (320x680) is wide enough that headline column (620px) constrains the type to 62pt — text reads tight but still legible.

## Token estimate
~14k tokens across this family (2 batch_design calls).
