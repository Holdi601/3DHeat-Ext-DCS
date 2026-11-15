---
title: "地名：towns"
nav_order: 5
lang: zh-Hant
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# 地名：`towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

印出戰區的地名，來源為其 `map/towns.lua`（以文字讀取，從不執行），格式為 JSON：每個城鎮的名稱、其經緯度，以及透過戰區投影計算出的 DCS `x`（北）與 `z`（東），單位為公尺。

1. 用 [`list`](list.md) 找出戰區的資料夾名稱。
2. 執行 `heat3d-dcs-maps towns <theatre> > towns.json`。
3. 使用 `x`/`z` 為關卡加上標籤，或檢查錄製中的位置。

![在合成安裝上的城鎮](../assets/img/towns.svg)

| 選項 | 作用 |
|---|---|
| `theatre` | `Mods\terrains` 下的資料夾名稱 |
| `--dcs FOLDER` | DCS World 資料夾 |

位於關卡區域內的城鎮，也會列在其 `<name>.json` 中，並附上每個城鎮下方地面的高度（[關卡檔案](output.md)）。
