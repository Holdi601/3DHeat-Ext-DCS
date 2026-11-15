---
title: "Projekcije: fit"
nav_order: 6
lang: bs
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcije: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Svaki teatar je Transverse Mercator projekcija s vlastitim konstantama. Alat
ih zna za teatre na kojima je provjeren; za teatar koji ne zna,
`fit` ih nalazi iz bilo kojeg snimka koji drži i geografsku širinu/dužinu i
DCS metre, kao što je sesija jednog leta u 3DHeat Watcheru.

1. Snimi let na teatru pomoću 3DHeat Watchera (ili napravi bilo koji
   snimak s kolonama `lat`, `lon`, `x`, `z` u DCS metrima: x su metri
   prema sjeveru, z metri prema istoku, kao svugdje u DCS-u).
2. Pokreni `heat3d-dcs-maps fit "<session>/heat.parquet"` (ili `.jsonl` ili `.csv`).
3. Ispisuje pronađenu projekciju kao JSON, korijen srednje kvadratne
   greške preko tačaka i argumente `--projection` koje treba koristiti.
4. Izgradi nivo s njima:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit na sintetičkom snimku](../assets/img/fit.svg)

Snimak na slici je devet tačaka napravljenih iz poznate projekcije,
koje `fit` pronalazi nazad do milimetra.

| Argument | Šta radi |
|---|---|
| `recording` | `.parquet`, `.jsonl` ili `.csv` s kolonama `lat`, `lon`, `x`, `z` (DCS metri); redovi koji se ne čitaju se preskaču |

Projekcija je Krügerov red kako ga daje C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Izlazni status: 0 dobro poklapanje (ispod 5 m korijena srednje kvadratne greške); 1 loše poklapanje ili
manje od tri upotrebljiva reda; 2 datoteka nije pronađena.
