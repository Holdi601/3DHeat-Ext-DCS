---
title: Vilkår og licens
nav_order: 8
lang: "da"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Vilkår og licens {#terms-and-licence}

## Hvad læseren læser {#what-the-reader-reads}

Læseren læser datafiler fra din egen DCS World-installation på din computer ([Sådan læses filerne](reading.md)). Den ændrer intet i spillet og taler ikke med nogen server.

Intet fra spillet følger med eller videredistribueres: ingen spilfiler, ingen spilkode, ingen DLL'er; testene bygger selv hver fil, de læser. De baner, den skriver, bliver på din maskine.

3DHeat DCS er ikke tilknyttet eller godkendt af Eagle Dynamics. DCS World og tilhørende navne og varemærker tilhører deres ejere.

Rettighedshavere: opret et issue på [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - vi svarer hurtigt og fjerner hvad som helst på anmodning.

## Licens og kilder {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kræver numpy (BSD-3-Clause); `fit` på en
`.parquet` kræver pyarrow (Apache-2.0). Skrevet til dette projekt. Projektionskonstanterne er fakta,
offentliggjort af pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); kun tallene
er taget. Projektionen er Krügers række, sådan som C. F. F. Karney giver den
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ingen kode er taget fra noget andet projekt.
