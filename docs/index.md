---
title: Home
nav_order: 1
---

# 3DHeat DCS

**What is it?** A theatre is DCS World's word for a map: a region of the
world you fly over. This tool turns the ground of one theatre, read from
**your own install**, into a 3D level - a model you can fly over - for the
[3DHeat](https://github.com/Holdi601/3DHeat) viewer
([documentation](https://holdi601.github.io/3DHeat/)).

**Why would I use it?** To see your DCS flights over the game's own map: its
hills, coast, airfields, roads, railways, towns and buildings.

**Example:** `heat3d-dcs-maps level <theatre> -o levels` ->
`levels/<theatre>.glb` (the level) + `levels/<theatre>.json` (where it lies on
the earth, its towns and airfields).

What it is useful for:

- **Flights on the game's own map.** The 3DHeat world backdrop draws today's
  earth from open data; this draws the theatre as DCS draws it.
- **No placement step.** The level is in DCS's own world metres, so telemetry
  in DCS metres (the 3DHeat Watcher's DCS hook writes exactly that) lands on
  it with the viewer's defaults.
- **Latitude and longitude.** Every level carries its projection, its corners
  and its towns in both frames.

![From a DCS install to a 3DHeat level](assets/img/flow.svg)

## The standalone program (no Python needed)

Each [release](https://github.com/Holdi601/3DHeat-Ext-DCS/releases/latest)
has a ready-to-run program for Windows (`heat3d-dcs-<version>-windows-x64.zip`)
and Linux (`heat3d-dcs-<version>-linux-x64.tar.gz`, for DCS World installed
under Proton by Steam or under Wine), with a `SHA256SUMS` file to check the
download. Unpack it anywhere and start `heat3d-dcs`.

Started without arguments it opens a window that:

- finds your DCS World install (the registry, the Steam libraries and the
  usual folders; on Linux the Steam libraries and Wine prefixes), or lets you
  choose its folder (the one holding `Mods\terrains`);
- says what is missing: the game, a theatre it can read, free disk space;
- lists the theatres as new, changed by a game update, extracted by an older
  version, or up to date, and extracts the ones you pick, one at a time, into
  the 3DHeat levels folder (`HEAT3D_LEVELS`, by default
  `%LOCALAPPDATA%\3DHeat\levels` on Windows and `~/.local/share/3dheat/levels`
  on Linux), under `dcs/`, where the viewer finds them: each theatre's `.glb`,
  its `.json` and its airbase layouts. A theatre above 30 million vertices is
  thinned to 50 m cells there; for full detail use `level` with a region;
- checks for updates and asks before installing one, unless you tick
  *Update automatically*.

A new terrain module or a game update that changes a theatre is found the
next time: each extracted theatre is recorded in
`<levels>/dcs/.heat3d-extract.json` with the version that extracted it, the
game's build and the size and SHA-256 of the files it was made from.

The same program runs every command below: `heat3d-dcs heat3d-dcs-maps list`,
`heat3d-dcs heat3d-dcs-maps level <theatre> -o <folder>`. For scripts:
`heat3d-dcs status --json` reports the theatres' state,
`heat3d-dcs extract --new` extracts only the new ones and
`heat3d-dcs --check --json` says what is found and missing. The 3DHeat app's
Extractors panel installs, updates and starts it for you.
`python -m heat3d_ext_dcs.standalone_spec` opens the same window from the
source.

## Quick start (Python)

You need Windows, Python 3.10 or later ("Add python.exe to PATH" ticked in its
installer), DCS World installed (found by itself) and about 800 MB of disk
space for a whole Caucasus; no Git. New to the command line? Read
[Before you start](before-you-start.md) first.

```bash
python -m pip install https://github.com/Holdi601/3DHeat-Ext-DCS/archive/refs/tags/v0.3.0.zip
heat3d-dcs-maps list                               # the theatres installed, and whether each can be read
heat3d-dcs-maps level Caucasus -o levels           # a whole (small) theatre
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name <name>   # 12 km either side of a point
```

You should see one line per theatre from `list`, ending `readable`. `level`
writes `levels\Caucasus.glb` (the level, about 710 MB) and
`levels\Caucasus.json` beside it (where it lies on the earth, its towns and
airfields); the whole Caucasus takes about 3 minutes. A large theatre (above 30
million vertices, as `list` shows) stops and asks for a region, such as the
`--around` square above. A DCS folder that is not found needs
`--dcs "<DCS World folder>"` (the one holding `Mods\terrains`).

Then open the `.glb` in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
download it (**Code -> Download ZIP**, unpack), double-click `start.bat` (it
offers to install Node.js when it is missing and opens `http://127.0.0.1:5273`),
then **Background / level -> 3D model...** and pick the file
([Levels](https://holdi601.github.io/3DHeat/levels.html)); **Captured colour**
in the same panel shows the ground classes. The level stays on your machine.

When a new release is out, the tool says so when it starts, shows its notes
and asks: update now, later, or skip this version. It updates without asking
only when you chose that: `--auto-update` (this run), the standalone window's
*Update automatically*, or `HEAT3D_AUTO_UPDATE=1`.

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

## Pages

| Page | What it covers |
|---|---|
| [Before you start](before-you-start.md) | Python, a terminal, a first run |
| [Finding theatres: list](list.md) | where the install is found, what `list` prints |
| [Building a level: level](level.md) | every option, regions, size, step by step |
| [The level files](output.md) | the `.glb` parts, the ground classes and their colours, the `.json`, the coordinates |
| [Place names: towns](towns.md) | a theatre's towns with DCS coordinates |
| [Weapon and sensor ranges: ranges](ranges.md) | a catalogue of weapon and sensor ranges for the match replay |
| [Projections: fit](fit.md) | finding a theatre's projection from a recording |
| [How the files are read](reading.md) | the formats, what was verified, what is not read |
| [Terms and licence](terms.md) | what is read, what is not shipped, the licence |
| [Command reference](cli-reference.md) | every option, generated from the code |
| [Maintaining these docs](maintaining.md) | the release checklist |

## Related

- The 3DHeat viewer: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation at [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Telemetry for these levels: the [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/)
  records DCS flights; the viewer's file formats, including its
  one-file-a-match container, are described in
  [One file a match (.3dheat)](https://holdi601.github.io/3DHeat/container.html).

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
