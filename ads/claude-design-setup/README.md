# Claude Design Setup Bundle — StoreHub Ads

Drop-in folder for seeding Claude Design with the StoreHub brand. Use with **`form-fields.md`** as your fill-in guide.

## What's in here

```
claude-design-setup/
├── README.md                  ← you are here
├── form-fields.md             ← exact paste-in copy for each form field
├── brand-snapshot.md          ← condensed human-readable brand brief
├── compliance-and-positioning.md  ← competitor naming rules + 4 verticals + feature taxonomy
├── meta-safe-zones.md         ← Meta safe-zone boundaries for 1:1 / 16:9 / 9:16 + ASCII diagrams
├── family-prompts.md          ← 4 family paste-blocks for Batch 2 concepts
├── fix-prompts.md             ← retroactive fix prompts for already-made ads
├── brand.json                 ← full brand spec (colors, type, logo, imagery, gradients)
├── logos/                     ← 4 official StoreHub logos
│   ├── 01-storehub-wordmark-orange-on-light.png    (light BG default)
│   ├── 02-storehub-wordmark-white-on-dark.png      (dark / orange BG)
│   ├── 03-storehub-wordmark-black-mono.png         (mono / print)
│   └── 04-storehub-h-mark-icon.webp                (icon-only contexts)
└── ad-references/             ← 4 vetted production-quality ad PNGs (policy-compliant)
    ├── champion-no1-pos-simple-1x1.png             (proven launched ad)
    ├── champion-future-proof-restaurant-1x1.png
    ├── champion-storehub-vs-competitor-1x1.png
    └── champion-choose-your-fighter-split-screen.png

    [PENDING] c007-six-vs-one-compliant.png — drop new compliant C007 here once
              regenerated in Claude Design (no GrabFood/FoodPanda/ShopeeFood naming).
```

## How to use

1. Open Claude Design's "Set up your design system" page
2. Open `form-fields.md` side-by-side
3. Paste **Field 1** blurb into the company-name-and-blurb field
4. Skip GitHub (Field 2), code-from-computer (Field 3), and the .fig upload (Field 4)
5. Drag this **entire `claude-design-setup/` folder** into the "Add fonts, logos and assets" field (Field 5)
6. Paste the **Field 6** block into "Any other notes?"

## Choices made (so you know what's deliberate)

- **No `.pen` files.** Claude Design doesn't read Pencil's format. Use the flattened PNGs in `ad-references/`.
- **No font uploads.** Barlow, Open Sans, Caveat, Noto Sans SC, IBM Plex Sans Thai are all on Google Fonts.
- **No code link.** Our `config/*.json` files are configuration, not frontend code — they'd be misread. The full `brand.json` is included as an asset instead.
- **No random batch_002 frames.** Only 4 launched champions retained. Eliminates risk of accidentally shipping a frame with the hallucinated "ScoreHub" typo from C006.
- **Old C007 references removed.** They named GrabFood/FoodPanda/ShopeeFood — out of policy. Removed on 2026-06-04. A compliant replacement will be regenerated in Claude Design and dropped in as `ad-references/c007-six-vs-one-compliant.png`.
- **No hardware photos / illustration library.** Kept in `~/Desktop/Creative/SH Hardware/` and `~/Desktop/Creative/SH ILLUSTRATIONS/`. Add later if scope expands beyond static ads.

## When to update this folder

- Refresh `brand.json` whenever `config/brand.json` changes (sourced from March 2026 brand guideline)
- Swap `ad-references/` whenever a new winning concept ships — Claude Design will anchor on whatever's here. Use the `champion-` prefix for launched winners.
