---
title: "Condiții și licență"
nav_order: 8
lang: ro
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Condiții și licență {#terms-and-licence}

## Condițiile Eagle Dynamics {#eagle-dynamics-terms}

Citite pe 2026-11-07 din `Doc/license_en.txt` al instalării (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). „Program”-ul licențiat
include „THE DATA SUPPLIED WITH IT”. Clauza 3.1:

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

Clauza 3.1 (a) interzice să „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program” fără consimțământ, iar (e) interzice să
„exploit this Program or any of its parts commercially”.

Ce face acest cititor: citește fișiere de date de pe propriul calculator, după ce ați
instalat jocul, în afara jocului. Nu schimbă nimic în joc, nu sparge nicio criptare (singurul
fișier criptat dintr-un dosar de teren este lăsat în pace) și nu vorbește cu niciun server.
Aflarea aspectului unui fișier de date este inginerie inversă în sensul clauzei 3.1 (c), iar un
nivel construit din terenul jocului poate fi considerat o operă derivată. Folosirea cititorului
este decizia dumneavoastră, pentru uzul propriu; nivelurile pe care le scrie sunt ale
dumneavoastră pentru vizualizare, nu pentru a fi distribuite sau publicate. De aceea este un pachet separat.

Alternativa aprobată, care nu citește niciun fișier: scripturile de misiune ale simulatorului
pot măsura solul (`land.getHeight`, `land.getSurfaceType`) și pot lista aerodromurile
(`world.getAirbases`) cât rulează o misiune. Are nevoie de DCS pornit ore întregi pentru fiecare
teatru și dă o grilă mai grosieră; nu a fost construită, pentru că fișierele s-au dovedit
lizibile.

## Licență și surse {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Are nevoie de numpy (BSD-3-Clause); `fit` pe un
`.parquet` are nevoie de pyarrow (Apache-2.0). Scris pentru acest proiect. Constantele de proiecție sunt
fapte publicate de pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); s-au luat doar
numerele. Proiecția este seria lui Krüger, așa cum o dă C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers”, Journal of Geodesy 85, 2011). Niciun cod nu a
fost luat din alt proiect.
