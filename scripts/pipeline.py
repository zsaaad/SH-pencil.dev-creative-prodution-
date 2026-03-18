#!/usr/bin/env python3
"""
Ad Creative Pipeline Orchestrator
Runs: Analyse → Strategy → Create → (manual: launch ads) → Results → Loop
"""

import json
import os
import subprocess
import sys
import argparse
from pathlib import Path
from datetime import datetime

# ─── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
ITERATIONS_DIR = DATA_DIR / "iterations"
CONFIG_DIR = ROOT / "config"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_next_iteration() -> int:
    """Find the next iteration number."""
    ITERATIONS_DIR.mkdir(parents=True, exist_ok=True)
    existing = [d for d in ITERATIONS_DIR.iterdir() if d.is_dir() and d.name.startswith("iter_")]
    return len(existing) + 1


def get_iteration_dir(n: int) -> Path:
    d = ITERATIONS_DIR / f"iter_{n:03d}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def run_claude_agent(agent_name: str, prompt: str, cwd: Path = ROOT) -> str:
    """Run a Claude Code subagent via CLI and return output."""
    cmd = [
        "claude",
        "--print",
        "--agent", agent_name,
        prompt
    ]
    print(f"\n{'='*60}")
    print(f"  Running agent: {agent_name}")
    print(f"  Prompt: {prompt[:100]}...")
    print(f"{'='*60}")

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(cwd)
    )

    if result.returncode != 0:
        print(f"  [WARN] Agent returned code {result.returncode}")
        print(f"  stderr: {result.stderr[:500]}")

    output = result.stdout
    print(f"  Output length: {len(output)} chars")
    return output


def check_config() -> bool:
    """Validate that config files are filled in."""
    brand = json.loads((CONFIG_DIR / "brand.json").read_text())
    if brand["brand_name"] == "YOUR BRAND NAME":
        print("ERROR: Please fill in config/brand.json with your brand details.")
        return False

    products = json.loads((CONFIG_DIR / "products.json").read_text())
    if products["products"][0]["name"] == "Product Name":
        print("ERROR: Please fill in config/products.json with your products.")
        return False

    return True


def step_analyse(iteration: int, performance_data_path: str = None) -> bool:
    """Step 1: Analyse current ad performance."""
    iter_dir = get_iteration_dir(iteration)

    if performance_data_path:
        prompt = f"""Analyse the ad performance data at {performance_data_path}.
Read config files from {CONFIG_DIR}.
Save analysis to {iter_dir}/analysis.json.
Iteration number: {iteration}."""
    else:
        # Check for data in default location
        data_files = list((DATA_DIR / "ad_performance").glob("*.csv")) + \
                     list((DATA_DIR / "ad_performance").glob("*.json"))

        if not data_files:
            print("\n[STEP 1] No ad performance data found.")
            print(f"  Drop CSV/JSON exports into: {DATA_DIR}/ad_performance/")
            print("  Or pass --data path/to/file.csv")

            # On first iteration, create a placeholder analysis to bootstrap
            if iteration == 1:
                print("  First iteration — creating bootstrap analysis from config...")
                bootstrap = {
                    "iteration": 1,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "summary": {"total_ads_analyzed": 0, "winners": 0, "challengers": 0, "losers": 0, "fatigued": 0},
                    "top_performers": [],
                    "bottom_performers": [],
                    "patterns": {"winning_elements": [], "losing_elements": [], "untested_angles": ["ALL - first iteration, no prior data"]},
                    "fatigued_ads": [],
                    "recommendations": ["Run first-ever creative test — no prior data to constrain strategy. Focus on testing 3+ distinct angles across all core value propositions."]
                }
                (iter_dir / "analysis.json").write_text(json.dumps(bootstrap, indent=2))
                return True
            return False

        data_path = data_files[0]
        prompt = f"""Analyse the ad performance data at {data_path}.
Read config files from {CONFIG_DIR}.
Save analysis to {iter_dir}/analysis.json.
Iteration number: {iteration}."""

    run_claude_agent("ad-analyst", prompt)

    if not (iter_dir / "analysis.json").exists():
        print(f"  [ERROR] analysis.json not created. Check agent output.")
        return False

    print(f"  ✓ Analysis saved to {iter_dir}/analysis.json")
    return True


def step_strategy(iteration: int) -> bool:
    """Step 2: Generate experiment plan."""
    iter_dir = get_iteration_dir(iteration)
    kb_path = DATA_DIR / "knowledge_base.json"

    kb_context = f"Knowledge base at {kb_path} (if it exists, apply learnings)." if kb_path.exists() else "No knowledge base yet — first iteration."

    prompt = f"""Read the ad analysis from {iter_dir}/analysis.json.
Read all config files from {CONFIG_DIR}.
{kb_context}
Generate a creative experiment plan and save to {iter_dir}/experiment_plan.json.
Iteration number: {iteration}."""

    run_claude_agent("ad-strategy-agent", prompt)

    if not (iter_dir / "experiment_plan.json").exists():
        print(f"  [ERROR] experiment_plan.json not created.")
        return False

    plan = json.loads((iter_dir / "experiment_plan.json").read_text())
    total = plan.get("total_new_variants", 0)
    print(f"  ✓ Strategy saved — {total} variants planned")
    return True


