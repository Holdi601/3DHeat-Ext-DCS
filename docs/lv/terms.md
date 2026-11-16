---
title: Noteikumi un licence
nav_order: 8
lang: "lv"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Noteikumi un licence {#terms-and-licence}

## Ko lasītājs lasa {#what-the-reader-reads}

Lasītājs lasa datu failus no tavas DCS World instalācijas tavā datorā ([Kā tiek nolasīti faili](reading.md)). Tas neko nemaina spēlē un nesazinās ne ar vienu serveri.

No spēles nekas netiek piegādāts vai izplatīts tālāk: nekādu spēles failu, nekāda spēles koda, nekādu DLL; testi paši izveido katru failu, ko tie lasa. Līmeņi, ko tas uzraksta, paliek tavā datorā.

3DHeat DCS nav saistīts ar Eagle Dynamics un to neatbalsta Eagle Dynamics. DCS World un saistītie nosaukumi un preču zīmes pieder to īpašniekiem.

Tiesību īpašnieki: atveriet pieteikumu vietnē [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - mēs atbildam ātri un pēc pieprasījuma noņemam jebko.

## Licence un avoti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vajag numpy (BSD-3-Clause); `fit` ar
`.parquet` vajag pyarrow (Apache-2.0). Rakstīts šim projektam. Projekcijas konstantes ir fakti, ko publicējis pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); ņemti tikai skaitļi. Projekcija ir Krīgera rinda, kā to dod C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Kods no citiem projektiem nav ņemts.
