---
title: "投影：fit"
nav_order: 6
lang: zh-Hant
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# 投影：`fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

每個戰區都是一個橫向麥卡托投影，並有其自己的常數。本工具已知道那些經過檢驗的戰區的常數；對於它不認識的戰區，`fit` 會從任何同時包含經緯度與 DCS 公尺座標的錄製中找出這些常數，例如一次飛行的 3DHeat Watcher 工作階段。

1. 使用 3DHeat Watcher 在該戰區錄製一次飛行（或製作任何含有 `lat`、`lon`、`x`、`z` 欄位的錄製，單位為 DCS 公尺：x 為朝北的公尺，z 為朝東的公尺，與 DCS 中的一般慣例相同）。
2. 執行 `heat3d-dcs-maps fit "<session>/heat.parquet"`（或 `.jsonl` 或 `.csv`）。
3. 它會以 JSON 印出擬合出的投影、各點的均方根誤差，以及要使用的 `--projection` 參數。
4. 以這些參數建立關卡：
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`。

![在合成錄製上執行 fit](../assets/img/fit.svg)

圖中的錄製是由一組已知投影所產生的九個點，`fit` 可以精確地找回到毫米。

| 參數 | 作用 |
|---|---|
| `recording` | `.parquet`、`.jsonl` 或 `.csv`，欄位為 `lat`、`lon`、`x`、`z`（DCS 公尺）；無法讀取的列會被略過 |

此投影採用 C. F. F. Karney 所給出的 Krüger 級數（"Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011）。

結束狀態：0 代表擬合良好（均方根誤差低於 5 公尺）；1 代表擬合不佳，或可用的列少於三列；2 代表找不到該檔案。
