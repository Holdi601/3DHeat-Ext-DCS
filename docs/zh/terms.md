---
title: "条款与许可证"
nav_order: 8
lang: "zh"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# 条款与许可证 {#terms-and-licence}

## Eagle Dynamics 的条款 {#eagle-dynamics-terms}

于 2026-11-07 从安装目录中的 `Doc/license_en.txt` 读取（DCS World 最终用户许可协议，The Fighter Collection Ltd）。许可的“程序”包括“THE DATA SUPPLIED WITH IT”（随其提供的数据）。第 3.1 条：

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

第 3.1 (a) 条禁止未经同意“sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program”（出售、交易、出租、租赁、再许可、合并、
改编、变更、修改该程序），第 (e) 条禁止“exploit this
Program or any of its parts commercially”（将本程序或其任何部分用于商业牟利）。

本读取器的作用：它在你自己的电脑上、在你安装数据文件之后、在游戏之外，读取这些数据文件。它不会改变游戏中的任何内容，不会破解任何加密（战区文件夹中唯一的加密文件保持不动），也不会与任何服务器通信。分析数据文件的布局，在第 3.1 (c) 条的意义上属于逆向工程，而由游戏地形构建的关卡，可以说是一种衍生作品。使用本读取器是你自己的决定，仅供你自己使用；它生成的关卡只供你自己查看，不得分享或发布。这正是它被作为单独软件包发布的原因。

有一种经许可的替代方案，它不读取任何文件：在任务运行期间，模拟器自身的任务脚本可以对地面进行采样（`land.getHeight`、`land.getSurfaceType`），并列出机场（`world.getAirbases`）。它需要为每个战区运行 DCS 数小时，并且给出的网格更粗略；我们没有采用它，因为事实证明这些文件是可以读取的。

## 许可证与来源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）；对于 `.parquet` 的 `fit` 还需要 pyarrow（Apache-2.0）。本软件为本项目专门编写。投影常数是由 pydcs（github.com/pydcs/dcs，`dcs/terrain/*/projection.py`）公布的事实；我们只取用了其中的数字。投影采用 C. F. F. Karney 给出的克吕格级数（"Transverse Mercator with an accuracy of a few nanometers"，Journal of Geodesy 85，2011）。没有使用任何其他项目的代码。
