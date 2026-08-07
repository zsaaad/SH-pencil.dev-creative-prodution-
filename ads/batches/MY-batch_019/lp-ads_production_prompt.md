# LP-Ads Build Brief v2 — 3 ad variations per interactive landing page (18 frames, 9:16, MY)

_v2 after the 2-critic round; deltas in `crit-and-final.md`. This file is the production prompt._

**Job:** For each of the 6 interactive experience landing pages, build 3 ad frames (lanes V1/V2/V3), 1080×1920. The ad's art must **message-match the LP's first frame** — the LP's mechanic is visible in the ad (playbook §8: "the ad's last frame should look like the LP's first frame"). Market = MY.

**Frame codes:** `{THEME}.A1.{V#}` → e.g. `LP-PLAY.A1.V2`. Print the code as a small label above each frame (Open Sans Semibold 28px `#2f2922`, 20px above the art, left-aligned).

**Build unit:** one theme at a time = its 3 lanes side by side (3 × 1080×1920 on one canvas, 60px gutters). After all 6, tile a 6-column contact sheet for review.

---

## ⛔ THREE HARD RULES — apply to every frame; breaking one = reject + regenerate

**RULE 1 · RENDER ONLY THE TABLE COPY.** The per-theme cell table below is the single source of rendered truth. Never paraphrase LP prototype copy, grid hooks, or your own instincts onto a frame.
- No cash-register language in ANY readable string: never the 4-letter register word, "cash tin", or the "ring up / rang / rung" verb family. <!-- lint-allow: quotes banned terms as rules -->
- Use "cashier / checkout / POS / the counter / record / recorded" ("cash drawer" OK for reconciliation artifacts).
- Malaysian/British English only — no American spelling, vocabulary, or idiom (colour not color; queue not line; shop/outlet not store; maths not math). Brand/feature names verbatim. Full tables: `malaysian-english-voice.md`.

**RULE 2 · NEVER a downmarket / low-income setting.** Aspirational, upmarket venues only: well-fitted specialty café, modern bistro / full-service restaurant, established boutique, contemporary salon/studio. Good natural or warm designed lighting, tidy counter, merchant clearly doing well.
- BANNED settings: roadside mamak, basic kopitiam, hawker/food-court/wet-market stall, plastic stools. <!-- lint-allow: quotes banned settings as the ban list -->
- Also banned: bare-bulb/fluorescent-strip lighting, run-down interiors, a literal cash tin on the counter. <!-- lint-allow: quotes banned settings as the ban list -->
- Pan-Asian / SEA faces only — never Western. Mess belongs only in a pain artifact, never in the venue.
- **The Day-In-The-Life LP illustration uses an old-shophouse style — translate it UP to a modern specialty café in the ad; never render its venue literally, and never render the LP's fictional shop name.**

**RULE 3 · Build the frame from the cell table, not from memory.** When in doubt about a word, check `malaysian-english-voice.md`; about a venue, re-read RULE 2.

---

## Brand system (all 18 frames)

