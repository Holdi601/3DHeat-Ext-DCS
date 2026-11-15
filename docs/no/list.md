---
title: "Finne teatre: list"
nav_order: 2
lang: "no"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Finne teatre: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ny til kommandolinjen? Les [Før du starter](before-you-start.md) først.

1. Installer én gang: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, åpne
   en terminal i den mappen og kjør `python -m pip install -e .` (Python 3.10
   eller nyere; det henter numpy, og pyarrow for `fit` på en `.parquet`).
2. Kjør `heat3d-dcs-maps list`.
3. Hvert installerte teater skriver ut én linje: mappenavnet (navnet de andre
   kommandoene tar), størrelsen på bakkefilen, flisene og toppunktene,
   om dets breddegrad/lengdegrad-projeksjon er kjent, og om det kan leses.
   Du bør se `readable` til slutt på hver linje.

![list på en syntetisk installasjon](../assets/img/list.svg)

Bildet er en kjøring på en installasjon testene lager (`tests/synth.py`), ikke på
spillet.

## Hvor installasjonen finnes {#where-the-install-is-found}

`--dcs <folder>` (mappen som holder `Mods\terrains`) eller miljøvariabelen `DCS_PATH`;
ellers søkes registeret, Steam-bibliotekene og de vanlige mappene.

| Alternativ | Gjør |
|---|---|
| `--dcs FOLDER` | DCS World-mappen, den som holder `Mods\terrains` |

Avslutningsstatus: 0 ferdig, 2 ingen installasjon eller intet teater funnet.
