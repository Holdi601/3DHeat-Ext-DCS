# DCS World theatres

The ground of a DCS World theatre - Normandy 1944, The Channel, Marianas WWII,
Germany Cold War and the rest - as a 3D level for the 3DHeat viewer, read from
**your own install**. The 3DHeat world backdrop draws today's earth from open
data; this draws the game's own map: its terrain, its coast, and the
airfields, roads, railways and towns of the period the theatre shows.

This reader is kept outside the 3DHeat tools on purpose: it reads Eagle
Dynamics' terrain files, and their licence (below) is strict about that. If it
ever has to go, nothing else goes with it. The levels it writes stay on your
machine.

```bash
pip install -e .                                          # installs the heat3d-dcs-maps command
heat3d-dcs-maps list                                      # the theatres installed, and whether each can be read
heat3d-dcs-maps level MarianasWWII -o levels              # a whole theatre
heat3d-dcs-maps level Normandy --around 49.19 -0.37 12 -o levels --name Caen   # 12 km either side of Caen
heat3d-dcs-maps towns TheChannel                          # its place names, with DCS coordinates
```

The install is found from the registry, the Steam libraries and the usual
folders; `--dcs <folder>` (the one holding `Mods\terrains`) or the `DCS_PATH`
environment variable say where it is otherwise. Exit status: 0 done, 1
failed, 2 nothing found.

## What comes out

`<out>/<name>.glb` and `<name>.json` beside it.

| Part | What it is |
|---|---|
| `ground:<Level>` | the terrain's own triangles, coloured by what the game draws over each |
| `water:<Level>` | every triangle the game marks as under the sea, laid flat at sea level |

The colours show with **Captured colour** in the viewer's level panel. Each
ground triangle takes the class of the overlay the game draws it with:

| Class | Colour | From the game's overlay |
|---|---|---|
| runway | near black | `Runway` - runways, taxiways and aprons |
| road | dark grey | `Road` |
| rail | brown | `Rail` |
| town | brick red | `Town`, `Building` |
| water | blue | `River`, `Lake` (inland water, drawn as ground) |
| beach | sand | `Beach` |
| rock | grey | `Rock` |
| field | light green | `Field`, `Grass` |
| forest | dark green | `Forest`, `Trees` |
| land | khaki | none of these |

Where several overlays draw the same triangle, the order of the table decides
(a road through a forest is road). Every overlay triangle is one of the
ground's own - checked on all classes of two theatres, every one matched - so
the classes are exact, not guessed from nearby points.

**Coordinates** are DCS's own world metres: x north, y up, z east, and the
glTF axes are the same (X = x, Y = y, Z = z). Telemetry in DCS metres - the
3DHeat Watcher's DCS hook writes exactly that - lands on the level with the
viewer's defaults (Y up, scale 1) and no placement step.

**Latitude and longitude:** every theatre is a Transverse Mercator projection
with its own constants; `<name>.json` carries them, the level's corners in
latitude and longitude, and every town with both its latitude/longitude and
its DCS x/z. Iraq's constants are not published; `fit` finds them from any
recording that holds both, such as a Watcher session of one Iraq flight:

```bash
heat3d-dcs-maps fit "<session>/heat.parquet"   # or .jsonl / .csv with lat, lon, x, z
heat3d-dcs-maps level Iraq --projection <LON0> <FE> <FN> -o levels --around 33.3 44.4 30
```

**The sea floor** is left out (a flight-sim heatmap does not need the bottom
of the Pacific); `--seabed` keeps it as ground. `--no-water` leaves out the
flat sea.

**Size.** The game's mesh is adaptive - open sea in triangles kilometres
across, coasts and roads in a few metres - and the whole of a small theatre
is a few million triangles (Marianas WWII: 5.7 million vertices). The big ones
are 35 to 90 million vertices; for those, `level` asks for a region
(`--around LAT LON KM`, or `--bounds X0 Z0 X1 Z1` in DCS metres) or a thinner
mesh (`--cell 50`: every vertex within 50 m becomes one), or `--force`.

`<name>.json` also records the source file, its size and date, the tiles
read, the triangle count per class, and how many of the theatre's towns land
on the ground - a check of the projection that should read "N of N".

## What it reads, and how

Only `Mods/terrains/<theatre>/surface/*.surface5` (the ground mesh) and
`map/towns.lua` (place names, read as text, never run). Not the encrypted
`terrain.cfg.lua.pak.crypt`, not `manifest.bin`, nothing of the program.

The `.surface5` format is undocumented; the layout, as read from the files,
is written down in [`heat3d_ext_dcs/surface5.py`](heat3d_ext_dcs/surface5.py).
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
- `tests/` builds `.surface5` files to the same layout, so no game data is
  kept here; `tests/test_real_install.py` runs on the install of the machine
  running the tests, and is skipped without one.

**Not checked:** the whole of a large theatre in one level (the size guard
above exists for a reason), and versions of DCS other than the one above.

## Not read

- **Buildings and other objects** (`Scenes/*.scn5` places them, the models
  are `.edm` in `Models/`): not decoded, so there is no `structure:` part. A
  town shows as town-coloured ground, not as houses.
- **Airfield names and positions** (`AirfieldsTaxiways/*.rn4`) and the road
  network as a graph (`roads/*.rn4`): not decoded. Airfields show as runway
  ground; their names are not in the level.
- Textures, trees, the sea's waves, the terrain's own lower levels of detail.

## Eagle Dynamics' terms

Read on 2026-11-07 from `Doc/license_en.txt` of the install (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). The licensed
"Program" includes "THE DATA SUPPLIED WITH IT". Clause 3.1:

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

Clause 3.1 (a) forbids to "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" without consent, and (e) to "exploit this
Program or any of its parts commercially".

What this reader does: it reads data files on your own machine, after you
installed them, outside the game. It changes nothing in the game, breaks no
encryption (the one enciphered file in a terrain folder is left alone) and
talks to no server. Working out the layout of a data file is reverse
engineering in the sense of 3.1 (c), and a level built from the game's
terrain is arguably a derivative work. Using the reader is your decision,
for your own use; the levels it writes are yours to view, not to share or
publish. That is why it is a separate package.

The sanctioned alternative, which reads no file: the sim's own mission
scripting can sample the ground (`land.getHeight`, `land.getSurfaceType`)
and list airbases (`world.getAirbases`) while a mission runs. It needs DCS
running for hours per theatre and gives a coarser grid; it was not built,
because the files proved readable.

## Licence and sources

MIT ([`LICENSE`](LICENSE)). Needs numpy (BSD-3-Clause); `fit` on a
`.parquet` needs pyarrow (Apache-2.0). Written for this project. The
projection constants are facts published by pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); only the numbers were
taken. The projection is Krüger's series as C. F. F. Karney gives it
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No code was taken from any other project.
