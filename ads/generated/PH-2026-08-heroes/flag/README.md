# PH National Heroes Day flight — flag palette

## STATUS: prompts are current, renders are STALE

The four PNGs in this folder were generated from an EARLIER revision of the prompts.
They do not match `prompts/f1–f4.txt` as they now stand. Known divergences:

| | Render shows | Prompt now specifies |
|---|---|---|
| Price line | "63 pesos a day" | `From ₱22,995/year` |
| Offer | "21,000 pesos off hardware" | `Up to ₱21,000 off hardware` |
| f4 headline | "Three channels. One screen." | `From chaos to control.` |
| Wordmark | STOREHUB all-caps | StoreHub, mixed case |
| Peso symbol | spelled "pesos" in body copy | literal ₱ glyph |

Regenerate before treating any render as a candidate.

## Governance
- Standard: `~/Code/cranium/reference/storehub/storehub-creative-master.md` (wins on conflict)
- Flight system + unresolved conflicts: `prompts/_shared_system.md`
- Palette exception: `~/Code/cranium/decisions/2026-08-13-ph-heroes-flag-palette-override.md`

## Before spend — open items
1. PH price is contradictory: master says ₱22,995/year, `config/products.json` says ₱49,900/year.
2. Offer number is contradictory: config says "Up to ₱20,000", shipped copy used ₱21,000.
3. Master §8 Lateral Protocol has NOT been run on these four concepts. By §8 Stage C.4 they
   cluster as one structure (merchant/product shown → price CTA), where max 2 may ship.
   Nothing is registered in `reference/lateral/shipped-concepts.jsonl`.
4. No primary text / headline copy written for any of the four.
5. Type should be composited in Pencil per master §7 rule 4 — each prompt has a PLATE VARIANT.
