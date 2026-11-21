"""
DCS World's catalogue: every aircraft, helicopter, ground unit and ship, and every weapon, of your own install
(the modules', asset packs' and Saved Games mods' plain Lua, read as `ranges` reads it), as `catalog.json`.

Each unit: its type name (what recordings and missions name it by), display name, class (from its attributes:
fighter, attack helicopter, tank, SAM radar, ship...), domain, the model it is drawn with (`Shape`), the weapons its
pylons or launchers carry and a few numbers its table states. DCS units have no fixed side, so `nation` is left
empty. The core database the game keeps packed (`Scripts/Database.edce`) is not read: units defined only there are
missing.
"""

from __future__ import annotations

import re
from pathlib import Path

from . import __version__
from .lua import LuaTable
from .ranges import Catalogue, _s, _n, read_install

#: A unit's class from the words of its `attribute` list, first match wins: (pattern, domain, class).
CLASSES = (
    (r"attack helicopters", "air", "heli-attack"), (r"helicopters?", "air", "heli-transport"),
    (r"strategic bombers|bombers", "air", "bomber"), (r"awacs", "air", "awacs"), (r"tankers", "air", "tanker"),
    (r"transports", "air", "transport"), (r"uav", "air", "uav"), (r"battleplanes|attack", "air", "attack"),
    (r"multirole fighters|fighters|interceptors", "air", "fighter"), (r"planes|aircraft", "air", "aircraft"),
    (r"aircraft carriers", "sea", "carrier"), (r"cruisers|destroyers|frigates|corvettes|heavy armed ships", "sea", "warship"),
    (r"submarines", "sea", "submarine"), (r"ships|boats|unarmed ships|armed ships|ship", "sea", "boat"),
    (r"sam sr|sam tr|sam elements|sam cc|sam ll|sam|ewr", "ground", "sam"),
    (r"aaa|ir guided sam|manpads", "ground", "spaa"), (r"tanks|modern tanks|old tanks", "ground", "mbt"),
    (r"ifv", "ground", "ifv"), (r"apc|armored vehicles", "ground", "apc"),
    (r"mlrs|artillery|indirect fire", "ground", "artillery"), (r"infantry", "ground", "infantry"),
    (r"trucks|cars|unarmed vehicles|vehicles", "ground", "car"), (r"fortifications|buildings|static", "ground", "static"),
)
#: Real vehicles' names that DCS's type names put differently (the rest use the display name).
KEYS = {"t-72b": "T-72B", "t-72b3": "T-72B3", "t-80ud": "T-80UD", "t-90": "T-90", "m-1 abrams": "M1A2",
        "m1a2c sep v3": "M1A2C SEP v3", "leopard-2": "Leopard 2A6M", "leopard-2a5": "Leopard 2A5",
        "leopard1a3": "Leopard 1A3", "challenger2": "Challenger 2", "merkava_mk4": "Merkava Mk.4",
        "bmp-1": "BMP-1", "bmp-2": "BMP-2", "bmp-3": "BMP-3", "btr-80": "BTR-80", "btr-82a": "BTR-82A",
        "m-2 bradley": "M2A2 Bradley", "lav-25": "LAV-25", "m1126 stryker icv": "M1126 Stryker", "zsu-23-4 shilka": "ZSU-23-4",
        "2s6 tunguska": "2K22 Tunguska", "gepard": "Gepard", "f-16c_50": "F-16C", "fa-18c_hornet": "F/A-18C",
        "f-15c": "F-15C", "f-15esE": "F-15E", "su-27": "Su-27", "su-33": "Su-33", "mig-29a": "MiG-29A",
        "mig-29s": "MiG-29S", "su-25": "Su-25", "su-25t": "Su-25T", "a-10c": "A-10C", "a-10c_2": "A-10C",
        "ah-64d_blk_ii": "AH-64D", "ka-50": "Ka-50", "mi-8mt": "Mi-8MTV2", "mi-24p": "Mi-24P", "uh-1h": "UH-1H",
        "uh-60a": "UH-60A", "ch-47d": "CH-47D", "oh58d": "OH-58D", "f-14b": "F-14B", "f-14a-135-gr": "F-14A",
        "av8bna": "AV-8B", "m-2000c": "Mirage 2000C", "jf-17": "JF-17", "f-5e-3": "F-5E", "mig-21bis": "MiG-21bis"}


#: Category words DCS puts before a display name ("MBT T-72B", "SAM SA-11 Buk LN 9A310M1").
PREFIX = re.compile(r"^(?:(?:MBT|IFV|APC|MT|LT|AAA|SAM|SPAAA|SPAAG|EWR|ARV|ATGM|SPG|SPH|MLRS|CV|FFG|FF|CG|DDG|LHA|LST|"
                    r"Scout|IFV/APC|Armed truck|Truck|Tanker|Bus|Car|SAM/AAA|AAA/SAM)\s+)+")


#: A mod's tag after the name ("T-90M [CH]").
TAG = re.compile(r"\s*\[[^\]]*\]\s*$")


def _words(t) -> list[str]:
    if not isinstance(t, LuaTable):
        return []
    return [x.lower() for x in t.array() if isinstance(x, str)]


