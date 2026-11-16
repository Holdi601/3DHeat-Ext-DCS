---
title: "Podmienky a licencia"
nav_order: 8
lang: "sk"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Podmienky a licencia {#terms-and-licence}

## Čo čítačka číta {#what-the-reader-reads}

Čítačka číta dátové súbory vašej vlastnej inštalácie DCS World na vašom počítači ([Ako sa čítajú súbory](reading.md)). V hre nič nemení a nekomunikuje so žiadnym serverom.

Nič z hry sa nedodáva ani ďalej nešíri: žiadne súbory hry, žiadny kód hry, žiadne knižnice DLL; testy si každý súbor, ktorý čítajú, vytvoria samy. Úrovne, ktoré zapíše, zostávajú na vašom počítači.

3DHeat DCS nie je pridružený k Eagle Dynamics ani ním schválený. DCS World a súvisiace názvy a ochranné známky patria ich vlastníkom.

Držitelia práv: založte hlásenie na [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odpovedáme rýchlo a na požiadanie čokoľvek odstránime.

## Licencia a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potrebuje numpy (BSD-3-Clause); `fit` na
`.parquet` potrebuje pyarrow (Apache-2.0). Napísané pre tento projekt. Konštanty projekcie sú fakty zverejnené
pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); prebrali sa len čísla. Projekcia je Krügerov rad, ako ho podáva C. F. F. Karney („Transverse Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011). Žiadny kód sa neprebral z iného projektu.
