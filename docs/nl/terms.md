---
title: "Voorwaarden en licentie"
nav_order: 8
lang: nl
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Voorwaarden en licentie {#terms-and-licence}

## De voorwaarden van Eagle Dynamics {#eagle-dynamics-terms}

Gelezen op 2026-11-07 uit `Doc/license_en.txt` van de installatie (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Het gelicentieerde
"Program" omvat "THE DATA SUPPLIED WITH IT". Clausule 3.1:

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

Clausule 3.1 (a) verbiedt om het Programma "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" te verkopen, verhandelen, verhuren, in sublicentie geven, samenvoegen,
aanpassen, wijzigen zonder toestemming, en (e) om "exploit this
Program or any of its parts commercially" commercieel te exploiteren.

Wat deze lezer doet: hij leest gegevensbestanden op je eigen computer, nadat je ze hebt geïnstalleerd,
buiten het spel. Hij verandert niets aan het spel, breekt geen versleuteling (het ene versleutelde
bestand in een terreinmap wordt met rust gelaten) en praat met geen server. Uitzoeken hoe een
gegevensbestand is opgebouwd, is reverse engineering in de zin van 3.1 (c), en een level dat uit het
terrein van het spel is gebouwd, is naar alle waarschijnlijkheid een afgeleid werk. Het gebruik van de
lezer is jouw beslissing, voor eigen gebruik; de levels die hij schrijft mag jij bekijken, niet delen
of publiceren. Daarom is het een apart pakket.

Het toegestane alternatief, dat geen bestand leest: het eigen missiescript van de simulator kan de grond
bemonsteren (`land.getHeight`, `land.getSurfaceType`) en luchthavens opsommen (`world.getAirbases`)
terwijl een missie draait. Dat vraagt uren DCS-gebruik per thema en geeft een grover raster; het is
niet gebouwd, omdat de bestanden leesbaar bleken.

## Licentie en bronnen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vereist numpy (BSD-3-Clause); `fit` op een
`.parquet` vereist pyarrow (Apache-2.0). Voor dit project geschreven. De
projectieconstanten zijn feiten die gepubliceerd zijn door pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); alleen de getallen zijn overgenomen. De
projectie is die van Krüger, zoals C. F. F. Karney die geeft ("Transverse Mercator with an
accuracy of a few nanometers", Journal of Geodesy 85, 2011). Er is geen code van een ander project overgenomen.
