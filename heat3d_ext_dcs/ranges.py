"""
A catalogue of weapon and sensor ranges from your own DCS World install, for
3DHeat's match replay (engagement ranges, view cones, sensor sectors).

What is read: the plain Lua definitions of the modules and asset packs
(`CoreMods/*/*`, `Mods/*/*`, and the mods in Saved Games), starting from each
one's `entry.lua` the way the game does, through the tolerant reader in
`lua.py`. The core database the game keeps packed (`Scripts/Database.edce`)
is not read, so weapons and sensors defined only there show up by name, if a
unit names them, without their numbers.

Nothing is invented: a value the files do not state is left out.
"""

from __future__ import annotations

import math
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from .lua import LuaTable, Namespace, Reader, Ref, deepcopy, number

#: A seeker's `Head_Type` in a weapon's table.
HEAD_TYPES = {1: "IR", 2: "ARH", 3: "anti-radiation", 4: "laser", 5: "autonomous (INS/GPS/TV/IIR)", 6: "SARH",
              7: "command"}

#: Sensors kinds by the key a unit names them under (`Sensors = { RADAR = ..., OPTIC = ... }`).
SENSOR_KEYS = {"RADAR": "radar", "IRST": "irst", "OPTIC": "camera", "RWR": "rwr", "TGP": "tgp", "LASER": "ldp",
               "MAWS": "mlws", "MLWS": "mlws", "LWS": "lws", "SONAR": "sonar", "ESM": "esm"}

#: A launcher's `type` on a ground unit or ship.
LN_TYPES = {2: "heavy gun", 3: "AA autocannon", 9: "machine gun", 10: "AA machine gun", 11: "heavy AA gun",
            12: "AG autocannon"}

_POD = re.compile(r"pod|sniper|litening|atflir|lantirn|damocles|pave|tram|tgp|tads|wmd7|aaq-", re.I)
_ATGM = re.compile(r"atgm|ataka|vikhr|hot ?\d|tow|hellfire|agm.?114|spike|kornet|konkurs|fagot|shturm|malyutka|milan|"
                   r"9m1\d\d|9m11\d|9m3\d|9m4\d|bgm.?71", re.I)

_DECLS = ("declare_weapon", "declare_sensor", "declare_loadout", "add_aircraft", "add_surface_unit")
_SKIP_DIRS = {"Cockpit", "Cockpits", "UI", "Input", "Options", "Missions", "DTC", "Liveries", "Shapes", "Textures",
              "Sounds", "Skins", "l10n", "Doc", "ImagesGUI", "Encyclopedia", "Kneeboard", "Datalinks", "bin"}


def saved_games() -> list[Path]:
    """Saved Games folders of DCS (the release and the old open beta), where installed mods live."""
    home = Path(os.environ.get("USERPROFILE") or Path.home())
    return [p for p in (home / "Saved Games" / "DCS", home / "Saved Games" / "DCS.openbeta") if (p / "Mods").is_dir()]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "x"


def _s(v) -> str | None:
    return v.strip() if isinstance(v, str) and v.strip() else None


def _n(v) -> float | None:
    x = number(v)
    if x is None or isinstance(x, bool) or not math.isfinite(x):
        return None
    return x


def _r(x: float | None, nd: int = 0):
    if x is None:
        return None
    v = round(float(x), nd)
    return int(v) if nd == 0 or v.is_integer() else v


def _ref(v) -> str | None:
    return v.path if isinstance(v, Ref) else None


class Collector:
    def __init__(self):
        self.weapons: list[LuaTable] = []
        self.sensors: list[tuple[LuaTable, str]] = []
        self.loadouts: list[LuaTable] = []
        self.aircraft: list[tuple[LuaTable, str]] = []
        self.surface: list[tuple[LuaTable, str]] = []
        self.file = ""
        self.mod = ""

    def hooks(self) -> dict:
        def keep(store, with_file=False):
            def hook(args):
                if args and isinstance(args[0], LuaTable):
                    store.append((args[0], self.file) if with_file else args[0])
                return None
            return hook

        return {"declare_weapon": keep(self.weapons), "declare_sensor": keep(self.sensors, True),
                "declare_loadout": keep(self.loadouts), "add_aircraft": keep(self.aircraft, True),
                "add_surface_unit": keep(self.surface, True)}


