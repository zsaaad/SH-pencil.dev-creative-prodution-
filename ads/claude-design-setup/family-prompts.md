# Claude Design — Family Prompts (8 families)

Eight self-contained paste-blocks. Each yields all variants × 3 ratios. All copy is policy-compliant (no GrabFood / FoodPanda / ShopeeFood naming).

> **Rendered words follow `malaysian-english-voice.md` (non-negotiable):** Malaysian / British English only — no American spelling, vocabulary, or idiom (colour not color, queue not line, shop/outlet not store, "took off" not "blew up"); never the cash-register word (use cashier / checkout / POS / counter); render only the copy given in each family block — never echo loose source-note wording. Brand + official feature names stay verbatim.

**Why 8 families now (up from 4):** the original 4 families (T5, T11, T7, T12) leaned on patterns we've already shipped many times — split-screens, "Your X. Our tech." gradient overlays, cream stat cards. They started to look like "every other StoreHub ad." Families 5–8 introduce wildly different visual grammars drawn from the AdFolio pattern library — bold-colour object metaphors, single-word typography, direct identity call-outs, and deliberate restraint. Mix across families when launching a batch — don't run 3 ads from the same family back-to-back.

**Recommended order:**
1. **Family 1 — T5 Competitive Contrast** (calibrated already, C007 proven)
2. **Family 2 — T11 Artifact Native** (highest historical performer)
3. **Family 6 — Audacious Typography** (pattern-breaks the rotation early)
4. **Family 5 — Visual Metaphor Pop** (no-people object-led; visual reset)
5. **Family 7 — Identity Call-Out** (voice-led; direct address)
6. **Family 3 — T7 Cultural Pride** (local food + heritage)
7. **Family 4 — T12 Milestone Math** (rewritten for variety)
8. **Family 8 — Wildcards / Restraint** (last; deliberate weirdness)

**Variant scope per family:** F1 (3) · F2 (4) · F3 (3) · F4 (3) · F5 (3) · F6 (3) · F7 (3) · F8 (3) = **25 variants × 3 ratios = 75 frames.** Run any subset — don't feel obligated to produce all 75 in one batch. A healthy rotation pulls 6–8 winners across at least 4 different families.

