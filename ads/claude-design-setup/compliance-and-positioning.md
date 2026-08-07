# StoreHub Ads — Compliance Rules + Positioning Vocabulary

Source of truth for what we **can** and **cannot** put in paid creative. Pair this with `brand-snapshot.md` (visual rules) and `brand.json` (full spec).

---

## 1 · Competitor / third-party naming — HARD COMPLIANCE RULE

**Never name competitors or third-party delivery platforms in creative.**

| ❌ Never say | ✅ Say instead |
|---|---|
| GrabFood | "food delivery" / "delivery apps" / "third-party delivery" |
| FoodPanda | "food delivery" / "delivery apps" / "third-party delivery" |
| ShopeeFood | "food delivery" / "delivery apps" / "third-party delivery" |
| Grab | "ride and delivery apps" / "third-party platforms" |
| Lalamove / Pickupp | "third-party logistics" / "delivery riders" |
| Any named POS competitor | "your old POS" / "legacy systems" / "manual systems" |

**Why:** Legal / competitor IP / Meta policy risk. This applies to copy AND visuals — never show competitor logos, app icons, or recognisable UI in any ad frame.

**Reframes for common patterns:**

- ~~"GrabFood commission RM4,200 + FoodPanda RM1,500"~~ → **"Delivery app commissions: RM5,700/month"**
- ~~"GrabFood. FoodPanda. ShopeeFood. Excel. WhatsApp. Manual POS."~~ → **"Delivery apps. Spreadsheets. Messaging. Manual POS. Paper receipts. Old systems."**
- ~~"Stop paying 30% to FoodPanda"~~ → **"Stop paying 30% in delivery commissions"**
- ~~"You're paying how much in GrabFood fees?"~~ → **"You're paying how much in delivery fees?"** ✓ (already in tone-of-voice good list)

**Applies retroactively:** The C007 reference PNGs in `ad-references/` were produced before this rule was finalised and still show GrabFood / FoodPanda / ShopeeFood in the left-panel icons. **Use them as references for visual style only — never replicate the competitor naming.**

---

## 2 · Industry verticals (4) — positioning + feature checklists

We target four verticals. Use the feature checklists below when writing vertical-targeted ads. The "From X to Y" hooks are proven examples of a free formula — any pair can serve any vertical; nothing is vertical-locked.

### F&B 🥐
- **Hook:** "From chaos to control."
- **Promise:** "Handle peak hours without breaking a sweat. Zero mistakes."
- **Checklist:** e-Invoicing compliant · Robust cost management · Minimal staff training · Integrated digital payments · Actionable sales reports
- **CTA:** Learn more / Book a free demo

### Retail 🛍️
- **Hook:** "From clutter to clarity."
- **Promise:** "Sell both online and offline with perfect inventory accuracy."
- **Checklist:** e-Invoicing compliant · Smart stock management · Minimal staff training · Integrated digital payments · Actionable sales reports
- **CTA:** Learn more / Book a free demo

### Service 💅 (salons, clinics, fitness, beauty, repair)
- **Hook:** "From friction to flow."
- **Promise:** "Keep schedules full and stress low: no double-ups, no chaos."
- **Checklist:** e-Invoicing compliant · Customer management · Minimal staff training · Integrated digital payments · Actionable sales reports
- **CTA:** Learn more / Book a free demo

### Enterprise 🏢 (multi-outlet, franchises, chains)
- **Hook:** "From gaps to structure."
- **Promise:** "Manage hundreds of outlets or franchises from one dashboard."
- **Checklist:** Enterprise support · Priority feature request · Custom developments · Centralised management · Dedicated API access
- **CTA:** Contact us (NOT "Book a demo")
- **Card style:** Orange background card — visually elevated as premium tier

---

## 3 · Feature taxonomy — official product names + JTBD groupings

Use these names verbatim in copy. Group them under the matching JTBD when listing features.

### Seamless Checkouts & Payments 💳
- Point of Sale (POS)
- Payments

### Run your store smoothly 🏪
- QR Order & Pay
- E-Invoice
- Inventory Management
- Kitchen Display System (KDS)
- Multi Location Management
- Reporting & Analytics
- Employee Management

### Customer Loyalty made easy 🏷️
- Loyalty Program
- Membership
- Engage (CRM / Marketing Automation)
- Customisable Promotions

### Reach more customers and sell online 🌐
- Online Ordering
- Webstore
- Marketplace Integration
- Takeaway & Pickup
- Integrated Logistics

**Usage:** When picking 3–5 features for a bullet list in an ad, draw from one or two adjacent JTBD groups. Don't cherry-pick across all four — feels scattered. For F&B leaning ads, lead with "Run your store smoothly" + "Customer Loyalty"; for retail, lead with "Seamless Checkouts" + "Reach more customers"; for service, lead with "Customer Loyalty"; for enterprise, lead with "Run your store smoothly" + "Multi Location".

---

## 4 · The "From X to Y" formula

This is a portable copy structure that works across all 4 verticals:

> **From {pain state} to {promise state}.**

Examples:
- F&B: "From chaos to control."
- Retail: "From clutter to clarity."
- Service: "From friction to flow."
- Enterprise: "From gaps to structure."

Extendable patterns for ad headlines:
- "From spreadsheets to single source."
- "From queues to flow."
- "From manual to magic."
- "From midnight to 6pm." (already used in batch_002 C_002)
- "From 6 tools to 1." (rephrase of C_007 hook — competitor-safe)

This formula is short (4–6 words), question-adjacent, and reusable across markets — keep it in the rotation.

---

## 5 · Imagery tier + copy — HARD do-not-repeat rules

Two recurring errors, same root cause: positioning StoreHub merchants as downscale / manual instead of modern / aspirational.

**5a · Venue tier = aspirational, not downmarket.**
- **Show:** modern, well-fitted cafés, bistros, full-service restaurants, established retail / boutiques — good lighting, clean fit-out, mid-to-upmarket; the merchant looks successful.
- **Keep:** Pan-Asian / SEA faces only (never Western); authentic, documentary, real venues.
- **Never:** roadside mamak, basic kopitiam, hawker stalls, cluttered / run-down interiors, "cash tin" aesthetics, anything that reads low-income.
- The MY ad-grid (`storehub-my-ad-grid.html`) describes settings as kopitiam / mamak — **translate these UP** to modern venues when prompting; do not render them literally.

**5b · Never use the word "till."**
- Use "cashier", "checkout", "POS", or "the counter" (e.g. "never hit the till" → "never reach the cashier").
- "Cash drawer" is fine for reconciliation-pain themes; "till" and old-world cash-register language are not — they frame the business as manual / cash-only.

Cross-project mirror: `~/.claude/CLAUDE.md` (brand essentials) + `~/cranium/reference/storehub-creative-rules.md`.
