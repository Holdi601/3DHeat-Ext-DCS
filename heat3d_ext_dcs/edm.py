"""
A reader for DCS World's `.edm` models (versions 8 and 10): the node tree, its transforms and animation arguments,
levels of detail and visibility switches, and the triangle meshes that hang from it, with every vertex placed in the
model's own frame for a chosen set of argument values.

The file is little-endian. After the magic `EDM` and a 16-bit version, a version 10 file has a string table (a
32-bit size and that many bytes of NUL-separated strings); every later string is a 32-bit index into it (version 8
writes strings inline, a 32-bit length and the bytes). Two maps of object counts follow, then the root node, the
list of transform nodes (each written as its type name and then its fields), one parent index per node, and the
render items: a map from a category name to a list of typed objects (render nodes, skinned nodes, collision
shells, connectors, lights...).

Each object type is read field by field; the reader knows the layouts it needs to reach the meshes and stops with
`EdmError` naming the type and offset where it meets one it does not know. Nothing here writes or changes a file.
"""

from __future__ import annotations

import math
import struct
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


class EdmError(ValueError):
    pass


class Reader:
    def __init__(self, data: bytes):
        self.b = data
        self.o = 0
        self.strings: list[str] | None = None

    def take(self, n: int) -> bytes:
        if self.o + n > len(self.b):
            raise EdmError(f"read past the end at {self.o} (+{n})")
        v = self.b[self.o:self.o + n]
        self.o += n
        return v

    def u8(self) -> int:
        if self.o >= len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = self.b[self.o]
        self.o += 1
        return v

    def u16(self) -> int:
        if self.o + 2 > len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = struct.unpack_from("<H", self.b, self.o)[0]
        self.o += 2
        return v

    def u32(self) -> int:
        if self.o + 4 > len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = struct.unpack_from("<I", self.b, self.o)[0]
        self.o += 4
        return v

    def i32(self) -> int:
        if self.o + 4 > len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = struct.unpack_from("<i", self.b, self.o)[0]
        self.o += 4
        return v

    def f32(self) -> float:
        if self.o + 4 > len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = struct.unpack_from("<f", self.b, self.o)[0]
        self.o += 4
        return v

    def f64(self) -> float:
        if self.o + 8 > len(self.b):
            raise EdmError(f"read past the end at {self.o}")
        v = struct.unpack_from("<d", self.b, self.o)[0]
        self.o += 8
        return v

    def arr(self, dtype: str, n: int) -> np.ndarray:
        dt = np.dtype(dtype)
        if n < 0 or self.o + n * dt.itemsize > len(self.b):
            raise EdmError(f"array of {n} past the end at {self.o}")
        v = np.frombuffer(self.b, dt, n, self.o)
        self.o += n * dt.itemsize
        return v

    def vec(self, n: int) -> tuple:
        return tuple(self.arr("<f8", n).tolist())

    def vecf(self, n: int) -> tuple:
        return tuple(self.arr("<f4", n).tolist())

    def string(self) -> str:
        if self.strings is not None:
            i = self.u32()
            if i >= len(self.strings):
                raise EdmError(f"string index {i} out of range at {self.o - 4}")
            return self.strings[i]
        n = self.u32()
        return self.take(n).decode("latin-1")

    def text(self) -> str:
        """A string written in place (a 32-bit length and the bytes), as node names are in every version."""
        n = self.u32()
        return self.take(n).decode("latin-1")

    def matrix(self) -> np.ndarray:
        return self.arr("<f8", 16).reshape(4, 4).T.copy()  # stored column-major


# ---------------------------------------------------------------------------------------------------- properties

def _value(r: Reader, kind: str):
    if kind == "unsigned int":
        return r.u32()
    if kind == "int":
        return r.i32()
    if kind == "float":
        return r.f32()
    if kind == "osg::Vec2f":
        return r.vecf(2)
    if kind == "osg::Vec3f":
        return r.vecf(3)
    if kind == "osg::Vec4f":
        return r.vecf(4)
    if kind == "osg::Vec2d":
        return r.vec(2)
    if kind == "osg::Vec3d":
        return r.vec(3)
    if kind in ("const char*", "std::string", "string"):
        return r.string()
    raise EdmError(f"property type {kind!r} at {r.o}")


