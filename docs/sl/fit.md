---
title: "Projekcije: fit"
nav_order: 6
lang: "sl"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcije: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <posnetek>
```

Vsak teater je projekcija Transverse Mercator s svojimi konstantami. Orodje jih pozna za
teatre, na katerih je bilo preverjeno; za teater, ki ga ne pozna, `fit` poišče konstante iz
vsakega posnetka, ki vsebuje zemljepisno širino in dolžino ter metre DCS, na primer seje
3DHeat Watcher enega leta.

1. Posnemi let nad teatrom z 3DHeat Watcherjem (ali naredi kak posnetek s stolpci `lat`, `lon`,
   `x`, `z` v metrih DCS: x je meter proti severu, z meter proti vzhodu, kot povsod v DCS).
2. Zaženi `heat3d-dcs-maps fit "<seja>/heat.parquet"` (ali `.jsonl` ali `.csv`).
3. Izpiše prilagojeno projekcijo kot JSON, koren povprečne kvadratne napake čez točke in
   argumente `--projection`, ki jih je treba uporabiti.
4. Z njimi zgradi raven:
   `heat3d-dcs-maps level <teater> --projection <LON0> <FE> <FN> -o levels`.

![fit na sintetičnem posnetku](../assets/img/fit.svg)

Posnetek na sliki je devet točk, narejenih iz znane projekcije, ki jo `fit` najde nazaj
na milimeter natančno.

| Argument | Naredi |
|---|---|
| `posnetek` | `.parquet`, `.jsonl` ali `.csv` s stolpci `lat`, `lon`, `x`, `z` (metri DCS); vrstice, ki se ne preberejo, se preskočijo |

Projekcija je Krügerjeva vrsta, kot jo podaja C. F. F. Karney ("Transverse Mercator with an
accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Izhodna koda: 0 dobro prilagajanje (pod 5 m koren povprečne kvadratne napake); 1 slabo
prilagajanje ali manj kot tri uporabne vrstice; 2 datoteka ni bila najdena.
