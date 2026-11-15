---
title: "Названия мест: towns"
nav_order: 5
lang: ru
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Названия мест: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Выводит названия мест театра из его `map/towns.lua` (читается как текст, никогда не выполняется)
в виде JSON: название каждого города, его широта и долгота, а также его `x` (север) и `z`
(восток) в метрах DCS через проекцию театра.

1. Найдите имя папки театра с помощью [`list`](list.md).
2. Выполните `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Используйте `x`/`z`, чтобы подписать уровень или проверить позиции записи.

![towns на синтетической установке](../assets/img/towns.svg)

| Параметр | Что делает |
|---|---|
| `theatre` | имя папки в `Mods\terrains` |
| `--dcs FOLDER` | папка DCS World |

Города внутри региона уровня также есть в его `<name>.json`, с высотой земли под каждым
([Файлы уровня](output.md)).
