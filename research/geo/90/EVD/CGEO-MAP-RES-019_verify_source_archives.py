#!/usr/bin/env python3
"""Verify Native/War Sails Main_map originals and compare scene/PHYM structure.

Requires: numpy, lz4
Example:
  python CGEO-MAP-RES-019_verify_source_archives.py --native-dir ./native --war-sails-dir ./war-sails
Input directories may use original filenames or prefixed names produced by the Drive download bridge.
Reads files only; never modifies source assets.
"""
from __future__ import annotations
import argparse, hashlib, json, struct, sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
import lz4.block
import numpy as np

EXPECTED = {
    "Native": {
        "atmosphere.xml": (4962, "7848867d9e0e72a5fbec4db20c9f022a7b3d77410da52eab7435f2a0d90d623d"),
        "flora.bin": (7849897, "78fe9777af8cc7161796a72e325803be83bbd5bf73c4e8c9b72cbb4375f4815d"),
        "navmesh.bin": (839040, "e01ad7ff2aa870a8933ece39df35be4370b7e4d29683b6df8e680a81880eb7f7"),
        "scene.xscene": (19877756, "919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019"),
        "terrain.bin": (27646798, "3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49"),
    },
    "War Sails": {
        "atmosphere.xml": (4941, "8375ecccc7a721b5d32e8e4fbc59e00b3a2182202d334a79cd01972668533f6d"),
        "flora.bin": (7253409, "7996acbbcbfc09ed9cc8e3fc88fe74de2008cbc736c42e584a2efc3742a2d884"),
        "flowmap.dds": (1048704, "22d11e2e488535c95f1ab80abefe9da1fd85b186a80d5f4346b13212ec31deea"),
        "navmesh.bin": (926074, "f8b4b846eb930fbfb64da64bf9c9c191a5aee2f825bfce7d1a59deaa21b0175f"),
        "river_triangles.bin": (1057044, "24fefdbe74302bb2f678db7b4533f00524c9f153613114d88db9187a3252ab24"),
        "scene.xscene": (21127988, "1fb8bb08210a377fb727dc9e69454f0368254f28f317cb81c5db2569e3862ebc"),
        "terrain.bin": (28336976, "56c3a0663fb2bf8404210772e187dcd707eb64d8b7e9b5496dfb509bdc3ea9fd"),
    },
}

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def locate(directory, version, filename):
    prefix = "Native_Main_map_" if version == "Native" else "WarSails_Main_map_"
    candidates = [directory / filename, directory / (prefix + filename)]
    if filename.endswith((".xml", ".xscene")):
        candidates.append(directory / (prefix + filename + ".xsl"))
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError(f"{version}: cannot locate {filename}; tried: " + ", ".join(map(str, candidates)))

def first_tag(root, tag):
    tag = tag.lower()
    return next((e for e in root.iter() if e.tag.lower() == tag), None)

def parse_scene(path):
    root = ET.parse(path).getroot()
    paths_el, layers_el, terrain_el = first_tag(root, "paths"), first_tag(root, "layers"), first_tag(root, "terrain")
    path_nodes = list(paths_el) if paths_el is not None else []
    paths = {}
    for el in path_nodes:
        points_el = el.find("points")
        points = []
        if points_el is not None:
            for point in points_el.findall("point"):
                xyz = [float(v.strip()) for v in point.attrib["position"].split(",")]
                points.append((xyz[0], xyz[1]))
        paths[el.attrib.get("name", "")] = points
    nile = paths.get("nile", [])
    nile_bbox = None
    if nile:
        nile_bbox = {"min_x": min(p[0] for p in nile), "max_x": max(p[0] for p in nile),
                     "min_y": min(p[1] for p in nile), "max_y": max(p[1] for p in nile)}
    river_script = next((e for e in root.iter() if e.tag.lower() == "script" and e.attrib.get("name") == "river_generator"), None)
    river_vars = {}
    if river_script is not None:
        for e in river_script.iter():
            if e.tag.lower() == "variable":
                river_vars[e.attrib.get("name", "")] = e.attrib.get("value", "")
    water_entities = [e for e in root.iter() if e.tag.lower() == "game_entity" and
                      any(e.attrib.get(k) == "water_plane" for k in ("name", "prefab", "old_prefab_name"))]
    water_materials = Counter(m.attrib["material"] for e in water_entities for m in e.iter()
                              if m.tag.lower() == "mesh" and m.attrib.get("material"))
    layers = [e.attrib.get("name") for e in layers_el if e.tag.lower() == "layer"] if layers_el is not None else []
    terrain_attrs = {k: terrain_el.attrib.get(k) for k in
                     ("node_dimension_x", "node_dimension_y", "node_size", "min_height", "max_height")} if terrain_el is not None else {}
    return {
        "root": root.attrib,
        "game_entity_count": sum(1 for e in root.iter() if e.tag.lower() == "game_entity"),
        "terrain": terrain_attrs,
        "terrain_layers_by_index": layers,
        "paths_container_count": len(path_nodes),
        "path_control_point_count": sum(len(points) for points in paths.values()),
        "path_names": list(paths),
        "nile_bbox": nile_bbox,
        "river_generator_variables": river_vars,
        "water_plane_entity_count": len(water_entities),
        "water_plane_materials": dict(water_materials),
        "ocean_material": [e.attrib.get("value") for e in root.iter()
                           if e.tag.lower() == "property" and e.attrib.get("name") == "water_material"],
    }

