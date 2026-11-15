---
title: "シアターを探す: list"
nav_order: 2
lang: "ja"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# シアターを探す: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

コマンドラインは初めてですか？ まず [始める前に](before-you-start.md) を読んでください。

1. 一度だけインストール: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`、そのフォルダーでターミナルを開き、`python -m pip install -e .` を実行します（Python 3.10 以降。numpyが入り、`.parquet` に対する `fit` のためにpyarrowも入ります）。
2. `heat3d-dcs-maps list` を実行します。
3. インストールされたシアターごとに1行が表示されます。その行には、フォルダー名（ほかのコマンドが使う名前）、地面のファイルのサイズ、タイルと頂点、緯度・経度の投影法がわかっているかどうか、そして読めるかどうかが示されます。各行の最後に `readable` と表示されるはずです。

![合成インストールでの list](../assets/img/list.svg)

この図は、テストが作ったインストール（`tests/synth.py`）での実行です。ゲームでの実行ではありません。

## インストールの場所 {#where-the-install-is-found}

`--dcs <folder>`（`Mods\terrains` を含むフォルダー）、または `DCS_PATH` 環境変数。指定がなければ、レジストリ、Steamのライブラリ、よくあるフォルダーを探します。

| オプション | 働き |
|---|---|
| `--dcs FOLDER` | DCS Worldのフォルダー。`Mods\terrains` を含むもの |

終了ステータス: 0 完了。2 インストールもシアターも見つからなかった。
