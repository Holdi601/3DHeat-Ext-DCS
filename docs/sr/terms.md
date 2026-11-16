---
title: Услови и лиценца
nav_order: 8
lang: "sr"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Услови и лиценца {#terms-and-licence}

## Шта читач чита {#what-the-reader-reads}

Читач чита датотеке са подацима твоје сопствене инсталације DCS World-а на твом рачунару ([Како се датотеке читају](reading.md)). Ништа не мења у игри и не комуницира ни са једним сервером.

Ништа из игре се не испоручује нити даље дистрибуира: нема датотека игре, нема кода игре, нема DLL-ова; тестови сами праве сваку датотеку коју читају. Нивои које запише остају на твом рачунару.

3DHeat DCS није повезан са Eagle Dynamics нити га Eagle Dynamics подржава. DCS World и повезани називи и жигови припадају својим власницима.

Носиоци права: отворите пријаву на [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - одговарамо брзо и на захтев уклањамо било шта.

## Лиценца и извори {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Потребан је numpy (BSD-3-Clause); `fit` над
`.parquet` датотеком захтева pyarrow (Apache-2.0). Написано за овај пројекат. Константе
пројекције су чињенице које објављује pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); узети су само бројеви.
Пројекција је Krüger-ов ред, онако како га даје C. F. F. Karney
(„Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ниједан код није узет из другог пројекта.
