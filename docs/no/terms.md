---
title: Vilkår og lisens
nav_order: 8
lang: "no"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Vilkår og lisens {#terms-and-licence}

## Hva leseren leser {#what-the-reader-reads}

Leseren leser datafiler fra din egen DCS World-installasjon på datamaskinen din ([Slik leses filene](reading.md)). Den endrer ingenting i spillet og snakker ikke med noen server.

Ingenting fra spillet følger med eller videredistribueres: ingen spillfiler, ingen spillkode, ingen DLL-er; testene bygger selv hver fil de leser. Banene den skriver, blir værende på maskinen din.

3DHeat DCS er ikke tilknyttet eller godkjent av Eagle Dynamics. DCS World og tilhørende navn og varemerker tilhører sine eiere.

Rettighetshavere: opprett en sak på [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - vi svarer raskt og fjerner hva som helst på forespørsel.

## Lisens og kilder {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Krever numpy (BSD-3-Clause); `fit` på en
`.parquet` krever pyarrow (Apache-2.0). Skrevet for dette prosjektet. Projeksjonskonstantene er fakta
publisert av pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); bare tallene
ble tatt. Projeksjonen er Krügers serie slik C. F. F. Karney gir den («Transverse
Mercator with an accuracy of a few nanometers», Journal of Geodesy 85, 2011). Ingen kode
ble tatt fra andre prosjekter.
