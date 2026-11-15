---
title: "Schauplätze finden: list"
nav_order: 2
lang: "de"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Schauplätze finden: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Neu in der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).

1. Einmal installieren: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, ein Terminal in diesem Ordner öffnen
   und `python -m pip install -e .` ausführen (Python 3.10 oder neuer; es bringt numpy mit und pyarrow für `fit` auf einer `.parquet`-Datei).
2. Führe `heat3d-dcs-maps list` aus.
3. Jeder installierte Schauplatz gibt eine Zeile aus: sein Ordnername (den die anderen Befehle verwenden), die Größe
   seiner Bodendatei, seine Kacheln und Eckpunkte, ob seine Breiten-/Längengrad-Projektion bekannt ist, und ob er sich lesen lässt.
   Am Ende jeder Zeile solltest du `readable` sehen.

![list auf einer synthetischen Installation](../assets/img/list.svg)

Das Bild zeigt einen Lauf auf einer Installation, die die Tests bauen (`tests/synth.py`), nicht auf dem Spiel.

## Wo die Installation gefunden wird {#where-the-install-is-found}

`--dcs <folder>` (der Ordner, der `Mods\terrains` enthält) oder die Umgebungsvariable `DCS_PATH`;
sonst werden die Registry, die Steam-Bibliotheken und die üblichen Ordner durchsucht.

| Option | Wirkung |
|---|---|
| `--dcs FOLDER` | der DCS-World-Ordner, der `Mods\terrains` enthält |

Exit-Status: 0 fertig, 2 keine Installation oder kein Schauplatz gefunden.