#: Names the game's engine defines before any database file runs. They are kept as names (a file that
#: sets them to numbers again does not change them), so a sensor's kind reads the same in every file.
ENGINE_NAMES = ("SENSOR_OPTICAL", "SENSOR_RADAR", "SENSOR_IRST", "SENSOR_RWR", "RADAR_AS", "RADAR_SS",
                "RADAR_MULTIROLE", "ASPECT_HEAD_ON", "ASPECT_TAIL_ON", "HEMISPHERE_UPPER", "HEMISPHERE_LOWER",
                "OPTIC_SENSOR_TV", "OPTIC_SENSOR_LLTV", "OPTIC_SENSOR_IR")


def _engine_hooks(reader: Reader) -> dict:
    """Stand-ins for the few engine helpers unit files build their weapons with."""

    def inc_ws(args):  # GT_t.inc_ws(): the next weapon-system slot of the unit being defined
        gt = reader.globals.vars.get("GT")
        ws = gt.get("WS") if isinstance(gt, LuaTable) and not isinstance(gt, Namespace) else None
        return len(ws.array()) + 1 if isinstance(ws, LuaTable) else 1

    def add_launcher(args):  # add_launcher(GT.WS[i], GT_t.LN_t.<proto>): a copy of the launcher, on the slot
        if not args or not isinstance(args[0], LuaTable):
            return None
        proto = args[1] if len(args) > 1 else None
        if isinstance(proto, Namespace):
            ln = Namespace(proto.path)
        elif isinstance(proto, LuaTable):
            ln = deepcopy(proto)
        else:
            ln = Namespace(proto.path if isinstance(proto, Ref) else "launcher")
        lns = args[0].h.get("LN")
        if not isinstance(lns, LuaTable):
            lns = LuaTable()
            args[0].set("LN", lns)
        lns.set(len(lns.array()) + 1, ln)
        return ln

    def pylon(args):  # pylon(number, type, x, y, z, params, launchers)
        t = LuaTable()
        for a in reversed(args):
            if isinstance(a, LuaTable) and any(isinstance(x, LuaTable) and x.get("CLSID") for x in a.array()):
                t.set("Launchers", a)
                break
        if args:
            t.set("Number", args[0])
        return t

    return {"inc_ws": inc_ws, "add_launcher": add_launcher, "pylon": pylon}


def _mods(dcs: Path, extra: list[Path]) -> list[Path]:
    out = []
    for base in [dcs / "CoreMods", dcs / "Mods"] + [p / "Mods" for p in extra]:
        if not base.is_dir():
            continue
        for e in sorted(base.glob("*/entry.lua")) + sorted(base.glob("*/*/entry.lua")):
            out.append(e.parent)
    # asset packs (tech) first: their launchers and sensors are what units and aircraft refer to
    out.sort(key=lambda p: (0 if p.parent.name == "tech" else 1))
    return out


def _declaring_files(mod: Path) -> list[Path]:
    out = []
    for root, dirs, files in os.walk(mod):
        dirs[:] = sorted(d for d in dirs if d not in _SKIP_DIRS)
        for f in sorted(files):
            if f.lower().endswith(".lua"):
                p = Path(root) / f
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if any(d + "(" in text or d + " (" in text for d in _DECLS):
                    out.append(p)
    return out


