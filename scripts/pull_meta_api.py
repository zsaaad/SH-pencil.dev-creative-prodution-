#!/usr/bin/env python3
"""
Pull ad performance data from Meta Marketing API.

Setup:
  1. Copy .env.example → .env
  2. Set FACEBOOK_ACCESS_TOKEN (System User token with ads_read + read_insights)
  3. Set FACEBOOK_AD_ACCOUNT_ID (format: act_XXXXXXXXXX)

Usage:
  python3 scripts/pull_meta_api.py --start 2026-03-24 --end 2026-04-07
  python3 scripts/pull_meta_api.py --start 2026-03-24 --end 2026-04-07 --output data/iterations/1/meta_perf.json
"""

import json
import os
import sys
import argparse
import urllib.request
import urllib.parse
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

ACCESS_TOKEN = os.environ.get("FACEBOOK_ACCESS_TOKEN", "")
AD_ACCOUNT_ID = os.environ.get("FACEBOOK_AD_ACCOUNT_ID", "")
API_VERSION = os.environ.get("FACEBOOK_API_VERSION", "v19.0")

# All fields we want per ad
FIELDS = ",".join([
    "ad_id", "ad_name", "adset_name", "campaign_name",
    "impressions", "clicks", "spend", "ctr", "cpc", "cpm", "cpp", "reach", "frequency",
    "actions", "action_values", "cost_per_action_type",
    "unique_clicks", "unique_ctr",
    "outbound_clicks", "outbound_clicks_ctr",
    "video_play_actions",
    "video_p25_watched_actions", "video_p50_watched_actions",
    "video_p75_watched_actions", "video_p100_watched_actions",
])


def api_get(path: str, params: dict) -> dict:
    params["access_token"] = ACCESS_TOKEN
    url = f"https://graph.facebook.com/{API_VERSION}/{path}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return {"error": f"HTTP {e.code}: {body[:500]}"}
    except Exception as e:
        return {"error": str(e)}


def get_action_value(row: dict, action_type: str) -> float:
    for a in row.get("actions", []):
        if a.get("action_type") == action_type:
            return float(a.get("value", 0))
    return 0.0


def get_video_view(row: dict, key: str) -> float:
    for a in row.get(key, []):
        if a.get("action_type") == "video_view":
            return float(a.get("value", 0))
    return 0.0


def pull_insights(date_start: str, date_end: str, output_path: Path) -> bool:
    if not ACCESS_TOKEN or ACCESS_TOKEN == "your_system_user_access_token_here":
        print("  [META] ❌ FACEBOOK_ACCESS_TOKEN not set in .env")
        print("  Get one at: https://developers.facebook.com/tools/explorer/")
        return False

    if not AD_ACCOUNT_ID or AD_ACCOUNT_ID == "act_XXXXXXXXXX":
        print("  [META] ❌ FACEBOOK_AD_ACCOUNT_ID not set in .env")
        return False

    print(f"  [META] Pulling insights {date_start} → {date_end} for {AD_ACCOUNT_ID}")

    params = {
        "level": "ad",
        "fields": FIELDS,
        "time_range": json.dumps({"since": date_start, "until": date_end}),
        "time_increment": 1,  # daily breakdown
        "limit": 500,
    }

    all_rows = []
    path = f"{AD_ACCOUNT_ID}/insights"

    # Handle pagination
    while path:
        data = api_get(path, params)

        if "error" in data:
            print(f"  [META] ❌ API error: {data['error']}")
            return False

        all_rows.extend(data.get("data", []))

        # Check for next page
        paging = data.get("paging", {})
        next_url = paging.get("next")
        if next_url:
            # Extract path and params from next URL for next iteration
            parsed = urllib.parse.urlparse(next_url)
            path = parsed.path.lstrip("/")
            params = dict(urllib.parse.parse_qsl(parsed.query))
            params.pop("access_token", None)  # will be re-added
        else:
            path = None

    print(f"  [META] Fetched {len(all_rows)} rows")

    # Normalize to pipeline format
    ads = []
    for row in all_rows:
        spend = float(row.get("spend", 0) or 0)

        # Lead events — try multiple action types
        leads = (
            get_action_value(row, "lead")
            or get_action_value(row, "onsite_web_lead")
            or get_action_value(row, "offsite_conversion.fb_pixel_lead")
            or get_action_value(row, "contact")
        )

        impressions = float(row.get("impressions", 0) or 0)
        clicks = float(row.get("clicks", 0) or 0)

        ads.append({
            "ad_id": row.get("ad_id"),
            "ad_name": row.get("ad_name"),
            "adset_name": row.get("adset_name"),
            "campaign_name": row.get("campaign_name"),
            "platform": "meta",
            "date": row.get("date_start"),
            "impressions": impressions,
            "clicks": clicks,
            "spend": spend,
            "ctr": float(row.get("ctr", 0) or 0),
            "cpc": float(row.get("cpc", 0) or 0),
            "cpm": float(row.get("cpm", 0) or 0),
            "reach": float(row.get("reach", 0) or 0),
            "frequency": float(row.get("frequency", 0) or 0),
            "leads": leads,
            "cpl": (spend / leads) if leads > 0 else 0,
            "outbound_clicks": float((row.get("outbound_clicks") or [{}])[0].get("value", 0)),
            "video_plays": get_video_view(row, "video_play_actions"),
            "video_p25": get_video_view(row, "video_p25_watched_actions"),
            "video_p50": get_video_view(row, "video_p50_watched_actions"),
            "video_p75": get_video_view(row, "video_p75_watched_actions"),
            "video_p100": get_video_view(row, "video_p100_watched_actions"),
        })

    output = {
        "platform": "meta",
        "pulled_at": datetime.now().isoformat(),
        "date_range": {"start": date_start, "end": date_end},
        "ad_count": len(ads),
        "ads": ads,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2))
    print(f"  [META] ✓ {len(ads)} ad-day rows → {output_path}")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pull Meta Ads performance data")
    parser.add_argument("--start", required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="End date YYYY-MM-DD")
    parser.add_argument("--output", default=None, help="Output JSON path")
    args = parser.parse_args()

    out = (
        Path(args.output)
        if args.output
        else ROOT / "data" / "ad_performance" / f"meta_{args.start}_{args.end}.json"
    )
    sys.exit(0 if pull_insights(args.start, args.end, out) else 1)
