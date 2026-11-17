"""The Lua reader and the ranges catalogue, on synthetic Lua written here."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from heat3d_ext_dcs import cli, lua, ranges


def read(text: str) -> lua.Reader:
    r = lua.Reader()
    r.run(text)
    return r


def test_tables_and_arithmetic():
    r = read("""
        local k = 2
        T = { a = 1 + 2 * 3, b = -k ^ 2, c = "x" .. 1, d = math.rad(180), [k] = "two", "one",
              e = _("Shown"), f = { 10, 20; 30 }, g = 7 // 2, h = nil, ['q r'] = true }
        T.f[4] = 40
        T.a = T.a + 1  -- comments
        --[[ a long
             comment ]] T.long = [[text]]
    """)
    t = r.get("T")
    assert t.get("a") == 8 and t.get("b") == -4.0 and t.get("c") == "x1"
    assert t.get("d") == pytest.approx(math.pi) and t.get(2) == "two" and t.get(1) == "one"
    assert t.get("e") == "Shown" and t.get("f").array() == [10, 20, 30, 40]
    assert t.get("g") == 3 and t.get("h") is None and t.get("q r") is True and t.get("long") == "text"


def test_unknown_names_are_refs():
    r = read("W = { category = CAT_MISSILES, kind = ENGINE.thing.x, n = UNKNOWN + 1 }")
    w = r.get("W")
    assert w.get("category") == lua.Ref("CAT_MISSILES") and w.get("kind") == lua.Ref("ENGINE.thing.x")
    assert w.get("n") is None


def test_functions_loops_and_hooks():
    seen = []
    r = lua.Reader(hooks={"declare_weapon": lambda a: seen.append(a[0])})
    r.run("""
        local function make(name, range, ...)
            local t = { name = name, D_max = range }
            t.extra = ...
            declare_weapon(t)
            return t
        end
        for i, n in ipairs({ "A", "B" }) do make(n, i * 1000, "x") end
        for i = 1, 3 do LAST = i end
        local base = { fm = { mass = 5 } }
        local copy = deepcopy(base)
        copy.fm.mass = 6
        BASE, COPY = base.fm.mass, copy.fm.mass
        local function deepcopy(o) return o end
        function obj_method(self) return 1 end
    """)
    assert [(w.get("name"), w.get("D_max"), w.get("extra")) for w in seen] == [("A", 1000, "x"), ("B", 2000, "x")]
    assert r.get("LAST") == 3
    assert (r.get("BASE"), r.get("COPY")) == (5, 6)


def test_recursion_and_bad_syntax_do_not_stop_reading():
    r = read("""
        local function f(x) return f(x) + f(x) end
        A = f(1)
        B = { 1, 2,, }  )))  end end
        C = 3
    """)
    assert r.get("A") is None and r.get("C") == 3


def test_metatables_and_namespaces():
    r = read("""
        P = { distanceMax = 5000, PL = { { shell_name = { "S1" } } } }
        L = {}
        set_recursive_metatable(L, P)
        L.distanceMin = 10
        GT_t.LN_t.gun = { name = "G" }
    """)
    assert r.get("L").get("distanceMax") == 5000 and r.get("L").get("distanceMin") == 10
    assert r.get("L").get("PL").array()[0].get("shell_name").array() == ["S1"]
    assert r.get("GT_t") is None  # an unknown table takes no fields unless the caller makes it a Namespace
    ns = lua.Reader()
    ns.globals.vars["GT_t"] = lua.Namespace("GT_t")
    ns.run("GT_t.LN_t.gun = { name = 'G' } X = GT_t.LN_t.other")
    assert ns.get("GT_t").get("LN_t").get("gun").get("name") == "G" and ns.get("X").path == "GT_t.LN_t.other"


def test_dofile_stays_inside_root(tmp_path):
    (tmp_path / "root").mkdir()
    (tmp_path / "root" / "in.lua").write_text("INSIDE = 1", encoding="utf-8")
    (tmp_path / "out.lua").write_text("OUTSIDE = 1", encoding="utf-8")
    r = lua.Reader(tmp_path / "root")
    r.run(f'dofile("{(tmp_path / "root" / "in.lua").as_posix()}") dofile("{(tmp_path / "out.lua").as_posix()}")'
          ' dofile("../out.lua")')
    assert r.get("INSIDE") == 1 and r.get("OUTSIDE") is None


# -- a synthetic install ---------------------------------------------------------

WSTYPES = """
wsType_Weapon = 4
wsType_Missile = 4
wsType_Bomb = 5
wsType_Shell = 6
wsType_NURS = 7
wsType_AA_Missile = 7
wsType_AS_Missile = 8
wsType_SA_Missile = 34
wsType_SS_Missile = 11
TEST_AAM = 900
TEST_SAM = 901
"""

PACK_ENTRY = """
declare_plugin("Test Pack", { installed = true })
dofile(current_mod_path .. "/Database/sensors.lua")
dofile(current_mod_path .. "/Database/weapons.lua")
dofile(current_mod_path .. "/Database/units.lua")
"""

SENSORS = """
local SENSOR_RADAR = 1
declare_sensor({
    Name = "Test SR",
    category = SENSOR_RADAR,
    type = RADAR_AS,
    scan_volume = { azimuth = {-180, 180}, elevation = {-5, 70} },
    max_measuring_distance = 60000,
    detection_distance = {
        [HEMISPHERE_UPPER] = { [ASPECT_HEAD_ON] = 50000, [ASPECT_TAIL_ON] = 45000 },
        [HEMISPHERE_LOWER] = { [ASPECT_HEAD_ON] = 40000, [ASPECT_TAIL_ON] = 35000 },
    },
    lock_on_distance_coeff = 0.85,
    RBM_detection_distance = 30000,
})
declare_sensor({
    Name = "Test Pod FLIR",
    category = SENSOR_OPTICAL,
    type = OPTIC_SENSOR_IR,
    scan_volume = { azimuth = {-150, 150}, elevation = {-150, 45} },
    view_volume_max = { azimuth_sector = 4.0, elevation_sector = 3.0 },
    magnifications = {2, 8},
})
"""

WEAPONS = """
local sam = {
    category = CAT_MISSILES,
    wsTypeOfWeapon = {wsType_Weapon, wsType_Missile, wsType_SA_Missile, TEST_SAM},
    name = "TEST_SAM",
    display_name = _("Test SAM"),
    Head_Type = 6,
    H_max = 12000.0, H_min = 25.0,
    D_max = 20000.0, D_min = 2500.0, Range_max = 30000.0,
    Nr_max = 20, Mach_max = 3.0,
    Fi_start = 3.14152, Fi_search = 99.9,
}
declare_weapon(sam)

