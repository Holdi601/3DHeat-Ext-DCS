# Changelog

## 0.6.0

- Its own icon: the 3DHeat cube with a text badge for its game (letters in 3DHeat's colours), as the
  program, window, taskbar and docs icon.
- A new window: the 3DHeat look in dark and light (follows the system, switchable), the logo and
  icon, sharp at any display scaling. Four steps: find the game (each requirement with its fix),
  choose (maps ticked when there is something to do, filters, search; jobs with their fields
  inline), work (progress, time left, cancel), done (open in 3DHeat, open the output folder, and
  for a failure what went wrong and what to do, copy details, report a problem).
- No console window on Windows: the program is a window program. From a terminal it still prints
  as before; `heat3d-dcs-cli.cmd` beside it waits for it in a terminal and passes its exit code.
- The update offer in the same look: Update now / Later / Skip this version, and "Update
  automatically" from the dialog.
- CI draws every page and dialog of the window (on Linux under a virtual display) and checks the
  Windows build is a window program.

## 0.5.0

- A standalone program for Windows and Linux (no Python needed), built by CI with a `SHA256SUMS` file. Without
  arguments it opens a window: what is found and what is missing (install, readable theatres, disk space), the
  levels folder, the theatres as new / changed by a game update / extracted by an older version / up to date, and
  extraction of the picked ones one at a time into `<levels>/dcs/` (the level, its `.json` and its airbase
  layouts; a theatre above 30 million vertices thinned to 50 m cells), and updates.
- Each extracted theatre is recorded in `<levels>/dcs/.heat3d-extract.json` (extractor version, game build, size
  and SHA-256 of its terrain, scene and towns files), so a new terrain module or a changed theatre is found and
  only those extracted: `status --json`, `extract --new` / `--changed` / `--outdated` / `<theatre>...`,
  `--progress-json`.
- Updates ask first (update now / later / skip this version) unless automatic updates were chosen
  (`--auto-update`, the window's checkbox, or `HEAT3D_AUTO_UPDATE=1`).
- The install is also found in Steam libraries on Linux (native, flatpak, Steam Deck; DCS World under Proton)
  and in the usual Wine prefixes of a standalone DCS World there.

## 0.4.2

- `models`: no more dark patches over aircraft. Where simplifying a model fell back to joining nearby vertices, the
  triangles it kept were stored with their corners sorted, which turned about half of them inside out; the viewer
  takes a face's side from its winding, so they were lit as seen from behind. Each triangle now keeps its winding.
- `models`: an aircraft's landing gear takes at most 12 % of each level of detail (it took up to 30 % of a jet's),
  so the airframe keeps the detail. Pieces stretched between the hull and a gear leg (rubber boots, hoses: meshes
  split over both) now come down with the gear. A deployed drag chute is no longer part of the model at rest.
- The EDM reader reads models whose root node is of version 2 (it carries one more byte before its bounding boxes);
  the 17 such files of an installation, a static warning board among them, failed to read.

## 0.4.1

- `models`: an aircraft's or helicopter's retractable landing gear is a part of its own (`gear`, posed down with
  its doors open, extras `{retract: true, pivot}`; `gear: "retract"` in the index entry), so the viewer can raise
  and lower it; the hull keeps the gear bays shut. Static objects are written too, tagged `kind` and `type`
  `static`. `--only` limits a run to some domains or classes, `--force` rewrites models that are up to date. Units
  whose names differ only in case get files of their own.
- `catalog`: static objects (fortifications, buildings, cargo, heliports, markers...) have the class `static`,
  from their table's category or their `wsType_Static` attribute.

## 0.4.0

- `models`: every unit's model of your installation as a local model pack (`model-packs/dcs/`) the viewer draws
  in place of its figures. A new reader for DCS's `.edm` models (versions 8 and 10): the node tree with its
  transforms, animation arguments, levels of detail and visibility switches, and the meshes hanging from it,
  including meshes split over several nodes and skinned meshes. Each model at rest, with a ground unit's turret and
  gun and a helicopter's main rotor as parts that turn, wheels and tracks as running gear, and the collision shells
  as hit regions; three levels of detail. Files that are not EDM models it can open are skipped and listed.
- `catalog`: a unit's model is also found where its Lua sets the shape field by field, and units drawn with
  another unit's model file link to it.

## 0.3.0

- `layouts`: each theatre's airbases (ids and names), runways and the parking stands the missions in your install
  start aircraft from, as `<theatre>.layouts.json` and, cut to each level, `<level>.layouts.json` beside the
  levels. Docs: [Level](docs/level.md#airbases-runways-and-parking-layouts).
- `catalog`: every aircraft, helicopter, ground unit, ship and weapon of your installation (the modules', asset
  packs' and Saved Games mods' Lua, as `ranges` reads it) as `catalog.json`: type name, display name, class,
  domain, the model it is drawn with, its weapons and a few numbers, and the real vehicle each stands for. The
  viewer names DCS units by it and draws them with another game's local model of the same vehicle.

## 0.2.0

- `ranges`: builds a catalogue of weapon and sensor ranges, and the units that carry them, from your own installation, for the viewer's match replay.

- Buildings from the theatre's scene, as boxes (`structure` part, `buildings` in the `.json`; `--no-buildings`).
- Airfields: names and positions from the taxiway files.
- A theatre's projection fitted to its own beacons where none is published; `fit` for any other.
- Installs with one pip line from the release zip, no Git needed; a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## 0.1.0

- First version: a DCS World theatre's ground and sea as a 3DHeat level; `list`, `level`, `towns`.

## Docs

Where each feature is documented
([holdi601.github.io/3DHeat-Ext-DCS](https://holdi601.github.io/3DHeat-Ext-DCS/)):

| Feature | Page |
|---|---|
| Installing, a first run | [Before you start](docs/before-you-start.md) |
| Finding the install and its theatres (`list`, `--dcs`, `DCS_PATH`) | [Finding theatres: list](docs/list.md) |
| Building a level, regions, size (`level` and its options) | [Building a level: level](docs/level.md) |
| The `.glb` parts, ground classes and colours, the `.json`, coordinates, airfields, buildings | [The level files](docs/output.md) |
| Place names (`towns`) | [Place names: towns](docs/towns.md) |
| Weapon and sensor ranges (`ranges`) | [Weapon and sensor ranges: ranges](docs/ranges.md) |
| Projections (`fit`, `--projection`) | [Projections: fit](docs/fit.md) |
| How the files are read, what was checked, what is not read | [How the files are read](docs/reading.md) |
| What is read, what is not shipped, the licence | [Terms and licence](docs/terms.md) |
| Every option and output key, generated | [Command reference](docs/cli-reference.md) |
| Release checklist for the docs | [Maintaining these docs](docs/maintaining.md) |
