---
title: "Uertsnimm: towns"
nav_order: 5
lang: "lb"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Uertsnimm: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Gëtt d'Uertsnimm vum Theater aus senger `map/towns.lua` (als Text gelies,
ni ausgeféiert) als JSON aus: den Numm vun all Stad, hire Breeden- a Längtegrad, a säin
DCS-`x` (Norden) an `z` (Ouschten) a Meter, duerch d'Projektioun vum Theater.

1. Fannt den Dossiernumm vum Theater mat [`list`](list.md).
2. `heat3d-dcs-maps towns <theatre> > towns.json` ausféieren.
3. De `x`/`z` benotzen, fir e Level ze beschrëften, oder d'Positioune vun enger Opnam ze préiwen.

![towns op enger syntheteschen Installatioun](../assets/img/towns.svg)

| Optioun | Mécht |
|---|---|
| `theatre` | den Dossiernumm ënner `Mods\terrains` |
| `--dcs FOLDER` | den DCS-World-Dossier |

D'Stied an der Regioun vun engem Level sinn och a sengem `<name>.json`, mat der
Héicht vum Buedem ënner all enger ([D'Level-Dateien](output.md)).
