---
title: Uvjeti i licenca
nav_order: 8
lang: hr
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Uvjeti i licenca {#terms-and-licence}

## Uvjeti tvrtke Eagle Dynamics {#eagle-dynamics-terms}

Pročitano 2026-11-07 iz `Doc/license_en.txt` instalacije (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Licencirani
"Program" uključuje "THE DATA SUPPLIED WITH IT". Klauzula 3.1:

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

Klauzula 3.1 (a) zabranjuje "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" bez suglasnosti, a (e) zabranjuje
"exploit this Program or any of its parts commercially".

Što ovaj čitač radi: čita datoteke podataka na vašem računalu, nakon što ste ih instalirali, izvan igre. Ništa ne mijenja u igri, ne razbija šifriranje (jedina šifrirana datoteka u mapi terena ostavlja se netaknuta) i ne razgovara ni s jednim poslužiteljem. Utvrđivanje rasporeda datoteke podataka je obrnuti inženjering u smislu 3.1 (c), a razina izrađena iz terena igre može se smatrati izvedenim djelom. Upotreba čitača je vaša odluka, za vašu vlastitu upotrebu; razine koje on piše vaše su za gledanje, a ne za dijeljenje ili objavljivanje. Zato je to zaseban paket.

Dopuštena alternativa, koja ne čita nijednu datoteku: sama skriptna podrška simulatora može uzorkovati tlo (`land.getHeight`, `land.getSurfaceType`) i popisati zračne baze (`world.getAirbases`) dok misija radi. Potrebno je da DCS radi satima po karti i daje grublju mrežu; nije izrađena, jer su datoteke bile čitljive.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Treba numpy (BSD-3-Clause); `fit` na
`.parquet` datoteci treba pyarrow (Apache-2.0). Napisano za ovaj projekt. Konstante projekcije su činjenice koje objavljuje pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); uzeti su samo brojevi. Projekcija je Krügerov niz kako ga daje C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Nijedan kod nije preuzet ni iz jednog drugog projekta.
