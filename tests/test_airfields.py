import json
import struct

from heat3d_ext_dcs import airfields, cli

import synth


def rn4(points, junk=b"landscape4::lRoadNetwork\x05\x00\x00\x00vpp" + bytes(13)):
    """A taxi network's bytes: a header, a few integers, then the points as (x, y, z) doubles."""
    body = b"".join(struct.pack("<3d", *p) for p in points)
    return junk + struct.pack("<4i", 2, 3, 0, 11) + body + struct.pack("<3i", 7, 0, 1)


def test_points_and_centre(tmp_path):
    pts = [(1000.0 + i * 10, 50.0, 2000.0 + i * 100) for i in range(6)] + [(1200.0, 51.0, 2300.0)]
    f = tmp_path / "Some_Field.rn4"
    f.write_bytes(rn4(pts))
    a = airfields.read_one(f)
    assert a is not None and a.name == "Some Field" and a.points == 7
    assert a.box == (1000.0, 2000.0, 1200.0, 2500.0)
    assert (a.x, a.z) == (1100.0, 2250.0)


def test_outliers_and_short_runs_left_out(tmp_path):
    pts = [(1000.0, 50.0, 2000.0), (1010.0, 50.0, 2010.0), (1020.0, 50.0, 2020.0)]
    far = [(900000.0, 50.0, 900000.0)] * 3
    two = struct.pack("<3d", 5.0e5, 10.0, 5.0e5) * 2  # a run too short to be points
    f = tmp_path / "A.rn4"
    f.write_bytes(rn4(pts) + two + rn4(pts) + rn4(far, junk=b"x" * 8))
    a = airfields.read_one(f)
    assert a is not None and a.box == (1000.0, 2000.0, 1020.0, 2020.0)


def test_folder_prefers_rn4(tmp_path):
    (tmp_path / "B.rn5").write_bytes(rn4([(1.0e4, 0.0, 2.0e4)] * 3))
    (tmp_path / "B.rn4").write_bytes(rn4([(3.0e4, 0.0, 4.0e4)] * 3))
    (tmp_path / "notes.txt").write_text("x")
    assert [(a.name, a.x) for a in airfields.read(tmp_path)] == [("B", 3.0e4)]
    assert airfields.read(tmp_path / "missing") == []


def test_level_lists_airfields_in_region(tmp_path):
    root = synth.theatre(tmp_path / "DCS")
    folder = root / "Mods" / "terrains" / "TestTheatre" / "AirfieldsTaxiways"
    folder.mkdir()
    (folder / "Inside.rn4").write_bytes(rn4([(1100.0, 30.0, 2100.0), (1150.0, 30.0, 2150.0), (1200.0, 30.0, 2200.0)]))
    (folder / "Outside.rn4").write_bytes(rn4([(90000.0, 30.0, 90000.0)] * 3))
    out = tmp_path / "out"
    assert cli.main(["level", "TestTheatre", "--dcs", str(root), "-o", str(out), "--bounds", "1000", "2000", "1390", "2390"]) == 0
    meta = json.loads((out / "TestTheatre.json").read_text(encoding="utf-8"))
    assert [a["name"] for a in meta["airfields"]] == ["Inside"]
    a = meta["airfields"][0]
    assert a["x"] == 1150.0 and a["z"] == 2150.0 and a["ground"] is not None
