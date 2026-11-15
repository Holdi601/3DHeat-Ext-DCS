---
title: "Назви місць: towns"
nav_order: 5
lang: uk
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Назви місць: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Виводить назви місць театру з його `map/towns.lua` (читається як текст, ніколи не
виконується) у форматі JSON: назву кожного міста, його широту і довготу та його DCS
`x` (північ) і `z` (схід) у метрах через проєкцію театру.

1. Знайдіть назву папки театру за допомогою [`list`](list.md).
2. Виконайте `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Використовуйте `x`/`z`, щоб підписати рівень або перевірити позиції із запису.

![міста на синтетичній інсталяції](../assets/img/towns.svg)

| Параметр | Що робить |
|---|---|
| `theatre` | назва папки в `Mods\terrains` |
| `--dcs FOLDER` | папка DCS World |

Міста всередині регіону рівня також містяться у його `<name>.json` разом із висотою землі
під кожним ([Файли рівня](output.md)).
