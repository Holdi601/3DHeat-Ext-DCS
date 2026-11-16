---
title: "條款與授權"
nav_order: 8
lang: "zh-Hant"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# 條款與授權 {#terms-and-licence}

## 讀取器讀取什麼 {#what-the-reader-reads}

讀取器讀取你電腦上你自己的 DCS World 安裝中的資料檔案（[檔案如何被讀取](reading.md)）。它不更動遊戲中的任何內容，也不與任何伺服器通訊。

不隨附也不再散布遊戲中的任何東西：沒有遊戲檔案、沒有遊戲程式碼、沒有 DLL；測試會自行產生它們讀取的每個檔案。它寫出的關卡留在你的電腦上。

3DHeat DCS 與 Eagle Dynamics 無關聯，也未獲其認可。DCS World 及相關名稱和商標歸其各自所有者所有。

權利人：請在 [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) 提出 issue——我們會迅速回覆，並依要求移除任何內容。

## 授權與來源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）；對 `.parquet` 使用 `fit` 則需要 pyarrow（Apache-2.0）。為本專案撰寫。投影常數是 pydcs（github.com/pydcs/dcs，`dcs/terrain/*/projection.py`）所公開的事實；取用的只有數字。此投影採用 C. F. F. Karney 所給出的 Krüger 級數（"Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011）。未從任何其他專案取用程式碼。
