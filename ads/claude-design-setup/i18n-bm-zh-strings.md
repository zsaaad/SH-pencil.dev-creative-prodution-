# Existing Ads → BM + Chinese (localise in place)

Localises the 4 built themes (CR-01, HC-06, BW-09, CR-02) into Bahasa Melayu + Simplified
Chinese. **You already have the EN frames — do NOT rebuild.** Paste the snippet below per frame,
swap in the matching BM or ZH strings from the table. Market = MY. Copy is compliance-checked
(no cash-register word / "cash tin"; BM never "tin duit", ZH uses 收银抽屉/抽屉 not 钱箱; StoreHub ·
e-Invoice · LHDN kept verbatim; no competitor names; no invented claims). Reviewed by native BM +
native MY-Chinese passes.

> **Render only these table strings — never the grid hook/concept/setting** (those are dirty source
> notes; see `malaysian-english-voice.md` RULE A). The EN reference is the cleaned table copy, not the
> raw English hook. BM/ZH here are pre-translated from the *cleaned* EN, so the cash-register word and
> American idiom never re-enter through the back door.

## LOCALIZE-IN-PLACE SNIPPET (paste per frame)

```
LOCALIZE THIS EXISTING FRAME — do NOT rebuild it. Keep the layout, composition, photo/artifact,
colours, logo, safe zones and crop EXACTLY as-is. Change ONLY the rendered text to {BAHASA MELAYU
| SIMPLIFIED CHINESE}, using the exact strings I give you below — do not auto-translate or improvise:

  Headline:  «paste BM/ZH headline»
  Subcopy:   «paste BM/ZH transition phrase»
  CTA pill:  «TEMPAH DEMO | 预约演示»
  Price chip:«Dari RM3.40/hari | 每天 RM3.40 起»
  [V3 frames] Shock line / subline: «paste»
  [V2 frames] Artifact/chat/reveal text: «paste»

Keep "StoreHub", "e-Invoice", "LHDN", "RM" and all numbers/equations exactly as written (latin is
correct in both languages). Pan-Asian / SEA faces, brand colours, and the 9:16 safe zones stay
unchanged. For Chinese: render Simplified characters, crisp, with the spacing shown around RM /
e-Invoice / numbers. Headline must still fit ≤ 952px wide and end ≤ y 1090.
```

> If a frame is V1 (photo, no big readable copy beyond headline/subcopy), only the Headline + Subcopy
> + CTA + chip change. V2 = also the artifact/chat text. V3 = the shock word + subline.

## Global anchors (every frame)
| Element | EN | BM | 中文 |
|---|---|---|---|
| Transition — F&B (CR-01/HC-06/BW-09) | From chaos to control. | Dari kalut jadi terkawal. | 从混乱到掌控。 |
| Transition — Retail (CR-02) | From clutter to clarity. | Dari serabut jadi jelas. | 从杂乱到清晰。 |
| CTA | BOOK A DEMO | TEMPAH DEMO | 预约演示 |
| Price chip | From RM3.40/day | Dari RM3.40/hari | 每天 RM3.40 起 |
| Logo / official terms | StoreHub · e-Invoice · LHDN | (unchanged) | (unchanged — keep latin) |

Equations / pure numbers (RM3,200 − RM2,650 = ?, −RM50, 12 → 1, ×4, RM0) stay identical in all languages.

## CR-01 "Where'd It Go" (F&B)
| Slot | BM | 中文 |
|---|---|---|
| A1 H | Penuh sepanjang hari. Separuh order tak masuk sistem. | 整天满座，一半订单根本没入账。 |
| A1 V3 | "1 in 2" / order tak masuk sistem. · *alt word:* Lesap. | "1 in 2" / 订单没入账。 · *alt:* 没了。 |
| A2 H | Chit catat RM3,200. Sistem rekod RM2,650. Mana baki? | 单子写 RM3,200，系统只记 RM2,650。差额去哪了？ |
| A2 V3 | (eqn) / Mana baki? | (eqn) / 差额去哪了？ |
| A3 H | Bos — separuh order ni tak masuk sistem. | 老板，这些订单一半都没进系统。 |
| A3 V2 chat | Bos — separuh ni tak masuk sistem 😬 | 老板，这些一半没进系统 😬 |
| A3 V3 | Bocor. / bocor duit. | 漏钱。 / 一直在漏。 |
| A4 H | Setiap jualan tak direkod, untung yang hilang. | 每一笔没记录的销售，都是留不住的利润。 |
| A4 V2 note | tak direkod | 未记录 |
| A4 V3 | RM0 masuk poket. / dari jualan tak direkod. | 留住 RM0。 / 没记录的每笔销售。 |
| A5 H | Sibuk sepanjang hari. Bank hampir tak gerak. Ada yang bocor. | 忙了一整天，进账几乎没动。肯定在漏。 |
| A5 V2 | hampir tak gerak | 几乎没动 |
| A5 V3 | "RM0" / …itu yang masuk bank hari ni. | "RM0" / …就是今天银行进的钱。 |

