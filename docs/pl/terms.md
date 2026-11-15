---
title: "Warunki i licencja"
nav_order: 8
lang: pl
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Warunki i licencja {#terms-and-licence}

## Warunki Eagle Dynamics {#eagle-dynamics-terms}

Przeczytane 2026-11-07 z `Doc/license_en.txt` instalacji (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Licencjonowany „Program”
obejmuje „THE DATA SUPPLIED WITH IT”. Klauzula 3.1:

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

Klauzula 3.1 (a) zabrania „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program” bez zgody, a (e) zabrania „exploit this
Program or any of its parts commercially”.

Co robi ten czytnik: czyta pliki danych na twoim własnym komputerze, po ich zainstalowaniu, poza grą.
Niczego nie zmienia w grze, nie łamie żadnego szyfrowania (jedyny zaszyfrowany plik w folderze terenu zostaje nietknięty)
i nie łączy się z żadnym serwerem. Ustalenie układu pliku danych to inżynieria wsteczna w rozumieniu 3.1 (c),
a poziom zbudowany z terenu gry można uznać za utwór pochodny. Użycie czytnika to twoja decyzja,
do własnego użytku; poziomy, które zapisuje, są twoje do oglądania, a nie do udostępniania
ani publikowania. Dlatego to osobny pakiet.

Dozwolona alternatywa, która nie czyta żadnego pliku: skrypty misji samego symulatora mogą próbkować teren
(`land.getHeight`, `land.getSurfaceType`) i wypisywać lotniska (`world.getAirbases`), gdy misja działa. Wymaga to
działania DCS przez godziny na teatr i daje grubszą siatkę; nie została zbudowana, ponieważ pliki okazały się czytelne.

## Licencja i źródła {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Wymaga numpy (BSD-3-Clause); `fit` na pliku
`.parquet` wymaga pyarrow (Apache-2.0). Napisane na potrzeby tego projektu. Stałe projekcji to fakty opublikowane przez pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); wzięto tylko liczby. Projekcja to szereg Krügera w ujęciu
C. F. F. Karneya („Transverse Mercator with an accuracy of a few nanometers”, Journal of
Geodesy 85, 2011). Żaden kod nie został wzięty z żadnego innego projektu.
