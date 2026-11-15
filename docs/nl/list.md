---
title: "Thema's zoeken: list"
nav_order: 2
lang: "nl"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Thema's zoeken: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nog nooit met de opdrachtregel gewerkt? Lees eerst [Voordat je begint](before-you-start.md).

1. Installeer eenmalig: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, open
   een terminal in die map en voer `python -m pip install -e .` uit (Python 3.10
   of later; het haalt numpy mee, en pyarrow voor `fit` op een `.parquet`).
2. Voer `heat3d-dcs-maps list` uit.
3. Elk geïnstalleerd thema drukt één regel af: zijn mapnaam (de naam die de andere
   commando's gebruiken), de grootte van zijn grondbestand, zijn tegels en hoekpunten,
   of zijn projectie in breedte-/lengtegraad bekend is, en of het gelezen kan worden.
   Aan het eind van elke regel zie je `readable`.

![list op een synthetische installatie](../assets/img/list.svg)

De afbeelding is een run op een installatie die de tests bouwen (`tests/synth.py`), niet op
het spel zelf.

## Waar de installatie wordt gevonden {#where-the-install-is-found}

`--dcs <folder>` (de map die `Mods\terrains` bevat) of de omgevingsvariabele `DCS_PATH`;
anders worden het register, de Steam-bibliotheken en de gebruikelijke mappen doorzocht.

| Optie | Doet |
|---|---|
| `--dcs FOLDER` | de map van DCS World, die met `Mods\terrains` |

Exitstatus: 0 klaar, 2 geen installatie of geen thema gevonden.
