"""The .surface5 reader on files built to the real layout."""

from __future__ import annotations

import struct

import numpy as np
import pytest

import synth
from heat3d_ext_dcs.surface5 import FormatError, Surface5, parse_record


@pytest.fixture
def surface(tmp_path):
    root = synth.theatre(tmp_path)
    with Surface5(root / "Mods/terrains/TestTheatre/surface/TestTheatre.surface5") as s:
        yield s


def test_tiles_and_sets(surface):
    assert len(surface.tiles) == 3
    ground = surface.ground_tiles
    assert [t.index for t in ground] == [0, 1]  # the second-set copy carries no TRITYPE
    assert ground[0].translation == (1000.0, 0.0, 2000.0)
    assert ground[0].vertex_count == 25
    assert [(g.shader, g.material) for g in ground[0].groups] == [("Surface5.0", "Land"), ("Splatmap5.1", "Road")]


def test_positions_are_world_metres(surface):
    t = surface.ground_tiles[0]
    p = surface.positions(t)
    assert p[:, 0].min() == 1000.0 and p[:, 0].max() == 1400.0
    assert p[:, 2].min() == 2000.0 and p[:, 2].max() == 2400.0
    assert np.allclose(p[:, 1], 10.0 + (p[:, 0] - 1000.0) * 0.1)
    wb = t.world_bounds()
    assert wb[0] == 1000.0 and wb[5] == 2400.0


def test_ground_and_types(surface):
    tri, kinds = surface.ground(surface.ground_tiles[1])
    assert tri.shape == (32, 3) and tri.max() == 24
    assert set(kinds.tolist()) == {1, 1024}
    assert (kinds == 1).sum() == 8  # the first row of cells is sea


def test_overlay_maps_through_base_index(surface):
    t = surface.ground_tiles[0]
    road = next(g for g in t.groups if g.material == "Road")
    tri = surface.overlay(t, road)
    assert tri.shape == (8, 3)
    # Overlay vertex 2i is tile vertex 5i (z = 0), 2i + 1 is 5i + 1 (z = 100).
    assert set(np.unique(tri).tolist()) == {i * 5 + j for i in range(5) for j in range(2)}


def test_ground_group_is_not_an_overlay(surface):
    t = surface.ground_tiles[0]
    assert surface.overlay(t, t.ground) is None  # no baseIndex: it indexes the tile directly


def test_not_a_surface(tmp_path):
    p = synth.write(tmp_path / "x.surface5", [], type_name=b"landscape5::Scene5File")
    with pytest.raises(FormatError, match="Scene5File"):
        Surface5(p)
    (tmp_path / "y.surface5").write_bytes(b"\x01\0\0\0" + b"\0" * 100)
    with pytest.raises(FormatError):
        Surface5(tmp_path / "y.surface5")


def test_unknown_layout_is_reported_not_skipped(tmp_path):
    pos, tri = synth.grid(3, 10.0)
    spec = synth.TileSpec((0.0, 0.0, 0.0), pos, tri, np.zeros(len(tri)))
    p = synth.write(tmp_path / "z.surface5", [spec])
    data = bytearray(p.read_bytes())
    # Rotate the tile: its transform no longer has an identity rotation.
    at = data.find(struct.pack("<I", 7) + struct.pack("<f", 1.0))
    struct.pack_into("<f", data, at + 4, 0.0)
    p.write_bytes(bytes(data))
    with Surface5(p) as s, pytest.raises(FormatError, match="layout"):
        s.tiles


def test_offsets_are_48_bit():
    # A vertex stream 5 GiB into the data: the high u16 carries bit 32 and up.
    seg = struct.pack("<I", 7) + struct.pack("<16f", 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    seg += struct.pack("<6f", 0, 0, 0, 1, 1, 1)
    seg += struct.pack("<IIII", 0, 2, 1, 1) + synth._entry("Pbase", 2, 12, 0, (5 << 30, 12))
    t = parse_record(seg, 0)
    assert t.vertices.offset == 5 << 30 and t.vertices.count == 12


def test_stream_past_the_end(surface):
    t = surface.ground_tiles[0]
    t.vertices.offset = surface.size
    with pytest.raises(FormatError, match="past the end"):
        surface.positions(t)
