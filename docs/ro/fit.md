---
title: "Proiecții: fit"
nav_order: 6
lang: ro
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Proiecții: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Fiecare teatru este o proiecție Transverse Mercator cu constantele sale proprii. Instrumentul
le cunoaște pentru teatrele pe care a fost verificat; pentru unul pe care nu îl cunoaște,
`fit` le găsește dintr-o înregistrare oarecare care conține și latitudinea/longitudinea, și
metrii DCS, cum ar fi o sesiune a 3DHeat Watcher dintr-un singur zbor.

1. Înregistrați un zbor pe teatrul respectiv cu 3DHeat Watcher (sau faceți orice înregistrare cu
   coloanele `lat`, `lon`, `x`, `z` în metri DCS: x este metri spre nord, z metri spre est, așa
   cum este peste tot în DCS).
2. Rulați `heat3d-dcs-maps fit "<session>/heat.parquet"` (sau un `.jsonl` sau `.csv`).
3. Afișează proiecția găsită ca JSON, eroarea pătratică medie pe puncte și argumentele
   `--projection` de folosit.
4. Construiți nivelul cu ele:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit pe o înregistrare sintetică](../assets/img/fit.svg)

Înregistrarea din imagine are nouă puncte făcute dintr-o proiecție cunoscută, pe care `fit` o
găsește înapoi până la milimetru.

| Argument | Ce face |
|---|---|
| `recording` | `.parquet`, `.jsonl` sau `.csv` cu coloanele `lat`, `lon`, `x`, `z` (metri DCS); rândurile care nu se citesc sunt sărite |

Proiecția este seria lui Krüger, așa cum o dă C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers”, Journal of Geodesy 85, 2011).

Codul de stare: 0 înseamnă o potrivire bună (sub 5 m eroare pătratică medie); 1 înseamnă o potrivire slabă sau
mai puțin de trei rânduri utilizabile; 2 înseamnă că fișierul nu a fost găsit.
