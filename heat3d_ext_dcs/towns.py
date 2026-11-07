"""
A theatre's place names: `Mods/terrains/<theatre>/map/towns.lua`, a plain Lua
table the mission editor shows on its map:

    towns = {
    ["Garapan"] = { latitude = 15.207571, longitude = 145.719597, display_name = _("Garapan")},
    ...

Read as text with a pattern, never run.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

_ENTRY = re.compile(r'\[\s*"((?:[^"\\]|\\.)*)"\s*\]\s*=\s*\{([^{}]*)\}')
_FIELD = re.compile(r"(latitude|longitude)\s*=\s*(-?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?)")
_DISPLAY = re.compile(r'display_name\s*=\s*_?\(?\s*"((?:[^"\\]|\\.)*)"')


@dataclass
class Town:
    name: str
    lat: float
    lon: float
    display: str


def parse(text: str) -> list[Town]:
    out: list[Town] = []
    for m in _ENTRY.finditer(text):
        fields = dict(_FIELD.findall(m.group(2)))
        if "latitude" not in fields or "longitude" not in fields:
            continue
        d = _DISPLAY.search(m.group(2))
        name = m.group(1)
        out.append(Town(name, float(fields["latitude"]), float(fields["longitude"]), d.group(1) if d else name))
    return out


def read(path: str | Path) -> list[Town]:
    p = Path(path)
    if not p.is_file():
        return []
    return parse(p.read_text(encoding="utf-8", errors="replace"))
