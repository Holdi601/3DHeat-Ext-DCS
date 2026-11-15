---
title: "Ortnamn: towns"
nav_order: 5
lang: "sv"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Ortnamn: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Skriver ut teaterns ortnamn, från dess `map/towns.lua` (läst som text,
aldrig körd), som JSON: varje stads namn, dess latitud och longitud, och dess
DCS `x` (norrut) och `z` (österut) i meter, genom teaterns projektion.

1. Hitta teaterns mappnamn med [`list`](list.md).
2. Kör `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Använd `x`/`z` för att märka en nivå, eller för att kontrollera en inspelnings positioner.

![towns på en syntetisk installation](../assets/img/towns.svg)

| Alternativ | Gör |
|---|---|
| `theatre` | mappnamnet under `Mods\terrains` |
| `--dcs FOLDER` | DCS World-mappen |

Städerna inom en nivås region finns också i dess `<name>.json`, med höjden på marken under varje ([Nivåfilerna](output.md)).
