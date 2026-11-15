---
title: "查找战区：list"
nav_order: 2
lang: zh
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# 查找战区：`list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

第一次使用命令行？请先阅读 [开始之前](before-you-start.md)。

1. 安装一次：`git clone https://github.com/Holdi601/3DHeat-Ext-DCS`，在该文件夹中打开终端并运行 `python -m pip install -e .`（需要 Python 3.10 或更高版本；它会安装 numpy，对于 `.parquet` 文件的 `fit` 还会安装 pyarrow）。
2. 运行 `heat3d-dcs-maps list`。
3. 每个已安装的战区输出一行：它的文件夹名称（其他命令使用的名称）、地面文件的大小、瓦片数和顶点数、其纬度/经度投影是否已知，以及它能否被读取。每行末尾都应显示 `readable`。

![在合成安装上运行 list](../assets/img/list.svg)

图片是在测试程序构建的一个安装（`tests/synth.py`）上的运行结果，而不是在游戏上的运行结果。

## 安装位置如何被找到 {#where-the-install-is-found}

`--dcs <folder>`（包含 `Mods\terrains` 的文件夹），或者环境变量 `DCS_PATH`；否则会搜索注册表、Steam 库和常见的文件夹。

| 选项 | 作用 |
|---|---|
| `--dcs FOLDER` | DCS World 文件夹，即包含 `Mods\terrains` 的那个 |

退出状态：0 表示完成；2 表示未找到安装或战区。
