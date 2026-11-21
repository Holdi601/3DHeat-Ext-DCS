"""The EDM reader and the model pack on a small model written here: no game file is read."""

import json
import struct

import numpy as np
import pytest

from heat3d_ext_dcs import edm, models


class W:
    """Writes a version 10 EDM file the way the reader expects one."""

    def __init__(self):
        self.strings: list[str] = []
        self.body = bytearray()

    def sym(self, s: str) -> None:
        if s not in self.strings:
            self.strings.append(s)
        self.u32(self.strings.index(s))

    def text(self, s: str) -> None:
        b = s.encode()
        self.u32(len(b))
        self.body += b

    def u8(self, v):
        self.body += struct.pack("<B", v)

    def u32(self, v):
        self.body += struct.pack("<I", v)

    def i32(self, v):
        self.body += struct.pack("<i", v)

    def f64s(self, *v):
        self.body += struct.pack(f"<{len(v)}d", *v)

    def f32s(self, *v):
        self.body += struct.pack(f"<{len(v)}f", *v)

    def matrix(self, m):
        self.f64s(*np.asarray(m, float).T.reshape(-1))

    def props(self):
        self.u32(1)
        self.sym("model::Property<unsigned int>")
        self.sym("__VERSION__")
        self.u32(1)

    def node_base(self, type_, name):
        self.sym(type_)
        self.text(name)
        self.u32(0)
        self.props()

    def done(self) -> bytes:
        table = "\0".join(self.strings).encode() + b"\0"
        return b"EDM" + struct.pack("<H", 10) + struct.pack("<I", len(table)) + table + bytes(self.body)


