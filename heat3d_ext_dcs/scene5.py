"""
DCS World scenes: `Mods/terrains/<theatre>/Scenes/<name>.scn5`, every object a
theatre places on its ground - houses, hangars, bridges, trees, fences, lamps.

Eagle Dynamics documents none of this either. The layout below was read from
the files themselves (the data, never the program); it holds for every
theatre installed at the time of writing (all version 9), and starts with the
same header as the `.surface5` files:

    0x00  u32 2, u32 0x30
    0x08  u64 index length = where the data begins; every data offset counts from here
    0x20  u32 n, the type name `landscape5::Scene5File`, u32 version (9)
    ...   u32 m, then m model names (u32 length + text each): `home1_a_new`, `angar_a_new`, ...
    ...   u32 m, then m boxes, float32[6] each: the model's own bounds
          (min x y z, max x y z, metres; zero for a model it never places)
    ...   u32 k, then k render-group records (`HwInstancer5.2` and its
          defines, each ending `NODEFINITIONS` and u32 0xFFFFFFFF)
    ...   u32 0, u32 node count, then the nodes

A **node** is one patch of ground's placements of a few models:

    float64[16] transform (column-major; the translation is [12..14]; the
                rotation is always the identity), float32 (a radius),
    float32[6]  bounds in world metres (min x y z, max x y z),
    u32 0, u32 2, u32 instance count, u32 stream count (4),
    the streams, as in `.surface5`: u32 1, u32 n, name[n], u16 element type,
    u16 element size, u32 flags, u64 byte count, u32 offset (low), u16 offset (high),
    u32 0, u32 t, t model indices (the models the node places), ...

and its four streams hold one element per instance:

    P             float32 x, y, z in the node's frame (add the translation)
    TYPE_OPTIONS  u32: the low 16 bits are the model's index in the name list
    SEED_SCALE    u32: not needed here, not interpreted
    AXIS          six u16, each (v - 32768) / 32767: the model's x axis, then
                  its z axis, in world axes; y is z cross x (wagons on a
                  track line up with their x axis, every one checked)

Older scenes (Nevada, The Channel; still version 9) list five streams
instead: `TYPE` (u32, the model's index), `P`, `AXISX` (float32 x and z: the
model's x axis on the ground, scaled - only its direction is used), `SEED`
and `OPTIONS`. Lines of fence and wall segments line up with the axis on
both layouts (Nevada: 381 of 381 checked).

World metres are DCS's own: x north, y up, z east - the frame of the
`.surface5` ground and of the sim's export. An instance's y is the ground
under its origin.
"""

from __future__ import annotations

import re
import struct
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .surface5 import FormatError

TYPE_NAME = b"landscape5::Scene5File"

#: The position stream every node starts its list with.
_P_ENTRY = re.compile(re.escape(struct.pack("<II", 1, 1) + b"P" + struct.pack("<HH", 2, 12)))
#: The model stream older scenes list before `P`.
_TYPE_ENTRY = struct.pack("<II", 1, 4) + b"TYPE" + struct.pack("<HH", 4, 4)
#: Bytes of a node before its first stream entry: the transform, the radius, the bounds, four u32.
_HEAD = 128 + 4 + 24 + 16


@dataclass
class Node:
    translation: tuple[float, float, float]
    #: World metres: min x, y, z, max x, y, z.
    bounds: tuple[float, float, float, float, float, float]
    count: int
    #: Stream name -> (byte count, offset from the start of the data).
    streams: dict[str, tuple[int, int]]


@dataclass
class Instances:
    """Placements, one row each."""

    model: np.ndarray  # uint16 index into Scene5.models
    position: np.ndarray  # float64 n x 3, world metres
    x_axis: np.ndarray  # float32 n x 3, unit
    z_axis: np.ndarray  # float32 n x 3, unit

    def __len__(self) -> int:
        return len(self.model)


def _string(buf: bytes, at: int) -> tuple[str, int]:
    n = struct.unpack_from("<I", buf, at)[0]
    if n > 4096:
        raise FormatError(f"a name {n} bytes long at {at}")
    return buf[at + 4 : at + 4 + n].decode("latin-1"), at + 4 + n


def _stream(buf: bytes, at: int) -> tuple[str, int, int, int]:
    if struct.unpack_from("<I", buf, at)[0] != 1:
        raise FormatError(f"no stream entry at {at}")
    name, at = _string(buf, at + 4)
    _kind, _size, _flags, count, low, high = struct.unpack_from("<HHIQIH", buf, at)
    return name, count, low | (high << 32), at + 22