- **Colours:** Orange `#ff9419` + Black `#2f2922` dominant. Accents sparingly: Pink `#ff546f`, Bold Orange `#ff630f`, Azure `#2a6ee8`. Cream `#fff8ea` for type-led backgrounds. **NEVER orange + green.** LP-HB only: gold `#ffc94a` allowed for celebration ping marks only (sanctioned single-use accent), never UI chrome.
- **Fonts:** Barlow (Bold/ExtraBold/Black) headlines + giant type. Open Sans (Semibold/Bold/Regular) subcopy, CTA, microcopy. Caveat only for a handwritten accent.
- **Logo:** wordmark **StoreHub** — one word, capital S + capital H. Top-right, top edge y ≥ 270.
- **Imagery:** photographic, documentary, candid, natural/warm light, upmarket venues (RULE 2), Pan-Asian/SEA faces only.
- **CTA:** rounded pill, fill `#ff9419`, label per theme table (campaign-locked CTA — these ads drive clicks into an interactive page, so the pill names the LP's verb, not "BOOK A DEMO"), Open Sans Bold `#2f2922`.
- **Microcopy chip** by the CTA: **"From RM3.40/day"** (low-key). LP-DAY and LP-HB (brand plays) drop the chip and instead run the microline in the table.
- **Gradient (scoped — never on cream V3):** linear `#2f2922` ~0% → 75% opacity, y ~900 → 1420, applied ONLY where the bottom block sits over a photo (V1) or a dark/busy artifact (LP-HB map). SKIP it where the artifact is a white/light card (LP-RCPT receipt, LP-PLAY POS card, LP-CALC slider panel) — a scrim over our own product UI reads as a render bug; use a solid reveal-strip panel there instead.
- **Headline scale:** V1 = 90–120px · V2 reveal = 48–64px · V3 giant = 240–560px (box ≤952px wide, ≤720px tall, y 320–1040).

## 9:16 safe zones (hard — every frame)

1080×1920 · top 250 · bottom 500 · side 64 → safe area 952×1170 (y 250→1420).
- Headline starts y ≥ 280 · headline (V1/V2) ends ≤ y 1090.
- Subcopy (transition phrase) ~y 1110–1170, Open Sans ~40px.
- CTA pill ~y 1240–1380, **ends ≤ y 1400**. Chip beside/above CTA ≤ y 1400.
- Top-right logo top edge ≥ y 270.
- **Bottom 500px (y 1420→1920) = DEAD ZONE.** Nothing important there.
- **V2 lane exemption:** artifact fills y 0→1140; reveal line + subcopy + CTA + chip all stack INSIDE the reveal strip y 1150→1400 (CTA still ends ≤ 1400). The "headline ends ≤ y 1090" rule applies to V1 only.

## Artifact & photo compliance (V2 lane risk zone)

- Never name or show competitors / third-party platforms; no real logos, app icons, delivery/POS/bank UI. StoreHub's own product UI is allowed and encouraged (it's ours) — stylised, clean, no fake claims.
- Receipt headers: the fictional shop's own generic name or "StoreHub" only. Any barcode/QR is decorative.
- Map artifacts (LP-HB): stylised Malaysia outline only — no real place-name pins beyond city labels, no third-party map tiles/watermarks.
- Simulated numbers are labelled: low-contrast microcopy **"Illustrative example"** on any invented sales/leak figure (LP-DAY sales card, LP-CALC leak number).
- Social proof string verbatim: **"20,000+ merchants across Southeast Asia"**.
- No delivery-commission framing, no uptime %, no fabricated named testimonials.

---

## The 6 themes — per-cell tables (single source of rendered truth)

### LP-PLAY — "Playable POS" (F&B · warm/retarget)
LP hero: a working POS the visitor runs — tap favourites, send to kitchen, get paid, beat 30 seconds.
Subcopy (all 3): **"From first tap to paid."** · CTA **"RUN THE COUNTER"** · chip "From RM3.40/day" · logo StoreHub top-right.

| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "Think a POS is hard to run? You've got 30 seconds." | *Documentary:* a barista's hands mid-tap on a clean POS tablet at a modern specialty café counter, kitchen ticket printing, warm light, motion energy. No overlay chips — the headline's "30 seconds" carries the time claim. |
| **V2** | Reveal line: "Tap the menu. Send to kitchen. Get paid. No training." · Artifact text: header "StoreHub POS · Table A1 · Dine in", menu tiles "Nasi Lemak RM12 · Teh Tarik RM4", button "Send to kitchen", timer chip "0:17" + low-contrast microcopy "Illustrative example" | *Artifact (spine):* the LP's opening POS screen as hero — a clean stylised StoreHub POS card filling y 0→1140, one tile mid-tap with a finger shadow. Reveal strip y 1150→1400. Mirrors the LP's first frame exactly. |
| **V3** | Giant: **"Beat 30s."** · subline: "Run a real counter. Zero training." | Pure type on cream `#fff8ea`, Barlow Black, no object, no UI. |