def read_install(dcs: Path, extra: list[Path] | None = None, progress=None) -> tuple[Collector, Reader]:
    """Read every module and pack under the install (and `extra` Saved Games folders); the declarations found."""
    col = Collector()
    roots = [dcs] + list(extra or [])
    reader = Reader(dcs, col.hooks())
    reader.hooks.update(_engine_hooks(reader))
    for n in ENGINE_NAMES:
        reader.globals.vars[n] = Ref(n)
    reader.globals.vars["GT_t"] = Namespace("GT_t")
    reader.frozen.update(ENGINE_NAMES + ("GT_t",))
    reader.roots = [Path(p).resolve() for p in roots]  # dofile may read inside any of these
    ws = dcs / "Scripts" / "Database" / "wsTypes.lua"
    if ws.is_file():
        reader.run_file(ws)
    mods = _mods(dcs, list(extra or []))
    for i, mod in enumerate(mods):
        reader.globals.vars["current_mod_path"] = mod.as_posix()
        reader.globals.vars["__DCS_VERSION__"] = None
        col.mod = mod.name
        col.file = str(mod / "entry.lua")
        reader.root = _root_of(mod, reader.roots)
        reader.run_file(mod / "entry.lua", once=True)
        if progress:
            progress(i + 1, len(mods), mod)
    # files that declare something but that no entry.lua reached
    for mod in mods:
        reader.globals.vars["current_mod_path"] = mod.as_posix()
        reader.root = _root_of(mod, reader.roots)
        for f in _declaring_files(mod):
            col.file = str(f)
            reader.run_file(f, once=True)
    return col, reader


def _root_of(mod: Path, roots: list[Path]) -> Path:
    m = mod.resolve()
    for r in roots:
        if r == m or r in m.parents:
            return r
    return m


# -- weapons -----------------------------------------------------------------


def _wstype(t: LuaTable | None) -> list:
    return t.array() if isinstance(t, LuaTable) else []


def _names(w: LuaTable) -> list[str]:
    out = []
    for k in ("name", "user_name", "display_name", "displayName", "display_name_short", "Name", "short_name"):
        v = _s(w.get(k))
        if v and v not in out:
            out.append(v)
    std = w.get("shape_table_data")
    if isinstance(std, LuaTable):
        for row in std.array():
            if isinstance(row, LuaTable):
                for k in ("name", "username"):
                    v = _s(row.get(k))
                    if v and v not in out:
                        out.append(v)
    for v in list(out):  # "<name> - <what it is>": its first part is a name too
        head = v.split(" - ")[0].strip()
        if head and head not in out:
            out.append(head)
    return out


def _weapon_class(w: LuaTable, g: dict) -> tuple[str | None, str]:
    """(cls, shape) for a declared weapon, or (None, '') for what is not a weapon (pods, tanks, shells)."""
    cat = _ref(w.get("category")) or ""
    wt = _wstype(w.get("wsTypeOfWeapon"))
    lvl2 = wt[1] if len(wt) > 1 else None
    lvl3 = wt[2] if len(wt) > 2 else None
    if cat == "CAT_SHELLS" or lvl2 == g.get("wsType_Shell"):
        return None, ""
    if cat == "CAT_AIR_TO_AIR" or (lvl2 == g.get("wsType_Missile") and lvl3 == g.get("wsType_AA_Missile")):
        return "aam", "cone"
    if cat == "CAT_TORPEDOES" or lvl2 == g.get("wsType_Torpedo"):
        return "torpedo", "sphere"
    if cat == "CAT_BOMBS" or lvl2 == g.get("wsType_Bomb"):
        return "strike", "drop"
    if cat == "CAT_ROCKETS" or lvl2 == g.get("wsType_NURS"):
        return "strike", "cone"
    if cat == "CAT_MISSILES" or lvl2 == g.get("wsType_Missile"):
        if lvl3 == g.get("wsType_SA_Missile"):
            return "sam", "sphere"
        return "strike", "cone"
    return None, ""


