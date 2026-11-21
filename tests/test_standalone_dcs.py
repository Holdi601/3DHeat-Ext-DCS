"""The standalone app on a synthetic DCS install: theatres as maps, a new terrain found as new."""

from __future__ import annotations

import json

import pytest

import synth
from heat3d_ext_dcs import install
from heat3d_ext_dcs.app import entry, paths
from heat3d_ext_dcs.standalone_spec import SPEC


@pytest.fixture
def dcs(tmp_path, monkeypatch):
    root = synth.theatre(tmp_path / "DCS", name="Alpha")
    (root / "autoupdate.cfg").write_text('{\n  "branch": "release",\n  "version": "2.9.0.1"\n}\n', encoding="utf-8")
    monkeypatch.setenv("DCS_PATH", str(root))
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")
    monkeypatch.setattr("heat3d_ext_dcs.update.startup", lambda *a, **k: None)
    return root


def status(capsys) -> dict:
    assert entry.main(SPEC, ["status", "--json"]) == 0
    return json.loads(capsys.readouterr().out)["games"][0]


def test_find_and_maps(dcs):
    g = SPEC.games[0]
    assert g.find(None) == dcs
    maps = g.maps(dcs)
    assert [m.id for m in maps] == ["Alpha"]
    assert maps[0].sources[0].name == "Alpha.surface5"
    assert g.build(dcs) == "2.9.0.1"


def test_steam_library_found(tmp_path, monkeypatch):
    monkeypatch.delenv("DCS_PATH", raising=False)
    lib = tmp_path / "Steam"
    (lib / "steamapps").mkdir(parents=True)
    game = synth.theatre(lib / "steamapps" / "common" / "DCSWorld")
    monkeypatch.setattr(install, "_registry", lambda: [])
    monkeypatch.setattr(paths, "steam_roots", lambda: [lib])
    assert install.find() == game


def test_install_that_gains_a_theatre(dcs, tmp_path, capsys):
    g = status(capsys)
    assert g["found"] and g["build"] == "2.9.0.1" and g["counts"]["new"] == 1

    assert entry.main(SPEC, ["extract", "--new", "--progress-json"]) == 0
    events = [json.loads(l) for l in capsys.readouterr().out.splitlines() if l.startswith("{")]
    assert events[-1] == {"event": "done", "ok": 1, "failed": 0}
    out = tmp_path / "levels" / "dcs"
    assert (out / "Alpha.glb").is_file() and (out / "Alpha.json").is_file()
    man = json.loads((out / ".heat3d-extract.json").read_text(encoding="utf-8"))
    assert "dcs/Alpha.glb" in man["entries"]["Alpha"]["outputs"]

    # A new terrain module: the new theatre is new, the extracted one stays current.
    synth.theatre(dcs, name="Bravo")
    states = {m["id"]: m["state"] for m in status(capsys)["maps"]}
    assert states == {"Alpha": "current", "Bravo": "new"}
