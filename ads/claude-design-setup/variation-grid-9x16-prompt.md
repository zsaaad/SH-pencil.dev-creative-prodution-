# StoreHub 9:16 Variation Grid — Master Pencil Prompt

*Rewrites the original "1 ad per theme" brief into a system that builds **3 creative variations × 5 static ads per theme = 15 frames**. Grounded in the StoreHub MY ad grid (`storehub-my-ad-grid.html`); variation lanes + device menu sourced from the ADFOLIO inspiration banks. Market = MY (swap the price chip + transition phrases for PH/TH).*

---

## ⛔ THREE HARD RULES — READ FIRST, APPLY TO EVERY FRAME
*These are the failures that keep slipping into generated frames. A frame that breaks any one is a **reject** — regenerate, do not ship it. They override anything below if they ever conflict. Words-on-frame are governed in full by **`malaysian-english-voice.md`** — read it; the rules below are the short version.*

**RULE 1 · RENDER ONLY THE TABLE COPY — never the source notes. Clean words only.**
The single source of rendered truth is the **pre-cleaned `Headline / Subcopy / Artifact / Shock` text in the §7/§8 per-cell table.** Render that, and only that.
- **NEVER read, translate, paraphrase, or echo** a grid `hook` / `concept` / `setting` / `s2note` / `beat` onto a frame. Those are loose internal video-VO notes — they contain the banned cash-register word, "cash tin", "kopitiam", "mamak", and American idiom, and they are **NOT rendering copy**. *Don't clean the source — ignore it.* If a string isn't in the table, it doesn't go on the frame.
- **No cash-register language** in ANY readable string (headline, subcopy, artifact text, sticky note, chat bubble, receipt, Z-report, margin note, shock-word): never the 4-letter register word (t-i-l-l), never "cash tin" / biscuit-tin / shoebox-of-cash. Use **"cashier" / "checkout" / "POS" / "the counter"** ("cash drawer" is fine for a reconciliation artifact).
- **Malaysian / British English only — no Americanisms** (spelling *and* vocabulary *and* idiom). Market = MY; American English breaks brand.json's "avoid Western cultural references". Full banned→use tables in `malaysian-english-voice.md` (e.g. colour not color, queue not line, shop/outlet not store, "took off" not "blew up"). Brand/feature names stay verbatim.

**RULE 2 · NEVER a downmarket / low-income setting. Aspirational, upmarket venues ONLY.**
- **BANNED settings:** roadside mamak, basic kopitiam, hawker stall, pasar / wet-market stall, food-court lot, plastic-stool / bare-table setups, bare-bulb or harsh fluorescent-strip lighting, cluttered or run-down interiors, a literal cash tin on the counter.
- **DEFAULT TO instead:** a well-fitted specialty café, a modern bistro or full-service restaurant, an established boutique / retail shop with a clean fit-out, a contemporary salon / clinic / studio — good natural or warm designed lighting, a tidy counter, the merchant clearly **doing well**. **Pan-Asian / SEA faces only, never Western.**
- *Pain artifacts can still be messy* (a cluttered drawer, a stack of chits, an overflowing receipt spike) — that's the problem we solve. The mess lives in the **artifact/desk**, never in a **downmarket venue**. The shop around it always reads successful.
- If a frame could read as low-income at a glance, **it's wrong — push it more upmarket and regenerate.**

**RULE 3 · Build the frame from the §7/§8 cell, not from your instincts.** When in doubt about a word, check `malaysian-english-voice.md`; about a venue, re-read RULE 2. The word-gate (RULE 1) and the setting-gate (RULE 2) both run again at §9.

---

## 0 · WHAT THIS BUILDS
For ONE theme from the grid, build **15 static frames**, each **1080 × 1920 px (9:16, Stories/Reels)**:
- **5 static ads** `A1…A5` (each its own slot, copy taken from the §7/§8 per-cell table — never the raw grid hook) × **3 variation lanes** `V1 / V2 / V3` (§4).
- **Frame naming:** `{THEME}.{A#}.{V#}` → e.g. `CR-01.A1.V1`. Print the code as a small label above each frame (Open Sans Semibold 28px `#2f2922`, 20px above the art, left-aligned).

