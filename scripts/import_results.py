#!/usr/bin/env python3
"""
Ad Results Importer — normalizes ad platform CSV exports into pipeline format.

Supports: Meta Ads Manager, Google Ads, TikTok Ads Manager, LinkedIn Campaign Manager
"""

import csv
import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"


PLATFORM_COLUMN_MAPS = {
    "meta": {
        "ad_id": ["Ad ID", "Ad id"],
        "ad_name": ["Ad name", "Ad Name"],
        "impressions": ["Impressions"],
        "clicks": ["Link clicks", "Clicks (all)"],
        "spend": ["Amount spent (USD)", "Amount spent"],
        "ctr": ["CTR (link click-through rate)", "CTR (all)"],
        "cpc": ["CPC (cost per link click)", "CPC (all)"],
        "conversions": ["Purchases", "Results", "Leads"],
        "revenue": ["Purchase conversion value", "Conversion values"],
        "cpa": ["Cost per purchase", "Cost per result"],
        "roas": ["Purchase ROAS (return on ad spend)"],
    },
    "google": {
        "ad_id": ["Ad ID"],
        "ad_name": ["Ad", "Ad name"],
        "impressions": ["Impr."],
        "clicks": ["Clicks"],
        "spend": ["Cost"],
        "ctr": ["CTR"],
        "cpc": ["Avg. CPC"],
        "conversions": ["Conversions"],
        "revenue": ["Conv. value"],
        "cpa": ["Cost / conv."],
        "roas": ["Conv. value / cost"],
    },
    "tiktok": {
        "ad_id": ["Ad ID"],
        "ad_name": ["Ad Name"],
        "impressions": ["Impressions"],
        "clicks": ["Clicks"],
        "spend": ["Cost"],
        "ctr": ["CTR"],
        "cpc": ["CPC"],
        "conversions": ["Conversions", "Complete Payment"],
        "revenue": ["Total Purchase Value"],
        "cpa": ["Cost Per Conversion"],
        "roas": ["ROAS"],
    },
    "linkedin": {
        "ad_id": ["Creative ID", "Ad ID"],
        "ad_name": ["Creative name", "Ad name"],
        "impressions": ["Impressions"],
        "clicks": ["Clicks"],
        "spend": ["Amount Spent (USD)", "Cost"],
        "ctr": ["CTR"],
        "cpc": ["Avg. CPC"],
        "conversions": ["Conversions", "Leads"],
        "cpa": ["Cost Per Conversion"],
    }
}


def detect_platform(headers: list[str]) -> str:
    """Auto-detect platform from CSV headers."""
    header_str = " ".join(headers).lower()

    if "purchase roas" in header_str or "link click-through" in header_str:
        return "meta"
    elif "impr." in header_str or "avg. cpc" in header_str:
        return "google"
    elif "complete payment" in header_str or "tiktok" in header_str:
        return "tiktok"
    elif "creative id" in header_str or "linkedin" in header_str:
        return "linkedin"
    return "unknown"


def get_col(row: dict, candidates: list[str]) -> str:
    """Get first matching column value from a row."""
    for col in candidates:
        if col in row and row[col]:
            return row[col]
    return ""


def parse_number(val: str) -> float:
    """Parse a numeric string, handling $, %, commas."""
    if not val:
        return 0.0
    cleaned = val.replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def import_csv(file_path: str, platform: str = None, output_dir: str = None) -> str:
    """Import a platform CSV and save normalized JSON."""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("Error: CSV is empty")
        sys.exit(1)

    headers = list(rows[0].keys())

    # Auto-detect platform
    if not platform or platform == "auto":
        platform = detect_platform(headers)
        print(f"  Detected platform: {platform}")

    if platform not in PLATFORM_COLUMN_MAPS:
        print(f"  Unknown platform '{platform}'. Supported: {list(PLATFORM_COLUMN_MAPS.keys())}")
        # Try generic import
        platform = "meta"

    col_map = PLATFORM_COLUMN_MAPS[platform]

    ads = []
    for row in rows:
        ad = {
            "ad_id": get_col(row, col_map.get("ad_id", [])),
            "ad_name": get_col(row, col_map.get("ad_name", [])),
            "platform": platform,
            "impressions": parse_number(get_col(row, col_map.get("impressions", []))),
            "clicks": parse_number(get_col(row, col_map.get("clicks", []))),
            "spend": parse_number(get_col(row, col_map.get("spend", []))),
            "ctr": parse_number(get_col(row, col_map.get("ctr", []))),
            "cpc": parse_number(get_col(row, col_map.get("cpc", []))),
            "conversions": parse_number(get_col(row, col_map.get("conversions", []))),
            "revenue": parse_number(get_col(row, col_map.get("revenue", []))),
            "cpa": parse_number(get_col(row, col_map.get("cpa", []))),
            "roas": parse_number(get_col(row, col_map.get("roas", []))),
        }

        # Compute missing derived metrics
        if ad["impressions"] > 0 and ad["ctr"] == 0:
            ad["ctr"] = (ad["clicks"] / ad["impressions"]) * 100

        if ad["conversions"] > 0:
            if ad["cpa"] == 0 and ad["spend"] > 0:
                ad["cpa"] = ad["spend"] / ad["conversions"]
            if ad["roas"] == 0 and ad["revenue"] > 0 and ad["spend"] > 0:
                ad["roas"] = ad["revenue"] / ad["spend"]

        ads.append(ad)

    # Determine output path
    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = DATA_DIR / "ad_performance"

    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = out_dir / f"{platform}_{timestamp}.json"

    output = {
        "platform": platform,
        "imported_at": datetime.now().isoformat(),
        "source_file": str(path.name),
        "ad_count": len(ads),
        "ads": ads
    }

    out_path.write_text(json.dumps(output, indent=2))
    print(f"  ✓ Imported {len(ads)} ads → {out_path}")
    return str(out_path)


def main():
    parser = argparse.ArgumentParser(description="Import ad platform CSV exports")
    parser.add_argument("file", help="Path to CSV file from ad platform")
    parser.add_argument("--platform", choices=["meta", "google", "tiktok", "linkedin", "auto"],
                        default="auto", help="Ad platform (default: auto-detect)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output directory (default: data/ad_performance)")
    args = parser.parse_args()

    print(f"\nImporting: {args.file}")
    out = import_csv(args.file, args.platform, args.output)
    print(f"\nDone. Run pipeline with:")
    print(f"  python3 scripts/pipeline.py --data {out}\n")


if __name__ == "__main__":
    main()