**For every prompt below, Claude Design should produce:**
- One frame per variant at 1080×1080
- Same frame redrawn at 1920×1080 (landscape — recompose, don't stretch)
- Same frame redrawn at 1080×1920 (vertical — recompose, don't stretch)
- Logo top-right inside safe zone (orange wordmark on light BG, white on dark/orange)
- Rounded orange CTA pill, Open Sans Bold ALL CAPS, "BOOK A FREE DEMO NOW"
- Brand colours strictly: Orange `#ff9419`, Black `#2f2922`, accents Pink `#ff546f` / Bold Orange `#ff630f` / Azure `#2a6ee8` only
- Headlines in Barlow Black 900 (largest element), sub in Open Sans SemiBold 70% of headline, body in Open Sans Regular 50–60% of headline
- Pan-Asian faces only where humans appear; never Western
- Never name GrabFood, FoodPanda, ShopeeFood, Grab, Lalamove, Pickupp, or any competitor — use the generic terms below

---

## Family 1 — T5 Competitive Contrast (3 variants × 3 ratios = 9 frames)

> **Family pattern:** Visual split — chaos / pain state on the left or top, calm / StoreHub solution on the right or bottom. Single concept that says "this manual + scattered way vs the StoreHub way."
>
> **Visual rule:** the StoreHub side always dominates the eye via brand orange `#ff9419`. The pain side is dark, desaturated, or grey.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `everest-metaphor` (the "expected to lose" control)**
>
> - Top zone (60%): AI image of a Pan-Asian climber, dirt on face, gripping snowy rock face, dramatic grey-blue sky. Beautiful but heavy.
> - Bottom zone (40%): warm cream `#fff8ea` background with text.
> - Headline (Barlow Black, dark): "Running a restaurant shouldn't feel like climbing Everest."
> - Sub-headline (Open Sans SemiBold): "One dashboard. From RM3.40/day."
> - Body bullets (Open Sans Regular): Manual stock counts · Delivery apps to juggle · Paper receipts · Late-night reconciliation.
> - CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark on the dark sky portion.
>
> ---
>
> **Variant 2 — `midnight-or-30-seconds` (split-screen)**
>
> - Two-panel split, 50/50 vertical division.
> - **Left panel:** AI image — Pan-Asian merchant late at night in a storeroom, clipboard + calculator under a dim bulb, "FRAGILE / KEEP DRY" cardboard boxes around. Exhausted look. Cool blue tone.
> - **Right panel:** clean orange `#ff9419` background with an illustrated StoreHub POS tablet showing inventory dashboard, "Stock auto-counted" tag, green check.
> - Headline below image area (Barlow Black): "Midnight. Or 30 seconds."
> - Sub-headline (Open Sans SemiBold): "Automated inventory. Done."
> - CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark on right panel orange.
>
> ---
>
> **Variant 3 — `six-vs-one` (use the calibrated layout from compliant C007)**
>
> - Two-panel split, 50/50.
> - **Left panel (dark `#2f2922` background, "6 TOOLS" label top):** 6 desaturated grey rounded-square tiles, each labelled with **generic** category names only — never brand names:
>   1. "Delivery apps" (scooter icon)
>   2. "Spreadsheets" (chart icon)
>   3. "Messaging" (chat bubble icon)
>   4. "Manual POS" (receipt icon)
>   5. "Paper receipts" (printer icon)
>   6. "Old systems" (clock icon)
> - **Right panel (orange `#ff9419` background, "1 SYSTEM" label top, StoreHub wordmark top-right corner):** clean illustration of a StoreHub POS tablet showing dashboard with line items and an orange "RM23.90" pill.
> - Below image area (cream BG): Headline (Barlow Black, dark with orange highlight on "Or 1."): "6 tools. **Or 1.**"
> - Sub-headline (Open Sans SemiBold, grey): "All-in-one POS system."
> - CTA pill: orange, BOOK A FREE DEMO NOW.

---

## Family 2 — T11 Artifact Native (4 variants × 3 ratios = 12 frames)

> **Family pattern:** Ad mimics a familiar non-ad UI artifact (job classifieds, group chat, review card, bank statement). The artifact reveals the StoreHub line halfway through. Highest scroll-stop in cold acquisition because it doesn't look like an ad.
>
> **Visual rule:** artifact chrome must be pixel-accurate to the genre — not StoreHub-branded. The StoreHub reveal is a single orange line that breaks the artifact pattern.
>
> **Generate 4 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `hiring-ad-v2` (job-classifieds chrome)**
>
> - Render as a JobStreet / Indeed-style listing on light grey background. Top bar: "JOB LISTING · Posted 2 hours ago". Pagination dots.
> - Job title (largest, Barlow Black inside the artifact): "One person who can do the work of five systems"
> - Job description block (Open Sans Regular, looks like real job-post body): "Manage POS across 2 stores, inventory, loyalty programme, delivery orders, daily reconciliation, monthly reports. Salary: RM4,800/mth."
> - One row breaks the pattern — orange `#ff9419` highlighted: **"OR — StoreHub POS from RM3.40/day does all of it."**
> - Below the artifact (white BG): Real headline (Barlow Black): "Hiring a human or a system?" Sub: "StoreHub from RM3.40/day." CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right corner of the white frame, not inside the artifact.
>
> ---
>
> **Variant 2 — `staff-whatsapp` (group chat chrome)**
>
> - Pixel-accurate WhatsApp group chat UI. Green `#25D366` header bar "Restaurant Bosses 🍜 · 4 members". Beige `#ECE5DD` wallpaper.
> - 6–7 chat messages (white incoming bubbles + `#DCF8C6` outgoing). Sarah, Akmal as names. Sample messages:
>   - "Sarah: Stock count off lah... 2 boxes chicken missing 😩"
>   - "Akmal: Same! Still waiting for today's total at 11:47PM"
>   - "Sarah: Every night same story"
> - One incoming message breaks the pattern — orange-tinted bubble: **"Wait — StoreHub POS closes the day automatically. Real-time reports. Zero manual reconciliation. From RM3.40/day."**
> - Below the chat artifact (white BG): Headline (Barlow Black): "When 'tomorrow' becomes every night." Sub: "Auto daily close. RM3.40/day." CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right corner of the white frame.
>
> ---
>
> **Variant 3 — `google-review` (review-card chrome)**
>
> - Google-review-style card on light grey background. Avoid the actual Google logo — use a generic reviewer avatar circle.
> - Reviewer name: "Binq Dessert · Local Guide". Location pill: "Hartamas · SS15 · SS2". Posted: "3 weeks ago". Yellow 5-star row `#FBBC04`.
> - Review body (Open Sans Regular): "Switched from our old POS 6 months ago. Queue times cut in half. Staff save 2 hours every night on closing. Inventory across 3 outlets finally reconciles. Only regret: we didn't do it sooner."
> - Small attribution line: "Reviewing: StoreHub POS"
> - Below the card (white BG): Headline (Barlow Black): "The review you'll leave in 6 months." Sub: "20,000+ merchants. 1 POS." CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right corner of the white frame.
>
> ---
>
> **Variant 4 — `month-end-receipt` (bank-statement chrome)**
>
> - Bank-statement / accounting artifact on white. Use a monospace font (Roboto Mono or JetBrains Mono) for line items — genre-correct.
> - Header (black bar): "MONTHLY BUSINESS EXPENSES · MARCH 2026"
> - Left-aligned items + right-aligned RM amounts:
>   - Delivery app commissions ............... RM 5,700.00
>   - Manual reconciliation .................. RM 1,150.00
>   - Stock write-offs ....................... RM   680.00
>   - Admin overhead ......................... RM   220.00
> - Bold total row in `#ff630f` (red-orange): "TOTAL BLEEDING ................. RM 7,750.00"
> - Highlighted row in brand orange `#ff9419` below total: "StoreHub POS ...................... RM   408.00"
> - Below the statement: Headline (Barlow Black): "Which line are you cutting?" Sub: "See what you're really paying." CTA pill: orange, BOOK A FREE DEMO NOW.
> - Logo: top-right corner of the white frame.

---

## Family 3 — T7 Cultural Pride (3 variants × 3 ratios = 9 frames)

> **Family pattern:** "Your {local thing}. Our tech." Local food + local context = scroll-stop in SEA. Full-bleed environment photo with bottom 40% gradient overlay; white headline reads cleanly.
>
> **Visual rule:** Pan-Asian merchants and customers only. Real, specific local food and shop type. Never staged. Subtle StoreHub tablet may be in frame edge — never hero.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `kopitiam` (Malaysian Chinese coffee shop)**
>
> - Full-bleed AI photo: overhead shot of a marble modern cafe table. Kaya toast on plate. Two soft-boiled eggs in classic saucer with white pepper + dark soy. Kopi-O in blue-rim mug. Patrons' hands in background.
> - Bottom 40% gradient overlay (`#2f2922` 0 → 87% opacity).
> - Headline (Barlow Black, white): "Your kopi. Our tech."
> - Sub-headline (Open Sans SemiBold, white): "Built for Malaysian F&B."
> - CTA pill (orange, white text): BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark on the photo.
>
> **Stop-condition before launch:** confirm landing page CTA reads "Book your free demo" — must match ad CTA or this loses (Batch 1 T7 root cause).
>
> ---
>
> **Variant 2 — `mamak-2am` (Indian-Muslim 24h restaurant)**
>
> - Full-bleed AI photo: packed modern restaurant interior at night. Roti canai mid-toss caught in motion. Patrons at marble tables. Warm yellow ambient lighting. Generic signage in background ("ROTI CANAI · TEH TARIK · NASI KAND...") — do NOT use any real shop name on signage.
> - Bottom 40% gradient overlay (`#2f2922` 0 → 87% opacity).
> - Headline (Barlow Black, white): "2am at your mamak."
> - Sub-headline (Open Sans SemiBold, white): "POS that runs when you do."
> - CTA pill (orange, white text): BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark.
>
> ---
>
> **Variant 3 — `steamboat` (Chinese hot-pot restaurant)**
>
> - Full-bleed AI photo: vibrant packed Chinese hot-pot restaurant. Red lanterns hanging overhead. Central steaming hot-pot on the table. Multiple Pan-Asian families dining. Chinese signage in soft focus background — use generic decorative Chinese characters, NOT a real restaurant name.
> - Bottom 40% gradient overlay (`#2f2922` 0 → 87% opacity).
> - Headline (Barlow Black, white): "Your steamboat. Our tech."
> - Sub-headline (Open Sans SemiBold, white): "Table orders. Split bills. Inventory. From RM3.40/day."
> - CTA pill (orange, white text): BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark.

---

## Family 4 — T12 Milestone Math (3 variants × 3 ratios = 9 frames) — REWRITTEN FOR VARIETY

> **Family pattern:** Confront the merchant with their numbers. Same thesis (cost contrast) — three visually distinct executions so the rotation doesn't read as three versions of the same stat card.
>
> **Anti-template rule:** No two variants share the same background colour, layout grammar, or compositional centre of gravity. If two of these come back looking like cousins, the prompt failed.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `opening-week-on-bold` (cost card on confident colour, NOT cream)**
>
> - Background: **bold orange `#ff630f`** full-bleed (not cream — breaks the standard StoreHub cream-card pattern).
> - White card centred, slight drop shadow, title (Barlow ExtraBold black): "OPENING WEEK EXPENSES"
> - Line items inside the card (Open Sans SemiBold black labels, right-aligned tabular numerals):
>   - Renovation ........................... RM 48,000
>   - Kitchen equipment .................... RM 25,000
>   - Signage .............................. RM  3,500
>   - Staff training ....................... RM  1,200
>   - Insurance ............................ RM    850
> - One row highlighted in brand orange `#ff9419` with white text: "POS system (StoreHub) ......... RM 102/week"
> - Below the card on the bold orange BG, in **Caveat italic (handwritten accent) white**: "One of these pays you back."
> - Headline below (Barlow Black white, sentence case): "You saved where it counted."
> - CTA pill: dark `#2f2922` background with white text (reverses against the orange BG instead of the standard orange-on-cream pill). "BOOK A FREE DEMO NOW".
> - Logo: top-right, **white wordmark** (because BG is bold orange).
>
> ---
>
> **Variant 2 — `year-2-cinematic-shopfront` (full-bleed photo, no stat-card cousin)**
>
> - Full-bleed cinematic AI photo. Concept: small Malaysian shopfront from across a rainy street at dusk. Lights off inside. Faded "For Lease" notice in the window. Single Pan-Asian figure with umbrella walking away. Cool blue-grey tones. Dramatic but not horror. **Background detail only — no close-up faces.**
> - Bottom 45% gradient overlay `#2f2922` 0 → 90% opacity for legibility.
> - Headline top-left (Barlow Black, white, 2 lines): "Year 1: you survived."
> - Sub-headline directly below (Open Sans SemiBold, white): "But at what cost?"
> - **No stat cards.** Instead: a single line of small white tabular text bottom-centre — "Year 1 delivery commissions: RM 21,900   ·   Year 2 with StoreHub: RM 1,240"
> - Final line (Open Sans SemiBold, white italic): "Same business. Different system."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW. Bottom inside safe zone (y ≤ 1400 on 9:16).
> - Logo: top-right, white wordmark.
>
> **Pre-launch gate:** Finance must approve the RM 21,900 vs RM 1,240 figures before any spend. Claim defensibility.
>
> ---
>
> **Variant 3 — `receipt-is-the-ad` (thermal-printer receipt as the entire canvas — full Artifact-as-Hero)**
>
> - Light beige paper-texture background (`#f4ecd9`).
> - **A thermal-printer receipt fills ~90% of the canvas**, slight curl shadow, faint paper grain. The receipt IS the ad — no traditional headline outside it.
> - Receipt content in monospace (Roboto Mono or JetBrains Mono), centre-aligned where possible, left-aligned for line items:
>
> ```
>           STOREHUB DEMO RECEIPT
>             Date: 04/06/2026
>     ------------------------------------
>     1× cash drawer panic ........ RM  0.00
>     1× midnight reconciliation .. RM  0.00
>     1× kid's school recital ..... REFUNDED
>     1× peace of mind ............ INCLUDED
>     ------------------------------------
>           TOTAL .... RM 3.40/day
>          THANK YOU FOR SWITCHING
> ```
>
> - Tiny CTA pill bottom (orange `#ff9419`, white text), sitting on the beige BG below the receipt edge: BOOK A FREE DEMO NOW.
> - Logo: orange wordmark top-right, outside the receipt, sitting on the beige.
> - **No conventional headline.** The receipt does the storytelling. The CTA is small because the artifact is the message.
>
> ---

## Family 5 — Visual Metaphor Pop (3 variants × 3 ratios = 9 frames) — NEW

> **Family pattern:** Single bold object on a confident solid colour. No merchant photos. No StoreHub hardware. No "Your X. Our tech." gradient overlay. Pure visual idiom + 2-line typography. Breaks every "StoreHub ad" pattern.
>
> **Anti-template rule:** the object IS the metaphor — don't add explainer iconography. Headline is short (≤6 words), Barlow Black, dominates upper third.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `broken-hammer`**
>
> - Background: solid pink `#ff546f`.
> - Hero: photo (or photoreal CG) of a wooden-handled hammer with the head snapped clean off, lying centred on the pink with soft natural shadow.
> - Headline (Barlow Black 140pt, white, centred above the hammer): "Cheap POS systems are expensive."
> - Sub-headline (Open Sans SemiBold, white, below hammer): "RM3.40/day. Not a discount — a category."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW, bottom.
> - Logo: top-right, white wordmark.
>
> ---
>
> **Variant 2 — `vintage-crt-tv-with-teh-tarik`**
>
> - Background: cream `#fff8ea`.
> - Hero: photoreal 1980s wood-grain CRT TV with rabbit-ear antenna, centred. A small bottle (or glass) of teh tarik balanced precariously on top. Soft directional light. Object-only — no people.
> - Headline (Barlow Black 110pt, **orange `#ff9419`**, top): "Some traditions stay."
> - Sub-headline (Barlow Black 90pt, black, below): "Your POS shouldn't."
> - Tiny body line (Open Sans Regular, dark grey): "Modern POS for modern shops. From RM3.40/day."
> - CTA pill: dark `#2f2922` background with white text (so it doesn't disappear into the cream).
> - Logo: top-right, orange wordmark.
>
> ---
>
> **Variant 3 — `wobbly-kopitiam-chair`**
>
> - Full-bleed photographic modern cafe interior. Warm fluorescent light. Marble table mid-frame. One red plastic chair dramatically tilted at 30° as if about to fall. Slight motion blur on a customer passing. Documentary feel.
> - Bottom 30% dark `#2f2922` gradient overlay for text legibility.
> - Headline (Barlow Black 110pt, white, bottom area): "Closing time gone sideways?"
> - Sub-headline (Open Sans SemiBold, white): "StoreHub steadies the counter in 24 hours."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW.
> - Logo: top-right, white wordmark.

---

## Family 6 — Audacious Typography (3 variants × 3 ratios = 9 frames) — NEW

> **Family pattern:** Typography IS the visual. One word or short phrase fills 50–70% of the canvas at a confidently oversized scale. Background is a single bold colour. Minimal supporting visual. The headline has to earn its size — no soft language.
>
> **Anti-template rule:** no product mockups, no hardware shots, no merchant photos. Just colour, type, maybe one tiny supporting element. If the headline could shrink without losing impact, it's too small.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `susah` (single Bahasa word — Malaysian cultural code)**
>
> - Background: solid black `#2f2922`.
> - Headline (Barlow Black, **orange `#ff9419`**, centred, **massive — fills ~60% of canvas height**): "Susah."
> - Sub-headline (Open Sans SemiBold 32pt, white, below the giant word): "Manual close-out. Tally cash by hand. Stock count Sunday."
> - Tiny body line (Open Sans Regular, white): "RM3.40/hari je. Untuk POS yang faham."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW, bottom inside safe zone.
> - Logo: top-right, white wordmark — small, above the giant "Susah." but inside the safe zone (y ≥ 250 on 9:16).
>
> ---
>
> **Variant 2 — `what-the-stock` (pun headline + geometric background)**
>
> - Background: purple `#9F7BFF` with sparse abstract geometric shapes — 3–5 floating black circles, triangles, ovals scattered (NOT crowded — restraint matters).
> - Headline (Barlow Black, black, centred, 2 lines, **massive**): "WHAT THE / STOCK?"
> - Sub-headline (Open Sans SemiBold 32pt, black): "Track every plate, every cup, every kuih. No more surprises."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW.
> - Logo: top-right, **black** wordmark (purple BG is light enough that black reads cleanly).
>
> ---
>
> **Variant 3 — `552-hours` (giant-number-as-headline)**
>
> - Background: mint green `#D9F4E8` (cool, calm — contrasts with the bleed implied by the number).
> - Headline (Barlow Black 220pt, **black**, centred): "552 hours."
> - Sub-headline (Open Sans SemiBold 36pt, black, directly below): "What you bled last year on manual reconciliation."
> - Body (Open Sans Regular, black): "Get those hours back. From RM3.40/day."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW.
> - Logo: top-right, **orange** wordmark (mint BG calls for orange to anchor brand).

---

## Family 7 — Identity Call-Out (3 variants × 3 ratios = 9 frames) — NEW

> **Family pattern:** Direct second-person address. The headline is a stacked multi-line phrase that names the reader's specific situation. No product copy at the top — empathy first, product later. Tonally adjacent to a friend texting, not a brand selling.
>
> **Anti-template rule:** stack the headline vertically across 3–5 lines using Barlow Black at a confidently large size (left-aligned, not centred). The line breaks ARE the rhythm. Don't normalise to a single line.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `if-youve-ever-counted-twice`**
>
> - Background: cream `#fff8ea`.
> - Layout: left 55% text, right 45% AI photo of a Pan-Asian merchant hand holding a calculator at a marble modern cafe counter — close crop, low golden light. Hand only or partial profile, no full face.
> - Headline (Barlow Black 80pt, black, left-aligned, **4 stacked lines**):
>   `If you've ever`
>   `counted the cash drawer twice`
>   `and still felt unsure,`
>   `this is for you.`
> - Tiny body line below (Open Sans SemiBold): "StoreHub flags every discrepancy in real time. From RM3.40/day."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW, bottom-left.
> - Logo: top-right, orange wordmark.
>
> ---
>
> **Variant 2 — `hey-kopitiam-owner` (intimate dark-bg direct address)**
>
> - Background: deep navy `#0F1B3D`. Behind the text, a very faint orange `#ff9419` cursor-arrow / loop trail at 15% opacity — barely there, just texture.
> - Headline (Barlow Black 90pt, white, left-aligned, **5 stacked lines**):
>   `Hey kopitiam owner,`
>   `your wife told us`
>   `you spend Sundays`
>   `counting cash.`
>   `Want a different Sunday?`
> - No sub-headline. The headline IS the entire pitch.
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW, bottom inside safe zone.
> - Logo: top-right, white wordmark.
>
> ---
>
> **Variant 3 — `wanted-classifieds-impossible-job`**
>
> - Background: magenta `#E63B7E`.
> - Headline (Barlow Black 120pt, white, **all caps**, centred top): "WANTED: ONE HUMAN (MUST BE FOUR)."
> - Body block (Open Sans Regular, white, centred, smaller):
>   `Manages POS. Inventory. Loyalty.`
>   `Reports. Never sleeps. Never gets sick.`
>   `Salary: RM900/month.`
> - Final line below (Barlow Black, **orange `#ff9419`**, 1 line): "OR: StoreHub. RM3.40/day."
> - CTA pill: black `#2f2922` background, white text (against the magenta BG, orange pill would clash).
> - Logo: top-right, white wordmark.

---

## Family 8 — Wildcards / Restraint (3 variants × 3 ratios = 9 frames) — NEW

> **Family pattern:** Each variant deliberately breaks a different "StoreHub ad" convention. Pattern-interrupt is the goal. These are the variants the strategy team will instinctively want to cut — keep them.
>
> **Anti-template rule:** if a variant looks like it could blend into an existing StoreHub batch, it failed the brief. Restraint, weirdness, or aesthetic specificity are the test.
>
> **Generate 3 variants, each at 1080×1080, 1920×1080, and 1080×1920.**
>
> ---
>
> **Variant 1 — `empty-canvas-restraint` (the "we said nothing" ad)**
>
> - Background: pure cream `#fff8ea`. **No photo. No graphic. No card.**
> - Single tiny line dead-centre (Open Sans Italic 24pt, soft grey `#7a7672`):
>   "An ad goes here. We thought a free Sunday was a better gift."
> - Small orange CTA pill bottom-right (inside safe zone): "BOOK A FREE DEMO NOW".
> - Logo: top-right, small orange wordmark.
> - **The whitespace IS the ad.** Don't add anything else. Even decorative orange. Even a soft border. Resist.
>
> ---
>
> **Variant 2 — `risograph-print-poster` (aesthetic specificity)**
>
> - Background: cream `#fff8ea`.
> - All visual elements rendered in **risograph print aesthetic**: slight off-register orange `#ff9419` + black `#2f2922` only, ~2% texture grain, slight ink mottle.
> - Centred: a line illustration in risograph style of a Pan-Asian merchant at a modern cafe counter with a tablet. Stylised, flat, no shading.
> - Headline (Barlow Black 90pt, black, top): "A POS that looks like a poster on your wall."
> - Sub-headline (Open Sans SemiBold, black): "Form. Function. From RM3.40/day."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW.
> - Logo: top-right, orange wordmark.
> - **Tonal target:** indie zine / Risograph art print / Tokyo café poster — not corporate SaaS.
>
> ---
>
> **Variant 3 — `chalkboard-menu-with-punchline` (familiar artifact, dark surprise)**
>
> - Background: full-bleed photographic chalkboard — slightly dusty, real chalk texture, slight glare.
> - Hand-chalked menu (Caveat-style or actual chalk hand-lettering), white chalk on black, left-aligned:
>   `Kopi-O ............ RM 2.00`
>   `Kopi-C ............ RM 2.50`
>   `Teh Tarik ......... RM 3.20`
>   `Roti Bakar ........ RM 3.50`
>   `Sales last night .. ???`
> - The last line in **orange chalk** (`#ff9419`).
> - Headline above the menu (Barlow Black 70pt, **orange chalk-textured**, white outline): "One line you should always know."
> - CTA pill: orange `#ff9419`, BOOK A FREE DEMO NOW, bottom inside safe zone.
> - Logo: top-right, white wordmark.

---

## Production checklist (apply to every output)

- [ ] All copy contains zero competitor names — Grab / FoodPanda / ShopeeFood / Lalamove etc.
- [ ] All 3 ratios produced per variant — square / landscape / vertical (not stretched, recomposed)
- [ ] CTA pill present, orange `#ff9419`, ALL CAPS "BOOK A FREE DEMO NOW"
- [ ] Logo top-right within safe zone, correct colour variant for background
- [ ] StoreHub spelt correctly — one word, mid-cap H — on every frame
- [ ] Barlow Black headline is the largest element on every frame
- [ ] Pan-Asian faces only where humans appear
- [ ] No "ScoreHub" / "Score Hub" / "Store Hub" anywhere on any frame
- [ ] Brand colours match exact hex (`#ff9419` orange, `#2f2922` black) — not visually similar approximations
- [ ] Numbers and claims are defensible (RM21,900 vs RM1,240 needs finance sign-off; testimonials need merchant release)
