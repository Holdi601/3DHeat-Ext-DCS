---
title: "Theatere fannen: list"
nav_order: 2
lang: lb
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Theatere fannen: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nei op der Kommandozeil? Liest fir d'éischt [Ier Dir ufänkt](before-you-start.md).

1. Eemol installéieren: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, e
   Terminal an deem Ordner opmaachen an `python -m pip install -e .` ausféieren (Python 3.10
   oder méi nei; et bréngt numpy mat, an pyarrow fir `fit` op enger `.parquet`).
2. `heat3d-dcs-maps list` ausféieren.
3. All installéiert Theater gëtt eng Zeil aus: säin Ordnernumm (den Numm, dee
   déi aner Kommandoe huelen), d'Gréisst vu senger Buedemdatei, seng Kachele a Vertices,
   ob seng Breeden-/Längtegrad-Projektioun bekannt ass, an ob et sech liese léisst.
   Dir sollt um Enn vun all Zeil `readable` gesinn.

![list op enger syntheteschen Installatioun](../assets/img/list.svg)

D'Bild ass en Duerchlaf op enger Installatioun, déi d'Tester bauen (`tests/synth.py`), net op
dem Spill.

## Wou d'Installatioun fonnt gëtt {#where-the-install-is-found}

`--dcs <folder>` (den Ordner mat `Mods\terrains`) oder d'`DCS_PATH`-
Ëmgéigungsvariabel; soss ginn d'Registry, d'Steam-Bibliothéiken an d'
gewéinlech Ordner duerchsicht.

| Optioun | Mécht |
|---|---|
| `--dcs FOLDER` | den DCS-World-Ordner, deen mat `Mods\terrains` |

Exit-Status: 0 fäerdeg, 2 keng Installatioun oder kee Theater fonnt.