def read_property(r: Reader) -> tuple[str, object]:
    t = r.string()
    if t.startswith("model::Property<") and t.endswith(">"):
        kind = t[len("model::Property<"):-1]
        name = r.string()
        return name, _value(r, kind)
    if t.startswith("model::AnimatedProperty<") and t.endswith(">"):
        kind = t[len("model::AnimatedProperty<"):-1]
        name = r.string()
        arg = r.u32()
        keys = [(r.f64(), _value(r, kind)) for _ in range(r.u32())]
        return name, {"arg": arg, "keys": keys}
    if t == "model::ArgumentProperty":
        name = r.string()
        return name, {"arg": r.u32()}
    raise EdmError(f"property object {t!r} at {r.o}")


def read_props(r: Reader) -> dict:
    return dict(read_property(r) for _ in range(r.u32()))


# ---------------------------------------------------------------------------------------------------- materials

@dataclass
class Material:
    name: str = ""
    material: str = ""
    vertex_format: list[int] = field(default_factory=list)
    textures: list[str] = field(default_factory=list)
    blending: int = 0


def read_material(r: Reader) -> Material:
    m = Material()
    for _ in range(r.u32()):
        key = r.string()
        if key in ("BLENDING", "SHADOWS", "CULLING", "DECAL"):
            v = r.u8()
            if key == "BLENDING":
                m.blending = v
        elif key == "DEPTH_BIAS":
            r.u32()
        elif key == "VERTEX_FORMAT":
            m.vertex_format = list(r.take(r.u32()))
        elif key == "TEXTURE_COORDINATES_CHANNELS":
            r.arr("<i4", r.u32())
        elif key == "MATERIAL_NAME":
            m.material = r.string()
        elif key == "NAME":
            m.name = r.string()
        elif key == "TEXTURES":
            for _ in range(r.u32()):
                r.i32()
                r.i32()
                m.textures.append(r.string())
                r.arr("<u4", 4)
                r.arr("<f4", 16)
        elif key in ("UNIFORMS", "ANIMATED_UNIFORMS"):
            read_props(r)
        else:
            raise EdmError(f"material key {key!r} at {r.o}")
    return m


# ---------------------------------------------------------------------------------------------------- nodes

@dataclass
class Node:
    type: str
    name: str = ""
    props: dict = field(default_factory=dict)
    parent: int = -1
    #: The node's rest transform (4x4, column vectors) when it has one.
    matrix: np.ndarray | None = None
    #: ArgAnimationNode: base pose and per-argument keys.
    base: dict | None = None
    pos: list = field(default_factory=list)  # [(arg, [(frame, (x, y, z))])]
    rot: list = field(default_factory=list)  # [(arg, [(frame, (x, y, z, w))])]
    scale: list = field(default_factory=list)
    #: ArgVisibilityNode: [(arg, [(start, end)])]
    vis: list = field(default_factory=list)
    #: LodNode: [(near, far)] metres, one per child in order.
    lods: list = field(default_factory=list)
    children: list[int] = field(default_factory=list)


def _node_base(r: Reader, n: Node) -> None:
    n.name = r.text()
    r.u32()  # the node's own version
    n.props = read_props(r)


def _anim_base(r: Reader, n: Node) -> None:
    m = r.matrix()
    pos = r.vec(3)
    q1 = r.vec(4)
    q2 = r.vec(4)
    sc = r.vec(3)
    n.base = {"matrix": m, "position": pos, "quat1": q1, "quat2": q2, "scale": sc}


def _anim_keys(r: Reader, n: Node) -> None:
    n.pos = [(r.u32(), [(r.f64(), r.vec(3)) for _ in range(r.u32())]) for _ in range(r.u32())]
    n.rot = [(r.u32(), [(r.f64(), r.vec(4)) for _ in range(r.u32())]) for _ in range(r.u32())]
    sc = []
    for _ in range(r.u32()):
        arg = r.u32()
        keys = [(r.f64(), r.vec(4)) for _ in range(r.u32())]
        r.arr("<f8", 4 * r.u32())  # a second key list the scale keys carry (unused)
        sc.append((arg, keys))
    n.scale = sc


