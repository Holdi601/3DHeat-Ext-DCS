---
title: "Găsirea teatrelor: list"
nav_order: 2
lang: "ro"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Găsirea teatrelor: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nu ați mai lucrat în linia de comandă? Citiți mai întâi [Înainte de a începe](before-you-start.md).

1. Instalați o singură dată: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, deschideți
   un terminal în acel dosar și rulați `python -m pip install -e .` (Python 3.10 sau mai nou; aduce
   numpy, iar pentru `fit` pe un `.parquet` și pyarrow).
2. Rulați `heat3d-dcs-maps list`.
3. Fiecare teatru instalat afișează o linie: numele dosarului său (numele pe care îl primesc celelalte
   comenzi), dimensiunea fișierului său de sol, plăcile și vârfurile sale, dacă proiecția sa latitudine/longitudine
   este cunoscută și dacă se poate citi. Ar trebui să vedeți `readable` la finalul fiecărei linii.

![list pe o instalare sintetică](../assets/img/list.svg)

Imaginea este o rulare pe o instalare pe care o construiesc testele (`tests/synth.py`), nu pe joc.

## Unde se găsește instalarea {#where-the-install-is-found}

`--dcs <folder>` (dosarul care conține `Mods\terrains`) sau variabila de mediu `DCS_PATH`; altfel
se caută în registru, în bibliotecile Steam și în dosarele obișnuite.

| Opțiune | Ce face |
|---|---|
| `--dcs FOLDER` | dosarul DCS World, cel care conține `Mods\terrains` |

Codul de stare: 0 gata; 2 nu s-a găsit nicio instalare sau niciun teatru.
