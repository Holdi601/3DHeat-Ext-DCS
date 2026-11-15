---
title: "Imena krajev: towns"
nav_order: 5
lang: "sl"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Imena krajev: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <teater> [--dcs MAPA]
```

Izpiše imena krajev teatra iz njegove datoteke `map/towns.lua` (prebrana kot besedilo, nikoli
zagnana) kot JSON: ime vsakega mesta, njegova zemljepisna širina in dolžina ter njegov DCS `x`
(sever) in `z` (vzhod) v metrih prek projekcije teatra.

1. Poišči ime mape teatra z [`list`](list.md).
2. Zaženi `heat3d-dcs-maps towns <teater> > towns.json`.
3. Uporabi `x`/`z`, da označiš raven, ali da preveriš položaje iz posnetka.

![mesta na sintetični namestitvi](../assets/img/towns.svg)

| Možnost | Naredi |
|---|---|
| `teater` | ime mape pod `Mods\terrains` |
| `--dcs MAPA` | mapa DCS World |

Mesta znotraj območja ravni so tudi v njeni datoteki `<ime>.json` z višino tal pod vsakim
([Datoteke ravni](output.md)).
