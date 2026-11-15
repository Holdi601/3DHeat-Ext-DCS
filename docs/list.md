---
title: "Finding theatres: list"
nav_order: 2
---

# Finding theatres: `list`

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

New to the command line? Read [Before you start](before-you-start.md) first.

1. Install once: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, open
   a terminal in that folder and run `python -m pip install -e .` (Python 3.10
   or later; it brings numpy, and pyarrow for `fit` on a `.parquet`).
2. Run `heat3d-dcs-maps list`.
3. Each installed theatre prints one line: its folder name (the name the other
   commands take), the size of its ground file, its tiles and vertices,
   whether its latitude/longitude projection is known, and whether it reads.
   You should see `readable` at the end of each line.

![list on a synthetic install](assets/img/list.svg)

The picture is a run on an install the tests build (`tests/synth.py`), not on
the game.

## Where the install is found

`--dcs <folder>` (the folder holding `Mods\terrains`) or the `DCS_PATH`
environment variable; otherwise the registry, the Steam libraries and the
usual folders are searched.

| Option | Does |
|---|---|
| `--dcs FOLDER` | the DCS World folder, the one holding `Mods\terrains` |

Exit status: 0 done, 2 no install or no theatre found.
