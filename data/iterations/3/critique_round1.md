# Round 1 Critique — for strategy agent to apply in Round 2

Plan reviewed: `data/iterations/3/experiment_plan.json` (v1, dated 2026-05-28).

The plan is solid in shape — 12 concepts, 50/50 safe/wildcard, unique levers per concept, four wildcard categories represented, anti-recycling claimed. The defects below are surgical, not structural. Refine on these and re-write the file.

## Defects to fix (apply all)

### D1 — Pre-launch gate mismapping
The "Kopitiam LP audit complete" gate currently blocks `C_007` (LHDN tax form, T11) and `C_008` (nasi lemak surreal, T7). C_007 uses no kopitiam/cultural LP. The cultural concepts are **C_006 (mamak)** and **C_008 (nasi lemak)**. Fix the `blocks_concept` list to `["C_006", "C_008"]`.

### D2 — Add Meta-policy + LHDN-backlash gate for C_007
C_007 mocks an LHDN (Inland Revenue Board of Malaysia) tax form. Two real risks:
- Meta deceptive-content auto-rejection (looks like a government document).
- Reputational risk if a real auditor or news outlet picks it up.

Add a new pre-launch gate: *"C_007 LHDN form artwork — legal + brand review for Meta deceptive-content policy and LHDN-impersonation risk; add 'illustrative — not a real LHDN document' microcopy bottom-right."* Owner: legal/brand. Blocks C_007.

### D3 — Add Beep product-manager gate for C_005
C_005 claims "Beep keeps 100% of every order" — a Beep-specific claim, not core POS. Add gate: *"Beep product manager validates the Year-1 RM21,900 commission and Year-2 RM1,240 numbers and the '100% of every order' claim — specifically what fee structure Beep currently charges."* Blocks C_005 (in addition to existing finance gate).

### D4 — Explicit hybrid-theme labelling
Three concepts are deliberate theme hybrids (this is core to the experiment). Add a `secondary_theme` field where applicable, so the next analyst can decompose results:
- C_001: `theme_id: T11`, `secondary_theme: T9` (artifact wrapper × hidden-cost copy)
- C_003: `theme_id: T11`, `secondary_theme: T6` (artifact wrapper × social proof)
- C_010: `theme_id: T1`, `secondary_theme: T11` (gut-punch × artifact-adjacent wrapper — confirm if T11-adjacent, otherwise drop the secondary).

If T1 in this plan is meant to live INSIDE a T11 wrapper, make C_010's `theme_id: T11` with `secondary_theme: T1` for consistency with C_001/C_003. Pick one model and apply consistently across all hybrids.

### D5 — C_006 CTR target is below Batch 1 control
C_006 sets `CTR >= 0.9%`. Batch 1 control (job-post) ran CTR 1.42%. A target below control is incoherent. Raise to **CTR >= 1.2%** (or whatever defensible figure clears control). Update success_metric accordingly.

### D6 — C_002 success_metric mixes QA with KPI
The clause *"format-render quality flagged if WhatsApp UI looks fake at 2-sec glance"* is a QA gate, not a numeric success metric. Remove it from `success_metric` and add it under `pre_launch_gates` as a per-concept QA gate, or add a new top-level field `per_concept_qa_gates` that captures C_002 (WhatsApp UI realism), C_003 (Google review chrome realism), C_007 (LHDN form realism) — all the artifact concepts need this check.

### D7 — Anti-recycling miscounts artifact concepts
Anti-recycling check claims "4 artifact concepts." Actual artifact concepts: C_001 (receipt), C_002 (WhatsApp), C_003 (Google review), C_007 (LHDN), **C_011 (job-post)** = **5 artifact concepts**. Either:
- (a) Accept this is an intentionally T11-heavy batch (the primary research question demands it) — update anti-recycling text to say "5 artifact concepts, deliberate — testing T11 format generalisation across copy angles", or
- (b) Drop one artifact concept and replace with an untested-angle wildcard (Aspirational Self or Value Unlocked never got real runway in Batch 1).

**Recommend (a)** — the primary research question requires the T11 weight. Just be honest about it.

### D8 — C_009 metaphor implies motion in a static format
C_009's hook_visual says *"coins slowly turning into smoke and drifting off-frame"* — that's video motion in a still-image format. Either:
- Specify it as a video concept (and call out 5–15s duration in success_metric), or
- Rewrite the static framing: *"Frozen mid-dissolve — bottom coins half-transformed into stylised smoke wisps, captured at peak visual tension. Single still frame, no motion implied beyond the visual metaphor."*

Pick one and lock it.

### D9 — Tighten primary_research_question
Currently: *"Is the artifact-native format (T11) the true structural driver of the Batch 1 win across copy angles, AND can a milestone+math fusion (T12) lift SQL% from 6.3% to above 15%?"*

That's two questions. The batch's load-bearing question is T11 isolation (5 of 12 concepts ride on it). Tighten to:

*"Is artifact-native format (T11) the true structural driver of the Batch 1 job-post win — generalising across copy angles (cost, social proof, classifieds, tax form, chat) — at SQL% ≥ 25%?"*

Move T12 SQL% lift to the **secondary_research_questions** field (new). Add: *"Does milestone+math fusion (T12) lift SQL% above the 6.3% opening-expenses floor to ≥15%?"* and *"Does the cultural-pride creative survive a fixed LP (T7 mamak)?"* and *"Do untested wildcards (gut-punch, metaphor, absurdist, government-form, entertainment-first) earn enough hook rate to justify next-batch slots?"*

## What to keep unchanged
- 12 concepts, 50/50 split — locked.
- All 12 concept names, themes, headlines, sub-headlines — keep as-is unless directly flagged above.
- Theme distribution math — keep as-is.
- Wildcard category mix — keep as-is.
- Unique levers — keep as-is.

## Output

Re-write `data/iterations/3/experiment_plan.json` v2 applying D1–D9. Same schema, plus the two new optional fields: `secondary_theme` (per concept where applicable) and `per_concept_qa_gates` (top-level array) and `secondary_research_questions` (top-level array). Bump `version: 2` if you add a version field. After writing, respond with one line: `WROTE: data/iterations/3/experiment_plan.json v2 (applied D1–D9)`.
