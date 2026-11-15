---
title: "Sąlygos ir licencija"
nav_order: 8
lang: lt
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Sąlygos ir licencija {#terms-and-licence}

## Eagle Dynamics sąlygos {#eagle-dynamics-terms}

Perskaityta 2026-11-07 iš įdiegimo `Doc/license_en.txt` (DCS World
galutinio vartotojo licencijos sutartis, The Fighter Collection Ltd). Licencijuojama
„Program“ apima „THE DATA SUPPLIED WITH IT“. 3.1 punktas:

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

3.1 (a) draudžia be sutikimo „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program“, o (e) – „exploit this
Program or any of its parts commercially“.

Ką daro šis skaitytuvas: skaito duomenų failus jūsų kompiuteryje, įdiegus juos, už žaidimo ribų. Jis nieko nekeičia žaidime, nelaužo
šifravimo (vienas užšifruotas failas reljefo aplanke paliekamas nepaliestas) ir su jokiu serveriu nebendrauja. Duomenų failo
išdėstymo nustatymas yra atvirkštinė inžinerija 3.1 (c) punkto prasme, o lygis, sukurtas iš žaidimo reljefo, galbūt yra
išvestinis kūrinys. Skaitytuvo naudojimas yra jūsų sprendimas, skirtas jūsų pačių naudojimui; lygiai, kuriuos jis įrašo, yra jūsų
žiūrėti, o ne dalintis ar skelbti. Todėl tai atskiras paketas.

Sankcionuota alternatyva, kuri neskaito failų: pačios simuliacijos misijų scenarijai gali išmatuoti reljefą (`land.getHeight`,
`land.getSurfaceType`) ir išvardyti oro bazes (`world.getAirbases`), kol misija vykdoma. Tam reikia DCS veikiančio valandas kiekvienam
teatrui ir jis duoda grubesnį tinklelį; jis nebuvo sukurtas, nes failai pasirodė skaitomi.

## Licencija ir šaltiniai {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Reikia numpy (BSD-3-Clause); `fit` su
`.parquet` reikia pyarrow (Apache-2.0). Parašyta šiam projektui. Projekcijos konstantos yra pydcs paskelbti faktai
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); paimti tik skaičiai. Projekcija yra Krüger eilutė, kaip ją pateikia C. F. F. Karney
(„Transverse Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011). Jokio kodo iš kitų projektų nepaimta.
