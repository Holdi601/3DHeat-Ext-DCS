---
title: "檔案如何被讀取"
nav_order: 7
lang: zh-Hant
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# 檔案如何被讀取 {#how-the-files-are-read}

只會讀取 `Mods/terrains/<theatre>/surface/*.surface5`（地面網格）、
`Scenes/*.scn5`（物件的站立位置，以及每個模型的方框）、
`AirfieldsTaxiways/*.rn4`，以及 `map/towns.lua`（地名，以文字讀取，從不執行）。
不讀取加密的 `terrain.cfg.lua.pak.crypt`、不讀取 `manifest.bin`，也不讀取程式的任何內容。

`.surface5` 格式並無公開文件；其版面根據檔案讀取，記載於
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py)。
簡單來說：一個由圖塊記錄所組成的索引（變換、邊界，以及帶有型別的位元組串流清單，每個清單之後接著繪製時所用的著色器與材質），然後是原始資料。它既未壓縮，也未加密。圖塊的 `Pbase` 串流保存其頂點；以 `Land` 繪製的群組保存三角形，以及每個三角形的 `TRITYPE`，其最低位元標示為海；其他群組則是產生上述類別的覆蓋層。

## 已驗證 {#verified}

- `list` 讀取了每個已安裝戰區的索引（每個戰區從數百萬到數千萬個地面頂點），所取樣的每個圖塊都解碼成合理的公尺數。
- 在兩個戰區的區域上，來自 `towns.lua` 的城鎮落在距離地面頂點數公尺之內、位於陸地上，N of N；最高的地面與真實山頂相符，誤差在十公尺以內；機場、河流、村莊與道路都以其類別顯示。兩個關卡都已在檢視器中載入，城鎮標記以相同的 DCS 公尺座標正確地位於地面上。
- 在一個場景區域上，建築的放置位置都落在其地面上；跑道燈沿著遊戲的跑道排列，而貨車與牆段都與解碼出的朝向對齊。
- `tests/` 會以相同的版面建立 `.surface5` 檔案，因此這裡不保存任何遊戲資料；`tests/test_real_install.py` 會在執行測試的電腦上的安裝中執行，若沒有安裝則會略過。

**未檢查：** 大型戰區的整體是否能在單一關卡中完成（上方的大小防護存在是有原因的），以及 DCS 的其他版本。

## 未被讀取 {#not-read}

- **建築的形狀**（模型為 `Models/` 中的 `.edm`）：刻意只以方塊表示。它們的版面，以及場景的版面，記載於
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py)；所安裝的每個戰區都能讀取（另有兩個較舊、採用變體版面的戰區，讀取器也認得）。
- 樹木、燈具與場景中的其他物件：已讀取，但未繪製。
- **道路網路的圖形**（`roads/*.rn4`）：未解碼。
- 材質、樹木、海浪，以及地形自身較低的細節層級。
