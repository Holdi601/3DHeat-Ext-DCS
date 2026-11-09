"""Where DCS World is installed, and the theatres in it."""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

#: Folder names DCS installs under: the standalone version, then Steam's.
_NAMES = ("DCS World", "DCS World OpenBeta", "DCSWorld", "DCS")


def _registry() -> list[Path]:
    if sys.platform != "win32":
        return []
    try:
        import winreg
    except ImportError:
        return []
    out = []
    for key in (r"Software\Eagle Dynamics\DCS World", r"Software\Eagle Dynamics\DCS World OpenBeta"):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key) as k:
                out.append(Path(winreg.QueryValueEx(k, "Path")[0]))
        except OSError:
            pass
    return out


def _steam_libraries() -> list[Path]:
    roots = [Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Steam"]
    libs: list[Path] = []
    for root in roots:
        vdf = root / "steamapps" / "libraryfolders.vdf"
        try:
            text = vdf.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        libs += [Path(p.replace("\\\\", "\\")) for p in re.findall(r'"path"\s+"([^"]+)"', text)]
    return libs


def candidates() -> list[Path]:
    out = list(_registry())
    for lib in _steam_libraries():
        out += [lib / "steamapps" / "common" / n for n in _NAMES]
    drives = [f"{c}:\\" for c in "CDEFGHIJ"] if sys.platform == "win32" else []
    for d in drives:
        for base in ("Program Files\\Eagle Dynamics", "Eagle Dynamics", "Games", "SteamLibrary\\steamapps\\common"):
            out += [Path(d) / base / n for n in _NAMES]
    return out


def find(explicit: str | None = None) -> Path | None:
    """The DCS install: `explicit`, else the DCS_PATH environment variable, else the first place found."""
    for p in ([Path(explicit)] if explicit else []) + ([Path(os.environ["DCS_PATH"])] if os.environ.get("DCS_PATH") else []):
        return p if (p / "Mods" / "terrains").is_dir() else None
    for p in candidates():
        try:
            if (p / "Mods" / "terrains").is_dir():
                return p
        except OSError:
            continue
    return None


@dataclass
class Theatre:
    name: str  # the folder under Mods/terrains
    folder: Path
    surface: Path | None
    towns: Path
    scene: Path | None = None

    @property
    def size(self) -> int:
        return self.surface.stat().st_size if self.surface else 0


def theatres(dcs: Path) -> list[Theatre]:
    out = []
    for d in sorted((dcs / "Mods" / "terrains").iterdir()):
        if not d.is_dir():
            continue
        surfaces = sorted((d / "surface").glob("*.surface5")) if (d / "surface").is_dir() else []
        scenes = sorted((d / "Scenes").glob("*.scn5")) if (d / "Scenes").is_dir() else []
        out.append(Theatre(d.name, d, surfaces[0] if surfaces else None, d / "map" / "towns.lua",
                           scenes[0] if scenes else None))
    return out


def theatre(dcs: Path, name: str) -> Theatre | None:
    for t in theatres(dcs):
        if t.name.lower() == name.lower():
            return t
    return None
