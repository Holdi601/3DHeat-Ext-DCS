"""
DCS World terrain surfaces: `Mods/terrains/<theatre>/surface/<name>.surface5`,
the ground mesh every theatre since terrain version 5 ships in.

Eagle Dynamics documents none of this. What follows was read from the files
themselves (the data, never the program), and holds for every theatre
installed at the time of writing: Afghanistan, Caucasus, Falklands, Germany
Cold War, Iraq, Kola, Mariana Islands, Marianas WWII, Nevada, Normandy 2,
Persian Gulf, Sinai, Syria, The Channel. The file is not compressed and not
enciphered.

    0x00  u32 2, u32 0x30
    0x08  u64 index length = where the data begins; every data offset counts from here
    0x20  u32 n, the type name `landscape5::Surface5File`, u32 version (5)
    ...   the index: one record per tile, then the data

A **tile record** begins with

    u32 7, float32[16] transform (column-major; the translation is [12..14]),
    float32[6] bounds in the tile's own frame (min x y z, max x y z)

and then lists of **streams**, each list followed by the shader and material
it is drawn with (`Surface5.0` / `Land`, `Splatmap5.1` / `Road`,
`Sea5.1` / `Sea`, ...: a u32-length string each). A stream entry:

    u32 1, u32 n, name[n], u16 element type, u16 element size, u32 flags,
    u64 byte count, u32 offset (low), u16 offset (high: offsets are 48-bit)

Counts and offsets are in bytes. Element type 2 is float32 (size 12: three of
them), 0 a float32, 4 a u32, 6 three u32 (a triangle).

The tile's vertices are the list that starts with `Pbase` (float32 x, y, z in
the tile's frame; add the translation for world metres) - followed by
`nextLodIndex`, `Nbase`, `maxEdge`, `depth`. The ground itself is the group
drawn as `Land` that carries `TRITYPE` (a u32 per triangle) and `TRI` (three
u32 vertex indices). Other groups are overlays drawn over the same vertices:
their `TRI` index a `baseIndex` list, which names the tile vertex.

There are two sets of tile records covering the same ground with the same
vertices: one whose ground group has `TRITYPE`, and a second, cut into more
tiles, without it. This reader uses the first; the second adds nothing a
level needs.

`TRITYPE` bit 0 marks a triangle under the sea (its height is the sea floor).
The other bits were not needed and are not interpreted.

Coordinates are DCS's own world metres: x north, y up, z east - the same frame
the sim's export (`LoGetSelfData().Position`) and its mission scripting use.
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

TYPE_NAME = b"landscape5::Surface5File"

#: A record's start: u32 7 and a transform whose rotation is the identity.
#: Terrain tiles are only ever translated; the count is checked against the
#: vertex lists, so a tile that was not would be noticed, not skipped.
_RECORD = re.compile(
    re.escape(
        struct.pack("<I", 7)
        + struct.pack("<12f", 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0)
    )
)
_ENTRY = re.compile(rb"\x01\x00\x00\x00([\x02-\x30])\x00\x00\x00([A-Za-z_][A-Za-z0-9_]{1,47})")
_SHADER = re.compile(rb"([\x03-\x30])\x00\x00\x00([A-Za-z]+[0-9]\.[0-9])([\x01-\x30])\x00\x00\x00")
_VERTEX_LIST = b"\x01\x00\x00\x00\x05\x00\x00\x00Pbase"
#: The streams this reader uses; every other entry is passed over.
_WANTED = {"TRITYPE", "TRI", "baseIndex", "Pbase"}


class FormatError(ValueError):
    """The file is not laid out the way this reader knows."""


@dataclass
class Stream:
    name: str
    kind: int
    size: int
    count: int  # bytes
    offset: int  # bytes from the start of the data


@dataclass
class Group:
    shader: str
    material: str
    streams: dict[str, Stream] = field(default_factory=dict)


@dataclass
class Tile:
    index: int
    translation: tuple[float, float, float]
    #: In the tile's own frame: min x, y, z, max x, y, z.
    bounds: tuple[float, float, float, float, float, float]
    vertices: Stream
    groups: list[Group]

    @property
    def ground(self) -> Group | None:
        """The group drawn as the ground, when this tile is one of the set that carries it."""
        for g in self.groups:
            if "TRITYPE" in g.streams and "TRI" in g.streams:
                return g
        return None

    def world_bounds(self) -> tuple[float, float, float, float, float, float]:
        x, y, z = self.translation
        b = self.bounds
        return (b[0] + x, b[1] + y, b[2] + z, b[3] + x, b[4] + y, b[5] + z)

    @property
    def vertex_count(self) -> int:
        return self.vertices.count // 12


def _entry(seg: bytes, m: re.Match) -> Stream | None:
    n = m.group(1)[0]
    if len(m.group(2)) < n:
        return None
    name = m.group(2)[:n].decode()
    at = m.start() + 8 + n
    if at + 22 > len(seg):
        return None
    kind, size, _flags, count, low, high = struct.unpack_from("<HHIQIH", seg, at)
    return Stream(name, kind, size, count, low | (high << 32))


def _shaders(seg: bytes) -> list[tuple[int, str, str]]:
    out = []
    for m in _SHADER.finditer(seg):
        if m.group(1)[0] != len(m.group(2)):
            continue
        n = m.group(3)[0]
        material = seg[m.end() : m.end() + n]
        if len(material) == n and re.fullmatch(rb"[A-Za-z0-9_ ]+", material):
            out.append((m.start(), m.group(2).decode(), material.decode()))
    return out


def parse_record(seg: bytes, index: int) -> Tile:
    """One tile record (`seg` starts at its u32 7)."""
    t = struct.unpack_from("<16f", seg, 4)
    bounds = struct.unpack_from("<6f", seg, 68)
    vertex_at = seg.find(_VERTEX_LIST)
    if vertex_at < 0:
        raise FormatError(f"tile {index} has no vertex list")
    vm = _ENTRY.match(seg, vertex_at)
    vertices = _entry(seg, vm) if vm else None
    if vertices is None or vertices.kind != 2 or vertices.size != 12 or vertices.count % 12:
        raise FormatError(f"tile {index}: vertices are not float32 x, y, z")
    shaders = _shaders(seg[:vertex_at])
    groups: dict[int, Group] = {}
    for m in _ENTRY.finditer(seg, 0, vertex_at):
        s = _entry(seg, m)
        if s is None or s.name not in _WANTED:
            continue
        follow = next((sh for sh in shaders if sh[0] > m.start()), None)
        if follow is None:
            continue
        g = groups.setdefault(follow[0], Group(follow[1], follow[2]))
        g.streams.setdefault(s.name, s)
    return Tile(index, (t[12], t[13], t[14]), bounds, vertices, [groups[k] for k in sorted(groups)])


class Surface5:
    """A .surface5 file: its tiles, and their vertices and triangles on demand."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._f = open(self.path, "rb")
        head = self._f.read(0x60)
        if len(head) < 0x40 or struct.unpack_from("<I", head, 0)[0] != 2:
            raise FormatError(f"{self.path.name} is not a DCS terrain file")
        self.data_start = struct.unpack_from("<Q", head, 8)[0]
        n = struct.unpack_from("<I", head, 0x20)[0]
        if head[0x24 : 0x24 + n] != TYPE_NAME:
            raise FormatError(f"{self.path.name} is {head[0x24:0x24 + n]!r}, not {TYPE_NAME.decode()}")
        self.version = struct.unpack_from("<I", head, 0x24 + n)[0]
        self.size = self.path.stat().st_size
        if not 0x40 < self.data_start <= self.size:
            raise FormatError(f"{self.path.name}: the index length {self.data_start} does not fit the file")
        self._tiles: list[Tile] | None = None

    def close(self) -> None:
        self._f.close()

    def __enter__(self) -> "Surface5":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    @property
    def tiles(self) -> list[Tile]:
        """Every tile record, both sets."""
        if self._tiles is None:
            self._f.seek(0)
            index = self._f.read(self.data_start)
            starts = [m.start() for m in _RECORD.finditer(index)]
            lists = index.count(_VERTEX_LIST)
            if not starts or len(starts) != lists:
                raise FormatError(
                    f"{self.path.name}: {lists} vertex lists but {len(starts)} tile transforms - "
                    "a layout this reader does not know"
                )
            starts.append(len(index))
            self._tiles = [parse_record(index[a:b], i) for i, (a, b) in enumerate(zip(starts, starts[1:]))]
        return self._tiles

    @property
    def ground_tiles(self) -> list[Tile]:
        """The set of tiles that carries the ground (`TRITYPE`)."""
        out = [t for t in self.tiles if t.ground is not None]
        if not out:
            raise FormatError(f"{self.path.name}: no tile carries a ground group with TRITYPE")
        return out

    def read(self, s: Stream, dtype: str) -> np.ndarray:
        if s.offset + s.count > self.size - self.data_start:
            raise FormatError(f"{self.path.name}: stream {s.name} runs past the end of the file")
        self._f.seek(self.data_start + s.offset)
        raw = self._f.read(s.count)
        item = np.dtype(dtype).itemsize
        return np.frombuffer(raw[: len(raw) // item * item], dtype)

    def positions(self, tile: Tile) -> np.ndarray:
        """The tile's vertices in world metres (float64, n x 3: x north, y up, z east)."""
        p = self.read(tile.vertices, "<f4").reshape(-1, 3).astype(np.float64)
        p += np.asarray(tile.translation)
        return p

    def ground(self, tile: Tile) -> tuple[np.ndarray, np.ndarray]:
        """The ground's triangles (m x 3 vertex indices) and their TRITYPE."""
        g = tile.ground
        if g is None:
            raise FormatError(f"tile {tile.index} carries no ground")
        tri = self.read(g.streams["TRI"], "<u4").reshape(-1, 3)
        kinds = self.read(g.streams["TRITYPE"], "<u4")
        if len(kinds) != len(tri):
            raise FormatError(f"tile {tile.index}: {len(tri)} triangles but {len(kinds)} TRITYPE")
        if len(tri) and int(tri.max()) >= tile.vertex_count:
            raise FormatError(f"tile {tile.index}: a triangle names a vertex the tile does not have")
        return tri, kinds

    def overlay(self, tile: Tile, group: Group) -> np.ndarray | None:
        """An overlay's triangles as tile vertex indices, or None when it is not drawn over the tile's vertices."""
        if "TRI" not in group.streams or "baseIndex" not in group.streams:
            return None
        tri = self.read(group.streams["TRI"], "<u4").reshape(-1, 3)
        base = self.read(group.streams["baseIndex"], "<u4")
        if not len(tri):
            return tri
        if int(tri.max()) >= len(base) or (len(base) and int(base.max()) >= tile.vertex_count):
            return None
        return base[tri]
