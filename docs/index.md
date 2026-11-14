---
title: Home
nav_order: 1
---

# 3DHeat DCS

3DHeat DCS turns the ground of a **DCS World theatre** into a 3D level for the
[3DHeat](https://github.com/Holdi601/3DHeat) viewer
([documentation](https://holdi601.github.io/3DHeat/)), read from **your own
install**: the terrain, the coast, and the airfields, roads, railways, towns
and buildings of the period the theatre shows.

What it is useful for:

- **Flights on the game's own map.** The 3DHeat world backdrop draws today's
  earth from open data; this draws the theatre as DCS draws it.
- **No placement step.** The level is in DCS's own world metres, so telemetry
  in DCS metres (the 3DHeat Watcher's DCS hook writes exactly that) lands on
  it with the viewer's defaults.
- **Latitude and longitude.** Every level carries its projection, its corners
  and its towns in both frames.

![From a DCS install to a 3DHeat level](assets/img/flow.svg)

## Quick start

```bash
pip install -e .                                   # installs the heat3d-dcs-maps command
heat3d-dcs-maps list                               # the theatres installed, and whether each can be read
heat3d-dcs-maps level <theatre> -o levels          # a whole (small) theatre
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name <name>   # 12 km either side of a point
```

Then load `levels/<name>.glb` in the viewer's Level panel
([Levels](https://holdi601.github.io/3DHeat/levels.html)).

The levels it writes are built from the game's data: they stay **on your
machine**, to view, not to share or publish ([Terms](terms.md)).

## Pages

| Page | What it covers |
|---|---|
| [Finding theatres: list](list.md) | where the install is found, what `list` prints |
| [Building a level: level](level.md) | every option, regions, size, step by step |
| [The level files](output.md) | the `.glb` parts, the ground classes and their colours, the `.json`, the coordinates |
| [Place names: towns](towns.md) | a theatre's towns with DCS coordinates |
| [Projections: fit](fit.md) | finding a theatre's projection from a recording |
| [How the files are read](reading.md) | the formats, what was verified, what is not read |
| [Terms and licence](terms.md) | Eagle Dynamics' licence, and why this is a separate package |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Telemetry for these levels: the [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/)
  records DCS flights; the viewer's file formats, including its
  one-file-a-match container, are described in
  [One file a match (.3dheat)](https://holdi601.github.io/3DHeat/container.html).
