# StoreHub Ads — Malaysian-English Voice + Rendered-Copy Rules

**The single source of truth for the WORDS that get rendered on any StoreHub MY ad frame.** Every
prompt (the 9:16 variation grid, the family prompts, the stillwater blocks) points here. If a rule here
conflicts with a prompt, **this file wins**.

Grounded in: `brand.json → tone_of_voice` (personality: practical · modern · empowering · authentic ·
upbeat; **avoid: corporate jargon, over-formal language, exaggerated enthusiasm, Western cultural
references**), `compliance-and-positioning.md §5b` (the cash-register-word ban), and the global
CLAUDE.md hard creative rules. Market = **Malaysia → Malaysian / British English, never American.**

---

## RULE A · RENDER ONLY THE TABLE COPY — never the source notes (the #1 leak)
The grid data (`themes-*.json`, `live-*.json`) carries `hook`, `concept`, `setting`, `s2note`, `beats`.
**These are loose internal notes written for video voiceover. They are NOT rendering copy.** They are
full of the banned cash-register word, "cash tin", "kopitiam", "mamak", and American idiom.

- **Render ONLY** the pre-cleaned `Headline / Subcopy / Artifact text / Shock line` given in the prompt's
  per-cell table. That table is the *single source of rendered truth*.
- **NEVER** read, translate, paraphrase, summarise, or echo a hook / concept / setting / s2note / beat
  into a rendered string. If a string is not in the table, it does not go on the frame.
- This replaces the old "strip the bad words out of the hook as you go" instruction — that put the burden
  on mid-generation editing and kept failing. **Don't clean the source. Ignore the source.**

## RULE B · NEVER the cash-register word, or any cash-only language (anywhere a viewer can read)
- ❌ the 4-letter cash-register word (t-i-l-l) · "cash tin" · biscuit-tin / shoebox-of-cash · "ring up
  on the register" · any old-world cash-register framing.
- ❌ **the cash-register VERB family too** — "ring up / rang / rung / ringing up / unrung" (a sale "rang up
  on the register" is the banned frame wearing a different coat). ✅ use **record / recorded / log / logged /
  enter / keyed in / unrecorded**.
- ✅ **"cashier" · "checkout" · "POS" · "the counter".** "Cash drawer" is allowed for a reconciliation
  artifact (the drawer that won't balance); the banned word and "cash tin" are not — they frame the
  business as manual / cash-only / downmarket.
- Applies to EVERY readable string: headline, subcopy, artifact text, sticky note, chat bubble, receipt,
  Z-report, margin note, shock-word, CTA.

## RULE C · MALAYSIAN / BRITISH ENGLISH ONLY — no Americanisms (spelling, vocabulary, idiom)
American English reads foreign to a Malaysian owner and breaks brand.json's "avoid Western cultural
references". Use Malaysian/British forms everywhere.

**Spelling — use the British form. The patterns catch most of it:**
- **`-ize / -ization` → `-ise / -isation`** · **`-yze` → `-yse`** (organise, optimise, customise, analyse, recognise, realise, specialise, prioritise, summarise, maximise, minimise, apologise…). *Exception: keep the official feature name **"Loyalty Program"** verbatim — do NOT change it to "Programme".*
- **`-or` → `-our`** (colour, favourite, behaviour, labour, flavour, honour, neighbour).
- **`-ll-` → `-l-` in -ment/-ing/-ed** (fulfilment, instalment, enrolment, cancelled, travelling).

| ❌ American | ✅ MY/British |
|---|---|
| center, theater | centre, theatre |
| catalog | catalogue |
| check (payment) | cheque |
| license (noun) | licence |
| gray | grey |
| stylized | stylised |
| math | maths |

**Vocabulary — use the MY word** *(exception: brand/feature names stay verbatim — "StoreHub", "Webstore"):*
| ❌ American | ✅ MY/British |
|---|---|
| store (generic shop) | shop / outlet / kedai *(brand "StoreHub" + feature "Webstore" stay)* |
| line (of people) | queue |
| register / cash register | cashier / checkout / counter / POS |
| parking lot | car park |
| cell phone | mobile / handphone |
| vacation | holiday |
| buck / bucks / dollars | ringgit / RM · cents → **sen** |
| mom & pop / mom-and-pop | family-run shop |
| downtown | town |
| gotten | got |
| out of business | shut down / closed down |
| elevator | lift |
| apartment | flat / unit / condo |
| trash / garbage | rubbish |
| truck | lorry |
| storefront | shopfront |
| ring up / rang / rung / unrung *(a sale)* | record / recorded / log / logged / keyed in / unrecorded |
| date `06/15/2026` (MM/DD) | `15/06/2026` or "15 Jun" (DD/MM) |

**Idiom & tone — drop loud American ad-speak (brand: authentic, not exaggerated):**
| ❌ Avoid | ✅ Prefer |
|---|---|
| "blew up" (for popular) | "took off" / "went viral" |
| "didn't blink" / "didn't miss a beat" | "didn't flinch" / "never stalled" / "held steady" |
| "a black box" | "a mystery" / "pure guesswork" |
| "in my pocket" (for reclaimed time) | "back to me" / "mine again" |
| "crush it" / "killing it" / "game-changer" | name the actual outcome ("sold out clean", "every sale recorded") |
| "awesome", "folks", "y'all", "gonna/wanna" | plain MY English |
| corporate jargon: "reach out", "touch base", "circle back", "ballpark", "leverage", "synergy" | say it plainly |

- **Do NOT force Manglish into English ads** — particles like "lah / makan" belong in the BM cut, not the
  EN cut. EN ads are clean, natural Malaysian English; warmth comes from the owner's situation, not slang.
  *(Two carve-outs: **"Boss"** as a term of address is natural MY English and fine; and a **single Malay
  shock-word** as a V3 typographic device — "Bocor.", "Susah.", "Hilang." — is allowed, the one place BM
  enters an EN cut.)*
- Keep it the way a real MY owner talks: practical, a little tired, proud of the win. Short. Concrete.

> **Naming map:** RULE A / B / C here = the variation-grid master's RULE **1a / 1b / 1c** (the grid also has
> RULE 2 = upmarket setting, RULE 3 = build-from-the-cell). Same rules, two docs.

---

## REJECT GATE (run on every rendered frame — fail any = regenerate)
1. **Source-echo:** every rendered string traces to the prompt's per-cell table. No hook/concept/setting
   text leaked onto the frame. *(If you can find the sentence in `themes-*.json` or `live-*.json`, it's wrong.)*
2. **Cash-register word:** the banned 4-letter word, "cash tin", the ring-up verb family, or any cash-only
   framing appears nowhere.
3. **Americanism:** no American spelling, vocabulary, or idiom (scan against the tables above).
4. **Brand/feature names verbatim:** "StoreHub" (one word, capital S + H), official feature names exact.
