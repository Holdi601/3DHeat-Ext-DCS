---
title: "Projections : fit"
nav_order: 6
lang: fr
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projections : `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <enregistrement>
```

Chaque théâtre est une projection de Transverse Mercator avec ses propres constantes. L'outil les
connaît pour les théâtres sur lesquels il a été vérifié ; pour un théâtre qu'il ne connaît pas,
`fit` les trouve à partir de tout enregistrement qui contient à la fois la latitude/longitude et les mètres DCS,
comme une session du 3DHeat Watcher d'un seul vol.

1. Enregistrez un vol sur le théâtre avec le 3DHeat Watcher (ou faites tout enregistrement
   avec les colonnes `lat`, `lon`, `x`, `z` en mètres DCS : x en mètres vers le nord, z en
   mètres vers l'est, comme partout dans DCS).
2. Lancez `heat3d-dcs-maps fit "<session>/heat.parquet"` (ou un `.jsonl` ou `.csv`).
3. Il affiche la projection ajustée en JSON, l'erreur quadratique moyenne sur les points, et les
   arguments `--projection` à utiliser.
4. Construisez le niveau avec ceux-ci :
   `heat3d-dcs-maps level <théâtre> --projection <LON0> <FE> <FN> -o levels`.

![fit sur un enregistrement synthétique](../assets/img/fit.svg)

L'enregistrement de l'image compte neuf points issus d'une projection connue, que `fit`
retrouve au millimètre près.

| Argument | Effet |
|---|---|
| `enregistrement` | un `.parquet`, `.jsonl` ou `.csv` avec les colonnes `lat`, `lon`, `x`, `z` (mètres DCS) ; les lignes qui ne se lisent pas sont ignorées |

La projection est la série de Krüger telle que la donne C. F. F. Karney (« Transverse
Mercator with an accuracy of a few nanometers », Journal of Geodesy 85, 2011).

Code de sortie : 0 un bon ajustement (moins de 5 m d'erreur quadratique moyenne) ; 1 un mauvais ajustement, ou
moins de trois lignes utilisables ; 2 le fichier est introuvable.
