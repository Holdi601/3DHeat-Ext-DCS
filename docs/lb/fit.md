---
title: "Projektiounen: fit"
nav_order: 6
lang: lb
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektiounen: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

All Theater ass eng Transverse-Mercator-Projektioun mat eegene Konstanten. D'Tool
kennt se fir d'Theatere, op deenen et gepréift gouf; fir een, dat et net kennt,
fënnt `fit` se aus all Opnam, déi souwuel Breeden-/Längtegrad wéi
DCS-Meter hält, zum Beispill eng 3DHeat-Watcher-Sessioun vun engem Fluch.

1. Een Fluch op dem Theater mam 3DHeat Watcher opzeechnen (oder eng
   Opnam mat de Kolonnen `lat`, `lon`, `x`, `z` an DCS-Meter maachen: x ass Meter
   no Norden, z Meter no Osten, wéi iwwerall an DCS).
2. `heat3d-dcs-maps fit "<session>/heat.parquet"` ausféieren (oder eng `.jsonl` oder `.csv`).
3. Et gëtt déi gefëttte Projektioun als JSON aus, de Root-Mean-Square-Feeler iwwer
   d'Punkten, an d'`--projection`-Argumenter, déi ze benotze sinn.
4. D'Level domat bauen:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit op enger syntheteschen Opnam](../assets/img/fit.svg)

D'Opnam um Bild sinn néng Punkten aus enger bekannter Projektioun,
déi `fit` op de Millimeter zeréckfënnt.

| Argument | Mécht |
|---|---|
| `recording` | `.parquet`, `.jsonl` oder `.csv` mat de Kolonnen `lat`, `lon`, `x`, `z` (DCS-Meter); Zeilen, déi sech net liese loossen, ginn iwwersprong |

D'Projektioun ass d'Krüger-Serie, wéi C. F. F. Karney se gëtt („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).

Exit-Status: 0 ee gudde Fit (ënner 5 m Root-Mean-Square); 1 ee schlechte Fit, oder
manner wéi dräi benotzbar Zeilen; 2 d'Datei gouf net fonnt.
