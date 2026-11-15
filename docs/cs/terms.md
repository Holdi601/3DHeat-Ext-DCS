---
title: "Podmínky a licence"
nav_order: 8
lang: cs
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Podmínky a licence {#terms-and-licence}

## Podmínky Eagle Dynamics {#eagle-dynamics-terms}

Přečteno 2026-11-07 ze souboru `Doc/license_en.txt` instalace (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Licencovaný „Program“
zahrnuje „THE DATA SUPPLIED WITH IT“. Článek 3.1:

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

Článek 3.1 (a) zakazuje „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program“ bez souhlasu a (e) zakazuje „exploit this
Program or any of its parts commercially“ (komerčně využívat tento Program
nebo jakoukoli jeho část).

Co tato čtečka dělá: čte datové soubory na vašem počítači, poté co jste je nainstalovali, mimo
hru. Nic ve hře nemění, nelame žádné šifrování (jediný šifrovaný soubor ve složce terénu zůstává
nedotčen) a nekomunikuje s žádným serverem. Zjišťování rozložení datového souboru je zpětné
inženýrství ve smyslu článku 3.1 (c) a úroveň postavená z terénu hry je sporně odvozené dílo.
Použití čtečky je vaše rozhodnutí, pro vaše vlastní účely; úrovně, které zapisuje, si smíte
prohlížet, ne sdílet nebo zveřejňovat. Proto je to samostatný balíček.

Schválená alternativa, která žádný soubor nečte: vlastní skriptování mise v simulátoru umí
vzorkovat terén (`land.getHeight`, `land.getSurfaceType`) a vypsat letiště (`world.getAirbases`),
dokud mise běží. Vyžaduje to běžící DCS po hodiny na území a dává hrubší mřížku; nebylo to
postaveno, protože soubory se ukázaly jako čitelné.

## Licence a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potřebuje numpy (BSD-3-Clause); `fit` na
`.parquet` potřebuje pyarrow (Apache-2.0). Napsáno pro tento projekt. Konstanty projekce jsou
údaje zveřejněné knihovnou pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); převzata
byla jen čísla. Projekce je Krügerova řada, jak ji podává C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).
Žádný kód nebyl převzat z jiného projektu.
