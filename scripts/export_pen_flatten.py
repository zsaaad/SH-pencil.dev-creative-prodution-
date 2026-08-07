#!/usr/bin/env python3
"""Flatten-export every 1080x1080 ad frame in a .pen file as its own PNG.

Differs from export_pen.py: walks the full tree (not just top-level children),
filters to 1080x1080 frames, skips reusable component frames (CTA / Wordmark /
PALETTE), and optionally routes outputs to per-family batch dirs based on the
frame name prefix (B_, C_, ..., N_).

Usage:
    python scripts/export_pen_flatten.py <input.pen> [--out-dir DIR] [--route-by-family]
                                          [--scale N] [--type png|jpeg|webp]
                                          [--only PREFIX] [--dry-run]

--route-by-family routes each frame into ads/batches/MY-batch_NNN/exports/
based on its family-letter prefix. Otherwise everything lands in --out-dir.

--only restricts to frames whose name starts with the given prefix (e.g. --only B_).
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FAMILY_TO_BATCH = {
    "B_": "MY-batch_004",
    "C_": "MY-batch_005",
    "D_": "MY-batch_006",
    "E_": "MY-batch_007",
    "F_": "MY-batch_008",
    "G_": "MY-batch_009",
    "H_": "MY-batch_010",
    "I_": "MY-batch_011",
    "J_": "MY-batch_012",
    "K_": "MY-batch_013",
    "L_": "MY-batch_014",
    "M_": "MY-batch_015",
    "N_": "MY-batch_016",
}

REUSABLE_PATTERNS = ("CTA ", "Wordmark", "PALETTE")

# Generic sub-frame names that aren't real ads — skip even if they happen to be 1080x1080.
GENERIC_NAMES = {"bg", "overlay", "Spreadsheet Grid", "Spreadsheet Grid 1"}


def sanitize(name: str) -> str:
    name = re.sub(r"[^\w\-.]+", "_", name).strip("_")
    return re.sub(r"_+", "_", name) or "frame"


def walk_frames(node, ancestors=()):
    """Yield (frame_dict, ancestor_names) for every frame node in the tree."""
    if node.get("type") == "frame":
        yield node, ancestors
    name = node.get("name", "")
    new_ancestors = ancestors + (name,) if name else ancestors
    for child in (node.get("children", []) or []):
        yield from walk_frames(child, new_ancestors)


def is_ad_frame(frame: dict) -> bool:
    if frame.get("width") != 1080 or frame.get("height") != 1080:
        return False
    name = frame.get("name", "")
    if any(name.startswith(p) or p in name for p in REUSABLE_PATTERNS):
        return False
    if name in GENERIC_NAMES:
        return False
    return True


def family_prefix(name: str) -> str | None:
    m = re.match(r"^([A-N])_", name)
    return f"{m.group(1)}_" if m else None


def export_pen_flatten(
    pen_path: Path,
    out_dir: Path | None,
    repo_root: Path,
    scale: int,
    fmt: str,
    only: str | None,
    route_by_family: bool,
    dry_run: bool,
) -> list[Path]:
    doc = json.loads(pen_path.read_text())

    ad_frames = []
    for child in doc.get("children", []):
        for frame, ancestors in walk_frames(child):
            if not is_ad_frame(frame):
                continue
            if only and not frame.get("name", "").startswith(only):
                continue
            ad_frames.append((frame, ancestors))

    if not ad_frames:
        print(f"No ad frames matched in {pen_path}", file=sys.stderr)
        return []

    print(f"Found {len(ad_frames)} ad frames to export.\n")
    written: list[Path] = []

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for idx, (frame, ancestors) in enumerate(ad_frames, start=1):
            name = frame.get("name", f"frame_{idx:03d}")
            safe_name = sanitize(name)

            if route_by_family:
                fam = family_prefix(name)
                if fam and fam in FAMILY_TO_BATCH:
                    target_dir = repo_root / "ads" / "batches" / FAMILY_TO_BATCH[fam] / "exports"
                else:
                    target_dir = repo_root / "ads" / "batches" / "MY-batch_unknown" / "exports"
            else:
                target_dir = out_dir or (repo_root / "ads" / "batches" / "_exports")

            target_dir.mkdir(parents=True, exist_ok=True)
            out_path = target_dir / f"{idx:03d}_{safe_name}.{fmt}"

            if dry_run:
                print(f"[{idx:>3}/{len(ad_frames)}] (dry) {name!r} -> {out_path}")
                continue

            single = {k: v for k, v in doc.items() if k != "children"}
            fr = copy.deepcopy(frame)
            fr["x"] = 0
            fr["y"] = 0
            single["children"] = [fr]

            tmp_pen = tmp_dir / f"frame_{idx:03d}.pen"
            tmp_pen.write_text(json.dumps(single))

            cmd = [
                "pencil",
                "--in", str(tmp_pen),
                "--export", str(out_path),
                "--export-type", fmt,
                "--export-scale", str(scale),
            ]
            print(f"[{idx:>3}/{len(ad_frames)}] {name!r} -> {out_path.name}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0 or not out_path.exists():
                err = result.stderr.strip().splitlines()[-1] if result.stderr else "unknown error"
                print(f"  FAILED: {err}", file=sys.stderr)
                continue
            written.append(out_path)

    print(f"\nWrote {len(written)} files.")
    return written


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pen", type=Path, help="Input .pen file")
    ap.add_argument("--out-dir", type=Path, default=None,
                    help="Output directory (ignored if --route-by-family is set)")
    ap.add_argument("--route-by-family", action="store_true",
                    help="Route into ads/batches/MY-batch_NNN/exports/ by frame name prefix")
    ap.add_argument("--scale", type=int, default=1)
    ap.add_argument("--type", default="png", choices=["png", "jpeg", "webp", "pdf"])
    ap.add_argument("--only", default=None,
                    help="Only export frames whose name starts with this prefix (e.g. B_)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    export_pen_flatten(
        pen_path=args.pen.resolve(),
        out_dir=args.out_dir,
        repo_root=repo_root,
        scale=args.scale,
        fmt=args.type,
        only=args.only,
        route_by_family=args.route_by_family,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
