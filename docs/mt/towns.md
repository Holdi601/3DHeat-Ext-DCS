---
title: "Ismijiet tal-postijiet: towns"
nav_order: 5
lang: mt
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Ismijiet tal-postijiet: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Jistampa l-ismijiet tal-postijiet tat-teatru, mill-`map/towns.lua` tiegħu (moqri bħala test,
qatt ma jitħaddem), bħala JSON: l-isem ta' kull raħal, il-latitudni u l-lonġitudni tiegħu, u
`x` (tramuntana) u `z` (lvant) ta' DCS f'metri, mill-projezzjoni tat-teatru.

1. Sib l-isem tal-folder tat-teatru b'[`list`](list.md).
2. Ħaddem `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Uża l-`x`/`z` biex tikteb tikketti fuq livell, jew biex tivverifika l-pożizzjonijiet ta' reġistrazzjoni.

![towns fuq installazzjoni sintetika](../assets/img/towns.svg)

| Għażla | Tagħmel |
|---|---|
| `theatre` | l-isem tal-folder taħt `Mods\terrains` |
| `--dcs FOLDER` | il-folder ta' DCS World |

L-irħula fir-reġjun ta' livell huma wkoll fil-`<name>.json` tiegħu, bl-
għoli tal-art taħt kull wieħed ([Il-fajls tal-livell](output.md)).