## HC-06 "Drawer Of Doom" (F&B)
| Slot | BM | 中文 |
|---|---|---|
| A1 H | Surat e-Invoice dalam laci. Tarikh akhir LHDN tak tunggu. | e-Invoice 信还在抽屉里，LHDN 截止日期可不等你。 |
| A1 V3 | Tarikh akhir e-Invoice: [DATE]. Tinggal [N] hari. / Masih dalam laci? | e-Invoice 截止：[DATE]。剩 [N] 天。 / 还在抽屉里？ |
| A2 H | Belum panik. Cuma tarikh makin dekat. | 还没慌，只是日期越来越近。 |
| A2 V3 | "[N] hari." / sebelum tarikh yang kau asyik buat tak tahu. | "[N] 天。" / 直到你一直逃避的那天。 |
| A3 H | "Nanti la settle e-Invoice." Tapi "nanti" ada hujungnya. | "e-Invoice 迟点搞。" 但"迟点"总会到头。 |
| A3 V2 sticky | e-Invoice — nanti la 🙄 | e-Invoice — 迟点啦 🙄 |
| A3 V3 | "Nanti?" / ada hujungnya. | "迟点？" / 总会到头。 |
| A4 H | Dua belas laci. Dua belas jam berdetik. Satu tarikh akhir. | 十二个抽屉，十二个倒数，一个截止日。 |
| A4 V3 | "12 → 1" / outlet, satu tarikh yang denda semua. | "12 → 1" / 家分店，一个截止日罚全部。 |
| A5 H | Sebelum: tertimbus dalam laci. Selepas: settle, patuh. | 之前：埋在抽屉里。之后：搞定，合规。 |
| A5 V2 | Patuh ✓ / e-Invoice sedia | 已合规 ✓ / e-Invoice 就绪 |
| A5 V3 | "Settle." / sebelum tarikh LHDN. | "搞定。" / 赶在 LHDN 截止前。 |

## BW-09 "Went Viral, Handled" (F&B — breakout, brighter)
| Slot | BM | 中文 |
|---|---|---|
| A1 H | Satu post viral. Checkout langsung tak tersekat. | 一条帖爆了，结账一点没卡。 |
| A1 V2 card | Habis! 🔥 | 售罄 🔥 |
| A1 V3 | Viral. Tenang. | 爆单。淡定。 |
| A2 H | Orang ramai serbu. Skrin dapur tak tertinggal satu pun. | 人潮涌进，厨房屏幕一单没漏。 |
| A2 V3 | 0 tertinggal. | 0 漏单。 |
| A3 H | Viral. Habis dijual kemas — tak pernah terlebih jual. | 爆红，利落售罄——从不超卖。 |
| A3 V2 | Habis dijual — kemas · 0 terlebih jual | 售罄——利落 · 0 超卖 |
| A3 V3 | Habis. | 售罄。 |
| A4 H | Satu reel viral. Satu reminder, semua slot penuh. | 一条 reel 爆了，轻轻一推，每个时段全约满。 |
| A4 V3 | Penuh ditempah. | 全约满。 |
| A5 H | Orang ramai serbu setiap outlet — semua bertahan. | 人潮涌向每家分店——家家撑住。 |
| A5 V2 | Semua outlet ✓ | 所有分店 ✓ |
| A5 V3 | Semua bertahan. | 全撑住。 |

## CR-02 "RM50 Short. Again." (Retail)
| Slot | BM | 中文 |
|---|---|---|
| A1 H | Laci kurang RM50. Kali ketiga minggu ni. | 收银抽屉少了 RM50，这周第三次了。 |
| A1 V3 | "−RM50" / kali ketiga minggu ni. | "−RM50" / 这周第三次。 |
| A2 H | Dah kira empat kali. Masih tak padan. | 数了四遍，还是对不上。 |
| A2 V3 | "×4. Masih tak padan." | "×4。还是不对。" |
| A3 H | Bos, kaunter kurang — takde siapa tahu siapa key in apa. | 老板，收银对不上——没人知道谁收了什么。 |
| A3 V2 chat | laci kurang lagi — siapa tutup tadi? | 抽屉又少了——谁结的账？ |
| A3 V3 | Siapa? | 谁？ |
| A4 H | Jualan kata RM2,400. Laci kata RM2,310. Mana betul? | 销售记 RM2,400，抽屉只有 RM2,310。哪个对？ |
| A4 V3 | (eqn) / mana betul? | (eqn) / 哪个对？ |
| A5 H | Satu laci kurang dalam sepuluh outlet. HQ tak nampak yang mana. | 十家分店里一个抽屉对不上，总部看不出是哪家。 |
| A5 V2 | Outlet 7 dikesan ✓ | 第7分店已标记 ✓ |
| A5 V3 | "10 → 1" / outlet mana yang bocor? | "10 → 1" / 哪家分店在漏？ |

## QA when the localized frames come back
- **Chinese characters render correctly** (Simplified, no garbled/missing glyphs) — image models often mangle CJK; re-gen any frame with broken characters.
- **No cash-register word (t-i-l-l) / cash-only language, no 钱箱** crept back in (it never should — these strings are pre-scrubbed).
- Headline still fits the safe band (ends ≤ y 1090); BM runs longer than EN — size down before it wraps past 3 lines.
- StoreHub / e-Invoice / LHDN / RM still latin and spelled right.
