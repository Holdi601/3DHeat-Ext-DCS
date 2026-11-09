"""
The scene reader and the buildings drawn from it, on a .scn5 built to the
layout real ones have (see heat3d_ext_dcs/scene5.py): no game data is kept here.
"""

from __future__ import annotations

import math
import struct

import numpy as np
import pytest

from heat3d_ext_dcs import buildings
from heat3d_ext_dcs.level import Region
from heat3d_ext_dcs.scene5 import Scene5
from heat3d_ext_dcs.surface5 import FormatError


def _s(text: str) -> bytes:
    raw = text.encode()
    return struct.pack("<I", len(raw)) + raw


def _entry(name: str, kind: int, size: int, count: int, at: int) -> bytes:
    return struct.pack("<I", 1) + _s(name) + struct.pack("<HHIQIH", kind, size, 0, count, at & 0xFFFFFFFF, at >> 32)


def _axis(v) -> list[int]:
    return [int(round(c * 32767 + 32768)) for c in v]


def write_scene(path, models, nodes) -> None:
    """models: [(name, box6)]; nodes: [(translation, [(model, (x, y, z) in the node, heading_deg)])]."""
    index = bytearray(struct.pack("<IIQ", 2, 0x30, 0) + b"\0" * 16)
    index += _s("landscape5::Scene5File") + struct.pack("<II", 9, len(models))
    for name, _ in models:
        index += _s(name)
    index += struct.pack("<I", len(models))
    for _, box in models:
        index += struct.pack("<6f", *box)
    index += struct.pack("<I", 1) + struct.pack("<I", 2) + _s("HwInstancer5.2") + _s("Undef")
    index += struct.pack("<I", 1) + _s("shaderDefine") + struct.pack("<II", 0, 1) + _s("NODEFINITIONS") + b"\xff" * 4
    index += struct.pack("<II", 0, len(nodes))
    data = bytearray()

    def add(raw: bytes) -> int:
        at = len(data)
        data.extend(raw + b"\0" * (-len(raw) % 16))
        return at

    for t, inst in nodes:
        n = len(inst)
        p = np.array([q for _, q, _ in inst], "<f4")
        mod = np.array([0x300000 | m for m, _, _ in inst], "<u4")
        ax = []
        for _, _, h in inst:
            c, s = math.cos(math.radians(h)), math.sin(math.radians(h))
            ax.append(_axis((c, 0, s)) + _axis((-s, 0, c)))
        ax = np.array(ax, "<u2")
        world = p + np.array(t, "<f4")
        bounds = list(world.min(0)) + list(world.max(0))
        m = np.eye(4)
        m[3, :3] = t
        index += struct.pack("<16d", *m.reshape(-1)) + struct.pack("<f", 100.0) + struct.pack("<6f", *bounds)
        index += struct.pack("<IIII", 0, 2, n, 4)
        index += _entry("P", 2, 12, n * 12, add(p.tobytes()))
        index += _entry("TYPE_OPTIONS", 4, 4, n * 4, add(mod.tobytes()))
        index += _entry("SEED_SCALE", 4, 4, n * 4, add(np.zeros(n, "<u4").tobytes()))
        index += _entry("AXIS", 6, 12, n * 12, add(ax.tobytes()))
        models_here = sorted({m for m, _, _ in inst})
        index += struct.pack("<II", 0, len(models_here)) + struct.pack(f"<{len(models_here)}I", *models_here)
        index += struct.pack("<I", 8) + b"\xff" * 4
    struct.pack_into("<Q", index, 8, len(index))
    path.write_bytes(bytes(index) + bytes(data))


MODELS = [
    ("european_beech", (-10, 0, -10, 10, 29, 10)),
    ("home2_b", (-4, -11.6, -11, 4, 7.9, 11)),
    ("lap-house", (-32, -10, -10, 4, 13, 10)),
    ("blk_light_pole", (-1.5, -3, 0, 1.5, 9.7, 0.1)),
    ("unused", (0, 0, 0, 0, 0, 0)),
]


@pytest.fixture
def scene(tmp_path):
    path = tmp_path / "Test.scn5"
    write_scene(
        path,
        MODELS,
        [
            ((-100000.0, 0.0, 600000.0), [(0, (5, 300, 5), 0), (1, (100, 310, 50), 90), (3, (0, 300, 0), 0)]),
            ((-50000.0, 0.0, 700000.0), [(2, (0, 500, 0), 30)]),
        ],
    )
    return path


def test_reads_models_nodes_and_placements(scene):
    with Scene5(scene) as s:
        assert s.version == 9
        assert s.models[1] == "home2_b"
        assert s.boxes[2, 0] == -32
        assert len(s.nodes) == 2 and s.instance_count == 4
        inst = s.instances()
        assert inst.model.tolist() == [0, 1, 3, 2]
        assert inst.position[1] == pytest.approx((-99900, 310, 600050))
        # Turned 90 degrees: its x axis points east (DCS z).
        assert inst.x_axis[1] == pytest.approx((0, 0, 1), abs=1e-4)
        assert inst.z_axis[1] == pytest.approx((-1, 0, 0), abs=1e-4)
        far = Region(-60000, 690000, -40000, 710000)
        assert s.instances(touches=far.touches).model.tolist() == [2]
        assert s.instances(models={1}).model.tolist() == [1]


def test_buildings_are_told_by_name_and_box(scene):
    with Scene5(scene) as s:
        kinds = buildings.model_kinds(s.models, s.boxes)
        assert kinds == {1: "house", 2: "block"}
        inst = s.instances(models=set(kinds))
        rows = buildings.boxes(inst, s.boxes)
    house, lap = rows
    # The house: 8 x 22 m, its box centred on it, turned to the east, its footing 3 m deep at most.
    assert house[:2] == pytest.approx((-99900, 600050))
    assert house[2:6] == pytest.approx((307, 317.9, 4, 11), abs=1e-4)
    assert house[6:] == pytest.approx((0, 1), abs=1e-4)
    # The long house's box lies off its origin: 14 m back along its x axis (30 degrees east of north).
    c, sn = math.cos(math.radians(30)), math.sin(math.radians(30))
    assert lap[:2] == pytest.approx((-50000 - 14 * c, 700000 - 14 * sn), abs=1e-3)
    prim = buildings.mesh(rows, (1, 1, 1), "house")
    assert prim.positions.shape == (16, 3) and prim.triangles.shape == (20, 3)
    # Every face turns outward: its normal points away from the box's middle.
    p = prim.positions.astype(float)
    for a, b, cc in prim.triangles[:10]:
        n = np.cross(p[b] - p[a], p[cc] - p[a])
        mid = p[:8].mean(0)
        assert np.dot(n, (p[a] + p[b] + p[cc]) / 3 - mid) > 0


def test_a_file_of_another_kind_is_refused(tmp_path):
    bad = tmp_path / "x.scn5"
    bad.write_bytes(struct.pack("<IIQ", 2, 0x30, 0x80) + b"\0" * 16 + _s("landscape5::Surface5File") + b"\0" * 80)
    with pytest.raises(FormatError):
        Scene5(bad)
