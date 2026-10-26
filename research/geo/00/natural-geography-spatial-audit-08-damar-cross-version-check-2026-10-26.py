#!/usr/bin/env python3
"""Reproduce descriptive cross-version anchor-spacing and elevation checks.

Inputs are the previously archived audit-06 and audit-07 CSV files in this folder.
This script does not parse raw map binaries and does not reconstruct a river centerline.
"""
from pathlib import Path
import csv
import math
import statistics

BASE = Path(__file__).resolve().parent
NATIVE_CSV = BASE / "natural-geography-spatial-audit-06-damar-native-anchor-results-2026-10-26.csv"
WARSAILS_CSV = BASE / "natural-geography-spatial-audit-07-damar-warsails-anchor-results-2026-10-26.csv"
SEGMENT_OUT = BASE / "natural-geography-spatial-audit-08-damar-cross-version-segment-results-2026-10-26.csv"
ELEVATION_OUT = BASE / "natural-geography-spatial-audit-08-damar-elevation-results-2026-10-26.csv"
SUMMARY_OUT = BASE / "natural-geography-spatial-audit-08-damar-settlement-elevation-group-summary-2026-10-26.csv"
ORDER = ["Zalm", "Mabwaz", "Nahlan", "Hamoshawat", "Mijayit"]
CONTROLS = ["Qidnar", "Bait Hatif", "Abba", "Asmait"]
NOMINAL_MAP_EXTENT_RATIO = 1040.0 / 848.0

def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def xy_distance(a, b):
    return math.hypot(float(b["x_scene"]) - float(a["x_scene"]),
                      float(b["y_scene"]) - float(a["y_scene"]))

native_rows = {r["anchor"]: r for r in read_csv(NATIVE_CSV)}
ws_rows = {r["name"]: r for r in read_csv(WARSAILS_CSV)}
missing = [n for n in ORDER + CONTROLS if n not in ws_rows]
missing += [n for n in ORDER if n not in native_rows]
if missing:
    raise ValueError(f"Missing required site(s): {missing}")

segment_fields = [
    "segment_order", "from_anchor", "to_anchor",
    "native_distance_scene_units", "warsails_distance_scene_units",
    "warsails_native_distance_ratio", "nominal_map_extent_ratio_1040_848",
    "ratio_after_nominal_extent_normalization", "interpretation_note"
]
segment_rows = []
for i, (a_name, b_name) in enumerate(zip(ORDER, ORDER[1:]), start=1):
    nd = xy_distance(native_rows[a_name], native_rows[b_name])
    wd = xy_distance(ws_rows[a_name], ws_rows[b_name])
    ratio = wd / nd
    segment_rows.append({
        "segment_order": i,
        "from_anchor": a_name,
        "to_anchor": b_name,
        "native_distance_scene_units": f"{nd:.3f}",
        "warsails_distance_scene_units": f"{wd:.3f}",
        "warsails_native_distance_ratio": f"{ratio:.3f}",
        "nominal_map_extent_ratio_1040_848": f"{NOMINAL_MAP_EXTENT_RATIO:.3f}",
        "ratio_after_nominal_extent_normalization": f"{ratio / NOMINAL_MAP_EXTENT_RATIO:.3f}",
        "interpretation_note": ("该段在《战帆》中显著拉长；不解释为世界内迁移"
                                if a_name == "Mabwaz" else "版本内描述性比较；非地理位移量")
    })
with SEGMENT_OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=segment_fields)
    writer.writeheader()
    writer.writerows(segment_rows)

