---
title: Условия и лицензия
nav_order: 8
lang: ru
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Условия и лицензия {#terms-and-licence}

## Условия Eagle Dynamics {#eagle-dynamics-terms}

Прочитано 2026-11-07 из `Doc/license_en.txt` установки (DCS World End-User Licence Agreement,
The Fighter Collection Ltd). Лицензируемая «Программа» включает «THE DATA SUPPLIED WITH IT».
Пункт 3.1:

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

Пункт 3.1 (a) запрещает «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» без согласия, а (e) — «exploit this
Program or any of its parts commercially» (использовать эту Программу или любую её часть в коммерческих целях).

Что делает этот читатель: он читает файлы данных на вашем компьютере, после того как вы их установили,
вне игры. Он ничего не меняет в игре, не ломает шифрование (единственный зашифрованный файл в папке
местности оставлен в покое) и не обращается ни к одному серверу. Выяснение раскладки файла данных —
это обратная разработка в смысле 3.1 (c), а уровень, построенный по местности игры, по сути может быть
производным произведением. Использование читателя — ваше решение, для вашего личного использования;
уровни, которые он пишет, принадлежат вам для просмотра, но не для передачи или публикации. Поэтому он
и выделен в отдельный пакет.

Санкционированная альтернатива, которая не читает ни одного файла: скриптовый язык миссий самого
симулятора может брать пробы земли (`land.getHeight`, `land.getSurfaceType`) и перечислять аэродромы
(`world.getAirbases`) во время работы миссии. Для этого нужно, чтобы DCS работала часами на каждый
театр, и сетка получается грубее; его не строили, потому что файлы оказались читаемыми.

## Лицензия и источники {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Нужен numpy (BSD-3-Clause);
`fit` на `.parquet` нужен pyarrow (Apache-2.0). Написано для этого проекта. Константы проекции — это
факты, опубликованные pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); взяты только числа.
Проекция — это ряд Крюгера в том виде, как его даёт C. F. F. Karney («Transverse Mercator with an
accuracy of a few nanometers», Journal of Geodesy 85, 2011). Код из других проектов не заимствован.
