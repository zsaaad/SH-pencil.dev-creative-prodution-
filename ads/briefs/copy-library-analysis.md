# MY Ad Copy Library — Structural Analysis

**Source:** `Input Files/Ad Copy Library - Performance Team - MY Ad Captions.csv` (20,093 lines, ~810KB)
**Analysed:** 2026-04-30
**Purpose:** Distil the StoreHub MY Performance Team's house copy style into a reusable formula library so the `ad-copy-generator` agent can write new captions without re-reading the raw CSV.

The CSV is the historical living archive of every Meta/Google caption the StoreHub MY Performance Team has shipped — typically 2 or 3 caption variants per concept, paired with 2–5 short headlines and 1–2 descriptions, in three columns: **EN · CN (Simplified) · MS (Bahasa Malaysia, Manglish-leaning)**.

---

## 1 · File schema

```
H4,Ad Creatives Library - Performance Team,,,,
,EN,CN,MS,Creative link
{row#},"<EN block>","<CN block>","<MS block>","<creative ref name>"
```

Every concept block typically contains:

```
[<Concept Name / Promo Tag>]

Caption 1
<hook>
<body bullets>
<offer line>
<CTA>

Caption 2
…

Caption 3
…

Headline 1: <short>
Headline 2: <short>
Headline 3: <short>          ← 2 to 5 short headlines
Headline 4: <short>

Description: <social-proof or offer line>
```

A `-` token in any language column means "no copy in this language for this concept".

---

## 2 · Recurring hook archetypes

Across the dataset, EVERY caption opens with one of these eight hook patterns. Copy agents should pick the hook archetype first, then write the body around it.

| # | Hook archetype | English example | MS (Manglish) example |
|---|---|---|---|
| H1 | **Audience callout (megaphone)** | `📣 Restaurant owners! 📣` | `📢 Hai owner-owner restoran!` |
| H2 | **Pain question** | `Tired of slow service and missed orders?` · `Is your POS slowing you down? 🐢` | `Pening nak urus banyak sistem?` · `Penat layan sistem kedai lama yang slow?` |
| H3 | **Cost question** | `How much are you paying in delivery fees?` · `Are you tired of dealing with slow customer support?` | `Berapa kos sebenar bisnes korang?` |
| H4 | **Stat / authority** | `15,000+ F&B merchants trust us with our POS — why don't you?` | `Lebih 15,000 perniaga di 3 negara percayakan POS kami` |
| H5 | **Promo lead** | `Psst… for a LIMITED TIME, StoreHub POS is up to 80% off!` | `Sekarang StoreHub tengah buat promo kawwww kawwww!` |
| H6 | **Story / scenario** | `Dah lewat malam, Bos masih stress kira sales 😫` · `Lunch rush at your café = chaos?` | `Tengah tak menang tangan, tiba-tiba sistem POS 'buat hal'?` |
| H7 | **Merchant quote** | `"It's simple to use, yet packed with features."` · `"The uptime is always there."` | `"Memang menjimatkan kos kita sebab tak perlu guna ramai staff macam dulu."` |
| H8 | **Holiday / milestone tie-in** | `🎄 Christmas rush coming? No problem.` · `Opening a new restaurant?` | `🎉 Nak buka kedai butik bulan depan?` · `Jangan biarkan Raya tutup kedai korang!` |

Cross-reference to `config/creative_themes.json`:
- H2/H3 ↔ T1 Pain Amplification, T9 Hidden Cost
- H4 ↔ T6 Social Proof
- H5 ↔ T4 The Math (when paired with hard numbers)
- H6 / H7 ↔ T11 Artifact Native (chat / story / quote rendered as artifact), T6 Social Proof
- H8 ↔ T2 New Chapter, T12 Milestone Math

---

## 3 · Body scaffold (the 3-bullet to 7-bullet ladder)

Every caption uses a **3-to-7 emoji-led bullet block** between the hook and the CTA. The bullets are not feature lists — they are framed as benefits or actions the merchant gets back.

```
✅ Order & pay via QR code — Fast & easy!
✅ Cashback System & Loyalty Program
✅ Automatic SMS marketing
✅ Stock management system
✅ Track daily, weekly, monthly & yearly sales easily
✅ Run your own food delivery service
✅ 30+ functions and more!
```

Conventions across all three languages:
- **One line per bullet.** If it wraps, rewrite shorter.
- **Lead with an emoji** — typically `✅`, `📊`, `📦`, `💳`, `🚀`, `📱`, `💪`, `⚡`, `🎯`.
- **Max ~50 characters per bullet.**
- **Keep bullets parallel** — same verb tense, same length cadence.
- **Plain Sentence case**, not Title Case.

