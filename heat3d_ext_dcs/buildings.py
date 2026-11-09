"""
A theatre's buildings as plain boxes: the game's own placements (scene5),
each drawn as its model's box - footprint, height, heading - and nothing of
the model itself. No mesh or texture of the game is copied.

Which models are buildings is told by name and by box. Trees, shrubs,
lamps, runway lights, wires, fences, walls, signs, vehicles, wagons, boats,
cranes, masts, pylons and bridges are not: a box would misdraw them, and
most stand in thousands along every road. What is left - houses, flats,
sheds, hangars, factories, towers, terminals - is drawn when its box is at
least 2.5 m high and 2.5 m across both ways.

A model's box reaches below its origin (foundations, for slopes); the box is
drawn from that depth, at most 3 m, to its top, so a building on a slope does
not float.
"""

from __future__ import annotations

import re

import numpy as np

from .level import Primitive
from .scene5 import Instances

#: Model names that are not buildings (substring, lower case).
NOT_BUILDINGS = re.compile(
    r"tree|shrub|spruce|beech|ash|cypress|poplar|mesquite|palm|oak|fir\b|_fir|pine|bush|elnya"
    r"|light|lamp|spot|omni|papi|pole|stolb|wire|tros|fence|ograd|wall|vorota|gate|flag|zont|canopy"
    r"|course|block|_left|_right|_frwd|sign|table|barrel|box|ladder|conditioner|ventilation|antenna|anten"
    r"|mast|vyshka$|^vyshka_|kran|crane|derrick|neftevyshka|tele_bash|radar|lokator|localizer|beacon|tacan"
    r"|most|mst|bridge|tunnel|perehod|prichal|volnorez|helipad|platform|truboprovod|football|tennis"
    r"|bascetball|stadion|wagon|platforma|teplowoz|elektrowoz|boat|barge|yastrebow|dok_s|vessel"
    r"|gaz|vaz|kamaz|ural|zil|ikarus|liaz|laz-|trolebus|atz|btr|bmp|rls|rsp|prw|mi-8|an-2|il76|mig|su-|tu-"
    r"|monument|smoke|_crush|_crash"
)

MIN_HEIGHT = 2.5
MIN_SIDE = 2.5
#: Deepest a box is drawn below the model's origin, metres.
MAX_FOOTING = 3.0

KINDS = ("house", "block", "industrial", "airfield", "tower", "other")
KIND_COLOURS = {
    "house": (0.80, 0.72, 0.62),
    "block": (0.72, 0.70, 0.68),
    "industrial": (0.62, 0.62, 0.60),
    "airfield": (0.56, 0.60, 0.56),
    "tower": (0.70, 0.66, 0.60),
    "other": (0.76, 0.70, 0.64),
}


def kind_of(name: str, box: np.ndarray) -> str | None:
    """The building kind of a model, or None when it is not drawn as one."""
    n = name.lower()
    if NOT_BUILDINGS.search(n):
        return None
    w = box[3] - box[0]
    d = box[5] - box[2]
    h = box[4]
    if not (h >= MIN_HEIGHT and w >= MIN_SIDE and d >= MIN_SIDE and box[1] <= 0.5):
        return None
    if re.search(r"angar|hangar|hungar|airbase|airport|terminal|kdp|aviashtab|afb|meteo|babushara", n):
        return "airfield"
    if re.search(r"ceh|sklad|tech|tec_|ferma|kotelnaya|bak|gradir|tank|tuapse|zavod|garag|garage|elevator", n):
        return "industrial"
    if h > 2.5 * max(w, d) or re.search(r"bashnja|majak|mechet_hight|wodokachka|tower", n):
        return "tower"
    if h >= 12 or re.search(r"home[3-9]|home1[0-9]|home5|hotel|korpus|uniwersam|school|polyklinika", n):
        return "block"
    if re.search(r"home|dom|domik|s[1-4]_|kam_h|saray|hozdomik", n):
        return "house"
    return "other"


def model_kinds(models: list[str], boxes: np.ndarray) -> dict[int, str]:
    """Model index -> kind, for every model drawn as a building."""
    out = {}
    for i, (name, box) in enumerate(zip(models, boxes)):
        k = kind_of(name, box)
        if k is not None:
            out[i] = k
    return out


def boxes(inst: Instances, model_boxes: np.ndarray) -> np.ndarray:
    """
    Per placement: x, z of the footprint's middle, base y, top y, half
    lengths along the model's x and z, and its x axis's heading (x, z) on
    the ground - float64 n x 8. The model's own box decides the size; a box
    off its origin moves the footprint with it.
    """
    b = model_boxes[inst.model.astype(np.int64)]
    cx = (b[:, 0] + b[:, 3]) / 2
    cz = (b[:, 2] + b[:, 5]) / 2
    # Heading on the ground: the x axis flattened; z is square to it.
    ax = inst.x_axis[:, [0, 2]].astype(np.float64)
    ax /= np.maximum(np.linalg.norm(ax, axis=1, keepdims=True), 1e-9)
    zx, zz = -ax[:, 1], ax[:, 0]
    x = inst.position[:, 0] + ax[:, 0] * cx + zx * cz
    z = inst.position[:, 2] + ax[:, 1] * cx + zz * cz
    y = inst.position[:, 1]
    base = y + np.maximum(b[:, 1], -MAX_FOOTING)
    top = y + b[:, 4]
    return np.column_stack([x, z, base, top, (b[:, 3] - b[:, 0]) / 2, (b[:, 5] - b[:, 2]) / 2, ax[:, 0], ax[:, 1]])


#: A box's corners (sign along the model's x, along its z; bottom 0-3, top 4-7) and its faces.
_CORNERS = np.array([(-1, -1), (1, -1), (1, 1), (-1, 1)], np.float64)
_FACES = np.array(
    [
        (4, 5, 6), (4, 6, 7),  # roof
        (0, 1, 5), (0, 5, 4),
        (1, 2, 6), (1, 6, 5),
        (2, 3, 7), (2, 7, 6),
        (3, 0, 4), (3, 4, 7),
    ],
    np.uint32,
)


def mesh(rows: np.ndarray, colour: tuple[float, float, float], label: str) -> Primitive:
    """Boxes (rows as `boxes` gives them) as one primitive: walls and a roof, no floor."""
    n = len(rows)
    x, z, base, top, hx, hz, ux, uz = rows.T
    vx, vz = -uz, ux
    pos = np.empty((n, 8, 3))
    for i, (sx, sz) in enumerate(_CORNERS):
        px = x + ux * sx * hx + vx * sz * hz
        pz = z + uz * sx * hx + vz * sz * hz
        pos[:, i] = np.column_stack([px, base, pz])
        pos[:, i + 4] = np.column_stack([px, top, pz])
    # _FACES runs clockwise seen from outside; glTF wants counter-clockwise.
    faces = _FACES[:, [0, 2, 1]]
    tri = (faces[None, :, :] + (np.arange(n, dtype=np.uint32) * 8)[:, None, None]).reshape(-1, 3)
    return Primitive(pos.reshape(-1, 3).astype(np.float32), tri.astype(np.uint32), colour, label)
