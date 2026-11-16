---
title: "Uvjeti i licenca"
nav_order: 8
lang: "bs"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Uvjeti i licenca {#terms-and-licence}

## Šta čitač čita {#what-the-reader-reads}

Čitač čita datoteke s podacima tvoje vlastite instalacije DCS Worlda na tvom računaru ([Kako se datoteke čitaju](reading.md)). Ništa ne mijenja u igri i ne komunicira ni sa jednim serverom.

Ništa iz igre se ne isporučuje niti dalje distribuira: nema datoteka igre, nema koda igre, nema DLL-ova; testovi sami prave svaku datoteku koju čitaju. Nivoi koje zapiše ostaju na tvom računaru.

3DHeat DCS nije povezan s Eagle Dynamics niti ga Eagle Dynamics podržava. DCS World i povezani nazivi i zaštitni znakovi pripadaju svojim vlasnicima.

Nosioci prava: otvorite prijavu na [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odgovaramo brzo i na zahtjev uklanjamo bilo šta.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Treba numpy (BSD-3-Clause); `fit` na
`.parquet` treba pyarrow (Apache-2.0). Napisano za ovaj projekat. Konstante
projekcije su činjenice koje je objavio pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); uzeti su samo brojevi.
Projekcija je Krügerov red kako ga daje C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nikakav kod nije preuzet ni iz jednog drugog projekta.