GT_t.LN_t.test_gun = { name = "Test Gun", type = 3, distanceMin = 10, distanceMax = 3000, max_trg_alt = 2000 }
GT_t.LN_t.test_gun.PL = { { shell_name = { "TEST_20_HE" }, shell_display_name = "20mm HE" } }
declare_weapon({ category = CAT_SHELLS, name = "TEST_20_HE", user_name = _("20mm HE"), v0 = 1050.0 })
declare_weapon({ category = CAT_BOMBS, name = "TEST_BOMB", user_name = _("Test bomb") })
"""

UNITS = """
local function vehicle(f) dofile(current_mod_path .. "/Database/" .. f) add_surface_unit(GT) GT = nil end
vehicle("vehicles/test_sam.lua")
"""

VEHICLE = """
GT = {};
set_recursive_metatable(GT, GT_t.generic_stationary);
GT.WS = {};
GT.WS.maxTargetDetectionRange = 40000;
local ws = GT_t.inc_ws();
GT.WS[ws] = {};
GT.WS[ws].angles = { {math.rad(180), math.rad(-180), math.rad(-10), math.rad(80)} };
__LN = add_launcher(GT.WS[ws], GT_t.LN_t.unknown_launcher);
__LN.PL[1].type_ammunition = {4, 4, 34, 901};
ws = GT_t.inc_ws();
GT.WS[ws] = {};
GT.WS[ws].angles = { {math.rad(180), math.rad(-180), math.rad(-5), math.rad(85)} };
add_launcher(GT.WS[ws], GT_t.LN_t.test_gun);
GT.Sensors = { RADAR = "Test SR", OPTIC = { "Core Sight day" } };
GT.Name = "TEST_SAM_LN";
GT.DisplayName = _("SAM Test launcher");
"""

JET_ENTRY = """
declare_plugin("Test Jet", {})
local aam = {
    category = CAT_AIR_TO_AIR,
    name = "TEST_AAM",
    user_name = _("TAAM-1"),
    displayName = _("TAAM-1 - Active Radar AAM"),
    wsTypeOfWeapon = {wsType_Weapon, wsType_Missile, wsType_AA_Missile, WSTYPE_PLACEHOLDER},
    Head_Type = 2, D_max = 15000, D_min = 700, Range_max = 50000, H_max = 20000, H_min = 1,
    Fi_start = 0.5, Fi_search = 1.05, Nr_max = 30,
}
declare_weapon(aam)
declare_loadout({ category = CAT_AIR_TO_AIR, CLSID = "{TEST-AAM}", attribute = aam.wsTypeOfWeapon,
                  displayName = _("TAAM-1") })
declare_loadout({ category = CAT_AIR_TO_AIR, CLSID = "{TEST-AAM-RACK}",
                  Elements = { { payload_CLSID = "{TEST-AAM}" } } })
