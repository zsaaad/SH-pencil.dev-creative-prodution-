# PH Heroes Day flight — creative review

Six 1:1 statics. Assets 1–4 Heroes Day, 5–6 Independence Day. Two messages: ₱21,000 off (1/2/6) and price-forward ₱63/day or ₱1,800/month (3/4/5).
Reviewed 2026-08-13 over three rounds, verified against the repo. Assets are **not in this repo** — no batch dir, no `ad-copy.md`, no manifest, and files are 599–656px non-square against the 1080×1080 standard.

---

## THE CALL

**Ship 2. Kill 4.**

| | Asset | Role |
|---|---|---|
| Control | **5**, re-headlined to Heroes Day | ₱63/day + F&B scene (real food, named venue) |
| Variant | **4**, price changed to ₱63/day | ₱63/day + café interior (brick, chairs) |
| Rotation filler only | 3 | Same price, near-white product gradient — not a clean cell |
| Kill | **1, 2, 6** | ₱21,000 hook, wrong unit, wrong noun |

Single variable: **background context**. Price held constant at ₱63/day across both cells. Read-out per `config/campaigns.json → experiment_settings`: 1,000 impressions minimum, 7-day duration, kill at CPL >RM150 or SQL% <20.6%.

---

## STOP-SHIP — resolve before touching any file

