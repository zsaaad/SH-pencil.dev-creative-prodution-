#!/usr/bin/env python3
"""
Ad Research Cycle Manager — the brain of the auto-research loop.

Runs daily via system cron. Checks if the 2-week run period is complete,
pulls performance data from APIs (or falls back to manual CSVs), then
triggers the full pipeline: results → strategy → create.

─── Setup ────────────────────────────────────────────────────────────────────

1. Copy .env.example → .env and fill in your API credentials
2. Install the system cron (runs daily at 8:47am):
     python3 scripts/cycle_check.py --install-cron

─── Manual commands ──────────────────────────────────────────────────────────

  # Check current status
  python3 scripts/cycle_check.py

  # Mark iteration N as launched (sets the 2-week countdown)
  python3 scripts/cycle_check.py --mark-launched

  # Mark launched with a specific date (e.g. if you launched yesterday)
  python3 scripts/cycle_check.py --mark-launched --launched-on 2026-03-23

  # Force-run the pipeline loop now (ignores date check)
  python3 scripts/cycle_check.py --force

  # Install/update the system cron
  python3 scripts/cycle_check.py --install-cron

─── Cycle flow ───────────────────────────────────────────────────────────────

  [Ads created in Pencil.dev]
      → python3 scripts/cycle_check.py --mark-launched
  [14 days pass]
      → cycle_check.py fires automatically
      → pulls data from Meta/BigQuery (or uses manual CSVs)
      → runs: ad-results-analyzer → ad-strategy-agent → ad-creative-generator
      → iteration N+1 ads created in Pencil.dev
      → sends desktop notification
  [Review ads → upload to platforms]
      → python3 scripts/cycle_check.py --mark-launched
  [Repeat]
"""

import json
import os
import subprocess
import sys
import argparse
from datetime import datetime, date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
ITERATIONS_DIR = DATA_DIR / "iterations"
CYCLE_STATE_PATH = DATA_DIR / "cycle_state.json"
SCRIPTS_DIR = ROOT / "scripts"


# ─── Env ──────────────────────────────────────────────────────────────────────

def load_env():
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())


load_env()


# ─── State ────────────────────────────────────────────────────────────────────

def load_state() -> dict:
    if not CYCLE_STATE_PATH.exists():
        print("❌ No cycle_state.json found. Run /ad-pipeline to create your first iteration.")
        sys.exit(0)
    return json.loads(CYCLE_STATE_PATH.read_text())


def save_state(state: dict):
    state["last_checked"] = date.today().isoformat()
    CYCLE_STATE_PATH.write_text(json.dumps(state, indent=2))


def get_iter_dir(n: int) -> Path:
    """Support both naming formats: plain '1' and 'iter_001'."""
    plain = ITERATIONS_DIR / str(n)
    padded = ITERATIONS_DIR / f"iter_{n:03d}"
    if plain.exists():
        return plain
    if padded.exists():
        return padded
    plain.mkdir(parents=True, exist_ok=True)
    return plain


# ─── Notifications ────────────────────────────────────────────────────────────

def notify(title: str, message: str):
    """macOS desktop notification."""
    subprocess.run(
        ["osascript", "-e",
         f'display notification "{message}" with title "{title}" sound name "Glass"'],
        capture_output=True,
    )


# ─── Data Pull ────────────────────────────────────────────────────────────────

def pull_api_data(iter_state: dict, iter_n: int) -> list:
    """Try to pull from Meta via BigQuery. Returns list of output file paths."""
    launched = iter_state.get("launched_at")
    if not launched:
        return []

    date_start = launched
    date_end = (date.today() - timedelta(days=1)).isoformat()  # yesterday (platform data lag)
    iter_dir = get_iter_dir(iter_n)
    pulled = []

    if os.environ.get("BIGQUERY_PROJECT_ID"):
        out = iter_dir / f"meta_performance_{date_start}_{date_end}.json"
        r = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "pull_meta_bq.py"),
             "--start", date_start, "--end", date_end, "--output", str(out)],
            cwd=str(ROOT), capture_output=True, text=True,
        )
        print(r.stdout.strip())
        if r.returncode == 0 and out.exists():
            pulled.append(str(out))
        elif r.stderr:
            print(f"  [META-BQ] {r.stderr[:300]}")
    else:
        print("  [META-BQ] BIGQUERY_PROJECT_ID not set — skipping auto-pull")

    return pulled


def find_manual_data(iter_n: int) -> list:
    """Find CSVs or JSONs dropped manually into the iteration folder or ad_performance/."""
    iter_dir = get_iter_dir(iter_n)
    perf_dir = DATA_DIR / "ad_performance"
    files = []
    for folder in [iter_dir, perf_dir]:
        if folder.exists():
            files += list(folder.glob("*.csv"))
            files += list(folder.glob("*performance*.json"))
            files += list(folder.glob("*perf*.json"))
    return [str(f) for f in sorted(files, key=lambda x: x.stat().st_mtime, reverse=True)]


# ─── Pipeline ─────────────────────────────────────────────────────────────────

