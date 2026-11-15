---
title: "Назвы месцаў: towns"
nav_order: 5
lang: "be"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Назвы месцаў: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Друкуе назвы месцаў тэатра з яго `map/towns.lua` (чытаецца як тэкст,
ніколі не выконваецца) як JSON: назва кожнага горада, яго шырата і даўгата, і
яго `x` (поўнач) і `z` (усход) DCS у метрах, праз праекцыю тэатра.

1. Знайдзіце назву папкі тэатра праз [`list`](list.md).
2. Выканайце `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Выкарыстоўвайце `x`/`z`, каб падпісаць узровень або праверыць пазіцыі запісу.

![towns на сінтэтычнай усталёўцы](../assets/img/towns.svg)

| Опцыя | Што робіць |
|---|---|
| `theatre` | назва папкі пад `Mods\terrains` |
| `--dcs FOLDER` | папка DCS World |

Гарады ў рэгіёне ўзроўню ёсць таксама ў яго `<name>.json`, з
вышынёй зямлі пад кожным ([Файлы ўзроўню](output.md)).
