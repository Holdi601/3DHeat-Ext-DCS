---
title: "Пабудова ўзроўню: level"
nav_order: 3
lang: "be"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Пабудова ўзроўню: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Крок за крокам {#step-by-step}

Упершыню ў камандным радку? Спачатку прачытайце [Перад пачаткам](before-you-start.md).

1. Знайдзіце назву папкі тэатра праз [`list`](list.md).
2. Малы тэатр пабудуйце цалкам: `heat3d-dcs-maps level <theatre> -o levels`.
3. Для вялікага абярыце рэгіён: `--around <lat> <lon> <km>` (квадрат, які
   на столькі км у кожны бок ад кропкі) або `--bounds X0 Z0 X1 Z1` у метрах DCS.
   Назавіце яго праз `--name`.
4. Каманда друкуе пліткі па меры чытання, колькасць трохвугольнікаў,
   запісаны файл і колькі гарадоў тэатра трапляюць на зямлю - гэта
   праверка праекцыі, і павінна быць «N з N».
5. Загрузіце `<folder>/<name>.glb` на панэлі «Фон / узровень» праглядальніка і ўключыце
   **Зняты колер**, каб убачыць класы зямлі.

![level на сінтэтычнай усталёўцы](../assets/img/level.svg)

Рэгіён таго ж сінтэтычнага тэатра, у метрах DCS:

![level з --bounds і --name](../assets/img/level-bounds.svg)

## Опцыі {#options}

| Опцыя | Па змаўчанні | Што робіць |
|---|---|---|
| `theatre` | - | назва папкі пад `Mods\terrains`, як яе друкуе `list` (рэгістр не важны) |
| `-o`, `--out` | абавязкова | папка, у якую пішуцца `<name>.glb` і `<name>.json` |
| `--dcs FOLDER` | знаходзіцца | папка DCS World ([як яна знаходзіцца](list.md#where-the-install-is-found)) |
| `--name NAME` | назва тэатра | назва ўзроўню і яго файлаў |
| `--around LAT LON KM` | - | толькі квадрат на столькі км у кожны бок ад кропкі |
| `--bounds X0 Z0 X1 Z1` | - | толькі гэтая скрынка, у метрах DCS (x на поўнач, z на ўсход) |
| `--cell M` | `0` | зрадзіць сетку: кожная вяршыня ў межах *M* метраў становіцца адной (0: уласныя трохвугольнікі гульні) |
| `--seabed` | выключана | пакінуць марское дно як зямлю (па змаўчанні яго не бярэцца) |
| `--no-water` | выключана | не ўключаць плоскае мора |
| `--no-buildings` | выключана | не ўключаць будынкі сцэны тэатра |
| `--force` | выключана | экспартаваць вельмі вялікую карту цалкам з поўнай дэталізацыяй |
| `--projection LON0 FE FN` | тэатра | канстанты Transverse Mercator для тэатра, якога гэты інструмент не ведае ([fit](fit.md)) |

Кожная опцыя, як яе друкуе праграма: [Даведнік каманд](../cli-reference.md).

## Памер {#size}

Сетка гульні адаптыўная - адкрытае мора ў трохвугольніках шырынёй у кіламетры, узбярэжжы
і дарогі ў некалькі метраў. Малы тэатр — некалькі мільёнаў трохвугольнікаў; вялікія —
дзесяткі мільёнаў вяршынь. Пры больш чым 30 мільёнах вяршынь для чытання `level`
спыняецца (статус выхаду 1) і просіць рэгіён, радзейшую сетку (`--cell 50`) або
`--force`.

Статус выхаду: 0 — гатова; 1 — збой або занадта вялікі; 2 — усталёўка або тэатр
не знойдзены (знойдзеныя тэатры пералічаны).

## Прыклады {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Што ў файлах: [Файлы ўзроўню](output.md).
