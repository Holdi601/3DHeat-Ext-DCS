---
title: "Podmínky a licence"
nav_order: 8
lang: "cs"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Podmínky a licence {#terms-and-licence}

## Co čtečka čte {#what-the-reader-reads}

Čtečka čte datové soubory vaší vlastní instalace DCS World na vašem počítači ([Jak se soubory čtou](reading.md)). Ve hře nic nemění a s žádným serverem nekomunikuje.

Nic ze hry se nedodává ani dále nešíří: žádné soubory hry, žádný kód hry, žádné knihovny DLL; testy si každý soubor, který čtou, vytvoří samy. Úrovně, které zapíše, zůstávají na vašem počítači.

3DHeat DCS není přidružen k Eagle Dynamics ani jím schválen. DCS World a související názvy a ochranné známky patří jejich vlastníkům.

Držitelé práv: založte hlášení na [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odpovídáme rychle a na požádání cokoli odstraníme.

## Licence a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potřebuje numpy (BSD-3-Clause); `fit` na
`.parquet` potřebuje pyarrow (Apache-2.0). Napsáno pro tento projekt. Konstanty projekce jsou
údaje zveřejněné knihovnou pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); převzata
byla jen čísla. Projekce je Krügerova řada, jak ji podává C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).
Žádný kód nebyl převzat z jiného projektu.
