---
title: Условия и лицензия
nav_order: 8
lang: "ru"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Условия и лицензия {#terms-and-licence}

## Что читает читатель {#what-the-reader-reads}

Читатель читает файлы данных вашей собственной установки DCS World на вашем компьютере ([Как читаются файлы](reading.md)). Он ничего не меняет в игре и не связывается ни с каким сервером.

Ничего из игры не поставляется и не распространяется: ни файлов игры, ни кода игры, ни DLL; тесты сами создают каждый файл, который читают. Уровни, которые он записывает, остаются на вашем компьютере.

3DHeat DCS не связан с компанией Eagle Dynamics и не одобрен ею. DCS World и связанные с ней названия и товарные знаки принадлежат их владельцам.

Правообладатели: откройте задачу на [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - мы быстро отвечаем и по запросу удаляем что угодно.

## Лицензия и источники {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Нужен numpy (BSD-3-Clause);
`fit` на `.parquet` нужен pyarrow (Apache-2.0). Написано для этого проекта. Константы проекции — это
факты, опубликованные pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); взяты только числа.
Проекция — это ряд Крюгера в том виде, как его даёт C. F. F. Karney («Transverse Mercator with an
accuracy of a few nanometers», Journal of Geodesy 85, 2011). Код из других проектов не заимствован.
