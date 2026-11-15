---
title: "Insibu t-teatri: list"
nav_order: 2
lang: mt
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Insibu t-teatri: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ġdid mal-linja tal-kmandi? Aqra [Qabel ma tibda](before-you-start.md) l-ewwel.

1. Installa darba: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, iftaħ
   terminal f'dak il-folder u ħaddem `python -m pip install -e .` (Python 3.10
   jew aktar ġdid; iġib miegħu numpy, u pyarrow għal `fit` fuq `.parquet`).
2. Ħaddem `heat3d-dcs-maps list`.
3. Kull teatru installat jistampa linja waħda: l-isem tal-folder tiegħu (l-isem li jieħdu
   l-kmandi l-oħra), id-daqs tal-fajl tal-art tiegħu, it-tiles u l-vertiċi tiegħu,
   jekk il-projezzjoni tiegħu tal-latitudni/lonġitudni hijiex magħrufa, u jekk jinqarax.
   Għandek tara `readable` fl-aħħar ta' kull linja.

![list fuq installazzjoni sintetika](../assets/img/list.svg)

L-istampa hija użu fuq installazzjoni li jibnu t-testijiet (`tests/synth.py`), mhux fuq
il-logħba.

## Fejn tinstab l-installazzjoni {#where-the-install-is-found}

`--dcs <folder>` (il-folder li fih `Mods\terrains`) jew il-variabbli tal-ambjent
`DCS_PATH`; inkella jitfittxu r-registry, il-libreriji ta' Steam u l-folders
tas-soltu.

| Għażla | X'jagħmel |
|---|---|
| `--dcs FOLDER` | il-folder ta' DCS World, dak li fih `Mods\terrains` |

Status tal-ħruġ: 0 lest, 2 ebda installazzjoni jew teatru ma nstab.
