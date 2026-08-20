# MY Merdeka Day flight — 31 August 2026

Sibling of the PH Heroes Day set (`../PH-2026-08-heroes/flag/`). **Same date, different market.**
`m1.txt` is the MY counterpart of PH `f5.txt` — same 16:9 feature-showcase layout, market-swapped.

## Set inventory
| File | Format | Type | Vertical | Feature group (master §3) | Offer emphasis |
|---|---|---|---|---|---|
| m1 | 16:9 | feature showcase, 5 floating chips | F&B café | Run your store smoothly | 55% off hardware |
| m2 | 1:1 | promo, human hero at dawn | F&B café | — | RM7.60/day hero |
| m3 | 1:1 | promo, flat product poster | — | — | 55% OFF hero + 4 months free |
| m4 | 1:1 | feature + promo | **Retail boutique** | Reach more customers / sell online | RM7.60/day + 55% |
| m5 | **9:16** | feature + promo, peak service | F&B bistro | Run your store smoothly | RM7.60/day + 55% |
| m6 | **9:16** | feature + promo, salon reception | **Service** (hair salon) | Customer Loyalty made easy | RM7.60/day + 55% |
| m7 | **9:16** | feature + promo, ops room | **Enterprise** (multi-outlet) | Run your store smoothly | RM7.60/day + 55% |
| m8 | **9:16** | feature + promo, checkout tap | Retail checkout | Seamless Checkouts & Payments | RM7.60/day + 55% |

Deliberate spread: two promo-led (m2, m3) and six feature-led (m1, m4, m5, m6, m7, m8); three formats;
all four supported verticals; all four §3 feature groups used exactly once or twice. m4 is the set's **Retail** entry —
`data/knowledge_base.json` flags Retail as critically undertested. m5 is the only 9:16 in either
the MY or PH set, and Meta delivery is heavily Reels-weighted.

All four 9:16s (m5–m8) are built to the §4 Reels spec — top 250 / bottom 500 dead zones stated in
the prompt, headline y>=280, CTA pill y<=1400. Designing to Reels auto-passes Stories.

§2 "From X → Y" formulas: Retail "From clutter to clarity." (m4), F&B "From chaos to control." (m5),
Service "From friction to flow." (m6), Enterprise "From gaps to structure." (m7). m8 uses a fresh pair,
"From queue to clear." — §2 states the formula is free and not vertical-locked.

**m7 Enterprise carries two §2 obligations:** CTA is "CONTACT US", never the demo-booking CTA (the
linter WARNs file-level on this), and Enterprise uses an accent card. §2 specifies an ORANGE accent
card, which the palette override makes unavailable — m7 renders it in flag yellow. That substitution
is a knock-on of the palette exception, not an independent call. Flag if the orange card is load-bearing.

## Why this exists
Merdeka Day and PH National Heroes Day both fall on **Monday 31 August 2026**. MY carries the
larger budget (`config/campaigns.json`: MY RM362,489 = 56.4% vs PH RM209,143 = 32.5%) and
`EN_Merdeka Promo` is the best-documented seasonal winner in the knowledge base
(CPWon RM885, best MY Q3). The PH set had no MY counterpart — this closes that gap.

## Market deltas vs the PH prompt
| | PH (f5) | MY (m1) |
|---|---|---|
| Occasion | Araw ng mga Bayani | Selamat Hari Merdeka · 31 Ogos |
| Palette | blue #0038A8 · red #CE1126 · gold #FCD116 | red #CC0001 · blue #010066 · yellow #FFCC00 |
| Motif | eight-ray sun + three stars | crescent + fourteen-point star |
| National flower prop | sampaguita garland | bunga raya (red hibiscus) |
| Extra prop | — | folded songket with gold thread |
| Dish on screen | Filipino rice plate | nasi lemak |
| Offer | Up to ₱21,000 off hardware | Up to 55% off hardware + 4 months free |
| Price line | From ₱63/day (₱22,995/year) | From RM7.60/day |
| Compliance badge | BIR Accredited | e-Invoicing Compliant |

## Pricing notes
- **RM7.60/day is canonical** (master §1) and the linter has a `pricing-my-number` rule that
  ERRORs on any other MY figure — stricter than PH, which only checks the unit.
- **Do not pair it with an annual line.** RM7.60 × 365 = RM2,774, which does NOT reconcile with
  `config/products.json` "From RM3,960/year". Unlike PH (₱63 × 365 = ₱22,995 exactly), the MY
  daily and annual figures are not the same price. Shipping both would invite the arithmetic.
- Offer per `config/products.json` active_offers MY: "55% off on POS hardware + free months
  (RM996 savings / buy 1 year get 4 months free)".

## Open items before spend
1. **Palette scope.** The flag-palette override was signed off for the PH Heroes Day flight only
   and explicitly marked "do not propagate". This MY extension follows the same logic but has
   NOT been separately approved. Confirm with Zaid.
2. Master §8 Lateral Protocol not run; nothing registered in `shipped-concepts.jsonl`.
3. No primary text / headline copy written.
4. Type should be composited in Pencil per master §7 rule 4 — the prompt carries a PLATE VARIANT.
