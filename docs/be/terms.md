---
title: "Умовы і ліцэнзія"
nav_order: 8
lang: be
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Умовы і ліцэнзія {#terms-and-licence}

## Умовы Eagle Dynamics {#eagle-dynamics-terms}

Прачытана 2026-11-07 з `Doc/license_en.txt` усталёўкі (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Ліцэнзаваная
«Program» уключае «THE DATA SUPPLIED WITH IT». Пункт 3.1:

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

Пункт 3.1 (a) забараняе «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» без згоды, а (e) — «exploit this
Program or any of its parts commercially».

Што робіць гэты чытач: ён чытае файлы даных на вашым кампутары, пасля таго як вы
іх усталявалі, па-за гульнёй. Ён нічога не змяняе ў гульні, не ломіць ніякага
шыфравання (адзіны зашыфраваны файл у папцы рэльефу застаецца недакранутым) і
не звязваецца ні з якім серверам. Высвятленне структуры файла даных — гэта зваротная
інжынерыя ў сэнсе 3.1 (c), а ўзровень, пабудаваны з рэльефу гульні, —
магчыма, вытворная праца. Выкарыстанне чытача — ваша рашэнне,
для ўласнага карыстання; узроўні, якія ён піша, вы можаце глядзець, але не дзяліцца імі і не
публікаваць іх. Таму гэта асобны пакет.

Дазволеная альтэрнатыва, што не чытае ніводнага файла: уласныя скрыпты місій
сімулятара могуць здымаць зямлю (`land.getHeight`, `land.getSurfaceType`)
і пералічваць аэрадромы (`world.getAirbases`), пакуль ідзе місія. Ёй патрэбны DCS,
які працуе гадзінамі на тэатр, і яна дае грубейшую сетку; яе не пабудавалі,
бо файлы аказаліся чытэльнымі.

## Ліцэнзія і крыніцы {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Патрэбны numpy (BSD-3-Clause); `fit` на
`.parquet` патрабуе pyarrow (Apache-2.0). Напісана для гэтага праекта. Канстанты
праекцыі — гэта факты, апублікаваныя pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); узяты толькі лічбы. Праекцыя — гэта
шэраг Крюгера ў выглядзе, у якім яго дае C. F. F. Karney
(«Transverse Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). Ніякага кода з іншых праектаў не ўзята.
