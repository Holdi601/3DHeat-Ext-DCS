---
title: "レベルを作る: level"
nav_order: 3
lang: ja
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# レベルを作る: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## 手順ごとの説明 {#step-by-step}

コマンドラインは初めてですか？ まず [始める前に](before-you-start.md) を読んでください。

1. [`list`](list.md) で、シアターのフォルダー名を調べます。
2. 小さなシアターなら、全体を作ります: `heat3d-dcs-maps level <theatre> -o levels`。
3. 大きなシアターなら、範囲を選びます: `--around <lat> <lon> <km>`（ある地点の両側それぞれ何kmの正方形）、または DCSのメートルで `--bounds X0 Z0 X1 Z1`。`--name` で名前を付けます。
4. コマンドは、読み取りながらタイルを表示し、三角形の数、書き出したファイル、そしてシアターの町のうち地面に乗った数を表示します。これは投影法の確認で、「N of N」と表示されるはずです。
5. `<folder>/<name>.glb` をビューアの背景/レベルパネルで読み込み、**取得した色** をオンにすると、地面の種類が見えます。

![合成インストールでのレベル](../assets/img/level.svg)

同じ合成シアターの一部を、DCSのメートルで指定したもの:

![--bounds と --name でのレベル](../assets/img/level-bounds.svg)

## オプション {#options}

| オプション | 既定値 | 働き |
|---|---|---|
| `theatre` | - | `Mods\terrains` の下のフォルダー名。`list` が表示する通り（大文字小文字は問わない） |
| `-o`, `--out` | 必須 | `<name>.glb` と `<name>.json` を書き込むフォルダー |
| `--dcs FOLDER` | 自動検出 | DCS Worldのフォルダー（[見つけ方](list.md#インストールの場所)） |
| `--name NAME` | シアターの名前 | レベルの名前、およびそのファイルの名前 |
| `--around LAT LON KM` | - | ある地点の両側それぞれ何kmの正方形だけ |
| `--bounds X0 Z0 X1 Z1` | - | DCSのメートルでの、この箱だけ（xが北、zが東） |
| `--cell M` | `0` | メッシュを間引く。*M* メートル以内の頂点は一つにまとめる（0: ゲーム自身の三角形） |
| `--seabed` | オフ | 海底を地面として残す（既定では除外） |
| `--no-water` | オフ | 平らな海を除く |
| `--no-buildings` | オフ | シアターのシーンの建物を除く |
| `--force` | オフ | 非常に大きなマップを、全体を最大の詳細度で書き出す |
| `--projection LON0 FE FN` | シアターのもの | このツールが知らないシアターの横メルカトル定数（[fit](fit.md)） |

プログラムが表示する通りのすべてのオプション: [コマンドリファレンス](../cli-reference.md)。

## サイズ {#size}

ゲームのメッシュは適応的です。外洋は数キロメートルの三角形、海岸と道路は数メートルです。小さなシアターは数百万の三角形、大きいものは数千万の頂点です。読み取る頂点が3,000万を超えると、`level` は止まり（終了ステータス 1）、範囲、より粗いメッシュ（`--cell 50`）、または `--force` を求めます。

終了ステータス: 0 完了。1 失敗、または大きすぎる。2 インストールまたはシアターが見つからなかった（見つかったシアターを一覧表示します）。

## 例 {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # 全体、最大の詳細度
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24km四方
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # DCSのメートルでの箱
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # 全体を50mに間引く
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # 地面だけ
```

ファイルの中身: [レベルのファイル](output.md)。
