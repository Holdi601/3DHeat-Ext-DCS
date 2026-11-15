---
title: "投影：fit"
nav_order: 6
lang: "zh"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# 投影：`fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

每个战区都是一种横轴墨卡托投影，并带有其自己的常数。本工具已知它在测试过的战区上的常数；对于未知的战区，`fit` 可以从任何同时包含纬度/经度和 DCS 米制坐标的录制中求出这些常数，例如 3DHeat Watcher 记录的一次飞行。

1. 使用 3DHeat Watcher 在该战区录制一次飞行（或者制作任何包含 `lat`、`lon`、`x`、`z` 列的录制，其中 `x` 为 DCS 米制的北向距离，`z` 为东向距离，这与 DCS 中的一切约定相同）。
2. 运行 `heat3d-dcs-maps fit "<session>/heat.parquet"`（也可以是 `.jsonl` 或 `.csv` 文件）。
3. 它会以 JSON 形式打印拟合出的投影，打印各点的均方根误差，并给出要使用的 `--projection` 参数。
4. 用这些参数构建关卡：
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`。

![对一段合成录制执行 fit](../assets/img/fit.svg)

图中的录制由九个点组成，它们由一个已知的投影生成，`fit` 可以精确地将其反推回来，误差只有毫米。

| 参数 | 作用 |
|---|---|
| `recording` | 带有 `lat`、`lon`、`x`、`z` 列（DCS 米）的 `.parquet`、`.jsonl` 或 `.csv` 文件；无法读取的行会被跳过 |

该投影采用 C. F. F. Karney 给出的克吕格级数（"Transverse Mercator with an accuracy of a few nanometers"，Journal of Geodesy 85，2011）。

退出状态：0 表示拟合良好（均方根误差低于 5 米）；1 表示拟合较差，或可用的行少于三行；2 表示找不到该文件。
