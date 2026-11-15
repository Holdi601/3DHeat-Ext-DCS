---
title: "利用条件とライセンス"
nav_order: 8
lang: ja
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# 利用条件とライセンス {#terms-and-licence}

## Eagle Dynamicsの利用条件 {#eagle-dynamics-terms}

2026-11-07 に、インストールの `Doc/license_en.txt`（DCS World エンドユーザー使用許諾契約、The Fighter Collection Ltd）から読みました。許諾された「プログラム」には「それに付属するデータ」が含まれます。第3.1条は、英語の原文のまま引用します:

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

第3.1条(a)は、同意なしに、プログラムを "sell, trade, rent, lease, sub-license, merge, adapt, vary, modify the Program" することを禁じ、(e)は、"exploit this Program or any of its parts commercially" することを禁じています。

このリーダーがすること: インストールの後、ゲームの外で、あなたのマシン上のデータファイルを読みます。ゲームには何も変更せず、暗号化を破らず（地形フォルダー内の唯一の暗号化ファイルには触れません）、サーバーとは通信しません。データファイルの構造を読み解くことは、第3.1条(c)の意味でのリバースエンジニアリングであり、ゲームの地形から作ったレベルは、派生的著作物と言えるかもしれません。このリーダーを使うかどうかはあなたの判断で、あなた自身の使用のため、そこで作られるレベルは、見るためだけのあなたのものであり、共有や公開はできません。そのため、これは別のパッケージになっています。

許諾された代替手段は、ファイルを読まないものです。シミュレーター自身のミッションのスクリプトは、ミッションの実行中に、地面をサンプルし（`land.getHeight`、`land.getSurfaceType`）、飛行場を一覧にできます（`world.getAirbases`）。これにはシアターごとにDCSを数時間動かす必要があり、粗い格子しか得られません。ファイルが読めることがわかったため、これは作っていません。

## ライセンスと情報源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。numpy（BSD-3-Clause）が必要です。`.parquet` に対する `fit` には pyarrow（Apache-2.0）が必要です。このプロジェクトのために書かれました。投影法の定数は、pydcs（github.com/pydcs/dcs、`dcs/terrain/*/projection.py`）が公開している事実です。取ったのは数値だけです。投影法は、C. F. F. Karneyが示したクリューガーの級数です（"Transverse Mercator with an accuracy of a few nanometers"、Journal of Geodesy 85、2011）。ほかのプロジェクトからコードは一切取っていません。
