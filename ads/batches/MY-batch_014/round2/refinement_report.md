# Family L — Round 2 Refinement Report

**Container:** `Sso3K` y:72000
**Critique lens:** for wildcards, is the risk paying off or burying the offer?

## Fixes applied

1. **Courier New invalid font** (8 nodes across L_128 memo + L_130 receipt) → swapped to `JetBrains Mono` to preserve the typed-memo / thermal-receipt feel without the font error.
2. **L_120 microcopy too small** — italic body bumped from 24pt to 32pt and darkened from `#7a7a7a` to `#5a5a5a` so the gag actually reads.
3. **L_123 Pac-Man** — headline pushed to y:60, Pac-Man+ghost cluster repositioned for cleaner left-to-right chase line.
4. **L_126 audit-warning** — headline moved to y:60, sub repositioned so the yellow diamond is the visual centre.
5. **L_129 sticky-notes** — original black headline competed with yellow notes against AI photo bg. Added `#2f2922cc` scrim band top of frame, swapped to white headline. Original black headline disabled.

## R2 verdict per frame

- **L_120**: kept the restraint, made it readable. Risk paying off.
- **L_121**: 240pt orange ticker is dominant. CTA below is sufficient. Pass.
- **L_122**: photo-only frame depends on Meta caption working. Highest risk. Pass with the documented caveat.
- **L_123**: retro chase metaphor lands. Pass.
- **L_124**: crossword spells STOREHUB across — payoff is fast. Pass.
- **L_125**: self-aware "still works" is meta but supports the offer. Pass.
- **L_126**: yellow diamond on black gives the warning feel; "Scary, isn't it?" intercepts. Pass.
- **L_127**: pending AI render. If too photographic, swap fill to flat 2-tone illustration in next pass.
- **L_128**: URGENT stamp is the eye magnet, memo body carries product reasoning. Pass.
- **L_129**: 7 sticky notes cover the kopitiam pain list. Pass once AI desk render lands.
- **L_130**: receipt-as-canvas is the strongest L concept; total line ties to RM3.40/day. Pass.

## FLAGGED for human review post-render
- L_122 — confirm the AI render shows a Pan-Asian merchant (not Western default)
- L_127 — confirm the risograph image came back as 2-tone, not photographic
- L_129 — confirm desk photo composition leaves space behind sticky notes

## Layout audit
- `snapshot_layout(parentId:Sso3K, problemsOnly:true)` returned "No layout problems."
