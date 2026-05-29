---
name: ad-pipeline
description: Run the ad creative pipeline. Triggers the full analyse → strategy → create → results cycle using the ad agents. Usage examples: /ad-pipeline, /ad-pipeline new, /ad-pipeline results 3, /ad-pipeline loop
user_invocable: true
---

The user has invoked the ad creative pipeline skill. Follow these instructions exactly.

## Understand the request

The user may say one of:
- `/ad-pipeline` or `/ad-pipeline new` → run a new full iteration (analyse + strategy + create)
- `/ad-pipeline results [N]` → analyse results for iteration N
- `/ad-pipeline loop [N]` → analyse results for iteration N then kick off iteration N+1
- `/ad-pipeline status` → show the state of all iterations
- `/ad-pipeline create [N]` → re-run just the creative step for iteration N
- `/ad-pipeline strategy [N]` → re-run just the strategy step for iteration N

## Execution

### For `/ad-pipeline` or `/ad-pipeline new`:

1. **Check config first.** Read `config/brand.json` and `config/products.json`. If brand_name is still "YOUR BRAND NAME", tell the user they must fill in their config files first.

2. **Run Ad Analyst agent** with prompt:
   ```
   Check data/ad_performance/ for any CSV or JSON files.
   Read all config files from config/.
   Determine the next iteration number from data/iterations/ directory.
   Run the analysis and save to data/iterations/{N}/analysis.json.
   ```

3. **Run Ad Strategy agent** with prompt:
   ```
   Read data/iterations/{N}/analysis.json.
   Read all config files from config/.
   Read data/knowledge_base.json if it exists.
   Generate experiment plan and save to data/iterations/{N}/experiment_plan.json.
   ```

4. **Run Ad Creative Generator agent** with prompt:
   ```
   Read data/iterations/{N}/experiment_plan.json.
   Read config/brand.json.
   Open or create ads/iteration_{N}.pen in Pencil.dev.
   Design all variants from the experiment plan.
   Save creative manifest to data/iterations/{N}/creative_manifest.json.
   ```

5. Report to user: how many variants were created, where to find them, and what to do next (launch on platform, then run `/ad-pipeline results {N}` with results data).

### For `/ad-pipeline results [N]`:

1. **Run Ad Results Analyzer agent** with prompt:
   ```
   Analyse results for iteration N from data/iterations/{N}/.
   Look for results CSV/JSON files in that directory.
   Update data/knowledge_base.json with learnings.
   Save results to data/iterations/{N}/results.json.
   Save next iteration brief to data/iterations/{N}/next_iteration_brief.json.
   ```

2. Report findings and ask if user wants to run `/ad-pipeline loop {N}` to start the next iteration automatically.

### For `/ad-pipeline status`:

Read all `data/iterations/*/` directories and report:
- Which iterations exist
- Which steps are complete for each (analysis.json ✓, experiment_plan.json ✓, creative_manifest.json ✓, results.json ✓)
- Current knowledge base size
- Top learnings so far

---

## Auto-Research Cycle Commands

These commands control the 2-week performance cycle. Each cycle: ads run for ~14 days → data is pulled → results are analysed → new iteration is created automatically.

### For `/ad-pipeline cycle-status`:

Run:
```
python3 scripts/cycle_check.py --status
```
Report the current iteration number, status (draft/running/complete), days remaining, and whether API credentials are configured.

### For `/ad-pipeline cycle-launch`:

The user has just uploaded the ads to their ad platform. Run:
```
python3 scripts/cycle_check.py --mark-launched
```
This starts the 14-day countdown. Confirm the launch date and data-pull due date back to the user.

If the user wants to backdate the launch (ads were launched earlier), run:
```
python3 scripts/cycle_check.py --launched-on YYYY-MM-DD
```

### For `/ad-pipeline cycle-check`:

Manually trigger a cycle check (same as the daily cron):
```
python3 scripts/cycle_check.py
```
This will pull API data if credentials are set, or report where to drop manual CSVs if not. If the cycle is complete, it will run the results → strategy → create pipeline automatically.

### For `/ad-pipeline cycle-install-cron`:

Install the persistent daily cron so checks happen automatically without Claude:
```
python3 scripts/cycle_check.py --install-cron
```
Confirm the cron is installed and show the user the log path (`logs/cycle_check.log`).

---

## First-Time Setup

If the user is setting up for the first time, guide them:

1. Copy credentials template: `cp .env.example .env`
2. Fill in `FACEBOOK_ACCESS_TOKEN` and `FACEBOOK_AD_ACCOUNT_ID` in `.env`
3. Upload ads to Meta (or other platform)
4. Run `/ad-pipeline cycle-launch` to start the countdown
5. Run `/ad-pipeline cycle-install-cron` for fully automated checks

Always work from the `/Users/zaidsaad/Desktop/Code/Pencil.dev/` directory.