anchor_rows = [ws_rows[name] for name in ORDER]
anchor_ground = [float(r["ground_z_at_settlement"]) for r in anchor_rows]
anchor_nav = [float(r["River11_navmesh_z"]) for r in anchor_rows]
anchor_ground_mean = statistics.mean(anchor_ground)
anchor_ground_median = statistics.median(anchor_ground)
anchor_ground_max = max(anchor_ground)
elevation_fields = [
    "sequence_order", "site", "group", "settlement_ground_z", "nearest_River11_face_id",
    "distance_to_River11_scene_units", "nearest_River11_navmesh_z",
    "terrain_z_at_nearest_River11", "navmesh_minus_terrain_z", "component_faces",
    "settlement_z_descends_from_previous_anchor", "navmesh_z_descends_from_previous_anchor",
    "interpretation_note"
]
elevation_rows = []
for i, name in enumerate(ORDER):
    r = ws_rows[name]
    prev = ws_rows[ORDER[i - 1]] if i else None
    ground_z = float(r["ground_z_at_settlement"])
    nav_z = float(r["River11_navmesh_z"])
    elevation_rows.append({
        "sequence_order": i + 1, "site": name, "group": r["group"],
        "settlement_ground_z": f"{ground_z:.3f}",
        "nearest_River11_face_id": r["nearest_River11_face_id"],
        "distance_to_River11_scene_units": f'{float(r["distance_to_River11"]):.3f}',
        "nearest_River11_navmesh_z": f"{nav_z:.3f}",
        "terrain_z_at_nearest_River11": f'{float(r["terrain_z_at_nearest_River11"]):.3f}',
        "navmesh_minus_terrain_z": f'{float(r["River11_minus_terrain_z"]):.3f}',
        "component_faces": r["River11_component_faces"],
        "settlement_z_descends_from_previous_anchor": ("n/a" if prev is None else
            str(ground_z <= float(prev["ground_z_at_settlement"])).lower()),
        "navmesh_z_descends_from_previous_anchor": ("n/a" if prev is None else
            str(nav_z <= float(prev["River11_navmesh_z"])).lower()),
        "interpretation_note": "河流锚点的局部采样；不代表连续河床纵剖面"
    })
for name in CONTROLS:
    r = ws_rows[name]
    elevation_rows.append({
        "sequence_order": "", "site": name, "group": r["group"],
        "settlement_ground_z": f'{float(r["ground_z_at_settlement"]):.3f}',
        "nearest_River11_face_id": r["nearest_River11_face_id"],
        "distance_to_River11_scene_units": f'{float(r["distance_to_River11"]):.3f}',
        "nearest_River11_navmesh_z": f'{float(r["River11_navmesh_z"]):.3f}',
        "terrain_z_at_nearest_River11": f'{float(r["terrain_z_at_nearest_River11"]):.3f}',
        "navmesh_minus_terrain_z": f'{float(r["River11_minus_terrain_z"]):.3f}',
        "component_faces": r["River11_component_faces"],
        "settlement_z_descends_from_previous_anchor": "n/a",
        "navmesh_z_descends_from_previous_anchor": "n/a",
        "interpretation_note": "非随机对照点；到River(11)的最近距离不表示其局地水源"
    })
with ELEVATION_OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=elevation_fields)
    writer.writeheader()
    writer.writerows(elevation_rows)

control_rows = [ws_rows[name] for name in CONTROLS]
control_ground = [float(r["ground_z_at_settlement"]) for r in control_rows]
summary_fields = [
    "group", "n", "min_ground_z", "median_ground_z", "mean_ground_z", "max_ground_z",
    "sites_above_damar_anchor_max", "mean_difference_vs_damar_anchor_mean",
    "median_difference_vs_damar_anchor_median", "interpretation"
]
summary_rows = [
    {
        "group": "Damar_anchor", "n": len(anchor_ground),
        "min_ground_z": f"{min(anchor_ground):.3f}",
        "median_ground_z": f"{anchor_ground_median:.4f}",
        "mean_ground_z": f"{anchor_ground_mean:.3f}",
        "max_ground_z": f"{anchor_ground_max:.3f}",
        "sites_above_damar_anchor_max": "n/a",
        "mean_difference_vs_damar_anchor_mean": "0.000",
        "median_difference_vs_damar_anchor_median": "0.000",
        "interpretation": "五个稳定达玛尔河锚点；仅作点位描述统计"
    },
    {
        "group": "comparison_control", "n": len(control_ground),
        "min_ground_z": f"{min(control_ground):.3f}",
        "median_ground_z": f"{statistics.median(control_ground):.4f}",
        "mean_ground_z": f"{statistics.mean(control_ground):.3f}",
        "max_ground_z": f"{max(control_ground):.3f}",
        "sites_above_damar_anchor_max": sum(z > anchor_ground_max for z in control_ground),
        "mean_difference_vs_damar_anchor_mean": f"{statistics.mean(control_ground) - anchor_ground_mean:.3f}",
        "median_difference_vs_damar_anchor_median": f"{statistics.median(control_ground) - anchor_ground_median:.3f}",
        "interpretation": "四个非随机局地水源／地貌对照点；不作统计显著性推断"
    }
]
with SUMMARY_OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=summary_fields)
    writer.writeheader()
    writer.writerows(summary_rows)

print(f"Wrote {SEGMENT_OUT.name} ({len(segment_rows)} rows)")
print(f"Wrote {ELEVATION_OUT.name} ({len(elevation_rows)} rows)")
print(f"Wrote {SUMMARY_OUT.name} ({len(summary_rows)} rows)")
