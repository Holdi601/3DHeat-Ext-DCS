---
title: "利用条件とライセンス"
nav_order: 8
lang: "ja"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# 利用条件とライセンス {#terms-and-licence}

## リーダーが読むもの {#what-the-reader-reads}

リーダーは、あなたのコンピューター上にあるあなた自身の DCS World のインストールのデータファイルを読みます（[ファイルの読み方](reading.md)）。ゲームの中身は何も変更せず、どのサーバーとも通信しません。

ゲームのものは何も同梱・再配布しません。ゲームのファイルも、ゲームのコードも、DLL もありません。テストは読むファイルをすべて自分で作ります。書き出したレベルはあなたのマシンに残ります。

3DHeat DCS は Eagle Dynamics とは提携しておらず、承認も受けていません。DCS World および関連する名称と商標は、それぞれの所有者に帰属します。

権利者の方へ: [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) で issue を開いてください。迅速に対応し、ご要望があれば何でも削除します。

## ライセンスと情報源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)）。numpy（BSD-3-Clause）が必要です。`.parquet` に対する `fit` には pyarrow（Apache-2.0）が必要です。このプロジェクトのために書かれました。投影法の定数は、pydcs（github.com/pydcs/dcs、`dcs/terrain/*/projection.py`）が公開している事実です。取ったのは数値だけです。投影法は、C. F. F. Karneyが示したクリューガーの級数です（"Transverse Mercator with an accuracy of a few nanometers"、Journal of Geodesy 85、2011）。ほかのプロジェクトからコードは一切取っていません。
