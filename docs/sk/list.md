---
title: "Hľadanie území: list"
nav_order: 2
lang: "sk"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Hľadanie území: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nikdy ste nepracovali s príkazovým riadkom? Najprv si prečítajte [Ako začať](before-you-start.md).

1. Nainštalujte raz: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, otvorte
   terminál v tom priečinku a spustite `python -m pip install -e .` (Python 3.10
   alebo novší; nainštaluje numpy a pyarrow pre `fit` na `.parquet`).
2. Spustite `heat3d-dcs-maps list`.
3. Každé nainštalované územie vypíše jeden riadok: názov priečinka (názov, ktorý berú ostatné príkazy), veľkosť jeho súboru zeme, jeho dlaždice a vrcholy,
   či je známa jeho projekcia zemepisnej šírky a dĺžky, a či sa dá čítať.
   Na konci každého riadka by ste mali vidieť `readable`.

![list na syntetickej inštalácii](../assets/img/list.svg)

Obrázok je spustenie na inštalácii, ktorú vytvárajú testy (`tests/synth.py`), nie na hre.

## Kde sa inštalácia nachádza {#where-the-install-is-found}

`--dcs <folder>` (priečinok, ktorý obsahuje `Mods\terrains`) alebo premenná prostredia
`DCS_PATH`; inak sa prehľadá register, knižnice Steam a obvyklé priečinky.

| Možnosť | Čo robí |
|---|---|
| `--dcs FOLDER` | priečinok DCS World, ten, ktorý obsahuje `Mods\terrains` |

Stavový kód: 0 hotovo, 2 nenájdená inštalácia alebo územie.
