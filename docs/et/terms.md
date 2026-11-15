---
title: "Tingimused ja litsents"
nav_order: 8
lang: "et"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Tingimused ja litsents {#terms-and-licence}

## Eagle Dynamicsi tingimused {#eagle-dynamics-terms}

Loetud 2026-11-07 installi failist `Doc/license_en.txt` (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Litsentseeritud
"Program" hõlmab "THE DATA SUPPLIED WITH IT". Punkt 3.1:

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

Punkt 3.1 (a) keelab "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" ilma nõusolekuta ja (e) "exploit this
Program or any of its parts commercially".

Mida see lugeja teeb: ta loeb andmefaile sinu enda masinas pärast nende paigaldamist,
väljaspool mängu. Ta ei muuda mängus midagi, ei murra ühtegi krüptot (ühte krüpteeritud
faili terrain-kaustas ei puututa) ega suhtle ühegi serveriga. Andmefaili paigutuse väljaselgitamine
on punkti 3.1 (c) mõttes pöördprojekteerimine, ja tase, mis on tehtud mängu maastikust, on
tõenäoliselt tuletatud teos. Lugeja kasutamine on sinu otsus, sinu enda kasutuseks; tasemed,
mida see kirjutab, on sinu omad vaatamiseks, mitte jagamiseks ega avaldamiseks. Sellepärast
on see eraldi pakett.

Lugemata faili jätev alternatiiv on sim'i enda missiooni skriptimine: see võib mängu ajal
maapinda mõõta (`land.getHeight`, `land.getSurfaceType`) ja loetleda lennuväljad
(`world.getAirbases`), kui missioon käib. See vajab DCS-i tundide kaupa iga teatri kohta,
annab karedama võrgu ja seda ei ehitatud, sest failid osutusid loetavaks.

## Litsents ja allikad {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vajab numpy (BSD-3-Clause); `fit` `.parquet`-failil
vajab pyarrow (Apache-2.0). Kirjutatud selle projekti jaoks. Projektsiooni konstandid on
pydcs'i avaldatud faktid (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); võeti ainult numbrid. Projektsioon on Krügeri rida, nagu seda annab C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ühtegi koodi ei võetud ühestki teisest projektist.
