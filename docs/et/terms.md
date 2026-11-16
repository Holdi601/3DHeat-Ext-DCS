---
title: "Tingimused ja litsents"
nav_order: 8
lang: "et"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Tingimused ja litsents {#terms-and-licence}

## Mida lugeja loeb {#what-the-reader-reads}

Lugeja loeb sinu enda DCS Worldi paigalduse andmefaile sinu arvutis ([Kuidas faile loetakse](reading.md)). See ei muuda mängus midagi ega suhtle ühegi serveriga.

Mängust ei tarnita ega levitata midagi: ei mängufaile, ei mängu koodi, ei DLL-faile; testid ehitavad iga loetava faili ise. Tema kirjutatud tasemed jäävad sinu arvutisse.

3DHeat DCS ei ole seotud ettevõttega Eagle Dynamics ega selle poolt heaks kiidetud. DCS World ja sellega seotud nimed ning kaubamärgid kuuluvad nende omanikele.

Õiguste omajad: avage pöördumine aadressil [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - vastame kiiresti ja eemaldame soovi korral mida tahes.

## Litsents ja allikad {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vajab numpy (BSD-3-Clause); `fit` `.parquet`-failil
vajab pyarrow (Apache-2.0). Kirjutatud selle projekti jaoks. Projektsiooni konstandid on
pydcs'i avaldatud faktid (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); võeti ainult numbrid. Projektsioon on Krügeri rida, nagu seda annab C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ühtegi koodi ei võetud ühestki teisest projektist.
