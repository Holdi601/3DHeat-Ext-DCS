---
title: "Feltételek és licenc"
nav_order: 8
lang: "hu"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Feltételek és licenc {#terms-and-licence}

## Mit olvas az olvasó {#what-the-reader-reads}

Az olvasó a saját DCS World-telepítésed adatfájljait olvassa a számítógépeden ([Hogyan olvasódnak be a fájlok](reading.md)). Semmit nem változtat a játékban, és semmilyen szerverrel nem kommunikál.

A játékból semmi nem kerül kiadásra vagy továbbterjesztésre: sem játékfájl, sem játékkód, sem DLL; a tesztek maguk állítják elő minden fájlt, amelyet olvasnak. Az általa írt pályák a gépeden maradnak.

A(z) 3DHeat DCS nem áll kapcsolatban a(z) Eagle Dynamics céggel, és az nem is támogatja. A(z) DCS World és a kapcsolódó nevek és védjegyek a tulajdonosaikat illetik.

Jogtulajdonosok: nyissatok bejelentést itt: [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - gyorsan válaszolunk, és kérésre bármit eltávolítunk.

## Licenc és források {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Szükséges a numpy (BSD-3-Clause);
a `fit` `.parquet` fájlon a pyarrow-t (Apache-2.0) igényli. Ezt a projektnek írták. A vetítési állandók a pydcs
által közzétett tények (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); csak a számokat vettük át. A vetítés
Krüger-sorozata, ahogy C. F. F. Karney adja meg („Transverse Mercator with an accuracy of a few nanometers”, Journal
of Geodesy 85, 2011). Kódot más projektből nem vettünk át.
