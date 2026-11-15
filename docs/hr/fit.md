---
title: "Projekcije: fit"
nav_order: 6
lang: hr
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcije: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Svaka karta je Transverzalna Mercatorova projekcija sa svojim konstantama. Alat ih poznaje za karte na kojima je provjeren; za onu koju ne poznaje, `fit` ih pronalazi iz bilo koje snimke koja sadrži i geografsku širinu/dužinu i DCS metre, na primjer sesiju programa 3DHeat Watcher jednog leta.

1. Snimite let nad kartom programom 3DHeat Watcher (ili napravite bilo koju snimku sa stupcima `lat`, `lon`, `x`, `z` u DCS metrima: x su metri na sjever, z metri na istok, kao i svugdje u DCS-u).
2. Pokrenite `heat3d-dcs-maps fit "<session>/heat.parquet"` (ili `.jsonl` ili `.csv`).
3. Ispisuje prilagođenu projekciju kao JSON, korijensku srednju kvadratnu pogrešku po točkama i argumente `--projection` za upotrebu.
4. Izradite razinu s njima:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit na sintetičkoj snimci](../assets/img/fit.svg)

Snimka na slici je devet točaka napravljenih iz poznate projekcije, koju `fit` pronalazi natrag do milimetra.

| Argument | Što radi |
|---|---|
| `recording` | `.parquet`, `.jsonl` ili `.csv` sa stupcima `lat`, `lon`, `x`, `z` (DCS metri); redci koji se ne mogu pročitati preskaču se |

Projekcija je Krügerov niz kako ga daje C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Izlazni status: 0 dobra prilagodba (ispod 5 m korijenske srednje kvadratne pogreške); 1 loša prilagodba ili manje od tri upotrebljiva retka; 2 datoteka nije pronađena.
