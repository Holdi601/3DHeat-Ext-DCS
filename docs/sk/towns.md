---
title: "Názvy miest: towns"
nav_order: 5
lang: "sk"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Názvy miest: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Vypíše názvy miest územia zo súboru `map/towns.lua` (čítaného ako text, nikdy nespusteného) ako JSON: názov každého mesta, jeho zemepisnú šírku a dĺžku a jeho
`x` (sever) a `z` (východ) v metroch DCS, cez projekciu územia.

1. Názov priečinka územia zistite príkazom [`list`](list.md).
2. Spustite `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Použite `x`/`z` na označenie úrovne alebo na kontrolu polôh zo záznamu.

![mestá na syntetickej inštalácii](../assets/img/towns.svg)

| Možnosť | Čo robí |
|---|---|
| `theatre` | názov priečinka pod `Mods\terrains` |
| `--dcs FOLDER` | priečinok DCS World |

Mestá v oblasti úrovne sú aj v jej `<name>.json`, s výškou zeme pod každým z nich ([Súbory úrovne](output.md)).
