---
title: "Умовы і ліцэнзія"
nav_order: 8
lang: "be"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Умовы і ліцэнзія {#terms-and-licence}

## Што чытае чытальнік {#what-the-reader-reads}

Чытальнік чытае файлы даных вашай уласнай усталёўкі DCS World на вашым камп'ютары ([Як чытаюцца файлы](reading.md)). Ён нічога не мяняе ў гульні і не звязваецца ні з якім серверам.

Нічога з гульні не пастаўляецца і не распаўсюджваецца: ні файлаў гульні, ні кода гульні, ні DLL; тэсты самі ствараюць кожны файл, які чытаюць. Узроўні, якія ён запісвае, застаюцца на вашым камп'ютары.

3DHeat DCS не звязаны з кампаніяй Eagle Dynamics і не ўхвалены ёю. DCS World і звязаныя з ёй назвы і гандлёвыя маркі належаць іх уладальнікам.

Праваўладальнікі: адкрыйце задачу на [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - мы хутка адказваем і на просьбу прыбіраем што заўгодна.

## Ліцэнзія і крыніцы {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Патрэбны numpy (BSD-3-Clause); `fit` на
`.parquet` патрабуе pyarrow (Apache-2.0). Напісана для гэтага праекта. Канстанты
праекцыі — гэта факты, апублікаваныя pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); узяты толькі лічбы. Праекцыя — гэта
шэраг Крюгера ў выглядзе, у якім яго дае C. F. F. Karney
(«Transverse Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). Ніякага кода з іншых праектаў не ўзята.
