---
title: "Weapon and sensor ranges: ranges"
nav_order: 5.5
---

# Weapon and sensor ranges: `ranges`

```text
heat3d-dcs-maps ranges [-o FILE] [--dcs FOLDER] [--saved-games FOLDER | --no-saved-games]
```

Builds a catalogue from your own installation: how far each weapon reaches,
how far and how wide each sensor sees, and which units carry them. The
3DHeat viewer's match replay reads it to draw engagement ranges, view cones
and sensor sectors for DCS World recordings, in place of its own general
values.

1. Run `heat3d-dcs-maps ranges -o ranges.json`.
2. Put `ranges.json` where the viewer looks for it (its documentation says
   where). It stays on your machine.

| Option | Does |
|---|---|
| `-o`, `--out FILE` | the `.json` to write (default: `ranges.json` in the current folder) |
| `--dcs FOLDER` | the DCS World folder |
| `--saved-games FOLDER` | the DCS Saved Games folder whose `Mods` are read too (default: found) |
| `--no-saved-games` | read the install only |

It takes a few seconds. Exit status: 0 done; 1 nothing found to write; 2 no
install.

## What goes in

The definitions of the modules and asset packs (`CoreMods`, `Mods` and the
mods in Saved Games), each read from its `entry.lua` the way the game loads
it:

- **Weapons**: missiles, guided bombs and torpedoes with their stated ranges
  (`D_min`, `D_max`, `Range_max`), target altitudes, seeker, launch angle,
  g limit and speed; the guns of ground units and ships with the range they
  open fire at, their highest target and their muzzle velocity. A weapon whose
  files state no range (most unguided bombs and rockets) is left out.
- **Sensors**: radars with their detection range per hemisphere and aspect,
  their scan volume and ground mapping; cameras and targeting pods with their
  field of view and zoom.
- **Units**: aircraft, helicopters, ground units and ships, under the names a
  recording uses (the type name and the display name),
  with the weapons on their pylons or launchers and the sensors they name.

The core database the game keeps packed is not read. A sensor that only it
defines appears by name and kind, without numbers (`"declared": false`).

## The file

One line of JSON (`version` 1): `weapons` (each with `id`, `cls`, `name`,
`range` as minimum, typical and maximum in metres, `shape`, `cone`, `elev`,
`alt`, `los`, the `labels` a recording may use, and `detail`), `sensors` (by
id: `kind`, `name`, `range`, `az`, `el`, `rcsRef`, `modes`, `mount`,
`detail`) and `units` (`names`, `weapons`, `sensors`, `optics`). Metres and
degrees throughout. A value the files do not state is left out, never
guessed.
