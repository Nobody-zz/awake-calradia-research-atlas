#!/usr/bin/env python3
"""Recompute Damar anchor-to-path and PHYM river-layer distances from Native originals.

Dependencies: numpy, scipy, lz4.
Inputs: Native Main_map scene.xscene and terrain.bin, unmodified originals.
"""
from pathlib import Path
import argparse, hashlib, math, struct, xml.etree.ElementTree as ET
import lz4.block
import numpy as np
from scipy.ndimage import distance_transform_edt

SCENE_SHA = '919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019'
TERRAIN_SHA = '3b583d9ff5504a6c871caa466a14654593bee42c27df3e3316eda6cb4d85ab49'
ANCHORS = {
    'Zalm': ('village_A7_4', 390.254, 97.643),
    'Mabwaz': ('village_A7_3', 413.587, 124.973),
    'Nahlan': ('village_A6_4', 404.877, 160.318),
    'Hamoshawat': ('village_A6_2', 394.921, 177.046),
    'Mijayit': ('village_A6_1', 410.054, 178.898),
}
SEA_PATHS = {'northsea', 'ocean', 'mediterranean', 'capsian', 'lake_bat'}
RIVER_LAYER_INDEX = 7
SCENE_EXTENT = 848.0
GRID_SIDE = 4097
PHYM_NODE_BYTES = 264228
PHYM_TILE_SIDE = 257

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''): h.update(block)
    return h.hexdigest()

def point_segment(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]
    den = vx * vx + vy * vy
    t = 0.0 if den == 0 else max(0.0, min(1.0, ((p[0]-a[0])*vx + (p[1]-a[1])*vy) / den))
    q = (a[0] + t * vx, a[1] + t * vy)
    return math.dist(p, q), t, q

def parse_scene(scene_path):
    root = ET.parse(scene_path).getroot()
    paths_el = next((e for e in root.iter() if e.tag.lower() == 'paths'), None)
    if paths_el is None: raise ValueError('No Paths container in Native scene.xscene')
    paths = {}
    total_points = 0
    for el in list(paths_el):
        pel = el.find('points')
        if pel is None: continue
        pts = []
        for point in pel.findall('point'):
            xyz = [float(v.strip()) for v in point.attrib['position'].split(',') ]
            pts.append((xyz[0], xyz[1]))
        if len(pts) >= 2:
            paths[el.attrib.get('name','')] = pts
            total_points += len(pts)
    return root, paths, len(list(paths_el)), total_points

def decode_phym_summer(terrain_path):
    data = Path(terrain_path).read_bytes()
    if data[:12] != b'ZGR6RTRN\\x02\\x00\\x00\\x00': raise ValueError('Unexpected terrain.bin header')
    phym_dir = 12 + 20 * 4
    if data[phym_dir:phym_dir+4] != b'PHYM': raise ValueError('PHYM section directory entry missing')
    version, off, csize, usize = struct.unpack_from('<4I', data, phym_dir + 4)
    # The 256-entry raw-offset table precedes the 40-byte Blob header.
    table_bytes = 1024
    offsets = struct.unpack_from('<256I', data, off)
    blob_off = off + table_bytes
    codec, pad, blob_usize, blob_csize, reserved, stamp = struct.unpack_from('<IIQQQQ', data, blob_off)
    if codec != 3 or blob_csize != csize or blob_usize != usize: raise ValueError('Unexpected PHYM Blob header')
    raw = lz4.block.decompress(data[blob_off + 40:blob_off + csize], uncompressed_size=usize)
    if len(raw) != 256 * PHYM_NODE_BYTES: raise ValueError('Unexpected PHYM raw size')
    mosaic = np.zeros((GRID_SIDE, GRID_SIDE), dtype=np.uint8)
    for idx in range(256):
        start = offsets[idx]
        end = offsets[idx + 1] if idx < 255 else len(raw)
        node = raw[start:end]
        season, count = struct.unpack_from('<II', node, 0)
        if season != 0 or count != PHYM_TILE_SIDE * PHYM_TILE_SIDE:
            raise ValueError(f'Unexpected summer record in tile {idx}: season={season}, count={count}')
        arr = np.frombuffer(node, offset=8, count=PHYM_TILE_SIDE*PHYM_TILE_SIDE, dtype=np.uint8).reshape((PHYM_TILE_SIDE, PHYM_TILE_SIDE))
        # In this format the tile directory is Y-major; each tile's sample array is X-major.
        tx, ty = idx % 16, idx // 16
        tile = arr.T
        x0, y0 = tx * 256, ty * 256
        mosaic[y0:y0+257, x0:x0+257] = tile
    return mosaic

