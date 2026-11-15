---
title: "Uvjeti i licenca"
nav_order: 8
lang: bs
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Uvjeti i licenca {#terms-and-licence}

## Uvjeti kompanije Eagle Dynamics {#eagle-dynamics-terms}

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

Klauzula 3.1 (a) zabranjuje da se "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" bez pristanka, a (e) da se "exploit this
Program or any of its parts commercially".

Šta ovaj čitač radi: čita datoteke podataka na tvom vlastitom računaru, nakon što si ih
instalirao, izvan igre. Ništa u igri ne mijenja, ne razbija nikakvu
šifru (jedna šifrirana datoteka u folderu terena ostavlja se na miru) i
ne komunicira ni s jednim serverom. Utvrđivanje rasporeda datoteke podataka je obrnuti
inženjering u smislu 3.1 (c), a nivo izgrađen od terena igre je
vjerovatno izvedeno djelo. Korištenje čitača je tvoja odluka,
za tvoju vlastitu upotrebu; nivoi koje piše tvoji su za gledanje, ne za dijeljenje ni
objavljivanje. Zato je ovo poseban paket.

Odobrena alternativa, koja ne čita nijednu datoteku: vlastito skriptiranje misija
simulatora može uzorkovati tlo (`land.getHeight`, `land.getSurfaceType`)
i navesti baze (`world.getAirbases`) dok misija traje. Treba da DCS
radi satima po teatru i daje grublju mrežu; nije izgrađena,
jer su se datoteke pokazale čitljivima.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Treba numpy (BSD-3-Clause); `fit` na
`.parquet` treba pyarrow (Apache-2.0). Napisano za ovaj projekat. Konstante
projekcije su činjenice koje je objavio pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); uzeti su samo brojevi.
Projekcija je Krügerov red kako ga daje C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nikakav kod nije preuzet ni iz jednog drugog projekta.
