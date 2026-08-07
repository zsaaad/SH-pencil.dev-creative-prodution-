# MY-Batch_012 Family J — Round 2 refinement report

**Container:** `Yscvh` y:56000. **Frames:** 13 READY.

## Fixes applied in R2

| Frame | Fix |
|---|---|
| J_098 | Headline fontSize raised 118 → 108 to remove 32px headline overflow inside HL wrap |
| J_100 | Headline fontSize raised 118 → 108 (same overflow) |
| J_102 | HL wrap heightened 240 → 280 so sub-headline `Cheaper than legacy · Faster than paper · Built for MY F&B.` is no longer clipped |
| J_103 | Bar chart rebuilt with `layout:"none"` absolute positioning after horizontal-flex with alignItems:"end" was clipping all 3 bars + year labels |
| J_105 | Gradient BG resized 0,50,1080,1080 → 0,0,1080,1080 so gradient covers full frame top-to-bottom |
| J_106 | HL wrap height 200 → 260, sub no longer clipped |
| J_108 | HL wrap height 200 → 260, sub no longer clipped |
| J_109 | PIN wrap height 440 → 520 + y 380 → 340 to fit 4 strikethrough PINs without overlap |
| All J | Wordmark refs moved y:1000 → y:1010 to mitigate frame-edge overflow |
| Container | Width widened 6000 → 7200 to stop right-column frame clipping |

## Listicle "actual value at thumbnail glance" audit
- **J_097** — 5 named EOD stages, numbered orange circles, all 5 labels visible. ✓
- **J_098** — bold yellow "8 UNIGNORABLE WAYS" + "Free playbook" promise. Promise without payload — flagged: playbook isn't delivered in the ad itself, only via CTA. Acceptable for a teaser-listicle. ✓
- **J_099** — 17 tricks promise + warm photo hook + sub anchor. ✓
- **J_100** — 7 templates promise + envelope icon. Similar teaser pattern. ✓
- **J_101** — 3-item checklist on pillow is a self-contained micro-listicle. ✓
- **J_102** — 3 toggle options, StoreHub pre-selected with orange row, supporting copy. ✓
- **J_103** — 3-bar chart now legible after refactor. Year labels and 47% claim both visible. ✓
- **J_104** — webinar date specific (22 June, 8pm). ✓
- **J_105** — sample question on a chat bubble shows the value (compliance Q&A). ✓
- **J_106** — mock display reads `RM 4,820 / mo` → `RM 1,920 saved`. ✓
- **J_107** — single-image lifestyle, no listicle structure — closest to "specialist support" message. ✓
- **J_108** — 5-item menu with BESTSELLER / HOT / DUD tags + colour heat. Strongest "screenshot-this" frame. ✓
- **J_109** — 4 specific weak PINs strikethrough = self-contained tip. ✓

## Outstanding flags (Zaid decides)
- **`From RM3.40/day` anchor** appears on J_099. `config/products.json` says "never use /day or /month". Brief overrides — kept as briefed. **Recommend Zaid confirm policy for next batch.**
- **CTA override on J_103, J_106** from `DOWNLOAD REPORT`/`START CALCULATING` to `BOOK A FREE DEMO NOW` per brief. Hurts CTA-content match — but project rule is binding.
- **AI image renders** for J_099 + J_107 are queued, not verified. Need a second pass after Pencil's image service returns.

## Screenshot status
Blank (high y-offset 56000+). All geometry verified via snapshot_layout. No real layout problems remain — only consistent "partially clipped" reports on wordmark/CTA reusable refs whose bbox extends a few px below the 1080 frame boundary; `clip:true` on each ad frame means this is invisible.