**The flight advertises a price the repo cannot confirm.** `config/products.json` lists PH at **From ₱49,900/year**, with `anchor_format: "/year (always — never use /day or /month in copy)"`. The ads say ₱63/day (= ₱22,995/yr per the repo's own math in `PH-batch_001/production_prompt.md`) and ₱1,800/month. That's a 54% gap against list. These leads go to an in-person BC visit — if the LP or the BC quotes ₱49,900, CPL looks great while lead→Won craters and the creative gets credited as a winner for two weeks. PH targets: CPL RM100, CPWon RM1,376.

**If the honoured PH price is ₱49,900/year, kill all six.** Nothing below matters until someone confirms which number is real.

Related: **₱1,800/month appears nowhere in the repo.** ₱63/day × 30 = ₱1,890; × 365 = ₱22,995. Asset 4's price is invented. Change it to ₱63/day (which also cleans the test).

---

## WHY 1, 2 AND 6 DIE

**The unit and the noun are wrong, and that's fatal on its own.** `config/products.json → active_offers[0]` is `"type": "hardware_discount"` — PH "Up to PHP 20,000 off on hardware." The repo's own approved copy says it correctly: *"₱21,000 off StoreHub **hardware**. While supplies last."* The creative says "Get ₱21,000 **/month** Off **On Your POS**." A capped one-time hardware discount rendered as a recurring software discount. ₱21,000/month off a ₱1,800/month product is impossible on its face — and the tell is that 1/2/6 reuse the *identical* stacked "PHP / month" lockup from 3/4, where it correctly labels a price. A price label pasted onto a discount.

**The hook is CPL-expensive for cold traffic.** `data/knowledge_base.json`, high confidence: *"High absolute price as primary hook (₱21,000) creates CPL spike — 4.6x benchmark — even if SQL% is high."* Evidence: `PH Q4: Independenceday_P21000 CPL RM456` against a RM100 target.

**But be precise about what that means.** `PH-batch_001/theme-analysis.md` lists `Independenceday_P21000_promo` under **high performers** — SQL% 43.1%, Won% 5.88%, *"the highest-quality leads in the dataset."* ₱21,000 isn't a bad offer; it's an expensive-CPL, high-quality hook. It belongs in **warm/retargeting**, correctly worded as a hardware discount. It does not belong in an 11-day cold CPL-targeted flight. Kill for this flight, not forever.

**Asset 2 is a duplicate of 1** (same layout, different crop), so it adds nothing regardless.

---

## WHY 5 IS THE CONTROL, NOT 3

KB, high confidence: *"F&B vertical-specific imagery lifts SQL% — PH Allinonepos_Fnb 45% vs generic 20–25%"* and *"Generic product-only white background ads have near-zero conversion."*

Asset 3 has the proven message on a near-white product gradient — closer to the documented failure mode than its clean thumbnail suggests. Asset 5 has the proven message **and** the F&B context. Asset 4 has a genuine café interior and is the better fit for both the KB's moody-photography pattern and the CLAUDE.md aspirational-venue rule. Correct order: **5 > 4 > 3**.

Blockers on the survivors:
- **Assets 5/6 clip real content.** Verified at 4× zoom: the orange total bar cuts mid-figure ("PHP 195."), and Sub-Total, Discount and Tax *values* run entirely off-canvas.
- **Independence Day is expired** (June 12). Asset 5 needs the Heroes Day headline.
- **"POS Software for ₱63/day" over a dual-screen terminal + customer display + tablet.** Merchants will read ₱63/day as buying the counter. Delete "Software" — the KB says price anchors work *specifically* when paired with a hardware visual, so the image is right and the word is wrong.
- **No on-canvas CTA, no end date.** `campaigns.json` sets the universal CTA as "Book a free demo now" / "Mag-book ng libreng demo". Heroes Day 2026 is **Monday 31 August** (RA 9492, last Monday).
- **No primary text exists** for this flight anywhere in the repo. Pull the pattern from `PH-batch_001/ad-copy.md`.

---

## TIMELINE IS WRONG

Live Aug 20 + hard stop Aug 31 = **11 days of delivery**, not the 2.5 weeks it looks like. Minus learning phase that's 4–6 days of stable read on a 2-cell test. **Launch Aug 17**, or drop the hard end date and run past the holiday.

Delivery concentration: six near-identical statics in one adset means Meta picks a winner on early CTR inside 48 hours and the rest never accumulate readable data. Split across adsets at RM100 CPL, every cell sits under the 50-conversion learning threshold for the whole window. **Two cells, one adset, inside the existing PH campaign. Do not build a new campaign for an 11-day promo.**

Volume is also thinner than it looks: the six are really three base compositions (1≈2, 3≈4, 5≈6). After the kill you have ~2 distinct looks. That's a fatigue risk over 11+ days — asset 3 is worth keeping in rotation as filler, explicitly not read as a test cell.

---

## HEROES DAY HAS A LOSING PH RECORD

`theme-analysis.md`, poor performers: **`NationalHeroesDay` — CPL RM100, CPSQL RM1,197** vs period avg CPSQL RM425. `agents/ad-copy-generator.md:170` codifies it: *"Holiday hooks WITHOUT a hard offer attached (PH National Heroes Day with no promo flopped)."*

These assets do carry an offer, so it isn't disqualifying — the KB rule is *"Seasonal hooks boost performance when paired with price — not effective alone."* But there is **no Heroes Day + price data point**. Treat the occasion as unproven, not proven. Also worth noting: `Independenceday_P63_promo` returned CPL RM48 — the strongest PH seasonal number in the repo — so the price-forward seasonal pattern itself is sound.

**The bigger calendar miss: Merdeka is also 31 August.** MY carries 56% of budget (RM362k vs PH RM209k) and `EN_Merdeka Promo` is the repo's best-documented seasonal winner (CPWon RM885, best MY Q3). This set has zero MY assets. The higher-EV occasion on the same date is unstaffed. TH has no August occasion and only "Up to 55% off" with no daily anchor — nothing to port.

---

## FREE WINS

- **Orange "BIR-Accredited" corner ribbon** on both survivors. Existing pattern in `knowledge_base.json → visual_design_patterns`. BIR accreditation is plausibly the strongest PH purchase driver — a non-accredited POS can't issue valid official receipts — and this flight buried it as an illegible watermark on the three assets being killed.
- **"3,350+ local businesses"** (`products.json → pricing_by_market.PH.social_proof_count`). Stronger local proof than "20,000+ across SEA". Appears on none of the six.
- **"Mas mura pa sa isang milk tea"** in primary text, not the image. Anchors ₱63 to something merchants already price. Competitor-free, clears compliance.
- **"Promo" not "Offer"** — "Offer" isn't a PH retail word. "Araw ng mga Bayani" reads native where "Heroes Day" reads translated.
- **₱ prefixed, not "PHP" trailing.** Trailing the unit is also what let "21,000 PHP/month" glue the unit to the wrong noun.
- **"Aunty Jane" → "Tita Jane."** Real PH register tell; "Aunty" is MY/SG.
- **9:16 for the control only** (bottom safe zone is 400px per `campaigns.json`, and the logo sits bottom-left at 92–96% of canvas height on 3/4/5/6). Exclude Stories/Reels for the variant rather than building two natives in 11 days.

---

## THE BIR SEAL — narrower than it first looked

Verified by pixel zoom: the badge on 1/2 is the **official Bureau of Internal Revenue Philippines agency seal**, not an accreditation mark, and it physically occludes the first line item's price. But the risk is smaller than it appears: StoreHub PH already markets BIR accreditation publicly, PH POS vendors displaying BIR marks is normal, and the KB itself documents *"Circular seal — BIR Accredited"* as an in-use PH badge style. **Surviving note: use a text/ribbon accreditation badge, not the agency seal.** Dies with the assets anyway.

---

## LOOP HYGIENE

`data/cycle_state.json` reads `current_iteration: 1`, `markets: ["MY"]`, `last_checked: 2026-03-24`. `data/iterations/PH-1/` exists but is **not registered**. Register this flight before launch or `scripts/import_results.py` has nowhere to land results and the loop learns nothing from the spend.

**Reconcile the repo's conflicting PH numbers** — ₱49,900/yr vs ₱22,995/yr vs ₱1,890/mo vs ₱63/day, KB says "₱63/month" where everything else says /day, offer is ₱20,000 in config and ₱21,000 in batch copy, and `anchor_format` forbids /day while the KB says ₱63/day is the top PH performer over two quarters. Every future batch inherits this.

---

## CLAIMS TESTED AND DROPPED

Recorded so they don't get re-raised:

- **"Asset 6's headline is illegible."** Wrong — white type with a heavy navy outline, reads clearly at 130px. Only the yellow "Offer" is low-contrast.
- **"Nothing reads at thumbnail on 1/2/6."** Refuted by the same test; "21,000" reads clearly.
- **"Text density → higher CPM."** Meta retired the 20% text rule in 2021. No delivery tax.
- **"The KKK banner is a Meta-classifier risk."** Speculative, no evidentiary base. ~0.2% of canvas, unambiguously Katipunan in context.
- **"Asset 1's panel occludes the POS."** Wrong element — the BIR seal does.
- **"Asset 1's headline touches the frame / clips at 4:5."** ~3.7% gutter; Meta renders 1:1 natively in feed.
- **"Basket prices are absurd in pesos."** The ₱729.90 line carries "Gift Wrap / Card" modifiers — a gift item. Assets 5/6 show ₱160 + ₱35 = ₱195, textbook PH.
- **"Wrong VAT beside a tax emblem"** as a compliance event. ~5px tall, unreadable at feed size; and PH requires VAT-*inclusive* display, so the proposed correction was wrong too. Craft nit.
- **"The flight can't learn anything / needs 3–4 angles."** Execution testing at a fixed proven angle is the correct stage. The real constraint is delivery concentration.
- **"Menu grid is Malaysian."** Real tells exist ("Double Chipsmore", "Tongkat Ali") but at ~7px they're invisible at feed size. Fix if the file's open; don't schedule it.
- **Standardise type / add brand orange / comma-format 1,800.** Brand housekeeping in a performance costume.

Compliance (CLAUDE.md hard rules): **clean.** No competitor names, no "till", venue tier acceptable.

---

## SHIP ORDER

1. **Verify the honoured PH price and the LP.** Stop-ship. If ₱49,900/yr, kill all six.
2. **Kill 1, 2, 6.** Free.
3. **Asset 5:** headline → Heroes Day; fix right-edge clip and bottom crop. This is the control.
4. **Asset 4:** price → ₱63/day so background is the only variable.
5. **Delete "Software" from 3, 4, 5.**
6. **Write the primary text** — pattern from `PH-batch_001/ad-copy.md`.
7. **Add CTA + "Ends 31 Aug"** to both survivors.
8. **BIR-Accredited orange ribbon + "3,350+ local businesses."**
9. **Structure:** 2 cells, 1 adset, existing PH campaign. **Live Aug 17.**
10. **Register the flight** in `cycle_state.json` + `data/iterations/`.
11. **9:16 for the control only.**
12. **Raise the MY Merdeka gap** — same date, 56% of budget, best seasonal evidence, zero assets.
13. **Queue a Sept 1 "ber months" headline re-skin** on the same files so you don't go dark Aug 31 → 9.9.

**Not worth the hours:** any repair on 1/2/6 for this flight; the asset-3/asset-5 composite (hold for Sept 1 — asset 5's headline swap gets 85% of it for 5% of the work); menu-grid localisation; 9:16 for non-control; angle diversification (next iteration — the KB already names the better brief: **PH retail has no dedicated ad at all**, and stop-motion unboxing is the highest-volume PH format at CPL RM48 on RM37k spend, with zero video in this flight).
