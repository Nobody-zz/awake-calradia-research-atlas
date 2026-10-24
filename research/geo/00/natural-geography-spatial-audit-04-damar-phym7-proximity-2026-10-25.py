#!/usr/bin/env python3
"""Image-level proximity audit for Nahasa/Damar text anchors.

This script does NOT parse terrain.bin, scene.xscene, or raw PHYM data. It
reproduces an exploratory measurement from the archived rendered PHYM7 map and
heightfield PNGs. Distances are game-scene units, not real-world units.

Inputs expected beside this script:
  SandBox.zip
  CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png
  CGEO-MAP-RES-005_双版本同尺度高程图.png

Requires Pillow, NumPy, SciPy, Matplotlib.
"""
from pathlib import Path
import csv
import hashlib
import zipfile
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image
from matplotlib import colormaps
from scipy.ndimage import distance_transform_edt, label

ROOT = Path(__file__).resolve().parent
ZIP_PATH = ROOT / "SandBox.zip"
RIVER_PNG = ROOT / "CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png"
HEIGHT_PNG = ROOT / "CGEO-MAP-RES-005_双版本同尺度高程图.png"
OUT_CSV = ROOT / "natural-geography-spatial-audit-04-damar-phym7-proximity-2026-10-25.csv"

EXPECTED_SHA256 = {
    "SandBox.zip": "54c358e5b318ffeda8a69ce41a7e665f3b9bef06a6e49b142a972c80ea9c1d55",
    "CGEO-MAP-RES-005_原版河流路径与PHYM7叠加.png": "8d99624edc94fce86f0f8ae14d6200dc5582941f638187c6f9f62632a61e1006",
    "CGEO-MAP-RES-005_双版本同尺度高程图.png": "a5e58c6937ead7726bdca7bed69feb4943a5c2213babf51fe50e9d37410eedd1",
}


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


for p in (ZIP_PATH, RIVER_PNG, HEIGHT_PNG):
    if not p.exists():
        raise FileNotFoundError(f"Missing input: {p}")
    actual = sha256(p)
    expected = EXPECTED_SHA256[p.name]
    if actual != expected:
        raise ValueError(f"SHA-256 mismatch for {p.name}: {actual} != {expected}")

# Extract Aserai settlement entities from the archived official SandBox XML.
with zipfile.ZipFile(ZIP_PATH) as zf:
    xml_bytes = zf.read("Modules/SandBox/ModuleData/settlements.xml")
root = ET.fromstring(xml_bytes)
entities = []
for node in root.findall(".//Settlement"):
    if node.get("culture") != "Culture.aserai" or not node.get("posX") or not node.get("posY"):
        continue
    sid = node.get("id", "")
    name = node.get("name", "").split("}")[-1]
    entities.append({
        "entity_id": sid,
        "entity_type": "castle_village" if sid.startswith("castle_village_") else sid.split("_")[0],
        "english_name": name,
        "x": float(node.get("posX")),
        "y": float(node.get("posY")),
    })

# The archived river image's audited plotting frame is [128,39,1222,1131],
# mapped to X/Y = 0..848 scene units. The gray PHYM7 layer is approximated by
# near-neutral pixels; colored named Paths are not included in this mask.
river_img = np.asarray(Image.open(RIVER_PNG).convert("RGB"))
river_panel = river_img[39:1131, 128:1222]
mask = ((river_panel.max(axis=2) - river_panel.min(axis=2)) <= 8) & (river_panel.mean(axis=2) < 160)
mask[:2, :] = False
mask[-2:, :] = False
mask[:, :2] = False
mask[:, -2:] = False
x_scale = 848 / (mask.shape[1] - 1)
y_scale = 848 / (mask.shape[0] - 1)
distance, nearest = distance_transform_edt(~mask, sampling=(y_scale, x_scale), return_indices=True)
components_8, component_count_8 = label(mask, structure=np.ones((3, 3), dtype=np.uint8))

# The archived highfield is a rendered terrain-colormap panel, not the raw
# 16-bit HGHT raster. Inverting the 256-color terrain palette gives approximate
# Z values for qualitative neighborhood comparison only.
height_img = np.asarray(Image.open(HEIGHT_PNG).convert("RGB"))
height_panel = height_img[83:859, 218:994]
palette = np.asarray([np.asarray(colormaps["terrain"](i / 255)[:3]) * 255 for i in range(256)])
flat = height_panel.reshape(-1, 3).astype(np.int16)
indices = np.empty(len(flat), dtype=np.uint8)
for start in range(0, len(flat), 30000):
    block = flat[start:start + 30000]
    squared = ((block[:, None, :] - palette[None, :, :]) ** 2).sum(axis=2)
    indices[start:start + len(block)] = squared.argmin(axis=1)
