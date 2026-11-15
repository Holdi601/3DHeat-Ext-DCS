---
title: "Kohanimed: towns"
nav_order: 5
lang: "et"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Kohanimed: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Prindib teatri kohanimed tema `map/towns.lua` failist (loetud tekstina,
mitte käivitatuna) JSON-ina: iga linna nimi, tema laiuskraad ja pikkuskraad ning
tema DCS-i `x` (põhi) ja `z` (ida) meetrites, teatri projektsiooni kaudu.

1. Leia teatri kaustanimi käsuga [`list`](list.md).
2. Käivita `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Kasuta `x`/`z`-i taseme märgistamiseks või salvestuse asukohtade kontrollimiseks.

![towns sünteetilisel installil](../assets/img/towns.svg)

| Valik | Teeb |
|---|---|
| `theatre` | kaustanimi kaustas `Mods\terrains` |
| `--dcs FOLDER` | DCS World'i kaust |

Teatri piirkonna linnad on ka tema `<name>.json` failis, koos maapinna kõrgusega iga linna all ([Tasemefailid](output.md)).
