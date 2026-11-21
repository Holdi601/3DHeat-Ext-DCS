"""
Each theatre's airbases as a 3DHeat layout: the airfields with their names and ids (`Radio.lua`, `Beacons.lua`),
their runways (from the instrument-landing beacons at both ends), and the parking stands aircraft start from, as
the missions in your install place them (every `.miz` under the install is read for its `mission` table only:
units that start from a stand carry the stand's number, and their place is the stand's).

Read only from the install: the terrain's Lua files that are plain text and the mission files; nothing encrypted
is opened. Positions are DCS metres, x north, z east, y up - the DCS levels' own frame (glb X = x, Z = z).

Written as `<Theatre>.layouts.json` for the whole theatre (the mission importer names airbases from it) and as
`<level>.layouts.json` beside each level of it, with what lies inside the level.
"""

from __future__ import annotations

import bisect
import json
import math
import re
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable

from . import airfields

FORMAT = "3dheat-layouts"
GAME = "dcs"

#: A theatre's folder name and the name its missions give it (`theatre` in the mission), where they differ.
THEATRE_IDS = {"GermanyColdWar": "GermanyCW", "Sinai": "SinaiMap", "MarianasWWII": "MarianaIslandsWWII"}

_RADIO = re.compile(r"--\s*([^\n]+?)\s*\n\s*radioId\s*=\s*'airfield(\d+)_\d+'")
_BEACON_START = re.compile(r"\{\s*display_name\s*=")
_BEACON = re.compile(
    r"display_name\s*=\s*_\('((?:[^'\\]|\\.)*)'\);.*?beaconId\s*=\s*'airfield(\d+)_\d+';.*?type\s*=\s*(\w+);"
    r".*?position\s*=\s*\{\s*([-\d.eE]+),\s*([-\d.eE]+),\s*([-\d.eE]+)\s*\};(?:\s*direction\s*=\s*([-\d.eE]+);)?",
    re.S)
#: Beacons on a runway's centre line, with how far beyond the runway's end (or before its threshold) each lies, m.
_ON_AXIS = {"BEACON_TYPE_ILS_LOCALIZER": 300.0, "BEACON_TYPE_PRMG_LOCALIZER": 300.0,
            "BEACON_TYPE_ILS_NEAR_HOMER": 1000.0}
RUNWAY_WIDTH = 50.0


def _theatre_id(folder: str) -> str:
    return THEATRE_IDS.get(folder, folder)


# ---------------------------------------------------------------- the terrain's files


def radio_names(text: str) -> dict[int, str]:
    """Airfield ids and the names `Radio.lua` gives them (the comment over each)."""
    return {int(m.group(2)): m.group(1).strip() for m in _RADIO.finditer(text)}


def beacons(text: str) -> list[dict[str, Any]]:
    """The airfields' beacons in `Beacons.lua`: name, airfield id, type, position, direction."""
    out = []
    starts = [m.start() for m in _BEACON_START.finditer(text)] + [len(text)]
    for a, b in zip(starts, starts[1:]):
        m = _BEACON.search(text, a, b)
        if not m:
            continue
        out.append({"name": m.group(1).replace("\\'", "'"), "id": int(m.group(2)), "type": m.group(3),
                    "x": float(m.group(4)), "y": float(m.group(5)), "z": float(m.group(6)),
                    "direction": float(m.group(7)) if m.group(7) else None})
    return out


