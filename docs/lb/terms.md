---
title: "Bedingungen a Lizenz"
nav_order: 8
lang: lb
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Bedingungen a Lizenz {#terms-and-licence}

## D'Bedingunge vun Eagle Dynamics {#eagle-dynamics-terms}

Den 2026-11-07 aus `Doc/license_en.txt` vun der Installatioun gelies (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Dat lizenzéiert
„Program“ enthält „THE DATA SUPPLIED WITH IT“. Klausel 3.1:

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

Klausel 3.1 (a) verbitt, ouni Zoustëmmung de Program ze „sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify“, an (e) „exploit this
Program or any of its parts commercially“.

Wat dëse Reader mécht: en liest Datendateien op Ärem eegene Rechner, nodeems Dir se
installéiert hutt, ausserhalb vum Spill. Hie ännert näischt am Spill, brécht keng
Verschlësselung (déi eenzeg verschlësselt Datei an engem Terrain-Dossier gëtt a Rou gelooss) a
schwätzt mat kengem Server. D'Layout vun enger Datendatei erauszefannen ass Reverse
Engineering am Sënn vun 3.1 (c), an e Level, dat aus dem Terrain vum Spill gebaut gëtt, ass
mat Grond e Derivat-Wierk. De Reader ze benotzen ass Är Entscheedung,
fir Äre perséinleche Gebrauch; d'Levelen, déi en schreift, sinn Är, fir ze kucken, net fir ze deelen oder ze
publizéieren. Dofir ass et e getrennte Package.

Déi erlaabten Alternativ, déi keng Datei liest: dem Sim säin eegent Mission-
Scripting kann de Buedem ofdasten (`land.getHeight`, `land.getSurfaceType`)
an Airbasen oplëschten (`world.getAirbases`), wärend eng Mission leeft. Et brauch DCS,
dat Stonne pro Theater leeft, a gëtt e gréiwert Gitter; et gouf net gebaut,
well d'Dateien sech als liesbar erausgestallt hunn.

## Lizenz a Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Brauch numpy (BSD-3-Clause); `fit` op enger
`.parquet` brauch pyarrow (Apache-2.0). Fir dëse Projet geschriwwen. D'
Projektiounskonstanten sinn Fakten, déi pydcs publizéiert
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); nëmmen d'Zuele goufen
geholl. D'Projektioun ass d'Krüger-Serie, wéi C. F. F. Karney se gëtt
(„Transverse Mercator with an accuracy of a few nanometers“, Journal of
Geodesy 85, 2011). Et gouf kee Code vun engem anere Projet geholl.
