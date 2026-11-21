"""
DCS World's unit models as a local 3DHeat model pack: every aircraft, helicopter, ground unit and ship of
`catalog` whose model (`.edm`) is in your install, posed at rest, split into the parts the viewer moves and
simplified to three levels of detail.

- The model of a unit is the `Shape` its Lua names (or the file named like the unit); a `<shape>.lods` file gives
  its levels of detail, the nearest is read. Within a model, a level-of-detail node keeps its nearest child.
- Every node's transform is taken with all animation arguments at 0 (the rest pose: wheels down for ground units,
  gear up and canopy closed for aircraft), and a visibility switch shows what it shows at 0 (no muzzle flash, no
  damaged pieces, no rotor blur disc).
- Parts, by the arguments that move them: ground units' turret (argument 0, yaw) and gun (argument 1, pitch), and
  their wheels and tracks (arguments 12-14, or so named); a helicopter's main rotor (argument 40), blades bound to
  its bones included. The rest is the hull.
- Collision shells (`ShellNode`) are kept as hit regions under `dm`, with the part they move with.
- A model file that is not an EDM model a version of this reader knows (a protected third-party file, say) is
  skipped and named in the summary. Packed databases (`*.edce`) are never opened.

Positions are metres in the viewer's figure frame, which is DCS's own model frame: x forward, y up, z right.
"""

from __future__ import annotations

import hashlib
import math
import os
import re
import time
from pathlib import Path

import numpy as np

from . import edm
from .modelpack import Pack, norm_key

#: Parts by the arguments that turn them, per domain.
TURRET_ARGS = {"ground": (0,), "sea": ()}
GUN_ARGS = {"ground": (1,), "sea": ()}
ROTOR_ARGS = {"heli": (40,)}
WHEEL_ARGS = {"ground": (12, 13, 14)}
#: Materials and node names that are effects, not the body.
SKIP_MATERIAL = re.compile(r"bano|additive|self_illum|lines|fake_|flame|smoke|halo|shadow|forest", re.I)
SKIP_NAME = re.compile(r"flame|fire|smoke|blur|outline|shadow|pilot|_dmg|damage|oblomok|lamp|light|halo|glow|"
                       r"muzzle|tracer|collision|bound", re.I)
GEAR_NAME = re.compile(r"wheel|koleso|track|gusen|katok|kolesa|tire|tyre", re.I)
NOT_GEAR = re.compile(r"above|over|cover|fender|guard|mudflap|box", re.I)


# ------------------------------------------------------------------------------------------------ transforms

def _quat_matrix(q) -> np.ndarray:
    x, y, z, w = q
    n = math.sqrt(x * x + y * y + z * z + w * w) or 1.0
    x, y, z, w = x / n, y / n, z / n, w / n
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w), 0],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w), 0],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y), 0],
        [0, 0, 0, 1]])


def _translate(p) -> np.ndarray:
    m = np.eye(4)
    m[:3, 3] = p
    return m


def _scale(s) -> np.ndarray:
    return np.diag([s[0], s[1], s[2], 1.0])


def _key(keys: list, a: float, quat: bool):
    """A key track's value at argument `a`: linear between the frames around it (quaternions normalised)."""
    if not keys:
        return None
    keys = sorted(keys, key=lambda k: k[0])
    if a <= keys[0][0]:
        return keys[0][1]
    for (f0, v0), (f1, v1) in zip(keys, keys[1:]):
        if f0 <= a <= f1:
            t = 0.0 if f1 == f0 else (a - f0) / (f1 - f0)
            v0, v1 = np.array(v0), np.array(v1)
            if quat and float(np.dot(v0, v1)) < 0:
                v1 = -v1
            v = v0 + (v1 - v0) * t
            return tuple(v / (np.linalg.norm(v) or 1.0)) if quat else tuple(v)
    return keys[-1][1]


def local_matrix(n: edm.Node, args: dict) -> np.ndarray:
    if n.base is not None:
        b = n.base
        pos = np.array(b["position"], np.float64)
        for arg, keys in n.pos:  # position keys move the node from its base position
            v = _key(keys, args.get(arg, 0.0), False)
            if v is not None:
                pos = pos + np.array(v[:3])
        rot = np.eye(4)
        for arg, keys in n.rot:
            v = _key(keys, args.get(arg, 0.0), True)
            if v is not None:
                rot = rot @ _quat_matrix(v)
        sc = b["scale"]
        for arg, keys in n.scale:
            v = _key(keys, args.get(arg, 0.0), False)
            if v is not None:
                sc = v[:3]
        return b["matrix"] @ _translate(pos) @ _quat_matrix(b["quat1"]) @ rot @ _quat_matrix(b["quat2"]) @ _scale(sc)
    if n.matrix is not None:
        return n.matrix
    return np.eye(4)


