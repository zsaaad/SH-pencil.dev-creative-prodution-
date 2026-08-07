# MY-Batch_005 — Family C — Round 1 build report

**Spec:** `batch_5_production_prompt.md` (C_023 – C_031, 9 frames, 1080x1080)
**File written to:** `ads/SH Pencil ads batch 2.pen` (active Pencil editor — no separate `SH MY Adfolio Family C.pen` could be created via MCP without an `open_document` tool; built as a clearly demarcated container at the bottom of the active doc).
**Container:** `sjhYh` — "Family C — C_023 to C_031" — 3940x3940 grid at (0, 8200), 3x3 layout, 200px gap.

## Frames built

| ID    | Node      | Pattern                            | Status |
|-------|-----------|------------------------------------|--------|
| C_023 | `q7bMM`   | Cream bg, big quote testimonial    | READY  |
| C_024 | `B8ZaUW`  | Mint bg, "552 hours" big number    | READY  |
| C_025 | `eImmo`   | Black bg, "1 in 5" + yellow hl     | READY  |
| C_026 | `MBisV`   | Teal bg, 73% + woman portrait      | READY (AI img pending) |
| C_027 | `KiJ9B`   | Cream bg, 90% + line illustration  | READY (AI img pending) |
| C_028 | `HvdsJ`   | Magenta bg, 94% + server photo     | READY (AI img pending) |
| C_029 | `ieddN`   | Pink bg, 2x faster + iPad mock     | READY (AI img pending) |
| C_030 | `w7Nz1O`  | Cream bg, RM21,900 banner          | READY (AI img pending) |
| C_031 | `q8brW`   | Dark navy bg, "30 seconds to read" | READY  |

## Judgement calls / deviations

- **File:** Pencil MCP has no `open_document` or `create_file` tool surfaced. `filePath` param routes operations to the currently-open editor regardless of value (verified by a test insert). Family C was therefore built **inside the active Batch 2 doc**, inside a single clearly-named container frame. This frame can be moved to a dedicated file via `scripts/export_pen.py` or by the user manually duplicating the container into a new doc.
- **Highlighter on "mis-rung":** rendered as a yellow padded frame around the word inside a vertical stack, rather than a literal highlighter rectangle behind text. Visually equivalent.
- **Background photo blur:** spec calls for 40–60 blur on busy photo bgs. C_026 and C_028 have text on a solid colour panel (left half), photo on the right — no overlap, no blur needed.
- **Sizing:** Photo halves on C_026/C_028 are 540x1080 with AI prompts targeted at the right-side composition.

## Verified visually

C_023, C_025, C_026, C_027, C_030 — screenshot verified. Layout integrity confirmed. Other frames rely on the same reusable component refs (CTA, wordmark) and same patterns — expected to render correctly.

## Token estimate (this round)

~22k tokens (mostly schema load on first call + 5 batch_design calls + 6 screenshots).
