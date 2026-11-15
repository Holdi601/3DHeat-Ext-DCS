---
title: "Pronalaženje teatara: list"
nav_order: 2
lang: bs
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Pronalaženje teatara: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Komandna linija ti je nova? Prvo pročitaj [Prije nego počneš](before-you-start.md).

1. Instaliraj jednom: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, otvori
   terminal u tom folderu i pokreni `python -m pip install -e .` (Python 3.10
   ili noviji; donosi numpy, te pyarrow za `fit` na `.parquet`).
2. Pokreni `heat3d-dcs-maps list`.
3. Svaki instalirani teatar ispisuje jedan red: naziv njegovog foldera (naziv koji uzimaju ostale
   naredbe), veličinu datoteke tla, pločice i vrhove,
   je li njegova projekcija geografske širine/dužine poznata i čita li se.
   Na kraju svakog reda trebao bi vidjeti `readable`.

![list na sintetičkoj instalaciji](../assets/img/list.svg)

Slika je pokretanje na instalaciji koju grade testovi (`tests/synth.py`), a ne na
igri.

## Gdje se instalacija pronalazi {#where-the-install-is-found}

`--dcs <folder>` (folder koji drži `Mods\terrains`) ili varijabla okruženja
`DCS_PATH`; inače se pretražuju registar, Steam biblioteke i
uobičajeni folderi.

| Opcija | Šta radi |
|---|---|
| `--dcs FOLDER` | folder DCS Worlda, onaj koji drži `Mods\terrains` |

Izlazni status: 0 gotovo, 2 nije pronađena instalacija ni teatar.
