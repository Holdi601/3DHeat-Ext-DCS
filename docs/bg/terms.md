---
title: "Условия и лиценз"
nav_order: 8
lang: bg
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Условия и лиценз {#terms-and-licence}

## Условията на Eagle Dynamics {#eagle-dynamics-terms}

Прочетено на 2026-11-07 от `Doc/license_en.txt` на инсталацията (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Лицензираната "Program" включва "THE DATA SUPPLIED WITH IT". Клауза 3.1:

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

Клауза 3.1 (a) забранява да "sell, trade, rent, lease, sub-license, merge, adapt, vary, modify the Program" без съгласие, а (e) - да "exploit this Program or any of its parts commercially".

Какво прави този четец: чете файлове с данни на вашата собствена машина, след като сте ги инсталирали, извън играта. Не променя нищо в играта, не нарушава никакво шифроване (единственият шифрован файл в папката на терена се оставя на мира) и не говори с никакъв сървър. Разбирането на оформлението на файл с данни е обратно инженерство по смисъла на 3.1 (c), а нивото, изградено от терена на играта, е основателно производна работа. Използването на четеца е ваше решение, за ваша собствена употреба; нивата, които той записва, са ваши за преглед, не за споделяне или публикуване. Затова той е отделен пакет.

Санкционираната алтернатива, която не чете никакъв файл: скриптовият език на самата симулация може да вземе проби от земята (`land.getHeight`, `land.getSurfaceType`) и да изброи летищата (`world.getAirbases`), докато мисия работи. Изисква DCS да работи часове за всеки театър и дава по-груба мрежа; не е изградена, защото файловете се оказаха четливи.

## Лиценз и източници {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Изисква numpy (BSD-3-Clause); `fit` върху
`.parquet` изисква pyarrow (Apache-2.0). Написано за този проект. Константите на проекцията са факти, публикувани от pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); взети са само числата. Проекцията е редицата на Krüger, както я дава C. F. F. Karney („Transverse Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011). Не е взет код от друг проект.
