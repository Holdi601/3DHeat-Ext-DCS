---
title: "條款與授權"
nav_order: 8
lang: zh-Hant
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# 條款與授權 {#terms-and-licence}

## Eagle Dynamics 的條款 {#eagle-dynamics-terms}

於 2026-11-07 從安裝目錄中的 `Doc/license_en.txt` 讀取（DCS World
最終使用者授權合約，The Fighter Collection Ltd）。被授權的「Program」包括「THE DATA SUPPLIED WITH IT」。第 3.1 條：

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

第 3.1 (a) 條禁止未經同意而「sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program」（出售、交易、出租、租賃、再授權、合併、
改編、變更、修改本程式），第 (e) 款則禁止「exploit this
Program or any of its parts commercially」（將本程式或其任何部分用於商業營利）。

本讀取器的作法：它在你安裝遊戲之後，於你自己的電腦上、遊戲之外，讀取資料檔案。它不改變遊戲的任何內容，不破解任何加密（終端機資料夾中唯一的加密檔案會被保持不動），也不與任何伺服器通訊。理解資料檔案的版面，依第 3.1 (c) 條屬於逆向工程，而由遊戲地形建成的關卡，可以說是衍生作品。使用本讀取器是你自己的決定，供你個人使用；它寫出的關卡只供你自己檢視，不可分享或發布。這也是它之所以是獨立套件的原因。

另一種獲准的做法，不需讀取任何檔案：模擬器自身的任務腳本，可以在任務執行期間取樣地面（`land.getHeight`、`land.getSurfaceType`）並列出機場（`world.getAirbases`）。但它需要 DCS 每個戰區運行數小時，而且得到的網格較粗；由於檔案已被證明可以讀取，因此沒有去建構它。

## 授權與來源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）；對 `.parquet` 使用 `fit` 則需要 pyarrow（Apache-2.0）。為本專案撰寫。投影常數是 pydcs（github.com/pydcs/dcs，`dcs/terrain/*/projection.py`）所公開的事實；取用的只有數字。此投影採用 C. F. F. Karney 所給出的 Krüger 級數（"Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011）。未從任何其他專案取用程式碼。