def step_create(iteration: int) -> bool:
    """Step 3: Create ads in Pencil.dev."""
    iter_dir = get_iteration_dir(iteration)

    prompt = f"""Read the experiment plan from {iter_dir}/experiment_plan.json.
Read brand guidelines from {CONFIG_DIR}/brand.json.
Open or create Pencil.dev file: ads/iteration_{iteration:03d}.pen
Design all variants from the experiment plan with correct dimensions and brand styling.
Save creative manifest to {iter_dir}/creative_manifest.json.
Iteration number: {iteration}."""

    run_claude_agent("ad-creative-generator", prompt)

    if not (iter_dir / "creative_manifest.json").exists():
        print(f"  [ERROR] creative_manifest.json not created.")
        return False

    manifest = json.loads((iter_dir / "creative_manifest.json").read_text())
    total = manifest.get("total_created", 0)
    pen_file = manifest.get("pen_file", "")
    print(f"  ✓ {total} ad creatives created in {pen_file}")
    return True


def step_results(iteration: int, results_data_path: str = None) -> bool:
    """Step 4: Analyse results of a completed iteration."""
    iter_dir = get_iteration_dir(iteration)
    kb_path = DATA_DIR / "knowledge_base.json"

    if results_data_path:
        data_ref = f"Results data at {results_data_path}."
    else:
        results_files = list(iter_dir.glob("*results*.csv")) + list(iter_dir.glob("*results*.json"))
        if not results_files:
            print(f"  Drop results CSV/JSON into {iter_dir}/ and re-run with --step results")
            return False
        data_ref = f"Results data at {results_files[0]}."

    prompt = f"""{data_ref}
Read experiment plan from {iter_dir}/experiment_plan.json.
Read creative manifest from {iter_dir}/creative_manifest.json.
Analyse results, update knowledge base at {kb_path}, and save:
- {iter_dir}/results.json
- {iter_dir}/next_iteration_brief.json
Iteration number: {iteration}."""

    run_claude_agent("ad-results-analyzer", prompt)

    if not (iter_dir / "results.json").exists():
        print(f"  [ERROR] results.json not created.")
        return False

    results = json.loads((iter_dir / "results.json").read_text())
    summary = results.get("summary", {})
    print(f"  ✓ Results: {summary.get('confirmed', 0)} confirmed, {summary.get('disproven', 0)} disproven, {summary.get('inconclusive', 0)} inconclusive")
    return True


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Ad Creative Pipeline — analyse → strategize → create → results → loop"
    )
    parser.add_argument(
        "--step",
        choices=["all", "analyse", "strategy", "create", "results", "loop"],
        default="all",
        help="Which step to run (default: all = analyse+strategy+create)"
    )
    parser.add_argument("--iteration", type=int, default=None,
                        help="Specific iteration number (default: auto-detect next)")
    parser.add_argument("--data", type=str, default=None,
                        help="Path to ad performance data CSV/JSON")
    parser.add_argument("--results", type=str, default=None,
                        help="Path to results data CSV/JSON for --step results")
    parser.add_argument("--loops", type=int, default=1,
                        help="Number of strategy→create loops to run (requires results data)")

    args = parser.parse_args()

    # ── Validate config ────────────────────────────────────────────────────────
    if not check_config():
        sys.exit(1)

    # ── Determine iteration ────────────────────────────────────────────────────
    iteration = args.iteration or get_next_iteration()

    print(f"\n{'#'*60}")
    print(f"  AD CREATIVE PIPELINE — Iteration {iteration}")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'#'*60}")

    # ── Run requested step(s) ──────────────────────────────────────────────────
    if args.step in ("all", "analyse"):
        if not step_analyse(iteration, args.data):
            if args.step == "all":
                print("\n[WARN] Analysis step incomplete. Continuing with strategy anyway...")
            else:
                sys.exit(1)

    if args.step in ("all", "strategy"):
        if not step_strategy(iteration):
            sys.exit(1)

    if args.step in ("all", "create"):
        if not step_create(iteration):
            sys.exit(1)

    if args.step == "results":
        if not step_results(iteration, args.results):
            sys.exit(1)

    if args.step == "loop":
        # Run results for current iteration, then kick off next
        if not step_results(iteration, args.results):
            sys.exit(1)

        next_iter = iteration + 1
        print(f"\n  → Starting iteration {next_iter}")
        if not step_analyse(next_iter):
            sys.exit(1)
        if not step_strategy(next_iter):
            sys.exit(1)
        if not step_create(next_iter):
            sys.exit(1)

    print(f"\n{'#'*60}")
    print(f"  PIPELINE COMPLETE — Iteration {iteration}")
    print(f"  Files in: {get_iteration_dir(iteration)}")
    print(f"{'#'*60}\n")


if __name__ == "__main__":
    main()
