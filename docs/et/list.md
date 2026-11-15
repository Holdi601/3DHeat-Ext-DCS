---
title: "Teatrite leidmine: list"
nav_order: 2
lang: "et"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Teatrite leidmine: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Pole sul käsurealt kogemust? Loe esmalt [Enne alustamist](before-you-start.md).

1. Paigalda üks kord: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, ava
   terminal selles kaustas ja käivita `python -m pip install -e .` (Python 3.10
   või uuem; see toob kaasa numpy, ja pyarrow'd `fit` jaoks `.parquet`-failil).
2. Käivita `heat3d-dcs-maps list`.
3. Iga paigaldatud teater prindib ühe rea: tema kaustanime (nime, mida teised käsud võtavad), maapinna faili suuruse, kahhelid ja tipud,
   selle, kas tema laiuskraadi/pikkuskraadi projektsioon on teada, ja kas ta loetakse. Iga rea lõpus peaks olema `readable`.

![list sünteetilisel installil](../assets/img/list.svg)

Pilt on käivitus installil, mille testid koostavad (`tests/synth.py`), mitte mängul.

## Kust install leitakse {#where-the-install-is-found}

`--dcs <folder>` (kaust, mis hoiab `Mods\terrains`) või keskkonnamuutuja `DCS_PATH`;
muidu otsitakse registrist, Steami raamatukogudest ja tavalistest kaustadest.

| Valik | Teeb |
|---|---|
| `--dcs FOLDER` | DCS World'i kaust, see, mis hoiab `Mods\terrains` |

Väljumisolek: 0 valmis, 2 installi või teatrit ei leitud.
