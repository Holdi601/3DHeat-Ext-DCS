---
title: "地名：towns"
nav_order: 5
lang: "zh"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# 地名：`towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

打印战区的地名，来源是其 `map/towns.lua`（以文本形式读取，从不运行），输出为 JSON：每个城镇的名称、纬度和经度，以及通过该战区的投影得到的 DCS `x`（北）和 `z`（东）坐标（单位为米）。

1. 用 [`list`](list.md) 找到战区的文件夹名称。
2. 运行 `heat3d-dcs-maps towns <theatre> > towns.json`。
3. 使用 `x`/`z` 为关卡添加标注，或者检查录制中的位置。

![在合成安装上的城镇](../assets/img/towns.svg)

| 选项 | 作用 |
|---|---|
| `theatre` | `Mods\terrains` 下的文件夹名称 |
| `--dcs FOLDER` | DCS World 文件夹 |

关卡区域内的城镇也记录在其 `<name>.json` 中，并附有每个城镇下方地面的高度（[关卡文件](output.md)）。
