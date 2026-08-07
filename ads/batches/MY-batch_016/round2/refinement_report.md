# Family N — Round 2 Refinement Report

**Container:** `cBTuM` y:88000
**Critique lens:** every numerical/authority claim traceable to verified anchor set?

## Verified anchor set
- From RM3.40/day
- 24-hour setup
- 17,000+ MY merchants

## Fixes applied
1. **N_N7** anchor line rewritten to "Setup time for 17,000+ MY merchants." — clearer link between the 24-hour claim and the 17k operator base.
2. **N_141** headline 74pt → 66pt so the long line fits comfortably in the top scrim band.
3. **N_142** headline + sub repositioned to avoid the warning triangles colliding with the read.
4. **N_149** headline + sub repositioned so the boat and wave illustration breathe between them.
5. **N_N10** headline pushed below the open-quote glyph so the testimonial framing reads as quotation, not stray decoration.

## Authority audit (per frame)

| Frame | Claim | Source |
|---|---|---|
| N_141 | none numerical, descriptive only | n/a |
| N_142 | none numerical | n/a |
| N_144 | none numerical | n/a |
| N_146 | none numerical | n/a |
| N_147 | none numerical | n/a |
| N_149 | none numerical | n/a |
| N_N7 | "24 HOURS" + "17,000+ MY merchants" | both verified |
| N_N8 | "17,000+" + "From RM3.40/day" | both verified |
| N_N9 | "RM3.40" + "24-hour setup" + "Built for MY F&B" | all verified |
| N_N10 | "17,000+ MY merchants" + "RM3.40/day" | both verified |

No fabricated statistics. No "94%" / "73%" / "152 hours" claims pulled forward.

## Pricing-anchor conflict (flagged in env brief)
- This batch uses `RM3.40/day` because the master ADFOLIO production prompt for these frames specifies it verbatim.
- `config/products.json` says "never use /day or /month". This is a known live conflict noted in the env brief.
- Followed production prompt as directed; flagging here for human decision.

## FLAGGED for human review post-render
- N_141 — confirm bridge photo lands as cinematic / not stock-photo
- N_144 — confirm merchant is Pan-Asian and the STOP sign actually rendered
- N_146 — confirm the bouquet looks out-of-place against the kopitiam counter
- N_147 — confirm handwritten Bahasa Malaysia / English supplier list rendered

## Layout audit
- `snapshot_layout(parentId:cBTuM, problemsOnly:true)` returned no problems.
