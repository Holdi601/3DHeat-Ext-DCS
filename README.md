# 3DHeat DCS: DCS World maps as 3D levels

**What is it?** A theatre is DCS World's word for a map: a region of the
world you fly over. This tool turns the ground of one theatre, read from your
own DCS install, into a 3D model you can fly over in the
[3DHeat](https://github.com/Holdi601/3DHeat) viewer.

**Why would I use it?** To see your DCS flights over the game's own map -
its hills, coast, airfields, roads and towns - instead of today's earth.

**Example:** `heat3d-dcs-maps level <theatre> -o levels` -> `levels/<theatre>.glb`
(the 3D level) + `levels/<theatre>.json` (where it lies on the earth, its
towns and airfields).

![From a DCS install to a 3DHeat level](docs/assets/img/flow.svg)

**Documentation:** [holdi601.github.io/3DHeat-Ext-DCS](https://holdi601.github.io/3DHeat-Ext-DCS/), a page per
command with step-by-step use and example output. Part of
[3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

The levels it writes stay on your machine.

## Quick start for new users

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), DCS World installed (found
by itself from the registry, the Steam libraries and the usual folders), and
about 800 MB of disk space for a whole Caucasus. No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt):

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-DCS/archive/refs/tags/v0.2.0.zip
   ```

2. List the theatres, then export one (a DCS folder that is not found needs
   `--dcs "<DCS World folder>"`, the one holding `Mods\terrains`):

   ```bash
   heat3d-dcs-maps list
   heat3d-dcs-maps level Caucasus -o levels
   ```

   A large theatre (above 30 million vertices, as `list` shows) stops and asks
   for a region: `heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name <name>`
   writes a square 12 km either side of a point.
3. The output is `levels\Caucasus.glb` (the level, about 710 MB) and
   `levels\Caucasus.json` beside it (where it lies on the earth, its towns and
   airfields); the whole Caucasus takes about 3 minutes.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There,
   **Background / level -> 3D model...** and pick the `.glb`; **Captured
   colour** in the same panel shows the ground classes.

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_dcs.update` does the same).

## Install from a checkout

