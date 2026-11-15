---
title: "Поиск театров: list"
nav_order: 2
lang: ru
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Поиск театров: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Впервые в командной строке? Сначала прочитайте [С чего начать](before-you-start.md).

1. Установите один раз: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, откройте
   терминал в этой папке и выполните `python -m pip install -e .` (нужен Python 3.10 или новее;
   он подтянет numpy, а для `fit` на `.parquet` — pyarrow).
2. Выполните `heat3d-dcs-maps list`.
3. Каждый установленный театр выводит одну строку: имя его папки (то, что принимают остальные
   команды), размер его файла земли, его тайлы и вершины, известна ли его проекция широты и долготы,
   и читается ли он. В конце каждой строки вы должны увидеть `readable`.

![list на синтетической установке](../assets/img/list.svg)

На картинке — запуск на установке, которую строят тесты (`tests/synth.py`), а не на самой игре.

## Где находится установка {#where-the-install-is-found}

`--dcs <folder>` (папка, где лежит `Mods\terrains`) или переменная окружения `DCS_PATH`; иначе
ищутся реестр, библиотеки Steam и обычные папки.

| Параметр | Что делает |
|---|---|
| `--dcs FOLDER` | папка DCS World, та, в которой лежит `Mods\terrains` |

Код выхода: 0 — готово; 2 — установка или театр не найдены.
