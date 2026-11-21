"""
A local model pack and catalogue in 3DHeat's formats, shared by the `models` and `catalog` commands.

Model pack: a folder with `model-pack.json` (`{format: "3dheat-model-pack", version: 1, game, gameBuild, source,
units: {<unit id>: {file, name, names, displayName, kind, type, domain, key, aliases, parts, box, pivots, length,
width, height, tris}}}`; `name` is the real vehicle's name, the same in every game's pack) and one
`.glb` per unit. A unit's file has a root node `unit` (extras: the index entry) with children `lod0`, `lod1`,
`lod2` (full, coarse, far), each holding one mesh node per part: `hull`, `gear` (wheels and tracks), `turret`
(extras {joint: "yaw", pivot}), `gun` (extras {joint: "pitch", pivot, parent}) and `rotor` (extras {joint: "spin",
pivot}); and an optional child `dm` with one node per hit region, `dm:<name>`, extras {part, group}. Positions are
float32 metres in the viewer's figure frame (x forward, y up, z right) about the unit's own origin.

Catalogue: `catalog.json` (`{format: "3dheat-catalog", version: 1, game, gameBuild, source, items: [{id, kind,
name, class, nation, key, model, numbers}]}`). `key` is the real-world name of the vehicle or weapon (like
"T-72B3"), which lets one game's unit be drawn with another game's model of the same real vehicle.

Everything written here stays on this machine: the files are made from the user's own installation.
"""

from __future__ import annotations

import hashlib
import json
import re
import struct
from pathlib import Path

import numpy as np

PACK_FORMAT = "3dheat-model-pack"
CATALOG_FORMAT = "3dheat-catalog"
PARTS = ("hull", "gear", "turret", "gun", "rotor")
#: Triangles per level of detail (full, coarse, far), by domain.
BUDGET = {"person": (8000, 2000, 500), "ground": (14000, 2600, 700), "air": (16000, 3000, 800),
          "heli": (16000, 3000, 800), "sea": (30000, 6000, 1500), "item": (3000, 800, 200)}


