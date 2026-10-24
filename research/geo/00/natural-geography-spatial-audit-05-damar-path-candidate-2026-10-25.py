#!/usr/bin/env python3
"""Reproduce the image-level Damar path-extent screening figure.

Important: this is NOT a parser for scene.xscene or terrain.bin. It verifies
archived PNG-derived distances and compares the settlement anchors against the
bounding box of ten river_* paths reported by CGEO-MAP-RES-005. The path bbox
is a previously archived statistic; the original path controls are not present
in the current working directory.

Expected inputs beside this script (or set the CLI paths):
  CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png
  natural-geography-spatial-audit-04-damar-phym7-proximity-2026-10-25.csv

Requires Pillow, NumPy, SciPy, Matplotlib.
"""
from pathlib import Path
import argparse
import csv
import hashlib

import numpy as np
from PIL import Image
from scipy.ndimage import distance_transform_edt
import matplotlib.pyplot as plt

EXPECTED = {
    "CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png": "8d99624edc94fce86f0f8ae14d6200dc5582941f638187c6f9f62632a61e1006",
    "natural-geography-spatial-audit-04-damar-phym7-proximity-2026-10-25.csv": "ce3bb62989009c4e7a753a82286420dceff64e2b05064013113786dc1a105553",
}
# Bounding box from the archived RES-005 report for the ten explicitly plotted river_* paths.
RIVER_PATH_BBOX = {"xmin": 87.26, "xmax": 573.38, "ymin": 255.84, "ymax": 535.89}
STABLE_GROUP = "stable_Damar_text_anchor"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--image", default="CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png")
    ap.add_argument("--csv", default="natural-geography-spatial-audit-04-damar-phym7-proximity-2026-10-25.csv")
    ap.add_argument("--out", default="natural-geography-damar-path-candidate-audit-2026-10-25.png")
    args = ap.parse_args()
    image_path, csv_path = Path(args.image), Path(args.csv)
    for p in (image_path, csv_path):
        if not p.exists():
            raise FileNotFoundError(p)
        expected = EXPECTED.get(p.name)
        if expected and sha256(p) != expected:
            raise ValueError(f"SHA-256 mismatch for {p.name}: {sha256(p)} != {expected}")

    # Match the audited plotting panel and the image-level PHYM7 candidate mask.
    image = np.asarray(Image.open(image_path).convert("RGB"))
    panel = image[39:1131, 128:1222]
    mask = ((panel.max(axis=2) - panel.min(axis=2)) <= 8) & (panel.mean(axis=2) < 160)
    mask[:2, :] = False
    mask[-2:, :] = False
    mask[:, :2] = False
    mask[:, -2:] = False
    x_scale = 848 / (mask.shape[1] - 1)
    y_scale = 848 / (mask.shape[0] - 1)
    distances = distance_transform_edt(~mask, sampling=(y_scale, x_scale))

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    anchors = [r for r in rows if r["analysis_group"] == STABLE_GROUP]
    if len(anchors) != 5:
        raise ValueError(f"Expected 5 stable Damar anchors, found {len(anchors)}")

    # Ensure the prior image-derived CSV is reproducible to its 0.001-unit rounding.
    max_abs_error = 0.0
    for r in rows:
        x, y = float(r["x_scene_units"]), float(r["y_scene_units"])
        px = int(round((x / 848) * (mask.shape[1] - 1)))
        py = int(round(((848 - y) / 848) * (mask.shape[0] - 1)))
        recomputed = float(distances[py, px])
        saved = float(r["nearest_PHYM7_mask_distance_scene_units"])
        max_abs_error = max(max_abs_error, abs(recomputed - saved))
    if max_abs_error > 0.0011:
        raise ValueError(f"CSV distance mismatch; maximum absolute error={max_abs_error:.6f}")

    xs = [float(r["x_scene_units"]) for r in anchors]
    ys = [float(r["y_scene_units"]) for r in anchors]
    min_path_y = RIVER_PATH_BBOX["ymin"]
    max_anchor_y = max(ys)
    gap = min_path_y - max_anchor_y
    if gap <= 0:
        raise ValueError("Damar anchors overlap the archived river_* path Y extent; exclusion no longer holds")

    fig, ax = plt.subplots(figsize=(9, 10), dpi=180)
    ax.imshow(panel, extent=(0, 848, 0, 848), origin="upper", interpolation="nearest")
    x0, x1 = RIVER_PATH_BBOX["xmin"], RIVER_PATH_BBOX["xmax"]
    y0, y1 = RIVER_PATH_BBOX["ymin"], RIVER_PATH_BBOX["ymax"]
    ax.plot([x0, x1, x1, x0, x0], [y0, y0, y1, y1, y0], linestyle="--", linewidth=1.5,
            label="10 river_* paths: bounding box")
    ax.scatter(xs, ys, s=42, marker="o", label="Five stable Damar text anchors", zorder=5)
    offsets = {"Hamoshawat": (8, 12), "Mijayit": (8, -15), "Nahlan": (8, -2), "Mabwaz": (8, 5), "Zalm": (8, -3)}
    for r in anchors:
        x, y = float(r["x_scene_units"]), float(r["y_scene_units"])
        dx, dy = offsets[r["english_name"]]
        ax.annotate(r["english_name"], (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.15", facecolor="white", alpha=0.78, linewidth=0))
    xgap = 590
    ax.plot([xgap, xgap], [max_anchor_y, y0], linestyle=":", linewidth=1.4)
    ax.plot([xgap - 5, xgap + 5], [max_anchor_y, max_anchor_y], linewidth=1.2)
    ax.plot([xgap - 5, xgap + 5], [y0, y0], linewidth=1.2)
    ax.annotate(f"{gap:.3f} scene-unit Y separation", xy=(xgap, y0),
                xytext=(xgap + 12, (max_anchor_y + y0) / 2), fontsize=8, va="center",
                arrowprops={"arrowstyle": "-", "linewidth": 0.8})
    ax.text(x0 + 5, y1 - 16, "Extent of the ten plotted river_* paths", fontsize=8,
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8, linewidth=0))
    ax.set_xlim(0, 848)
    ax.set_ylim(0, 848)
    ax.set_xlabel("Scene X (game units)")
    ax.set_ylabel("Scene Y (game units)")
    ax.set_title("Damar text anchors are outside the ten river_* path extent")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.9)
    fig.tight_layout()
    out = Path(args.out)
    fig.savefig(out, bbox_inches="tight")
    print(f"rows_checked={len(rows)}")
    print(f"stable_anchor_count={len(anchors)}")
    print(f"max_csv_distance_abs_error={max_abs_error:.6f}")
    print(f"river_star_bbox_ymin={min_path_y:.3f}")
    print(f"highest_anchor_y={max_anchor_y:.3f}")
    print(f"y_separation_scene_units={gap:.3f}")
    print(f"figure={out.resolve()}")


if __name__ == "__main__":
    main()
