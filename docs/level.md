---
title: "Building a level: level"
nav_order: 3
---

# Building a level: `level`

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Step by step

1. Find the theatre's folder name with [`list`](list.md).
2. For a small theatre, build it whole: `heat3d-dcs-maps level <theatre> -o levels`.
3. For a large one, pick a region: `--around <lat> <lon> <km>` (a square that
   many km either side of a point) or `--bounds X0 Z0 X1 Z1` in DCS metres.
   Name it with `--name`.
4. The command prints the tiles as it reads them, the triangle count, the
   file written, and how many of the theatre's towns land on the ground - a
   check of the projection that should read "N of N".
5. Load `<folder>/<name>.glb` in the viewer's Level panel and turn on
   **Captured colour** to see the ground classes.

![level on a synthetic install](assets/img/level.svg)

A region of the same synthetic theatre, by DCS metres:

![level with --bounds and --name](assets/img/level-bounds.svg)

## Options

| Option | Default | Does |
|---|---|---|
| `theatre` | - | the folder name under `Mods\terrains`, as `list` prints it (any case) |
| `-o`, `--out` | required | the folder to write `<name>.glb` and `<name>.json` into |
| `--dcs FOLDER` | found | the DCS World folder ([where it is found](list.md#where-the-install-is-found)) |
| `--name NAME` | the theatre's | the level's name, and its files' |
| `--around LAT LON KM` | - | only a square this many km either side of a point |
| `--bounds X0 Z0 X1 Z1` | - | only this box, in DCS metres (x north, z east) |
| `--cell M` | `0` | thin the mesh: every vertex within *M* metres becomes one (0: the game's own triangles) |
| `--seabed` | off | keep the sea floor as ground (by default it is left out) |
| `--no-water` | off | leave out the flat sea |
| `--no-buildings` | off | leave out the buildings of the theatre's scene |
| `--force` | off | export a very large map whole at full detail |
| `--projection LON0 FE FN` | the theatre's | Transverse Mercator constants for a theatre this tool does not know ([fit](fit.md)) |

## Size

The game's mesh is adaptive - open sea in triangles kilometres across, coasts
and roads in a few metres. A small theatre is a few million triangles; the big
ones are 35 to 90 million vertices. Above 30 million vertices to read, `level`
stops (exit status 1) and asks for a region, a thinner mesh (`--cell 50`) or
`--force`.

Exit status: 0 done; 1 failed or too large; 2 the install or the theatre was
not found (the theatres found are listed).

## Examples

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

What is in the files: [The level files](output.md).
