---
title: Vilkår og lisens
nav_order: 8
lang: no
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Vilkår og lisens {#terms-and-licence}

## Eagle Dynamics sine vilkår {#eagle-dynamics-terms}

Lest 2026-11-07 fra `Doc/license_en.txt` i installasjonen (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Det lisensierte
«Program» inkluderer «THE DATA SUPPLIED WITH IT». Punkt 3.1:

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

Punkt 3.1 (a) forbyr å «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» uten samtykke, og (e) å «exploit this
Program or any of its parts commercially».

Hva denne leseren gjør: den leser datafiler på din egen maskin, etter at du
installerte dem, utenfor spillet. Den endrer ingenting i spillet, bryter ingen
kryptering (den ene krypterte filen i en terrengmappe blir liggende urørt) og
snakker ikke med noen server. Å finne ut oppsettet til en datafil er reverse engineering i
betydningen 3.1 (c), og et nivå bygget fra spillets terreng er trolig et avledet verk. Å bruke
leseren er din egen avgjørelse, til eget bruk; nivåene den skriver er dine å se på, ikke å dele eller
publisere. Derfor er den en egen pakke.

Det godkjente alternativet, som ikke leser noen fil: simulatorens egen oppdragsscripting kan
prøve bakken (`land.getHeight`, `land.getSurfaceType`) og liste flybaser (`world.getAirbases`)
mens et oppdrag kjører. Det krever at DCS kjører i timevis per teater og gir et grovere rutenett;
det ble ikke bygget, fordi filene viste seg å kunne leses.

## Lisens og kilder {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Krever numpy (BSD-3-Clause); `fit` på en
`.parquet` krever pyarrow (Apache-2.0). Skrevet for dette prosjektet. Projeksjonskonstantene er fakta
publisert av pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); bare tallene
ble tatt. Projeksjonen er Krügers serie slik C. F. F. Karney gir den («Transverse
Mercator with an accuracy of a few nanometers», Journal of Geodesy 85, 2011). Ingen kode
ble tatt fra andre prosjekter.
