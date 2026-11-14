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

The `.surface5` format is undocumented; the layout, as read from the files,
is written down in [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
In short: an index of tile records (a transform, bounds, and lists of typed
byte streams, each list followed by the shader and material it is drawn
with), then the raw data. It is neither compressed nor enciphered. The tile's
`Pbase` stream holds its vertices; the group drawn as `Land` holds the
triangles and a `TRITYPE` per triangle, whose lowest bit marks the sea; the
other groups are the overlays that give the classes above.

## Verified

On the theatres installed on 2026-11-07 (DCS 2.9.30.28738, standalone):

- `list` reads the index of all fourteen: Afghanistan, Caucasus, Falklands,
  Germany Cold War, Iraq, Kola, Mariana Islands, Marianas WWII, Nevada,
  Normandy 2, Persian Gulf, Sinai, Syria, The Channel - 5.6 to 91 million
  ground vertices each, every sampled tile decoding to plausible metres.
- Marianas WWII, Saipan and Tinian (28 km square): 1.58 million triangles.
  The 1944 towns from `towns.lua` land 3 to 12 m from a ground vertex, at
  9 to 63 m above the sea; 6 of 6 on land. The highest ground of the theatre
  is 973 m (Agrihan's summit is 965 m). Isely Field and the Tinian strips show
  as runway.
- Normandy 2, Caen (24 km square): 508,000 triangles, 64 of 64 towns on
  land (Caen at 3 m on the Orne, Ouistreham 8 m on the coast); Carpiquet
  airfield, the Orne and its canal, the villages and the roads show in their
  classes.
- Both loaded in the viewer (WebGL2 in software), with town markers in the
  same DCS metres sitting on the ground.
- Caucasus scene, Beslan and Vladikavkaz (60 km square): 20,887 buildings.
  Placements land on their ground (an instance's height is the ground's);
  runway lights trace the game's runway (Beslan: 53 m beside the surveyed
  one and about 85 m along it, as the runway-coloured ground says too), and
  wagons and wall segments line up with the decoded heading (297 of 297 and
  381 of 381).
- `tests/` builds `.surface5` files to the same layout, so no game data is
  kept here; `tests/test_real_install.py` runs on the install of the machine
  running the tests, and is skipped without one.

**Not checked:** the whole of a large theatre in one level (the size guard
above exists for a reason), and versions of DCS other than the one above.

## Not read

- **Buildings as shapes** (the models are `.edm` in `Models/`): boxes only,
  on purpose. Their layout, and the scene's, is written down in
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); every theatre
  installed reads (two older ones, Nevada and The Channel, in a variant
  layout the reader knows too).
- Trees, lights and the other objects of the scene: read, not drawn.
- **The road network as a graph** (`roads/*.rn4`): not decoded.
- Textures, trees, the sea's waves, the terrain's own lower levels of detail.
