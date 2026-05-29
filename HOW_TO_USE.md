# Ad Creative Pipeline — How to Use

## 1. Fill in your config (one-time setup)

Edit these 4 files with your real data:

| File | What goes in it |
|------|----------------|
| `config/brand.json` | Colors, fonts, logo, tone of voice |
| `config/products.json` | What you sell, USPs, social proof, offers |
| `config/audience.json` | Audience segments, pain points, buying triggers |
| `config/campaigns.json` | Platform KPI targets, budgets, ad formats |

---

## 2. Run the pipeline in Claude Code

### First iteration (no performance data yet):
```
/ad-pipeline new
```
This bootstraps a first-run strategy from your config and creates test ads in Pencil.dev.

### With existing ad data:
```
# Drop your CSV exports into data/ad_performance/
# Then:
/ad-pipeline
```

### After launching ads and getting results back:
```
# Drop results CSV into data/iterations/iter_001/
/ad-pipeline results 1
```

### Full loop (results → next iteration):
```
/ad-pipeline loop 1
```

### Check what's been done:
```
/ad-pipeline status
```

---

## 3. Import ad platform CSVs

```bash
# Meta Ads Manager export
python3 scripts/import_results.py path/to/meta_export.csv

# Google Ads export
python3 scripts/import_results.py path/to/google_export.csv --platform google

# TikTok
python3 scripts/import_results.py path/to/tiktok_export.csv --platform tiktok
```

---

## 4. The loop

```
[1] CREATE ads in Pencil.dev → save to ads/batches/batch_NNN/
      ↓
[2] EXPORT + LAUNCH on Meta — mark launched:
      python3 scripts/cycle_check.py --mark-launched
      ↓
[3] WAIT ~14 days (cron fires automatically)
      ↓
[4] ANALYSE — pull from BigQuery, classify winners/losers, find patterns
      ↓
[5] STRATEGY — generate hypotheses + creative briefs for next batch
      ↓
[repeat from 1 — each cycle feeds the next]
```

Each iteration, `data/knowledge_base.json` grows with proven patterns, so every cycle gets smarter.

---

## 5. Batch folder structure

Drop each batch of Pencil.dev `.pen` files here:

```
ads/batches/
  batch_001/   ← current batch
  batch_002/   ← next batch (created after results come in)
  ...
```

Name convention: `batch_NNN` matches `data/iterations/iter_NNN/`

---

## 6. What the agents do

| Agent | What it does |
|-------|-------------|
| `ad-analyst` | Reads CSV data, classifies winners/losers, finds patterns |
| `ad-strategy-agent` | Designs hypotheses and writes creative briefs for next test |
| `ad-creative-generator` | Builds ad frames in Pencil.dev with correct brand/dimensions |
| `ad-results-analyzer` | Validates hypotheses, updates knowledge base, seeds next iteration |

---

## 6. What you need to provide (minimum viable)

- [ ] `config/brand.json` — colors + fonts (minimum)
- [ ] `config/products.json` — at least one product with USPs
- [ ] `config/campaigns.json` — which platforms are active + KPI targets
