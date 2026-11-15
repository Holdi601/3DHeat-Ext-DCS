---
title: Vilkår og licens
nav_order: 8
lang: "da"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Vilkår og licens {#terms-and-licence}

## Eagle Dynamics' vilkår {#eagle-dynamics-terms}

Læst den 2026-11-07 fra `Doc/license_en.txt` i installationen (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Det licenserede
"Program" omfatter "THE DATA SUPPLIED WITH IT". Punkt 3.1:

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

Punkt 3.1 (a) forbyder at "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" uden samtykke, og (e) at "exploit this
Program or any of its parts commercially".

Hvad denne læser gør: den læser datafiler på din egen maskine, efter du har
installeret dem, uden for spillet. Den ændrer intet i spillet, bryder ingen
kryptering (den ene krypterede fil i en terrænmappe lades urørt) og taler med
ingen server. At finde ud af layoutet i en datafil er reverse engineering i
forstanden af 3.1 (c), og en bane bygget af spillets terræn er formentlig et
afledt værk. Brug af læseren er din beslutning, til dit eget brug; de baner, den
skriver, er dine til at se, ikke til at dele eller offentliggøre. Derfor er det en
separat pakke.

Det godkendte alternativ, som ikke læser nogen fil: simulatorens egen missionsscripting
kan prøve jorden (`land.getHeight`, `land.getSurfaceType`) og liste flyvepladser
(`world.getAirbases`), mens en mission kører. Det kræver, at DCS kører i timevis pr. teater
og giver et grovere gitter; det blev ikke bygget, fordi filerne viste sig at kunne læses.

## Licens og kilder {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kræver numpy (BSD-3-Clause); `fit` på en
`.parquet` kræver pyarrow (Apache-2.0). Skrevet til dette projekt. Projektionskonstanterne er fakta,
offentliggjort af pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); kun tallene
er taget. Projektionen er Krügers række, sådan som C. F. F. Karney giver den
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ingen kode er taget fra noget andet projekt.
