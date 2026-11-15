---
title: "Projektiot: fit"
nav_order: 6
lang: fi
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektiot: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Jokainen teatteri on Transverse Mercator -projektio omilla vakioillaan. Työkalu tuntee ne
teattereille, joilla se on testattu; teatterille, jota se ei tunne, `fit` löytää ne mistä tahansa
tallenteesta, jossa on sekä leveys- ja pituusaste että DCS-metrit, kuten yhden lennon
3DHeat Watcher -istunnosta.

1. Tallenna lento teatterilla 3DHeat Watcherilla (tai tee mikä tahansa tallenne, jossa on sarakkeet
   `lat`, `lon`, `x`, `z` DCS-metreinä: x on metriä pohjoiseen, z metriä itään, kuten kaikkialla DCS:ssä).
2. Suorita `heat3d-dcs-maps fit "<session>/heat.parquet"` (tai `.jsonl`- tai `.csv`-tiedosto).
3. Se tulostaa sovitetun projektion JSON-muodossa, pisteiden juuren keskineliövirheen ja
   `--projection`-argumentit, joita käytetään.
4. Rakenna kenttä niillä:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit synteettisellä tallenteella](../assets/img/fit.svg)

Kuvan tallenne on yhdeksän pistettä, jotka on tehty tunnetusta projektiosta; `fit` löytää sen
takaisin millimetrin tarkkuudella.

| Argumentti | Tekee |
|---|---|
| `recording` | `.parquet`, `.jsonl` tai `.csv` sarakkeilla `lat`, `lon`, `x`, `z` (DCS-metreinä); rivit, joita ei voi lukea, ohitetaan |

Projektio on Krügerin sarja sellaisena kuin C. F. F. Karney sen esittää ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Poistumistila: 0 hyvä sovitus (alle 5 m juuren keskineliövirhe); 1 huono sovitus tai alle
kolme käyttökelpoista riviä; 2 tiedostoa ei löytynyt.
