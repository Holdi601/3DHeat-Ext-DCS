"""
Builds .surface5 files to the layout real ones have (see heat3d_ext_dcs/surface5.py),
so the tests need no game data: none is kept in this repository.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

TYPE_NAME = b"landscape5::Surface5File"


def _s(text: str) -> bytes:
    raw = text.encode()
    return struct.pack("<I", len(raw)) + raw


@dataclass
class Overlay:
    shader: str
    material: str
    base: np.ndarray  # overlay vertex -> tile vertex
    triangles: np.ndarray  # overlay vertex indices


@dataclass
class TileSpec:
    translation: tuple[float, float, float]
    positions: np.ndarray  # tile frame
    triangles: np.ndarray
    kinds: np.ndarray | None  # TRITYPE; None: a tile of the second set
    overlays: list[Overlay] = field(default_factory=list)


class _Blob:
    def __init__(self) -> None:
        self.data = bytearray()

    def add(self, array: np.ndarray) -> tuple[int, int]:
        raw = np.ascontiguousarray(array).tobytes()
        at = len(self.data)
        self.data += raw + b"\0" * (16 + (-len(raw) % 16))
        return at, len(raw)


def _entry(name: str, kind: int, size: int, flags: int, at_count: tuple[int, int]) -> bytes:
    at, count = at_count
    return struct.pack("<I", 1) + _s(name) + struct.pack("<HHIQIH", kind, size, flags, count, at & 0xFFFFFFFF, at >> 32)


def _group(entries: list[bytes], nverts: int, shader: str, material: str) -> bytes:
    out = struct.pack("<IIII", 5, 2, nverts, len(entries)) + b"".join(entries)
    # The shader, the material, and the define list real files carry after them.
    out += struct.pack("<I", 2) + _s(shader) + _s(material)
    out += struct.pack("<I", 1) + _s("shaderDefine") + struct.pack("<II", 0, 1) + _s("NODEFINITIONS")
    out += b"\xff\xff\xff\xff" + struct.pack("<I", 1000) + b"\xff\x00"
    return out


def record(t: TileSpec, blob: _Blob) -> bytes:
    p = np.asarray(t.positions, "<f4")
    lo, hi = p.min(0), p.max(0)
    mat = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, *t.translation, 1]
    out = struct.pack("<I", 7) + struct.pack("<16f", *mat) + struct.pack("<6f", *lo, *hi) + struct.pack("<I", 0)
    tri = np.asarray(t.triangles, "<u4")
    n = len(p)
    if t.kinds is not None:
        out += _group(
            [_entry("TRITYPE", 4, 4, 1, blob.add(np.asarray(t.kinds, "<u4"))), _entry("TRI", 6, 12, 1, blob.add(tri))],
            n, "Surface5.0", "Land",
        )
    else:
        out += _group([_entry("TRI", 6, 12, 1, blob.add(tri))], n, "Surface5.0", "Land")
    for o in t.overlays:
        m = len(o.base)
        out += _group(
            [
                _entry("offset", 0, 4, 0, blob.add(np.ones(m, "<f4"))),
                _entry("parametricUVW", 2, 12, 0, blob.add(np.zeros((m, 3), "<f4"))),
                _entry("baseIndex", 4, 4, 0, blob.add(np.asarray(o.base, "<u4"))),
                _entry("materialParamsIndex", 4, 4, 0, blob.add(np.zeros(m, "<u4"))),
                _entry("TRI", 6, 12, 1, blob.add(np.asarray(o.triangles, "<u4"))),
            ],
            m, o.shader, o.material,
        )
    out += struct.pack("<IIII", 0, 2, n, 5)
    out += _entry("Pbase", 2, 12, 0, blob.add(p))
    out += _entry("nextLodIndex", 4, 4, 0, blob.add(np.zeros(n, "<u4")))
    out += _entry("Nbase", 2, 12, 0, blob.add(np.tile(np.asarray([0, 1, 0], "<f4"), (n, 1))))
    out += _entry("maxEdge", 0, 4, 0, blob.add(np.zeros(n, "<f4")))
    out += _entry("depth", 0, 4, 0, blob.add(np.zeros(n, "<f4")))
    out += struct.pack("<HI", 0, 3) + b"\0" * 24 + b"\xff" * 6
    return out


def write(path: Path, tiles: list[TileSpec], type_name: bytes = TYPE_NAME) -> Path:
    blob = _Blob()
    body = b"".join(record(t, blob) for t in tiles)
    head = struct.pack("<I", len(type_name)) + type_name + struct.pack("<IIQI", 5, 4, 0, len(tiles))
    index_len = 0x20 + len(head) + len(body)
    out = struct.pack("<IIQ", 2, 0x30, index_len) + b"\0" * 16 + head + body
    assert len(out) == index_len
    Path(path).write_bytes(out + bytes(blob.data))
    return Path(path)


def grid(n: int, step: float, height=lambda x, z: 0.0 * x) -> tuple[np.ndarray, np.ndarray]:
    """An n x n vertex grid in the tile's frame (x north, z east) and its triangles."""
    xs, zs = np.meshgrid(np.arange(n) * step, np.arange(n) * step, indexing="ij")
    pos = np.stack([xs.ravel(), height(xs, zs).ravel(), zs.ravel()], axis=1)
    tris = []
    for i in range(n - 1):
        for j in range(n - 1):
            a, b, c, d = i * n + j, i * n + j + 1, (i + 1) * n + j, (i + 1) * n + j + 1
            tris += [(a, c, b), (b, c, d)]
    return pos, np.asarray(tris)


def theatre(root: Path, name: str = "TestTheatre", towns: str | None = None) -> Path:
    """A DCS install folder holding one synthetic theatre: two tiles of ground, one of them half sea, a road, and a second-set copy."""
    folder = root / "Mods" / "terrains" / name
    (folder / "surface").mkdir(parents=True)
    (folder / "map").mkdir(parents=True)
    pos, tri = grid(5, 100.0, lambda x, z: 10.0 + x * 0.1)
    kinds = np.full(len(tri), 1024)
    # Tile two: the first row of cells (x < 100) is under the sea.
    pos2 = pos.copy()
    pos2[:, 1] = np.where(pos2[:, 0] < 50, -20.0, 5.0)
    kinds2 = np.where(pos2[tri][:, :, 0].mean(1) < 100, 1, 1024)
    # A road along the first two vertex columns of tile one (z = 0 and 100).
    road_base = np.asarray([i * 5 + j for i in range(5) for j in range(2)])
    road_tri = []
    for i in range(4):
        a, b, c, d = 2 * i, 2 * i + 1, 2 * i + 2, 2 * i + 3
        road_tri += [(a, c, b), (b, c, d)]
    tiles = [
        TileSpec((1000.0, 0.0, 2000.0), pos, tri, kinds, [Overlay("Splatmap5.1", "Road", road_base, np.asarray(road_tri))]),
        TileSpec((1400.0, 0.0, 2000.0), pos2, tri, kinds2),
        TileSpec((1000.0, 0.0, 2000.0), pos, tri, None),
    ]
    write(folder / "surface" / f"{name}.surface5", tiles)
    if towns is not None:
        (folder / "map" / "towns.lua").write_text(towns, encoding="utf-8")
    return root
