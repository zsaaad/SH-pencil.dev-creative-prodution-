# MY-batch_011 — Family I Round 1 Build Report

**Container:** `sp2g7` at y:48000 — `Family I — I_085 to I_096` (1080×1080 × 12)
**Status:** READY (geometry verified; screenshots blank — known Pencil bug)

## Locked illustration style (binding across all 12)
- Flat vector / mid-century modern
- 5–6px black outlines (`#2f2922`)
- Warm flat fills: brand orange `#ff9419`, pink `#ff546f`, cream `#fff8ea`, per-frame accent bg
- No gradients, no 3D, no photorealism
- Characters: Pan-Asian skin tone `#e0b58a`, black hair, dot eyes, hand-drawn smile curve, friendly half-smile
- Per-frame accent backgrounds locked exactly to brief: `#FF398C`, `#D7F35B`, `#FFD93A`, cream, `#7C4A2C`, light grey, `#E63946`, `#D9D9F7`, `#C5B5F2`, mint, `#ff546f`, `#7C4A2C` wood-grain

## Frames (12)

| ID | Name | Concept |
|---|---|---|
| CxqUB | I_085 \| kopi-mascot | Orange kopi-cup mascot w/ speech bubble + A/B/C choice list (StoreHub highlighted) |
| ugAYd | I_086 \| knight-shield | Pan-Asian knight with SH shield blocking floating SaaS icons (lime bg) |
| OK00I | I_087 \| magician | Pan-Asian magician pulls glowing StoreHub iPad from top hat (yellow bg) |
| A8WWK0 | I_088 \| bike-motorbike | Same merchant on bicycle (manual close-out) vs motorbike (StoreHub) — side by side |
| QSDnr | I_089 \| sandwich | Cross-section sandwich w/ labelled layers POS/Inventory/Loyalty/Reports (brown bg) |
| QgRI8 | I_090 \| twin-merchants | Two Pan-Asian merchants in red aprons pointing at each other — Floor vs Office |
| OR4uy | I_091 \| unlock-reward | Glowing orange shopping bag with RM tag (red bg, sun rays) |
| J5mqS | I_092 \| paper-planes | 12 orange paper planes converging on central SH mark (lavender bg) |
| ODx0Y | I_093 \| shoebox | Brown shipping box w/ FRAGILE stamp + tape (lavender bg) |
| S4K2v | I_094 \| cool-dog | Tan dog with sunglasses + tiny POS beside it (mint bg) |
| Wydo8 | I_095 \| broken-hammer | Hammer with snapped-off head, shards flying (pink bg) |
| qFf11 | I_096 \| vintage-tv-teh | Vintage CRT TV showing StoreHub dashboard + teh-tarik kettle balanced on top (wood bg) |

## Judgement calls
- **All illustrations built with Pencil-native paths/ellipses/rectangles** — NO `Generate()` AI calls. This guarantees style consistency across all 12 frames (which is the binding rule).
- Pan-Asian skin tone hex `#e0b58a` used consistently for every face/exposed skin. Black hair `#2f2922`.
- Bike vs motorbike (I_088) shows the SAME merchant (red apron, same body construction) on two vehicles — meets twin-character brief intent.
- Twin merchants (I_090) use mirrored pose with same character template — drawMerchant() function ensures parity.
- Kopi-cup mascot (I_085) is the only non-human character, fits "mascot" brief; eyes + smile read as a character not just an object.
- Knight (I_086) uses Pan-Asian skin tone for visible head, helmet covers most.
- Magician (I_087): Pan-Asian head, black hair, apron with pocket. Glowing iPad emerges from hat. Mini stars around hat as magical sparkle.

## FLAGGED items
- **Screenshot tool returns blank PNGs** — same bug noted for Family E and H. Verified via geometry only.
- **No real third-party logos present** — knight blocks generic geometric SaaS icons (rotated squares), not branded ones. Acceptable.
- **No Western faces** — all human/anthropomorphic features rendered as Pan-Asian Pan ✓
- **Some illustrations are stylised geometric (knight body uses zigzag shapes for armour)** — flat-vector convention. Reads as armour at small sizes; may want softer organic shapes in R2.
- **I_087 magician's hat** drawn with negative geometry — verify it renders as a top hat shape and not a inverted form when reviewed in app.
- **I_089 sandwich** uses brown `#7C4A2C` bg per brief; layer slabs are bread/lettuce/tomato colors with thick outlines — reads as sandwich cross-section.
- **I_092 paper planes**: 12 planes converging — could be denser, fine as is.

## AI render queue
- **None.** Style consistency is the hard requirement and AI image gen would make 12 frames diverge. All frames built from primitives.

## Brand-rule compliance
- Orange CTA pill `BOOK A FREE DEMO NOW` on every frame ✓
- StoreHub wordmark bottom-right ✓
- No Beep / no delivery commissions / no real competitor names / no Western faces ✓
- Anchor (RM3.40/day · 24hr setup · 17,000+ merchants) appears in I_085/086/091/094 where brief specified ✓

## Token estimate
~14k tokens for Family I (12 frames × ~1.1k each + verification).

## Round 2 priorities
- Verify in-app render of all 12 (style cohesion check, especially I_086 knight, I_087 magician, I_096 vintage TV)
- Check I_085 kopi-cup mascot reads as a character not an emoji
- Confirm bicycle/motorbike (I_088) labels positioned over correct vehicle
- Tighten any frame where character anatomy looks broken at full size