def _weapon(w: LuaTable, g: dict) -> dict | None:
    cls, shape = _weapon_class(w, g)
    if cls is None:
        return None
    names = _names(w)
    if not names:
        return None
    dmin, dmax, rmax = _n(w.get("D_min")), _n(w.get("D_max")), _n(w.get("Range_max"))
    rng = [x for x in (dmax, rmax) if x is not None and x > 0]
    if not rng:
        return None  # no stated range: nothing to draw
    hi = max(rng)
    lo = dmin if dmin is not None and dmin < hi else 0
    best = dmax if dmax is not None and rmax is not None and lo < dmax < rmax else (lo + hi) / 2
    head = _n(w.get("Head_Type"))
    seeker = HEAD_TYPES.get(int(head)) if head is not None else None
    lvl3 = (_wstype(w.get("wsTypeOfWeapon")) + [None] * 3)[2]
    los = True
    if cls == "strike" and lvl3 == g.get("wsType_SS_Missile"):
        los = False  # surface-to-surface missiles fly to a point beyond sight
    if cls == "strike" and shape == "cone" and hi <= 10000 and (head in (4, 7) or any(_ATGM.search(n) for n in names)):
        cls = "atgm"
    out = {"cls": cls, "name": _display(w, names), "range": [_r(lo), _r(best), _r(hi)], "shape": shape,
           "los": los, "labels": names}
    fi_start = _n(w.get("Fi_start"))
    if fi_start is not None and fi_start < 3.1:
        out["cone"] = _r(math.degrees(fi_start), 1)
    elif fi_start is not None and shape == "cone":
        out["shape"] = "sphere"  # launched at any bearing
    hmin, hmax = _n(w.get("H_min")), _n(w.get("H_max"))
    if cls == "sam" and hmax is not None:
        out["alt"] = [_r(hmin or 0), _r(hmax)]  # from the ground: target height is height above the launcher
    detail = {}
    for key, name, nd in (("Nr_max", "gLimit", 1), ("Mach_max", "machMax", 2), ("H_min", "targetAltMin", 0),
                          ("H_max", "targetAltMax", 0), ("D_min", "dMin", 0), ("D_max", "dMax", 0),
                          ("Range_max", "rangeMax", 0), ("v_mid", "speedMid", 0), ("Life_Time", "lifeTime", 1),
                          ("KillDistance", "killDistance", 1), ("SeekerGen", "seekerGen", 0)):
        v = _n(w.get(key))
        if v is not None:
            detail[name] = _r(v, nd)
    for key, name in (("Fi_search", "seekerFovHalf"), ("Fi_start", "launchOffBoresight"), ("Fi_rak", "gimbal"),
                      ("OmViz_max", "trackRateMax")):
        v = _n(w.get(key))
        if v is not None and v < 3.1:  # 3.14 and 99.9 stand for "any direction"
            detail[name] = _r(math.degrees(v), 1)
    if seeker:
        detail["seeker"] = seeker
    elif head is not None:
        detail["headType"] = _r(head)
    for key, name in (("loft", "loft"), ("hoj", "homeOnJam")):
        v = _n(w.get(key))
        if v is not None:
            detail[name] = bool(v)
    out["detail"] = detail
    return out


def _display(w: LuaTable, names: list[str]) -> str:
    for k in ("user_name", "display_name", "displayName", "name"):
        v = _s(w.get(k))
        if v:
            return v
    return names[0]


# -- sensors -----------------------------------------------------------------


def _pair(t, scale=1.0) -> list | None:
    if isinstance(t, LuaTable):
        a = [_n(x) for x in t.array()[:2]]
        if len(a) == 2 and None not in a:
            return [_r(a[0] * scale, 1), _r(a[1] * scale, 1)]
    return None


#: The engine's sensor enumerations, as the files that restate them give their numbers.
_SENSOR_CATS = {0: "SENSOR_OPTICAL", 1: "SENSOR_RADAR", 2: "SENSOR_IRST", 3: "SENSOR_RWR"}
_RADAR_TYPES = {0: "RADAR_AS", 1: "RADAR_SS", 2: "RADAR_MULTIROLE"}
_OPTIC_TYPES = {0: "OPTIC_SENSOR_TV", 1: "OPTIC_SENSOR_LLTV", 2: "OPTIC_SENSOR_IR"}
_HEMI = {0: "HEMISPHERE_UPPER", 1: "HEMISPHERE_LOWER"}
_ASPECT = {0: "ASPECT_HEAD_ON", 1: "ASPECT_TAIL_ON"}


def _enum(v, table: dict) -> str:
    if isinstance(v, Ref):
        return v.path
    if isinstance(v, str):
        return v
    n = _n(v)
    return table.get(int(n), str(int(n))) if n is not None else ""


