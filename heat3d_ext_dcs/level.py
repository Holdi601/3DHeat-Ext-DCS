"""
A theatre's ground as a 3DHeat level: `ground:<Level>`, `water:<Level>`.

- **Ground** is the terrain's own triangles, in DCS world metres. Each
  triangle is coloured by what the game draws over it - runway, road, rail,
  town, river or lake, beach, rock, field, forest, else bare land - so the
  viewer's *Captured colour* shows the period airfields, roads and towns.
  Every overlay triangle is one of the ground's own (checked on every class,
  on two theatres: all of them match), so a triangle takes the class of the
  overlay that draws it; where several do, the order above decides (a road
  through a forest is road).
- **Water** is every triangle the game marks as under the sea, laid flat at
  sea level (y = 0). The sea floor itself is left out unless `seabed` is
  asked for; then it is ground too, in its own colour.

`cell` (metres) thins the mesh by vertex clustering: every vertex in a cell of
that size (in x and z) becomes one, at their mean, and triangles that collapse
are dropped. 0 keeps the game's own triangles. The game's mesh is already
adaptive - flat sea in triangles kilometres across, coasts and roads in a few
metres - so a cell only removes detail finer than itself.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np

from .surface5 import Surface5, Tile

#: Highest first: a triangle takes the first class all its corners belong to.
PRIORITY = ("runway", "road", "rail", "town", "water", "beach", "rock", "field", "forest")
MATERIAL_CLASS = {
    "runway": "runway",
    "road": "road",
    "rail": "rail",
    "town": "town",
    "building": "town",
    "river": "water",
    "lake": "water",
    "beach": "beach",
    "rock": "rock",
    "field": "field",
    "grass": "field",
    "forest": "forest",
    "trees": "forest",
}
CLASSES = ("land",) + PRIORITY + ("seabed",)
COLOURS = {
    "land": (0.63, 0.59, 0.49),
    "forest": (0.29, 0.41, 0.23),
    "field": (0.60, 0.65, 0.38),
    "rock": (0.55, 0.53, 0.50),
    "beach": (0.86, 0.80, 0.62),
    "water": (0.24, 0.45, 0.72),
    "town": (0.74, 0.40, 0.31),
    "rail": (0.38, 0.30, 0.26),
    "road": (0.28, 0.28, 0.28),
    "runway": (0.10, 0.10, 0.10),
    "seabed": (0.33, 0.43, 0.53),
}
SEA = 1  # TRITYPE bit: under the sea


@dataclass
class Region:
    """A box in DCS metres: x (north) and z (east)."""

    x0: float
    z0: float
    x1: float
    z1: float

    def __post_init__(self) -> None:
        self.x0, self.x1 = sorted((self.x0, self.x1))
        self.z0, self.z1 = sorted((self.z0, self.z1))

    def touches(self, b: tuple[float, ...]) -> bool:
        return not (b[3] < self.x0 or b[0] > self.x1 or b[5] < self.z0 or b[2] > self.z1)

    def holds(self, x: np.ndarray, z: np.ndarray) -> np.ndarray:
        return (x >= self.x0) & (x <= self.x1) & (z >= self.z0) & (z <= self.z1)


@dataclass
class Primitive:
    positions: np.ndarray  # float32 n x 3
    triangles: np.ndarray  # uint32 m x 3
    colour: tuple[float, float, float] | None = None
    label: str = ""


@dataclass
class Level:
    name: str
    ground: list[Primitive] = field(default_factory=list)
    water: list[Primitive] = field(default_factory=list)
    classes: dict[str, int] = field(default_factory=dict)
    tiles: int = 0

    def parts(self) -> list[tuple[str, list[Primitive]]]:
        out = []
        if self.ground:
            out.append((f"ground:{self.name}", self.ground))
        if self.water:
            out.append((f"water:{self.name}", self.water))
        return out

    def bounds(self) -> tuple[np.ndarray, np.ndarray] | None:
        prims = self.ground + self.water
        if not prims:
            return None
        lo = np.min([p.positions.min(0) for p in prims], axis=0)
        hi = np.max([p.positions.max(0) for p in prims], axis=0)
        return lo, hi

    @property
    def triangle_count(self) -> int:
        return sum(len(p.triangles) for p in self.ground + self.water)


def _keys(tri: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    t = np.sort(tri.astype(np.int64), axis=1)
    return t[:, 0] * n + t[:, 1], t[:, 2]


def matching(base: np.ndarray, other: np.ndarray, n: int) -> np.ndarray:
    """Which triangles of `base` have the same three vertices as one of `other` (in any order)."""
    if not len(base) or not len(other):
        return np.zeros(len(base), bool)
    b1, b2 = _keys(base, n)
    o1, o2 = _keys(other, n)
    k1, k2 = np.concatenate([b1, o1]), np.concatenate([b2, o2])
    flag = np.concatenate([np.zeros(len(b1), np.int8), np.ones(len(o1), np.int8)])
    order = np.lexsort((flag, k2, k1))
    s1, s2, sf = k1[order], k2[order], flag[order]
    hit = (s1[:-1] == s1[1:]) & (s2[:-1] == s2[1:]) & (sf[:-1] == 0) & (sf[1:] == 1)
    out = np.zeros(len(base), bool)
    out[order[:-1][hit]] = True
    return out


def classify(surface: Surface5, tile: Tile, tri: np.ndarray) -> np.ndarray:
    """Each ground triangle's class, as an index into CLASSES (0: land)."""
    cls = np.zeros(len(tri), np.uint8)
    overlays: dict[str, list[np.ndarray]] = {}
    for g in tile.groups:
        c = MATERIAL_CLASS.get(g.material.lower())
        if c is None or g is tile.ground:
            continue
        t = surface.overlay(tile, g)
        if t is not None and len(t):
            overlays.setdefault(c, []).append(t)
    # Lowest priority first, so a higher class overwrites it.
    for c in reversed(PRIORITY):
        if c in overlays:
            cls[matching(tri, np.concatenate(overlays[c]), tile.vertex_count)] = CLASSES.index(c)
    return cls


