---
title: "Ortsnamen: towns"
nav_order: 5
lang: "de"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Ortsnamen: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Gibt die Ortsnamen des Schauplatzes aus seiner `map/towns.lua` aus (als Text gelesen,
nie ausgeführt), als JSON: der Name jeder Stadt, ihr Breiten- und Längengrad und ihr
DCS-`x` (Nord) und `z` (Ost) in Metern, über die Projektion des Schauplatzes.

1. Finde den Ordnernamen des Schauplatzes mit [`list`](list.md).
2. Führe `heat3d-dcs-maps towns <theatre> > towns.json` aus.
3. Verwende `x`/`z`, um ein Level zu beschriften oder die Positionen einer Aufnahme zu prüfen.

![Städte auf einer synthetischen Installation](../assets/img/towns.svg)

| Option | Wirkung |
|---|---|
| `theatre` | der Ordnername unter `Mods\terrains` |
| `--dcs FOLDER` | der DCS-World-Ordner |

Die Städte innerhalb der Region eines Levels stehen ebenfalls in dessen `<name>.json`, mit der
Höhe des Bodens unter jeder ([Die Level-Dateien](output.md)).