def world_matrices(e: edm.Edm, args: dict) -> list[np.ndarray]:
    out: list[np.ndarray | None] = [None] * len(e.nodes)

    def get(i: int) -> np.ndarray:
        if out[i] is not None:
            return out[i]
        chain = []
        j = i
        while 0 <= j < len(e.nodes) and out[j] is None and j not in chain:
            chain.append(j)
            p = e.nodes[j].parent
            j = p if p != j else -1
        base = out[j] if 0 <= j < len(e.nodes) and out[j] is not None else np.eye(4)
        for k in reversed(chain):
            base = base @ local_matrix(e.nodes[k], args)
            out[k] = base
        return out[i]

    for i in range(len(e.nodes)):
        get(i)
    return out  # type: ignore[return-value]


def visible_nodes(e: edm.Edm, args: dict) -> np.ndarray:
    """Whether each node shows at the arguments: every visibility switch above it on, every LOD the nearest."""
    vis = np.ones(len(e.nodes), bool)
    for i, n in enumerate(e.nodes):
        if n.vis:
            on = True
            for arg, ranges in n.vis:
                a = args.get(arg, 0.0)
                if not any(s <= a < t for s, t in ranges):
                    on = False
            vis[i] = on
        if n.lods and n.children:
            kids = sorted(n.children)
            for k, c in enumerate(kids):
                near = n.lods[k][0] if k < len(n.lods) else 1.0
                if k > 0 and near > 0:
                    vis[c] = False
    out = vis.copy()
    for i in range(len(e.nodes)):  # parents come before children in the file; follow the chain anyway
        j, seen = e.nodes[i].parent, 0
        while 0 <= j < len(e.nodes) and seen < 512:
            if not vis[j]:
                out[i] = False
                break
            j, seen = e.nodes[j].parent, seen + 1
    return out


def _moving_ancestor(e: edm.Edm, i: int, args: tuple) -> int:
    """The nearest node at or above `i` turned by one of `args`, or -1."""
    seen = 0
    while 0 <= i < len(e.nodes) and seen < 512:
        n = e.nodes[i]
        if any(a in args for a, _ in n.rot):
            return i
        i, seen = n.parent, seen + 1
    return -1


def _gear_named(*names: str) -> bool:
    """A mesh, its node or that node's parent named as running gear ("track_L", "wheel_3"), not "above_tracks"."""
    return any(GEAR_NAME.search(n or "") and not NOT_GEAR.search(n or "") for n in names)


# ------------------------------------------------------------------------------------------------ assembly

