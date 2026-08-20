# PH National Heroes Day — shared creative system
Governed by `~/Code/cranium/reference/storehub/storehub-creative-master.md`. That doc wins on conflict.
Occasion: Araw ng mga Bayani, Monday 31 August 2026 (last Monday, RA 9492).

## Canonical lines (master §1 — do not drift)
  PH price HERO:    From ₱63/day        <- the main callout on every ad (Zaid, 2026-08-14)
  PH price SUPPORT: That's ₱22,995/year  <- master §1 canonical line, always present alongside
  BIR Accredited on every ad.
  The two are the same price: ₱63 x 365 = ₱22,995. Daily is the hook, annual is the canonical
  unit and the compliance-safe anchor. Never ship one without the other.
  Promo this flight: ₱21,000 off hardware  (config active_offers.type = hardware_discount)
  NEVER "/month" and NEVER "off your POS" — that error killed the previous PH flight.
  Social proof:     20,000+ merchants across Southeast Asia (canonical; PH-local alternative
                    "3,350+ local businesses" exists in products.json but is NOT canonical)
  Logo spelling:    StoreHub — one word, mid-cap H. Reject all other casings/spacings. lint-allow

## Vertical + formula (master §2)
  F&B only in this set: cafés, bistros, full-service restaurants. All are supported verticals.
  "From X → Y" tension formula available: F&B canonical is "From chaos to control."

## Official feature names (master §3 — verbatim, one or two adjacent JTBD groups only)
  Run your store smoothly: QR Order & Pay · E-Invoice · Inventory Management ·
    Kitchen Display System (KDS) · Multi Location Management · Reporting & Analytics · Employee Management
  Reach more customers and sell online: Online Ordering · Webstore · Marketplace Integration ·
    Takeaway & Pickup · Integrated Logistics
  Never paraphrase these. "real-time sales reports" is NOT a feature name — Reporting & Analytics is.
  §3 also caps a feature list at 3–5 items from one or two ADJACENT groups. The CNY reference ad
  shows 7 chips and gets two names wrong — a hyphenated Multi-Location and a lowercase e-Invoice. lint-allow
  Correct forms are Multi Location Management and E-Invoice. The linter WARNs on the wrong ones. f5 uses 5 correct names from
  the single "Run your store smoothly" group. Do not copy the reference ad's chip list.

## Set inventory
  f1 promo, 1:1, merchant portrait at dawn        f2 promo, 1:1, product hero poster
  f3 feature+promo, 1:1, Reporting & Analytics    f4 feature+promo, 1:1, order channels
  f5 feature showcase, 16:9, café counter + floating feature chips + Heroes Day props
     (modelled on the CNY "GET UP TO 55% OFF" landscape ad; seasonal props swapped to
      sampaguita garland, gold eight-ray sun, three gold stars, desk-stand flag)

## Meta safe zones (master §4)
  1:1 Feed 1080×1080 — 64px all sides, safe area 952×952 centred.
  16:9 Landscape 1920×1080 — top 100, bottom 150, sides 100, safe area 1720×830 (y=100→930).
  9:16 Reels 1080×1920 — top 250, bottom 500, sides 64. Headline y≥280, CTA pill ends y≤1400.
  Bottom 500px is dead zone. Design to Reels; it auto-passes Stories.

## PALETTE — DOCUMENTED DEVIATION FROM MASTER §1
  Master §1 mandates StoreHub Orange #ff9419 + Black #2f2922 dominant.
  THIS FLIGHT DELIBERATELY OVERRIDES THAT, on Zaid's explicit direction (2026-08-13):
  Philippine national colours carry the design to evoke patriotic emotion.
      royal blue #0038A8 · flag red #CE1126 · flag gold #FCD116 · white
  StoreHub orange appears nowhere. The white StoreHub wordmark is the only brand mark.
  Do NOT "correct" this back to brand palette — it is an intentional, signed-off exception
  scoped to the Heroes Day flight only. Revert to master §1 for all other work.

## Occasion motif (consistent across all four)
  Stylised eight-ray sun in flag gold + three gold five-pointed stars.
  Sun always entirely clear of the headline — no ray may touch a letter.
  Composition echoes the flag's own geometry: blue field, red block, white division.
  Lockup: gold uppercase ARAW NG MGA BAYANI / white uppercase NATIONAL HEROES DAY, AUGUST 31
  Promo band: red, containing HEROES DAY PROMO.