def nearest_path(p, pts):
    return min((point_segment(p, pts[i], pts[i+1])[0], i, point_segment(p, pts[i], pts[i+1])[1], point_segment(p, pts[i], pts[i+1])[2]) for i in range(len(pts)-1))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scene', required=True, help='Native Main_map scene.xscene')
    ap.add_argument('--terrain', required=True, help='Native Main_map terrain.bin')
    ap.add_argument('--skip-hash-check', action='store_true')
    args = ap.parse_args()
    scene_path, terrain_path = Path(args.scene), Path(args.terrain)
    scene_sha, terrain_sha = sha256(scene_path), sha256(terrain_path)
    if not args.skip_hash_check and scene_sha != SCENE_SHA: raise SystemExit(f'scene SHA-256 mismatch: {scene_sha}')
    if not args.skip_hash_check and terrain_sha != TERRAIN_SHA: raise SystemExit(f'terrain SHA-256 mismatch: {terrain_sha}')
    root, paths, path_count, point_count = parse_scene(scene_path)
    print(f'scene_sha256={scene_sha}')
    print(f'terrain_sha256={terrain_sha}')
    print(f'path_count={path_count}; control_point_count={point_count}')
    print(f'river_layer_label={[(i,e.attrib.get("name")) for i,e in enumerate(next(e for e in root.iter() if e.tag.lower()=="layers")) if e.tag.lower()=="layer"]}')
    print('anchor,path_distance,path_segment,second_nearest_path,second_nearest_distance')
    for name, (entity_id, x, y) in ANCHORS.items():
        p=(x,y); ranked=[]
        for path_name, pts in paths.items():
            if path_name in SEA_PATHS: continue
            d, seg, t, proj = nearest_path(p, pts)
            ranked.append((d,path_name,seg))
        ranked.sort()
        print(f'{name}({entity_id}),{ranked[0][1]},{ranked[0][0]:.6f},{ranked[0][2]},{ranked[1][1]},{ranked[1][0]:.6f}')
    mosaic=decode_phym_summer(terrain_path)
    mask=mosaic==RIVER_LAYER_INDEX
    step=SCENE_EXTENT/(GRID_SIDE-1)
    dist=distance_transform_edt(~mask)*step
    print(f'phym_summer_river_cells={int(mask.sum())}')
    print(f'phym_summer_river_fraction={float(mask.mean()):.8f}')
    print('anchor,phym_river_layer_distance,cell_value')
    for name,(_,x,y) in ANCHORS.items():
        px=max(0,min(GRID_SIDE-1,round(x/step))); py=max(0,min(GRID_SIDE-1,round(y/step)))
        print(f'{name},{dist[py,px]:.6f},{int(mosaic[py,px])}')
    nile=paths['nile']; samples=[]
    for i in range(len(nile)-1):
        a,b=nile[i],nile[i+1]; n=max(1,math.ceil(math.dist(a,b)/0.1))
        for j in range(n+1):
            t=j/n; x=a[0]+t*(b[0]-a[0]); y=a[1]+t*(b[1]-a[1])
            px=max(0,min(GRID_SIDE-1,round(x/step))); py=max(0,min(GRID_SIDE-1,round(y/step)))
            samples.append(float(dist[py,px]))
    print(f'nile_phym_distance_samples={len(samples)}')
    print(f'nile_phym_distance_median={float(np.median(samples)):.6f}')
    print(f'nile_phym_distance_p90={float(np.quantile(samples,.9)):.6f}')
    print(f'nile_phym_distance_max={max(samples):.6f}')
    for limit in (1.0,2.0,5.0): print(f'nile_within_{limit:g}_scene_units={sum(v<=limit for v in samples)/len(samples):.6%}')

if __name__ == '__main__': main()