def assemble(e: edm.Edm, domain: str, cls: str = "") -> dict:
    """The model at rest as {part: (verts, faces)} plus `pivots` and `dm`, in the figure frame."""
    args: dict = {}
    world = world_matrices(e, args)
    vis = visible_nodes(e, args)
    heli = domain == "air" and cls.startswith("heli")
    turret_args = TURRET_ARGS.get(domain, ())
    gun_args = GUN_ARGS.get(domain, ())
    rotor_args = ROTOR_ARGS["heli"] if heli else ()
    wheel_args = WHEEL_ARGS.get(domain, ())
    parts: dict[str, list] = {"hull": [], "gear": [], "turret": [], "gun": [], "rotor": []}
    pivot_nodes: dict[str, int] = {}

    def part_of(node: int, name: str) -> str:
        if rotor_args:
            r = _moving_ancestor(e, node, rotor_args)
            if r >= 0:
                pivot_nodes.setdefault("rotor", r)
                return "rotor"
        if gun_args:
            g = _moving_ancestor(e, node, gun_args)
            if g >= 0 and _moving_ancestor(e, g, turret_args) >= 0:
                pivot_nodes.setdefault("gun", g)
                pivot_nodes.setdefault("turret", _moving_ancestor(e, g, turret_args))
                return "gun"
        if turret_args:
            t = _moving_ancestor(e, node, turret_args)
            if t >= 0:
                pivot_nodes.setdefault("turret", t)
                return "turret"
        if wheel_args and _moving_ancestor(e, node, wheel_args) >= 0:
            return "gear"
        parent = e.nodes[node].parent
        if domain == "ground" and _gear_named(name, e.nodes[node].name, e.nodes[parent].name if parent >= 0 else ""):
            return "gear"
        return "hull"

    for m in e.meshes.get("RENDER_NODES", []) + e.meshes.get("SKIN_NODES", []):
        if m is None or not len(m.indices) or m.positions.shape[1] < 3:
            continue
        if m.material is not None and (SKIP_MATERIAL.search(m.material.material) or m.material.blending == 3):
            if "glass" not in m.material.material:
                continue
        if SKIP_NAME.search(m.name or ""):
            continue
        pos = m.positions[:, :3].astype(np.float64)
        tri = m.indices[: len(m.indices) - len(m.indices) % 3].reshape(-1, 3)
        if m.type == "model::SkinNode":
            vnode = np.full(len(pos), -1, np.int64)
        elif len(m.parents) > 1:
            # A render node split over several nodes: each vertex's fourth component picks its node.
            table = np.array([p[0] for p in m.parents], np.int64)
            w = np.clip(np.rint(m.positions[:, 3]).astype(np.int64), 0, len(table) - 1)
            vnode = table[w]
        else:
            vnode = np.full(len(pos), m.parents[0][0] if m.parents else -1, np.int64)
        vnode[(vnode < 0) | (vnode >= len(e.nodes))] = -1
        placed = pos.copy()
        for node in np.unique(vnode):
            if node >= 0:
                sel = vnode == node
                mat = world[node]
                placed[sel] = pos[sel] @ mat[:3, :3].T + mat[:3, 3]
        tnode = vnode[tri[:, 0]]
        for node in np.unique(tnode):
            if node >= 0 and (not vis[node] or SKIP_NAME.search(e.nodes[node].name or "")):
                continue
            sub = tri[tnode == node]
            if node >= 0:
                ok = vis[np.maximum(vnode[sub], 0)].all(1)
                sub = sub[ok]
            if not len(sub):
                continue
            used, inv = np.unique(sub, return_inverse=True)
            if node >= 0:
                part = part_of(int(node), m.name)
            elif domain == "ground" and _gear_named(m.name):
                part = "gear"
            elif m.bones and 0 <= m.bones[0] < len(e.nodes):
                part = part_of(int(m.bones[0]), m.name)  # a skinned mesh moves with its bones' part (rotor blades)
            else:
                part = "hull"
            parts[part].append((placed[used], inv.reshape(-1, 3)))
    out = {}
    for p, items in parts.items():
        if items:
            from .modelpack import merge
            out[p] = merge(items)
    pivots = {}
    for p, i in pivot_nodes.items():
        if p in out:
            pivots[p] = [round(float(x), 4) for x in world[i][:3, 3]]
    dm = []
    for m in e.meshes.get("SHELL_NODES", []):
        if m is None or not len(m.indices) or m.positions.shape[1] < 3:
            continue
        node = m.parents[0][0] if m.parents else -1
        mat = world[node] if 0 <= node < len(e.nodes) else np.eye(4)
        v = m.positions[:, :3].astype(np.float64) @ mat[:3, :3].T + mat[:3, 3]
        f = m.indices[: len(m.indices) - len(m.indices) % 3].reshape(-1, 3)
        if not len(f) or int(f.max()) >= len(v):
            continue
        part = part_of(node, m.name) if 0 <= node < len(e.nodes) else "hull"
        dm.append((m.name or f"shell{len(dm)}", v, f, {"part": part, "group": "shell"}))
    return {"parts": out, "pivots": pivots, "dm": dm}


# ------------------------------------------------------------------------------------------------ files

def shape_index(roots: list[Path]) -> dict[str, Path]:
    """Lower-case model name (no extension) -> its `.edm` or `.lods` file, the first root's first."""
    out: dict[str, Path] = {}
    for root in roots:
        if not root.is_dir():
            continue
        for dirpath, files in _walk(root):
            if "shapes" not in dirpath.lower().replace("\\", "/"):
                continue
            for f in files:
                low = f.lower()
                if low.endswith((".edm", ".lods")):
                    stem = low.rsplit(".", 1)[0]
                    key = stem + (".lods" if low.endswith(".lods") else "")
                    out.setdefault(key, Path(dirpath) / f)
    return out


def resolve(shape: str, index: dict[str, Path]) -> Path | None:
    """A unit's nearest model file: the first level of its `.lods`, else the `.edm` itself."""
    s = shape.lower().strip().rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
    s = s[:-4] if s.endswith(".edm") else s
    lods = index.get(s + ".lods")
    if lods is not None:
        try:
            text = lods.read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        first = re.search(r'\{\s*"([^"]+)"\s*,', text)
        if first:
            name = first.group(1).lower()
            name = name[:-4] if name.endswith(".edm") else name
            p = index.get(name) or (lods.parent / first.group(1) if (lods.parent / first.group(1)).is_file() else None)
            if p is not None:
                return p
    return index.get(s)


_NAME_RX = re.compile(r'\b(\w+)\.Name\s*=\s*"([^"]+)"')
_SHAPE_RX = re.compile(r'\b(\w+)\.visual\.shape\s*=\s*"([^"]+)"')


