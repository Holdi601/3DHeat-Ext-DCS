---
title: "Pogoji in licenca"
nav_order: 8
lang: "sl"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Pogoji in licenca {#terms-and-licence}

## Pogoji podjetja Eagle Dynamics {#eagle-dynamics-terms}

Prebrano 2026-11-07 iz `Doc/license_en.txt` namestitve (licenčna pogodba končnega uporabnika
DCS World, The Fighter Collection Ltd). Licencirani »Program« vključuje »THE DATA SUPPLIED WITH IT«.
Točka 3.1:

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

Točka 3.1 (a) prepoveduje »sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program« brez soglasja, točka (e) pa »exploit this
Program or any of its parts commercially«.

Kaj počne ta bralnik: bere podatkovne datoteke na tvojem računalniku, potem ko si jih namestil,
zunaj igre. Ničesar ne spremeni v igri, ne razbije nobenega šifriranja (ena šifrirana datoteka v
mapi terena je pustena pri miru) in se ne pogovarja z nobenim strežnikom. Ugotavljanje zgradbe
podatkovne datoteke je po točki 3.1 (c) vzvratni inženiring, raven, zgrajena iz terena igre, pa je
lahko izpeljano delo. Uporaba bralnika je tvoja odločitev, za tvojo lastno uporabo; ravni, ki jih
zapiše, so tvoje za ogled, ne za deljenje ali objavo. Zato je to ločen paket.

Dopustna možnost, ki ne bere nobene datoteke: vgrajeno skriptiranje misij v simulatorju lahko med
tekom misije vzorči tla (`land.getHeight`, `land.getSurfaceType`) in našteje letališča
(`world.getAirbases`). Potrebuje, da DCS teče ure na teater, in daje grobejšo mrežo; ni bila zgrajena,
ker so se datoteke izkazale za berljive.

## Licenca in viri {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potrebuje numpy
(BSD-3-Clause); `fit` na `.parquet` potrebuje pyarrow (Apache-2.0). Napisano za ta projekt. Konstante
projekcij so dejstva, ki jih objavlja pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); vzete
so bile samo številke. Projekcija je Krügerjeva vrsta, kot jo podaja C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Nobena koda ni vzeta iz
drugega projekta.