def _sensor(s: LuaTable, file: str) -> tuple[str, dict] | None:
    name = _s(s.get("Name"))
    if not name:
        return None
    cat = _enum(s.get("category"), _SENSOR_CATS)
    typ = _enum(s.get("type"), _RADAR_TYPES if cat == "SENSOR_RADAR" else _OPTIC_TYPES)
    out: dict = {"name": name}
    detail: dict = {}
    if typ:
        detail["type"] = typ
    vol = s.get("scan_volume")
    if isinstance(vol, LuaTable):
        az, el = _pair(vol.get("azimuth")), _pair(vol.get("elevation"))
        if az:
            out["az"] = sorted(az)
        if el:
            out["el"] = sorted(el)
    if cat == "SENSOR_RADAR":
        out["kind"] = "radar"
        dd = s.get("detection_distance")
        ranges = {}
        if isinstance(dd, LuaTable):
            for hemi in dd.keys():
                row = dd.get(hemi)
                if isinstance(row, LuaTable):
                    for aspect in row.keys():
                        v = _n(row.get(aspect))
                        if v is not None:
                            ranges[f"{_enum(hemi, _HEMI).replace('HEMISPHERE_', '').lower()}/"
                                   f"{_enum(aspect, _ASPECT).replace('ASPECT_', '').lower()}"] = _r(v)
        if ranges:
            detail["detection"] = ranges
            best = ranges.get("upper/head_on") or max(ranges.values())
            out["range"] = best
        mmd = _n(s.get("max_measuring_distance"))
        if mmd is not None:
            detail["maxMeasuringDistance"] = _r(mmd)
            out.setdefault("range", _r(mmd))
        rcs = _n(s.get("RCS"))
        out["rcsRef"] = _r(rcs, 2) if rcs is not None else None
        modes = ["search"]
        if _n(s.get("lock_on_distance_coeff")) is not None:
            modes.append("stt")
            detail["lockOnDistanceCoeff"] = _r(_n(s.get("lock_on_distance_coeff")), 2)
        rbm = _n(s.get("RBM_detection_distance"))
        if rbm is not None:
            modes.append("gm")
            detail["groundMapRange"] = _r(rbm)
        if s.get("vehicles_detection") is True:
            modes.append("gmti")
        out["modes"] = modes
        for key, nm in (("scan_period", "scanPeriod"), ("TWS_max_targets", "twsMaxTargets")):
            v = _n(s.get(key))
            if v is not None:
                detail[nm] = _r(v, 2)
        if s.get("airborne_radar") is not None:
            detail["airborne"] = bool(s.get("airborne_radar"))
    elif cat == "SENSOR_OPTICAL":
        out["kind"] = "tgp" if (_POD.search(name) or "targeting_pods" in file) else "camera"
        view = s.get("view_volume_max")
        if isinstance(view, LuaTable):
            a, e = _n(view.get("azimuth_sector")), _n(view.get("elevation_sector"))
            if a is not None:
                detail["viewAzimuth"] = _r(a, 2)
            if e is not None:
                detail["viewElevation"] = _r(e, 2)
        mags = s.get("magnifications")
        if isinstance(mags, LuaTable):
            m = [x for x in (_n(v) for v in mags.array()) if x is not None]
            if m:
                detail["magnifications"] = [_r(x, 2) for x in m]
        if s.get("laserRanger") is True:
            detail["laserRanger"] = True
        res = _n(s.get("resolution"))
        if res is not None:
            detail["resolution"] = _r(res, 3)
    elif cat == "SENSOR_IRST":
        out["kind"] = "irst"
    elif cat == "SENSOR_RWR":
        out["kind"] = "rwr"
    else:
        out["kind"] = "camera" if "OPTIC" in typ else "radar" if "RADAR" in typ else "esm"
    out["mount"] = "hull"
    out["detail"] = detail
    return name, out


def _optic(sensor: dict, who: str, mount: str) -> dict | None:
    d = sensor.get("detail", {})
    wide = d.get("viewAzimuth")
    if wide is None or sensor.get("kind") not in ("camera", "tgp"):
        return None
    mags = d.get("magnifications") or []
    narrow = wide * min(mags) / max(mags) if len(mags) > 1 and min(mags) > 0 else wide
    typ = d.get("type", "")
    return {"who": who, "fov": [_r(wide, 2), _r(narrow, 2)],
            "thermal": {"gen": None} if typ.endswith("_IR") else None,
            "nv": typ.endswith("LLTV") or "night" in sensor["name"].lower(), "mount": mount}


