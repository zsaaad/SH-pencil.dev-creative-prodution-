# Batch 2 — Image Generation TODOs

**Created:** 2026-04-27
**Why this exists:** Three concepts (C_006 right-panel, C_010, C_012) were revised in `ads/SH Pencil ads batch 2.pen`. C_006's typo'd dashboard image was replaced with primitive-rendered UI (no image needed). C_010 and C_012 still need photographic AI imagery — those frames currently reference 6 placeholder paths that don't exist on disk, so they will render blank dark-navy backgrounds until the images are generated.

Run these `G()` prompts in Pencil.dev, then save the outputs to the exact paths below.

---

## C_010 · Pasar Malam Gerai (3 images)

**Prompt (use verbatim):**
> Candid photo of a Malaysian pasar malam satay stall at night, string lights, smoke from the grill, merchant serving a customer, customer scanning a QR code with their phone, warm evening light, documentary, 35mm. Pan-Asian faces only. No Western faces. No visible text or branding.

| Save to | Aspect | Frame |
|---|---|---|
| `ads/images/c010-pasar-malam-1x1.png` | 1080×1080 | C_010 \| T7 \| pasar-malam-gerai \| 1080x1080 |
| `ads/images/c010-pasar-malam-16x9.png` | 1920×1080 | C_010 \| T7 \| pasar-malam-gerai \| 1920x1080 |
| `ads/images/c010-pasar-malam-9x16.png` | 1080×1920 | C_010 \| T7 \| pasar-malam-gerai \| 1080x1920 |

**Composition note:** lower 30% of the image must read clean for the dark gradient overlay + headline "Your gerai. Our tech." Position the merchant/customer interaction in the upper two-thirds so the gradient won't crop the action.

---

## C_012 · Cinematic gut-punch (3 images)

**Prompt (use verbatim):**
> Cinematic rain scene at dusk, closed-down Malaysian shop with "For Lease" sign in window, single person figure with umbrella walking away, muted blue-grey colour palette, wide lens, shallow depth of field, documentary photography. Pan-Asian figure. No visible text on the storefront other than a "For Lease" sign. No branding.

| Save to | Aspect | Frame |
|---|---|---|
| `ads/images/c012-cinematic-1x1.png` | 1080×1080 | C_012 \| T12 \| year-2-math \| 1x1 |
| `ads/images/c012-cinematic-16x9.png` | 1920×1080 | C_012 \| T12 \| year-2-math \| 16x9 |
| `ads/images/c012-cinematic-9x16.png` | 1080×1920 | C_012 \| T12 \| year-2-math \| 9x16 |

**Composition note:**
- 1×1 and 9×16: the white "Year 1 GrabFood / Year 2 StoreHub" number panel sits bottom-right (1×1) or middle-bottom (9×16). Keep that area visually quiet — broad pavement, dark wall, rain texture rather than busy detail.
- 16×9: the right half of the frame holds the headline + numbers + CTA on a dark gradient. Compose the closed shop and umbrella figure on the LEFT half.

---

## C_006 · No image regeneration needed

The right-panel image with "ScoreHub" + "SKUa" typos has been removed and replaced with a primitive-rendered dashboard mock (header pill with type-set "StoreHub" + "TOTAL SKUs · 1,247" stat + "✓ ALL RECONCILED" green badge). Brand text is now type-set, so no AI hallucination risk remains.

Left-panel warehouse image is unchanged across all 3 ratios (`generated-1777263541087.png`, `generated-1777263551429.png`, `generated-1777263545602.png`) — those are clean and stay.

---

## Other pre-launch hard gates (unchanged from analysis.md)

- C_008 — confirm LP CTA reads "Book your free demo" before any spend (Batch 1 stop-condition)
- C_003 — confirm Binq Dessert testimonial release covers paid Meta usage; $5–10 preflight before scaling
- C_012 — finance team must approve the RM 21,900 vs RM 1,240 numbers
- C_009 — 30-second Google search on "REST KEDAI MAKAN SYED" signage; regenerate if it matches a real shop
