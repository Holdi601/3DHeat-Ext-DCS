"""The command line on a synthetic install."""

from __future__ import annotations

import json

import pytest

import synth
from heat3d_ext_dcs import cli, projection
from heat3d_ext_dcs.projection import Projection

TOWNS = """towns = {
["Inland"] = { latitude = 0.0108, longitude = 0.0181, display_name = _("Inland")},
["Far away"] = { latitude = 10.0, longitude = 10.0, display_name = _("Far away")},
}
"""


@pytest.fixture
def dcs(tmp_path, monkeypatch):
    root = synth.theatre(tmp_path / "DCS", towns=TOWNS)
    # The origin on the equator and the prime meridian: "Inland" is about 1195 m north, 2015 m east - in tile one.
    monkeypatch.setitem(projection.THEATRES, "TestTheatre", Projection(0, 0.0, 0.0))
    monkeypatch.setattr("heat3d_update.startup", lambda *a, **k: None)
    return root


def test_list(dcs, capsys):
    assert cli.main(["list", "--dcs", str(dcs)]) == 0
    out = capsys.readouterr().out
    assert "TestTheatre" in out and "readable" in out and "lat/lon" in out


def test_level(dcs, tmp_path, capsys):
    out = tmp_path / "out"
    assert cli.main(["level", "testtheatre", "--dcs", str(dcs), "-o", str(out)]) == 0
    meta = json.loads((out / "TestTheatre.json").read_text(encoding="utf-8"))
    assert (out / "TestTheatre.glb").stat().st_size == meta["glb_bytes"]
    assert meta["triangles"] == {"ground": 56, "water": 8}
    assert meta["classes"]["road"] == 8
    assert meta["projection"]["central_meridian"] == 0
    inland = next(t for t in meta["towns"] if t["name"] == "Inland")
    assert 1000 < inland["x"] < 1400 and 2000 < inland["z"] < 2400 and inland["ground"] > 0
    assert meta["towns_on_land"] == "1 of 2"
    assert "towns on land: 1 of 2" in capsys.readouterr().out


def test_level_region_and_name(dcs, tmp_path):
    out = tmp_path / "out"
    rc = cli.main(["level", "TestTheatre", "--dcs", str(dcs), "-o", str(out),
                   "--bounds", "1000", "2000", "1390", "2390", "--name", "Part"])
    assert rc == 0
    meta = json.loads((out / "Part.json").read_text(encoding="utf-8"))
    assert meta["tiles"] == 1 and meta["region"]["x"] == [1000, 1390]
    assert [t["name"] for t in meta["towns"]] == ["Inland"]  # towns outside the region are left out


def test_too_large_asks(dcs, tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "LARGE", 10)
    assert cli.main(["level", "TestTheatre", "--dcs", str(dcs), "-o", str(tmp_path / "o")]) == 1
    assert "--cell" in capsys.readouterr().err
    assert cli.main(["level", "TestTheatre", "--dcs", str(dcs), "-o", str(tmp_path / "o"), "--cell", "50"]) == 0


def test_missing(dcs, tmp_path, capsys):
    assert cli.main(["level", "Nowhere", "--dcs", str(dcs), "-o", str(tmp_path)]) == 2
    assert "TestTheatre" in capsys.readouterr().err
    assert cli.main(["list", "--dcs", str(tmp_path / "nothing")]) == 2


def test_towns(dcs, capsys):
    assert cli.main(["towns", "TestTheatre", "--dcs", str(dcs)]) == 0
    rows = json.loads(capsys.readouterr().out)
    assert rows[0]["name"] == "Inland" and "x" in rows[0]


def test_fit_and_projection_override(dcs, tmp_path, capsys):
    true = projection.Projection(45, 12345.6, -3500000.0)
    rec = tmp_path / "flight.csv"
    lines = ["lat,lon,x,z,alt"]
    for lat in (31.0, 32.5, 34.0):
        for lon in (43.0, 44.4, 46.1):
            x, z = true.to_dcs(lat, lon)
            lines.append(f"{lat},{lon},{x:.2f},{z:.2f},1000")
    rec.write_text("\n".join(lines) + "\nbroken,row\n", encoding="utf-8")
    assert cli.main(["fit", str(rec)]) == 0
    out = capsys.readouterr().out
    assert "--projection 45 12345.6" in out and "a good fit" in out
    o = tmp_path / "o"
    assert cli.main(["level", "TestTheatre", "--dcs", str(dcs), "-o", str(o), "--projection", "0", "0", "0"]) == 0
    meta = json.loads((o / "TestTheatre.json").read_text(encoding="utf-8"))
    assert meta["projection"]["constants_from"] == "given on the command line"
