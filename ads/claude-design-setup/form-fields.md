# Claude Design — Setup Form Paste-In Copy

Open Claude Design's "Set up your design system" page and use this file as your fill-in guide. Each section maps 1:1 to a form field.

---

## Field 1 — Company name and blurb

**Paste this (≈45 words, fits the one-sentence example pattern):**

> **StoreHub Ads Design System** — for StoreHub, an all-in-one cloud POS platform serving 20,000+ F&B and retail merchants across Malaysia, Philippines, and Thailand. Used to generate paid Meta ad creative in three fixed sizes: 1080×1080, 1920×1080, 1080×1920.

---

## Field 2 — Link code on GitHub

**Skip.** Leave empty.

---

## Field 3 — Link code from your computer

**Skip.** Our brand JSON config is included as an asset (see Field 5) — that's the cleanest path. Don't drag the config folder here; Claude Design wants frontend code, not config JSON.

---

## Field 4 — Upload a .fig file

**Skip.** We don't maintain a Figma file. (Migrating away from Pencil.dev to Claude Design is exactly the reason this folder exists.)

---

## Field 5 — Add fonts, logos and assets

**Drag this entire folder in:**

```
/Users/zaidsaad/Desktop/Code/Pencil.dev/ads/claude-design-setup/
```

What Claude Design will pick up:
- `logos/` — 4 logo files (orange wordmark for light BG, white reverse for dark/orange BG, black mono, H-mark icon)
- `ad-references/` — 4 vetted policy-compliant launched champion ad PNGs (C007 references removed on 2026-06-04 for naming competitors; compliant replacement to follow)
- `brand.json` — full brand specification (colors, typography, gradients, logo rules, imagery rules, tone)
- `brand-snapshot.md` — condensed human-readable brand brief
- `compliance-and-positioning.md` — competitor-naming rules + 4 verticals + feature taxonomy

**Fonts:** All on Google Fonts — no upload needed:
- **Barlow** (Black 900, ExtraBold 800, Bold 700, SemiBold 600) — headlines
- **Open Sans** (Regular 400, SemiBold 600, Bold 700) — body, sub-headlines, CTA
- **Caveat** — handwritten display, lifestyle copy only
- Multi-language (for localized variants): **Noto Sans SC**, **Smiley Sans**, **IBM Plex Sans Thai**, **Noto Sans Thai**, **Sriracha**

---

## Field 6 — Any other notes?

**Paste this (covers compliance + verticals + features + visual rules — complements brand.json):**