**Build unit (recommended):** build **one static ad at a time = its 3 lanes side by side** (3 × 1080×1920 on one canvas, 60px gutters). That's 5 quick builds per theme. *Why per-ad, not all-15-at-once:* the 3 lanes share one hook so the trio stays visually consistent, and a 15-frame mega-canvas (~5.5k × 5.9k px) drifts on scale and safe-zone math. After all 5 are built, tile them into a **5-column (A1→A5) × 3-row (V1→V3) contact sheet** for review.

---

## 1 · BRAND SYSTEM (all 15 frames)
- **Colours:** Orange `#ff9419` + Black `#2f2922` dominant. Accents sparingly: Pink `#ff546f`, Bold Orange `#ff630f`, Azure `#2a6ee8`. Cream `#fff8ea` for type-led backgrounds. **NEVER orange + green together.**
- **Fonts:** Barlow (Bold / ExtraBold / Black) for headlines + giant type. Open Sans (Semibold / Bold / Regular) for subcopy, CTA, microcopy. Caveat only for a handwritten chalk/marker accent.
- **Logo:** wordmark **StoreHub** — one word, capital **S** + capital **H** (never ScoreHub / Store Hub / Score Hub / all-caps). Top-right, top edge **y ≥ 270**. *(Top-right is correct for 9:16 — do not "fix" it to a bottom corner; the bottom is dead zone.)*
- **Imagery (see RULE 2 up top — non-negotiable):** photographic, documentary, candid, natural light. **Aspirational, upmarket, modern venues** — a well-fitted specialty café, a modern bistro / full-service restaurant, an established boutique or retail shop with a clean fit-out, a contemporary salon / clinic / studio; good lighting, tidy counter, the merchant clearly doing well. **Pan-Asian / SEA faces only — never Western.** Authentic, not staged stock. **NEVER downmarket / low-income settings** — no roadside mamak, basic kopitiam, hawker / food-court / wet-market stall, plastic-stool setup, bare-bulb or fluorescent-strip lighting, run-down interior, or a literal cash tin. *Mess belongs only in the pain artifact (drawer/chits), never in the venue.*
- **Copy / rendered text (see RULE 1 up top — non-negotiable):** render only the §7/§8 table copy; never echo a grid hook/concept/setting. No cash-register language ("cashier" / "checkout" / "POS" / "the counter"; "cash drawer" OK, "cash tin" not). **Malaysian / British English only — no American spelling, vocabulary, or idiom.** *(Full rules: `malaysian-english-voice.md`; also CLAUDE.md "Hard creative rules" + `compliance-and-positioning.md` §5.)*
- **CTA:** rounded pill, fill `#ff9419`, label **"BOOK A DEMO"** in Open Sans Bold `#2f2922`. *(Ignore any "BOOK A FREE DEMO NOW" wording from other briefs — standardise on "BOOK A DEMO".)* Enterprise themes only: label becomes **"CONTACT US"** on an orange card.
- **Microcopy chip** by the CTA: **"From RM3.40/day"** (Open Sans, low-key).

---

## 2 · 9:16 SAFE ZONES (hard — every frame)
1080 × 1920 · top buffer 250 · bottom buffer 500 · side 64 → safe area 952 × 1170 (y 250 → 1420).
- Headline starts **y ≥ 280**.
- Top-right logo top edge **y ≥ 270**.
- CTA pill ends **y ≤ 1400**.
- **Bottom 500px (y 1420 → 1920) = DEAD ZONE.** Nothing important — no headline, no artifact reveal, no CTA. App chrome covers it.

**Fixed bottom block (use these guide coordinates so the CTA never slides into the dead zone):**
| Element | y-range | Notes |
|---|---|---|
| Headline (V1/V2) | ends **≤ y 1090** | ≥ 40px above subcopy |
| Subcopy (transition phrase) | ~y 1110 – 1170 | Open Sans ~40px |
| CTA pill | ~y 1240 – 1380 | **ends ≤ 1400** |
| "From RM3.40/day" chip | beside/above CTA, **≤ y 1400** | low-key |

---

