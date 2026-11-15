---
title: "Nume de locuri: towns"
nav_order: 5
lang: ro
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nume de locuri: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Afișează numele de locuri ale teatrului, din `map/towns.lua` (citit ca text,
niciodată rulat), ca JSON: numele fiecărui oraș, latitudinea și longitudinea sa și
`x` (nord) și `z` (est) DCS în metri, prin proiecția teatrului.

1. Aflați numele dosarului teatrului cu [`list`](list.md).
2. Rulați `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Folosiți `x`/`z` ca să etichetați un nivel sau ca să verificați pozițiile dintr-o înregistrare.

![orașe pe o instalare sintetică](../assets/img/towns.svg)

| Opțiune | Ce face |
|---|---|
| `theatre` | numele dosarului din `Mods\terrains` |
| `--dcs FOLDER` | dosarul DCS World |

Orașele din regiunea unui nivel se află și în `<name>.json` al acestuia, cu înălțimea
solului de sub fiecare ([Fișierele nivelului](output.md)).
