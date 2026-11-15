---
title: "Kushtet dhe licenca"
nav_order: 8
lang: "sq"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Kushtet dhe licenca {#terms-and-licence}

## Kushtet e Eagle Dynamics {#eagle-dynamics-terms}

Lexuar më 2026-11-07 nga `Doc/license_en.txt` i instalimit (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). "Programi" i licencuar
përfshin "THE DATA SUPPLIED WITH IT". Klauzola 3.1:

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

Klauzola 3.1 (a) ndalon të "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" pa pëlqim, dhe (e) të "exploit this
Program or any of its parts commercially".

Çfarë bën ky lexues: lexon skedarë të dhënash në kompjuterin tënd, pasi
i ke instaluar, jashtë lojës. Nuk ndryshon asgjë në lojë, nuk thyen asnjë
enkriptim (skedari i vetëm i enkriptuar në një dosje terreni lihet i paprekur) dhe
nuk flet me asnjë server. Nxjerrja e skemës së një skedari të dhënash është inxhinieri
e kundërt në kuptimin e 3.1 (c), dhe një nivel i ndërtuar nga terreni i lojës është
me arsye një vepër e derivuar. Përdorimi i lexuesit është vendimi yt,
për përdorimin tënd; nivelet që shkruan janë të tuat për t'i parë, jo për t'i ndarë ose
botuar. Prandaj është një paketë më vete.

Alternativa e lejuar, që nuk lexon asnjë skedar: skriptimi i misioneve të vetë simulatorit
mund të mostrojë tokën (`land.getHeight`, `land.getSurfaceType`)
dhe të listojë bazat ajrore (`world.getAirbases`) ndërsa një mision është në ecuri. Kërkon që DCS
të jetë i ndezur me orë për teatër dhe jep një rrjetë më të ashpër; nuk u ndërtua,
sepse skedarët u treguan të lexueshëm.

## Licenca dhe burimet {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kërkon numpy (BSD-3-Clause); `fit` mbi një
`.parquet` kërkon pyarrow (Apache-2.0). Shkruar për këtë projekt. Konstantet e
projeksionit janë fakte të botuara nga pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); u morën vetëm numrat. Projeksioni
është seria e Krüger-it siç e jep C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nuk u mor kod nga asnjë projekt tjetër.