New to the command line? Read [Before you start](https://holdi601.github.io/3DHeat-Ext-DCS/before-you-start.html) first.

1. Install Python 3.10 or later, and DCS World.
2. `git clone https://github.com/Holdi601/3DHeat-Ext-DCS` (or download the
   ZIP) and open a terminal in that folder.
3. Install the command and list your theatres:

```bash
python -m pip install -e .        # installs the heat3d-dcs-maps command
heat3d-dcs-maps list              # the theatres installed, and whether each can be read
```

You should see one line per installed theatre: its name, its size, and `readable`.

![list on a synthetic install](docs/assets/img/list.svg)

## Commands

| Command | Does | Page |
|---|---|---|
| `list [--dcs FOLDER]` | the theatres installed, and whether each can be read | [list](https://holdi601.github.io/3DHeat-Ext-DCS/list.html) |
| `level <theatre> -o <folder>` | one theatre's ground, sea and buildings as a `.glb` level | [level](https://holdi601.github.io/3DHeat-Ext-DCS/level.html) |
| `towns <theatre>` | the theatre's place names, with DCS coordinates, as JSON | [towns](https://holdi601.github.io/3DHeat-Ext-DCS/towns.html) |
| `ranges -o <file>` | a catalogue of weapon and sensor ranges from your own installation, for the match replay | [ranges](https://holdi601.github.io/3DHeat-Ext-DCS/ranges.html) |
| `catalog [-o <file>]` | every aircraft, helicopter, ground unit, ship and weapon of your installation (name, class, the model it is drawn with, its weapons), as `catalog.json` for the viewer's unit names and order (default `$HEAT3D_LEVELS/dcs/catalog.json`) | below |
| `fit <recording>` | find a theatre's projection from a recording | [fit](https://holdi601.github.io/3DHeat-Ext-DCS/fit.html) |

```bash
heat3d-dcs-maps level <theatre> -o levels                                      # a whole (small) theatre
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name <name>  # 12 km either side of a point
heat3d-dcs-maps towns <theatre>                                                # its place names
heat3d-dcs-maps ranges -o ranges.json                                          # weapon and sensor ranges
heat3d-dcs-maps catalog                                                        # unit and weapon catalogue
```

`<theatre>` is the name `list` prints. The install is found from the
registry, the Steam libraries and the usual folders; `--dcs <folder>` (the
one holding `Mods\terrains`) or the `DCS_PATH` environment variable say
where it is otherwise. Exit status: 0 done; 1 failed (or too large, or for
`fit` a poor fit); 2 nothing found.

| `level` option | Does |
|---|---|
| `-o`, `--out FOLDER` | where `<name>.glb` and `<name>.json` go (required) |
| `--dcs FOLDER` | the DCS World folder (also for `list` and `towns`) |
| `--name NAME` | the level's name (default: the theatre's) |
| `--around LAT LON KM` / `--bounds X0 Z0 X1 Z1` | only a square around a point / a box in DCS metres |
| `--cell M` | thin the mesh to *M* metres (default 0: the game's own triangles) |
| `--seabed`, `--no-water`, `--no-buildings` | keep the sea floor; leave out the flat sea; leave out the buildings |
| `--force` | export a very large theatre whole at full detail |
| `--projection LON0 FE FN` | Transverse Mercator constants for a theatre this tool does not know (see `fit`) |

Every option, as the program prints it: [Command reference](https://holdi601.github.io/3DHeat-Ext-DCS/cli-reference.html).

## What comes out

`<out>/<name>.glb` (a glTF binary level) and `<name>.json` beside it. Levels
are not match files: the viewer's one-file-a-match container
([One file a match (.3dheat)](https://holdi601.github.io/3DHeat/container.html))
holds the telemetry you load on top.

| Part | What it is |
|---|---|
| `ground:<Level>` | the terrain's own triangles, coloured by what the game draws over each |
| `water:<Level>` | every triangle the game marks as under the sea, laid flat at sea level |
| `structure:<Level>` | the theatre's buildings as boxes, where the game places them |

The colours show with **Captured colour** in the viewer's Background / level panel:

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
| seabed | slate blue | only with `--seabed` |

**Coordinates** are DCS's own world metres: x north, y up, z east, the same
as the glTF axes. Telemetry in DCS metres - the 3DHeat Watcher's DCS hook
writes exactly that - lands on the level with no placement step.
`<name>.json` carries the theatre's projection, the level's corners in
latitude and longitude, and its towns, airfields and buildings: see
[The level files](https://holdi601.github.io/3DHeat-Ext-DCS/output.html).

## The 3DHeat tools

| Tool | What it does | Code | Docs |
|---|---|---|---|
| 3DHeat viewer | shows the data: heatmaps, race analysis, match review | [3DHeat](https://github.com/Holdi601/3DHeat) | [docs](https://holdi601.github.io/3DHeat/) |
| GameFiles | levels and courses from a game's own files | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [docs](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [docs](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin: a level as one `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [docs](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [docs](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [docs](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | War Thunder replays | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [docs](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | World of Tanks replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [docs](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | World of Warships replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [docs](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [docs](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [docs](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | IL-2 Sturmovik maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [docs](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | the Dota 2 map from your own install as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [docs](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | Dota 2 replays | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [docs](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | League of Legends and VALORANT replays (what they carry unencrypted) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [docs](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | Forza courses, races and cars from your own install | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [docs](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | Battlefield levels (Frostbite) as 3D levels | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [docs](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | BeamNG.drive courses | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [docs](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | Assetto Corsa Rally stages as courses | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [docs](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | Arma Reforger worlds (Enfusion) as 3D levels | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [docs](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | Rainbow Six Siege match replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [docs](https://holdi601.github.io/3DHeat-Ext-R6/) |

## What the reader reads

The reader reads data files of your own DCS World installation on your
computer ([How the files are
read](https://holdi601.github.io/3DHeat-Ext-DCS/reading.html)). It changes
nothing in the game and talks to no server.

Nothing from the game is shipped or redistributed: no game files, no game
code, no DLLs; the tests build every file they read. The levels it writes stay
on your machine.

3DHeat DCS is not affiliated with or endorsed by Eagle Dynamics. DCS World and
related names and trademarks belong to their owners.

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) -
we respond quickly and remove anything on request.

## Licence and sources

MIT ([`LICENSE`](LICENSE)). Needs numpy (BSD-3-Clause); `fit` on a
`.parquet` needs pyarrow (Apache-2.0). Written for this project. The
projection constants are facts published by pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); only the numbers were
taken. The projection is Krüger's series as C. F. F. Karney gives it
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No code was taken from any other project.
