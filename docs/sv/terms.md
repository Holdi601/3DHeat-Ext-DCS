---
title: Villkor och licens
nav_order: 8
lang: sv
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Villkor och licens {#terms-and-licence}

## Eagle Dynamics villkor {#eagle-dynamics-terms}

Läst 2026-11-07 från `Doc/license_en.txt` i installationen (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Den licensierade
"Program" omfattar "THE DATA SUPPLIED WITH IT". Klausul 3.1:

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

Klausul 3.1 (a) förbjuder att "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" utan samtycke, och (e) att "exploit this
Program or any of its parts commercially".

Vad den här läsaren gör: den läser datafiler på din egen dator, efter att du installerat dem, utanför spelet. Den ändrar ingenting i spelet, bryter ingen kryptering (den enda krypterade filen i en terrängmapp lämnas ifred) och talar inte med någon server. Att räkna ut layouten på en datafil är omvänd utveckling i den mening som avses i 3.1 (c), och en nivå byggd av spelets terräng är möjligen ett härlett verk. Att använda läsaren är ditt beslut, för ditt eget bruk; nivåerna den skriver är dina att titta på, inte att dela eller publicera. Därför är den ett separat paket.

Det godkända alternativet, som inte läser någon fil: simulatorns egna missionsskript kan provta marken (`land.getHeight`, `land.getSurfaceType`) och lista flygbaser (`world.getAirbases`) medan ett uppdrag körs. Det kräver att DCS kör i timmar per teater och ger ett grövre rutnät; det byggdes inte, eftersom filerna visade sig gå att läsa.

## Licens och källor {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kräver numpy (BSD-3-Clause); `fit` på en
`.parquet` kräver pyarrow (Apache-2.0). Skriven för det här projektet. Projektionskonstanterna är fakta publicerade av pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); bara siffrorna togs. Projektionen är Krügers serie så som C. F. F. Karney ger den
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ingen kod togs från något annat projekt.
