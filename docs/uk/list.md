---
title: "Пошук театрів: list"
nav_order: 2
lang: uk
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Пошук театрів: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ви лише починаєте працювати з командним рядком? Спершу прочитайте [Перш ніж почати](before-you-start.md).

1. Встановіть один раз: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`,
   відкрийте термінал у цій папці і виконайте `python -m pip install -e .` (Python 3.10
   або новіший; він приносить numpy, а для `fit` на `.parquet` — pyarrow).
2. Виконайте `heat3d-dcs-maps list`.
3. Кожен встановлений театр виводить один рядок: назву його папки (назву, яку
   приймають інші команди), розмір його файлу землі, його тайли і вершини, чи відома
   його проєкція широти/довготи, і чи його можна прочитати. Наприкінці кожного
   рядка ви маєте побачити `readable`.

![list на синтетичній інсталяції](../assets/img/list.svg)

Малюнок — це запуск на інсталяції, яку будують тести (`tests/synth.py`), а не на
самій грі.

## Де шукається інсталяція {#where-the-install-is-found}

`--dcs <folder>` (папка, в якій лежить `Mods\terrains`) або змінна середовища
`DCS_PATH`; інакше шукаються реєстр, бібліотеки Steam і звичайні папки.

| Параметр | Що робить |
|---|---|
| `--dcs FOLDER` | папка DCS World, та, що містить `Mods\terrains` |

Код виходу: 0 — готово, 2 — інсталяцію або театр не знайдено.
