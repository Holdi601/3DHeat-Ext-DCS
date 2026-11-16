---
title: Villkor och licens
nav_order: 8
lang: "sv"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Villkor och licens {#terms-and-licence}

## Vad läsaren läser {#what-the-reader-reads}

Läsaren läser datafiler från din egen DCS World-installation på din dator ([Så läses filerna](reading.md)). Den ändrar ingenting i spelet och pratar inte med någon server.

Ingenting från spelet följer med eller distribueras vidare: inga spelfiler, ingen spelkod, inga DLL-filer; testerna bygger själva varje fil de läser. Banorna den skriver stannar på din dator.

3DHeat DCS är inte knutet till eller godkänt av Eagle Dynamics. DCS World och tillhörande namn och varumärken tillhör sina ägare.

Rättighetsinnehavare: öppna ett ärende på [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - vi svarar snabbt och tar bort vad som helst på begäran.

## Licens och källor {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kräver numpy (BSD-3-Clause); `fit` på en
`.parquet` kräver pyarrow (Apache-2.0). Skriven för det här projektet. Projektionskonstanterna är fakta publicerade av pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); bara siffrorna togs. Projektionen är Krügers serie så som C. F. F. Karney ger den
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Ingen kod togs från något annat projekt.