The bullet feature catalogue (any new copy can mix-and-match these — they're the proven message ground-truth):

| Bullet | Underlying product | Used in CSV |
|---|---|---|
| `📲 QR Order & Pay — fast & easy!` | QR Order & Pay | 100s of times |
| `📦 Stock / Inventory management` | BackOffice inventory | Constant |
| `💳 Cashback & Loyalty Program` | Loyalty + Membership | Constant |
| `📱 Automatic SMS marketing` | Engage / Auto SMS | Constant |
| `📊 Real-time sales reports` | BackOffice reports | Constant |
| `🚚 Run your own food delivery (Beep)` | Beep Delivery | Constant |
| `👥 Employee / staff management` | Employee Management | Frequent |
| `📸 AI Face Capture clock-in` | New AI feature | Recent (2025+) |
| `🧾 E-invoicing ready (LHDN)` | Compliance | Recent (2024+) |
| `🛒 Shopee / Lazada / TikTok integration` | Marketplace sync | Recent |
| `⭐ 7-day customer support` | Live Chat | Constant |
| `🏠 Manage from anywhere (mobile)` | Cloud BackOffice | Constant |
| `💼 Multi-store / multi-outlet sync` | Multi-location | Frequent |

If a body block contains more than 7 bullets it has aged badly — modern (2025+) winners cap at 3–5.

---

## 4 · Offer / proof line (sandwiched between body and CTA)

Most evergreen captions slot a single short offer or proof line between the bullets and the CTA:

- `Trusted by 20,000+ merchants across SEA.` (current — confirmed 2026-04-30)
- `Up to 55% OFF hardware. While supplies last.` (current promo, 2026)
- `From RM3.40/day. Hardware included.` (MY price anchor)
- `From ₱63/day. Hardware included.` (PH price anchor)
- `Backed by 7-day live support.` (service proof)
- `BIR-accredited.` (PH compliance proof)
- `LHDN-compliant e-invoicing built in.` (MY compliance proof)
- `Used by Grub, Binq, Coffeeboy Club and 20,000+ more.` (named-merchant proof)

Stats progression visible in the dataset over time: `15,000+` (2023) → `17,218` (early 2025) → `18,000+` (mid 2025) → `20,000+` (current, 2026). Use `20,000+` as the default — it is the confirmed current StoreHub merchant count across SEA.

---

## 5 · CTA conventions

Every caption ends with **exactly one** CTA line. Variants seen, in order of frequency:

| Rank | EN | MS | CN |
|---|---|---|---|
| 1 | `Book a FREE demo today!👇` | `Tempah demo PERCUMA hari ni!👇` | `立即预约免费试用！👇` |
| 2 | `Sign up now, get a FREE demo with us.👇` | `Daftar sekarang & dapatkan demo PERCUMA!👇` | `立即注册并享有免费试用！👇` |
| 3 | `Claim 55% OFF + free demo today!` | `Dapatkan 55% OFF + demo PERCUMA hari ni!` | `领取55%折扣 + 免费试用！` |
| 4 | `Click below to learn more.👇` | `Klik untuk maklumat lanjut.👇` | `点击下方了解更多。👇` |

The on-image CTA button copy (separate from caption CTA) is always: **`BOOK A FREE DEMO NOW`** — ALL CAPS, on an orange (`#ff9419`) or pink (`#ff546f`) pill button. This is the locked button label across all batches.

---

## 6 · Short headlines (Meta / Google headline asset format)

Each concept ships with **2 to 5 short headlines** under 40 characters each. Patterns observed:

1. **Category claim** — `#1 POS for Restaurants & Retail`, `POS Built for F&B & Retail`
2. **Promo headline** — `55% Off StoreHub POS`, `Up to 55% OFF Hardware`
3. **Audience-narrowed** — `POS System for Cafés`, `Sistem POS untuk Kedai Butik`
4. **Identity / vibe** — `Built For Busy Shifts`, `From Chaos to Calm`, `Manage It All.`
5. **Punchy benefit** — `Save Time Managing Staff`, `Run Your Café Like a Pro`
6. **Localised slang** — `POS Yang Memang Padu`, `Urus Kafe Macam Pro`

Conventions:
- **4–7 words** typically.
- Title Case for EN headlines (this is the one place the system uses Title Case — body / sub-headlines / CTAs all use Sentence case or ALL CAPS per `config/brand.json`).
- MS headlines often Manglish or sentence case (`Tukar Ke StoreHub Hari Ni!`).
- CN headlines are often shorter and punchier than EN (`高效POS系统` / `升级你的咖啡馆`).

---

## 7 · Description line (Meta description format)

Always one short line, used for paid Meta description fields. Pattern: **proof or offer**.

- `Trusted by 20,000+ businesses` / `Dipercayai oleh 20,000+ perniagaan` / `受20,000+家企业信赖`
- `Backed by 7-day support` / `Sokongan 7 hari` / `7天客服支持`
- `From RM3.40/day` / `Dari RM3.40/hari` / `每日只需 RM3.40`
- `LHDN-ready e-invoicing` / `E-invois LHDN siap sedia`

---

## 8 · Tone of voice — concrete patterns

### English (EN)
- Direct address: `you`, `your business`, `your café`.
- Lead with the merchant's reality: `Tired of …?`, `Stop letting …`, `Stop guessing …`.
- Avoid corporate jargon. The CSV is full of phrases like "Stop the chaos", "Beat the rush", "Sleigh your revenue goals".
- Punchy two-clause sentence: `Less hassle. More time to grow.`

### Malay (MS) — the Manglish house style
This is the most distinctive register in the library and the one most easily lost by copy-generators that aren't anchored.

- Address the audience as **`korang`** (informal "you-all"), **`Bos`**, or **`anda`** (formal). `korang` is the default for Meta; `anda` for LinkedIn/B2B.
- Borrow English keywords intact: `sales`, `stock`, `customer`, `staff`, `slow`, `update`, `system`, `cashier`, `peak hour`, `loyalty`, `book demo`. Do NOT translate these — Malaysian SME owners code-switch this way.
- Local intensifiers: `kawwww kawwww` (huge), `gilerr` (crazy/intense), `gempak` (dope), `padu` (solid), `power`, `terbaik`, `setel`, `senang gila`.
- Empathy verbs: `pening`, `serabut`, `letih`, `stress`, `risau`, `kalut`.
- `Jom …` to invite. `Tak payah …` / `Jangan risau …` to comfort.
- Sample MS opening lines from the corpus:
  - `📢 Hai owner-owner restoran! Korang dah tak payah nak kalut atau risau …`
  - `Pening nak urus banyak sistem?`
  - `Dah lewat dah ni tapi Bos masih stress kira sales 😫`
  - `Tengah tak menang tangan, tiba-tiba sistem POS 'buat hal'?`

### Chinese (CN, Simplified)
- More formal than EN/MS.
- Open with audience callout `📢 餐厅老板们！` or rhetorical question `还在烦服务慢、漏单问题吗？`.
- Stat-led claims: `超过15,000家餐饮和零售商信任我们的POS系统`.
- Closes with `立即预约免费试用！👇` or `今天就预约免费DEMO！👇`.
- CN never uses Manglish-style code-switching — it stays in Mandarin.

### Forbidden across all languages (per `config/brand.json` tone_of_voice)
- ❌ Western cultural references
- ❌ Corporate jargon (`leverage`, `synergy`, `paradigm`)
- ❌ Stock-photo cheerfulness
- ❌ Exaggerated enthusiasm without specifics
- ❌ Calling competitors by name (PH-specific risk: never name GrabFood inside an artifact ad)

---

## 9 · Concept tagging conventions

Concepts are typically prefixed in the CSV with a bracketed tag that signals **what's being tested**:

- `[55% Off Promo]`, `[80% Off]`, `[S1 80% Off]`, `[S2+S3 80% Off]` — promo-phase tags
- `[<Merchant> VP1 / VP2 / VP3 …]` — Visual Proposition (testimonial-derived) tags. Multi-VP series like `[Hauntu VP1]…[Hauntu VP8]`, `[Coffeeboy Club VP1]…[VP5]`, `[Naug Just Plants VP1]…[VP6]`, `[Sate Rono VP1]…[VP3]`.
- `[Christmas]`, `[Raya Promo]`, `[CNY]` — holiday-tied
- `[Whatsapp Chat - Sales Reports]`, `[Whatsapp Chat - Inventory]` — artifact-format experiments (early T11 ancestors)
- `[Lunch time rush meme]`, `[Bulletproof]`, `[How It Feels To Manage Your Business]` — meme / format experiments
- `[Save Time]`, `[The ONLY POS]`, `[Fun Fact]` — feature-led
- `[New Business Promo]`, `[Opening Day Expenses]`, `[Dayana - Retail Starter Kit]` — milestone / new-biz
- `[Face Capture With AI]`, `[E-Invoicing]` — feature launches

The tag is the operational concept ID. When the agent generates new copy, it should mirror this tagging convention so output slots into existing analysis pipelines.

---

## 10 · What's UNDERUSED in the library (gaps the copy agent can fill)

By cross-referencing the CSV with `config/creative_themes.json`, these are valid copy directions that have minimal or no representation:

1. **T11 Artifact Native — non-WhatsApp artifacts.** The library has WhatsApp/Viber chat formats but very few job posts, receipts, BIR forms, Google reviews, SMS screens. Copy agent should prioritise these.
2. **T9 Hidden Cost — receipt/audit format.** Annual commission audits, P&L breakdowns, sticky-notes — barely present. Copy agent should write the artifact text BODY (the receipt lines, the Post-It text, the form fields) as part of the deliverable, not just the caption.
3. **T12 Milestone Math.** Specific milestone × specific number combos (Week 1 / 90 days / Year 2 + RM3.40-day or PHP63-day). The library has the math separately and the milestone separately, never fused.
4. **Cultural pride hero with native-language copy.** EN copy dominates, but the highest-CPL angles (Batch 1 winners) used cultural specificity. Copy agent should write ONE language at a time and avoid bilingual mash-ups inside one caption.
5. **Identity-first headlines** like `From Chaos to Calm` — these are visible in newer entries but earlier batches over-rely on `#1 POS` and `Trusted by 15,000+`.

---

## 11 · "House style" cheat sheet (for copy generation)

When generating new captions, the agent should hit at least 6 of these markers per Caption block:

1. ✅ Hook archetype is one of H1–H8 above
2. ✅ Audience name appears in the first sentence (`Restaurant owners`, `Owner kafe`, `餐厅老板`)
3. ✅ Body has 3–5 emoji-led bullets, 1 line each
4. ✅ Bullets describe outcomes/actions, not pure features
5. ✅ One offer or proof line between body and CTA (`From RM3.40/day` / `20,000+ merchants` / `55% off hardware`)
6. ✅ CTA matches the locked patterns in §5
7. ✅ Currency matches market (RM for MY, ₱ for PH, ฿ for TH)
8. ✅ Tone register matches language (`korang/Bos` for MS Manglish, `you` for EN, formal address for CN)
9. ✅ Caption ≤120 words (Meta primary text optimum)
10. ✅ At least one specific, verifiable number (price, merchant count, % off, hours saved, etc.)

---

## 12 · Source-data evolution to flag in copy

If the brief references stats, prefer the most recent values from the corpus:

- **Merchant count:** `20,000+` — current StoreHub merchant count across SEA, confirmed 2026-04-30. Older stats (`15,000+`, `17,000+`, `18,000+`) are out of date and should not be reused.
- **Country count:** `3 countries` is consistent across the corpus; do not invent 4.
- **Years operating:** `since 2014` for SH (founded 2014). Reference appears as "10 years" in early 2024 entries — recompute for the current year (2026 → "12 years").
- **Hardware tier names:** `D3 Pro` (flagship), `D3 Mini`, `Falcon 1`, `Falcon 2`, `Falcon Mini` (PH), `Sunmi D3 Pro` (legacy referent — current is `D3 Pro`).
- **Compliance proofs:**
  - MY: `LHDN-compliant e-invoicing` (added 2024)
  - PH: `BIR-accredited` (verify before claiming — Hard gate per PH-batch_001/production_prompt.md)

Older claims (e.g. `15,000+`, `RM399 hardware promo`, `S2+S3 80% off`) should not be reused in 2026 output unless the brief specifies a campaign retread.

---

## 13 · Length budgets (Meta / Google asset specs)

| Asset | Optimum length | Hard limit | Source format in CSV |
|---|---|---|---|
| Meta primary text (caption) | 90–125 chars before "See more" cuts off; full text up to ~125 words still reads | 2,200 chars | "Caption N" blocks |
| Meta headline | 27 chars before truncation on mobile | 40 chars | "Headline N" blocks |
| Meta description | 27 chars before truncation; 30 max optimal | 30 chars | "Description" line |
| Google RSA headline | 30 chars (per asset) | 30 chars | Same as Meta headline |
| Google RSA description | 90 chars (per asset) | 90 chars | One-line offer/proof |

The CSV blocks Headlines as 2-5 short headlines (4-7 words each) — this is the asset format. Copy agent should output them inside the same range.

---

## End of analysis. Refer to this file from `agents/ad-copy-generator.md`.
