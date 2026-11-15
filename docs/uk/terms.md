---
title: Умови і ліцензія
nav_order: 8
lang: "uk"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Умови і ліцензія {#terms-and-licence}

## Умови Eagle Dynamics {#eagle-dynamics-terms}

Прочитано 2026-11-07 з `Doc/license_en.txt` інсталяції (DCS World End-User Licence
Agreement, The Fighter Collection Ltd). Ліцензована «Програма» включає «THE DATA
SUPPLIED WITH IT». Пункт 3.1:

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

Пункт 3.1 (a) забороняє «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» без згоди, а (e) — «exploit this
Program or any of its parts commercially» (використовувати цю Програму або будь-яку
її частину комерційно).

Що робить цей читач: він читає файли даних на вашому комп'ютері, після того як ви їх
встановили, поза грою. Він нічого не змінює в грі, не ламає шифрування (єдиний
зашифрований файл у папці тереїну залишається недоторканим) і ні з яким сервером не
розмовляє. З'ясування структури файлу даних — це зворотна інженерія в розумінні пункту
3.1 (c), а рівень, побудований з тереїну гри, можна вважати похідним твором. Користування
читачем — ваше рішення, для вашого власного використання; рівні, які він записує, — ваші,
щоб їх дивитися, а не ділитися ними чи публікувати. Тому це окремий пакет.

Санкціонована альтернатива, яка не читає жодного файлу: вбудований у симулятор скриптовий
інтерфейс місій може вибирати висоту землі (`land.getHeight`, `land.getSurfaceType`) і
перелічувати аеробази (`world.getAirbases`), поки місія працює. Це потребує запущеної
DCS годинами на кожен театр і дає грубішу сітку; її не побудовано, бо файли виявилися
придатними для читання.

## Ліцензія і джерела {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Потрібен
numpy (BSD-3-Clause); `fit` на `.parquet` потребує pyarrow (Apache-2.0). Написано для цього
проєкту. Константи проєкцій — це відомості, опубліковані в pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); взято лише числа. Проєкцію
обчислено за рядом Крюгера, як його дав C. F. F. Karney («Transverse Mercator with an
accuracy of a few nanometers», Journal of Geodesy 85, 2011). Жодного коду з інших проєктів
не взято.