def norm_key(s: str) -> str:
    """A real-vehicle key as compared across games: lower case, letters and digits only ("T-72B3" -> "t72b3")."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def weld(v: np.ndarray, f: np.ndarray, step: float = 1e-4) -> tuple[np.ndarray, np.ndarray]:
    """Joins vertices closer than `step`, drops degenerate triangles and unused vertices."""
    v = np.asarray(v, np.float64)
    f = np.asarray(f, np.int64).reshape(-1, 3)
    if not len(f):
        return np.zeros((0, 3), np.float32), np.zeros((0, 3), np.int64)
    q = np.round(v / step).astype(np.int64)
    _, first, inv = np.unique(q, axis=0, return_index=True, return_inverse=True)
    f2 = inv.reshape(-1)[f]
    ok = (f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 0] != f2[:, 2])
    f2 = f2[ok]
    used, inv2 = np.unique(f2, return_inverse=True)
    return v[first][used].astype(np.float32), inv2.reshape(-1, 3)


def merge(items: list[tuple[np.ndarray, np.ndarray]]) -> tuple[np.ndarray, np.ndarray]:
    vs, fs, at = [], [], 0
    for v, f in items:
        if not len(f):
            continue
        vs.append(np.asarray(v, np.float64))
        fs.append(np.asarray(f, np.int64).reshape(-1, 3) + at)
        at += len(v)
    if not vs:
        return np.zeros((0, 3)), np.zeros((0, 3), np.int64)
    return np.concatenate(vs), np.concatenate(fs)


def tris(parts: dict) -> int:
    return sum(len(f) for _, f in parts.values())


def simplify(parts: dict, budget: int) -> dict:
    """Quadric simplification of the parts to `budget` triangles in all; the gun and rotor keep more of theirs."""
    total = tris(parts)
    if total <= budget:
        return parts
    import fast_simplification

    weight = {"gun": 3.0, "turret": 1.5, "rotor": 2.0}
    ratio = budget / total
    keep = {n: min(len(f), int(len(f) * min(1.0, ratio * weight[n]))) for n, (_, f) in parts.items() if n in weight}
    rest = sum(len(f) for n, (_, f) in parts.items() if n not in weight)
    rest_ratio = max(0.002, (budget - sum(keep.values())) / rest) if rest else 1.0
    out = {}
    for name, (v, f) in parts.items():
        want = max(12, keep.get(name, int(len(f) * rest_ratio)))
        if len(f) <= want:
            out[name] = (v, f)
            continue
        lo, hi = v.min(0), v.max(0)
        pad = 0.01 * float((hi - lo).max()) + 1e-3
        try:
            v2, f2 = fast_simplification.simplify(np.asarray(v, np.float64), np.asarray(f, np.int64),
                                                  target_reduction=1 - want / len(f), agg=5)
        except Exception:  # noqa: BLE001
            out[name] = (v, f)
            continue
        if not len(f2):
            out[name] = (v, f)
            continue
        bad = ~((v2 >= lo - pad) & (v2 <= hi + pad)).all(1)
        if bad.any():
            f2 = f2[~bad[f2].any(1)]
        v2, f2 = weld(v2, f2, 1e-5)
        if len(f2) > want * 1.25:
            v2, f2 = cull_small(v2, f2, want)
        out[name] = (v2, f2)
    return out


def cull_small(v: np.ndarray, f: np.ndarray, want: int) -> tuple[np.ndarray, np.ndarray]:
    """Vertex clustering where quadric simplification stalls (models of many open surfaces, whose borders it
    keeps): vertices are joined on a grid whose cell grows until `want` triangles are left."""
    if len(f) <= want:
        return v, f
    whole = float(np.linalg.norm(v.max(0) - v.min(0))) or 1.0
    lo_s, hi_s = whole / 4000, whole / 8
    best = None
    for _ in range(14):
        step = (lo_s * hi_s) ** 0.5
        v2, f2 = weld(v, f, step)
        if len(f2):
            f2 = np.unique(np.sort(f2, 1), axis=0) if len(f2) > want else f2
        if len(f2) > want:
            lo_s = step
        else:
            hi_s = step
            best = (v2, f2)
    if best is None:
        best = weld(v, f, hi_s)
    v2, f2 = best
    return weld(v2, f2, 1e-6)


def lods_of(parts: dict, domain: str) -> list[dict]:
    """Three levels of detail, each simplified from the full-detail part set to its budget, 16-bit indexable."""
    out = []
    for budget in BUDGET.get(domain, BUDGET["ground"]):
        lod = simplify(parts, budget)
        while any(len(v) >= 65535 for v, _ in lod.values()):
            lod = simplify(lod, int(tris(lod) * 0.7))
        out.append(lod)
    return out


class _Bin:
    def __init__(self):
        self.chunks: list[bytes] = []
        self.size = 0
        self.views: list[dict] = []
        self.accessors: list[dict] = []

    def add(self, data: bytes, target: int) -> int:
        pad = (-self.size) % 4
        if pad:
            self.chunks.append(b"\0" * pad)
            self.size += pad
        self.views.append({"buffer": 0, "byteOffset": self.size, "byteLength": len(data), "target": target})
        self.chunks.append(data)
        self.size += len(data)
        return len(self.views) - 1

    def mesh(self, v: np.ndarray, f: np.ndarray) -> dict:
        v = np.ascontiguousarray(v, np.float32)
        pv = self.add(v.tobytes(), 34962)
        self.accessors.append({"bufferView": pv, "componentType": 5126, "count": len(v), "type": "VEC3",
                               "min": v.min(0).tolist(), "max": v.max(0).tolist()})
        pa = len(self.accessors) - 1
        idx = np.ascontiguousarray(np.asarray(f).reshape(-1), np.uint16 if len(v) < 65536 else np.uint32)
        iv = self.add(idx.tobytes(), 34963)
        self.accessors.append({"bufferView": iv, "componentType": 5123 if idx.dtype == np.uint16 else 5125,
                               "count": len(idx), "type": "SCALAR"})
        return {"primitives": [{"attributes": {"POSITION": pa}, "indices": len(self.accessors) - 1, "mode": 4}]}


def write_unit_glb(path: Path, lods: list[dict], pivots: dict, meta: dict, asset_extras: dict,
                   dm: list | None = None) -> int:
    """Writes one unit; `dm` is a list of (name, verts, faces, extras). Returns the file's size."""
    b = _Bin()
    meshes: list[dict] = []
    nodes: list[dict] = [{"name": "unit", "children": [], "extras": meta}]

    def node(name: str, parent: int, v=None, f=None, extras=None) -> int:
        n: dict = {"name": name}
        if v is not None and len(f):
            meshes.append(b.mesh(v, f))
            n["mesh"] = len(meshes) - 1
        if extras:
            n["extras"] = extras
        nodes.append(n)
        nodes[parent].setdefault("children", []).append(len(nodes) - 1)
        return len(nodes) - 1

    for k, lod in enumerate(lods):
        li = node(f"lod{k}", 0, extras={"triangles": tris(lod)})
        for part in PARTS:
            if part not in lod or not len(lod[part][1]):
                continue
            v, f = lod[part]
            ex = None
            if part == "turret" and "turret" in pivots:
                ex = {"joint": "yaw", "pivot": pivots["turret"]}
            elif part == "gun" and "gun" in pivots:
                ex = {"joint": "pitch", "pivot": pivots["gun"], "parent": "turret" if "turret" in pivots else None}
            elif part == "rotor" and "rotor" in pivots:
                ex = {"joint": "spin", "pivot": pivots["rotor"]}
            node(part, li, v, f, ex)
    if dm:
        di = node("dm", 0)
        for name, v, f, ex in dm:
            node(f"dm:{name}", di, v, f, ex)
    gltf = {
        "asset": {"version": "2.0", "generator": asset_extras.get("source", ""), "extras": asset_extras},
        "scene": 0, "scenes": [{"nodes": [0]}], "nodes": nodes, "meshes": meshes,
        "buffers": [{"byteLength": b.size}], "bufferViews": b.views, "accessors": b.accessors,
    }
    js = json.dumps(gltf, separators=(",", ":")).encode()
    js += b" " * ((-len(js)) % 4)
    binb = b"".join(b.chunks)
    binb += b"\0" * ((-len(binb)) % 4)
    total = 12 + 8 + len(js) + 8 + len(binb)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".glb.part")
    with tmp.open("wb") as fh:
        fh.write(struct.pack("<III", 0x46546C67, 2, total))
        fh.write(struct.pack("<II", len(js), 0x4E4F534A) + js)
        fh.write(struct.pack("<II", len(binb), 0x004E4942) + binb)
    tmp.replace(path)
    return total


