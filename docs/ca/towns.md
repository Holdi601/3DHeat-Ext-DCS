---
title: "Noms de llocs: towns"
nav_order: 5
lang: ca
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Noms de llocs: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <teatre> [--dcs CARPETA]
```

Imprimeix els noms de llocs del teatre, a partir del seu `map/towns.lua` (llegit com a text,
mai executat), com a JSON: el nom de cada poble, la seva latitud i longitud, i
la seva `x` (nord) i `z` (est) de DCS en metres, a través de la projecció del teatre.

1. Trobi el nom de la carpeta del teatre amb [`list`](list.md).
2. Executi `heat3d-dcs-maps towns <teatre> > towns.json`.
3. Utilitzi les `x`/`z` per posar etiquetes a un nivell, o per comprovar les posicions d'una gravació.

![pobles sobre una instal·lació sintètica](../assets/img/towns.svg)

| Opció | Què fa |
|---|---|
| `teatre` | el nom de la carpeta sota `Mods\terrains` |
| `--dcs CARPETA` | la carpeta de DCS World |

Els pobles dins de la regió d'un nivell també són al seu `<nom>.json`, amb l'
altura del terreny sota cadascun ([Els fitxers del nivell](output.md)).
