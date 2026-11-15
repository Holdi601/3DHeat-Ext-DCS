---
title: "Ehdot ja lisenssi"
nav_order: 8
lang: "fi"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Ehdot ja lisenssi {#terms-and-licence}

## Eagle Dynamicsin ehdot {#eagle-dynamics-terms}

Luettu 2026-11-07 asennuksen tiedostosta `Doc/license_en.txt` (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Lisensoitu
"Program" sisältää "THE DATA SUPPLIED WITH IT". Kohta 3.1:

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

Kohta 3.1 (a) kieltää "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" ilman lupaa, ja (e) kieltää "exploit this
Program or any of its parts commercially" eli hyödyntämisen kaupallisesti.

Mitä tämä lukija tekee: se lukee datatiedostoja omalla koneellasi sen jälkeen, kun
olet asentanut ne, pelin ulkopuolella. Se ei muuta mitään pelissä, ei riko salausta
(terrain-kansion yksi salattu tiedosto jätetään rauhaan) eikä ota yhteyttä mihinkään palvelimeen.
Datatiedoston asettelun selvittäminen on kohdan 3.1 (c) tarkoittamaa käänteistekniikkaa, ja
pelin maastosta rakennettu kenttä on väitettävästi johdannainen teos. Lukijan käyttö on sinun
päätöksesi, omaan käyttöösi; kentät, joita se kirjoittaa, ovat sinun katseltaviksi, eivät jaettaviksi
tai julkaistaviksi. Siksi se on erillinen paketti.

Hyväksytty vaihtoehto, joka ei lue yhtään tiedostoa: simulaattorin oma tehtäväskriptaus voi
näytteistää maaston (`land.getHeight`, `land.getSurfaceType`) ja luetella lentotukikohdat
(`world.getAirbases`) tehtävän ollessa käynnissä. Se vaatii DCS:n käynnissä tuntikausia teatteria kohden
ja antaa karkeamman ruudukon; sitä ei rakennettu, koska tiedostot osoittautuivat luettaviksi.

## Lisenssi ja lähteet {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Tarvitsee numpy-kirjaston (BSD-3-Clause);
`fit` `.parquet`-tiedostolle tarvitsee pyarrow-kirjaston (Apache-2.0). Kirjoitettu tätä projektia varten.
Projektiovakiot ovat pydcs:n julkaisemia tosiasioita (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`);
otettiin vain luvut. Projektio on Krügerin sarja sellaisena kuin C. F. F. Karney sen esittää
("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).
Koodia ei otettu mistään muusta projektista.
