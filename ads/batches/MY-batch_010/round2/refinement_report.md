# MY-batch_010 — Family H Round 2 Refinement Report

## Cross-check vs `config/products.json`

| UI feature shown | Real product? | Verdict |
|---|---|---|
| End-of-day sales total | ✓ "Real-time sales reports and analytics" USP | OK |
| Cash reconciliation badge | Not explicitly listed | Plausible POS function — keep, flag |
| Close-out time / 12-min timer | Not explicitly listed | Slightly inventive — but framed as outcome metric not a feature toggle. Keep. |
| Order taking + item-level pricing | ✓ Core POS | OK |
| Inventory / stock count | ✓ "Losing track of inventory and stock levels" | OK |
| Sales line chart over time | ✓ Real-time reports | OK |
| Today's sales push notification | Plausible mobile companion feature | Keep |
| Margin per item (sticky note in H_082) | Inventory + reports combine to this | OK |

**No fake AI assistant, no fake third-party integrations, no fake Grab/FoodPanda badges. UI honest.**

## Pricing anchor reconciliation
- Brief says `From RM3.40/day` (consistent with whole batch_002+ pipeline).
- `products.json` says `From RM3,960/year` and `anchor_format: "/year (always — never use /day or /month)"`.
- **Conflict.** Brief is the binding document for this batch — left RM3.40/day in copy.
- **Flagged for Zaid:** decide if pricing anchor format should align across config + briefs.

## Merchant-count anchor
- Brief: `17,000+ MY merchants`
- products.json: `20,000+` across SEA (MY+PH+TH combined)
- 17,000+ in MY alone is plausible but unverified — brief is binding.

## Refinements applied in R2
- iPad in H_076 resized to fit cleanly above CTA (was 800×560 → 760×520).
- H_084 chat bubbles repositioned y:170/300/430, headline at y:680 to prevent CTA overlap.
- CTA pills across all 9 frames given explicit `layout:"horizontal"` + `justifyContent:"center"` to ensure text centers correctly (initial render placed text below pill in some).
- Wordmark y:960 across all 9.

## Remaining FLAGGED items
- Screenshot tool returns blank for this y-offset range (40000+). Visual verification must happen in the Pencil app. Same bug as Family E.
- snapshot_layout reports several "fully clipped" warnings for CTA text inside pill frames; manual coordinate math shows text is within frame bounds. Likely tool false-positive related to rotated parents elsewhere in the doc tree.
- Caveat font (sticky note in H_082) — if not loaded, falls back. Acceptable but worth verifying in app.

## Final READY count: 9 / 9
- ngtcm H_076, v6CoL H_077, jykCA H_078, mbhdR H_079, AZMXL H_080, iYkbe H_081, mhkph H_082, hoMxj H_083, oRoNq H_084
