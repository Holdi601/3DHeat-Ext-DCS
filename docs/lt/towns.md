---
title: "Vietovardžiai: miestai"
nav_order: 5
lang: "lt"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Vietovardžiai: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Išveda teatro vietovardžius iš jo `map/towns.lua` (skaitomo kaip tekstas, niekada nevykdomo) JSON formatu: kiekvieno miesto
pavadinimą, jo platumą ir ilgumą bei DCS `x` (šiaurė) ir `z` (rytai) metrais, per teatro projekciją.

1. Raskite teatro aplanko pavadinimą su [`list`](list.md).
2. Vykdykite `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Naudokite `x`/`z` lygiui pažymėti arba įrašo pozicijoms patikrinti.

![towns ant sintetinio įdiegimo](../assets/img/towns.svg)

| Parinktis | Ką daro |
|---|---|
| `theatre` | aplanko pavadinimas `Mods\terrains` viduje |
| `--dcs FOLDER` | DCS World aplankas |

Miestai lygio regione taip pat yra jo `<name>.json` faile, su kiekvieno žemės aukščiu ([Lygio failai](output.md)).
