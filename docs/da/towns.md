---
title: "Stednavne: towns"
nav_order: 5
lang: da
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Stednavne: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Udskriver teatrets stednavne, fra dets `map/towns.lua` (læst som tekst,
aldrig kørt), som JSON: hver bys navn, dens breddegrad og længdegrad, og dens
DCS-`x` (nord) og `z` (øst) i meter, gennem teatrets projektion.

1. Find teatrets mappenavn med [`list`](list.md).
2. Kør `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Brug `x`/`z` til at mærke en bane, eller til at tjekke en optagelses positioner.

![towns på en syntetisk installation](../assets/img/towns.svg)

| Valgmulighed | Gør |
|---|---|
| `theatre` | mappenavnet under `Mods\terrains` |
| `--dcs FOLDER` | DCS World-mappen |

Byerne inden for en banes område står også i dens `<name>.json`, med
højden på jorden under hver ([Banefilerne](output.md)).
