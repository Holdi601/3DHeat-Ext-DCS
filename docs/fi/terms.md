---
title: "Ehdot ja lisenssi"
nav_order: 8
lang: "fi"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Ehdot ja lisenssi {#terms-and-licence}

## Mitä lukija lukee {#what-the-reader-reads}

Lukija lukee datatiedostoja omasta DCS World -asennuksestasi tietokoneellasi ([Miten tiedostot luetaan](reading.md)). Se ei muuta pelissä mitään eikä ota yhteyttä mihinkään palvelimeen.

Pelistä ei toimiteta eikä jaeta mitään: ei pelitiedostoja, ei pelin koodia, ei DLL-tiedostoja; testit rakentavat itse jokaisen lukemansa tiedoston. Sen kirjoittamat tasot pysyvät koneellasi.

3DHeat DCS ei ole sidoksissa yhtiöön Eagle Dynamics, eikä se ole sen hyväksymä. DCS World ja siihen liittyvät nimet ja tavaramerkit kuuluvat omistajilleen.

Oikeudenhaltijat: avatkaa issue osoitteessa [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - vastaamme nopeasti ja poistamme pyynnöstä mitä tahansa.

## Lisenssi ja lähteet {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Tarvitsee numpy-kirjaston (BSD-3-Clause);
`fit` `.parquet`-tiedostolle tarvitsee pyarrow-kirjaston (Apache-2.0). Kirjoitettu tätä projektia varten.
Projektiovakiot ovat pydcs:n julkaisemia tosiasioita (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`);
otettiin vain luvut. Projektio on Krügerin sarja sellaisena kuin C. F. F. Karney sen esittää
("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).
Koodia ei otettu mistään muusta projektista.
