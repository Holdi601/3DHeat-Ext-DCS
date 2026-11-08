"""
A theatre's airfields: one `Mods/terrains/<theatre>/AirfieldsTaxiways/<name>.rn4`
(and `.rn5`) per airfield, named after it. They hold the airfield's taxi
network (`landscape4::lRoadNetwork`: link types such as `vpp`, the runway,
then nodes and links); its points are little-endian doubles, three to a
point (x north, y up, z east, DCS metres), 24 bytes apart.

Only the points are read here, found by their shape rather than by walking
the whole structure: runs of at least `RUN` points whose coordinates are
plausible DCS metres and lie within a few kilometres of each other. The
airfield is placed at the middle of its runway points' box (all its points
when no runway is told apart), with the box itself as its extent. The name is
the file's, as the game's mission editor shows it (underscores as spaces).
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path

import numpy as np

RUN = 3
STRIDE = 24
# A point's coordinates: inside any theatre (DCS metres), at a plausible height.
FAR = 3_000_000.0
LOW, HIGH = -200.0, 6000.0
# Points this far from the median point are not the airfield's.
REACH = 8000.0


@dataclass
class Airfield:
    name: str
    x: float
    z: float
    # The box of the points read: x0, z0, x1, z1.
    box: tuple[float, float, float, float]
    points: int


def points(data: bytes) -> np.ndarray:
    """Every run of plausible (x, y, z) doubles, as an (n, 3) array."""
    out: list[tuple[float, float, float]] = []
    n = len(data)
    off = 0
    while off + STRIDE <= n:
        run: list[tuple[float, float, float]] = []
        o = off
        while o + STRIDE <= n:
            x, y, z = struct.unpack_from("<3d", data, o)
            if not (abs(x) < FAR and abs(z) < FAR and LOW < y < HIGH and abs(x) > 1.0 and abs(z) > 1.0):
                break
            if run and (abs(x - run[-1][0]) > REACH or abs(z - run[-1][2]) > REACH):
                break
            run.append((x, y, z))
            o += STRIDE
        if len(run) >= RUN:
            out.extend(run)
            off = o
        else:
            off += 4
    return np.array(out, dtype=np.float64).reshape(-1, 3)


def read_one(path: Path) -> Airfield | None:
    p = points(path.read_bytes())
    if len(p) == 0:
        return None
    mx, mz = np.median(p[:, 0]), np.median(p[:, 2])
    p = p[(np.abs(p[:, 0] - mx) < REACH) & (np.abs(p[:, 2] - mz) < REACH)]
    if len(p) == 0:
        return None
    x0, z0 = float(p[:, 0].min()), float(p[:, 2].min())
    x1, z1 = float(p[:, 0].max()), float(p[:, 2].max())
    name = path.stem.replace("_", " ")
    return Airfield(name, (x0 + x1) / 2, (z0 + z1) / 2, (x0, z0, x1, z1), len(p))


def read(folder: str | Path) -> list[Airfield]:
    """The airfields of `<theatre>/AirfieldsTaxiways`, by name; the .rn4 of each where both are present."""
    d = Path(folder)
    if not d.is_dir():
        return []
    files: dict[str, Path] = {}
    for f in sorted(d.iterdir()):
        if f.suffix.lower() in (".rn4", ".rn5") and (f.stem not in files or f.suffix.lower() == ".rn4"):
            files[f.stem] = f
    out = []
    for f in files.values():
        a = read_one(f)
        if a is not None:
            out.append(a)
    return out