def _shape(u: LuaTable) -> str:
    for key in ("Shape",):
        s = _s(u.get(key))
        if s:
            return s
    std = u.get("shape_table_data")
    if isinstance(std, LuaTable):
        for row in std.array():
            if isinstance(row, LuaTable) and _s(row.get("file")):
                return _s(row.get("file"))
    vis = u.get("visual")
    if isinstance(vis, LuaTable) and _s(vis.get("shape")):
        return _s(vis.get("shape"))
    return ""


def _classify(words: list[str], default_domain: str) -> tuple[str, str]:
    text = " | ".join(words)
    for rx, dom, cls in CLASSES:
        if re.search(rf"(^|\| ){rx}($| \|)", text):
            if default_domain == "air" and dom == "ground":
                continue
            return dom, cls
    return default_domain, "aircraft" if default_domain == "air" else "vehicle"


def build(dcs: Path, extra: list[Path]) -> list[dict]:
    col, reader = read_install(dcs, extra)
    cat = Catalogue(col, reader)
    by_name = {u["names"][0]: u for u in cat.units}
    items: list[dict] = []
    seen: set[str] = set()
    for table, default in ([(a, "air") for a, _f in col.aircraft] + [(u, "ground") for u, _f in col.surface]):
        uid = _s(table.get("Name"))
        if not uid or uid in seen:
            continue
        seen.add(uid)
        words = _words(table.get("attribute"))
        dom, cls = _classify(words, default)
        if default == "air" and re.search(r"helicopter", " ".join(words)) and not cls.startswith("heli"):
            cls = "heli-transport"
        name = _s(table.get("DisplayName")) or uid
        u = by_name.get(uid, {})
        nums = {}
        for k, out in (("M_empty", "emptyKg"), ("M_max", "maxKg"), ("V_max_sea_level", "vmaxSeaLevel"),
                        ("H_max", "ceiling"), ("range", "rangeKm"), ("max_speed", "maxSpeed")):
            v = _n(table.get(k))
            if v is not None:
                nums[out] = round(v, 3)
        items.append({
            "id": uid, "kind": "vehicle", "name": name, "short": _s(table.get("DisplayNameShort")) or "",
            "class": cls, "domain": dom, "nation": "", "key": KEYS.get(uid.lower(), TAG.sub("", PREFIX.sub("", name)).strip()),
            "shape": _shape(table), "weapons": [cat.weapons[w]["name"] for w in u.get("weapons", []) if w in cat.weapons],
            "attributes": words[:12], "numbers": nums,
        })
    for wid, w in cat.weapons.items():
        items.append({"id": wid, "kind": "weapon", "name": w.get("name", wid), "class": w.get("cls", ""), "nation": "",
                      "key": w.get("name", wid), "numbers": {"rangeMax": (w.get("range") or [None, None, None])[-1]}})
    return items


def source() -> str:
    return f"heat3d-dcs-maps {__version__}"


def game_build(dcs: Path) -> str:
    cfg = dcs / "autoupdate.cfg"
    if cfg.is_file():
        m = re.search(r'"version"\s*:\s*"([^"]+)"', cfg.read_text(encoding="utf-8", errors="replace"))
        if m:
            return m.group(1)
    return "unknown"


def cmd_catalog(args) -> int:
    import json
    import os
    import time

    from . import install, ranges

    dcs = install.find(args.dcs)
    if dcs is None:
        print("no DCS World install found: give it with --dcs <folder>", flush=True)
        return 2
    extra = [] if args.no_saved_games else ([Path(args.saved_games)] if args.saved_games else ranges.saved_games())
    lv = os.environ.get("HEAT3D_LEVELS")
    out = Path(args.out) if args.out else (Path(lv) / "dcs" / "catalog.json" if lv else Path("catalog.json"))
    t0 = time.monotonic()
    items = build(dcs, extra)
    pack = out.parent.parent / "model-packs" / "dcs" / "model-pack.json"
    if pack.is_file():
        units = json.loads(pack.read_text(encoding="utf-8")).get("units", {})
        for it in items:
            if it["id"] in units:
                it["model"] = f"model-packs/dcs/{units[it['id']]['file']}"
    doc = {"format": "3dheat-catalog", "version": 1, "game": "dcs", "gameBuild": game_build(dcs), "source": source(),
           "items": sorted(items, key=lambda i: (i["kind"], i["id"]))}
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".json.part")
    tmp.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(out)
    kinds: dict[str, int] = {}
    for it in items:
        kinds[it.get("domain", it["kind"])] = kinds.get(it.get("domain", it["kind"]), 0) + 1
    print(f"{len(items)} items {kinds} in {time.monotonic() - t0:.0f} s -> {out}")
    return 0


def add_verbs(sub) -> None:
    p = sub.add_parser("catalog", help="every aircraft, ground unit, ship and weapon of your install -> catalog.json")
    p.add_argument("-o", "--out", help="the .json to write (default <HEAT3D_LEVELS>/dcs/catalog.json)")
    p.add_argument("--dcs", help="the DCS World folder")
    p.add_argument("--saved-games", help="the DCS Saved Games folder whose Mods to read too (default: found)")
    p.add_argument("--no-saved-games", action="store_true", help="read the install only, not mods in Saved Games")
    p.set_defaults(run=cmd_catalog)
