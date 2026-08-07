# Higgsfield renders — A2 lane (v4 product-led copy), 2026-08-04

Model: `nano_banana_pro`, 9:16, 2k (1536×2752). Copy source: `../../copy-v4-final.md`.
Style/layout reference: `../LP-RCPT.A1.V1.png` (first pass), then `LP-PLAY.A2.V1.png`
(the cleanest frame) as reference for the rest.

| File | Headline | CTA |
|---|---|---|
| `LP-CALC.A2.V1.png` | The sales nobody recorded are the ones costing you. | GET YOUR NUMBER |
| `LP-PLAY.A2.V1.png` | Your new hire can run the counter on their first shift. | RUN THE COUNTER |
| `LP-DAY.A2.V1.png` | See every trading hour without standing at the counter. | SCROLL THE DAY |
| `LP-RCPT.A2.V1.png` | Every sale recorded. E-Invoice ready before you lock up. | WATCH IT PRINT |

Copy deltas vs `copy-v4-final.md` (shortened so the model rendered them without dropping
words — fold back into v4 if these ship):
- LP-DAY headline: "See every trading hour without standing at the counter."
  (was "See every hour your shop trades without standing behind the counter.")
- LP-RCPT headline: "Every sale recorded. E-Invoice ready before you lock up."
  (was "Every sale recorded and e-Invoicing compliant before you lock up.")

Known model quirks hit along the way (all fixed in the shipped frames): dropped/duplicated
words on long headlines; `$` instead of `RM` on rendered POS/receipt UI; percentage layout
instructions rendered as literal on-frame text; one Gemini sparkle watermark. Receipt and
POS line items are decorative gibberish at small size — acceptable, but check before scaling.

Rejected: an earlier pair flagged `nsfw` by the API when the female-subject reference frame
was used; regenerated against the receipt reference instead.