def write_json(p: Path, data: dict) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.part")
    tmp.write_text(json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    tmp.replace(p)


class Pack:
    """A model pack folder: its index, kept up to date as units are written."""

    def __init__(self, folder: Path, game: str, game_build: str, source: str):
        self.folder = Path(folder)
        self.index_path = self.folder / "model-pack.json"
        self.index = {"format": PACK_FORMAT, "version": 1, "game": game, "gameBuild": game_build, "source": source,
                      "units": {}}
        if self.index_path.is_file():
            try:
                old = json.loads(self.index_path.read_text(encoding="utf-8"))
                if old.get("format") == PACK_FORMAT and old.get("game") == game:
                    self.index["units"] = old.get("units", {})
            except (OSError, ValueError):
                pass
        self.index.update({"gameBuild": game_build, "source": source})
        self.bytes = 0

    def fresh(self, unit: str, fingerprint: str) -> bool:
        e = self.index["units"].get(unit)
        return bool(e and e.get("fingerprint") == fingerprint and e.get("source") == self.index["source"]
                    and (self.folder / e["file"]).is_file())

    def add(self, unit: str, parts: dict, domain: str, kind: str, key: str = "", pivots: dict | None = None,
            aliases: list | None = None, dm: list | None = None, fingerprint: str = "", extra: dict | None = None,
            anchor: str | None = None) -> dict:
        """Simplifies `parts` ({part: (verts, faces)}, figure frame) to three levels and writes the unit."""
        pivots = pivots or {}
        parts = {p: weld(*parts[p]) for p in parts if len(parts[p][1])}
        parts = {p: x for p, x in parts.items() if len(x[1])}
        if not parts:
            raise ValueError("no geometry")
        lods = lods_of(parts, domain)
        allv = np.concatenate([v for v, _ in lods[0].values()])
        lo, hi = allv.min(0), allv.max(0)
        fname = re.sub(r"[^a-z0-9_.-]", "_", unit.lower()) + ".glb"
        meta = {
            "kind": kind, "domain": domain, "key": key,
            "anchor": anchor or ("centre" if domain in ("air",) else "ground"),
            "box": [round(float(x), 4) for x in (*lo, *hi)], "pivots": pivots,
            "length": round(float(hi[0] - lo[0]), 3), "width": round(float(hi[2] - lo[2]), 3),
            "height": round(float(hi[1] - lo[1]), 3),
            "parts": sorted(lods[0]), "tris": [tris(x) for x in lods], "dm": len(dm or []),
        }
        if extra:
            meta.update(extra)
        size = write_unit_glb(self.folder / fname, lods, pivots, {"unit": unit, **meta},
                              {"source": self.index["source"], "version": 1, "game": self.index["game"],
                               "gameBuild": self.index["gameBuild"], "unit": unit, "scale": 1}, dm)
        self.bytes += size
        entry = {**meta, "file": fname, "aliases": sorted(set(aliases or [])), "fingerprint": fingerprint,
                 "gameBuild": self.index["gameBuild"], "source": self.index["source"],
                 "sha256": hashlib.sha256((self.folder / fname).read_bytes()).hexdigest()}
        # `name` is the real vehicle's name (what other games' units are matched on), `names` further names,
        # `type` the class word the viewer picks a stand-in figure by.
        display = entry.get("name") or ""
        entry["displayName"] = display
        entry["name"] = key or display
        entry["names"] = [display] if display and display != entry["name"] else []
        entry["type"] = kind + (" helicopter" if kind.startswith("heli") else "")
        self.index["units"][unit] = entry
        return entry

    def save(self) -> None:
        write_json(self.index_path, self.index)


def write_catalog(path: Path, game: str, game_build: str, source: str, items: list[dict]) -> None:
    write_json(path, {"format": CATALOG_FORMAT, "version": 1, "game": game, "gameBuild": game_build,
                      "source": source, "items": sorted(items, key=lambda i: (i.get("kind", ""), i["id"]))})


def levels_dir(given: str | None = None) -> Path | None:
    import os

    lv = given or os.environ.get("HEAT3D_LEVELS")
    return Path(lv) if lv else None