def run_pipeline_loop(iter_n: int, data_path: str) -> bool:
    """Run results(N) → strategy(N+1) → create(N+1) via pipeline.py."""
    print(f"\n  Running pipeline loop for iteration {iter_n}...")
    print(f"  Using data: {data_path}")
    r = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "pipeline.py"),
         "--step", "loop",
         "--iteration", str(iter_n),
         "--results", data_path],
        cwd=str(ROOT),
    )
    return r.returncode == 0


def advance_iteration(state: dict, current_n: int) -> dict:
    """Mark current iteration complete and initialize the next one."""
    today = date.today().isoformat()
    iter_state = state["iterations"][str(current_n)]
    iter_state["status"] = "complete"
    iter_state["completed_at"] = today
    state["iterations"][str(current_n)] = iter_state

    next_n = current_n + 1
    state["current_iteration"] = next_n
    state["total_iterations"] = next_n
    state["iterations"][str(next_n)] = {
        "status": "draft",
        "pen_file": f"ads/iteration_{next_n:03d}.pen",
        "platforms": iter_state.get("platforms", ["meta"]),
        "markets": iter_state.get("markets", ["MY"]),
        "campaign_ids": {},
        "cycle_duration_days": iter_state.get("cycle_duration_days", 14),
        "launched_at": None,
        "data_pull_due": None,
        "completed_at": None,
        "notes": f"Auto-generated from iteration {current_n} results",
    }
    return state


# ─── Status Display ───────────────────────────────────────────────────────────

def print_status(state: dict):
    today = date.today()
    print(f"\n{'─'*60}")
    print(f"  AD RESEARCH CYCLE STATUS — {today}")
    print(f"{'─'*60}")
    for n, it in sorted(state["iterations"].items(), key=lambda x: int(x[0])):
        status = it.get("status", "unknown")
        icon = {"draft": "📝", "running": "🟢", "complete": "✅"}.get(status, "❓")
        print(f"\n  {icon} Iteration {n}  [{status.upper()}]")
        if it.get("launched_at"):
            print(f"     Launched:   {it['launched_at']}")
        if it.get("data_pull_due") and status == "running":
            due = date.fromisoformat(it["data_pull_due"])
            remaining = (due - today).days
            if remaining > 0:
                print(f"     Pull due:   {it['data_pull_due']} ({remaining} days remaining)")
            else:
                print(f"     Pull due:   {it['data_pull_due']} ⚠️ OVERDUE")
        if it.get("completed_at"):
            print(f"     Completed:  {it['completed_at']}")
        if it.get("pen_file"):
            print(f"     Pen file:   {it['pen_file']}")
        if it.get("notes"):
            print(f"     Notes:      {it['notes']}")

    print(f"\n{'─'*60}")
    n = state["current_iteration"]
    it = state["iterations"].get(str(n), {})
    status = it.get("status", "unknown")
    if status == "draft":
        print(f"  Next step: Launch iteration {n} ads on Meta, then run:")
        print(f"    python3 scripts/cycle_check.py --mark-launched")
    elif status == "running":
        due = it.get("data_pull_due", "?")
        print(f"  Cycle running. Auto-pull fires on {due}.")
        print(f"  System cron should be installed — check with: crontab -l")
    elif status == "complete":
        print(f"  Iteration {n} complete. Run /ad-pipeline to start {n+1}.")
    print()


# ─── Cron Install ─────────────────────────────────────────────────────────────

