#!/usr/bin/env python3
"""Recompute Damar-anchor distances to all linear paths in Native Main_map scene.xscene."""
from pathlib import Path
import argparse, hashlib, math, xml.etree.ElementTree as ET

EXPECTED_SHA256 = '919796b65e497260a8eebab5442ac79af6992957de9e8a17fbb2aaf6fd1b5019'
ANCHORS = {
    'Zalm': ('village_A7_4', 390.254, 97.643),
    'Mabwaz': ('village_A7_3', 413.587, 124.973),
    'Nahlan': ('village_A6_4', 404.877, 160.318),
    'Hamoshawat': ('village_A6_2', 394.921, 177.046),
    'Mijayit': ('village_A6_1', 410.054, 178.898),
}
SEA_PATHS = {'northsea', 'ocean', 'mediterranean', 'capsian', 'lake_bat'}

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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('scene_xscene', help='Path to the Native Main_map scene.xscene file')
    ap.add_argument('--skip-hash-check', action='store_true')
    args = ap.parse_args()
    path = Path(args.scene_xscene)
    actual = sha256(path)
    if not args.skip_hash_check and actual != EXPECTED_SHA256:
        raise SystemExit(f'SHA-256 mismatch: {actual} != {EXPECTED_SHA256}')
    root = ET.parse(path).getroot()
    paths_container = next((e for e in root.iter() if e.tag.lower() == 'paths'), None)
    if paths_container is None: raise SystemExit('No Paths container found')
    paths = []
    for element in list(paths_container):
        points_element = element.find('points')
        if points_element is None: continue
        points = []
        for point in points_element.findall('point'):
            xyz = [float(v.strip()) for v in point.attrib['position'].split(',')]
            points.append((xyz[0], xyz[1]))
        if len(points) >= 2:
            paths.append((element.attrib.get('name', ''), points))
    print(f'sha256={actual}')
    print(f'path_count={len(paths)}')
    print(f'control_point_count={sum(len(p) for _, p in paths)}')
    for anchor, (entity_id, x, y) in ANCHORS.items():
        p = (x, y)
        ranked = []
        for name, points in paths:
            if name in SEA_PATHS: continue
            best = min((point_segment(p, points[i], points[i+1])[0], i, point_segment(p, points[i], points[i+1])[1], point_segment(p, points[i], points[i+1])[2]) for i in range(len(points)-1))
            ranked.append((best[0], name, best[1], best[2], best[3]))
        ranked.sort()
        print(f'[{anchor} {entity_id} x={x:.3f} y={y:.3f}]')
        for distance, name, segment, t, q in ranked[:3]:
            print(f'  {name}: distance={distance:.6f}, segment={segment}, t={t:.6f}, projection=({q[0]:.6f},{q[1]:.6f})')

if __name__ == '__main__': main()