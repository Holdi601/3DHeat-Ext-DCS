---
title: "Пошук тэатраў: list"
nav_order: 2
lang: be
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Пошук тэатраў: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Упершыню ў камандным радку? Спачатку прачытайце [Перад пачаткам](before-you-start.md).

1. Усталюйце адзін раз: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, адкрыйце
   тэрмінал у гэтай папцы і выканайце `python -m pip install -e .` (Python 3.10
   або навейшы; ён прыносіць numpy і pyarrow для `fit` на `.parquet`).
2. Выканайце `heat3d-dcs-maps list`.
3. Кожны ўсталяваны тэатр друкуецца ў адным радку: назва яго папкі (імя, якое
   прымаюць іншыя каманды), памер файла зямлі, пліткі і вяршыні,
   ці вядомая яго праекцыя шыраты/даўготы і ці чытаецца ён.
   У канцы кожнага радка вы ўбачыце `readable`.

![list на сінтэтычнай усталёўцы](../assets/img/list.svg)

Малюнак — гэта запуск на ўсталёўцы, якую будуюць тэсты (`tests/synth.py`), а не на
гульні.

## Дзе знаходзіцца ўсталёўка {#where-the-install-is-found}

`--dcs <folder>` (папка з `Mods\terrains`) або зменная асяроддзя
`DCS_PATH`; інакш шукаюць у рэестры, бібліятэках Steam і
звычайных папках.

| Опцыя | Што робіць |
|---|---|
| `--dcs FOLDER` | папка DCS World, тая, што змяшчае `Mods\terrains` |

Статус выхаду: 0 — гатова, 2 — усталёўка або тэатр не знойдзены.