> **What we use this for:** generating Meta paid-ad creative only. Three fixed output sizes — 1080×1080, 1920×1080, 1080×1920. Don't generate websites, dashboards, or app UI.
>
> **META SAFE ZONES — non-negotiable. All headlines, sub-headlines, CTA pills, and logos must stay inside these safe zones, or Meta's runtime UI (profile bar, caption, music sticker, like/comment/share, in-stream CTA bar) will cover them at delivery:**
> - **1:1 (1080×1080) — Feed:** 64px padding all sides. Safe zone 952×952 centered.
> - **16:9 (1920×1080) — In-stream:** 100px top, 150px bottom, 100px sides. Safe zone 1720×830 (y=100→930). CTA pill bottom at y ≤ 900.
> - **9:16 (1080×1920) — Stories + Reels (CRITICAL):** **250px top buffer, 500px bottom buffer**, 64px sides. Safe zone 952×1170 (y=250→1420). Headline top at y ≥ 280. CTA pill bottom at y ≤ 1400. Top-right logo at y ≥ 250. Bottom 500px is DEAD ZONE — never place anything critical there. The 500px figure uses the conservative Reels spec; do not use the smaller Stories spec.
> - Build a CSS safe-zone container per format and keep all critical content inside it. Backgrounds and decorative gradients may extend full-bleed.
> - Full spec with ASCII diagrams in attached `meta-safe-zones.md`.
>
> **HARD COMPLIANCE — never name competitors or third-party platforms.** Never write or show: GrabFood, FoodPanda, ShopeeFood, Grab, Lalamove, Pickupp, or any named POS competitor — in copy, in icons, in screenshots, in any visual. Always use generic terms: **"food delivery"**, **"delivery apps"**, **"third-party delivery"**, **"delivery commissions"**, **"old POS"**, **"legacy systems"**, **"manual systems"**.
>
> **Non-negotiable brand rules** (full spec in attached brand.json):
> - Colours: orange `#ff9419` + black `#2f2922` are dominant. Pink `#ff546f`, bold orange `#ff630f`, azure `#2a6ee8` are accents only. Never mix orange with green.
> - Fonts: Barlow Black for headlines (always largest), Open Sans for body and sub-headlines. Never use the same size across hierarchy levels.
> - Imagery: Pan-Asian Southeast Asian faces only. Never Western faces. Authentic real-merchant settings (modern cafe, modern restaurant, modern eatery, café, fashion retail, salon, multi-outlet chain). Real local food and contexts only.
> - Logo: top-right, safe zone, on a contrast plate if background is busy. Never spell as ScoreHub / Score Hub / Store Hub — always **StoreHub** (one word, mid-cap H).
> - Every static frame ends with a rounded pill CTA — orange or pink, ALL CAPS, max one line. "BOOK A FREE DEMO NOW" (MY) or "Sign up for a FREE demo" (PH). Enterprise tier uses "CONTACT US" instead.
>
> **4 industry verticals** (the "From X to Y" phrases are proven examples of a free formula — not vertical-locked):
> - **F&B 🥐** — "From chaos to control. Handle peak hours without breaking a sweat. Zero mistakes." Checklist: e-Invoicing compliant · Robust cost management · Minimal staff training · Integrated digital payments · Actionable sales reports.
> - **Retail 🛍️** — "From clutter to clarity. Sell both online and offline with perfect inventory accuracy." Checklist: e-Invoicing compliant · Smart stock management · Minimal staff training · Integrated digital payments · Actionable sales reports.
> - **Service 💅** (salons, clinics, fitness, beauty) — "From friction to flow. Keep schedules full and stress low: no double-ups, no chaos." Checklist: e-Invoicing compliant · Customer management · Minimal staff training · Integrated digital payments · Actionable sales reports.
> - **Enterprise 🏢** (multi-outlet, franchises) — "From gaps to structure. Manage hundreds of outlets or franchises from one dashboard." Checklist: Enterprise support · Priority feature request · Custom developments · Centralised management · Dedicated API access. **Use orange background card style + CTA = CONTACT US.**
>
> **Official feature names — use verbatim, group by JTBD:**
> - **Seamless Checkouts & Payments:** Point of Sale (POS), Payments
> - **Run your store smoothly:** QR Order & Pay, E-Invoice, Inventory Management, Kitchen Display System (KDS), Multi Location Management, Reporting & Analytics, Employee Management
> - **Customer Loyalty made easy:** Loyalty Program, Membership, Engage (CRM / Marketing Automation), Customisable Promotions
> - **Reach more customers and sell online:** Online Ordering, Webstore, Marketplace Integration, Takeaway & Pickup, Integrated Logistics
>
> **Voice:** practical, modern, empowering, merchant-first. Question hooks work ("You're paying how much in delivery fees?", "Hiring a human or a system?"). No corporate jargon, no Western references.
>
> **Pricing anchors:** MY = "From RM3.40/day" or "RM3,960/year". PH = "From ₱22,995/year" + "BIR Accredited". TH = "Up to 55% off hardware". Social proof: "20,000+ merchants across Southeast Asia".
>
> **Proven creative templates we lean on:** Artifact Native (ad mimics a job post / WhatsApp / Google review / bank statement), Cultural Pride ("Your kopi. Our tech."), Competitive Contrast (split-screen "6 tools. Or 1." using generic competitor terms only), Milestone Math (line-item cost comparison cards), Testimonial cards. Reference PNGs in `ad-references/` are visual ground truth — match that quality bar but obey the new naming rules.

---

## After submitting

Once seeded, the first thing to try is regenerating one of the C007 reference variants. If Claude Design can match the brand colors, type hierarchy, and CTA pill on a "6 tools. Or 1." prompt without further hand-holding, the brief is dialed in. If it drifts (wrong typeface, off-palette accent, missing CTA), come back and sharpen the "Any other notes?" field.
