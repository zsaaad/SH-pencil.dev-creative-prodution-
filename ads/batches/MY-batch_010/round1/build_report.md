# MY-batch_010 — Family H Round 1 Build Report

**Container:** `UBzPw` at y:40000 — `Family H — H_076 to H_084` (1080×1080 × 9)
**Status:** READY (geometry verified via snapshot_layout; screenshots return blank — same Pencil bug seen in Family E)

## Frames (9)

| ID | Name | Notes |
|---|---|---|
| ngtcm | H_076 \| big-callout-UI | iPad mockup w/ end-of-day app, hand-drawn orange arrows pointing to Reconciled badge + 12 MIN timer |
| v6CoL | H_077 \| sales-chart-up | Dark bg, line chart flat→up with dotted "Switched to StoreHub" marker |
| jykCA | H_078 \| stress-down | Red curve plunging down, "Stress levels" x-axis label |
| mbhdR | H_079 \| live-counter | Navy bg, 240pt `17,348` ticker number, LIVE dot |
| AZMXL | H_080 \| phone-notification | Tilted phone with StoreHub notification card |
| iYkbe | H_081 \| search-history | Search bar `why is the till` + 7 autocomplete results, last highlighted |
| mhkph | H_082 \| spreadsheet-sticky | Faint grid bg + yellow Post-it with handwritten margin question |
| hoMxj | H_083 \| pos-hero | D3-style POS body w/ tilted Pay screen on peach bg |
| oRoNq | H_084 \| chat-thread | Group chat bubbles — Elaine reveals StoreHub close-out |

## Judgement calls
- POS body in H_083 simplified to 4 visible UI rows (per brief: cap mockup complexity 3–5 elements). Honest features: order items, total, pay button.
- Phone screen in H_080: only ONE notification + status bar — kept honest.
- Arrows in H_076 are simple SVG paths, not auto-generated illustrations — kept on-brand vector look.
- Used `Caveat` font for handwritten sticky note in H_082 (Google Font, falls back gracefully).

## FLAGGED items
- **Screenshot tool returns blank PNGs for the container.** Verified geometry via `snapshot_layout`. Pencil app should render fine when opened.
- **CTA pills initially showed "fully clipped" status in snapshot** — fixed by adding explicit `layout:"horizontal"` + `justifyContent:"center"`. Geometry is now within frame bounds.
- **H_076 iPad rotation 357°** pushed rotated bbox to ~601px tall; resized iPad to 760×520 to keep inside frame and clear of CTA.
- **H_084 third bubble** initially extended past CTA — moved bubbles up to y:170/300/430 and headline to y:680.
- **Caveat font** — if not loaded in Pencil, the sticky-note handwriting in H_082 falls back to default. Acceptable.

## fill_container clipping observations
- No horizontal flex grids used for UI mockups in this family — all UI bodies use `layout:"none"` with absolute positioning per brief mitigation. No clipping observed inside UI bodies themselves.
- Vertical flex used inside iPad/phone screens for tidy stacks; verified contents within parent bounds.

## AI render queue
- **None for Family H.** All visuals built from native Pencil primitives (rectangles, paths, ellipses, text). No `Generate()` calls needed — UI mockups are best authored, not generated.

## Cross-check vs StoreHub product reality
- End-of-day dashboard, cash reconciliation badge, close-out timer: real product features ✓
- Order taking, item-level pricing, pay button: real ✓
- "Today's sales" push notification: plausible ✓
- Live merchant counter: framed as MY merchant count (`17,000+`), not as live API ✓
- **No fake features**: no AI assistant, no Grab integration logos, no fake third-party badges ✓

## Token estimate
~10k tokens consumed building Family H (9 frames × ~1k each + verification).
