# Changelog

## 0.4.0

- `models`: every unit's model of your installation as a local model pack (`model-packs/dcs/`) the viewer draws
  in place of its figures. A new reader for DCS's `.edm` models (versions 8 and 10): the node tree with its
  transforms, animation arguments, levels of detail and visibility switches, and the meshes hanging from it,
  including meshes split over several nodes and skinned meshes. Each model at rest, with a ground unit's turret and
  gun and a helicopter's main rotor as parts that turn, wheels and tracks as running gear, and the collision shells
  as hit regions; three levels of detail. Files that are not EDM models it can open are skipped and listed.
- `catalog`: a unit's model is also found where its Lua sets the shape field by field.

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
