---
title: "Имиња на места: towns"
nav_order: 5
lang: mk
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Имиња на места: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Ги печати имињата на местата на театарот, од неговата `map/towns.lua` (читана како текст,
никогаш не се извршува), како JSON: името на секој град, неговата географска ширина и должина, и
неговите DCS `x` (север) и `z` (исток) во метри, преку проекцијата на театарот.

1. Најдете го името на папката на театарот со [`list`](list.md).
2. Пуштете `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Користете ги `x`/`z` за да означите ниво, или за да ги проверите позициите на снимка.

![towns на синтетичка инсталација](../assets/img/towns.svg)

| Опција | Што прави |
|---|---|
| `theatre` | името на папката под `Mods\terrains` |
| `--dcs FOLDER` | папката на DCS World |

Градовите во регионот на едно ниво се и во неговата `<name>.json`, со
висината на теренот под секој ([Датотеките на нивото](output.md)).
