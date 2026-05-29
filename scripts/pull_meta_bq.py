#!/usr/bin/env python3
"""
Pull ad performance data from BigQuery (Meta/Facebook Ads).

Setup:
  1. Copy .env.example → .env
  2. Set BIGQUERY_PROJECT_ID
  3. Set BIGQUERY_DATASET
  4. Authenticate via: gcloud auth application-default login
     OR set GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

Usage:
  python3 scripts/pull_meta_bq.py --start 2026-03-24 --end 2026-04-07
  python3 scripts/pull_meta_bq.py --start 2026-03-24 --end 2026-04-07 --output data/iterations/1/meta_perf.json
"""

import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent


def load_env():
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())


load_env()

# ─── TODO: Fill these in ───────────────────────────────────────────────────────
PROJECT_ID = os.environ.get("BIGQUERY_PROJECT_ID", "YOUR_GCP_PROJECT_ID")
DATASET    = os.environ.get("BIGQUERY_DATASET",    "YOUR_DATASET_NAME")
TABLE      = os.environ.get("BIGQUERY_TABLE",      "YOUR_TABLE_NAME")

# Column name mapping — update these to match your actual BQ schema
COL = {
    "ad_id":          "ad_id",           # TODO: confirm column name
    "ad_name":        "ad_name",         # TODO: confirm column name
    "adset_name":     "adset_name",      # TODO: confirm column name
    "campaign_name":  "campaign_name",   # TODO: confirm column name
    "date":           "date",            # TODO: confirm column name (date of the row)
    "impressions":    "impressions",     # TODO: confirm column name
    "clicks":         "clicks",          # TODO: confirm column name
    "spend":          "spend",           # TODO: confirm column name
    "ctr":            "ctr",             # TODO: confirm column name (or set to None to compute)
    "cpc":            "cpc",             # TODO: confirm column name (or set to None to compute)
    "cpm":            "cpm",             # TODO: confirm column name (or set to None to compute)
    "reach":          "reach",           # TODO: confirm column name
    "frequency":      "frequency",       # TODO: confirm column name
    "leads":          "leads",           # TODO: confirm column name (conversions / lead events)
    "outbound_clicks": "outbound_clicks", # TODO: confirm column name (or set to None if absent)
    "video_plays":    "video_plays",     # TODO: confirm column name (or set to None if absent)
    "video_p25":      "video_p25",       # TODO: confirm column name (or set to None if absent)
    "video_p50":      "video_p50",       # TODO: confirm column name (or set to None if absent)
    "video_p75":      "video_p75",       # TODO: confirm column name (or set to None if absent)
    "video_p100":     "video_p100",      # TODO: confirm column name (or set to None if absent)
}
# ──────────────────────────────────────────────────────────────────────────────


def build_query(date_start: str, date_end: str) -> str:
    # Build SELECT list — skip any columns mapped to None
    select_cols = ", ".join(
        f"`{bq_col}` AS {field}"
        for field, bq_col in COL.items()
        if bq_col is not None
    )

    return f"""
        SELECT
            {select_cols}
        FROM
            `{PROJECT_ID}.{DATASET}.{TABLE}`
        WHERE
            `{COL['date']}` BETWEEN '{date_start}' AND '{date_end}'
        ORDER BY
            `{COL['date']}` ASC
    """


def pull_insights(date_start: str, date_end: str, output_path: Path) -> bool:
    try:
        from google.cloud import bigquery
    except ImportError:
        print("  [META-BQ] ❌ google-cloud-bigquery not installed.")
        print("  Run: pip install google-cloud-bigquery")
        return False

    if PROJECT_ID == "YOUR_GCP_PROJECT_ID":
        print("  [META-BQ] ❌ BIGQUERY_PROJECT_ID not set in .env")
        return False

    print(f"  [META-BQ] Querying {PROJECT_ID}.{DATASET}.{TABLE} for {date_start} → {date_end}")

    client = bigquery.Client(project=PROJECT_ID)
    query = build_query(date_start, date_end)

    try:
        rows = list(client.query(query).result())
    except Exception as e:
        print(f"  [META-BQ] ❌ Query failed: {e}")
        return False

    print(f"  [META-BQ] Fetched {len(rows)} rows")

    def fval(row, field, default=0.0):
        """Safely get a float from a BQ row, returning default if column is None/absent."""
        if COL.get(field) is None:
            return default
        v = getattr(row, field, None)
        return float(v) if v is not None else default

    ads = []
    for row in rows:
        spend  = fval(row, "spend")
        leads  = fval(row, "leads")
        clicks = fval(row, "clicks")
        imps   = fval(row, "impressions")

        ads.append({
            "ad_id":           getattr(row, "ad_id", None),
            "ad_name":         getattr(row, "ad_name", None),
            "adset_name":      getattr(row, "adset_name", None),
            "campaign_name":   getattr(row, "campaign_name", None),
            "platform":        "meta",
            "date":            str(getattr(row, "date", "")),
            "impressions":     imps,
            "clicks":          clicks,
            "spend":           spend,
            # Use BQ column if available, else compute
            "ctr":             fval(row, "ctr")  or (clicks / imps * 100 if imps else 0),
            "cpc":             fval(row, "cpc")  or (spend / clicks if clicks else 0),
            "cpm":             fval(row, "cpm")  or (spend / imps * 1000 if imps else 0),
            "reach":           fval(row, "reach"),
            "frequency":       fval(row, "frequency"),
            "leads":           leads,
            "cpl":             (spend / leads) if leads > 0 else 0,
            "outbound_clicks": fval(row, "outbound_clicks"),
            "video_plays":     fval(row, "video_plays"),
            "video_p25":       fval(row, "video_p25"),
            "video_p50":       fval(row, "video_p50"),
            "video_p75":       fval(row, "video_p75"),
            "video_p100":      fval(row, "video_p100"),
        })

    output = {
        "platform":   "meta",
        "source":     "bigquery",
        "pulled_at":  datetime.now().isoformat(),
        "date_range": {"start": date_start, "end": date_end},
        "ad_count":   len(ads),
        "ads":        ads,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2))
    print(f"  [META-BQ] ✓ {len(ads)} ad-day rows → {output_path}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull Meta Ads performance data from BigQuery")
    parser.add_argument("--start",  required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end",    required=True, help="End date YYYY-MM-DD")
    parser.add_argument("--output", default=None,  help="Output JSON path")
    args = parser.parse_args()

    out = (
        Path(args.output)
        if args.output
        else ROOT / "data" / "ad_performance" / f"meta_{args.start}_{args.end}.json"
    )
    sys.exit(0 if pull_insights(args.start, args.end, out) else 1)
