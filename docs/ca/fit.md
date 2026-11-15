---
title: "Projeccions: fit"
nav_order: 6
lang: "ca"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projeccions: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <gravació>
```

Cada teatre és una projecció Transverse Mercator amb les seves pròpies constants. L'eina
les coneix per als teatres amb què es va comprovar; per a un que no coneix,
`fit` les troba a partir de qualsevol gravació que tingui tant latitud/longitud com
metres de DCS, com una sessió d'un vol del Watcher de 3DHeat.

1. Grava un vol al teatre amb el Watcher de 3DHeat (o fes qualsevol gravació amb les columnes
   `lat`, `lon`, `x`, `z` en metres de DCS: x són metres cap al nord, z metres cap a l'est,
   com en tot DCS).
2. Executa `heat3d-dcs-maps fit "<sessió>/heat.parquet"` (o un `.jsonl` o `.csv`).
3. Imprimeix la projecció ajustada en JSON, l'error quadràtic mitjà arrel sobre
   els punts, i els arguments de `--projection` que cal fer servir.
4. Construeix el nivell amb ells:
   `heat3d-dcs-maps level <teatre> --projection <LON0> <FE> <FN> -o levels`.

![fit sobre una gravació sintètica](../assets/img/fit.svg)

La gravació de la imatge són nou punts fets a partir d'una projecció coneguda, que
`fit` recupera fins al mil·límetre.

| Argument | Què fa |
|---|---|
| `recording` | `.parquet`, `.jsonl` o `.csv` amb les columnes `lat`, `lon`, `x`, `z` (metres de DCS); les files que no es llegeixen s'ometen |

La projecció és la sèrie de Krüger tal com la va donar C. F. F. Karney («Transverse
Mercator with an accuracy of a few nanometers», Journal of Geodesy 85, 2011).

Estat de sortida: 0 un bon ajust (per sota de 5 m d'error quadràtic mitjà arrel); 1 un ajust
dolent, o menys de tres files utilitzables; 2 no s'ha trobat el fitxer.
