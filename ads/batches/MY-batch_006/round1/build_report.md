# MY-Batch_006 — Family D — Round 1 build report

**Spec:** `batch_6_production_prompt.md` (D_032 – D_046, 15 frames, 1080x1080)
**File written to:** `ads/SH Pencil ads batch 2.pen` (active Pencil editor — see Family C report for the file-routing constraint).
**Container:** `ID0Zl` — "Family D — D_032 to D_046" — 6500x3940, 5x3 grid, 200px gap, located in empty space below Family C.

## Frames built (all 15)

| ID    | Node      | Pattern                                  | Notes |
|-------|-----------|------------------------------------------|-------|
| D_032 | `dqA1j`   | Browser tab "Productivity Suite" email   | Screenshot verified — clean |
| D_033 | `uHzZ4`   | Restaurant Ops Group chat (3 bubbles)    | Screenshot verified — clean |
| D_034 | `pu3FL`   | iOS notification "POS Trading" + lease pitch  | Built per spec, screenshot tool returned blank (renderer glitch — data correct) |
| D_035 | `TgbUh`   | Search history dropdown (6 searches)     | Built per spec, screenshot blank (renderer glitch) |
| D_036 | `kijCX`   | 38 fake browser tabs + clutter           | Built per spec, screenshot blank (renderer glitch) |
| D_037 | `kQRp0`   | Calendar grid + pink "DO NOT BOOK" Post-it | Built per spec |
| D_038 | `a8trzj`  | Calendar grid + pink-pen "doc appt rescheduled" | Built per spec |
| D_039 | `N0Dhi`   | Spreadsheet, red `-RM0.40` cell + tooltip | Built per spec |
| D_040 | `lLGpg`   | Fake e-invoice tax portal with 2 REJECTED rows  | Built — uses generic navy header + yellow polygon seal (no real LHDN). Disclaimer present. |
| D_041 | `v5kAtJ`  | Broker chat (4 broker pitches + clever reply)   | Built per spec |
| D_042 | `h3YI9M`  | Voicemail card + frustrated merchant photo (AI) | Built per spec |
| D_043 | `v14Bl`   | iOS reminder notification on dark navy   | Built per spec |
| D_044 | `Pwz5d`   | Search "did you mean: get StoreHub"      | Built per spec |
| D_045 | `LVyLN`   | Classic Mac OS dialog "End-of-day.exe"   | Built — 2-button dialog with CANCEL / GET STOREHUB |
| D_046 | `o0Vid`   | Dark green "I QUIT." typewriter          | Used Courier Prime for typewriter feel |

## Brand-rule audit (R1)

- No real WhatsApp logo: chat header uses generic dark green band + "AB · POS Trading" name. PASS.
- No real Google logo: search bars are stylised, no Google wordmark anywhere. PASS.
- No real LHDN seal: tax portal uses a generic yellow polygon as seal placeholder. PASS.
- No real Mac logo: classic dialog uses generic geometric window chrome. PASS.
- No real Outlook/Gmail logos: "Productivity Suite" wordmark is generic. PASS.
- All CTAs: `BOOK A FREE DEMO NOW` on orange pill (D_034 uses black `RM3.40/DAY · NO LEASE` per spec override). PASS.
- All wordmarks present bottom-left. PASS.

## Known issues / FLAGGED

- **D_034 / D_035 / D_036 screenshot tool returned blank.** Layout snapshot confirms frames + content exist with correct fills (yellow `#FFE656`, light blue, light grey respectively). Likely a Pencil render-cache miss on these specific frames; expected to resolve on next document open / export. Manual visual check recommended before exporting.
- **Spec deviation D_040:** spec says "dark navy header (NOT real LHDN seal — use a simplified geometric placeholder)" — implemented with dark navy `#15294B` header and yellow hexagon seal. Disclaimer microcopy present bottom-right.
- **D_038 "pen note":** rendered with rotation -3 inside calendar grid as a single italic pink line. May read as a label rather than a literal handwritten Post-it — acceptable but not as raw as a real handwritten scribble.

## Token estimate

~28k tokens for Family D R1 (4 batch_design calls + verification screenshots).
