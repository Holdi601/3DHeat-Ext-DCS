---
title: "Helynevek: towns"
nav_order: 5
lang: hu
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Helynevek: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Kiírja a színház helyneveit a `map/towns.lua` fájlból (szövegként olvasva, sosem futtatva) JSON-ként:
minden város nevét, szélességi és hosszúsági fokát, és DCS `x` (észak) és `z` (kelet) értékét méterben,
a színház vetítésén keresztül.

1. Keresd meg a színház mappanevét a [`list`](list.md) paranccsal.
2. Futtasd a `heat3d-dcs-maps towns <theatre> > towns.json` parancsot.
3. Az `x`/`z` értékekkel címkézd fel a pályát, vagy ellenőrizd egy felvétel pozícióit.

![Városok egy szintetikus telepítésen](../assets/img/towns.svg)

| Kapcsoló | Mit csinál |
|---|---|
| `theatre` | a `Mods\terrains` alatti mappanév |
| `--dcs FOLDER` | a DCS World mappa |

Egy pálya régiójában lévő városok is benne vannak annak `<name>.json` fájljában, minden alattuk lévő talaj
magasságával ([A pályafájlok](output.md)).
