---
title: "Projecties: fit"
nav_order: 6
lang: nl
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projecties: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Elk thema is een Transverse Mercator-projectie met zijn eigen constanten. De tool kent ze voor de thema's
waarop hij is gecontroleerd; voor een thema dat hij niet kent, vindt `fit` ze uit elke opname die
zowel breedte-/lengtegraad als DCS-meters bevat, zoals een sessie van de 3DHeat Watcher met één vlucht.

1. Neem een vlucht op het thema op met de 3DHeat Watcher (of maak een andere opname met de kolommen `lat`, `lon`, `x`, `z` in DCS-meters:
   x is meters naar het noorden, z meters naar het oosten, zoals overal in DCS).
2. Voer `heat3d-dcs-maps fit "<session>/heat.parquet"` uit (of een `.jsonl`- of `.csv`-bestand).
3. Het drukt de gevonden projectie af als JSON, de wortel uit de gemiddelde kwadratische fout over
   de punten, en de argumenten `--projection` om te gebruiken.
4. Bouw het level ermee:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit op een synthetische opname](../assets/img/fit.svg)

De opname in de afbeelding bestaat uit negen punten, gemaakt uit een bekende projectie,
die `fit` tot op de millimeter terugvindt.

| Argument | Doet |
|---|---|
| `recording` | `.parquet`, `.jsonl` of `.csv` met de kolommen `lat`, `lon`, `x`, `z` (DCS-meters); rijen die niet gelezen kunnen worden, worden overgeslagen |

De projectie is die van Krüger, zoals C. F. F. Karney die geeft ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Exitstatus: 0 een goede pasvorm (onder 5 m wortel uit de gemiddelde kwadratische fout); 1 een slechte pasvorm, of
minder dan drie bruikbare rijen; 2 het bestand is niet gevonden.
