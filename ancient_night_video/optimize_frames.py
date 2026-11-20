#!/usr/bin/env python3
"""Shrink committed frames without a visible quality loss.

Why this exists: raw generated frames average ~1.6 MB each, so 316 frames is
~509 MB of git history. Kaggle clones the repo to build the video, so the
frames MUST be committed — but that size is hostile to the repo and to clone
time. These frames are flat illustration on 6 palette families, so palettising
to 96 colours is visually lossless (verified against a side-by-side crop) and
lands at ~0.54 MB, roughly 171 MB total.

Usage:
    python3 optimize_frames.py             # optimise all frames in place
    python3 optimize_frames.py --dry-run   # report only
    python3 optimize_frames.py --colors 128
"""
import argparse, glob, os, sys
from PIL import Image

DEFAULT_COLORS = 96


def optimize(path, colors):
    before = os.path.getsize(path)
    with Image.open(path) as im:
        im = im.convert("RGB")
        q = im.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.NONE)
        q.save(path, "PNG", optimize=True, compress_level=9)
    return before, os.path.getsize(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--colors", type=int, default=DEFAULT_COLORS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--glob", default="frames/*.png")
    a = ap.parse_args()

    files = sorted(glob.glob(a.glob))
    if not files:
        sys.exit(f"no files matched {a.glob}")

    tb = ta = 0
    for f in files:
        if a.dry_run:
            tb += os.path.getsize(f)
            continue
        b, af = optimize(f, a.colors)
        tb += b
        ta += af
    if a.dry_run:
        print(f"{len(files)} frames, {tb/1e6:.0f} MB total (dry run, nothing changed)")
        return
    print(f"{len(files)} frames: {tb/1e6:.0f} MB -> {ta/1e6:.0f} MB "
          f"({100*ta/max(tb,1):.0f}% of original)")


if __name__ == "__main__":
    main()
