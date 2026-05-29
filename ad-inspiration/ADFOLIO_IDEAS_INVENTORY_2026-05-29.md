# Adfolio.design — Idea Inventory for StoreHub (MY EN)

**Compiled:** 2026-05-29
**Source primary:** https://www.adfolio.design/ (feed + `/breakdowns` + `/breakdowns/tags/*` + `/landing-pages` + `/motion` + `/about`)
**Source supplementary:** Diligent Studios (same creators), adkit.so B2B teardowns, vibemyad.com static-ad library, saashero.net B2B design playbook, contentbeta ad-creative roundup, b2w.tv GIF banner ads, understoryagency LinkedIn teardowns.
**Cross-referenced against:** the StoreHub 12-theme test history (T1–T12) and the existing layout playbook (split cards, Choose-Your-Fighter, POS-pedestal, cream-bg typography, dark-overlay full-bleed).

> **Crawl note.** Adfolio.design is fronted by a Vercel security checkpoint that hard-throttles automated fetches (persistent 429s through this session). The site structure, taxonomy, brand list, and analysis framework were reconstructed from indexed search snippets across ~40 breakdown URLs plus deep reads of three adjacent swipe-file libraries that explicitly catalog the same patterns Adfolio teaches. Where a pattern is named below, it is documented in at least two independent sources, not invented. If/when Adfolio comes back online, the slugs in **Appendix A** are the highest-value to manually screenshot.

---

## 1. EXECUTIVE SUMMARY (read this first)

Adfolio is not a generic ad library. It is a **curated B2B SaaS swipe file** organized around a single analytical lens: **Hook → Visual → CTA**. Every breakdown is one image plus a three-part explanation of what stopped the scroll, what made the visual carry the idea, and what the click-action did. The featured brands are almost entirely **English-language Western B2B SaaS** — Figma, Webflow, Typeform, Notion, Vercel, Brex, Ramp, Deel, HiBob, Cognism, Mailchimp, PostHog, Intercom, Asana, Capchase, Lokalise, Weglot, Clockwise, Metadata, SOCi, Diligent Studios, reMarkable, Pleo, Pitch — and a heavy share of the work is by the duo's own agency, Diligent Studios, which is the cleanest signal of "what Adfolio thinks is the gold standard."

**What dominates Adfolio:** static single-image asset on a flat or cream background; oversized typography that **does the headline's job inside the image** rather than in the platform copy field; one specific number or one specific artifact (a fake spreadsheet, a fake email, a Slack screenshot, a "found 3 charges you didn't expect" mockup); restraint everywhere (one idea, one number, one face); and **landing pages that look like the ad** (continuity beats cleverness).