def shapes_from_lua(roots: list[Path]) -> dict[str, str]:
    """Type name -> model name for units whose Lua sets `<T>.visual.shape = "..."` field by field (the catalogue's
    table reading sees only shapes written inside the table)."""
    out: dict[str, str] = {}
    for root in roots:
        if not root.is_dir():
            continue
        for dirpath, files in _walk(root):
            low = dirpath.lower().replace("\\", "/")
            if "database" not in low and "/units" not in low:
                continue
            for f in files:
                if not f.lower().endswith(".lua"):
                    continue
                try:
                    text = (Path(dirpath) / f).read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                shapes = dict(_SHAPE_RX.findall(text))
                for var, name in _NAME_RX.findall(text):
                    if var in shapes:
                        out.setdefault(name, shapes[var])
    return out


def roots_of(dcs: Path, extra: list[Path]) -> list[Path]:
    roots = [dcs / "Bazar" / "World" / "Shapes", dcs / "CoreMods", dcs / "Mods" / "aircraft", dcs / "Mods" / "tech"]
    for x in extra:
        roots += [Path(x) / "Mods" / "aircraft", Path(x) / "Mods" / "tech"]
    return roots


#: Folders under a module that hold no models or unit Lua (walked past).
_PRUNE = {"textures", "sounds", "liveries", "cockpit", "terrains", "doc", "docs", "missions", "campaigns",
          "input", "l10n", "theme", "skins", "fonts", "images", "mfd", "indicators", "effects"}


def _walk(root: Path):
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d.lower() not in _PRUNE]
        yield dirpath, files


def fingerprint(path: Path) -> str:
    st = path.stat()
    return hashlib.sha1(f"{path.name}|{st.st_size}|{int(st.st_mtime)}".encode()).hexdigest()[:16]


def build(dcs: Path, extra: list[Path], out: Path, items: list[dict], game_build: str, source: str,
          only: set[str] | None = None, log=print) -> dict:
    """Writes the pack; returns counts and the files skipped."""
    t0 = time.monotonic()
    roots = roots_of(dcs, extra)
    index = shape_index(roots)
    lua_shapes = shapes_from_lua(roots[1:])
    pack = Pack(out, "dcs", game_build, source)
    stats = {"written": 0, "fresh": 0, "nomodel": 0, "failed": 0, "protected": [], "partial": 0}
    by_file: dict[Path, list[dict]] = {}
    for it in items:
        if it.get("kind") != "vehicle" or it.get("class") == "static":
            continue
        if only and it["id"] not in only:
            continue
        path = resolve(it.get("shape") or "", index) if it.get("shape") else None
        if path is None and lua_shapes.get(it["id"]):
            path = resolve(lua_shapes[it["id"]], index)
        if path is None:
            path = resolve(it["id"], index)
        if path is None:
            stats["nomodel"] += 1
            continue
        by_file.setdefault(path, []).append(it)
    for path, units in sorted(by_file.items(), key=lambda kv: kv[1][0]["id"].lower()):
        first, rest = units[0], units[1:]
        fp = fingerprint(path)
        if pack.fresh(first["id"], fp):
            stats["fresh"] += 1
            continue
        try:
            head = path.open("rb").read(3)
        except OSError:
            head = b""
        if head != b"EDM":
            stats["protected"].append(str(path))
            log(f"   skipped {path.name}: not an EDM model this reader can open (protected or another format)")
            continue
        try:
            e = edm.read_file(path)
            dom = first.get("domain") or "ground"
            got = assemble(e, dom, first.get("class") or "")
            if not got["parts"]:
                raise ValueError("no geometry")
            if e.stopped:
                stats["partial"] += 1
            domain = "heli" if dom == "air" and (first.get("class") or "").startswith("heli") else dom
            key = first.get("key") or first.get("name") or first["id"]
            entry = pack.add(first["id"], got["parts"], domain, first.get("class") or domain, key=key,
                             pivots=got["pivots"], aliases=[u["id"] for u in rest], dm=got["dm"], fingerprint=fp,
                             extra={"name": first.get("name") or first["id"], "model": path.name,
                                    **({"partial": e.stopped} if e.stopped else {})})
            names = {u.get("key") or "" for u in units} | {u.get("name") or "" for u in units}
            entry["names"] = sorted(n for n in names if n and norm_key(n) != norm_key(entry["name"]))
            stats["written"] += 1
        except (edm.EdmError, ValueError, IndexError, OSError) as exc:
            stats["failed"] += 1
            log(f"   FAILED {first['id']} ({path.name}): {exc}")
    pack.save()
    stats["seconds"] = round(time.monotonic() - t0)
    stats["bytes"] = sum((out / e["file"]).stat().st_size for e in pack.index["units"].values()
                         if (out / e["file"]).is_file())
    stats["units"] = len(pack.index["units"])
    return stats
