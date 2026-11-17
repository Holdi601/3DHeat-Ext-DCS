---
title: How the files are read
nav_order: 7
---

# How the files are read

Only `Mods/terrains/<theatre>/surface/*.surface5` (the ground mesh),
`Scenes/*.scn5` (where objects stand, and each model's box),
`AirfieldsTaxiways/*.rn4` and `map/towns.lua` (place names, read as text,
never run). Not the encrypted
`terrain.cfg.lua.pak.crypt`, not `manifest.bin`, nothing of the program.
For [`ranges`](ranges.md), also the `.lua` definitions of the modules and
asset packs (below).

The `.surface5` format is undocumented; the layout, as read from the files,
is written down in [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
In short: an index of tile records (a transform, bounds, and lists of typed
byte streams, each list followed by the shader and material it is drawn
with), then the raw data. It is neither compressed nor enciphered. The tile's
`Pbase` stream holds its vertices; the group drawn as `Land` holds the
triangles and a `TRITYPE` per triangle, whose lowest bit marks the sea; the
other groups are the overlays that give the classes above.

## Verified

- `list` read the index of every theatre installed (millions to tens of
  millions of ground vertices each), every sampled tile decoding to plausible
  metres.
- On regions of two theatres, the towns from `towns.lua` landed within metres
  of a ground vertex, on land, N of N; the highest ground matched the real
  summit to within ten metres; airfields, rivers, villages and roads showed in
  their classes. Both levels loaded in the viewer, with town markers in the
  same DCS metres sitting on the ground.
- On a scene region, the building placements landed on their ground; runway
  lights traced the game's runway, and wagons and wall segments lined up with
  the decoded heading, all of them.
- `tests/` builds `.surface5` files to the same layout, so no game data is
  kept here; `tests/test_real_install.py` runs on the install of the machine
  running the tests, and is skipped without one.

**Not checked:** the whole of a large theatre in one level (the size guard
above exists for a reason), and versions of DCS other than the one tried.

## The definitions read by `ranges`

The weapon, sensor and unit definitions are Lua tables. They are read by the
tool's own small reader ([`heat3d_ext_dcs/lua.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/lua.py)),
not by Lua: it reads tables, numbers, strings and arithmetic, follows names
and `dofile` inside the install, walks a function's body when it is called
and repeats a loop only over a table it knows. It opens no other files,
starts nothing and changes nothing. What it cannot know - a value from the
game's packed core database - stays unknown and is left out of the
catalogue. Checked on a full install: the stated ranges, angles and names of
the weapons, sensors and units came out as the files give them.

## Not read

- **Buildings as shapes** (the models are `.edm` in `Models/`): boxes only,
  on purpose. Their layout, and the scene's, is written down in
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); every theatre
  installed reads (two older theatres in a variant layout the reader knows
  too).
- Trees, lights and the other objects of the scene: read, not drawn.
- **The road network as a graph** (`roads/*.rn4`): not decoded.
- Textures, trees, the sea's waves, the terrain's own lower levels of detail.