def runways(bs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Runways from beacons on their centre lines at both ends: the stretch between, less how far beyond the ends
    the beacons lie; its heading the axis (degrees from north towards east), its two ends' headings in its name."""
    out = []
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for b in bs:
        if b["type"] in _ON_AXIS and b["direction"] is not None:
            by_type[b["type"]].append(b)
    used: set[int] = set()
    for kind, group in by_type.items():
        beyond = _ON_AXIS[kind]
        for i, a in enumerate(group):
            for j in range(i + 1, len(group)):
                b = group[j]
                if i in used or j in used:
                    continue
                diff = abs(((a["direction"] - b["direction"]) % 360) - 180)
                d = math.hypot(a["x"] - b["x"], a["z"] - b["z"])
                if diff > 3 or not (800 + 2 * beyond < d < 6000 + 2 * beyond):
                    continue
                axis = math.degrees(math.atan2(b["z"] - a["z"], b["x"] - a["x"])) % 360
                if min(abs(axis - a["direction"] % 360), 360 - abs(axis - a["direction"] % 360)) % 180 > 4 and \
                        abs((axis - a["direction"]) % 180) > 4 and abs((axis - a["direction"]) % 180) < 176:
                    continue  # not on one line
                used.update((i, j))
                length = d - 2 * beyond
                cx, cz = (a["x"] + b["x"]) / 2, (a["z"] + b["z"]) / 2
                out.append({"x": cx, "z": cz, "y": (a["y"] + b["y"]) / 2, "heading": axis % 180, "length": length})
    # The same runway seen by two kinds of beacon: keep the first (localizers before homers).
    kept: list[dict[str, Any]] = []
    for r in out:
        if not any(math.hypot(r["x"] - k["x"], r["z"] - k["z"]) < 300 and
                   min(abs(r["heading"] - k["heading"]), 180 - abs(r["heading"] - k["heading"])) < 5 for k in kept):
            kept.append(r)
    return kept


def _rect(r: dict[str, Any]) -> list[list[float]]:
    h = math.radians(r["heading"])
    ux, uz = math.cos(h), math.sin(h)
    vx, vz = -uz, ux
    L, W = r["length"] / 2, RUNWAY_WIDTH / 2
    return [[round(r["x"] + sx * L * ux + sw * W * vx, 1), round(r["y"], 1), round(r["z"] + sx * L * uz + sw * W * vz, 1)]
            for sx, sw in ((-1, -1), (1, -1), (1, 1), (-1, 1))]


# ---------------------------------------------------------------- the missions


_TABLE = re.compile(r'"(?:[^"\\]|\\.)*"|[{}]')


class _Braces:
    """Where each table of a Lua text opens and closes, strings skipped."""

    def __init__(self, text: str):
        self.opens: list[int] = []
        self.close: dict[int, int] = {}
        stack: list[int] = []
        for m in _TABLE.finditer(text):
            c = text[m.start()]
            if c == "{":
                stack.append(m.start())
                self.opens.append(m.start())
            elif c == "}" and stack:
                self.close[stack.pop()] = m.start()

    def around(self, pos: int, up: int = 0) -> tuple[int, int] | None:
        """The table holding `pos`, or the one `up` levels out from it."""
        i = bisect.bisect_left(self.opens, pos) - 1
        found = 0
        while i >= 0:
            o = self.opens[i]
            c = self.close.get(o, -1)
            if c > pos:
                if found == up:
                    return o, c
                found += 1
            i -= 1
        return None


def _own(text: str, br: _Braces, a: int, b: int, key: str) -> str | None:
    """A key's value in the table [a, b] itself, not in one inside it."""
    for m in re.finditer(r'\["' + key + r'"\]\s*=\s*("(?:[^"\\]|\\.)*"|[-\d.eE]+)', text[a:b]):
        p = a + m.start()
        if br.around(p) == (a, b):
            v = m.group(1)
            return v[1:-1] if v.startswith('"') else v
    return None


_PARKING = re.compile(r'\["parking_id"\]\s*=\s*"([^"]*)"|\["parking"\]\s*=\s*"?(\d+)"?')


def mission_stands(text: str) -> tuple[str, list[dict[str, Any]]]:
    """The mission's theatre, and its aircraft that start from a stand: airfield id, stand, place, type."""
    m = re.search(r'\["theatre"\]\s*=\s*"([^"]+)"', text)
    theatre = m.group(1) if m else ""
    if '["parking' not in text:
        return theatre, []
    br = _Braces(text)
    out: list[dict[str, Any]] = []
    seen: set[tuple[int, int]] = set()
    for m in _PARKING.finditer(text):
        unit = br.around(m.start())
        if unit is None or unit in seen:
            continue
        seen.add(unit)
        a, b = unit
        stand = _own(text, br, a, b, "parking_id") or _own(text, br, a, b, "parking")
        x, y = _own(text, br, a, b, "x"), _own(text, br, a, b, "y")
        if stand is None or x is None or y is None:
            continue
        group = br.around(m.start(), 2)  # unit -> units -> group
        if group is None:
            continue
        ga, gb = group
        ad = re.search(r'\["airdromeId"\]\s*=\s*(\d+)', text[ga:gb])
        if not ad:
            continue
        alt = _own(text, br, a, b, "alt")
        out.append({"airdrome": int(ad.group(1)), "stand": stand, "x": float(x), "z": float(y),
                    "y": float(alt) if alt else 0.0, "type": _own(text, br, a, b, "type") or ""})
    return theatre, out


def missions(root: Path) -> Iterable[Path]:
    for p in sorted(root.rglob("*.miz")):
        yield p


def stands(root: Path, log: Callable[[str], None] = lambda s: None) -> dict[str, dict[int, dict[str, dict]]]:
    """Every stand the install's missions start aircraft from: theatre -> airfield id -> stand -> place."""
    acc: dict[str, dict[int, dict[str, list]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    n = read = 0
    for p in missions(root):
        n += 1
        try:
            with zipfile.ZipFile(p) as z:
                name = next((i for i in z.namelist() if i.replace("\\", "/").lower() == "mission"), None)
                if name is None:
                    continue
                text = z.read(name).decode("utf-8", "replace")
        except (zipfile.BadZipFile, OSError, KeyError):
            continue
        theatre, found = mission_stands(text)
        read += 1
        for s in found:
            acc[theatre][s["airdrome"]][s["stand"]].append((s["x"], s["y"], s["z"], s["type"]))
        if n % 500 == 0:
            log(f"  {n} missions")
    log(f"  {read} missions read")
    out: dict[str, dict[int, dict[str, dict]]] = {}
    for theatre, fields in acc.items():
        out[theatre] = {}
        for ad, ss in fields.items():
            out[theatre][ad] = {}
            for stand, pts in ss.items():
                # The stand's place: the median of where missions put it (one mission's odd placement left out).
                xs = sorted(q[0] for q in pts)
                zs = sorted(q[2] for q in pts)
                mx, mz = xs[len(xs) // 2], zs[len(zs) // 2]
                near = [q for q in pts if math.hypot(q[0] - mx, q[2] - mz) < 30] or                     [min(pts, key=lambda q: math.hypot(q[0] - mx, q[2] - mz))]
                mx, mz = sum(q[0] for q in near) / len(near), sum(q[2] for q in near) / len(near)
                types = sorted({q[3] for q in near if q[3]})
                out[theatre][ad][stand] = {"x": mx, "z": mz, "y": min(q[1] for q in near), "missions": len(near),
                                           "types": types[:6]}
    return out


# ---------------------------------------------------------------- one theatre


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def theatre_layout(folder: Path, theatre_stands: dict[int, dict[str, dict]], tool: str) -> dict[str, Any]:
    """The theatre's airbases, runways and stands as one layout."""
    radio = radio_names((folder / "Radio.lua").read_text("utf-8", "replace")) if (folder / "Radio.lua").is_file() else {}
    bs = beacons((folder / "Beacons.lua").read_text("utf-8", "replace")) if (folder / "Beacons.lua").is_file() else []
    fields = airfields.read(folder / "AirfieldsTaxiways")
    ids = sorted(set(radio) | {b["id"] for b in bs} | set(theatre_stands))
    objectives: list[dict[str, Any]] = []
    spawns: list[dict[str, Any]] = []
    for ad in ids:
        mine = [b for b in bs if b["id"] == ad]
        names = [b["name"] for b in mine if b["name"]]
        name = max(set(names), key=names.count) if names else radio.get(ad, f"Airfield {ad}")
        st = theatre_stands.get(ad, {})
        # Where: its taxiways' middle (matched by name, else the nearest to its beacons or stands), else those.
        pts = [(b["x"], b["z"]) for b in mine] + [(s["x"], s["z"]) for s in st.values()]
        cx = sum(p[0] for p in pts) / len(pts) if pts else None
        cz = sum(p[1] for p in pts) / len(pts) if pts else None
        field = next((f for f in fields if _norm(f.name) and _norm(f.name) == _norm(radio.get(ad, ""))), None) or             next((f for f in fields if _norm(f.name) and (_norm(f.name) in _norm(name) or _norm(name).startswith(_norm(f.name)))), None)
        if field is None and cx is not None:
            near = min(fields, key=lambda f: math.hypot(f.x - cx, f.z - cz), default=None)
            if near is not None and math.hypot(near.x - cx, near.z - cz) < 6000:
                field = near
        if field is not None:
            cx, cz = field.x, field.z
        if cx is None:
            continue
        # Stands far from the airfield are a mission's misreading (a group taking off elsewhere that lands here).
        reach = 4000.0 if field is None else max(3000.0, math.hypot(field.box[2] - field.box[0], field.box[3] - field.box[1]))
        st = {k: v for k, v in st.items() if math.hypot(v["x"] - cx, v["z"] - cz) <= reach}
        # Its height: the beacons' (the missions' stand heights are often not the ground's); else 0, under the ground.
        ys = sorted(b["y"] for b in mine)
        y = ys[len(ys) // 2] if ys else 0.0
        rws = [r for r in runways(mine) if math.hypot(r["x"] - cx, r["z"] - cz) < 8000]
        obj: dict[str, Any] = {"type": "airfield", "team": None, "name": name, "airdromeId": ad,
                               "position": [round(cx, 1), round(y, 1), round(cz, 1)], "shape": "point",
                               "stands": len(st)}
        if radio.get(ad) and radio[ad] != name:
            obj["radioName"] = radio[ad]
        if field is not None:
            obj["taxiways"] = field.name
            obj["box"] = [round(v, 1) for v in field.box]
        if rws:
            obj["heading"] = round(rws[0]["heading"], 1)
        objectives.append(obj)
        for r in rws:
            ends = (round(r["heading"] / 10) % 36 or 36, (round(r["heading"] / 10) + 18) % 36 or 36)
            objectives.append({"type": "objective", "kind": "runway", "team": None, "airdromeId": ad,
                               "name": f"{name} {min(ends):02d}/{max(ends):02d}", "length": round(r["length"]),
                               "heading": round(r["heading"], 1), "points": _rect(r)})
        for stand, s in sorted(st.items(), key=lambda kv: (len(kv[0]), kv[0])):
            spawns.append({"type": "vehicle_spawn", "team": None, "base": name, "airdromeId": ad, "stand": stand,
                           "vehicle": "aircraft", "position": [round(s["x"], 1), round(y, 1), round(s["z"], 1)],
                           "missions": s["missions"], **({"types": s["types"]} if s["types"] else {})})
    return {"format": FORMAT, "version": 1, "game": GAME, "level": _theatre_id(folder.name), "theatre": folder.name,
            "source": tool, "units": "m", "up": "y",
            "coordinates": "DCS metres: x north, y up, z east (the DCS levels' own frame)",
            "layouts": [{"id": "airbases", "name": "Airbases", "mode": "airbases", "aliases": ["dcs"],
                         "objectives": objectives, "zones": [], "spawns": spawns}]}


def within(doc: dict[str, Any], level: str, box: tuple[float, float, float, float]) -> dict[str, Any]:
    """The theatre's layout cut to a level's box (x0, z0, x1, z1): what stands inside it."""
    x0, z0, x1, z1 = box
    inside = lambda p: x0 <= p[0] <= x1 and z0 <= p[2] <= z1  # noqa: E731
    lay = doc["layouts"][0]
    ids = {o["airdromeId"] for o in lay["objectives"] if o["type"] == "airfield" and inside(o["position"])}
    return {**doc, "level": level,
            "layouts": [{**lay, "objectives": [o for o in lay["objectives"] if o.get("airdromeId") in ids],
                         "spawns": [s for s in lay["spawns"] if s.get("airdromeId") in ids]}]}


def counts(doc: dict[str, Any]) -> tuple[int, int, int]:
    ls = doc["layouts"]
    return (sum(len(l["objectives"]) for l in ls), sum(len(l["zones"]) for l in ls), sum(len(l["spawns"]) for l in ls))


def write(path: Path, doc: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(doc, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)
