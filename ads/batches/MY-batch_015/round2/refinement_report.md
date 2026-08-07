# Family M — Round 2 Refinement Report

**Container:** `UmJXB` y:80000
**Critique lens:** is the compare legally clean AND visually unambiguous?

## Fixes applied

1. **M_131 stick figures** — face glyphs 54pt → 120pt so the slumped vs. smiling read works at thumbnail size.
2. **M_133 suitcase positions** — handles re-aligned to bag tops; small bag pulled to y:460 and shrunk to 290pt height so the size delta is obvious.
3. **M_135 shield rotation** — hexagonal polygon defaults to point-right in Pencil; rotated 90° so it reads as a shield.
4. **M_134 headline** — pulled to y:280 so geometric shapes (Geo1/Geo2/Geo3) form a frame around the type.
5. **M_136 we-say-you-say** — increased line-height so the 3-line "we say / you say" rhythm reads as a list; punchline bumped to 140pt orange to land hard.
6. **M_139 yellow bg** — headline 110pt → 88pt with tighter line-height so the copy fits without clipping the lunch reference.
7. **M_140 CALCULATE NOW** — secondary CTA repositioned to y:660 so the orange demo pill at y:820 is still the dominant primary CTA.

## Legal-clean R2 audit (per frame)

| Frame | Real brand leak? | Pass |
|---|---|---|
| M_131 | "Without StoreHub" — generic. No. | ✓ |
| M_132 | "manual close-out" — generic. No. | ✓ |
| M_133 | "legacy POS fees" — generic. No. | ✓ |
| M_134 | Pun only, no brand reference. | ✓ |
| M_135 | "More apps" — generic. SH is the only mark. | ✓ |
| M_136 | "POS" is a category, "StoreHub" is the brand. No competitor. | ✓ |
| M_137 | Abstract symbol icons, no logos. | ✓ |
| M_138 | "Suppliers / staff / taxes" — generic. No. | ✓ |
| M_139 | None. | ✓ |
| M_140 | Klang / PJ / Penang are MY cities, not brands. | ✓ |

## FLAGGED for human review
- M_134 — confirm the purple #9F7BFF on light geometric overlays still clears the 4.5:1 contrast for the black headline (visual scan suggests yes).
- M_140 — the secondary CTA "CALCULATE NOW" is on-brief (master prompt called for it). Primary `BOOK A FREE DEMO NOW` still present at y:820. If conflict, demo pill wins.

## Layout audit
- `snapshot_layout(parentId:UmJXB, problemsOnly:true)` returned no problems.