class Scene5:
    """A .scn5 file: its models and their boxes, its nodes, and their placements on demand."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self._f = open(self.path, "rb")
        head = self._f.read(0x40)
        if len(head) < 0x40 or struct.unpack_from("<I", head, 0)[0] != 2:
            raise FormatError(f"{self.path.name} is not a DCS scene file")
        self.data_start = struct.unpack_from("<Q", head, 8)[0]
        self.size = self.path.stat().st_size
        if not 0x40 < self.data_start <= self.size:
            raise FormatError(f"{self.path.name}: the index length {self.data_start} does not fit the file")
        self._f.seek(0)
        index = self._f.read(self.data_start)
        n = struct.unpack_from("<I", index, 0x20)[0]
        if index[0x24 : 0x24 + n] != TYPE_NAME:
            raise FormatError(f"{self.path.name} is {index[0x24:0x24 + n]!r}, not {TYPE_NAME.decode()}")
        at = 0x24 + n
        self.version, count = struct.unpack_from("<II", index, at)
        at += 8
        self.models: list[str] = []
        for _ in range(count):
            name, at = _string(index, at)
            self.models.append(name)
        if struct.unpack_from("<I", index, at)[0] != count:
            raise FormatError(f"{self.path.name}: {count} model names but a box list of another length")
        #: float32 m x 6 per model: min x, y, z, max x, y, z in its own frame.
        self.boxes = np.frombuffer(index, "<f4", count * 6, at + 4).reshape(count, 6).astype(np.float64)
        self.nodes = self._nodes(index, at + 4 + count * 24)

    def _nodes(self, index: bytes, after_boxes: int) -> list[Node]:
        out = []
        for m in _P_ENTRY.finditer(index, after_boxes):
            p = m.start()
            # Older scenes (Nevada, The Channel) list a `TYPE` stream first.
            first = p - 34 if index[p - 34 : p - 34 + len(_TYPE_ENTRY)] == _TYPE_ENTRY else p
            if first < after_boxes + _HEAD:
                continue
            t = struct.unpack_from("<16d", index, first - _HEAD)
            bounds = struct.unpack_from("<6f", index, first - 40)
            n, k = struct.unpack_from("<II", index, first - 8)
            if t[0] != 1.0 or t[5] != 1.0 or t[10] != 1.0 or t[15] != 1.0 or k > 16:
                raise FormatError(f"{self.path.name}: a node at {p} is not laid out as this reader knows")
            streams = {}
            at = first
            for _ in range(k):
                name, nbytes, off, at = _stream(index, at)
                streams[name] = (nbytes, off)
            model = "TYPE_OPTIONS" if "TYPE_OPTIONS" in streams else "TYPE"
            for name, size in (("P", 12), (model, 4)):
                if streams.get(name, (-1,))[0] != n * size:
                    raise FormatError(f"{self.path.name}: node at {p}: {name} does not hold {n} instances")
            out.append(Node((t[12], t[13], t[14]), bounds, n, streams))
        if not out:
            raise FormatError(f"{self.path.name}: no placements found")
        return out

    def close(self) -> None:
        self._f.close()

    def __enter__(self) -> "Scene5":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    @property
    def instance_count(self) -> int:
        return sum(n.count for n in self.nodes)

    def _read(self, nbytes: int, offset: int, dtype: str) -> np.ndarray:
        if offset + nbytes > self.size - self.data_start:
            raise FormatError(f"{self.path.name}: a stream runs past the end of the file")
        self._f.seek(self.data_start + offset)
        return np.frombuffer(self._f.read(nbytes), dtype)

    def instances(self, touches=None, models: set[int] | None = None) -> Instances:
        """
        Placements of the nodes whose bounds `touches(bounds)` accepts (all
        when None), of the models in `models` (all when None).
        """
        mods, pos, xs, zs = [], [], [], []
        for node in self.nodes:
            if touches is not None and not touches(node.bounds):
                continue
            n = node.count
            model = node.streams.get("TYPE_OPTIONS") or node.streams["TYPE"]
            mod = (self._read(*model, "<u4") & 0xFFFF).astype(np.uint16)
            keep = np.ones(n, bool) if models is None else np.isin(mod, list(models))
            if not keep.any():
                continue
            if int(mod.max()) >= len(self.models):
                raise FormatError(f"{self.path.name}: a placement names a model the file does not list")
            p = self._read(*node.streams["P"], "<f4").reshape(n, 3)[keep].astype(np.float64) + node.translation
            if "AXIS" in node.streams:
                ax = (self._read(*node.streams["AXIS"], "<u2").reshape(n, 6)[keep].astype(np.float32) - 32768.0) / 32767.0
                x_axis, z_axis = _unit(ax[:, :3]), _unit(ax[:, 3:])
            elif node.streams.get("AXISX", (0,))[0] == n * 8:
                # Older scenes: the x axis on the ground, x and z, float32 (scaled; only its direction is used).
                a = self._read(*node.streams["AXISX"], "<f4").reshape(n, 2)[keep]
                x_axis = _unit(np.column_stack([a[:, 0], np.zeros(len(a)), a[:, 1]]).astype(np.float32))
                z_axis = np.column_stack([-x_axis[:, 2], np.zeros(len(a)), x_axis[:, 0]]).astype(np.float32)
            else:
                raise FormatError(f"{self.path.name}: a node without a known axis stream")
            mods.append(mod[keep])
            pos.append(p)
            xs.append(x_axis)
            zs.append(z_axis)
        if not mods:
            e = np.zeros((0, 3))
            return Instances(np.zeros(0, np.uint16), e, e.astype(np.float32), e.astype(np.float32))
        return Instances(np.concatenate(mods), np.concatenate(pos), np.concatenate(xs), np.concatenate(zs))


def _unit(v: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(v, axis=1, keepdims=True)
    return v / np.where(n > 0, n, 1)
