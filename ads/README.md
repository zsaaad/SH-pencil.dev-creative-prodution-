# `/ads` — directory layout

Active creative production lives at the root. Per-batch deliverables live under `batches/`. Briefs are in `briefs/`. Anything historical or orphaned is in `_archive/`.

## Active files (root)

| Path | What |
|---|---|
| `SH Pencil ads batch 2.pen` | Current MY iteration. Open in Pencil app. Holds 36 frames (12 concepts × 3 ratios). |
| `SH PH ads batch 1.pen` | *(to be created)* PH market — 96 frames per `batches/PH-batch_001/production_prompt.md`. |
| `Outro Screens.pen` | Reusable outro/end-frame templates. |
| `images/` | All `G()`-generated AI images. Flat naming `generated-{timestamp}.png`. **Do not move** — `.pen` files reference these via `./images/...` paths and renaming will break image fills. |
| `exports/` | Reserved for final PNG drops handed to media buyers. Currently empty. |

## `briefs/`

Standalone creative briefs that are not tied to a specific batch.

| File | What |
|---|---|
| `storehub-new-biz-my-en-brief.md` | Original MY new-business positioning brief (March 2026). Reference doc, not an active production target. |

## `batches/`

One sub-directory per launched batch. Each holds the production prompt, exported PNGs, ad-copy markdown, and analysis files for that batch.

| Path | What |
|---|---|
| `batches/batch_001/` | MY Batch 1 — 8 themes, 20 creatives. Mar–Apr 2026. **Note:** historical naming convention (no market prefix). |
| `batches/batch_002/` | MY Batch 2 — 12 concepts × 3 ratios. Apr 2026. |
| `batches/PH-batch_001/` | PH Batch 1 — 32 concepts × 3 ratios = 96 frames. New naming: `{MARKET}-batch_{NN}/`. |

Going forward, every new batch dir uses the `{MARKET}-batch_{NN}` form (e.g. `MY-batch_003`, `TH-batch_001`). The two unprefixed `batch_00X` dirs stay as-is — they're referenced from `data/iterations/*/creative_manifest.json` and `data/cycle_state.json`, and renaming would break those.

Each batch dir typically contains:
- `*production_prompt.md` — the brief the creative agent executes
- `analysis.md` — post-production audit
- `ad-copy.md` — Meta upload-ready Primary Text / Headline / Description per concept
- `*.png` — exported frame renders
- `image-todo.md` *(when applicable)* — outstanding `G()` AI prompts the next session must run

## `_archive/`

Anything superseded, orphaned, or one-off. Nothing here should be referenced by active workflows.

| Path | What |
|---|---|
| `_archive/Legacy Ads/` | 66 PNGs from pre-pipeline manual ad work (Mar 2026 and earlier). Reference only. |
| `_archive/MY Creative testing Batch 2.pen` | 259-byte orphan stub. Superseded by `SH Pencil ads batch 2.pen`. |
| `_archive/MY_Creative Testing_Batch 2.pen/` | Earlier directory-form variant of the Batch 2 .pen. Same content as the active file but stale. |
| `_archive/fast ads SH.pen` | One-off experiment from April 21. Not part of any batch. |
| `_archive/storehub-new-biz-my-en.pen` | Original MY positioning .pen (March). Superseded by Batch 1 / 2 outputs. |
| `_archive/batches/compcontrast_iter2_20260413/` | Standalone competitive-contrast test from April 13. Predates the formal batch numbering. |

## Conventions

- **`.pen` filenames at root** use spaces (e.g. `SH PH ads batch 1.pen`). Do not change once Pencil app has them in its recent-files list.
- **Batch dirs** use snake_case + market prefix (`PH-batch_001`).
- **Image fills inside `.pen` files** are relative paths (`./images/c010-pasar-malam-1x1.png`). Keep `images/` at the root of `/ads`.
- **Production prompts** are absolute-path-referenced (`/Users/zaidsaad/Desktop/Code/Pencil.dev/...`) so they survive any cosmetic rearrangement of the surrounding layout.
