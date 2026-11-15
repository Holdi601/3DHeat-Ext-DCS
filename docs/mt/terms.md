---
title: Termini u liċenzja
nav_order: 8
lang: "mt"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Termini u liċenzja {#terms-and-licence}

## It-termini ta' Eagle Dynamics {#eagle-dynamics-terms}

Moqrija fis-2026-11-07 minn `Doc/license_en.txt` tal-installazzjoni (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Il-"Program" liċenzjat
jinkludi "THE DATA SUPPLIED WITH IT". Klawsola 3.1:

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

Il-klawsola 3.1 (a) tipprojbixxi li "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" mingħajr kunsens, u (e) li "exploit this
Program or any of its parts commercially".

Dak li jagħmel dan il-qarrej: jaqra fajls tad-dejta fuq il-magna tiegħek stess, wara li
installajthom, barra mill-logħba. Ma jibdel xejn fil-logħba, ma jkisser ebda
kriptaġġ (l-uniku fajl ikkriptat f'folder ta' terren jitħalla waħdu) u
ma jitkellem ma' ebda server. Li tifhem il-layout ta' fajl tad-dejta huwa reverse
engineering fis-sens tal-3.1 (c), u livell mibni mit-terren tal-logħba huwa
probabbilment xogħol derivat. L-użu tal-qarrej huwa d-deċiżjoni tiegħek,
għall-użu tiegħek; il-livelli li jikteb huma tiegħek biex tarahom, mhux biex taqsamhom jew
tippubblikahom. Huwa għalhekk li huwa pakkett separat.

L-alternattiva awtorizzata, li ma taqra ebda fajl: l-iscripting tal-missjonijiet tas-sim
innifsu jista' jieħu kampjuni tal-art (`land.getHeight`, `land.getSurfaceType`)
u jelenka l-bażijiet ajrei (`world.getAirbases`) waqt li missjoni taħdem. Teħtieġ DCS
jaħdem għal sigħat għal kull teatru u tagħti grilja aktar goffa; ma nbnietx,
għax il-fajls irriżultaw li jinqraw.

## Liċenzja u sorsi {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Teħtieġ numpy (BSD-3-Clause); `fit` fuq
`.parquet` jeħtieġ pyarrow (Apache-2.0). Miktub għal dan il-proġett. Il-
kostanti tal-projezzjoni huma fatti ppubblikati minn pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); ittieħdu in-numri biss.
Il-projezzjoni hija s-serje ta' Krüger kif tagħtha C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ebda kodiċi ma ttieħed minn ebda proġett ieħor.
