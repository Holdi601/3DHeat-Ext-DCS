---
title: "Имена места: towns"
nav_order: 5
lang: sr
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Имена места: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Исписује имена места театра, из његовог `map/towns.lua` (чита се као текст,
никад се не покреће), као JSON: име сваког града, његову географску ширину и дужину,
и његов DCS `x` (север) и `z` (исток) у метрима, преко пројекције театра.

1. Нађите име фасцикле театра помоћу [`list`](list.md).
2. Покрените `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Користите `x`/`z` да обележите ниво, или да проверите позиције из снимка.

![градови на пробној инсталацији](../assets/img/towns.svg)

| Опција | Шта ради |
|---|---|
| `theatre` | име фасцикле под `Mods\terrains` |
| `--dcs FOLDER` | фасцикла DCS World-а |

Градови унутар региона нивоа су такође у његовом `<name>.json`, са
висином тла испод сваког ([Датотеке нивоа](output.md)).
