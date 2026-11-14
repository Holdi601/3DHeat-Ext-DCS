---
title: "Place names: towns"
nav_order: 5
---

# Place names: `towns`

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Prints the theatre's place names, from its `map/towns.lua` (read as text,
never run), as JSON: each town's name, its latitude and longitude, and its
DCS `x` (north) and `z` (east) in metres, through the theatre's projection.

1. Find the theatre's folder name with [`list`](list.md).
2. Run `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Use the `x`/`z` to label a level, or to check a recording's positions.

![towns on a synthetic install](assets/img/towns.svg)

| Option | Does |
|---|---|
| `theatre` | the folder name under `Mods\terrains` |
| `--dcs FOLDER` | the DCS World folder |

The towns inside a level's region are also in its `<name>.json`, with the
height of the ground under each ([The level files](output.md)).
