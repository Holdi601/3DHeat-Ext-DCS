---
title: "Градење ниво: level"
nav_order: 3
lang: "mk"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Градење ниво: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Чекор по чекор {#step-by-step}

Нови сте со командната линија? Прво прочитајте [Пред да започнете](before-you-start.md).

1. Најдете го името на папката на театарот со [`list`](list.md).
2. За мал театар, изградете го цел: `heat3d-dcs-maps level <theatre> -o levels`.
3. За голем, изберете регион: `--around <lat> <lon> <km>` (квадрат толку
   km на секоја страна од една точка) или `--bounds X0 Z0 X1 Z1` во метри од DCS.
   Именувајте го со `--name`.
4. Командата ги печати плочките (tiles) додека ги чита, бројот на триаголници, запишаната
   датотека, и колку од градовите на театарот лежат на теренот - проверка
   на проекцијата што треба да гласи „N of N“.
5. Вчитајте `<folder>/<name>.glb` во панелот Позадина / ниво на прегледувачот и вклучете
   **Снимена боја** за да ги видите класите на терен.

![level на синтетичка инсталација](../assets/img/level.svg)

Регион од истиот синтетички театар, по метри од DCS:

![level со --bounds и --name](../assets/img/level-bounds.svg)

## Опции {#options}

| Опција | Стандардно | Што прави |
|---|---|---|
| `theatre` | - | името на папката под `Mods\terrains`, како што го печати `list` (било кои големи/мали букви) |
| `-o`, `--out` | задолжително | папката во која се пишуваат `<name>.glb` и `<name>.json` |
| `--dcs FOLDER` | пронајдена | папката на DCS World ([каде се наоѓа](list.md#where-the-install-is-found)) |
| `--name NAME` | на театарот | името на нивото, и на неговите датотеки |
| `--around LAT LON KM` | - | само квадрат толку km на секоја страна од една точка |
| `--bounds X0 Z0 X1 Z1` | - | само оваа кутија, во метри од DCS (x север, z исток) |
| `--cell M` | `0` | разредување на мрежата: секое теме (vertex) во рамките на *M* метри станува едно (0: сопствените триаголници на играта) |
| `--seabed` | исклучено | го задржува морското дно како терен (стандардно се изоставува) |
| `--no-water` | исклучено | го изоставува рамното море |
| `--no-buildings` | исклучено | ги изоставува зградите од сцената на театарот |
| `--force` | исклучено | извезува многу голема мапа цела со целосни детали |
| `--projection LON0 FE FN` | на театарот | константи на Трансверзална Меркаторова проекција за театар што оваа алатка не го знае ([fit](fit.md)) |

Секоја опција, како што ја печати програмата: [Упатство за команди](../cli-reference.md).

## Големина {#size}

Мрежата на играта е адаптивна - отворено море во триаголници широки километри, брегови
и патишта во неколку метри. Мал театар е неколку милиони триаголници; големите
се десетици милиони темиња. Над 30 милиони темиња за читање, `level`
запира (излезен статус 1) и бара регион, потенка мрежа (`--cell 50`) или
`--force`.

Излезен статус: 0 готово; 1 неуспех или преголемо; 2 инсталацијата или театарот не
беа пронајдени (пронајдените театри се наведуваат).

## Примери {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Што има во датотеките: [Датотеките на нивото](output.md).
