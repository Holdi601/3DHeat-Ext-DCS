---
title: "Projektionen: fit"
nav_order: 6
lang: de
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektionen: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Jeder Schauplatz ist eine Transversale-Mercator-Projektion mit eigenen Konstanten. Das Werkzeug kennt sie
für die Schauplätze, an denen es geprüft wurde; für einen unbekannten findet `fit` sie aus jeder
Aufnahme, die sowohl Breiten- und Längengrad als auch DCS-Meter enthält, etwa aus einer
3DHeat-Watcher-Sitzung eines einzigen Flugs.

1. Nimm einen Flug auf dem Schauplatz mit dem 3DHeat Watcher auf (oder mach eine beliebige Aufnahme
   mit den Spalten `lat`, `lon`, `x`, `z` in DCS-Metern: x sind Meter nach Norden, z Meter nach Osten,
   wie überall in DCS).
2. Führe `heat3d-dcs-maps fit "<session>/heat.parquet"` aus (oder eine `.jsonl`- oder `.csv`-Datei).
3. Es gibt die gefundene Projektion als JSON aus, den mittleren quadratischen Fehler über die
   Punkte und die `--projection`-Argumente, die du verwenden sollst.
4. Baue das Level damit:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit an einer synthetischen Aufnahme](../assets/img/fit.svg)

Die Aufnahme im Bild sind neun Punkte aus einer bekannten Projektion, und `fit` findet sie bis auf den Millimeter zurück.

| Argument | Wirkung |
|---|---|
| `recording` | `.parquet`, `.jsonl` oder `.csv` mit den Spalten `lat`, `lon`, `x`, `z` (DCS-Meter); Zeilen, die sich nicht lesen lassen, werden übersprungen |

Die Projektion ist Krügers Reihe, so wie C. F. F. Karney sie angibt ("Transverse Mercator with an accuracy of a few nanometers",
Journal of Geodesy 85, 2011).

Exit-Status: 0 eine gute Anpassung (unter 5 m mittlerer quadratischer Fehler); 1 eine schlechte Anpassung oder
weniger als drei brauchbare Zeilen; 2 die Datei wurde nicht gefunden.