def decode_phym_summer(path):
    data = path.read_bytes()
    if data[:8] != b"ZGR6RTRN" or struct.unpack_from("<I", data, 8)[0] != 2:
        raise ValueError(f"Unexpected terrain header: {path}")
    directory = 12 + 4 * 20
    if data[directory:directory + 4] != b"PHYM":
        raise ValueError(f"PHYM section missing: {path}")
    section_version, offset, compressed_size, uncompressed_size = struct.unpack_from("<4I", data, directory + 4)
    tile_offsets = struct.unpack_from("<256I", data, offset)
    blob_offset = offset + 1024
    codec, _pad, blob_uncompressed, blob_compressed, _reserved, _stamp = struct.unpack_from("<IIQQQQ", data, blob_offset)
    if codec != 3 or blob_uncompressed != uncompressed_size or blob_compressed != compressed_size:
        raise ValueError(f"Unexpected PHYM blob header: {path}")
    raw = lz4.block.decompress(data[blob_offset + 40:blob_offset + compressed_size], uncompressed_size=uncompressed_size)
    if len(raw) != 67_642_368:
        raise ValueError(f"Unexpected PHYM raw length {len(raw)}: {path}")
    grid = np.zeros((4097, 4097), dtype=np.uint8)
    tile_lengths, season_counts = [], Counter()
    for idx in range(256):
        start, end = tile_offsets[idx], tile_offsets[idx + 1] if idx < 255 else len(raw)
        node = raw[start:end]
        tile_lengths.append(len(node))
        cursor, summer = 0, None
        for _ in range(4):
            season, count = struct.unpack_from("<II", node, cursor)
            cursor += 8
            if count != 66_049:
                raise ValueError(f"Unexpected PHYM sample count {count} in tile {idx}: {path}")
            arr = np.frombuffer(node, offset=cursor, count=count, dtype=np.uint8)
            cursor += count
            season_counts[season] += 1
            if season == 0:
                summer = arr.reshape((257, 257)).T
        if cursor != len(node) or summer is None:
            raise ValueError(f"Malformed PHYM tile {idx}: {path}")
        tx, ty = idx % 16, idx // 16
        grid[ty * 256:ty * 256 + 257, tx * 256:tx * 256 + 257] = summer
    values, counts = np.unique(grid, return_counts=True)
    return {
        "section_version": section_version,
        "section_offset_table_offset": offset,
        "compressed_payload_offset": blob_offset + 40,
        "compressed_payload_size_bytes": compressed_size,
        "uncompressed_size_bytes": uncompressed_size,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "tile_count": 256,
        "tile_record_bytes": sorted(set(tile_lengths)),
        "season_records": dict(sorted(season_counts.items())),
        "summer_grid_shape": list(grid.shape),
        "summer_value_counts": {str(int(v)): int(c) for v, c in zip(values, counts)},
        "has_value_7": bool(np.any(grid == 7)),
        "value_7_cell_count": int(np.count_nonzero(grid == 7)),
    }

def verify_version(version, directory):
    files, located = {}, {}
    for filename, (expected_size, expected_sha) in EXPECTED[version].items():
        path = locate(directory, version, filename)
        actual_size, actual_sha = path.stat().st_size, sha256(path)
        ok = actual_size == expected_size and actual_sha == expected_sha
        files[filename] = {"local_path": str(path), "size_bytes": actual_size, "sha256": actual_sha,
                           "expected_size_bytes": expected_size, "expected_sha256": expected_sha, "match": ok}
        located[filename] = path
    if not all(v["match"] for v in files.values()):
        raise ValueError(f"File-level verification failed for {version}: " +
                         ", ".join(k for k, v in files.items() if not v["match"]))
    return {"files": files, "scene_structure": parse_scene(located["scene.xscene"]),
            "phym_summer": decode_phym_summer(located["terrain.bin"])}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--native-dir", required=True, type=Path)
    ap.add_argument("--war-sails-dir", required=True, type=Path)
    args = ap.parse_args()
    result = {"Native": verify_version("Native", args.native_dir),
              "War Sails": verify_version("War Sails", args.war_sails_dir)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