## 3 · SHARED LAYOUT + SCALE
- **Gradient (V1 + V2 only — NOT cream V3):** linear `#2f2922`, ~0% → 75% opacity, top edge ~y 900 down to y 1420, so the headline/reveal passes **WCAG AA**.
- **Per-lane headline scale:** V1 = 90–120px · V2 reveal = 48–64px · V3 giant = 240–560px (capped, see §4).
- **Transition phrase (subcopy) — chosen per theme, not vertical-locked.** Any "From X → Y" pair (canonical below or invented) that names the theme's tension; keep one phrase consistent across a theme's 15 variants. Canonical examples:
  - F&B → **"From chaos to control."**
  - Retail → **"From clutter to clarity."**
  - Service → **"From friction to flow."**
  - Enterprise → **"From gaps to structure."**

---

## 4 · THE 3 VARIATION LANES
Weighted by proven leverage, not equal status. **V2 is the spine; V3 is the restraint counter-test; V1 is the grounded control.**

**V1 — NATIVE TREATMENT** *(control / grounded)*
Build this slot's V1 frame from its **§7/§8 "V1 — native treatment" column** — the treatment (Documentary-realistic / Before→After split / Talking-head-UGC / Data-on-screen / Cinematic-lifestyle), perspective (self / staff / third-person) and scene are all specified there. **Never read the grid hook/setting.** Natural or warm designed light, an **upmarket venue (RULE 2 — a well-fitted café / bistro / boutique / salon / clinic; never "a generic shop" or any downmarket setting)**, Pan-Asian merchant clearly doing well. The cell's table headline + subcopy + CTA over the gradient in the bottom block.

**V2 — NATIVE ARTIFACT** *(the spine — ADFOLIO "Artifact Mimics" + Receipt-as-Hero; T11 is the proven winner)*
Deliver the same cell message as a believable everyday artifact tied to the theme's pain — a thermal receipt, a stack of handwritten order-chits, a cash-count slip, a stylised staff chat, a chalkboard, a Z-report tape, an unopened official letter, an internal stock-count slip. The artifact reads as a believable **type** of object at a glance, **built only from generic, neutral primitives** (§5). It fills y 0 → ~1140; a clean **reveal strip at y ~1150 → 1400** holds the reveal line (48–64px) + CTA + chip. Logo overlaid top-right. **All rendered artifact text obeys RULE 1** — use only the cell's table strings (the reveal/artifact text given in §7/§8), never wording pulled from the grid hook; "cash drawer" / "cash-count slip" are the compliant forms, the cash-register word and "cash tin" never appear.

**V3 — TYPOGRAPHIC SHOCK** *(pure type — NO object, NO artifact, NO UI chrome)*
One of: **(a)** one oversized shock-number (digits ≥ 60% of art height: "RM0", "1 in 2"); **(b)** one single Malay word ("Bocor.", "Susah.") — a punchy BM shock-word is the one place BM belongs in an EN cut; **(c)** one ≤3-word line in clean MY English. On a flat cream `#fff8ea` or brand-colour field, dark/contrasting type, no gradient. Tiny subline + CTA in the bottom block. **Hard rule:** if the frame contains a receipt, pad, screen, chalkboard, or *any thing*, it's V2, not V3. (Single-object-on-cream still-lifes live in V1 as a swap, never in V3.) Cap giant type to **≤ 952px wide AND ≤ ~700px tall**; sits upper-mid (~y 320 – 1040).

### 4b · DEVICE SWAP MENU (optional — any cell may swap its default lane for a higher-fit device)
*Every swap still obeys RULES 1 & 2: upmarket venue only; rendered text is table copy only, clean MY English, no cash-register wording (`malaysian-english-voice.md`).*
- **Calendar Countdown** — deadline/compliance themes. **HC-06 must include one countdown cell:** `e-Invoice deadline: [DATE]. Days left: [N].`
- **Before→After Split** — give A5 a real split (left = chaos/buried; right = one clean `Reconciled ✓` line), not just a before/after *headline*.
- **Behaviour Call-Out** — highest stop-rate static: "Every closing you tally by memory. Stop."
- **Festival Edition** — any F&B theme within ~45 days of Raya / CNY / Deepavali swaps one cell for a festival artifact. **Anchor upmarket (RULE 2):** a modern café's festive service, a contemporary catering spread in a well-appointed home, an established specialty shop's festive stock crunch — never a downmarket sweet-shop / kedai or modest home.
- **Classifieds / fake job-post** — this is a proven control winner; carry it forward as a swap.
- **Confession** — first-person owner quote. **Only with a real, permissioned merchant quote** — never a fabricated named testimonial (compliance, §5).

