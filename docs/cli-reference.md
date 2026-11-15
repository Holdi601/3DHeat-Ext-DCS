---
title: Command reference
nav_order: 90
---

# Command reference

Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.
The other pages explain each command step by step.

## `heat3d-dcs-maps`

```text
usage: heat3d-dcs-maps [-h] [--version] {list,level,towns,fit} ...

DCS World theatres into 3DHeat levels

positional arguments:
  {list,level,towns,fit}
    list                the theatres installed, and whether each can be read
    level               one theatre's ground and sea as a .glb level
    towns               a theatre's place names with DCS coordinates, as JSON
    fit                 a theatre's projection from a recording holding x, z, lat and
                        lon

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```

## `list`

```text
usage: heat3d-dcs-maps list [-h] [--dcs DCS]

options:
  -h, --help  show this help message and exit
  --dcs DCS   the DCS World folder (the one holding Mods\terrains)
```

## `level`

```text
usage: heat3d-dcs-maps level [-h] -o OUT [--dcs DCS] [--name NAME] [--cell CELL]
                             [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--seabed]
                             [--no-water] [--no-buildings] [--force]
                             [--projection LON0 FE FN]
                             theatre

positional arguments:
  theatre               the folder name under Mods\terrains, as list prints it

options:
  -h, --help            show this help message and exit
  -o, --out OUT         folder to write <name>.glb and <name>.json into
  --dcs DCS             the DCS World folder
  --name NAME           the level's name (default: the theatre's)
  --cell CELL           thin the mesh to this many metres (default 0: the game's own
                        triangles)
  --around LAT LON KM   only a square this many km either side of a point
  --bounds X0 Z0 X1 Z1  only this box, in DCS metres (x north, z east)
  --seabed              keep the sea floor as ground (default: left out)
  --no-water            leave out the flat sea
  --no-buildings        leave out the buildings of the theatre's scene
  --force               export a very large map whole at full detail
  --projection LON0 FE FN
                        the theatre's Transverse Mercator constants, for one this tool
                        does not know (see fit)
```

## `towns`

```text
usage: heat3d-dcs-maps towns [-h] [--dcs DCS] theatre

positional arguments:
  theatre

options:
  -h, --help  show this help message and exit
  --dcs DCS   the DCS World folder
```

## `fit`

```text
usage: heat3d-dcs-maps fit [-h] recording

positional arguments:
  recording   .parquet, .jsonl or .csv with columns lat, lon, x, z (DCS metres)

options:
  -h, --help  show this help message and exit
```

## Output

### Ground classes

The colour each class is drawn with (Captured colour in the viewer).

| Class | Colour (sRGB) |
|---|---|
| `land` | `#a0967c` |
| `forest` | `#49683a` |
| `field` | `#99a560` |
| `rock` | `#8c877f` |
| `beach` | `#dbcc9e` |
| `water` | `#3d72b7` |
| `town` | `#bc664f` |
| `rail` | `#604c42` |
| `road` | `#474747` |
| `runway` | `#191919` |
| `seabed` | `#546d87` |

### `<name>.glb` parts

Parts of the test level (each named `<part>:<Level>`): `ground`, `water` (a theatre whose scene has buildings adds `structure`).

### `<name>.json`

Top-level keys: `tool`, `version`, `written`, `theatre`, `level`, `source`, `coordinates`, `projection`, `bounds`, `bounds_latlon`, `region`, `cell`, `seabed`, `tiles`, `triangles`, `classes`, `colours`, `towns_on_land`, `towns`, `airfields`, `buildings`, `glb_bytes`, `seconds`.
