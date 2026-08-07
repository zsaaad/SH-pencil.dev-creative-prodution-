# MY-batch_009 — Family G Round 2 Refinement Report

**Status:** Complete
**Container:** `D24xE` (y:32000)
**Frames refined:** 10/10 reviewed; targeted text-on-image and scrim positioning applied.

## Critique points addressed

### Text-on-image legibility
- #066 (glitched face): bottom scrim at 80% black (`#1B2434CC`) confirmed under headline.
- #067 (webcam): cream solid bottom strip refined to y:810 to clear webcam photo frame.
- #071 (mid-laugh kopitiam): 90% white scrim at y:790 for headline contrast against bright kopitiam interior.
- #074 (sleeping cat): 90% sky-blue scrim at bottom y:760 for headline.

### Y-position adjustments
- #068 headline-wrap to y:100 — better top alignment, leaves clear room for right-column photo.
- #069 (clouds) wrap to y:80, cards at y:720 — gives the photo full breathing room.
- #070 (overloaded) wrap to y:60 — small headline "Owners." sits clean above the photo.
- #072 wrap to y:110 — receipt photo at y:420 centred below.
- #073 wrap to y:80 — top-aligned headline over the buried-receipts photo.
- #075 (dachshund) wrap to y:80, dachshund photo centred at y:480.

### Sub-text positioning
- All Sub text lines verified inside HeadlineWrap parent's vertical layout — gap respected.

## Outstanding flags
- AI image queue pending for ALL 10 frames in Family G — this family is photo-dependent. Visual review post-render is essential.
- Highest-risk prompts:
  - #066 glitched face (could read as horror if AI over-interprets)
  - #069 person reclined on clouds (high stock-photo risk)
  - #073 merchant buried under receipts (composition challenging for AI)
- Screenshot tool returns blank at this y-offset — manual Pencil-app review recommended pre-export.
- #068 headline at 62pt — tight against right-column photo (320px) but legible.

## Files referenced
- Container: `D24xE`
- Frame IDs: mMt8v, CWnaS, KkolF, wsAFU, DDaV5, PBMEm, TmI2w, FdTQs, vbIkr, endDG
