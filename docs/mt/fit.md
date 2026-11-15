---
title: "Projezzjonijiet: fit"
nav_order: 6
lang: mt
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projezzjonijiet: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Kull teatru huwa projezzjoni Transverse Mercator bil-kostanti tagħha. L-
għodda tafhom għat-teatri li ġiet ittestjata fuqhom; għal wieħed li ma tafx,
`fit` isibhom minn kull reġistrazzjoni li fiha kemm latitudni/lonġitudni kif ukoll
metri ta' DCS, bħal sessjoni tal-Watcher ta' 3DHeat ta' titjira waħda.

1. Irrekordja titjira fuq it-teatru bil-Watcher ta' 3DHeat (jew agħmel kull
   reġistrazzjoni b'kolonni `lat`, `lon`, `x`, `z` f'metri ta' DCS: x huwa metri
   lejn it-tramuntana, z metri lejn il-lvant, bħal kullimkien f'DCS).
2. Ħaddem `heat3d-dcs-maps fit "<session>/heat.parquet"` (jew `.jsonl` jew `.csv`).
3. Jistampa l-projezzjoni mqiegħda bħala JSON, l-iżball root mean square fuq
   il-punti, u l-argumenti `--projection` li għandek tuża.
4. Ibni l-livell bihom:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit fuq reġistrazzjoni sintetika](../assets/img/fit.svg)

Ir-reġistrazzjoni fl-istampa hija disa' punti magħmulin minn projezzjoni magħrufa,
li `fit` isibha lura sal-millimetru.

| Argument | X'jagħmel |
|---|---|
| `recording` | `.parquet`, `.jsonl` jew `.csv` b'kolonni `lat`, `lon`, `x`, `z` (metri ta' DCS); ringieli li ma jinqrawx jitqabżu |

Il-projezzjoni hija s-serje ta' Krüger kif tagħtha C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Status tal-ħruġ: 0 fit tajjeb (taħt 5 m root mean square); 1 fit ħażin, jew
inqas minn tliet ringieli użabbli; 2 il-fajl ma nstabx.