def read_node(r: Reader, t: str) -> Node:
    n = Node(t)
    if t == "model::Node":
        _node_base(r, n)
    elif t == "model::TransformNode":
        _node_base(r, n)
        n.matrix = r.matrix()
    elif t == "model::Bone":
        _node_base(r, n)
        n.matrix = r.matrix()
        r.matrix()
    elif t in ("model::ArgAnimationNode", "model::ArgRotationNode", "model::ArgPositionNode", "model::ArgScaleNode"):
        _node_base(r, n)
        _anim_base(r, n)
        _anim_keys(r, n)
    elif t == "model::ArgAnimatedBone":
        _node_base(r, n)
        _anim_base(r, n)
        _anim_keys(r, n)
        r.matrix()
    elif t == "model::ArgVisibilityNode":
        _node_base(r, n)
        n.vis = [(r.u32(), [(r.f64(), r.f64()) for _ in range(r.u32())]) for _ in range(r.u32())]
        if n.props.get("__VERSION__") == 1:
            n.matrix = r.arr("<f4", 16).astype(np.float64).reshape(4, 4).T.copy()  # this version carries a transform
    elif t == "model::LodNode":
        _node_base(r, n)
        n.lods = [(math.sqrt(max(0.0, r.f64())), math.sqrt(max(0.0, r.f64()))) for _ in range(r.u32())]
    else:
        raise EdmError(f"node type {t!r} at {r.o}")
    return n


# ---------------------------------------------------------------------------------------------------- render items

@dataclass
class Mesh:
    """Triangles of one render, skin or shell node: positions in its parent node's frame, or per range of
    indices in each of several parents' frames (a render node split over parents)."""
    type: str
    name: str
    material: Material | None
    positions: np.ndarray  # (n, 3) float
    indices: np.ndarray  # (m,) int
    #: [(node index, damage argument, first index)]: which node each run of indices hangs from.
    parents: list = field(default_factory=list)
    damage_arg: int = -1
    bones: list[int] = field(default_factory=list)
    weights: np.ndarray | None = None
    joints: np.ndarray | None = None


def _vertices(r: Reader) -> np.ndarray:
    count = r.u32()
    stride = r.u32()
    return r.arr("<f4", count * stride).reshape(count, stride) if stride else np.zeros((count, 0), np.float32)


def _indices(r: Reader) -> np.ndarray:
    kind = r.u8()
    count = r.u32()
    r.u32()
    dt = {0: "<u1", 1: "<u2", 2: "<u4"}.get(kind)
    if dt is None:
        raise EdmError(f"index size {kind} at {r.o}")
    return r.arr(dt, count).astype(np.int64)


def _parents(r: Reader) -> list:
    count = r.u32()
    if count == 1:
        return [(r.u32(), r.i32(), 0)]
    return [(r.u32(), r.i32(), r.u32()) for _ in range(count)]


def read_item(r: Reader, t: str, materials: list[Material]) -> object:
    if t in ("model::RenderNode", "model::NumberNode"):
        name = r.text()
        r.u32()
        read_props(r)
        r.u32()
        mi = r.u32()
        if mi >= len(materials):
            raise EdmError(f"material {mi} of {len(materials)} at {r.o}")
        mat = materials[mi]
        parents = _parents(r)
        v = _vertices(r)
        idx = _indices(r)
        if t == "model::NumberNode":
            r.take(16 * r.u32())  # the digits' arguments and steps; a number plate is not drawn here
            return None
        return Mesh(t, name, mat, v, idx, parents, parents[0][1] if parents else -1)
    if t == "model::SkinNode":
        name = r.text()
        r.u32()
        read_props(r)
        r.u32()
        mat = materials[r.u32()]
        bones = list(r.arr("<u4", r.u32()).tolist())
        post = r.i32()
        v = _vertices(r)
        idx = _indices(r)
        return Mesh(t, name, mat, v, idx, [(post, -1, 0)], -1, bones)
    if t == "model::ShellNode":
        name = r.text()
        r.u32()
        read_props(r)
        parent = r.u32()
        r.take(r.u32())  # vertex format
        v = _vertices(r)
        idx = _indices(r)
        return Mesh(t, name, None, v, idx, [(parent, -1, 0)])
    if t == "model::SegmentsNode":
        name = r.text()
        r.u32()
        read_props(r)
        r.u32()  # parent
        r.arr("<f4", 6 * r.u32())  # line segments, two points each
        return None
    if t == "model::FakeOmniLightsNode":
        r.text()
        r.u32()
        read_props(r)
        r.u32()
        if r.u32() >= len(materials):
            raise EdmError(f"material out of range at {r.o}")
        _parents(r)
        r.arr("<f4", 12 * r.u32())  # one sprite per light
        return None
    if t == "model::LightNode":
        r.text()
        r.u32()
        read_props(r)
        r.u32()  # parent
        r.u8()
        read_props(r)  # colour, brightness, distance, angles...
        r.u8()
        return None
    if t == "model::Connector":
        r.text()
        r.u32()
        read_props(r)
        r.u32()
        r.u32()
        return None
    raise EdmError(f"render item {t!r} at {r.o}")