---

## 5 · ARTIFACT & PHOTO COMPLIANCE (the highest-risk part — read before any V2 build)
Hard rule everywhere: **never name or show competitors / third-party platforms** (delivery apps, ride apps, named POS/payment competitors), and **no real logos, app icons, or recognisable delivery/POS UI** in any frame.

- **Government letters/portals (e-Invoice/LHDN):** NEVER render the Malaysian coat of arms (Jata Negara), any crest, official seal, watermark, or real LHDN/MyInvois letterhead. Use a plain official-style letter with a neutral geometric placeholder mark; the only government reference is the **words** "e-Invoice"/"LHDN" in plain type. Add low-contrast microcopy: *"Illustrative — not a real document."*
- **Chat artifacts:** neutral flat chat UI only. **No green wallpaper** (also breaks orange+green), no double-tick/read receipts, no platform header bar, no platform name/logo/icon. Grey/white bubbles, generic silhouette avatar, made-up contact name (e.g. "Shop Ops").
- **Bank/finance artifacts:** NEVER a real bank name, logo, brand colour, or app UI. Invented neutral name ("BANK ·····") on a plain mono row; phone "banking app" = abstract balance card. Add *"Illustrative — not a real statement."*
- **Receipt / Z-report / order-chit header:** the fictional shop's own name or "StoreHub" only — never a POS-vendor, payment-network, or bank name. Any barcode/QR is decorative and resolves to nothing.
- **Inventory slip:** a plain internal stock-count slip only — never a delivery-platform/marketplace order ticket (no platform order numbers or logos).
- **EDC / card-terminal objects:** blank screen — no Visa/Mastercard/bank/payment-network logos.
- **Documentary photos (V1):** scrub backgrounds for incidental real branding — delivery-app door stickers, rider jackets/bags, branded cups/packaging, app-store icons, competitor POS hardware/signage. None may appear.
- **No** delivery-commission framing ("30%", "0% commission"). **No** Beep / QR-ordering product. **No** unverified claims, uptime %, security certs, or fabricated named testimonials.

---

## 6 · HEADLINE DISCIPLINE
- **Render the §7/§8 table headline verbatim — do NOT re-derive it from the grid hook (HARD — RULE 1).** The table headlines are already tightened (≤ ~12 words, 2–3 lines) AND already cleaned of the cash-register word, "cash tin", "kopitiam"/"mamak"/"hawker", and American idiom. The grid `hook`/`concept`/`setting` are dirty video-VO notes — never read or paraphrase them onto a frame. *Don't clean the source — ignore it.* The single source of rendered truth is the table.
- **Adding a NEW cell not in §7/§8?** Write its headline fresh in clean MY English (`malaysian-english-voice.md`), pre-cleaned the same way — then render that. Never lift the raw hook. *(e.g. a raw hook "Full house all day. So why is the cash tin almost empty?" is rewritten to "Full house all day. Half the orders never reach the cashier." — and only the rewrite renders.)*
- Auto-fit to ≤ 952px width; size down before wrapping past 3 lines or crossing **y 1090**.
- V3 copy is restricted to a single word / single number / ≤ 3 words — push full sentences to V1/V2.
- Subcopy = the theme's chosen transition phrase (§3), consistent across all its variants.

---

## 7 · WORKED EXAMPLE — CR-01 "Where'd It Go" (F&B)
Scene: a busy modern café/bistro counter at close — owner with an open cash drawer + a stack of handwritten order chits, queue still buzzing behind. Subcopy (all 15): **"From chaos to control."** · CTA **BOOK A DEMO** · chip **From RM3.40/day** · logo **StoreHub** top-right.

