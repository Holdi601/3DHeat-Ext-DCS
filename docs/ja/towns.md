---
title: "地名: towns"
nav_order: 5
lang: "ja"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# 地名: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

シアターの地名を、その `map/towns.lua`（テキストとして読み、実行はしません）から、JSONで表示します。各町の名前、緯度と経度、そしてシアターの投影法によるDCSの `x`（北）と `z`（東）のメートルです。

1. [`list`](list.md) で、シアターのフォルダー名を調べます。
2. `heat3d-dcs-maps towns <theatre> > towns.json` を実行します。
3. `x`/`z` を使って、レベルに名前を付けたり、記録の位置を確かめたりします。

![合成インストールでの町](../assets/img/towns.svg)

| オプション | 働き |
|---|---|
| `theatre` | `Mods\terrains` の下のフォルダー名 |
| `--dcs FOLDER` | DCS Worldのフォルダー |

レベルの領域の中の町は、その `<name>.json` にも、それぞれの下の地面の高さとともに入っています（[レベルのファイル](output.md)）。