# -- the catalogue -------------------------------------------------------------


class Catalogue:
    def __init__(self, col: Collector, reader: Reader):
        self.g = reader.globals.vars
        self.weapons: dict[str, dict] = {}
        self.by_table: dict[int, str] = {}
        self.by_wstype: dict[tuple, str] = {}
        self.by_name: dict[str, str] = {}
        self.sensors: dict[str, dict] = {}
        self.sensor_id: dict[str, str] = {}
        self.units: list[dict] = []
        self.skipped = {"weapons_without_range": 0, "not_weapons": 0}
        self.shell_v0 = shell_velocities(col)
        for w in col.weapons:
            self._add_weapon(w)
        for s, file in col.sensors:
            got = _sensor(s, file)
            if got:
                self._add_sensor(*got)
        self.loadouts: dict[str, LuaTable] = {}
        for lo in col.loadouts:
            c = _s(lo.get("CLSID"))
            if c:
                self.loadouts[c] = lo
        seen: set[str] = set()
        for a, _file in col.aircraft:
            self._aircraft(a, seen)
        for u, _file in col.surface:
            self._surface(u, seen)

    def _unique(self, base: str, table) -> str:
        wid = f"local-dcs-{slug(base)}"
        n = 2
        while wid in table:
            wid = f"local-dcs-{slug(base)}-{n}"
            n += 1
        return wid

    def _add_weapon(self, w: LuaTable) -> None:
        row = _weapon(w, self.g)
        if row is None:
            cls, _shape = _weapon_class(w, self.g)
            self.skipped["weapons_without_range" if cls else "not_weapons"] += 1
            return
        # the same weapon declared twice (a pack and a module): keep the first
        key = row["labels"][0]
        if key in self.by_name:
            wid = self.by_name[key]
        else:
            wid = self._unique(key, self.weapons)
            row["id"] = wid
            self.weapons[wid] = row
        self.by_table[id(w)] = wid
        wt = w.get("wsTypeOfWeapon")
        if isinstance(wt, LuaTable):
            self.by_table[id(wt)] = wid
            tup = tuple(wt.array())
            if len(tup) == 4 and all(isinstance(x, int) for x in tup):
                self.by_wstype.setdefault(tup, wid)
        for n in row["labels"]:
            self.by_name.setdefault(n, wid)

    def _add_sensor(self, name: str, row: dict) -> str:
        if name in self.sensor_id and self.sensors[self.sensor_id[name]].get("detail", {}).get("declared", True):
            return self.sensor_id[name]
        sid = self.sensor_id.get(name) or self._unique(name, self.sensors)
        row["id"] = sid
        self.sensors[sid] = row
        self.sensor_id[name] = sid
        return sid

    def _sensor_ref(self, name: str, kind: str) -> str:
        """A sensor a unit names: the declared one, or one known by name only."""
        if name in self.sensor_id:
            return self.sensor_id[name]
        if kind == "camera" and _POD.search(name):
            kind = "tgp"
        return self._add_sensor(name, {"kind": kind, "name": name, "mount": "hull",
                                       "detail": {"declared": False,
                                                  "note": "named by a unit; its numbers are in the packed core database"}})

    def _unit_sensors(self, sens) -> list[str]:
        out = []
        if not isinstance(sens, LuaTable):
            return out
        for key in sens.keys():
            kind = SENSOR_KEYS.get(str(key).upper())
            if kind is None:
                continue
            v = sens.get(key)
            names = [v] if isinstance(v, str) else [x for x in v.array() if isinstance(x, str)] \
                if isinstance(v, LuaTable) else []
            for n in names:
                if n.strip():
                    sid = self._sensor_ref(n.strip(), kind)
                    if sid not in out:
                        out.append(sid)
        return out

    def _weapon_of_loadout(self, clsid: str, depth: int = 0) -> list[str]:
        lo = self.loadouts.get(clsid)
        if lo is None or depth > 4:
            return []
        for k in ("wsTypeOfWeapon", "attribute"):
            t = lo.get(k)
            if isinstance(t, LuaTable):
                if id(t) in self.by_table:
                    return [self.by_table[id(t)]]
                tup = tuple(t.array())
                if tup in self.by_wstype:
                    return [self.by_wstype[tup]]
        out = []
        els = lo.get("Elements")
        if isinstance(els, LuaTable):
            for e in els.array():
                if isinstance(e, LuaTable):
                    c = _s(e.get("payload_CLSID"))
                    if c:
                        out += [x for x in self._weapon_of_loadout(c, depth + 1) if x not in out]
        if not out:
            for k in ("name", "displayName"):
                v = _s(lo.get(k))
                if v and v in self.by_name:
                    return [self.by_name[v]]
        return out

    def _clean(self, names: list) -> list[str]:
        out = []
        for n in names:
            n = _s(n)
            if n and n not in out:
                out.append(n)
        return out

    def _aircraft(self, a: LuaTable, seen: set) -> None:
        names = self._clean([a.get("Name"), a.get("DisplayName"), a.get("DisplayNameShort")])
        if not names or names[0] in seen:
            return
        seen.add(names[0])
        sensors = self._unit_sensors(a.get("Sensors"))
        weapons: list[str] = []
        clsids: list[str] = []
        pylons = a.get("Pylons")
        if isinstance(pylons, LuaTable):
            for p in pylons.array():
                lau = p.get("Launchers") if isinstance(p, LuaTable) else None
                if isinstance(lau, LuaTable):
                    clsids += [c for c in (_s(x.get("CLSID")) for x in lau.array() if isinstance(x, LuaTable)) if c]
        for c in dict.fromkeys(clsids):
            for wid in self._weapon_of_loadout(c):
                if wid not in weapons:
                    weapons.append(wid)
        optics = []
        for sid in sensors:
            s = self.sensors[sid]
            o = _optic(s, "tgp" if s["kind"] == "tgp" else "pilot", "hull")
            if o:
                optics.append(o)
        self.units.append({"names": names, "weapons": weapons, "sensors": sensors, "optics": optics})

    def _surface(self, u: LuaTable, seen: set) -> None:
        names = self._clean([u.get("Name"), u.get("DisplayName"), u.get("DisplayNameShort")])
        if not names or names[0] in seen:
            return
        seen.add(names[0])
        sens = u.get("Sensors")
        sensors = self._unit_sensors(sens)
        turret = isinstance(sens, LuaTable) and sens.get("Mount_WS_ID") is not None
        weapons: list[str] = []
        ws = u.get("WS")
        if isinstance(ws, LuaTable):
            for w in ws.array():
                if not isinstance(w, LuaTable):
                    continue
                elev = None
                angles = w.get("angles") or w.get("angles_mech")
                if isinstance(angles, LuaTable):
                    rows = [r for r in angles.array() if isinstance(r, LuaTable)]
                    els = [(_n(r.get(3)), _n(r.get(4))) for r in rows]
                    els = [e for e in els if None not in e]
                    if els:
                        elev = [_r(math.degrees(min(e[0] for e in els)), 1), _r(math.degrees(max(e[1] for e in els)), 1)]
                lns = w.get("LN")
                for ln in (lns.array() if isinstance(lns, LuaTable) else []):
                    if isinstance(ln, LuaTable):
                        for wid in self._launcher(ln, elev, names[0]):
                            if wid not in weapons:
                                weapons.append(wid)
        optics = []
        for sid in sensors:
            o = _optic(self.sensors[sid], "gunner", "turret" if turret else "hull")
            if o:
                optics.append(o)
        self.units.append({"names": names, "weapons": weapons, "sensors": sensors, "optics": optics})

    def _launcher(self, ln: LuaTable, elev, unit: str) -> list[str]:
        out = []
        shells: list[str] = []
        shell_names: list[str] = []
        pls = ln.get("PL")
        for pl in (pls.array() if isinstance(pls, LuaTable) else []):
            if not isinstance(pl, LuaTable):
                continue
            ta = pl.get("type_ammunition")
            if isinstance(ta, LuaTable):
                tup = tuple(ta.array())
                if tup in self.by_wstype:
                    out.append(self.by_wstype[tup])
            na = _s(pl.get("name_ammunition"))
            if na and na in self.by_name and self.by_name[na] not in out:
                out.append(self.by_name[na])
            sn = pl.get("shell_name")
            if isinstance(sn, LuaTable):
                shells += [x for x in sn.array() if isinstance(x, str) and x not in shells]
            sd = _s(pl.get("shell_display_name"))
            if sd and sd not in shell_names:
                shell_names.append(sd)
        if out or not shells:
            return out
        dmax = _n(ln.get("distanceMax"))
        if dmax is None or dmax <= 0:
            return out
        dmin = _n(ln.get("distanceMin")) or 0
        typ = _n(ln.get("type"))
        alt = _n(ln.get("max_trg_alt"))
        cls = {9: "mg", 10: "mg", 3: "cannon", 12: "cannon", 2: "gun", 11: "gun"}.get(int(typ) if typ else -1, "gun")
        indirect = cls == "gun" and typ != 11 and dmax > 15000
        if indirect:
            cls = "artillery"
        proto = ln.path if isinstance(ln, Namespace) else (ln.proto or "")
        label = _s(ln.get("display_name")) or _s(ln.get("name")) or (shell_names[0] if shell_names else None) \
            or proto.rsplit(".", 1)[-1] or f"{unit} gun"
        labels = self._clean([ln.get("name"), ln.get("display_name"), proto.rsplit(".", 1)[-1] or None]
                             + shell_names + shells)
        key = (tuple(labels), dmin, dmax, alt, tuple(elev or ()))
        wid = self.by_name.get(repr(key))
        if wid is None:
            wid = self._unique(label, self.weapons)
            row = {"id": wid, "cls": cls, "name": label, "range": [_r(dmin), _r(dmax), _r(dmax)], "shape": "sphere",
                   "los": not indirect, "labels": labels or [label]}
            if elev:
                row["elev"] = elev
            if alt is not None and alt > 0:
                row["alt"] = [0, _r(alt)]
            detail = {"best": "distanceMax", "shells": shells}
            if typ is not None:
                detail["launcherType"] = LN_TYPES.get(int(typ), int(typ))
            v0 = self._muzzle(shells)
            if v0:
                detail["muzzleVelocity"] = v0
            row["detail"] = detail
            self.weapons[wid] = row
            self.by_name[repr(key)] = wid
        out.append(wid)
        return out

    def _muzzle(self, shells: list[str]) -> float | None:
        for s in shells:
            v = self.shell_v0.get(s)
            if v:
                return v
        return None

    def as_json(self) -> dict:
        weapons = [{k: v for k, v in w.items() if v is not None} for w in self.weapons.values()]
        weapons.sort(key=lambda w: w["id"])
        units = sorted(self.units, key=lambda u: u["names"][0].lower())
        return {"version": 1, "game": "dcs", "name": "DCS World", "source": "your installation",
                "built": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "tool": f"heat3d_ext_dcs {__version__}",
                "weapons": weapons, "sensors": {k: self.sensors[k] for k in sorted(self.sensors)}, "units": units}


def shell_velocities(col: Collector) -> dict[str, float]:
    out = {}
    for w in col.weapons:
        if _ref(w.get("category")) == "CAT_SHELLS":
            n, v = _s(w.get("name")), _n(w.get("v0"))
            if n and v:
                out.setdefault(n, _r(v))
    return out


def build(dcs: Path, extra: list[Path] | None = None, progress=None) -> tuple[dict, dict]:
    """The catalogue, and a summary of what was read."""
    col, reader = read_install(dcs, extra, progress)
    cat = Catalogue(col, reader)
    out = cat.as_json()
    declared = sum(1 for s in out["sensors"].values() if s.get("detail", {}).get("declared", True))
    summary = {"files": reader.files_read, "declared": {"weapons": len(col.weapons), "sensors": len(col.sensors),
                                                        "loadouts": len(col.loadouts), "aircraft": len(col.aircraft),
                                                        "surface_units": len(col.surface)},
               "weapons": len(out["weapons"]), "sensors": len(out["sensors"]), "sensors_with_numbers": declared,
               "units": len(out["units"]), "skipped": cat.skipped}
    return out, summary
