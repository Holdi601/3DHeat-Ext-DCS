---
title: "如何读取文件"
nav_order: 7
lang: zh
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# 如何读取文件 {#how-the-files-are-read}

只读取 `Mods/terrains/<theatre>/surface/*.surface5`（地面网格）、`Scenes/*.scn5`（对象的位置，以及每个模型的方盒）、`AirfieldsTaxiways/*.rn4`，以及 `map/towns.lua`（地名，以文本形式读取，从不运行）。不读取加密的 `terrain.cfg.lua.pak.crypt`、`manifest.bin`，也不读取程序的任何内容。

`.surface5` 格式没有公开文档；其布局是根据文件读取的，并记录在 [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py) 中。简而言之：先是一个瓦片记录的索引（一个变换、边界，以及带类型的字节流列表，每个列表之后跟着绘制它所用的着色器和材质），然后是原始数据。它既没有压缩，也没有加密。瓦片的 `Pbase` 流保存其顶点；被绘制为 `Land` 的组保存三角形，以及每个三角形的 `TRITYPE`，其最低位标记是否为海；其他组则是给出上述类别的覆盖层。

## 已验证 {#verified}

- `list` 读取了每个已安装战区的索引（每个战区从数百万到数千万个地面顶点），所采样的每个瓦片都解码为合理的米制数值。
- 在两个战区的区域上，`towns.lua` 中的城镇落在距离地面顶点不到几米的位置，位于陆地上，N 中的 N 个；最高的地面与真实山顶相差在十米以内；机场、河流、村庄和道路都以其类别显示。两个关卡都能在查看器中加载，并且以相同 DCS 米坐标标出的城镇标记都位于地面上。
- 在一个场景区域上，建筑摆放的位置都落在其地面上；跑道灯沿着游戏的跑道排列，车厢和墙段都与解码出的朝向对齐，全部如此。
- `tests/` 按相同的布局构建 `.surface5` 文件，因此这里不保存任何游戏数据；`tests/test_real_install.py` 会在运行测试的电脑上的安装中运行，没有安装时则跳过。

**未检查：**在一个关卡中包含大型战区的全部内容（上述大小限制正是为此而设），以及除所尝试版本之外的 DCS 版本。

## 未读取的内容 {#not-read}

- **作为形状的建筑**（模型是 `Models/` 中的 `.edm` 文件）：刻意只使用方盒。它们的布局以及场景的布局记录在 [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py) 中；所安装的每个战区都能读取（另有两个较旧的战区使用本读取器也认识的变体布局）。
- 树木、灯具和场景中的其他对象：已读取，但不绘制。
- **作为图形的道路网络**（`roads/*.rn4`）：未解码。
- 贴图、树木、海浪、地形自身较低的细节层级。
