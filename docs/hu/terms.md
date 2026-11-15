---
title: "Feltételek és licenc"
nav_order: 8
lang: "hu"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Feltételek és licenc {#terms-and-licence}

## Az Eagle Dynamics feltételei {#eagle-dynamics-terms}

Elolvasva 2026-11-07-én a telepítés `Doc/license_en.txt` fájljából (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). A licencelt
„Program” magában foglalja a „THE DATA SUPPLIED WITH IT”-et (a vele szállított adatokat). A 3.1. pont:

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

A 3.1. (a) pont tiltja, hogy a Programot az engedély nélkül „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program” (eladni, cserélni, bérbe adni, allicencelni, összeolvasztani, átalakítani,
módosítani), a (e) pont pedig, hogy „exploit this Program or any of its parts commercially” (kereskedelmi
célra hasznosítani).

Mit csinál ez az olvasó: a telepítés után, a játékon kívül, a saját gépén lévő adatfájlokat olvassa. Semmit
nem módosít a játékban, nem tör fel titkosítást (a terepmappában lévő egyetlen titkosított fájlhoz nem nyúl),
és nem kommunikál semmilyen szerverrel. Egy adatfájl elrendezésének kitalálása a 3.1. (c) pont szerinti
visszafejtés, és a játék terepéből épített pálya vitathatóan származékos mű. Az olvasó használata a te döntésed,
a saját használatodra; az általad írt pályák a tieid, megtekintésre, de nem megosztásra vagy közzétételre. Ezért
külön csomag.

Az engedélyezett alternatíva, amely nem olvas fájlt: a szimulátor saját küldetés-szkriptelése mintavételezheti a
talajt (`land.getHeight`, `land.getSurfaceType`), és felsorolhatja a repülőtereket (`world.getAirbases`) egy küldetés
futása közben. Ehhez a DCS órákig fut színházanként, és durvább rácsot ad; nem készült el, mert a fájlok olvashatónak
bizonyultak.

## Licenc és források {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Szükséges a numpy (BSD-3-Clause);
a `fit` `.parquet` fájlon a pyarrow-t (Apache-2.0) igényli. Ezt a projektnek írták. A vetítési állandók a pydcs
által közzétett tények (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); csak a számokat vettük át. A vetítés
Krüger-sorozata, ahogy C. F. F. Karney adja meg („Transverse Mercator with an accuracy of a few nanometers”, Journal
of Geodesy 85, 2011). Kódot más projektből nem vettünk át.