**What is underused on Adfolio** (and therefore wide open as net-new territory for StoreHub):
- Non-English / non-Western cultural cues (Adfolio has effectively zero Pan-Asian, Bahasa, kopitiam, hawker, or Ramadan context — StoreHub's biggest unfair advantage)
- F&B-vertical-specific artifacts (recipes, menus, POS receipts, hawker stall signage, banquet event sheets, kitchen prep boards)
- Multi-asset story carousels (Adfolio is overwhelmingly single-image, not 5-card narratives)
- Polls/quizzes/interactive Stories
- Time-of-day-anchored creative (lunch rush, opening morning, 11pm close-out)
- Print-mimic ads (Adfolio rarely showcases newspaper/poster/leaflet/menu mimics)

**Biggest unlock for StoreHub:** Adfolio proves the **"artifact native"** pattern is the structural winner in B2B. StoreHub already knows this (T11 was its winner). The unlock is to **expand T11's surface area dramatically** — there are 15+ artifact types StoreHub has not yet used (LHDN final-warning letter, MOH halal cert, JKM signboard, kopitiam chalkboard, MyKad, Touch-n-Go receipt, GrabMart picklist, e-invoice PDF, water-bill statement, broker WhatsApp pitching POS leasing, etc.). Each is a fresh ad.

**Brutal note.** Adfolio's brands sell to VPs of Engineering, RevOps, CFOs. StoreHub sells to **a kopitiam owner's wife who handles the cash register**. The structural lessons transfer (specificity, restraint, artifact mimicry, one-number ads). The vibe, faces, and references **do not**. Treat Adfolio as the format library, not the content library.

---

## 2. SITE TAXONOMY (as Adfolio organizes itself)

Use this scaffold when filing/tagging your own ads.

**Top-level sections (visible nav):**
- `/` — main feed (mixed static ads, all platforms)
- `/breakdowns/<slug>` — single-ad analyses (Hook + Visual + CTA)
- `/breakdowns/tags/<slug>` — filtered views (industry / pattern tags)
- `/landing-pages` — landing pages that the ads link to
- `/landing-pages/<slug>` — individual LP teardowns
- `/motion` — animated/GIF B2B ads ("39 of the coolest B2B GIF ads" Threads post Dec 2024 confirms motion is a curated sub-section)
- `/about` — duo philosophy, who they make ads for

**Analysis framework Adfolio uses on every breakdown (use this same triad on your own ads):**
1. **Hook** — the first second of attention. What did the viewer's brain do?
2. **Visual** — the asset choice. Why this image and not a stock photo?
3. **CTA** — what specifically clicks, and where does it go?

**Implicit brand-level taxonomy (industries featured):**
- Dev tools / design (Figma, Webflow, Vercel, Notion, Linear-adjacent, PostHog)
- Fintech / spend mgmt (Brex, Ramp, Pleo, Capchase, Mercury-adjacent)
- HR / payroll (Deel, HiBob, Rippling-adjacent)
- Sales / RevOps (Cognism, Metadata, SOCi)
- Workflow / productivity (Clockwise, Asana, Typeform, Mailchimp, Intercom)
- Localization (Lokalise, Weglot)
- Hardware / prosumer (reMarkable)

**No F&B, no retail SMB, no SE Asia, no non-English** — confirms the cultural-context gap for StoreHub to exploit.

---

## 3. THE IDEA INVENTORY

72 ideas, organized into 8 categories. Format for each:

> **#NN — Name** (one-line desc) · **Why it could win for StoreHub:** … · **Execution:** … · **Risk:** … · **Net-new vs T1–T12:** …

---

### A. ARTIFACT MIMICS — extend T11 (the structural winner)

Adfolio's most-repeated trick: make the ad look like *not an ad*. Make it a screenshot, a form, a letter, a printout. StoreHub already validated this with T11 (fake job-post, WhatsApp, Google review, LHDN). Below are 15 fresh artifact types Adfolio + adjacent swipe files surface that StoreHub has not yet shipped.

**#01 — LHDN e-Invoice Notice mimic**
Single static. Looks exactly like an LHDN e-invoice rejection letter / portal screenshot with a circled error: "Receipt format non-compliant — manual entry detected." Bottom strip: "StoreHub auto-generates compliant e-invoices. Setup in 24h." CTA bar.
- **Why it could win:** Every MY F&B owner has e-invoice anxiety in 2026. Compliance fear > feature pitch.
- **Execution:** Figma. Use real LHDN portal typography + color palette (red error band, navy header). 1080x1080 + 1080x1920 for Stories.
- **Risk:** Has to be *just* shy of mistakable — too real and the platform may flag; too cartoonish and it loses the trick.
- **Net-new vs T1–T12:** Evolution of T11 (artifact). Net-new artifact type.

**#02 — JKM/MOH Halal cert mimic with expiry callout**
Static. Halal cert template with a red "EXPIRING IN 14 DAYS" sticker stamped diagonally. Caption: "When was the last time you checked? StoreHub flags every cert + permit before it lapses." (Note: only ship if StoreHub actually has cert-tracking; otherwise switch to "your inventory expires too — milk in 3 days, rendang stock in 2.")
- **Why:** Hyper-MY-specific. No global SaaS will ever do this.
- **Execution:** Canva or Figma. Pan-Asian context, Bahasa accent words OK.
- **Risk:** Cert-tracking claim must be true. Use the inventory-expiry pivot if not.
- **Net-new:** New artifact under T11.

**#03 — Touch-n-Go receipt mimic**
Static. Receipt printout look. 12 line items, "Service charge — RM0.00 ❌", "Cash float reconcile — manual 23 min ❌". Bottom: "Replace 6 of these with one POS. StoreHub from RM3.40/day."
- **Why:** Receipts are universally readable to F&B owners; the pattern interrupt is "wait, that's MY receipt."
- **Execution:** Figma. 80mm thermal receipt aspect ratio, mono font (Roboto Mono / IBM Plex Mono works).
- **Risk:** Don't list things StoreHub doesn't actually replace.
- **Net-new:** Evolution of T11 + T9 (Hidden Cost) fused.

**#04 — Kopitiam chalkboard menu mimic**
Static. White-chalk-on-black menu board. Items in Bahasa + Cantonese. Last line is the headline in chalk: "Sales: ??? — that's the line we want to know." StoreHub bar at bottom.
- **Why:** Visual = exact F&B context. Pattern interrupt = "what's the chalkboard doing in my feed?"
- **Execution:** Figma + a real photo of an empty chalkboard with hand-chalked overlay (free from Unsplash + Procreate brush).
- **Risk:** Chalk handwriting must look authentic, not Photoshop chalk filter.
- **Net-new:** New under T7 + T11.

**#05 — Banquet/event run-sheet mimic**
Static. Looks like a kitchen run-sheet for a wedding banquet: 6:30pm tea, 7:00pm cocktail, 7:30pm 8-course… One column is "POS bottleneck (mins)" and it's red. CTA: "Run 800-pax weddings without the floor calling the kitchen."
- **Why:** Big-format F&B (banquet halls, wedding venues) is high-ACV. No competitor talks to them directly.
- **Execution:** Figma table layout.
- **Risk:** Niche segment — pair with broader cafe ad in same campaign.
- **Net-new:** New artifact, new sub-vertical pitch.

**#06 — MyKad / SSM Form-9 mimic with a redacted founder name**
Static. SSM business registration certificate look. Founder name redacted. Headline below: "Day 1 of your shop. Day 7, you'll wish you'd already had a POS." Anchored to T2 (New Chapter).
- **Why:** SSM = the universal MY founding ritual. Immediate emotional anchor.
- **Execution:** Replicate the SSM cert layout in Figma (not the real seal — use a stylized stand-in).
- **Risk:** Don't reproduce the actual SSM seal — modify the crest.
- **Net-new:** New artifact under T2 + T11.

**#07 — Bank statement mimic with margin highlighter pen**
Static. Maybank/CIMB-style monthly bank statement. Yellow highlighter pen drawn across "POS subscription RM149", "EDC fee RM89", "Reconciliation labour 8 hrs RM280." Bottom strip: "RM3.40/day replaces all of these."
- **Why:** Direct visual extension of T9 (Hidden Cost) but more visceral than a receipt.
- **Execution:** Figma. Use generic bank layout (no real logos). Yellow marker brush.
- **Risk:** Be honest about what RM3.40 replaces vs supplements.
- **Net-new:** Evolution of T9 + T11.

**#08 — Broker WhatsApp pitching POS leasing**
Static. WhatsApp screenshot — chat from "Ah Beng POS Trading" pitching a 5-year RM12,000 lease. Reply bubble: "Tahu kawan saya pakai StoreHub RM3.40/hari je." Read receipt blue ticks.
- **Why:** Directly addresses the #1 emotional friction in MY F&B: door-to-door POS sales bros. Wins on satisfaction.
- **Execution:** Figma WhatsApp template (already used in T11; new conversation script).
- **Risk:** Don't impersonate a real broker company.
- **Net-new:** New script under T11.

**#09 — Google Maps review screenshot, but 1-star**
Static. Google review card. 1 star. "Wait 22 min order salah. Last time." Below: "Kitchen blames POS. POS blames staff. Owner blames everyone. StoreHub fixes it." CTA.
- **Why:** Owners FEAR public bad reviews. Loss aversion is stronger than gain promise.
- **Execution:** Figma Google review card template.
- **Risk:** Don't use a real merchant's review.
- **Net-new:** Evolution of T11 (Google review type already tested; this is the **negative** flip).

**#10 — Insurance/water/Tenaga bill mimic with a red "FINAL NOTICE" stamp**
Static. Utility bill. Red "FINAL NOTICE" stamp. Bottom: "Your subscription stack has more 'final notices' than your bills. Consolidate to one POS." Lists 5 SaaS logos crossed out (generic, no real brands).
- **Why:** SaaS sprawl is a real pain. Bill format is universally legible.
- **Execution:** Figma. Generic utility layout.
- **Risk:** Don't name competitors.
- **Net-new:** New artifact under T11.

**#11 — Shopee/Lazada/GrabMart vendor portal screenshot**
Static. Looks like a marketplace seller portal showing 17 unread orders, low-stock alerts, and a "Sync to POS — FAILED" red banner. Bottom: "One backend. All channels. StoreHub."
- **Why:** Omnichannel headache is universal for retail SKUs. Marketplace screenshots feel real.
- **Execution:** Figma. Generic portal layout (don't replicate real platforms).
- **Risk:** Stay close enough to feel real, far enough to avoid IP issues.
- **Net-new:** New under T11.

**#12 — Daily Z-report tape spilled across the floor**
Static photo. Long thermal Z-report curling on the floor of a closed kopitiam at 11pm, with a calculator and a half-finished teh tarik. Headline overlay: "End of day. Or start of overtime?" Small CTA strip.
- **Why:** Pure mood. Owner sees themself instantly. Photographic, not artifact-mockup — different texture.
- **Execution:** Real photo shoot (or Midjourney/Sora "Pan-Asian kopitiam interior, thermal printer tape, calculator, night, fluorescent ceiling light, photographic").
- **Risk:** Midjourney can drift Western. Specify "kopitiam, Malaysian, fluorescent tube, marble table."
- **Net-new:** Evolution of T1 (Pain) but T1 was retired — this is **artifact-anchored** pain, not staged chaos.

**#13 — Cookbook recipe card with a "cost per plate" sticky note**
Static. Recipe card for Nasi Lemak. Yellow sticky on top: "Cost/plate RM4.20. Selling at RM6.50. Margin = ???" Below: "StoreHub does the maths. Every plate. Every shift."
- **Why:** F&B math is the operator's daily anxiety. Cookbook frame = native to their world.
- **Execution:** Figma recipe-card layout, real Pan-Asian recipe.
- **Risk:** None significant.
- **Net-new:** Evolution of T8 (Aspirational) + T11. Recipe-card mimic is new.

**#14 — Inspector clipboard report**
Static. MOH/local-council inspector clipboard. Checkboxes. Critical-fail item: "Sales register tampering risk — manual entries detected." Stamp: "Repeat inspection in 14 days." CTA.
- **Why:** Compliance fear, hyper-MY, fresh angle.
- **Execution:** Figma clipboard template, official-looking sans-serif (not real MOH seal).
- **Risk:** Don't replicate real council seal.
- **Net-new:** New artifact under T11.

**#15 — Calendar invite with title "FREE DEMO — StoreHub" already accepted**
Static. iCal/Outlook event card. RSVP "Accepted." Attendees: "Owner, Manager." Title: "30 min — get your time back." Below: "Already scheduled. We just need your email."
- **Why:** Plays the "this is already happening, just confirm" presumptive close. Strong for retargeting.
- **Execution:** Figma calendar event card.
- **Risk:** Works mostly for warm audiences (retargeting). Cold audiences won't get it.
- **Net-new:** New under T11. Pure CTA artifact.

---

### B. HOOK ARCHETYPES — beyond your 12 themes

**#16 — Behavior Call-Out**
"You do [thing] every [Monday/closing/end-of-shift]. Stop." Then the visual = the exact tool/action being called out, with a red X.
- **Why:** Adfolio + adkit document this as the single highest-stop-rate static for B2B. StoreHub equivalent: "Every Monday morning you tally Saturday's sales. Stop."
- **Execution:** Static. Cream bg, oversized type. Pan-Asian hand holding a calculator (cropped tight).
- **Risk:** Must call out a behavior the audience actually does — generic = dead.
- **Net-new:** New hook archetype not currently in T1–T12.

**#17 — Specific-Number Pattern Interrupt**
ONE oversized number on the canvas. "RM47,213." Tiny subtitle: "Untracked cash overage at 47 kopitiams in 2025. Yours is in there." StoreHub bar.
- **Why:** Number-only ads outperform text-only in thumbnail. Specificity (47,213 not 50k) signals real data.
- **Execution:** Figma. Number = 70% of canvas. Barlow Black. Orange digit, black bg.
- **Risk:** The number has to be real or believably sourced.
- **Net-new:** Format evolution of T4 (price math) — but T4 used RM3.40/day. This is a **shock number**, not a price.

**#18 — Identity Filter Hook**
"If you run a kopitiam with 2 cashiers, this is for you." Visual = a hand-drawn kopitiam diagram.
- **Why:** Audience filtering = higher CTR, lower CPL. Adfolio teaches this with "If you're a controller…" and "FP&A teams."
- **Execution:** Headline-first. Minimal visual.
- **Risk:** Each variant needs its own creative — costs scale.
- **Net-new:** Net-new hook structure.

**#19 — Reframe Hook ("It's not X, it's Y")**
"It's not a POS. It's the only person in the shop who never calls in sick." Pan-Asian owner photo, soft light.
- **Why:** Reframing reduces commodity perception (POS = commodity).
- **Execution:** Photo + 2-line headline. Cream/orange palette.
- **Risk:** Risk of being too clever; test against literal version.
- **Net-new:** New hook.

**#20 — Confession Hook**
"I lost RM1,800 last month to staff under-rings. I didn't know until June." Quote-style, named source ("— Owner, Banting bistro").
- **Why:** First-person voice + a number = high credibility, high CTR.
- **Execution:** Quote-card layout. Italic body, bold attribution.
- **Risk:** Must be a real anonymized story, with permission.
- **Net-new:** Evolution of T6 (Social Proof) but flipped to **negative** confession. Net-new tonal angle.

**#21 — Anti-Pitch Hook ("This is not for you if…")**
"This is not for you if you have 1 cashier, fewer than 30 covers a day, and never want to grow." Visual: empty kopitiam.
- **Why:** Reverse psychology + audience filter. Disarms skepticism.
- **Execution:** Headline-led. Low-key visual.
- **Risk:** Can read snobby; tone has to be warm.
- **Net-new:** Net-new hook.

**#22 — Calendar/Date-Based Urgency**
"e-Invoice deadline: 1 Jul 2026. Days left: 33." Big countdown number. Bottom: "StoreHub sets it up in 24h."
- **Why:** Real regulatory deadlines force action better than offers.
- **Execution:** Update weekly. Use a real deadline.
- **Risk:** Tied to deadline; rotate when it passes.
- **Net-new:** Net-new hook (urgency anchored to MY regulation).

**#23 — Three-Word Headline**
"Closing time. Again." On a photo of a darkened kopitiam interior. CTA in small caps.
- **Why:** Restraint. Adfolio's best ads use ≤8 words on canvas.
- **Execution:** Photo + 3 words. Barlow Black, white type on dark photo.
- **Risk:** Has to be ambiguous in the right direction — too vague misses.
- **Net-new:** New layout/format under T3 (Quiet Ambition) vibe but tighter.

**#24 — "Versus your subscription stack" Hook**
"Your tech stack right now:" — visual: 7 logos in a grid (fake/generic, e.g. an icon for "reservation tool", "loyalty app", "marketplace dashboard"). "After StoreHub:" — just the StoreHub mark.
- **Why:** Consolidation is a hidden buyer motivation.
- **Execution:** 2-frame static. Half-canvas before/after.
- **Risk:** Don't use real competitor logos.
- **Net-new:** Evolution of split-card layout but with **SaaS sprawl** as the angle. Net-new content under existing layout.

**#25 — "We Did The Math" Hook (but inverted)**
Not RM3.40/day. Instead: "Skipping a POS upgrade costs the average kopitiam RM18,400/year in shrinkage, comp time, and order errors." Big number, small footnote.
- **Why:** T4 (price anchor) failed. This is the **opportunity cost** anchor — different psychological lever.
- **Execution:** Number-dominant static. Footnote with assumptions.
- **Risk:** Need defensible math.
- **Net-new:** Reframe of failed T4. Not a rehash — the **direction** is inverted.

---

### C. VISUAL TREATMENTS — typography, composition, palette

**#26 — Newspaper Classifieds Column (full Berita Harian / The Star pastiche)**
Multi-line classifieds page mockup. One ad is highlighted with a red marker pen: "WANTED: cashier who never makes mistakes. Pay: peanuts. Or: get StoreHub." Pan-Asian retro newsprint feel.
- **Why:** Extends T5 (Competitive Contrast — fake job post) but as a full-page mimic, not a single card.
- **Execution:** Figma. Real classifieds typography (condensed serif, multi-column).
- **Risk:** Don't use a real publication's masthead.
- **Net-new:** Evolution of T5 winner — denser, more native.

**#27 — Print Receipt-as-Hero**
The ENTIRE canvas is one thermal receipt, full bleed, including curl shadow on edges. The receipt copy IS the headline + body + CTA.
- **Why:** Pure artifact ad. Zero "ad" framing.
- **Execution:** Figma. Mono font. Real receipt formatting (date, register #, items, RM totals).
- **Risk:** Hard to read in feed thumbnail — use bold lines, not all caps everywhere.
- **Net-new:** Layout-native. Extends T11 mimicry. New canvas treatment.

**#28 — Sticky-Note Stack**
Photo of a real desk with 7 yellow Post-its: "Cash float?", "Reorder gula?", "Closing tally?", "Tini absent again?". Headline at top: "Your POS should remember these." Pan-Asian hand in frame.
- **Why:** Universal owner mood. The clutter IS the message.
- **Execution:** Real photo or AI render. Pan-Asian context.
- **Risk:** Sticky notes have to feel handwritten, not Comic Sans.
- **Net-new:** New visual treatment. Not in current playbook.

**#29 — Single Object on Cream BG**
One photo: a single, hyper-specific F&B object centered on cream (an EDC terminal with a dead battery, a calculator with cracked screen, a faded order pad). Tiny headline below.
- **Why:** Pure visual restraint. Adfolio's most repeated layout.
- **Execution:** Real photo shoot OR AI render with cream BG. Object must be *worn*, not pristine.
- **Risk:** Object choice has to be ICP-resonant, not generic.
- **Net-new:** Format evolution. New "decay/worn" subtext under T1-adjacent territory.

**#30 — Annotated Photo (red circles + arrows)**
Photo of a busy hawker stall. Red marker circles + arrows on six chaos points: a missed order, queue, wrong change, etc. Bottom: a clean StoreHub screen with the same six "fixed" with checkmarks.
- **Why:** The annotations do the work. Photos with marker overlays scroll-stop because they look like notes, not ads.
- **Execution:** Photoshop/Procreate marker brush over real photo.
- **Risk:** Looks unprofessional if executed poorly — has to feel like a kitchen-print whiteboard, not Microsoft Paint.
- **Net-new:** New visual treatment.

**#31 — Single Giant Word**
Canvas is dominated by one Bahasa/Malay word: "Susah." or "Sibuk." or "Cukup." Tiny line below: "POS yang faham. From RM3.40/hari."
- **Why:** Pattern interrupt + language signal in 0.2s.
- **Execution:** Barlow Black 600pt. Orange word on black, or black word on cream.
- **Risk:** Single-word ads can feel cheap if not executed with weight.
- **Net-new:** New typography play under T7 (Cultural Pride).

**#32 — Risograph / 2-tone Print Aesthetic**
Cream + orange + black ONLY. Slightly off-register print look. Hand-drawn elements over photo.
- **Why:** Visual signature. Most B2B ads look identical to each other — this looks like a poster, not an ad.
- **Execution:** Figma + risograph texture overlay (free from rb-pages.com).
- **Risk:** Aesthetic risk; A/B test against clean version.
- **Net-new:** New visual treatment category.

**#33 — Crossword / Word-Search Grid**
A crossword puzzle, half-filled. The clue list contains F&B pain points: "1 ACROSS: When the cashier's till is RM47 short" → "STORE_UB". CTA below the grid.
- **Why:** Interactive-feeling static. Stops the scroll because viewers solve it.
- **Execution:** Figma grid + serif puzzle font.
- **Risk:** May confuse low-attention viewers. Pair with a clearer headline.
- **Net-new:** Pure experimental — new format.

**#34 — Photocopy / Faxed Memo Aesthetic**
Looks like a 1990s memo: "FROM: Owner / TO: Manager / RE: Why we still tally cash by hand." Faded edges, "URGENT" stamp. CTA.
- **Why:** Nostalgia + authority + analog = visual pattern interrupt.
- **Execution:** Figma + paper texture.
- **Risk:** Has to feel intentional, not lazy.
- **Net-new:** New treatment.

**#35 — Inventory Spreadsheet Mockup**
A static "spreadsheet" — rows of inventory with one cell highlighted red: "Margin: -RM0.40 per cup." Pop-up tooltip: "You're losing money on every kopi-o."
- **Why:** Spreadsheets are universally legible. Red cell = instant attention.
- **Execution:** Figma. Google Sheets visual language.
- **Risk:** Don't make it dense to the point of unreadable.
- **Net-new:** New artifact under T11. Spreadsheet mimic specifically.

---

### D. COPYWRITING STRUCTURES

**#36 — "If you've ever ___, this is for you"**
One sentence. The blank is hyper-specific. "If you've ever counted the till twice and still felt unsure, this is for you."
- **Why:** Self-identification headline.
- **Execution:** Headline-led. Photo support.
- **Risk:** None significant. Easy to test.
- **Net-new:** New copy structure.

**#37 — "I, [Owner Name], ___ — and ___"**
First-person founder confession. "I, Encik Raj, ran my mamak for 9 years with a notebook and a calculator. The 10th year I almost lost the shop. Here's what changed." Long-form caption + simple photo.
- **Why:** Long-copy ads outperform when targeted right. Founder-confession format converts.
- **Execution:** Caption-heavy. Photo of named merchant. Use real merchants if possible.
- **Risk:** Need real merchant cooperation + signed release.
- **Net-new:** New copy structure under T6 (Social Proof). T6 was facts; this is **story**.

**#38 — "We don't [feature]. We [outcome]."**
"We don't sell POS software. We give you your Sunday back." Pan-Asian family photo on Sunday morning.
- **Why:** Outcome-first sells better than feature-first. Adfolio teaches this repeatedly.
- **Execution:** Two-line headline + photo.
- **Risk:** Must back up the claim somewhere.
- **Net-new:** Copy structure. Net-new framing.

**#39 — Subheadline Stack ("…and…and…")**
Headline: "Inventory." Subhead: "And purchase orders." Sub-sub: "And shrinkage." Sub-sub-sub: "And payroll." Tiny: "One screen. RM3.40/day."
- **Why:** Demonstrates breadth without listing features. Stacked rhythm = readable.
- **Execution:** Vertical text stack. Decreasing font size.
- **Risk:** Has to actually be true of the product.
- **Net-new:** New copy layout.

**#40 — "Here's what you'll actually spend the time saved on"**
Caption-led. "8 hours saved/week. That's: 1× Saturday family lunch + 1× nap + 1 episode of K-drama + still some left over." Photo: a family at a restaurant.
- **Why:** Concretizes the abstract "save time" promise.
- **Execution:** Caption-heavy + supporting photo.
- **Risk:** Tone has to feel earned, not patronizing.
- **Net-new:** New copy direction under T10 (Value Unlocked).

**#41 — Sequential Headlines (3-line punchline)**
Line 1: "Your POS works." Line 2: "Your staff works." Line 3: "Your wife shouldn't have to." Photo of wife at the till looking exhausted.
- **Why:** 3-line build = punchline structure. Memorable.
- **Execution:** Stacked text. Pan-Asian context.
- **Risk:** Don't be sexist — frame as care, not stereotype. The wife angle resonates in many MY kopitiams (real demographic).
- **Net-new:** New copy structure.

**#42 — Direct Question Headline**
"Can your POS tell you which dish loses you money?" Visual: a plate of nasi lemak with a question mark over it.
- **Why:** Questions = engagement. Specific question = qualified click.
- **Execution:** One-line headline + single-dish visual.
- **Risk:** Must answer the question on the landing page.
- **Net-new:** Question-hook is partially in playbook (T11 review); this is a **product capability question** which is new.

**#43 — Imagined Future Letter ("Dear me, in 6 months…")**
"Dear me, in 6 months: you finally took Sundays off. Your inventory app stopped guilting you. Your daughter said 'Ayah, you smiled today.' Signed, future you." Cream BG, handwritten font.
- **Why:** Emotional letter format is rare in B2B. Disarming.
- **Execution:** Static. Calligraphic display font for the body. CTA at bottom.
- **Risk:** Risk of feeling saccharine. Test against a control.
- **Net-new:** New copy structure under T8 (Aspirational).

---

### E. ASSET TYPES — what to actually produce

**#44 — Pan-Asian UGC selfie video (15–20s, vertical)**
Real merchant (or merchant-look actor) speaking to phone camera in kopitiam interior, in Manglish: "Eh, I tell you. Before StoreHub, I count cash twice every night. Now? I jadi tido by 10pm. Try lah." Cuts to POS UI for 2s. End card.
- **Why:** UGC outperforms produced video for B2B SaaS (multiple sources). MY Manglish authenticity = unmissable.
- **Execution:** Phone-shot or phone-look. Vertical 1080x1920. Real audio, real noise.
- **Risk:** Casting matters. Use Pan-Asian, not anyone who reads as Western.
- **Net-new:** New asset type. UGC is currently absent from the 12 themes' deliverables.

**#45 — "Day-in-the-life" sequence as 5-card carousel**
Card 1: 6am coffee. Card 2: 11am rush. Card 3: 3pm lunch lull. Card 4: 8pm closing. Card 5: same evening 9pm at home with kids — caption: "Because StoreHub did the close-out." Photo carousel.
- **Why:** Carousels generate 6.6% engagement on LinkedIn, far above static. Storytelling format.
- **Execution:** Photo shoot or AI render. 5 frames with consistent owner.
- **Risk:** Production overhead higher than statics.
- **Net-new:** Evolution of T10 (Day-in-the-life) but **as a 5-card carousel**, not single image. Format is new.

**#46 — Talking-head explainer with split screen (vertical video)**
Top half: real merchant face talking. Bottom half: StoreHub UI showing exactly what they're talking about. 25-second loop. Captions burned in.
- **Why:** Synced narration + UI proof is the gold standard for SaaS demo ads.
- **Execution:** Loom + Descript. 1080x1920. Auto-captions.
- **Risk:** Pacing — keep tight.
- **Net-new:** New asset type.

**#47 — Stop-motion of POS being assembled**
8-second loop: a POS unboxes itself on a kopitiam counter — receipt printer slides in, EDC plugs in, cash drawer pops out — all stop-motion. End on "Setup. 24 hours."
- **Why:** Stop-motion in B2B SaaS = vanishingly rare. Massive scroll-stop.
- **Execution:** Phone tripod + 60 frames. Half a day of work.
- **Risk:** Quality control — pacing has to be tight.
- **Net-new:** New asset type entirely.

**#48 — Audio-quote card (voice memo aesthetic)**
Visual: an iPhone Voicenotes UI screenshot showing a 0:47 voice memo titled "Owner of Restoran Mawar." Tap-to-play. Below: "What our merchants actually say." (In feed it's a video that plays the voice memo with waveform animation.)
- **Why:** Audio = different sensory channel, breaks visual fatigue. Authentic.
- **Execution:** Record real merchant audio. Create waveform-overlay video.
- **Risk:** Audio quality matters more than video quality. Get permission + release.
- **Net-new:** New asset type.

**#49 — Animated GIF: cash drawer opens and closes with rotating message**
Looping GIF. Cash drawer slides open: "Sales today: RM2,341." Slides shut. Opens again: "Inventory low: 4 items." Shuts. Opens: "BOOK A FREE DEMO NOW." 3-frame loop.
- **Why:** Adfolio has a whole `/motion` section for GIFs. They are underused in B2B in MY market.
- **Execution:** Figma + Lottie or Photoshop GIF export. <150KB.
- **Risk:** Some Meta placements de-prioritize GIFs; test static control.
- **Net-new:** New asset type (motion).

**#50 — Static "screenshot from a future news article"**
"BERITA HARIAN — 23 December 2026: Local mamak chain crosses RM10 million in revenue. Owner credits 'one boring decision' made 12 months earlier." Faux newspaper layout.
- **Why:** Future-press hook. Aspirational + credible visual format.
- **Execution:** Figma. Newspaper layout. No real masthead.
- **Risk:** Don't impersonate a real publication.
- **Net-new:** New asset type under T8 (Aspirational). Newspaper mimic is new.

---

### F. SCROLL-NATIVE FORMATS — Reels, Stories, Carousels, Polls

**#51 — Reels-first 9-second loop ("the 9-second close-out")**
Speed-ramped close-out routine. 9 seconds: count cash → check inventory → print report → lock up. Caption: "All 9 seconds. Manually it's 47 minutes." End card.
- **Why:** Reels reward tight loops. Speed-ramps are scroll-stopping.
- **Execution:** Real shoot + Premier/CapCut speed ramp.
- **Risk:** Audio rights — use library track.
- **Net-new:** New format.

**#52 — Poll Sticker on Story**
Story image: a Pan-Asian owner at the till looking puzzled. Poll: "How many SaaS subscriptions does your shop have? 🅰 1–2 🅱 3–5 🅲 6+ 🅳 I lost count." Auto-DM follow-up.
- **Why:** Polls drive engagement → audience signal for retargeting.
- **Execution:** Native Story poll. Manychat or Meta auto-DM.
- **Risk:** Stories ≠ Feed; treat as funnel-builder, not primary acquisition.
- **Net-new:** New format entirely.

**#53 — Quiz carousel ("What kind of kopitiam owner are you?")**
5-card quiz. End card maps each answer to a StoreHub feature emphasis.
- **Why:** BuzzFeed-style quizzes work because they qualify intent.
- **Execution:** 5-card carousel + link to a quiz landing page.
- **Risk:** Production cost — but evergreen once built.
- **Net-new:** New format.

**#54 — "Before / 30 days in / Now" 3-card sequence**
Card 1: stressed owner at till. Card 2: hesitant owner with iPad. Card 3: smiling owner at family lunch. Caption: real owner story.
- **Why:** Story arc in 3 cards. Easier to consume than 5-card.
- **Execution:** Photo set or AI render. Consistent character.
- **Risk:** Casting consistency.
- **Net-new:** Evolution of split-card before/after — but **3-stage temporal**, which is new.

**#55 — Reels "POV" format**
"POV: you just closed for the night and your phone buzzes — StoreHub sent the daily summary already." Vertical POV from owner's eyes, kopitiam lights dimming, phone notification.
- **Why:** POV format dominates TikTok/Reels organic — borrow that grammar.
- **Execution:** Phone shoot, first-person handheld.
- **Risk:** Audio + caption pacing.
- **Net-new:** New format.

**#56 — Vertical text-on-screen "no music" ad**
Reels: phone vertical, owner silent, captions only. The whole ad is captions: "Bro. I serious. Used to take 2hrs to close. Now 12 min. Try lah." End card.
- **Why:** Silent autoplay-friendly. Bypasses audio drop-off.
- **Execution:** Phone vertical + captions burned in.
- **Risk:** Easy to look low-effort if pacing is off.
- **Net-new:** New format.

---

### G. CONCEPT CATEGORIES — testimonials, demos, education, comparison

**#57 — Reverse-Testimonial ("Don't take their word — take ours")**
Static. A grid of generic 5-star stock testimonial graphics with a giant red X across them. Below: "Here's a real demo instead." Photo of real merchant Zoom call screenshot.
- **Why:** Anti-pattern interrupt. Stands out in a sea of fake-testimonial ads.
- **Execution:** Figma. Red brush stroke X.
- **Risk:** Has to feel earned, not snarky.
- **Net-new:** New angle on T6.

**#58 — Stitch-style "Owner reacts to ad" video**
Real owner watching a StoreHub ad on their phone, then turning to camera: "OK, but does it actually work for someone like me?" Cut to demo footage. 18 seconds.
- **Why:** Self-aware meta format = TikTok-native. Disarming.
- **Execution:** Two-camera shoot or single-camera with cuts.
- **Risk:** Has to feel real — script lightly.
- **Net-new:** New concept.

**#59 — "Show me the actual product" demo (90 seconds, unedited)**
Single take. Owner opens StoreHub on iPad. Talks through their actual day. No cuts. No music. Just narration.
- **Why:** B2B buyers scream for "show me the product." Unedited = credible.
- **Execution:** Loom. Real merchant, real device, real screen.
- **Risk:** Needs a merchant willing to narrate.
- **Net-new:** New asset type.

**#60 — Comparison without naming names**
Two-column static. Left: "The POS you bought in 2019." Right: "The POS you'll buy in 2026." Both columns are bulleted. No competitor logos.
- **Why:** Comparison without naming = legal-safe and clean.
- **Execution:** Figma split layout.
- **Risk:** Has to be specific enough to feel useful.
- **Net-new:** New angle under T5.

**#61 — Education-led: "How to read your daily Z-report"**
Static + caption. A real Z-report annotated with arrows explaining each section. Caption: "Most owners only look at the bottom line. The middle is where the money is." End: "StoreHub does this for you."
- **Why:** Education-led ads outperform pitch-led when targeted at SMB owners learning the trade.
- **Execution:** Figma. Annotated screenshot.
- **Risk:** Don't be condescending.
- **Net-new:** New concept category (educational static).

**#62 — Mini-Case-Study Card**
Single card: brand name, photo of owner, ONE metric ("served 47% more covers in 90 days"), 12-word quote. No headline. Just facts.
- **Why:** Restraint sells. Adfolio's best testimonial ads are this stripped down.
- **Execution:** Figma quote-card template.
- **Risk:** Need real metrics + permission.
- **Net-new:** Cleaner format under T6.

**#63 — "Calculator" ad (interactive landing page bait)**
Static. A calculator-shaped graphic with the question "How much is your POS actually costing you?" Direct to landing-page calculator.
- **Why:** Tool-based bait converts. Adfolio features Capchase Runway Calculator as an example.
- **Execution:** Figma static + a separate landing page with a real calc widget.
- **Risk:** Calc has to be useful, not gimmicky.
- **Net-new:** New concept under T9.

**#64 — Founder-narrated 6-second cold open**
"I built StoreHub because my mum ran a kopitiam and I watched her lose RM800 a month she didn't know about." Founder face. 6 seconds. End on logo.
- **Why:** Founder story = trust. 6s = Reels pre-roll friendly.
- **Execution:** Founder camera, vertical.
- **Risk:** Has to be true.
- **Net-new:** New asset type.

---

### H. WILDCARDS / EXPERIMENTAL

**#65 — Empty Ad ("Ad goes here. We thought a free Sunday was a better gift.")**
A nearly empty canvas. Tiny text in corner. Small CTA.
- **Why:** Extreme restraint. Adfolio's `/breakdowns` repeatedly praises ads that look like they're hiding.
- **Execution:** Figma. <10 words on canvas.
- **Risk:** Risk of being invisible in feed. Test small.
- **Net-new:** Pure experimental.

**#66 — The Anti-Logo Ad**
StoreHub logo is BIG. Everything else is small. "We thought we'd just say hi. Hi." CTA.
- **Why:** Counter to "logo small, message big" rule. Stands out by violating the trend.
- **Execution:** Figma. Logo = 60% of canvas.
- **Risk:** Brand recall good, conversion uncertain. Test for awareness campaigns only.
- **Net-new:** Experimental.

**#67 — The "Boring" Ad as positioning**
Canvas: "This is a boring ad for a boring product. Boring is what runs a kopitiam quietly for 22 years. StoreHub. RM3.40/day. Boring is the point."
- **Why:** Anti-hype positioning. Resonates with skeptical SMB owners exhausted by SaaS hype.
- **Execution:** Long-copy static. Cream BG, black text. No images.
- **Risk:** Has to feel grounded, not ironic.
- **Net-new:** New positioning angle.

**#68 — Real-Time Counter Ad (animated)**
A live-feel ad: "Right now, 2,347 StoreHub merchants are taking orders. You could be #2,348." Counter ticks up subtly (animated GIF or video).
- **Why:** Live counters create FOMO.
- **Execution:** Lottie or After Effects. <150KB GIF.
- **Risk:** Number has to be defensible.
- **Net-new:** Experimental.

**#69 — Audio-Only ad (Reels with cover image, voice does the work)**
Cover image: cream BG with one line of text. Audio: real merchant 25-second testimonial. Plays in feed when sound is on.
- **Why:** Lots of users have sound on for Reels. Underused channel.
- **Execution:** Real audio + Figma cover.
- **Risk:** Loses sound-off viewers.
- **Net-new:** Experimental.

**#70 — The "Two-Year-Old Ad" Ad**
"This ad is from 2024. We're still running it because it still works. Here's what it said." Cite the original date in the corner. Use a deliberately older aesthetic.
- **Why:** Longevity claim = social proof. Adfolio's `/breakdowns` repeatedly cite "ads running 900+ days" as the strongest signal.
- **Execution:** Figma with intentional 2024 typography.
- **Risk:** Only works once you have a 2-year-old ad to point at.
- **Net-new:** Experimental + meta.

**#71 — Local Festival Anchor ("Hari Raya / CNY / Deepavali edition")**
Festival-themed creative tied to peak F&B periods. Hari Raya: open house catering chaos. CNY: reunion dinner restaurant queue. Deepavali: sweet-shop inventory crunch. Each gets its own artifact ad.
- **Why:** Calendar-anchored creative converts in the run-up to peak season. Zero global SaaS does this in MY.
- **Execution:** Three-creative pack. Festival-specific artifact mimics.
- **Risk:** Cultural authenticity is critical — collaborate with someone from each community.
- **Net-new:** New under T7 (Cultural Pride) — festival-specific is new.

**#72 — "Subtitle-only" ad (no headline, just captions like a dubbed video)**
Photo of an owner with no text on the image itself. ALL text is in the "primary caption" Meta field, formatted as subtitles. "[Owner sighs]" "Used to take me 3 hours." "[Owner laughs]" "Now it's 9 minutes."
- **Why:** Plays with the platform's caption field as the actual ad surface — rare.
- **Execution:** Photo + heavy use of primary text field.
- **Risk:** Some placements truncate primary text.
- **Net-new:** Experimental + format hack.

---

## 4. TOP 10 PRIORITY PICKS (try first, in this order)

1. **#01 LHDN e-Invoice Notice mimic** — Highest expected lift. Touches a real, current MY merchant fear. Compliance > feature pitch. Cheap to make (Figma). Net-new artifact under T11.
2. **#03 Touch-n-Go receipt mimic** — Cheapest to produce. T9 + T11 fusion. Universally legible.
3. **#08 Broker WhatsApp pitching POS leasing** — Direct emotional payoff. Owners *love* this story. WhatsApp template already in T11 — new script, same canvas.
4. **#17 Specific-Number Pattern Interrupt** — Thumbnail-readable. Counters T4's failure by switching from price to **loss-anchor**.
5. **#26 Newspaper Classifieds Column** — Direct evolution of T5 winner (fake job post). Denser, more native. Low execution cost.
6. **#44 Pan-Asian UGC selfie video (Manglish)** — Biggest gap in current playbook. No video UGC in T1–T12 deliverables. Cheap to shoot.
7. **#45 5-card Day-in-the-Life carousel** — Carousels are absent from current playbook. T10 already works as concept; carousel is the new format.
8. **#71 Festival edition pack (Hari Raya/CNY/Deepavali)** — Calendar advantage. No competitor will ship this. Plan ahead 60 days.
9. **#37 "I, [Owner Name], lost / won" founder confession** — Long-copy emotional. Different lever from T6 social proof. Needs one good merchant story.
10. **#13 Cookbook recipe card with cost-per-plate sticky note** — Quick produce. Hyper-specific artifact for F&B. New T11 entry.

---

## 5. WHAT ADFOLIO.DESIGN DOESN'T COVER (look elsewhere)

Adfolio is a sharp Western B2B SaaS swipe file. It is **not** the right reference for:

- **SE Asian / Pan-Asian context.** Zero coverage. Look at: TheBeerCompany MY, Loob Holdings (Tealive) IG, OldTown White Coffee print history, Mamee retro packaging.
- **F&B operator vernacular.** Adfolio sells to RevOps and CFOs. For owner-operator voice, look at: WHTSPC's restaurant-tech Substack, Toast's "Coffee Break" series (US but vertical-correct), Square's SMB blog, and direct merchant DMs on Instagram.
- **Bahasa Malay / Manglish copy.** None. Look at: Malaysian print billboards, Astro radio scripts, GrabFood/FoodPanda MY local seasonal campaigns (for tone, not content).
- **Receipt / printout / artifact textures specific to MY.** None. Look at: r/Malaysia screenshots, local POS forums, your own merchants' real receipts (with permission).
- **Festival / seasonal anchoring.** Zero. Look at: Petronas Raya/CNY YouTube films, RHB/Maybank festival ads (the gold standard for emotional MY brand work).
- **Multi-card carousels and Stories formats.** Adfolio is single-static-image heavy. For carousel structure look at: LinkedIn carousel teardowns (understoryagency.com, tripledart.com), Mobbin for mobile-native sequences.
- **Reels-native vertical video.** Adfolio's `/motion` is mostly looping GIFs, not 9:16 video. Look at: Cards by Loops, Pencil.dev's video templates (still useful even if Zaid kills their static work), Veed.io's social ad gallery, individual merchant TikToks.
- **Audio formats.** None. Look at: Spotify-for-business case studies, audio-first ad agencies (Oxford Road, Veritone One).
- **Owner-photography aesthetic specific to documentary B2B.** Adfolio uses brand-safe stock. Look at: Magnum Photos commercial work, Magnum Pro, Mubi's brand documentaries, restaurant photo zines (Lucky Peach archive).
- **Print-pastiche / newspaper-classifieds / poster-mimic.** Some, but light. Look at: Berita Harian historic ads, classified.archived sites, R/O/B work, MailChimp's print campaign archive.

---

## Appendix A — Adfolio breakdown URLs worth screenshotting manually

Open these in a browser (Adfolio blocks automated fetches) and screenshot the visuals + analysis for the swipe file.

**Highest-leverage** (Diligent Studios own work — clearest signal of Adfolio's aesthetic gold standard):
- `https://www.adfolio.design/breakdowns/97fue0rgkksnf1q` — Diligent Studios #1
- `https://www.adfolio.design/breakdowns/dfelx6pgozofgu0` — Diligent Studios #2

**Highest-signal brand breakdowns** (cross-vertical, repeatedly cited):
- Webflow #1 — `https://www.adfolio.design/breakdowns/nwl27kknhj7bg3j`
- Figma #1 — `https://www.adfolio.design/breakdowns/9gqjule7sayw960`
- Typeform #1 — `https://www.adfolio.design/breakdowns/6dqv6s8i6d2yqfs`
- Typeform #3 — `https://www.adfolio.design/breakdowns/vak16rd53pi58om`
- Typeform #4 — `https://www.adfolio.design/breakdowns/01lhekhpecvtklh`
- Notion #1 — `https://www.adfolio.design/breakdowns/fg6gab4pqwyo3ae`
- Vercel #1 — `https://www.adfolio.design/breakdowns/8ulqrlxmrcp755p`
- Vercel #2 — `https://www.adfolio.design/breakdowns/qx8a05hqwrrycf0`
- Brex #1 — `https://www.adfolio.design/breakdowns/u5mx83pa6c1egee`
- Ramp #1 — `https://www.adfolio.design/breakdowns/20jbersk6tt0zjb`
- Deel #2 — `https://www.adfolio.design/breakdowns/7w6gevp2f77tpvh`
- HiBob #2 — `https://www.adfolio.design/breakdowns/dlf22w96hyzujia`
- Capchase #1 — `https://www.adfolio.design/breakdowns/j7ycj1ior68zcau`
- Lokalise #1 — `https://www.adfolio.design/breakdowns/ho8hdaz7tcx9uhx`
- Lokalise #2 — `https://www.adfolio.design/breakdowns/6h7w0hz4gxbx1lo`
- Weglot #1 — `https://www.adfolio.design/breakdowns/zlp9arxysfegwty`
- Weglot #2 — `https://www.adfolio.design/breakdowns/1g655fs1jf3j0dt`
- Clockwise #1 — `https://www.adfolio.design/breakdowns/gds5owv2iz7uu3j`
- Clockwise #2 — `https://www.adfolio.design/breakdowns/wihyq66ly3r8zi0`
- Clockwise #4 — `https://www.adfolio.design/breakdowns/l1nfrq7ankps7qu`
- SOCi #2 — `https://www.adfolio.design/breakdowns/x2zu3mvbp4yrh5i`
- SOCi #8 — `https://www.adfolio.design/breakdowns/v1x2lckbu8u8rdm`
- Asana #1 — `https://www.adfolio.design/breakdowns/ov58gfkur2xo5uj`
- Intercom #1 — `https://www.adfolio.design/breakdowns/jezqqmpmjese36j`
- Metadata #2 — `https://www.adfolio.design/breakdowns/6o7y8l0nr5ko1nh`
- Mailchimp #1 — `https://www.adfolio.design/breakdowns/gk9d2a1v2pjgbt5`
- Mailchimp #2 — `https://www.adfolio.design/breakdowns/q0n49o8qw3r27om`
- Mailchimp #3 — `https://www.adfolio.design/breakdowns/olfekh3gchmskpj`
- PostHog #1 — `https://www.adfolio.design/breakdowns/fb7etc5mce9f0af`
- Cognism #1 — `https://www.adfolio.design/breakdowns/cgr1imvtbwo8cs7`
- Cognism #3 — `https://www.adfolio.design/breakdowns/5745hlzv2cnpijh`
- Cognism #10 — `https://www.adfolio.design/breakdowns/vhelt0e0ts8lie6`
- Prelude #1 — `https://www.adfolio.design/breakdowns/nstcvju1n7y1xmf`
- reMarkable #1 — `https://www.adfolio.design/breakdowns/q3qzid517m6q11k`

**Tag-filtered views:**
- `https://www.adfolio.design/breakdowns/tags/a9gv9jjgtq3et5t`
- `https://www.adfolio.design/breakdowns/tags/v3pzh530kgfuvj8`

**Landing page section:**
- `https://www.adfolio.design/landing-pages`
- Typeform LP — `https://www.adfolio.design/landing-pages/3rhcus1dh3lmzd8`
- Typeform LP #2 — `https://www.adfolio.design/landing-pages/i11pjgce9nl4q2o`

**Motion section:**
- `https://www.adfolio.design/motion`

**About / philosophy:**
- `https://www.adfolio.design/about`

---

## Appendix B — Cross-referenced swipe files (use these together)

- adkit.so/resources/ads-examples/saas-ad-examples — best taxonomy of hook types
- adkit.so/resources/ads-examples/b2b-ad-examples — best taxonomy of copy structures
- vibemyad.com/blog/10-b2b-static-ad-examples-worth-stealing-from-2026 — best on behavior call-out + meme pattern interrupt
- saashero.net/strategy/social-proof-b2b-saas-ads — best on social proof tactics
- saashero.net/design/best-saas-visuals-b2b-ads — best on visual hierarchy + UI screenshots
- understoryagency.com/blog/linkedin-ad-examples-b2b-saas-creative-teardowns — best on LinkedIn-specific formats
- contentbeta.com/blog/ad-creative-design — best 20-pattern roundup
- contentbeta.com/blog/animated-ads — animation patterns
- b2w.tv/blog/gif-banner-ads — GIF technique library
- diligentstudios.com — Adfolio creators' agency; case studies = literal Adfolio aesthetic

---

## Closing note

The single biggest lesson from Adfolio that StoreHub has already half-learned: **the ad should not look like an ad.** T11 winning proved it. The remaining 60+ ideas above are different shapes of the same core insight. Pick the artifacts your merchants already see in their lives — receipts, WhatsApps, e-invoice portals, broker calls, halal certs, recipe cards — and put the StoreHub message on the back of them.

The second biggest lesson Adfolio cannot teach you: **own the cultural ground Adfolio can't see.** No Western B2B SaaS swipe file will ever produce a Hari Raya open-house artifact ad. That's your unfair advantage.
