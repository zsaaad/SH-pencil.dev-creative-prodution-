#!/usr/bin/env python3
"""Export every frame in a .pen file as its own ad-ready PNG.

The Pencil CLI clamps multi-frame canvas exports to ~8192px, which thumbnails
1080px frames down to ~120px. This splits the .pen into one frame per temp
file and exports each individually at native resolution.

Usage:
    python scripts/export_pen.py <input.pen> [--out-dir DIR] [--scale N] [--type png|jpeg|webp]

The PALETTE frame (reusable components) is skipped automatically.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def sanitize(name: str) -> str:
    name = re.sub(r"[^\w\-.]+", "_", name).strip("_")
    return re.sub(r"_+", "_", name) or "frame"


def export_pen(
    pen_path: Path,
    out_dir: Path,
    scale: int = 1,
    fmt: str = "png",
    skip_palette: bool = True,
) -> list[Path]:
    doc = json.loads(pen_path.read_text())
    frames = [c for c in doc.get("children", []) if c.get("type") == "frame"]
    if skip_palette:
        frames = [f for f in frames if not f.get("name", "").upper().startswith("PALETTE")]

    if not frames:
        print(f"No frames found in {pen_path}", file=sys.stderr)
        return []

    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for idx, frame in enumerate(frames, start=1):
            single = {k: v for k, v in doc.items() if k != "children"}
            fr = copy.deepcopy(frame)
            fr["x"] = 0
            fr["y"] = 0
            single["children"] = [fr]

            tmp_pen = tmp_dir / f"frame_{idx:03d}.pen"
            tmp_pen.write_text(json.dumps(single))

            name = sanitize(frame.get("name", f"frame_{idx:03d}"))
            dims = f"{frame['width']}x{frame['height']}"
            out_path = out_dir / f"{idx:03d}_{name}_{dims}.{fmt}"

            cmd = [
                "pencil",
                "--in", str(tmp_pen),
                "--export", str(out_path),
                "--export-type", fmt,
                "--export-scale", str(scale),
            ]
            print(f"[{idx:>3}/{len(frames)}] {frame.get('name')} -> {out_path.name}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0 or not out_path.exists():
                print(f"  FAILED: {result.stderr.strip().splitlines()[-1] if result.stderr else 'unknown error'}", file=sys.stderr)
                continue
            written.append(out_path)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pen", type=Path, help="Path to .pen file")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="Output directory (default: ads/exports/<pen-stem>/)")
    parser.add_argument("--scale", type=int, default=1, help="Export scale (default 1)")
    parser.add_argument("--type", default="png", choices=["png", "jpeg", "webp", "pdf"])
    parser.add_argument("--include-palette", action="store_true",
                        help="Include PALETTE frames (skipped by default)")
    args = parser.parse_args()

    if not args.pen.exists():
        print(f"File not found: {args.pen}", file=sys.stderr)
        return 1
    if not shutil.which("pencil"):
        print("`pencil` CLI not on PATH. Install: npm install -g @pencil.dev/cli", file=sys.stderr)
        return 1

    out_dir = args.out_dir or Path("ads/exports") / args.pen.stem
    written = export_pen(args.pen, out_dir, args.scale, args.type, not args.include_palette)
    print(f"\nExported {len(written)} frame(s) to {out_dir}/")
    return 0 if written else 1


if __name__ == "__main__":
    sys.exit(main())
