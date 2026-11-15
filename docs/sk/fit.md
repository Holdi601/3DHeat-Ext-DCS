---
title: "Projekcie: fit"
nav_order: 6
lang: sk
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcie: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Každé územie je projekcia Transverse Mercator so svojimi konštantami. Nástroj ich pozná pre územia, na ktorých bol overený; pre územie, ktoré nepozná, `fit` nájde konštanty z ľubovoľného záznamu, ktorý obsahuje zemepisnú šírku a dĺžku aj metre DCS, napríklad zo záznamu jedného letu v 3DHeat Watcher.

1. Nahrajte let nad územím pomocou 3DHeat Watcher (alebo ľubovoľný záznam so stĺpcami `lat`, `lon`, `x`, `z` v metroch DCS: x sú metre na sever, z metre na východ, ako všade v DCS).
2. Spustite `heat3d-dcs-maps fit "<session>/heat.parquet"` (alebo `.jsonl` či `.csv`).
3. Vypíše nájdenú projekciu ako JSON, strednú kvadratickú chybu na bodoch
   a argumenty `--projection`, ktoré treba použiť.
4. Vytvorte úroveň s nimi:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit na syntetickom zázname](../assets/img/fit.svg)

Záznam na obrázku je deväť bodov vytvorených zo známej projekcie, ktorú `fit` nájde späť s presnosťou na milimeter.

| Argument | Čo robí |
|---|---|
| `recording` | `.parquet`, `.jsonl` alebo `.csv` so stĺpcami `lat`, `lon`, `x`, `z` (metre DCS); riadky, ktoré sa nedajú prečítať, sa preskočia |

Projekcia je Krügerov rad, ako ho podáva C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).

Stavový kód: 0 dobrá zhoda (pod 5 m stredná kvadratická chyba); 1 slabá zhoda alebo menej ako tri použiteľné riadky; 2 súbor sa nenašiel.