| Slot | Tightened headline | V1 — native treatment | V2 — artifact (spine) | V3 — pure type |
|---|---|---|---|---|
| **A1** | "Full house all day. Half the orders never reach the cashier." | *Documentary:* owner at the counter holding the open cash drawer + a handful of order chits, a modern POS terminal/tablet visible on the counter (reads as a real business with a reconciliation gap, not a cash-only stall), blurred queue behind, warm light, POV/self. | A stack of unrecorded order chits beside an open cash drawer — the unrecorded chits are the hero; reveal strip below. | **"1 in 2"** giant on cream, subline "orders never reach the cashier." *(alt: single word "Hilang.")* |
| **A2** | "Chits say RM3,200. POS recorded RM2,650. Where's the rest?" | *Before→After split:* left = chit stack labelled RM3,200; right = counted cash drawer RM2,650; the RM550 gap circled. | Split artifact — chit total slip vs cash-count slip, RM550 gap marked in red. | Equation: **"RM3,200 − RM2,650 = ?"** small line "Where's the rest?" |
| **A3** | "Boss — half these orders never hit the system." | *Talking-head/UGC:* staff member mid-sentence to camera, owner half-in-frame, phone-shot feel. | Stylised neutral staff chat (grey bubbles, made-up "Shop Ops", no platform chrome): "Boss — half these never hit the system 😬" + reveal. | Single word **"Bocor."** huge on cream, tiny English gloss "leaking." |
| **A4** | "Every sale you don't record is profit you can't keep." | *Data-on-screen:* owner at counter, clean stylised overlay tallying recorded vs unrecorded (no real UI), third-person. | Thermal receipt (fictional shop header) with the total line highlighted + handwritten "not recorded" margin note. | **"RM0 kept."** giant on cream, subline "from every sale you don't record." |
| **A5** | "Busy all day. Bank barely moved. Something's leaking." | *Cinematic-lifestyle:* owner at close in a softly-lit upmarket café after hours (warm low-key cinematic light — moody, not dingy; the upmarket fit-out still clearly reads), abstract balance card glow on face (no real app), reflective. | Stylised bank-statement strip ("BANK ·····", flat balance line) beside a curling Z-report tape; "barely moved" marked. | Big **"RM0"** with subline "…is what the bank moved today." |

---

## 8 · THE OTHER THREE THEMES (full per-cell detail — same depth as §7)
Same lanes, scale, safe-zones, compliance.

### HC-06 "Drawer Of Doom" (F&B)
Scene: inside a well-fitted modern café/bistro (clean fit-out, warm light, merchant clearly doing well) — on the counter, a cluttered shop drawer of receipts + paperwork with an unopened e-Invoice letter on top, a wall calendar behind. **The clutter is confined to the drawer; the venue around it always reads upmarket (RULE 2).** Subcopy (all 15): **"From chaos to control."** · CTA **BOOK A DEMO** · chip **From RM3.40/day** · logo **StoreHub** top-right.
⚠ **Govt-artifact compliance (§5) bites hardest here** — no Jata Negara/coat-of-arms, no seal, no MyInvois letterhead; plain letter + neutral placeholder mark + "Illustrative — not a real document". **Includes the required Calendar Countdown cell (A1.V3).**

| Slot | Tightened headline | V1 — native treatment | V2 — artifact (spine) | V3 — pure type |
|---|---|---|---|---|
| **A1** | "The e-Invoice letter's in the drawer. The LHDN deadline isn't." | *Documentary:* owner's hand resting on the still-sealed e-Invoice envelope on a cluttered drawer, wall calendar soft-focus behind, warm late-afternoon shop light, POV/self. | The letter as hero — plain official-style envelope/letter, neutral geometric placeholder where a crest would be, only the words "e-Invoice / LHDN" in plain type, faint "Illustrative — not a real document" microcopy. | **Countdown:** "e-Invoice deadline: [DATE]. Days left: [N]." giant on cream, subline "Still in your drawer?" |
| **A2** | "No panic yet. Just a date getting closer." | *Cinematic:* a wall calendar with one date ringed in red, the unopened letter just below on the drawer edge, single warm lamp on a clean modern counter, the upmarket fit-out still visible behind, shallow depth, reflective, self. | A calendar page, one date ringed in red marker, a small sticky-arrow pointing to it. | Giant **"[N] days."** subline "until the date you keep not opening." |
| **A3** | "'I'll sort e-Invoice later.' Later runs out of road." | *Talking-head/UGC:* owner mid-shrug to phone camera at the counter, half-smile "I'll get to it" energy, candid handheld, self. | A yellow sticky-note on the drawer front, handwritten marker: "e-Invoice — later 🙄". | Single word **"Later?"** huge on cream, tiny line "runs out of road." |
| **A4** | "Twelve drawers. Twelve clocks. One deadline." | *Data-on-screen:* a stylised multi-outlet board (no real UI), twelve outlet tiles each with the same deadline clock and one shared red due-date, third-person. | A flat-lay row of twelve identical unopened official-style letters (same neutral placeholder), one per drawer. | **"12 → 1"** giant, subline "outlets, one deadline that fines them all." |
| **A5** | "Before: buried in the drawer. After: handled, compliant." | *Before→After split:* left = stuffed drawer with the buried letter; right = empty tidy drawer + a clean "Compliant ✓" slip, self. | Split artifact — left a drawer crammed with paper, right an empty drawer holding one neat "e-Invoice ready" slip. | Single word **"Done."** giant on cream, subline "before LHDN's date." |

