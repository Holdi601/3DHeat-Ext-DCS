---
title: "尋找戰區：list"
nav_order: 2
lang: zh-Hant
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# 尋找戰區：`list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

第一次使用命令列？請先閱讀[開始之前](before-you-start.md)。

1. 安裝一次：`git clone https://github.com/Holdi601/3DHeat-Ext-DCS`，在該資料夾中開啟終端機，然後執行 `python -m pip install -e .`（Python 3.10 或更新版本；它會帶入 numpy，而若要對 `.parquet` 使用 `fit`，還會帶入 pyarrow）。
2. 執行 `heat3d-dcs-maps list`。
3. 每個已安裝的戰區會印出一行：它的資料夾名稱（其他指令所使用的名稱）、地面檔案的大小、它的網格與頂點數、其經緯度投影是否已知，以及它是否可以讀取。每一行的結尾都應該看到 `readable`。

![在合成安裝上執行 list](../assets/img/list.svg)

圖片是在測試建立的安裝（`tests/synth.py`）上執行的結果，不是在遊戲上。

## 安裝位置的尋找方式 {#where-the-install-is-found}

`--dcs <folder>`（包含 `Mods\terrains` 的資料夾），或 `DCS_PATH` 環境變數；若未指定，則會搜尋登錄檔、Steam 資料庫與一般常用的資料夾。

| 選項 | 作用 |
|---|---|
| `--dcs FOLDER` | DCS World 資料夾，即包含 `Mods\terrains` 的那一個 |

結束狀態：0 完成；2 找不到安裝或戰區。