z_grid = -1 + (indices.reshape(height_panel.shape[:2]).astype(float) / 255) * 31
px_per_scene = (height_panel.shape[1] - 1) / 848

stable_damar = {"village_A7_4", "village_A7_3", "village_A6_4", "village_A6_2", "village_A6_1"}
corridor_cities = {"town_A7", "town_A6"}
version_conflicts = {"castle_village_A4_2", "village_A7_2"}

rows = []
nearest_component_ids = {}
for e in entities:
    sid, x, y = e["entity_id"], e["x"], e["y"]
    px = int(round((x / 848) * (mask.shape[1] - 1)))
    py = int(round(((848 - y) / 848) * (mask.shape[0] - 1)))
    nearest_dist = float(distance[py, px])
    ny, nx = (int(nearest[0, py, px]), int(nearest[1, py, px]))
    nearest_x = nx / (mask.shape[1] - 1) * 848
    nearest_y = 848 - ny / (mask.shape[0] - 1) * 848
    nearest_component_ids[sid] = int(components_8[ny, nx])

    hp_x = int(round((x / 848) * (height_panel.shape[1] - 1)))
    hp_y = int(round(((848 - y) / 848) * (height_panel.shape[0] - 1)))
    center_z = float(z_grid[hp_y, hp_x])
    radius = int(round(10 * px_per_scene))
    y0, y1 = max(0, hp_y - radius), min(height_panel.shape[0], hp_y + radius + 1)
    x0, x1 = max(0, hp_x - radius), min(height_panel.shape[1], hp_x + radius + 1)
    yy, xx = np.ogrid[y0:y1, x0:x1]
    xx_scene = xx / px_per_scene
    yy_scene = 848 - yy / px_per_scene
    circle = (xx_scene - x) ** 2 + (yy_scene - y) ** 2 <= 100
    local = z_grid[y0:y1, x0:x1][circle]

    if sid in stable_damar:
        group = "stable_Damar_text_anchor"
    elif sid in corridor_cities:
        group = "Damar_corridor_city"
    elif sid in version_conflicts:
        group = "version_conflict_anchor_base_version_only"
    else:
        group = "comparison_other_Aserai_entity"

    rows.append({
        "entity_id": sid,
        "entity_type": e["entity_type"],
        "english_name": e["english_name"],
        "x_scene_units": round(x, 3),
        "y_scene_units": round(y, 3),
        "analysis_group": group,
        "nearest_PHYM7_mask_distance_scene_units": round(nearest_dist, 3),
        "nearest_PHYM7_pixel_x_scene_units": round(nearest_x, 3),
        "nearest_PHYM7_pixel_y_scene_units": round(nearest_y, 3),
        "approx_center_Z_from_rendered_heightfield": round(center_z, 3),
        "approx_local_median_Z_within_10_scene_units": round(float(np.median(local)), 3),
        "approx_local_q10_Z_within_10_scene_units": round(float(np.quantile(local, 0.1)), 3),
        "approx_local_q90_Z_within_10_scene_units": round(float(np.quantile(local, 0.9)), 3),
    })

rows.sort(key=lambda r: (r["analysis_group"], r["nearest_PHYM7_mask_distance_scene_units"]))
with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

# Print descriptive group summaries. These are screening statistics, not a
# significance test and not measurements from the raw PHYM/heightfield arrays.
for group in ("stable_Damar_text_anchor", "Damar_corridor_city", "version_conflict_anchor_base_version_only", "comparison_other_Aserai_entity"):
    values = sorted(r["nearest_PHYM7_mask_distance_scene_units"] for r in rows if r["analysis_group"] == group)
    if not values:
        continue
    med = float(np.median(values))
    q1, q3 = float(np.quantile(values, 0.25)), float(np.quantile(values, 0.75))
    within5 = sum(v <= 5 for v in values)
    print(f"{group}: n={len(values)}, median={med:.3f}, IQR={q1:.3f}-{q3:.3f}, <=5={within5}/{len(values)}")

anchor_ids = sorted(stable_damar)
anchor_components = {nearest_component_ids[sid] for sid in anchor_ids}
print(f"Aserai entities analysed: {len(rows)}")
print(f"PHYM7 mask components (8-neighbour): {component_count_8}")
print(f"Stable Damar anchors' nearest pixels share component(s): {sorted(anchor_components)}")
print(f"CSV written: {OUT_CSV}")
