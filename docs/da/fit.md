---
title: "Projektioner: fit"
nav_order: 6
lang: da
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektioner: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Hvert teater er en Transverse Mercator-projektion med sine egne konstanter. Værktøjet kender dem
for de teatre, det er blevet kontrolleret på; for et, det ikke kender, finder
`fit` dem ud fra en hvilken som helst optagelse, der indeholder både breddegrad/længdegrad og
DCS-meter, som en 3DHeat Watcher-session af én flyvning.

1. Optag en flyvning på teatret med 3DHeat Watcher (eller lav en hvilken som helst
   optagelse med kolonnerne `lat`, `lon`, `x`, `z` i DCS-meter: x er meter
   nord, z meter øst, som overalt i DCS).
2. Kør `heat3d-dcs-maps fit "<session>/heat.parquet"` (eller en `.jsonl`- eller `.csv`-fil).
3. Den udskriver den fittede projektion som JSON, rodmiddelkvadratfejlen over
   punkterne, og argumenterne `--projection`, der skal bruges.
4. Byg banen med dem:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit på en syntetisk optagelse](../assets/img/fit.svg)

Optagelsen på billedet er ni punkter lavet ud fra en kendt projektion,
som `fit` finder tilbage til millimeteren.

| Argument | Gør |
|---|---|
| `recording` | `.parquet`, `.jsonl` eller `.csv` med kolonnerne `lat`, `lon`, `x`, `z` (DCS-meter); rækker, der ikke kan læses, springes over |

Projektionen er Krügers række, som C. F. F. Karney giver den ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Exit-status: 0 en god pasform (under 5 m rodmiddelkvadrat); 1 en dårlig pasform, eller
færre end tre brugbare rækker; 2 filen blev ikke fundet.
