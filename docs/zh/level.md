---
title: "构建关卡：level"
nav_order: 3
lang: zh
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# 构建关卡：`level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## 逐步说明 {#step-by-step}

第一次使用命令行？请先阅读 [开始之前](before-you-start.md)。

1. 用 [`list`](list.md) 找到战区的文件夹名称。
2. 对于较小的战区，整体构建：`heat3d-dcs-maps level <theatre> -o levels`。
3. 对于较大的战区，选择一个区域：`--around <lat> <lon> <km>`（以某点为中心、每侧各 km 的正方形），或者以 DCS 米为单位的 `--bounds X0 Z0 X1 Z1`。
   用 `--name` 为它命名。
4. 命令会在读取瓦片时将其打印出来，同时打印三角形数量、写入的文件，以及战区中有多少城镇落在地面上：这是对投影的检查，正常应显示 “N of N”（N 个中的 N 个）。
5. 在查看器的 **背景/关卡面板** 中加载 `<folder>/<name>.glb`，并打开 **采集颜色**，即可看到地面类别。

![在合成安装上构建的关卡](../assets/img/level.svg)

同一个合成战区的一个区域，以 DCS 米为单位：

![使用 --bounds 和 --name 构建的关卡](../assets/img/level-bounds.svg)

## 选项 {#options}

| 选项 | 默认值 | 作用 |
|---|---|---|
| `theatre` | - | `Mods\terrains` 下的文件夹名称，与 `list` 打印的一致（大小写不限） |
| `-o`、`--out` | 必填 | 写入 `<name>.glb` 和 `<name>.json` 的文件夹 |
| `--dcs FOLDER` | 自动查找 | DCS World 文件夹（[安装位置如何被找到](list.md#where-the-install-is-found)） |
| `--name NAME` | 战区名称 | 关卡及其文件的名称 |
| `--around LAT LON KM` | - | 仅取某点两侧各此公里数的正方形 |
| `--bounds X0 Z0 X1 Z1` | - | 仅取此方框，以 DCS 米为单位（x 为北，z 为东） |
| `--cell M` | `0` | 稀疏化网格：距离在 *M* 米以内的每个顶点合并为一个（0：使用游戏自身的三角形） |
| `--seabed` | 关闭 | 将海底保留为地面（默认会被去除） |
| `--no-water` | 关闭 | 去除平坦的海面 |
| `--no-buildings` | 关闭 | 去除战区场景中的建筑 |
| `--force` | 关闭 | 以完整细节整体导出非常大的地图 |
| `--projection LON0 FE FN` | 战区自身的 | 本工具不认识的战区所用的横轴墨卡托常数（[fit](fit.md)） |

每个选项的完整说明，即程序自己打印的内容：[命令参考](../cli-reference.md)。

## 大小 {#size}

游戏的网格是自适应的：开阔的海面由相距数公里的三角形构成，海岸和道路则由几米的三角形构成。小型战区约为几百万个三角形；大型战区则有数千万个顶点。当需要读取的顶点超过 3000 万个时，`level` 会停止（退出状态 1），并要求你选择一个区域、使用更稀疏的网格（`--cell 50`），或者使用 `--force`。

退出状态：0 表示完成；1 表示失败或过大；2 表示找不到安装或战区（会列出已找到的战区）。

## 示例 {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # 整体，完整细节
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 一个 24 公里的正方形
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # 以 DCS 米为单位的一个方框
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # 整体，稀疏化到 50 米
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # 仅地面
```

文件中包含什么：[关卡文件](output.md)。
