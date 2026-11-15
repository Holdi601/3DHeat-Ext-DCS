---
title: "Vetítések: fit"
nav_order: 6
lang: "hu"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Vetítések: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Minden színház egy saját állandókkal rendelkező Transverse Mercator-vetítés. Az eszköz ismeri
ezeket azokhoz a színházakhoz, amelyeken ellenőrizték; egy ismeretlenhez a `fit` olyan felvételből
határozza meg őket, amely szélességet és hosszúságot is tartalmaz, valamint DCS-métereket, például
egy 3DHeat Watcher munkamenetből egy repülésről.

1. Rögzíts egy repülést a színházon a 3DHeat Watcherrel (vagy készíts bármilyen felvételt,
   amelynek oszlopai `lat`, `lon`, `x`, `z`, DCS-méterekben: az x méter észak felé, a z méter
   kelet felé, ahogy a DCS-ben mindenütt).
2. Futtasd a `heat3d-dcs-maps fit "<session>/heat.parquet"` parancsot (vagy egy `.jsonl`
   vagy `.csv` fájlt).
3. Kiírja az illesztett vetítést JSON-ként, a pontokra vett átlagos négyzetes hibát (root mean
   square), és a használandó `--projection` argumentumokat.
4. Építsd meg vele a pályát:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit egy szintetikus felvételen](../assets/img/fit.svg)

Az ábrán lévő felvétel kilenc pont egy ismert vetítésből, amelyet a `fit` a milliméterig visszatalál.

| Argumentum | Mit csinál |
|---|---|
| `recording` | `.parquet`, `.jsonl` vagy `.csv`, oszlopokkal: `lat`, `lon`, `x`, `z` (DCS-méter); az olvashatatlan sorok kimaradnak |

A vetítés Krüger-sorozata, ahogy C. F. F. Karney adja meg („Transverse Mercator with an accuracy
of a few nanometers”, Journal of Geodesy 85, 2011).

Kilépési állapot: 0 jó illesztés (5 m alatti átlagos négyzetes hiba); 1 gyenge illesztés, vagy
három-nál kevesebb használható sor; 2 a fájl nem található.
