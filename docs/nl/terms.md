---
title: "Voorwaarden en licentie"
nav_order: 8
lang: "nl"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Voorwaarden en licentie {#terms-and-licence}

## Wat de lezer leest {#what-the-reader-reads}

De lezer leest gegevensbestanden van je eigen DCS World-installatie op je computer ([Hoe de bestanden worden gelezen](reading.md)). Hij verandert niets aan het spel en praat met geen enkele server.

Niets uit het spel wordt meegeleverd of verspreid: geen spelbestanden, geen spelcode, geen DLL's; de tests bouwen elk bestand dat ze lezen zelf. De levels die hij schrijft blijven op je computer.

3DHeat DCS is niet verbonden aan en niet goedgekeurd door Eagle Dynamics. DCS World en bijbehorende namen en handelsmerken zijn van hun eigenaars.

Rechthebbenden: open een issue op [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - we reageren snel en verwijderen alles op verzoek.

## Licentie en bronnen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vereist numpy (BSD-3-Clause); `fit` op een
`.parquet` vereist pyarrow (Apache-2.0). Voor dit project geschreven. De
projectieconstanten zijn feiten die gepubliceerd zijn door pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); alleen de getallen zijn overgenomen. De
projectie is die van Krüger, zoals C. F. F. Karney die geeft ("Transverse Mercator with an
accuracy of a few nanometers", Journal of Geodesy 85, 2011). Er is geen code van een ander project overgenomen.
