---
title: Услови и лиценца
nav_order: 8
lang: "mk"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Услови и лиценца {#terms-and-licence}

## Условите на Eagle Dynamics {#eagle-dynamics-terms}

Прочитано на 2026-11-07 од `Doc/license_en.txt` на инсталацијата (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Лиценцираната
„Program“ вклучува „THE DATA SUPPLIED WITH IT“. Клаузула 3.1:

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

Клаузулата 3.1 (a) забранува „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program“ без согласност, а (e) „exploit this
Program or any of its parts commercially“.

Што прави овој читач: чита податочни датотеки на вашата сопствена машина, откако ги
инсталиравте, надвор од играта. Не менува ништо во играта, не пробива никакво
шифрирање (единствената шифрирана датотека во папка на терен е оставена на мира) и
не комуницира со ниту еден сервер. Утврдувањето на распоредот на една податочна датотека е reverse
engineering во смисла на 3.1 (c), а ниво изградено од теренот на играта е
веројатно изведено дело. Користењето на читачот е ваша одлука,
за ваша лична употреба; нивоата што ги пишува се ваши за гледање, не за споделување или
објавување. Затоа е посебен пакет.

Санкционираната алтернатива, која не чита ниту една датотека: сопственото скриптирање на мисии на симулаторот
може да го семплира теренот (`land.getHeight`, `land.getSurfaceType`)
и да ги наведе аеродромските бази (`world.getAirbases`) додека трае мисија. Бара DCS
да работи со часови по театар и дава погруба мрежа; не беше изградено,
затоа што датотеките се покажаа читливи.

## Лиценца и извори {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Бара numpy (BSD-3-Clause); `fit` на
`.parquet` бара pyarrow (Apache-2.0). Напишано за овој проект. Константите на
проекцијата се факти објавени од pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); земени се само броевите.
Проекцијата е серијата на Krüger како што ја дава C. F. F. Karney
(„Transverse Mercator with an accuracy of a few nanometers“, Journal of
Geodesy 85, 2011). Не е земен код од ниту еден друг проект.
