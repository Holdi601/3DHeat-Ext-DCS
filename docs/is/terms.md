---
title: "Skilmálar og leyfi"
nav_order: 8
lang: "is"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Skilmálar og leyfi {#terms-and-licence}

## Skilmálar Eagle Dynamics {#eagle-dynamics-terms}

Lesið 2026-11-07 úr `Doc/license_en.txt` í uppsetningunni (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). „Program“ með leyfi
nær yfir „THE DATA SUPPLIED WITH IT“. Grein 3.1:

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

Grein 3.1 (a) bannar að „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program“ án samþykkis, og (e) að „exploit this
Program or any of its parts commercially“.

Það sem þessi lesari gerir: hann les gagnaskrár á þinni eigin vél, eftir að þú
settir þær upp, utan leiksins. Hann breytir engu í leiknum, brýtur enga
dulkóðun (einu dulkóðuðu skránni í landsmöppu er látið í friði) og
talar við engan þjón. Að finna út uppbyggingu gagnaskrár er öfug
verkfræði í skilningi 3.1 (c), og borð smíðað úr landi leiksins er
að líkindum afleitt verk. Notkun lesarans er þín ákvörðun,
til eigin nota; borðin sem hann skrifar eru þín til að skoða, ekki til að deila eða
birta. Þess vegna er þetta sérstakur pakki.

Leyfði valkosturinn, sem les enga skrá: eigin verkefnaskriftun hermisins getur sýnatekið landið
(`land.getHeight`, `land.getSurfaceType`)
og talið upp flugstöðvar (`world.getAirbases`) meðan verkefni keyrir. Hún þarf að DCS
sé í gangi í klukkustundir fyrir hvert leiksvæði og gefur grófara net; hún var ekki smíðuð,
vegna þess að skrárnar reyndust læsilegar.

## Leyfi og heimildir {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Þarf numpy (BSD-3-Clause); `fit` á
`.parquet` þarf pyarrow (Apache-2.0). Skrifað fyrir þetta verkefni. Fastar
vörpunarinnar eru staðreyndir birtar af pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); aðeins tölurnar
voru teknar. Vörpunin er Krüger-röð eins og C. F. F. Karney gefur hana
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Enginn kóði var tekinn úr neinu öðru verkefni.