def _compact(positions: np.ndarray, tri: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    used, inverse = np.unique(tri.ravel(), return_inverse=True)
    return positions[used], inverse.reshape(-1, 3)


def cluster(positions: np.ndarray, tri: np.ndarray, cell: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Vertex clustering on an x/z grid of `cell` metres. Returns positions, triangles and which input triangles survived."""
    kx = np.floor(positions[:, 0] / cell).astype(np.int64)
    kz = np.floor(positions[:, 2] / cell).astype(np.int64)
    kx -= kx.min()
    kz -= kz.min()
    key = kx * (int(kz.max()) + 1) + kz
    cells, inverse = np.unique(key, return_inverse=True)
    count = np.bincount(inverse, minlength=len(cells)).astype(np.float64)
    merged = np.stack([np.bincount(inverse, positions[:, i], len(cells)) / count for i in range(3)], axis=1)
    t = inverse[tri]
    alive = (t[:, 0] != t[:, 1]) & (t[:, 1] != t[:, 2]) & (t[:, 0] != t[:, 2])
    keep = np.flatnonzero(alive)
    s = np.sort(t[keep], axis=1)
    _, first = np.unique(s, axis=0, return_index=True)
    keep = keep[np.sort(first)]
    return merged, t[keep], keep


def build(
    surface: Surface5,
    name: str,
    *,
    region: Region | None = None,
    cell: float = 0.0,
    seabed: bool = False,
    water: bool = True,
    progress: Callable[[int, int], None] | None = None,
) -> Level:
    tiles = [t for t in surface.ground_tiles if region is None or region.touches(t.world_bounds())]
    level = Level(name, tiles=len(tiles))
    gp: list[np.ndarray] = []
    gt: list[np.ndarray] = []
    gc: list[np.ndarray] = []
    wp: list[np.ndarray] = []
    wt: list[np.ndarray] = []
    gn = wn = 0
    for i, tile in enumerate(tiles):
        if progress:
            progress(i, len(tiles))
        p = surface.positions(tile)
        tri, kinds = surface.ground(tile)
        sea = (kinds & SEA) != 0
        if region is not None:
            c = p[tri].mean(axis=1)
            inside = region.holds(c[:, 0], c[:, 2])
        else:
            inside = np.ones(len(tri), bool)
        cls = classify(surface, tile, tri)
        cls[sea] = CLASSES.index("seabed")
        ground = inside & (~sea | seabed)
        if ground.any():
            q, t = _compact(p, tri[ground])
            gp.append(q)
            gt.append(t + gn)
            gc.append(cls[ground])
            gn += len(q)
        if water and (inside & sea).any():
            q, t = _compact(p, tri[inside & sea])
            q = q.copy()
            q[:, 1] = 0.0
            wp.append(q)
            wt.append(t + wn)
            wn += len(q)
    if progress:
        progress(len(tiles), len(tiles))

    if gp:
        pos, tri, cls = np.concatenate(gp), np.concatenate(gt), np.concatenate(gc)
        if cell > 0:
            pos, tri, keep = cluster(pos, tri, cell)
            cls = cls[keep]
        for k, cname in enumerate(CLASSES):
            sel = cls == k
            if not sel.any():
                continue
            q, t = _compact(pos, tri[sel])
            level.ground.append(Primitive(q.astype(np.float32), t.astype(np.uint32), COLOURS[cname], cname))
            level.classes[cname] = int(sel.sum())
    if wp:
        pos, tri = np.concatenate(wp), np.concatenate(wt)
        if cell > 0:
            pos, tri, _ = cluster(pos, tri, cell)
            pos[:, 1] = 0.0
        q, t = _compact(pos, tri)
        level.water.append(Primitive(q.astype(np.float32), t.astype(np.uint32), None, "sea"))
        level.classes["sea"] = len(t)
    return level


def ground_height(level: Level, x: float, z: float, reach: float = 500.0) -> float | None:
    """Height of the ground vertex nearest (x, z) within `reach` metres, or None."""
    best, best_d = None, reach * reach
    for p in level.ground:
        near = (np.abs(p.positions[:, 0] - x) < reach) & (np.abs(p.positions[:, 2] - z) < reach)
        if not near.any():
            continue
        q = p.positions[near]
        d = (q[:, 0] - x) ** 2 + (q[:, 2] - z) ** 2
        i = int(d.argmin())
        if d[i] < best_d:
            best, best_d = float(q[i, 1]), float(d[i])
    return best


def around(projection, lat: float, lon: float, km: float) -> Region:
    x, z = projection.to_dcs(lat, lon)
    r = km * 1000.0
    return Region(x - r, z - r, x + r, z + r)


def estimate_vertices(surface: Surface5, region: Region | None) -> int:
    return sum(t.vertex_count for t in surface.ground_tiles if region is None or region.touches(t.world_bounds()))


def fmt_bounds(level: Level) -> dict | None:
    b = level.bounds()
    if b is None:
        return None
    lo, hi = b
    return {"x": [float(lo[0]), float(hi[0])], "y": [float(lo[1]), float(hi[1])], "z": [float(lo[2]), float(hi[2])]}