### LP-SIM — "Shop Simulator" (F&B · warm)
LP hero: type your shop's name; the page rebuilds as your shop on StoreHub.
Subcopy (all 3): **"From a name to a whole shop."** · CTA **"SEE YOUR SHOP"** · chip "From RM3.40/day" · logo StoreHub top-right.

| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "Type your shop's name. Watch it run on StoreHub." | *Documentary:* an owner leaning on her boutique café counter, tablet propped up showing a big empty input field with a blinking cursor (stylised), curious half-smile, warm morning light. |
| **V2** | Reveal line: "One name in. Your POS, QR menu and report out." · Artifact text: label "What's your shop called?", input placeholder "e.g. Your Café Name", chips "Café · Curry house · Bakery" | *Artifact (spine):* the LP's hero input as hero — a giant rounded input field card with a blinking cursor, three cuisine chips below, faint ghosted POS/receipt/report surfaces behind it beginning to form. |
| **V3** | Giant: **"Name it."** · subline: "Type your shop's name. The page becomes your shop." | Pure type on cream, Barlow Black. |

### LP-DAY — "Day In The Life" (F&B · brand play)
LP hero: scrolling drags the sun over a shopfront, 7am–11pm, live sales ticking.
Subcopy (all 3): **"From open to close."** · **No price chip** — microline instead: "One scroll. One working day." · CTA **"SCROLL THE DAY"** · logo StoreHub top-right.

| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "One scroll runs this café from 7am to 11pm." | *Cinematic:* one modern specialty café interior, split light — dawn gold on the left of frame melting into night-blue window on the right, owner mid-service at the counter, unhurried. Time compressed inside one frame. |
| **V2** | Reveal line: "Scroll, and the sun drags the whole day with it." · Artifact text: giant clock "16:48", strip "7AM · OPEN — 11PM · CLOSE", phone card "Sales so far · RM1,912" + microcopy "Illustrative example" | *Artifact (spine):* the LP's hero as a poster — big sun over a stylised modern café façade (flat illustration, upmarket fit-out, awning + glass front — NOT the LP's old-shophouse styling — see RULE 2), phone in the foreground showing the live-sales card. |
| **V3** | Giant: **"7am–11pm."** · subline: "The whole day, in one scroll." | Pure type on cream, the en-dash oversized, Barlow Black. |

### LP-CALC — "The Calculator" (F&B/Retail · cold, strongest CPL angle)
LP hero: three sliders → your estimated monthly leakage vs the price.
Subcopy (all 3): **"From guesswork to numbers."** · CTA **"GET YOUR NUMBER"** · chip "From RM3.40/day" · logo StoreHub top-right.


| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "How much is your counter costing you? Move three sliders." | *Documentary:* owner at a tidy boutique counter after close, phone in hand, calculator glow on face, two or three receipts in one neat clip, otherwise clean counter — concentration, not despair. Upmarket, warm lamp light. |
| **V2** | Reveal line: "Your orders. Your ticket size. Your staff. Honest maths." · Artifact text: label "Orders per day", value "120" on a slider, output card "Estimated monthly loss · RM4,380" + microcopy "Illustrative example" | *Artifact (spine):* the LP's slider panel as hero — one giant orange slider mid-drag with a thumb on it, the leak number counting up beneath. |
| **V3** | Giant: **"RM4,380."** · subline: "One shop's monthly leak. Three sliders find yours." + low-contrast "Illustrative example" | Pure type on cream, Barlow Black. |
### LP-RCPT — "The Receipt" (F&B · cold + warm, fastest wow)
LP hero: the entire page is a thermal receipt that prints as you scroll; the form is a tear-off stub.
Subcopy (all 3): **"From first line to last."** · CTA **"WATCH IT PRINT"** · chip "From RM3.40/day" (dropped on V3 — FREE beside a price collides) · logo StoreHub top-right.

| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "This whole page prints like a receipt. Your answer's the last line." | *Documentary:* macro shot — a thermal receipt mid-print curling out of a clean printer at a modern café counter, shallow depth, warm light, barista blurred behind. |
| **V2** | Reveal line: "Scroll, and it prints your shop's story line by line." · Artifact text: receipt header "YOUR SHOP · StoreHub Demo", lines "QUEUE HANDLED ........ ✓", "STOCK COUNTED ........ ✓", "CLOSING DONE ......... ✓", final bold line "DEMO BOOKED ....... FREE" | *Artifact (spine):* one giant thermal receipt filling the frame, perforated tear line near the bottom edge of the art, last line bolded. Decorative barcode only. |
| **V3** | Giant: **"FREE."** · subline: "The last line this receipt prints." | Pure type on cream, Barlow Black. |

### LP-HB — "Heartbeat" (brand / social proof · warm)
LP hero: a live map of Malaysia pinging with orders; submitting drops your ping.
Subcopy (all 3): **"From watching to joining."** · **No price chip** — microline instead: "20,000+ merchants across Southeast Asia" · CTA **"JOIN THE MAP"** · logo StoreHub top-right (white on dark for V1/V2).

| Lane | Rendered copy | Art direction |
|---|---|---|
| **V1** | Headline: "Malaysia is ordering right now. Watch the map ping." | *Cinematic:* over-the-shoulder of an owner at a dark, handsome café bar after close, tablet glowing with a stylised pinging map, orange points of light reflected — quiet awe. |
| **V2** | Reveal line: "Pings like these, all day, across Malaysia. Yours next." · Artifact text: header "ORDER HEARTBEAT", counter "Orders since you opened this page · 47" + microcopy "Simulated feed" | *Artifact (spine):* dark `#2f2922` field, stylised Malaysia outline, orange `#ff9419` pings mid-ripple, ONE gold `#ffc94a` ping highlighted with a small tag "you". No map tiles, no third-party marks. |
| **V3** | Giant: **"20,000+"** · subline: "merchants across Southeast Asia. Join the map." (microline dropped on this lane — it would double the proof string) | Pure type — dark ink numerals on cream, one tiny gold dot as the full stop (the single sanctioned accent). |

---

## Review checklist — run on every frame before presenting

1a. **Source-echo:** every rendered string traces to the theme's cell table above. LP prototype copy (e.g. "Cafe Seng Huat", "Don't read about it. Use it.") never renders.
1b. **No cash-register language** in any readable string: never t-i-l-l, "cash tin", ring-up verb family. Cashier/checkout/POS/counter/record only. <!-- lint-allow: quotes banned terms as rules -->
1c. **No Americanisms:** British/MY spelling, vocab, idiom throughout.
2. **Setting reads upmarket** (RULE 2). LP-DAY especially: modern café façade, never old-shophouse styling (RULE 2 ban list applies).
3. **Safe band:** V1 headline ends ≤ y 1090; V2 per its lane exemption (everything in the strip y 1150→1400); CTA ends ≤ y 1400; logo top ≥ y 270; nothing important y 1420→1920.
4. **Subcopy matches the theme's phrase**; CTA pill matches the theme's locked label.
5. **Compliance:** no competitor/third-party logos or UI; simulated numbers carry "Illustrative example"/"Simulated feed"; decorative barcodes only; social-proof string verbatim.
6. **Logo spelling:** "StoreHub" exactly, everywhere. (Diegetic all-caps receipt lines are exempt only where the table specifies them; the LP-RCPT header renders "StoreHub Demo" mixed-case.)
7. **Lanes distinct:** V1 photo ≠ V2 artifact ≠ V3 pure type (V3 contains no object — if it has a receipt/screen/map, it's V2).
8. **Brand:** Barlow headline biggest element; orange CTA; no orange+green; Pan-Asian faces only; gradient scoped per the brand block (never over white artifacts, never on V3); gold accent only where sanctioned (LP-HB).
9. **Message-match:** the V2 artifact visibly mirrors its LP's first-frame MECHANIC. For LP-DAY it mirrors the mechanic (sun/clock/sales card), not the venue styling — the LP hero's upmarket restyle is a logged follow-up, not this batch's job.
