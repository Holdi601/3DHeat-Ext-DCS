---
title: Услови и лиценца
nav_order: 8
lang: "mk"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Услови и лиценца {#terms-and-licence}

## Што чита читачот {#what-the-reader-reads}

Читачот чита датотеки со податоци од твојата сопствена инсталација на DCS World на твојот компјутер ([Како се читаат датотеките](reading.md)). Не менува ништо во играта и не комуницира со ниеден сервер.

Ништо од играта не се испорачува ниту понатаму дистрибуира: ниту датотеки од играта, ниту код од играта, ниту DLL-датотеки; тестовите сами ја градат секоја датотека што ја читаат. Нивоата што ги запишува остануваат на твојата машина.

3DHeat DCS не е поврзан со Eagle Dynamics ниту е одобрен од нив. DCS World и поврзаните имиња и заштитни знаци им припаѓаат на нивните сопственици.

Носители на права: отворете пријава на [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - одговараме брзо и на барање отстрануваме што било.

## Лиценца и извори {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Бара numpy (BSD-3-Clause); `fit` на
`.parquet` бара pyarrow (Apache-2.0). Напишано за овој проект. Константите на
проекцијата се факти објавени од pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); земени се само броевите.
Проекцијата е серијата на Krüger како што ја дава C. F. F. Karney
(„Transverse Mercator with an accuracy of a few nanometers“, Journal of
Geodesy 85, 2011). Не е земен код од ниту еден друг проект.