add_aircraft({
    Name = "TestJet_A",
    DisplayName = _("Test Jet A"),
    Sensors = { RADAR = "Core Radar", RWR = "Abstract RWR", OPTIC = { "Test Pod FLIR" } },
    Pylons = {
        pylon(1, 0, 0, 0, 0, {}, { { CLSID = "{TEST-AAM}" }, { CLSID = "{CORE-ONLY}" } }),
        pylon(2, 0, 0, 0, 0, {}, { { CLSID = "{TEST-AAM-RACK}" } }),
    },
})
"""


def _write(root: Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


@pytest.fixture
def install(tmp_path, monkeypatch):
    root = tmp_path / "DCS"
    (root / "Mods" / "terrains").mkdir(parents=True)
    _write(root, "Scripts/Database/wsTypes.lua", WSTYPES)
    _write(root, "CoreMods/tech/TestPack/entry.lua", PACK_ENTRY)
    _write(root, "CoreMods/tech/TestPack/Database/sensors.lua", SENSORS)
    _write(root, "CoreMods/tech/TestPack/Database/weapons.lua", WEAPONS)
    _write(root, "CoreMods/tech/TestPack/Database/units.lua", UNITS)
    _write(root, "CoreMods/tech/TestPack/Database/vehicles/test_sam.lua", VEHICLE)
    _write(root, "CoreMods/aircraft/TestJet/entry.lua", JET_ENTRY)
    monkeypatch.setattr("heat3d_ext_dcs.update.startup", lambda *a, **k: None)
    return root


def test_catalogue(install):
    cat, summary = ranges.build(install)
    assert (cat["version"], cat["game"], cat["source"]) == (1, "dcs", "your installation")
    w = {x["id"]: x for x in cat["weapons"]}
    sam = w["local-dcs-test-sam"]
    assert sam["cls"] == "sam" and sam["shape"] == "sphere" and sam["range"] == [2500, 20000, 30000]
    assert sam["alt"] == [25, 12000] and "cone" not in sam and sam["detail"]["seeker"] == "SARH"
    assert "Test SAM" in sam["labels"] and sam["detail"]["gLimit"] == 20
    aam = w["local-dcs-test-aam"]
    assert aam["cls"] == "aam" and aam["shape"] == "cone" and aam["cone"] == pytest.approx(28.6)
    assert aam["range"] == [700, 15000, 50000] and "alt" not in aam
    assert {"TEST_AAM", "TAAM-1", "TAAM-1 - Active Radar AAM"} <= set(aam["labels"])
    assert aam["detail"]["seeker"] == "ARH" and aam["detail"]["seekerFovHalf"] == pytest.approx(60.2)
    gun = next(x for x in cat["weapons"] if x["name"] == "Test Gun")
    assert gun["cls"] == "cannon" and gun["range"] == [10, 3000, 3000] and gun["alt"] == [0, 2000]
    assert gun["elev"] == [-5, 85] and gun["detail"]["muzzleVelocity"] == 1050 and "TEST_20_HE" in gun["labels"]
    assert not any(x["name"] == "Test bomb" for x in cat["weapons"])  # no stated range: left out
    assert summary["skipped"]["weapons_without_range"] == 1

    s = {x["name"]: x for x in cat["sensors"].values()}
    sr = s["Test SR"]
    assert sr["kind"] == "radar" and sr["range"] == 50000 and sr["az"] == [-180, 180] and sr["el"] == [-5, 70]
    assert sr["modes"] == ["search", "stt", "gm"] and sr["detail"]["detection"]["lower/tail_on"] == 35000
    assert s["Test Pod FLIR"]["kind"] == "tgp"
    assert s["Core Radar"]["kind"] == "radar" and "range" not in s["Core Radar"]
    assert s["Core Radar"]["detail"]["declared"] is False and s["Abstract RWR"]["kind"] == "rwr"

    u = {x["names"][0]: x for x in cat["units"]}
    ln = u["TEST_SAM_LN"]
    assert ln["names"] == ["TEST_SAM_LN", "SAM Test launcher"]
    assert ln["weapons"] == ["local-dcs-test-sam", gun["id"]]
    assert [cat["sensors"][k]["name"] for k in ln["sensors"]] == ["Test SR", "Core Sight day"]
    jet = u["TestJet_A"]
    assert jet["weapons"] == ["local-dcs-test-aam"]
    assert jet["optics"] == [{"who": "tgp", "fov": [4, 1], "thermal": {"gen": None}, "nv": False, "mount": "hull"}]


def test_cli_ranges(install, tmp_path, capsys):
    out = tmp_path / "out" / "ranges.json"
    assert cli.main(["ranges", "--dcs", str(install), "--no-saved-games", "-o", str(out)]) == 0
    text = out.read_text(encoding="utf-8")
    assert "\n" not in text
    cat = json.loads(text)
    assert len(cat["weapons"]) == 3 and len(cat["units"]) == 2
    assert "3 weapons" in capsys.readouterr().out


def test_cli_ranges_without_install(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr("heat3d_ext_dcs.update.startup", lambda *a, **k: None)
    assert cli.main(["ranges", "--dcs", str(tmp_path), "-o", str(tmp_path / "r.json")]) == 2
