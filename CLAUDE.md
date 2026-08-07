## Project at a glance

StoreHub ad creative pipeline. Closed loop: pull Meta performance → analyse winners/losers → generate hypotheses → build creatives in Pencil.dev → launch → repeat every ~14 days. Markets: MY, PH, TH. Brand colors: `#ff9419` orange, `#2f2922` black. Fonts: Barlow + Open Sans.

**Where things live:**

- `config/` — brand, products, audience, campaigns, creative_themes. Source of truth for every agent prompt.
- `agents/` — `ad-analyst`, `ad-strategy-agent`, `ad-creative-generator`, `ad-copy-generator`, `ad-results-analyzer`, `ad-pipeline` (orchestrator skill), `weekly-report-analyst`, `prompts/`.
- `ads/batches/{MARKET}-batch_{NN}/` — per-batch production prompt, PNG renders, `ad-copy.md`, `analysis.md`. Two legacy dirs (`batch_001`, `batch_002`) have no market prefix — leave them; they're referenced by `data/iterations/*/creative_manifest.json` and `data/cycle_state.json`.
- `ads/images/` — every AI-generated image. **Never move or rename** — `.pen` files reference `./images/...` and will break.
- `ads/*.pen` — active Pencil.dev files at root. Filenames have spaces; don't rename once Pencil app has them in recent files.
- `data/iterations/{N}/` — `analysis.json`, `experiment_plan.json`, `creative_manifest.json`, `results.json`, `next_iteration_brief.json`.
- `data/knowledge_base.json` — accumulated proven patterns across iterations.
- `data/cycle_state.json` — current iteration, launch date, 14-day countdown state.
- `Reporting/week_*` — weekly Monday review: `data_dump.md` + action plan.
- `scripts/` — `cycle_check.py` (cron-driven cycle), `import_results.py` (CSV → iteration), `pull_meta_bq.py` / `pull_meta_api.py`, `export_pen.py` (split `.pen` frames → native-res PNGs).

**Primary skill:** `/ad-pipeline` — see `agents/ad-pipeline.md` for the full command surface (`new`, `results N`, `loop N`, `status`, `create N`, `strategy N`, `cycle-status`, `cycle-launch`, `cycle-check`, `cycle-install-cron`).

**Hard "don't break" rules:**

- Never move `ads/images/` or rename files inside it.
- Never rename existing `batch_001` / `batch_002` dirs (referenced from JSON state).
- New batch dirs use `{MARKET}-batch_{NN}` (e.g. `MY-batch_003`, `PH-batch_002`).
- Never auto-push to git. Wait for explicit instruction in the current message.
- All ad dimensions standardised: 1080x1080, 1920x1080, 1080x1920.

---

## Hard creative rules — do NOT repeat (visual + copy)

Two recurring errors, same root cause: positioning StoreHub merchants as downscale/manual instead of modern/aspirational. Enforce in every Pencil prompt, scene description, artifact, and headline:

1. **Venue tier = aspirational, not downmarket.** Show modern, well-fitted cafés, bistros, full-service restaurants, and established retail/boutiques — good lighting, clean interiors, mid-to-upmarket. Pan-Asian / SEA faces, still authentic and documentary, but the merchant looks successful. **Never** low-income/downscale settings: roadside mamak, basic kopitiam, hawker stalls, cluttered or run-down interiors, "cash tin" aesthetics. (The ad-grid themes lean kopitiam/mamak in their `setting` text — translate them UP to modern venues when prompting; do not render them literally.)
2. **Never use the word "till."** Use "cashier", "checkout", "POS", or "the counter" (e.g. "never hit the till" → "never reach the cashier"). "Cash drawer" is fine for reconciliation pain; "till" is not. Avoid old-world cash-register language that frames the business as manual/cash-only.

Cross-project mirror: `~/.claude/CLAUDE.md` (brand essentials) + `~/Code/cranium/reference/storehub/storehub-creative-master.md`.

---

## Post-PR plain-English recap (binding)

After every completed PR — or after the final commit if PRs aren't being used — give Zaid a plain-English recap of what part of the project is now done. Hard rule, not optional.

**Audience: a non-technical reader.** Imagine explaining to someone who has never seen the code and doesn't know what a "module," "API," "library," "schema," "workflow," "framework," "pipeline," or any tech term is.

**Hard rules:**

- **Zero jargon.** No file names, no module/class/library names, no acronyms, no architecture talk.
- **Talk about the product/output, not the code.** Frame it as what the end user / consumer of the output would now experience differently.
- **3–6 sentences, ~80 words max.** Bullets fine. No headers.
- **Concrete and visible.** If nothing user-visible changed, say so honestly in one sentence and frame what it sets up.

**Format:**

> **What just shipped (plain English):**
> <3–6 simple sentences/bullets>

**Cranium journal append (mandatory).** After showing the recap to Zaid, append a one-line plain-English entry to today's Cranium journal at `~/Code/cranium/journal/<YYYY-MM>/<YYYY-MM-DD>.md` (create with a `# <date>` heading if missing; nested month dir — flat journal files are dead) in this format, using the project slug from the Cranium section below:

```
- [storehub-ad-pipeline] <one-sentence plain-English recap>
```

Every push = one journal line. A reminder hook (`/Users/zaidsaad/Code/cranium/scripts/post-pr-recap-hook.sh`, wired via `.claude/settings.local.json`) fires on `git push` / `gh pr create` / `gh pr merge` / `git merge` and reinforces this. Do not rely on the hook — write the recap whether or not the reminder fires.

---

## Cranium (Zaid's external brain)

Before starting substantive work in this session, do this once:

1. Read `~/Code/cranium/CLAUDE.md` for operating principles
2. Read `~/Code/cranium/state/current.md` for what Zaid is currently focused on
3. Read `~/Code/cranium/projects/<this-project-slug>.md` if it exists
4. Read `~/Code/cranium/todos/<this-project-slug>.md` if it exists

If `~/Code/cranium/comms/inbox/` has unprocessed files, mention the count up front.

When you complete a meaningful unit of work, update `~/Code/cranium/todos/<this-project-slug>.md`
and append a one-line note to today's `~/Code/cranium/journal/<YYYY-MM>/<YYYY-MM-DD>.md` (create if missing).

When Zaid says "log this" or "remember this", figure out where it belongs:
- Project-specific learning → `~/Code/cranium/projects/<slug>.md`
- Decision with rationale → `~/Code/cranium/decisions/<today>-<slug>.md`
- Todo → `~/Code/cranium/todos/<slug>.md`
- Random thought to revisit → `~/Code/cranium/state/projects.md` "Idea parking lot"

Project slug for this repo: `storehub-ad-pipeline`
