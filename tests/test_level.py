"""Building the level: classes, sea, region, thinning, and the .glb it writes."""

from __future__ import annotations

import numpy as np
import pytest

import synth
from heat3d_ext_dcs import glb
from heat3d_ext_dcs.level import COLOURS, Region, build, cluster, ground_height
from heat3d_ext_dcs.surface5 import Surface5


@pytest.fixture
def surface(tmp_path):
    root = synth.theatre(tmp_path)
    with Surface5(root / "Mods/terrains/TestTheatre/surface/TestTheatre.surface5") as s:
        yield s


def test_ground_water_and_classes(surface):
    lv = build(surface, "Test")
    assert lv.tiles == 2
    assert lv.classes == {"land": (32 - 8) + (32 - 8), "road": 8, "sea": 8}  # tile one less its road, tile two less its sea
    assert {p.label for p in lv.ground} == {"land", "road"}
    road = next(p for p in lv.ground if p.label == "road")
    assert road.colour == COLOURS["road"]
    # The road runs along z = 2000..2100 of the first tile.
    assert road.positions[:, 2].min() == 2000.0 and road.positions[:, 2].max() == 2100.0
    assert len(lv.water) == 1 and np.all(lv.water[0].positions[:, 1] == 0.0)
    # No sea triangle is ground: nothing below 0 m.
    assert min(p.positions[:, 1].min() for p in lv.ground) >= 0.0


def test_seabed_is_kept_on_request(surface):
    lv = build(surface, "Test", seabed=True, water=False)
    assert lv.classes["seabed"] == 8 and not lv.water
    seabed = next(p for p in lv.ground if p.label == "seabed")
    assert seabed.positions[:, 1].min() == -20.0


def test_region(surface):
    lv = build(surface, "Test", region=Region(1000, 2000, 1390, 2390))
    assert lv.tiles == 1  # the second tile starts at x = 1400
    assert lv.bounds()[1][0] <= 1400.0
    assert build(surface, "Test", region=Region(0, 0, 10, 10)).triangle_count == 0


def test_cluster_thins_and_keeps_the_shape(surface):
    full = build(surface, "Test")
    thin = build(surface, "Test", cell=250.0)
    assert 0 < thin.triangle_count < full.triangle_count
    lo, hi = thin.bounds()
    assert lo[0] >= 1000.0 and hi[0] <= 1800.0


def test_cluster_drops_collapsed_triangles():
    pos = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 1], [100, 0, 0], [100, 0, 100]], float)
    tri = np.array([[0, 1, 2], [0, 3, 4], [1, 3, 4]])
    p, t, keep = cluster(pos, tri, 10.0)
    assert len(p) == 3 and len(t) == 1 and keep.tolist() == [1]


def test_ground_height(surface):
    lv = build(surface, "Test")
    assert ground_height(lv, 1100.0, 2100.0) == pytest.approx(20.0)
    assert ground_height(lv, -50_000.0, 0.0) is None


def test_glb_contract(surface, tmp_path):
    lv = build(surface, "Test")
    path = tmp_path / "t.glb"
    size = glb.write(path, lv.parts())
    assert path.stat().st_size == size
    doc, blob = glb.read(path)
    assert [n["name"] for n in doc["nodes"]] == ["ground:Test", "water:Test"]
    ground = doc["meshes"][0]["primitives"]
    assert {p["extras"]["class"] for p in ground} == {"land", "road"}
    for prim in ground:
        pos = glb.accessor(doc, blob, prim["attributes"]["POSITION"])
        col = glb.accessor(doc, blob, prim["attributes"]["COLOR_0"])
        idx = glb.accessor(doc, blob, prim["indices"])
        assert pos.dtype == np.float32 and col.shape == pos.shape and idx.max() < len(pos)
        assert len(idx) % 3 == 0
    water = doc["meshes"][1]["primitives"][0]
    assert "COLOR_0" not in water["attributes"]


def test_matching_ignores_vertex_order():
    from heat3d_ext_dcs.level import matching

    base = np.array([[0, 1, 2], [2, 3, 4], [5, 6, 7], [1, 2, 3]])
    other = np.array([[4, 2, 3], [7, 6, 5], [0, 1, 9]])
    assert matching(base, other, 10).tolist() == [False, True, True, False]
    assert not matching(base, other[:0], 10).any()
