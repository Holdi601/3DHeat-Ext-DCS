---
title: "Projekce: fit"
nav_order: 6
lang: cs
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekce: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Každé území je projekce Transverse Mercator s vlastními konstantami. Nástroj je zná pro
území, na kterých byl ověřen; pro území, které nezná, `fit` najde konstanty z libovolného
záznamu, který obsahuje zeměpisnou šířku a délku i metry DCS, například relaci 3DHeat Watcher
jednoho letu.

1. Nahrajte let nad územím pomocí 3DHeat Watcher (nebo udělejte jakýkoli záznam se sloupci `lat`, `lon`, `x`, `z`
   v metrech DCS: x jsou metry na sever, z metry na východ, jako všude v DCS).
2. Spusťte `heat3d-dcs-maps fit "<session>/heat.parquet"` (nebo `.jsonl` či `.csv`).
3. Vypíše nalezenou projekci jako JSON, střední kvadratickou chybu přes body
   a argumenty `--projection`, které máte použít.
4. Sestavte úroveň s nimi:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit na syntetickém záznamu](../assets/img/fit.svg)

Záznam na obrázku je devět bodů vytvořených ze známé projekce; `fit` ji najde zpět
na milimetr.

| Argument | Co dělá |
|---|---|
| `recording` | `.parquet`, `.jsonl` nebo `.csv` se sloupci `lat`, `lon`, `x`, `z` (metry DCS); řádky, které se nedají přečíst, se přeskočí |

Projekce je Krügerova řada, jak ji podává C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).

Stavový kód: 0 dobré přizpůsobení (střední kvadratická chyba pod 5 m); 1 špatné přizpůsobení,
nebo méně než tři použitelné řádky; 2 soubor nebyl nalezen.
