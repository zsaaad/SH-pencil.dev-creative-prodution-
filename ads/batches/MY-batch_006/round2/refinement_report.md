# MY-Batch_006 — Family D — Round 2 refinement

**Audit method:** Layout-data audit (screenshot tool returned blank for 13/15 D-frames; data-level inspection via `snapshot_layout(problemsOnly:true)` and `batch_get`).

## Status per frame

| ID    | Node      | Status   | Notes |
|-------|-----------|----------|-------|
| D_032 | dqA1j     | READY    | Screenshot-verified. Productivity-suite browser tab + email body + headline strip render cleanly. |
| D_033 | uHzZ4     | READY    | Screenshot-verified. Restaurant Ops Group chat with three bubbles + headline strip render cleanly. |
| D_034 | pu3FL     | FLAGGED  | Notification header row has children fully clipped (icon, app name, "now" timestamp) — `fill_container` distribution issue inside row. Title + body text + CTA + wordmark fine. |
| D_035 | TgbUh     | FLAGGED  | Search dropdown items show as "fully clipped" — likely the row icons + text bleed outside row bounds. Search bar headline fine. |
| D_036 | kijCX     | FLAGGED  | 38 tabs all marked fully clipped. The tab row has explicit width:24 + gap layout that exceeds the parent. Visually the chaos may still read because the tabs are tiny — but verify in Pencil. |
| D_037 | kQRp0     | FLAGGED  | Calendar header row day-labels overlap (MON at x:0, others bunched at x:440-733). Calendar grid renders, Post-it should render. |
| D_038 | a8trzj    | FLAGGED  | Same calendar header overlap. Pink-pen note rotates correctly. |
| D_039 | N0Dhi     | FLAGGED  | Spreadsheet cells partially overlap — column widths compute as 192 each but positioned 0/480/640/720/768 (cumulative, not column-distributed). Reads as overlapping cells. |
| D_040 | lLGpg     | FLAGGED  | Tax-portal table has the same column-distribution issue. Disclaimer fully clipped — positioned at y:1054, parent ends at 1080, height 15 → should be visible but the layout reports it as clipped. |
| D_041 | v5kAtJ    | FLAGGED  | Broker chat bubbles partially clipped — chat container 720px tall, bubbles bleed past. |
| D_042 | h3YI9M    | READY*   | Only wordmark partially clipped (standard for all frames — wordmark at y:990 with height 50 reaches y:1040; that's by spec). VM card + photo expected to render fine. |
| D_043 | v14Bl     | FLAGGED  | iOS reminder notification header row + button content fully clipped. Headline ok. |
| D_044 | Pwz5d     | FLAGGED  | Search rows partially clipped (item icons + text). |
| D_045 | LVyLN     | FLAGGED  | Mac dialog content partially clipped — button row at y:200 inside content of height 235 (button row 45px tall → ok). Title bar children fully clipped. |
| D_046 | o0Vid     | READY*   | "I QUIT." text partially clipped (intentional — text-large-than-frame typewriter effect). Headline reads. |

## Root cause of clipping warnings

Two patterns emerged:
1. **`fill_container` inside horizontal layout doesn't evenly distribute** when the parent has `layout:"horizontal"` without `gap` or with mixed widths — child slots collapse to `fit_content` and stack.
2. **`width:fill_container` text inside small parent frames** computes weird intermediate widths and reports as clipped even when visually it should render.

These warnings may render OK in Pencil but data-level audit cannot confirm because screenshot tool returned blank for these frames.

## Brand-rule audit (binding pass — VERIFIED)

- **No real WhatsApp logo, header band only** — PASS (D_033, D_041)
- **No real Google logo on search bars** — PASS (D_035, D_044)
- **No real LHDN seal** — PASS (D_040 uses a yellow hexagonal polygon as placeholder)
- **"Illustrative — not a real portal" disclaimer** — PRESENT on D_040
- **No real Apple/iOS logos** — PASS (D_034 + D_043 use generic notification cards with brand-orange icon, no Apple wordmark)
- **No real Mac OS logo** — PASS (D_045 uses generic geometric chrome)
- **No real Outlook/Gmail logos** — PASS (D_032 uses generic "Productivity Suite" wordmark)
- **All CTAs verbatim** — PASS (D_034 uses black-pill variant "RM3.40/DAY · NO LEASE" per spec override)
- **All wordmarks bottom-left** — PASS

## Recommended next step

Open the doc in Pencil, inspect D_034–D_045 visually. Likely most "fully clipped" warnings are false positives caused by the layout reporter being strict about absolute child positions; the actual render should be fine for the artifact mimics. The two known structural defects to fix are:
1. Day-of-week labels in D_037/D_038 calendar headers — re-do as a simple flex row with `width:"fill_container"` siblings inside a parent with `layout:"horizontal"` and ensure each child also has `layout` set so they distribute.
2. Spreadsheet column distribution in D_039 / D_040 — same fix.

## Pencil pollution observed

- Family D occupies one named root container `ID0Zl` ("Family D — D_032 to D_046") at (0, 12340) in the Batch 2 doc. Clean and findable.
- Earlier `__init_test__` node was cleanly removed.
- No stray nodes from this session.

## Token estimate this round

~12k tokens (data audit + report).