def _box(lo, hi):
    x0, y0, z0 = lo
    x1, y1, z1 = hi
    v = np.array([[x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
                  [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]], float)
    f = np.array([[0, 2, 1], [0, 3, 2], [4, 5, 6], [4, 6, 7], [0, 1, 5], [0, 5, 4],
                  [2, 3, 7], [2, 7, 6], [1, 2, 6], [1, 6, 5], [0, 4, 7], [0, 7, 3]])
    return v, f


def _render(w: W, name: str, parents: list[int], v: np.ndarray, f: np.ndarray, which: np.ndarray | None = None):
    w.sym("model::RenderNode")
    w.text(name)
    w.u32(0)
    w.props()
    w.u32(0)
    w.u32(0)  # material
    if len(parents) == 1:
        w.u32(1)
        w.u32(parents[0])
        w.i32(-1)
    else:
        w.u32(len(parents))
        for p in parents:
            w.u32(p)
            w.i32(-1)
            w.u32(0xFFFFFFFF)
    w.u32(len(v))
    w.u32(4)
    for i, p in enumerate(v):
        w.f32s(*p, float(which[i]) if which is not None else 0.0)
    w.u8(1)
    w.u32(f.size)
    w.u32(5)
    w.body += np.asarray(f, "<u2").tobytes()


def tank_edm() -> bytes:
    """A hull box, a turret box on a yaw node (argument 0) 1.5 m up, a gun box on a pitch node (argument 1), wheels
    split over two nodes in one render node, a muzzle flash hidden at rest, a collision shell on the turret."""
    w = W()
    w.u32(0)  # two maps of object counts, empty
    w.u32(0)
    w.sym("model::RootNode")
    w.text("Scene Root")
    w.u32(0)
    w.props()
    w.f64s(-3, 0, -2, 3, 3, 2)
    w.f64s(*([0.0] * 12))
    w.u32(1)  # one material
    w.u32(3)
    w.sym("BLENDING")
    w.u8(0)
    w.sym("MATERIAL_NAME")
    w.sym("def_material")
    w.sym("VERTEX_FORMAT")
    w.u32(2)
    w.body += bytes([4, 0])
    w.u32(0)
    w.u32(0)
    nodes = []

    def transform(name, m):
        w.node_base("model::TransformNode", name)
        w.matrix(m)
        nodes.append(name)

    def rotation(name, arg, pos):
        w.node_base("model::ArgRotationNode", name)
        w.matrix(np.eye(4))
        w.f64s(*pos)
        w.f64s(0, 0, 0, 1)
        w.f64s(0, 0, 0, 1)
        w.f64s(1, 1, 1)
        w.u32(0)  # position tracks
        w.u32(1)  # rotation tracks
        w.u32(arg)
        w.u32(2)
        w.f64s(-1, 0, 1, 0, 0)  # frame -1: half a turn about y
        w.f64s(0, 0, 0, 0, 1)  # frame 0: rest
        w.u32(0)  # scale tracks
        nodes.append(name)

    w.u32(7)  # nodes
    w.node_base("model::Node", "")
    nodes.append("")
    transform("body", np.eye(4))
    rotation("Dummy Tower", 0, (0.5, 1.5, 0))
    rotation("Dummy Gun", 1, (1.0, 0.3, 0))
    transform("wheel_L", np.eye(4))
    transform("wheel_R", np.eye(4))
    w.node_base("model::ArgVisibilityNode", "Flame")
    w.u32(1)
    w.u32(44)
    w.u32(1)
    w.f64s(0.5, 1.0)
    w.f32s(*np.eye(4).reshape(-1))  # a visibility node of version 1 carries a transform
    nodes.append("Flame")
    for p in (-1, 0, 1, 2, 1, 1, 3):
        w.i32(p)
    w.u32(2)  # categories
    w.sym("SHELL_NODES")
    w.u32(1)
    sv, sf = _box((-1, 0, -1), (1, 0.8, 1))
    w.sym("model::ShellNode")
    w.text("Target_turret")
    w.u32(0)
    w.props()
    w.u32(2)
    w.u32(1)
    w.u8(3)
    w.u32(len(sv))
    w.u32(3)
    w.f32s(*sv.reshape(-1))
    w.u8(1)
    w.u32(sf.size)
    w.u32(5)
    w.body += np.asarray(sf, "<u2").tobytes()
    w.sym("RENDER_NODES")
    w.u32(5)
    hv, hf = _box((-3, 0.5, -1.5), (3, 1.5, 1.5))
    _render(w, "hull", [1], hv, hf)
    tv, tf = _box((-1, 0, -1), (1, 0.8, 1))
    _render(w, "turret", [2], tv, tf)
    gv, gf = _box((0, -0.1, -0.1), (3, 0.1, 0.1))
    _render(w, "gun", [3], gv, gf)
    lv, lf = _box((-2, 0, -1.6), (2, 0.6, -1.2))
    rv, rf = _box((-2, 0, 1.2), (2, 0.6, 1.6))
    which = np.r_[np.zeros(8), np.ones(8)]
    _render(w, "wheels", [4, 5], np.r_[lv, rv], np.r_[lf, rf + 8], which)
    fv, ff = _box((4, 1.7, -0.2), (5, 2.0, 0.2))
    _render(w, "flame", [6], fv, ff)
    return w.done()


def test_reads_the_tree_and_meshes():
    e = edm.read(tank_edm())
    assert e.version == 10 and not e.stopped
    assert [n.name for n in e.nodes][:4] == ["", "body", "Dummy Tower", "Dummy Gun"]
    assert e.nodes[3].parent == 2 and e.nodes[2].children == [3]
    assert [a for a, _ in e.nodes[2].rot] == [0]
    rn = [m for m in e.meshes["RENDER_NODES"] if m is not None]
    assert [m.name for m in rn] == ["hull", "turret", "gun", "wheels", "flame"]
    assert rn[3].parents[1][0] == 5 and len(rn[3].indices) == 72
    assert e.meshes["SHELL_NODES"][0].name == "Target_turret"


def test_rest_pose_parts_and_pivots():
    got = models.assemble(edm.read(tank_edm()), "ground", "mbt")
    parts = got["parts"]
    assert set(parts) == {"hull", "turret", "gun", "gear"}
    tv, _ = parts["turret"]
    assert tv[:, 1].min() == pytest.approx(1.5) and tv[:, 0].min() == pytest.approx(-0.5)
    gv, _ = parts["gun"]
    assert gv[:, 0].max() == pytest.approx(4.5) and gv[:, 1].mean() == pytest.approx(1.8)
    wv, wf = parts["gear"]
    assert len(wf) == 24 and wv[:, 2].min() == pytest.approx(-1.6) and wv[:, 2].max() == pytest.approx(1.6)
    assert got["pivots"]["turret"] == [0.5, 1.5, 0.0]
    assert got["pivots"]["gun"] == [1.5, 1.8, 0.0]
    hv, _ = parts["hull"]
    assert hv[:, 0].max() == pytest.approx(3)  # the muzzle flash at rest is hidden
    assert got["dm"][0][0] == "Target_turret" and got["dm"][0][3]["part"] == "turret"


def test_an_argument_turns_the_turret():
    e = edm.read(tank_edm())
    world = models.world_matrices(e, {0: -1.0})
    gun = world[3][:3, 3]
    assert gun == pytest.approx([0.5 - 1.0, 1.8, 0.0])


def test_not_an_edm_is_refused():
    with pytest.raises(edm.EdmError):
        edm.read(b"PK\x03\x04protected")


def test_pack_from_a_model(tmp_path):
    shapes = tmp_path / "dcs" / "Bazar" / "World" / "Shapes"
    shapes.mkdir(parents=True)
    (shapes / "tank.edm").write_bytes(tank_edm())
    (shapes / "locked.edm").write_bytes(b"\x00\x11protected bytes")
    (shapes / "tank.lods").write_text('model = { lods = { {"tank.edm", 100.0}, }, }')
    items = [{"id": "Tank A", "kind": "vehicle", "class": "mbt", "domain": "ground", "name": "MBT Tank A",
              "key": "Tank A", "shape": "tank"},
             {"id": "Tank B", "kind": "vehicle", "class": "mbt", "domain": "ground", "name": "Tank B", "key": "Tank A",
              "shape": "tank"},
             {"id": "Locked", "kind": "vehicle", "class": "apc", "domain": "ground", "name": "Locked", "shape": "locked"},
             {"id": "Nothing", "kind": "vehicle", "class": "apc", "domain": "ground", "name": "Nothing", "shape": "none"}]
    out = tmp_path / "pack"
    stats = models.build(tmp_path / "dcs", [], out, items, "1.0", "test", log=lambda m: None)
    assert stats["written"] == 1 and stats["nomodel"] == 1 and len(stats["protected"]) == 1
    index = json.loads((out / "model-pack.json").read_text(encoding="utf-8"))
    unit = index["units"]["Tank A"]
    assert unit["aliases"] == ["Tank B"] and unit["name"] == "Tank A"
    assert {"hull", "turret", "gun", "gear"} <= set(unit["parts"]) and unit["dm"] == 1
    assert (out / unit["file"]).read_bytes()[:4] == b"glTF"
    again = models.build(tmp_path / "dcs", [], out, items, "1.0", "test", log=lambda m: None)
    assert again["fresh"] == 1 and again["written"] == 0
