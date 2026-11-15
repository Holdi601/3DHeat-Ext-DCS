---
title: "Hitta teatrar: list"
nav_order: 2
lang: "sv"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Hitta teatrar: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Har du aldrig använt kommandoraden förut? Läs [Innan du börjar](before-you-start.md) först.

1. Installera en gång: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, öppna
   en terminal i mappen och kör `python -m pip install -e .` (Python 3.10
   eller senare; det tar med sig numpy, och pyarrow för `fit` på en `.parquet`).
2. Kör `heat3d-dcs-maps list`.
3. Varje installerad teater skriver en rad: dess mappnamn (namnet de andra kommandona tar), storleken på dess markfil, dess kakelrutor och hörn, om dess latitud/longitud-projektion är känd, och om den kan läsas.
   Du bör se `readable` i slutet av varje rad.

![list på en syntetisk installation](../assets/img/list.svg)

Bilden är en körning på en installation som testerna skapar (`tests/synth.py`), inte på spelet.

## Var installationen hittas {#where-the-install-is-found}

`--dcs <folder>` (mappen som innehåller `Mods\terrains`) eller miljövariabeln `DCS_PATH`; annars söks registret, Steam-biblioteken och de vanliga mapparna.

| Alternativ | Gör |
|---|---|
| `--dcs FOLDER` | DCS World-mappen, den som innehåller `Mods\terrains` |

Avslutskod: 0 klart, 2 ingen installation eller teater hittades.