def install_cron():
    """Add a daily 8:47am system cron for this script."""
    script_path = Path(__file__).resolve()
    python = sys.executable
    cron_line = f"47 8 * * * cd {ROOT} && {python} {script_path} >> {ROOT}/logs/cycle_check.log 2>&1"

    # Ensure logs dir exists
    (ROOT / "logs").mkdir(exist_ok=True)
    (ROOT / "logs" / ".gitkeep").touch()

    # Read existing crontab
    r = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    existing = r.stdout if r.returncode == 0 else ""

    if str(script_path) in existing:
        print("  ✅ Cron already installed:")
        for line in existing.splitlines():
            if str(script_path) in line:
                print(f"     {line}")
        return

    new_crontab = existing.rstrip() + f"\n{cron_line}\n"
    subprocess.run(["crontab", "-"], input=new_crontab, text=True, check=True)
    print(f"  ✅ Cron installed: {cron_line}")
    print(f"  Logs at: {ROOT}/logs/cycle_check.log")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ad Research Cycle Manager")
    parser.add_argument("--mark-launched", action="store_true",
                        help="Mark current iteration as launched (starts 2-week countdown)")
    parser.add_argument("--launched-on", default=None,
                        help="Override launch date YYYY-MM-DD (default: today)")
    parser.add_argument("--force", action="store_true",
                        help="Force-run the pipeline loop now (ignores date check)")
    parser.add_argument("--status", action="store_true",
                        help="Show cycle status and exit")
    parser.add_argument("--install-cron", action="store_true",
                        help="Install the daily system cron")
    args = parser.parse_args()

    today = date.today()

    # ── Install cron ───────────────────────────────────────────────────────────
    if args.install_cron:
        install_cron()
        return

    state = load_state()

    # ── Status only ────────────────────────────────────────────────────────────
    if args.status:
        print_status(state)
        return

    # ── Mark launched ──────────────────────────────────────────────────────────
    if args.mark_launched:
        n = state["current_iteration"]
        it = state["iterations"].setdefault(str(n), {})
        launch_date = date.fromisoformat(args.launched_on) if args.launched_on else today
        cycle_days = int(os.environ.get("CYCLE_DURATION_DAYS", it.get("cycle_duration_days", 14)))
        it["status"] = "running"
        it["launched_at"] = launch_date.isoformat()
        it["data_pull_due"] = (launch_date + timedelta(days=cycle_days)).isoformat()
        it["cycle_duration_days"] = cycle_days
        state["iterations"][str(n)] = it
        save_state(state)
        print(f"\n  ✅ Iteration {n} marked as RUNNING")
        print(f"     Launched:  {it['launched_at']}")
        print(f"     Pull due:  {it['data_pull_due']} ({cycle_days} days)")
        print(f"\n  The cron will auto-fire on {it['data_pull_due']}.")
        print(f"  Make sure cron is installed: python3 scripts/cycle_check.py --install-cron\n")
        notify("Ad Pipeline", f"Iteration {n} launched — pull due {it['data_pull_due']}")
        return

    # ── Regular check ──────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  CYCLE CHECK — {today}")
    print(f"{'='*60}")

    n = state["current_iteration"]
    it = state["iterations"].get(str(n), {})
    status = it.get("status", "unknown")

    print(f"  Iteration {n} — {status.upper()}")

    if status == "complete":
        print(f"  Iteration {n} is done. Run /ad-pipeline to start iteration {n+1}.")
        save_state(state)
        return

    if status == "draft":
        print(f"  Ads not launched yet.")
        print(f"  Launch on Meta/TikTok, then: python3 scripts/cycle_check.py --mark-launched")
        save_state(state)
        return

    if status == "running":
        due_str = it.get("data_pull_due")
        if not due_str:
            print("  [ERROR] No data_pull_due in cycle_state.json — re-run with --mark-launched")
            return

        due = date.fromisoformat(due_str)
        days_remaining = (due - today).days

        if days_remaining > 0 and not args.force:
            print(f"  {days_remaining} days until data pull ({due_str})")
            print(f"  Launched: {it.get('launched_at')} → Pull due: {due_str}")
            save_state(state)
            return

        # ── Time to pull ───────────────────────────────────────────────────────
        if args.force:
            print(f"  [--force] Skipping date check. Running now.")
        else:
            print(f"\n  ✅ 2-week cycle complete! Pulling performance data...")

        notify("Ad Research Pipeline", f"Iteration {n} — pulling performance data now")

        # Try API pull
        data_files = pull_api_data(it, n)

        # Fall back to manual CSVs
        if not data_files:
            print("\n  Checking for manually dropped CSV/JSON exports...")
            data_files = find_manual_data(n)
            if data_files:
                print(f"  Found: {data_files[0]}")

        # Nothing found — instruct user
        if not data_files:
            print(f"""
  ⚠️  No performance data found. Choose one:

  OPTION A — Add BigQuery credentials to .env (auto-pull every cycle):
    BIGQUERY_PROJECT_ID=your_gcp_project_id
    BIGQUERY_DATASET=your_dataset_name
    BIGQUERY_TABLE=your_table_name

  OPTION B — Export manually from Meta Ads Manager:
    1. Ads Manager → Reports → Export → Level: Ad
    2. Date range: {it.get('launched_at')} → {today.isoformat()}
    3. Drop the CSV into: data/iterations/{n}/
    4. Re-run: python3 scripts/cycle_check.py

  OPTION C — Import + run:
    python3 scripts/import_results.py path/to/export.csv
    python3 scripts/cycle_check.py
""")
            notify("Ad Pipeline — Action Required", f"Iteration {n}: drop performance CSV to continue")
            save_state(state)
            return

        # Run the loop
        success = run_pipeline_loop(n, data_files[0])

        if success:
            state = advance_iteration(state, n)
            save_state(state)
            next_n = n + 1
            notify("Ad Pipeline", f"Iteration {next_n} ads ready — review in Pencil.dev")
            print(f"""
  ✅ Loop complete! Iteration {next_n} ads are ready.

  1. Review ads in Pencil.dev: ads/iteration_{next_n:03d}.pen
  2. Export and upload to Meta/TikTok
  3. Mark as launched:
       python3 scripts/cycle_check.py --mark-launched
""")
        else:
            print("\n  ❌ Pipeline loop failed. Check output above.")
            notify("Ad Pipeline Error", f"Iteration {n} loop failed — check terminal")
        return

    print(f"  Unknown status '{status}'. Check data/cycle_state.json.")


if __name__ == "__main__":
    main()