## Imagery (master §1)
  All faces must be Pan-Asian Southeast Asian — state this positively in every prompt. Aspirational modern venues, good lighting, clean
  fit-out, merchant looks successful. Never downmarket. Authentic and documentary, but upmarket.

## Standing negatives (append to every prompt)
  no competitor branding, no delivery app logos icons or brand names, no third-party app UI,
  no manual cash-handling props, no cash drawer, no cash-register unit beneath the screen,
  no downmarket venue, no clutter, no worn or dated fittings, no plastic furniture,
  no fluorescent lighting, no makeshift structures,
  no revolutionary or historical costume, no monuments, no banners with letters on them,
  no national flag draped or waving, no bunting, no confetti,
  no garbled text, no misspelled words, no invented or nonsense words,
  no extra words beyond those specified, no extra hands or fingers, no watermark.

## Known failure modes (all observed in this set — the constraints are load-bearing)
  1. Hallucinated words injected into headlines → "reading exactly these N words and no others".
  2. Duplicate objects (two phones, two terminals) → state the exact count explicitly.
  3. Small interface text garbles → cap on-screen items, demand short names at large size.
  4. Peso sign renders longhand as "pesos" → write the literal ₱ character inside a quoted
     exact string. Describing the glyph ("with a peso sign in front") reliably fails.
  6. Every string must be quoted verbatim, punctuation included. Described copy garbles;
     quoted copy survives. Keep total on-image strings low — each one is a failure surface.
  7. Floating screen-forward hardware reads as customer-operated self-service equipment,
     which master §0.1 bans depicting. Always ground the terminal on a counter surface.
  5. Terminals grow cash drawers → standing negative above.

## Gates
  Lint every prompt before use: python3 ~/Code/cranium/scripts/storehub-compliance-lint.py <file>
  Master §6: the linter guards words, not pixels. Review rendered output against §1 and §4 by eye.
  Master §7 rule 4 applies to stills too: generated type is unreliable. Final numbers, price
  lines, POS UI and the logo lockup MUST land as post overlays in Pencil, not generation.
  Every prompt carries a PLATE VARIANT block for exactly this. The in-prompt type exists so a
  single generation can be reviewed as a whole composition — it is not the shipping artwork.
  LINTER BLIND SPOT: pricing-ph-unit only fires when the ₱ glyph is present. A prompt that
  spells "pesos" or omits the symbol passes the gate while carrying a wrong price. Always
  write the literal ₱ character. Worth adding a pricing-ph-number rule to the linter.

## PRICE — one resolved, two still open
  RESOLVED 2026-08-14 (Zaid): ₱63/day is the main callout; ₱22,995/year rides with it as the
  canonical master §1 unit. This reconciles master §1 with data/knowledge_base.json, which records
  "₱63 is the top-performing PH message across 2 quarters" — they were never competing anchors,
  they are the same number in two units. Deviation from a strict reading of §1 is deliberate and
  mitigated by always showing the annual line.

  STILL OPEN 1 — the annual NUMBERS disagree. Master §1 says ₱22,995/year. config/products.json:21
  and :46 say ₱49,900/year. Gap of ₱26,905. This set follows the master. If ₱22,995 is right,
  patch products.json in the same commit. Blocks spend.

  STILL OPEN 2 — the offer number disagrees. config/products.json:53 = "Up to PHP 20,000 off on
  hardware". Shipped PH-batch_001/ad-copy.md used ₱21,000. This set uses "Up to ₱21,000" — the
  shipped number with the qualifier restored. An unqualified absolute discount claim is a DTI
  sales-promo exposure in PH, so "Up to" is mandatory whichever number wins.

  NOTE — KB warns the ₱21,000 hook is CPL-expensive: "High absolute price as primary hook
  (₱21,000) creates CPL spike — 4.6x benchmark" (PH Q4 Independenceday_P21000 CPL RM456).
  f2 and f5 make it the largest element. Deliberate, but it is a known-expensive hook — which is
  a further argument for ₱63/day carrying the price story on f1, f3 and f4.

## Not run for this set
  Master §8 Lateral Protocol (blind divergence → translation → registry gate → registry
  write-back) governs every NEW concept. These four were built directly from StoreHub
  context, so §8 has not been satisfied. Run it before treating these as approved concepts.
