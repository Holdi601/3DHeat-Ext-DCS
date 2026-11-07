"""
Just enough binary glTF for a level: one node per part, named by the 3DHeat
contract (`ground:<Level>`, `water:<Level>`), each a mesh of indexed triangle
primitives with float32 POSITION and, where given, a COLOR_0 the viewer's
*Captured colour* shows. No normals: the viewer computes them.
"""

from __future__ import annotations

import json
import struct
from pathlib import Path

import numpy as np

from .level import Primitive


def write(path: str | Path, parts: list[tuple[str, list[Primitive]]], generator: str = "heat3d_ext_dcs") -> int:
    """Write the .glb; returns its size in bytes."""
    blob = bytearray()
    views: list[dict] = []
    accessors: list[dict] = []
    meshes: list[dict] = []
    nodes: list[dict] = []

    def add(array: np.ndarray, target: int, kind: str, component: int, bounds: bool = False) -> int:
        blob.extend(b"\0" * (-len(blob) % 4))
        raw = np.ascontiguousarray(array).tobytes()
        views.append({"buffer": 0, "byteOffset": len(blob), "byteLength": len(raw), "target": target})
        blob.extend(raw)
        acc = {"bufferView": len(views) - 1, "componentType": component, "count": int(len(array)), "type": kind}
        if bounds:
            acc["min"] = [float(v) for v in array.min(axis=0)]
            acc["max"] = [float(v) for v in array.max(axis=0)]
        accessors.append(acc)
        return len(accessors) - 1

    for name, prims in parts:
        out = []
        for p in prims:
            if not len(p.triangles):
                continue
            pos = p.positions.astype("<f4", copy=False)
            attributes = {"POSITION": add(pos, 34962, "VEC3", 5126, bounds=True)}
            if p.colour is not None:
                colour = np.broadcast_to(np.asarray(p.colour, "<f4"), (len(pos), 3))
                attributes["COLOR_0"] = add(colour, 34962, "VEC3", 5126)
            index = p.triangles.astype("<u4", copy=False).reshape(-1)
            prim = {"attributes": attributes, "indices": add(index, 34963, "SCALAR", 5125), "mode": 4}
            if p.label:
                prim["extras"] = {"class": p.label}
            out.append(prim)
        if not out:
            continue
        meshes.append({"name": name, "primitives": out})
        nodes.append({"name": name, "mesh": len(meshes) - 1})

    doc = {
        "asset": {"version": "2.0", "generator": generator},
        "scene": 0,
        "scenes": [{"nodes": list(range(len(nodes)))}],
        "nodes": nodes,
        "meshes": meshes,
        "accessors": accessors,
        "bufferViews": views,
        "buffers": [{"byteLength": len(blob)}],
    }
    text = json.dumps(doc, separators=(",", ":")).encode()
    text += b" " * (-len(text) % 4)
    blob.extend(b"\0" * (-len(blob) % 4))
    total = 12 + 8 + len(text) + 8 + len(blob)
    with open(path, "wb") as f:
        f.write(struct.pack("<III", 0x46546C67, 2, total))
        f.write(struct.pack("<II", len(text), 0x4E4F534A))
        f.write(text)
        f.write(struct.pack("<II", len(blob), 0x004E4942))
        f.write(blob)
    return total


def read(path: str | Path) -> tuple[dict, bytes]:
    """The JSON document and binary chunk of a .glb (for tests and checks)."""
    data = Path(path).read_bytes()
    magic, _, length = struct.unpack_from("<III", data, 0)
    if magic != 0x46546C67:
        raise ValueError(f"{path} is not a .glb")
    doc, blob, at = None, b"", 12
    while at < length:
        size, kind = struct.unpack_from("<II", data, at)
        chunk = data[at + 8 : at + 8 + size]
        if kind == 0x4E4F534A:
            doc = json.loads(chunk)
        elif kind == 0x004E4942:
            blob = chunk
        at += 8 + size
    if doc is None:
        raise ValueError(f"{path} has no JSON chunk")
    return doc, blob


def accessor(doc: dict, blob: bytes, index: int) -> np.ndarray:
    a = doc["accessors"][index]
    v = doc["bufferViews"][a["bufferView"]]
    dtype = {5126: "<f4", 5125: "<u4"}[a["componentType"]]
    width = {"SCALAR": 1, "VEC3": 3}[a["type"]]
    arr = np.frombuffer(blob, dtype, count=a["count"] * width, offset=v.get("byteOffset", 0) + a.get("byteOffset", 0))
    return arr.reshape(a["count"], width) if width > 1 else arr
