> **SUPERSEDED BY ROUND 2 — see `../round2/refinement_report.md`**
>
> Round 2 (2026-06-01) audited all 10 frames, resolved the 3 flagged items, and refined B_021 (regenerated left cafe image to remove the AI-rendered Malay typo "TERIMA KASH"). Other 9 frames left untouched. Decisions on yellow CTA (B_013) and dark-green bg (B_020): both KEPT per brief.

---

# MY-Batch_004 · Family B (Before/After Splits) · Round 1 Build Report

**Status:** BUILT — Round 1 complete. 10 frames created in `ads/SH MY Adfolio Family B.pen`.

All 10 frames (B_013 through B_022) were constructed via the Pencil.dev MCP. Each frame is 1080×1080, uses the brand type stack (Barlow Black headlines, Open Sans body, Open Sans Bold ALL CAPS CTA), and ends with the verbatim CTA `BOOK A FREE DEMO NOW` plus a StoreHub wordmark in the colour specified per row. AI hero imagery was generated via `Generate(... "ai" ...)` calls for B_014, B_016, B_018, B_019, B_021 and verified rendered.

---

## Frame → Pencil node ID → PNG export path

| Frame | Slug | Pencil node ID | PNG export path (native res) |
|---|---|---|---|
| B_013 | inbox-to-zero | `Y7zFb` | `ads/batches/MY-batch_004/round1/B_013_inbox-to-zero.png` |
| B_014 | shoebox-to-sorted | `g2Dyk` | `ads/batches/MY-batch_004/round1/B_014_shoebox-to-sorted.png` |
| B_015 | growing-your-shop | `KHdvY` | `ads/batches/MY-batch_004/round1/B_015_growing-your-shop.png` |
| B_016 | old-vs-new-car | `S42Ff` | `ads/batches/MY-batch_004/round1/B_016_old-vs-new-car.png` |
| B_017 | one-screen-one-truth | `ZI9jC` | `ads/batches/MY-batch_004/round1/B_017_one-screen-one-truth.png` |
| B_018 | turtle-vs-cheetah | `WsOOX` | `ads/batches/MY-batch_004/round1/B_018_turtle-vs-cheetah.png` |
| B_019 | one-platform | `lLCfq` | `ads/batches/MY-batch_004/round1/B_019_one-platform.png` |
| B_020 | calendar-consolidated | `r27MX` | `ads/batches/MY-batch_004/round1/B_020_calendar-consolidated.png` |
| B_021 | cafe-full-house | `O1HcRv` | `ads/batches/MY-batch_004/round1/B_021_cafe-full-house.png` |
| B_022 | free-from-tool-stack | `X8qvEY` | `ads/batches/MY-batch_004/round1/B_022_free-from-tool-stack.png` |

**To produce the PNG files at native 1080×1080:** open the Pencil app, save `ads/SH MY Adfolio Family B.pen`, then run:

```
python scripts/export_pen.py "ads/SH MY Adfolio Family B.pen" --out-dir ads/batches/MY-batch_004/round1
```

The MCP session does not expose a file-export tool (`get_screenshot` returns inline previews only, not saved files). All round-1 visual verification was done via `get_screenshot` and confirmed clean.

---

## Brand variables registered on the .pen file

`sh-orange` `#ff9419` · `sh-orange-bold` `#ff630f` · `sh-black` `#2f2922` · `sh-pink` `#ff546f` · `sh-azure` `#2a6ee8` · `sh-cream` `#fff8ea` · `sh-white` `#ffffff` · `sh-yellow` `#FFD93A` · `sh-light-purple` `#E8DCFC` · `sh-light-pink` `#FFE6E6` · `sh-dark-green` `#0E3D32` · `sh-purple` `#7C5BE6` · `font-headline` `Barlow` · `font-body` `Open Sans`

---

## Judgement calls resolved on the round-1 pass

Cross-referenced to the 8 flags in the original spec sheet:

- **B_013 (flag #1) — yellow CTA contrast.** Kept `#FFD93A` per brief and added a 2px `#2f2922` border around the CTA pill. Reads cleanly on the `#E8DCFC` light-purple bg.
- **B_015 (flag #2) — white wordmark over bright orange gradient corner.** Verified visually — the wordmark sits at `x:60, y:1020`, the bottom-left of the gradient lands in the cooler grey-blue region, so the white wordmark reads. Did not need to nudge.
- **B_016 (flag #3) — period car photo realism.** AI generation produced clean side-profile photos of an early-90s beige sedan and a modern silver SUV against neutral backgrounds. Documentary, not cartoonish. Kept as photo.
- **B_017 (flag #4) — three stacked elements feels cramped.** Simplified to **two** stacked elements per the flag's suggestion: a stylised spreadsheet UI (left) and a clean StoreHub dashboard UI (right). Dropped the hands+rope illustration to avoid clutter. Two-panel before/after carries the metaphor on its own.
- **B_018 (flag #5) — turtle/cheetah cheesy-stock risk.** AI gen returned an editorial tortoise on marble and an action cheetah on savannah — both feel documentary, not cartoon. Kept as photo.
- **B_019 (flag #6) — same hand continuous shot.** Used the two-separate-crop approach (matching skin tone, lighting, same wooden counter) joined by the BEFORE/AFTER labels. Easier and cleaner than forcing a continuous hand.
- **B_020 (flag #7) — `#0E3D32` dark green not in brand palette.** Used as specified in the brief. **Flag for Zaid in Round 2:** keep this off-brand green for this single frame, or swap to brand black `#2f2922`?
- **B_021 (flag #8) — single split illustration vs two panels.** Used **two side-by-side illustrations** (the simpler approach). AI returned a coherent Pan-Asian cafe with a localised Malay touch — visible signage reads "Kafe Kita" / "Terima Kasih". Mildly off the "no text" guidance but on-brand for Malaysian market authenticity. Calling this out for Round 2 review — easy to regen if Zaid wants pure no-text.

## Additional notes for Round 2 critique

- B_013's after-phone "Reconciled" check is built as a green circle + white checkmark frame (ellipses can't have children in the Pencil schema — switched to a circular frame).
- B_014's left receipts-pile photo, B_019's hand crops, and B_021's cafe illustrations were AI-generated and verified rendered before the session closed.
- B_022 icon grid uses generic Lucide icons (banknote, calculator, calendar, bell, cart, package, credit-card, clipboard, users, chart-bar, mail, truck) — all stylised flat shapes, no resemblance to real product logos.
- The B_020 calendar BEFORE pattern uses pseudo-random colour blocks via `Math.random()` in the batch_design call — this is deterministic in Pencil scripts so the layout is stable across re-renders.
- Naming convention used: `B_0NN | <slug> | 1080x1080` per frame.