### BW-09 "Went Viral, Handled" (F&B)
Scene: an established café with a line down the street after a viral post, baristas locked in. **Mood: aspirational breakout — brighter, energetic, daylight** (vs the crisis themes). Subcopy (all 15): **"From chaos to control."** · CTA **BOOK A DEMO** · chip **From RM3.40/day** · logo **StoreHub** top-right.
⚠ Any "social post" element is a **generic neutral card** — no real platform name, logo, or chrome.

| Slot | Tightened headline | V1 — native treatment | V2 — artifact (spine) | V3 — pure type |
|---|---|---|---|---|
| **A1** | "One post took off. Checkout didn't stall." | *Documentary:* queue snaking down the street outside, inside the baristas calm and fast, owner unfazed at the counter, bright daylight, candid, self. | A neutral generic "post" card (no platform name/logo/chrome) — big like/view count + caption "Sold out 🔥". | **"Viral. Calm."** two words, Barlow Black, on a bold-orange `#ff630f` field. |
| **A2** | "The crowd hit. The kitchen screen lost none." | *Data-on-screen (staff POV):* a stylised kitchen display clearing a wall of tickets cleanly during the rush, staff hands moving, none dropped, staff perspective. | A full ticket rail of order chits, every one stamped done. | **"0 lost."** giant on cream. |
| **A3** | "Went viral. Sold out clean — never oversold." | *Stylised-graphic:* a bold flat-graphic stock counter ticking down to "Sold out" — clean shapes, brand orange/black, deliberately a graphic, not a photo (honours the grid treatment), self. | A stock-count slip ticking to zero: "Sold out — clean · 0 oversold". | **"Sold out."** single line huge on cream. |
| **A4** | "One reel took off. A quick nudge filled every slot." | *Talking-head/UGC:* owner grinning to phone camera, "fully booked this week", energetic handheld, self. | A neutral weekly booking sheet, every slot filled in. | **"Fully booked."** giant on cream. |
| **A5** | "Crowds hit every outlet — every one held." | *Before→After split:* left = owner blind to outlets (scattered, anxious); right = a live all-outlets board, every tile live (orange/black tiles, azure status dot — never green), third-person. | Split — left a scatter of loose chits, right one clean live "All outlets" board (✓ in black/orange, never green). | **"All held."** giant on cream. |

### CR-02 "RM50 Short. Again." (Retail)
Scene: a boutique retail counter at 10pm, one lamp on, owner recounting a fistful of notes that won't add up. Subcopy (all 15): **"From clutter to clarity."** · CTA **BOOK A DEMO** · chip **From RM3.40/day** · logo **StoreHub** top-right.

