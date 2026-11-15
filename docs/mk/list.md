---
title: "Наоѓање театри: list"
nav_order: 2
lang: mk
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Наоѓање театри: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Нови сте со командната линија? Прво прочитајте [Пред да започнете](before-you-start.md).

1. Инсталирајте еднаш: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, отворете
   терминал во таа папка и пуштете `python -m pip install -e .` (Python 3.10
   или понов; носи numpy, и pyarrow за `fit` на `.parquet`).
2. Пуштете `heat3d-dcs-maps list`.
3. Секој инсталиран театар печати по една линија: името на неговата папка (името што го земаат
   другите команди), големината на неговата датотека со терен, неговите плочки (tiles) и темиња (vertices),
   дали неговата проекција за географска ширина/должина е позната, и дали се чита.
   На крајот од секоја линија треба да видите `readable`.

![list на синтетичка инсталација](../assets/img/list.svg)

Сликата е извршување на инсталација што ја градат тестовите (`tests/synth.py`), а не
на играта.

## Каде се наоѓа инсталацијата {#where-the-install-is-found}

`--dcs <folder>` (папката што ја содржи `Mods\terrains`) или променливата на околината
`DCS_PATH`; инаку се бараат регистарот, библиотеките на Steam и
вообичаените папки.

| Опција | Што прави |
|---|---|
| `--dcs FOLDER` | папката на DCS World, онаа што ја содржи `Mods\terrains` |

Излезен статус: 0 готово, 2 не е пронајдена инсталација или театар.
