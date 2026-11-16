---
title: Умови і ліцензія
nav_order: 8
lang: "uk"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Умови і ліцензія {#terms-and-licence}

## Що читає читач {#what-the-reader-reads}

Читач читає файли даних вашої власної інсталяції DCS World на вашому комп'ютері ([Як читаються файли](reading.md)). Він нічого не змінює в грі й не зв'язується з жодним сервером.

Нічого з гри не постачається і не поширюється: ні файлів гри, ні коду гри, ні DLL; тести самі створюють кожен файл, який читають. Рівні, які він записує, залишаються на вашому комп'ютері.

3DHeat DCS не пов'язаний з компанією Eagle Dynamics і не схвалений нею. DCS World та пов'язані назви й торговельні марки належать їхнім власникам.

Правовласники: відкрийте задачу на [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - ми швидко відповідаємо й на прохання прибираємо будь-що.

## Ліцензія і джерела {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Потрібен
numpy (BSD-3-Clause); `fit` на `.parquet` потребує pyarrow (Apache-2.0). Написано для цього
проєкту. Константи проєкцій — це відомості, опубліковані в pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); взято лише числа. Проєкцію
обчислено за рядом Крюгера, як його дав C. F. F. Karney («Transverse Mercator with an
accuracy of a few nanometers», Journal of Geodesy 85, 2011). Жодного коду з інших проєктів
не взято.
