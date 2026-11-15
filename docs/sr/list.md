---
title: "Налажење театара: list"
nav_order: 2
lang: "sr"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Налажење театара: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Први пут у командној линији? Прво прочитајте [Пре почетка](before-you-start.md).

1. Инсталирајте једном: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, отворите
   терминал у тој фасцикли и покрените `python -m pip install -e .` (Python 3.10
   или новији; доноси numpy, а за `fit` над `.parquet` датотеком и pyarrow).
2. Покрените `heat3d-dcs-maps list`.
3. Сваки инсталирани театар исписује један ред: име његове фасцикле (име које
   узимају остале команде), величину његове датотеке тла, плочице и темена,
   да ли је његова пројекција географске ширине и дужине позната, и да ли се
   чита. На крају сваког реда требало би да видите `readable`.

![list на пробној инсталацији](../assets/img/list.svg)

Слика је покретање над инсталацијом коју прави тест (`tests/synth.py`), а не над
самом игром.

## Где се инсталација налази {#where-the-install-is-found}

`--dcs <folder>` (фасцикла која садржи `Mods\terrains`) или променљива окружења
`DCS_PATH`; иначе се претражују регистар, Steam библиотеке и уобичајене фасцикле.

| Опција | Шта ради |
|---|---|
| `--dcs FOLDER` | фасцикла DCS World-а, она која садржи `Mods\terrains` |

Излазни статус: 0 готово, 2 није нађена инсталација или театар.
