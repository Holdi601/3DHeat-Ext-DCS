---
title: "Find teatre: list"
nav_order: 2
lang: da
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Find teatre: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ny til kommandolinjen? Læs [Før du går i gang](before-you-start.md) først.

1. Installer én gang: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, åbn
   en terminal i den mappe, og kør `python -m pip install -e .` (Python 3.10
   eller nyere; det henter numpy med sig, og pyarrow til `fit` på en `.parquet`).
2. Kør `heat3d-dcs-maps list`.
3. Hvert installeret teater udskriver én linje: dets mappenavn (det navn de andre
   kommandoer tager), størrelsen af dets jordfil, dets flager og vertices,
   om dets breddegrad/længdegrad-projektion er kendt, og om det kan læses.
   Du bør se `readable` til sidst på hver linje.

![list på en syntetisk installation](../assets/img/list.svg)

Billedet er en kørsel på en installation, testene bygger (`tests/synth.py`), ikke på
spillet.

## Hvor installationen findes {#where-the-install-is-found}

`--dcs <folder>` (mappen, der indeholder `Mods\terrains`) eller miljøvariablen
`DCS_PATH`; ellers søges i registreringsdatabasen, Steam-bibliotekerne og de sædvanlige
mapper.

| Valgmulighed | Gør |
|---|---|
| `--dcs FOLDER` | DCS World-mappen, den der indeholder `Mods\terrains` |

Exit-status: 0 færdig, 2 ingen installation eller intet teater fundet.