| Slot | Tightened headline | V1 — native treatment | V2 — artifact (spine) | V3 — pure type |
|---|---|---|---|---|
| **A1** | "Drawer's RM50 short. Third time this week." | *Documentary:* owner under a single lamp at an upmarket boutique counter recounting a fan of notes, open cash drawer, a modern POS terminal/tablet visible on the counter (an established shop with a reconciliation gap, not a cash-only setup), tired expression, 10pm, self. | A cash-count slip with "−RM50" circled in red and a third tally mark scratched in the margin. | **"−RM50"** giant red on cream, subline "third time this week." |
| **A2** | "Counted it four times. Still doesn't match." | *Cinematic:* tight close on hands recounting notes in lamp glow, the rest of the upmarket boutique softly visible in warm shadow (not black/empty), frustrated stillness, self. | A slip showing four crossed-out tally totals, none matching, heavy pen-pressure marks. | **"×4. Still off."** on cream. |
| **A3** | "Boss, cashier's short — and nobody knows who closed what." | *Talking-head/UGC (staff POV):* a staff member turning to camera at the counter, owner half-in-frame behind, candid, staff perspective. | Neutral staff chat (grey bubbles, made-up "Shop Floor", no platform chrome): "drawer short again — who closed?". | Single word **"Who?"** huge on cream. |
| **A4** | "Sales say RM2,400. Drawer says RM2,310. Who's right?" | *Data-on-screen:* a stylised overlay (no real UI) showing "Sales RM2,400" vs "Drawer RM2,310", the RM90 gap highlighted, third-person. | A split slip — "Sales RM2,400" beside "Drawer RM2,310", RM90 gap marked in red. | Equation **"RM2,400 − RM2,310 = ?"** subline "who's right?" |
| **A5** | "One short drawer across ten outlets. HQ can't see which." | *Before→After split:* left = HQ blind (ten faceless outlet tiles, one quietly bleeding); right = HQ dashboard flagging the exact outlet, third-person. | Split — left ten identical cash drawers (one ringed red), right a clean "Outlet 7 flagged ✓" board. | **"10 → 1"** giant on cream, subline "which outlet's bleeding?" |

---

## 9 · REVIEW CHECKLIST (run on every frame before export)
**REJECT GATES — a frame that fails any of these does not ship; fix and regenerate (the failures that keep slipping through, see RULES 1–3 up top + `malaysian-english-voice.md`):**
1a. **Source-echo (RULE 1):** every rendered string traces to the §7/§8 cell table. No grid `hook`/`concept`/`setting`/`s2note`/`beat` text leaked onto the frame. *Test: if you can find the sentence inside `themes-*.json` or `live-*.json`, it's wrong — rewrite it from the table.*
1b. **No cash-register language (RULE 1):** scan EVERY readable string — headline, subcopy, artifact text, sticky note, chat bubble, receipt, Z-report, margin note, shock-word. Never the 4-letter register word (t-i-l-l), "cash tin"/biscuit-tin/shoebox-of-cash, or old cash-register framing. Use cashier/checkout/POS/counter ("cash drawer" OK).
1c. **No Americanisms (RULE 1):** Malaysian/British spelling, vocabulary AND idiom — scan against the tables in `malaysian-english-voice.md`. (colour not color; queue not line; shop/outlet not store; sen not cents; "took off" not "blew up"; no "reach out"/"game-changer"/"awesome".) Brand/feature names stay verbatim.
2. **Setting reads upmarket (RULE 2):** aspirational, well-lit, tidy, the merchant clearly doing well. NO roadside mamak / kopitiam / hawker / food-court / wet-market stall, plastic stools, bare-bulb or fluorescent-strip lighting, run-down interior, or cash tin. Mess is confined to the pain artifact (drawer/chits), never the venue. If it could read low-income at a glance → regenerate.

**Then the standard checks:**
3. **Safe band:** headline ends ≤ y 1090, CTA ends ≤ y 1400, logo top ≥ y 270, nothing important in the bottom 500px. Longest headlines (CR-01.A1, A2/A4 equations) get a deliberate line break / size-down.
4. **Subcopy matches the theme's chosen phrase:** CR-01/HC-06/BW-09 = "From chaos to control"; CR-02 = "From clutter to clarity".
5. **Compliance (§5):** no competitor/third-party logos or real app/POS/bank/govt UI; no Jata Negara/seal/letterhead; no WhatsApp green/ticks; receipt/Z-report header is the fictional shop or StoreHub only; photos scrubbed of incidental delivery-app branding; "Illustrative — not real" microcopy on govt/bank artifacts.
6. **Logo spelling:** every giant-word and artifact-text render reads **"StoreHub"** exactly — never ScoreHub / Store Hub / Score Hub.
7. **Lanes are distinct:** V1 photo ≠ V2 artifact ≠ V3 *pure type* (no object in V3). If V3 contains a thing, it belongs in V2.
8. **Brand:** Barlow headline is the biggest element; Orange `#ff9419` CTA; no orange+green; Pan-Asian faces only; gradient on V1/V2 only.
9. **Market:** MY price chip "From RM3.40/day" + MY phrases. PH/TH runs must swap the chip and revalidate phrases.
