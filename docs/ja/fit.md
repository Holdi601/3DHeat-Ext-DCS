---
title: "投影法: fit"
nav_order: 6
lang: "ja"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# 投影法: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

どのシアターも、独自の定数を持つ横メルカトル図法です。このツールは、確認済みのシアターについてはその定数を知っています。知らないシアターについては、`fit` が、緯度・経度とDCSのメートルの両方を含む記録から定数を求めます。たとえば、1回のフライトの3DHeat Watcherのセッションです。

1. 3DHeat Watcherでシアター上のフライトを記録します（または、DCSのメートルで `lat`、`lon`、`x`、`z` の列を持つ任意の記録。xは北へのメートル、zは東へのメートルで、DCSのどこでも同じです）。
2. `heat3d-dcs-maps fit "<session>/heat.parquet"` を実行します（`.jsonl` または `.csv` でも可）。
3. 求めた投影法をJSONで表示し、点の二乗平均平方根誤差と、使うべき `--projection` の引数を表示します。
4. その引数でレベルを作ります:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`。

![合成記録に対するfit](../assets/img/fit.svg)

図の記録は、既知の投影法から作った9点です。`fit` はそれをミリメートル単位まで正しく求め直します。

| 引数 | 働き |
|---|---|
| `recording` | 列 `lat`、`lon`、`x`、`z`（DCSのメートル）を持つ `.parquet`、`.jsonl`、`.csv`。読めない行は飛ばされます |

投影法は、C. F. F. Karneyが示したクリューガーの級数です（"Transverse Mercator with an accuracy of a few nanometers"、Journal of Geodesy 85、2011）。

終了ステータス: 0 は良い適合（二乗平均平方根誤差が 5m 未満）。1 は悪い適合、または使える行が3つ未満。2 はファイルが見つからなかった場合。
