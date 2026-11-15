---
title: "Pronalaženje karata: list"
nav_order: 2
lang: "hr"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Pronalaženje karata: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ne znate ništa o naredbenom retku? Prvo pročitajte [Prije nego što počnete](before-you-start.md).

1. Instalirajte jednom: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, otvorite
   terminal u toj mapi i pokrenite `python -m pip install -e .` (Python 3.10
   ili noviji; donosi numpy, a pyarrow za `fit` na `.parquet` datoteci).
2. Pokrenite `heat3d-dcs-maps list`.
3. Svaka instalirana karta ispisuje jedan redak: ime mape (ime koje uzimaju ostale naredbe), veličinu njezine datoteke tla, njezine pločice i vrhove, je li njezina projekcija geografske širine/dužine poznata i može li se čitati. Na kraju svakog retka trebali biste vidjeti `readable`.

![list na sintetičkoj instalaciji](../assets/img/list.svg)

Slika prikazuje pokretanje na instalaciji koju grade testovi (`tests/synth.py`), a ne na igri.

## Gdje se nalazi instalacija {#where-the-install-is-found}

`--dcs <folder>` (mapa koja sadrži `Mods\terrains`) ili varijabla okruženja `DCS_PATH`; inače se pretražuju registar, Steam biblioteke i uobičajene mape.

| Opcija | Što radi |
|---|---|
| `--dcs FOLDER` | mapa DCS Worlda, ona koja sadrži `Mods\terrains` |

Izlazni status: 0 gotovo, 2 nije pronađena instalacija ni karta.