# ---------------------------------------------------------------------------------------------------- file

@dataclass
class Edm:
    version: int
    materials: list[Material]
    nodes: list[Node]
    meshes: dict[str, list]  # category -> items read (None for those carrying no mesh)
    root_props: dict = field(default_factory=dict)
    bbox: tuple = ()
    #: The category where reading stopped early (an item type not known), or "".
    stopped: str = ""
    #: Item types passed over (their layout is not known), in order.
    skipped: list = field(default_factory=list)


def read(data: bytes, want: tuple[str, ...] = ("RENDER_NODES", "SHELL_NODES", "SKIN_NODES")) -> Edm:
    r = Reader(data)
    if r.take(3) != b"EDM":
        raise EdmError("not an EDM file")
    version = r.u16()
    if version not in (8, 10):
        raise EdmError(f"EDM version {version}")
    if version == 10:
        size = r.u32()
        r.strings = r.take(size).decode("latin-1").split("\0")
    for _ in range(2):
        for _ in range(r.u32()):
            r.string()
            r.u32()
    t = r.string()
    if t != "model::RootNode":
        raise EdmError(f"root is {t!r}")
    r.text()
    r.u32()
    root_props = read_props(r)
    bmin = r.vec(3)
    bmax = r.vec(3)
    r.arr("<f8", 12)
    materials = [read_material(r) for _ in range(r.u32())]
    r.arr("<u4", 2)
    nodes = [read_node(r, r.string()) for _ in range(r.u32())]
    for i, p in enumerate(r.arr("<i4", len(nodes)).tolist()):
        nodes[i].parent = p
        if 0 <= p < len(nodes) and p != i:
            nodes[p].children.append(i)
    meshes: dict[str, list] = {}
    stopped = ""
    skipped: list[str] = []
    known = {i for i, t in enumerate(r.strings or []) if t in ITEM_TYPES}
    cats = {i for i, t in enumerate(r.strings or []) if t.isupper() and t.endswith("_NODES") or t == "CONNECTORS"}
    for _ in range(r.u32()):
        if r.o >= len(r.b):  # some files end without their last categories
            break
        cat = r.string()
        items = []
        n = r.u32()
        k = 0
        while k < n:
            if r.o + 4 > len(r.b):
                stopped = f"{cat}: the file ends after {k} of {n} items"
                break
            at = r.o
            t = r.string()
            try:
                items.append(read_item(r, t, materials))
                k += 1
                continue
            except EdmError as exc:
                if not known:
                    stopped = f"{cat}: {exc}"
                    break
                skipped.append(t)
            # An item whose layout is not known (a number plate, a light sprite...): find where the next one begins.
            if not _resync(r, at + 4, known, cats, materials, last=k + 1 >= n):
                stopped = f"{cat}: could not pass {t!r} at {at}"
                break
            k += 1
        meshes[cat] = items
        if stopped:
            break
    return Edm(version, materials, nodes, meshes, root_props, (bmin, bmax), stopped, skipped)


#: Render item types `read_item` reads, by name.
ITEM_TYPES = {"model::RenderNode", "model::NumberNode", "model::SkinNode", "model::ShellNode", "model::SegmentsNode", "model::Connector",
              "model::LightNode", "model::FakeOmniLightsNode"}


def _sane(m) -> bool:
    if m is None:
        return True
    v, i = m.positions, m.indices
    return 3 <= v.shape[1] <= 64 and (not len(i) or (int(i.max()) < len(v) and len(i) % 3 == 0))


def _resync(r: Reader, start: int, known: set, cats: set, materials: list, last: bool) -> bool:
    """Moves `r` to the first offset from `start` where a known item reads whole and is followed by another item
    or the next category (or the end, for the category's last item)."""
    b = r.b
    keys = [struct.pack("<I", i) for i in known]
    pos = start
    while True:
        cands = [x for x in (b.find(k, pos) for k in keys) if x >= 0]
        if not cands:
            return False
        p = min(cands)
        save = r.o
        r.o = p
        try:
            t = r.string()
            m = read_item(r, t, materials)
            end = r.o
            ok = _sane(m)
            if ok and end + 4 <= len(b):
                nxt = struct.unpack_from("<I", b, end)[0]
                ok = nxt in known or (last and nxt in cats)
            elif ok:
                ok = last
        except (EdmError, IndexError, ValueError):
            ok = False
        if ok:
            r.o = p
            return True
        r.o = save
        pos = p + 1


def read_file(path: Path) -> Edm:
    return read(Path(path).read_bytes())
