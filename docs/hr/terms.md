---
title: Uvjeti i licenca
nav_order: 8
lang: "hr"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Uvjeti i licenca {#terms-and-licence}

## Što čitač čita {#what-the-reader-reads}

Čitač čita podatkovne datoteke tvoje vlastite instalacije DCS Worlda na tvom računalu ([Kako se datoteke čitaju](reading.md)). Ništa ne mijenja u igri i ne razgovara ni s jednim poslužiteljem.

Ništa iz igre ne isporučuje se niti dalje distribuira: nema datoteka igre, nema koda igre, nema DLL-ova; testovi sami grade svaku datoteku koju čitaju. Razine koje zapiše ostaju na tvom računalu.

3DHeat DCS nije povezan s Eagle Dynamics niti ga Eagle Dynamics podržava. DCS World i povezani nazivi i zaštitni znakovi pripadaju svojim vlasnicima.

Nositelji prava: otvorite prijavu na [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odgovaramo brzo i na zahtjev uklanjamo bilo što.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Treba numpy (BSD-3-Clause); `fit` na
`.parquet` datoteci treba pyarrow (Apache-2.0). Napisano za ovaj projekt. Konstante projekcije su činjenice koje objavljuje pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); uzeti su samo brojevi. Projekcija je Krügerov niz kako ga daje C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Nijedan kod nije preuzet ni iz jednog drugog projekta.
