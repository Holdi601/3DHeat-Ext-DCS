---
title: "Színházak keresése: list"
nav_order: 2
lang: hu
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Színházak keresése: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Még nem használt parancssort? Előbb olvassa el a [Mielőtt elkezdi](before-you-start.md) oldalt.

1. Telepítés egyszer: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, nyisson terminált
   ebben a mappában, és futtassa a `python -m pip install -e .` parancsot (Python 3.10 vagy
   újabb; ez hozza a numpy-t, és a pyarrow-t a `fit` parancshoz `.parquet` fájlon).
2. Futtassa a `heat3d-dcs-maps list` parancsot.
3. Minden telepített színház egy sort ír ki: a mappanevét (ezt veszik át a többi parancs), a talajfájl
   méretét, a csempéit és csúcsait, azt, hogy ismert-e a szélességi/hosszúsági vetítése, és hogy
   olvasható-e. Minden sor végén `readable` szót kell látnia.

![list egy szintetikus telepítésen](../assets/img/list.svg)

Az ábra egy olyan telepítésen készült futtatás, amelyet a tesztek építenek (`tests/synth.py`),
nem a játékon.

## Hol található a telepítés {#where-the-install-is-found}

`--dcs <folder>` (az a mappa, amelyben a `Mods\terrains` van), vagy a `DCS_PATH` környezeti változó;
egyébként a rendszerleíró adatbázisban, a Steam-könyvtárakban és a szokásos mappákban keres.

| Kapcsoló | Mit csinál |
|---|---|
| `--dcs FOLDER` | a DCS World mappa, amelyben a `Mods\terrains` található |

Kilépési állapot: 0 kész, 2 nincs telepítés vagy színház.
