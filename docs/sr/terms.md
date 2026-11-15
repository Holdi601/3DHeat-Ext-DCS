---
title: Услови и лиценца
nav_order: 8
lang: sr
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Услови и лиценца {#terms-and-licence}

## Услови Eagle Dynamics-а {#eagle-dynamics-terms}

Прочитано 2026-11-07 из `Doc/license_en.txt` инсталације (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Лиценцирани
„Program" укључује „THE DATA SUPPLIED WITH IT". Клауза 3.1:

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

Клаузула 3.1 (a) забрањује да се „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" без сагласности, а (e) да се „exploit this
Program or any of its parts commercially".

Шта овај читач ради: чита датотеке података на вашем рачунару, након што сте их
инсталирали, ван игре. Ништа не мења у игри, не разбија шифровање (једна шифрована
датотека у фасцикли терена се оставља на миру) и ни с киме не разговара преко
сервера. Откривање распореда датотеке података је обрнуто инжењерство у смислу
3.1 (c), а ниво направљен од игриног терена вероватно је изведено дело. Коришћење
читача је ваша одлука, за вашу употребу; нивои које он пише су ваши за
гледање, не за дељење или објављивање. Зато је то засебан пакет.

Одобрена алтернатива, која не чита ниједну датотеку: сопствени скриптни језик
симулатора може да узоркује тло (`land.getHeight`, `land.getSurfaceType`) и да
наброји аеродроме (`world.getAirbases`) док мисија ради. То захтева да DCS ради
по сатима за сваки театар и даје грубљу мрежу; није направљено, јер су се датотеке показале читљивим.

## Лиценца и извори {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Потребан је numpy (BSD-3-Clause); `fit` над
`.parquet` датотеком захтева pyarrow (Apache-2.0). Написано за овај пројекат. Константе
пројекције су чињенице које објављује pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); узети су само бројеви.
Пројекција је Krüger-ов ред, онако како га даје C. F. F. Karney
(„Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ниједан код није узет из другог пројекта.
