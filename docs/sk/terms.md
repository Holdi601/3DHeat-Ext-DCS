---
title: "Podmienky a licencia"
nav_order: 8
lang: sk
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Podmienky a licencia {#terms-and-licence}

## Podmienky spoločnosti Eagle Dynamics {#eagle-dynamics-terms}

Prečítané 2026-11-07 zo súboru `Doc/license_en.txt` inštalácie (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Licencovaný
„Program“ zahŕňa „THE DATA SUPPLIED WITH IT“ (ÚDAJE DODANÉ S NÍM). Článok 3.1:

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

Článok 3.1 (a) zakazuje „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program“ (predávať, obchodovať, prenajímať, lízingovať, sublicencovať, zlučovať,
upravovať, meniť, modifikovať Program) bez súhlasu, a (e) „exploit this
Program or any of its parts commercially“ (komerčne využívať tento Program alebo jeho časti).

Čo tento čítač robí: číta dátové súbory na vašom vlastnom počítači, po tom, ako ste ich nainštalovali, mimo hry. Nemení nič v hre, neprelomí žiadne šifrovanie (jediný zašifrovaný súbor v priečinku terénu sa nechá tak) a nekomunikuje so žiadnym serverom. Zistiť rozloženie dátového súboru je spätné inžinierstvo v zmysle 3.1 (c) a úroveň postavená z terénu hry je možno odvodené dielo. Používanie čítača je vaše rozhodnutie, na váš vlastný účel; úrovne, ktoré zapisuje, sú vaše na zobrazenie, nie na zdieľanie alebo zverejnenie. Preto je to samostatný balík.

Alternatíva, ktorá je schválená a nečíta žiadny súbor: vlastné skriptovanie misií simulátora môže počas behu misie vzorkovať zem (`land.getHeight`, `land.getSurfaceType`) a vypísať letiská (`world.getAirbases`). Vyžaduje to bežiaci DCS hodiny na každé územie a dáva hrubšiu mriežku; nebola postavená, pretože súbory sa ukázali ako čitateľné.

## Licencia a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potrebuje numpy (BSD-3-Clause); `fit` na
`.parquet` potrebuje pyarrow (Apache-2.0). Napísané pre tento projekt. Konštanty projekcie sú fakty zverejnené
pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); prebrali sa len čísla. Projekcia je Krügerov rad, ako ho podáva C. F. F. Karney („Transverse Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011). Žiadny kód sa neprebral z iného projektu.
