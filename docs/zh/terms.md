---
title: "条款与许可证"
nav_order: 8
lang: "zh"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# 条款与许可证 {#terms-and-licence}

## 读取器读取什么 {#what-the-reader-reads}

读取器读取你电脑上你自己的 DCS World 安装中的数据文件（[如何读取文件](reading.md)）。它不改动游戏中的任何内容，也不与任何服务器通信。

不随附也不再分发游戏中的任何东西：没有游戏文件、没有游戏代码、没有 DLL；测试会自行生成它们读取的每个文件。它写出的关卡留在你的电脑上。

3DHeat DCS 与 Eagle Dynamics 无关联，也未获其认可。DCS World 及相关名称和商标归其各自所有者所有。

权利人：请在 [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) 提交 issue——我们会迅速回复，并按要求删除任何内容。

## 许可证与来源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）；对于 `.parquet` 的 `fit` 还需要 pyarrow（Apache-2.0）。本软件为本项目专门编写。投影常数是由 pydcs（github.com/pydcs/dcs，`dcs/terrain/*/projection.py`）公布的事实；我们只取用了其中的数字。投影采用 C. F. F. Karney 给出的克吕格级数（"Transverse Mercator with an accuracy of a few nanometers"，Journal of Geodesy 85，2011）。没有使用任何其他项目的代码。
