---
title: "Hoe de bestanden worden gelezen"
nav_order: 7
lang: nl
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Hoe de bestanden worden gelezen {#how-the-files-are-read}

Alleen `Mods/terrains/<theatre>/surface/*.surface5` (het grondmesh),
`Scenes/*.scn5` (waar objecten staan, en de doos van elk model),
`AirfieldsTaxiways/*.rn4` en `map/towns.lua` (plaatsnamen, als tekst gelezen,
nooit uitgevoerd). Niet het versleutelde
`terrain.cfg.lua.pak.crypt`, niet `manifest.bin`, niets van het programma.

Het `.surface5`-formaat is niet gedocumenteerd; de indeling, zoals die uit de bestanden is gelezen,
staat beschreven in [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kort samengevat: een index van tegelrecords (een transformatie, begrenzingen, en lijsten van getypeerde
bytestromen, elke lijst gevolgd door de shader en het materiaal waarmee ze wordt getekend), daarna de ruwe
gegevens. Het is niet gecomprimeerd en ook niet versleuteld. De stroom `Pbase` van de tegel
bevat zijn hoekpunten; de groep die als `Land` wordt getekend bevat de driehoeken en een `TRITYPE` per
driehoek, waarvan het laagste bit de zee aangeeft; de andere groepen zijn de overlays die de klassen hierboven geven.

## Gecontroleerd {#verified}

- `list` las de index van elk geïnstalleerd thema (miljoenen tot tientallen miljoenen grondhoekpunten
  per thema), waarbij elke bemonsterde tegel als plausibele meters decodeerde.
- Op gebieden van twee thema's kwamen de steden uit `towns.lua` binnen meters van een grondhoekpunt
  terecht, op land, N van N; het hoogste punt kwam overeen met de echte top tot binnen tien meter;
  vliegvelden, rivieren, dorpen en wegen verschenen in hun klassen. Beide levels laadden in de
  viewer, met steden-markers in dezelfde DCS-meters die op de grond zitten.
- Op een scènegebied lagen de gebouwplaatsingen op hun grond; de landingsbaanverlichting volgde de
  startbaan van het spel, en wagons en muursegmenten lagen allemaal in lijn met de gedecodeerde richting.
- `tests/` bouwt `.surface5`-bestanden in dezelfde indeling, dus er worden hier geen spelgegevens bewaard;
  `tests/test_real_install.py` draait op de installatie van de computer die de tests draait, en wordt
  overgeslagen zonder installatie.

**Niet gecontroleerd:** een heel groot thema in één level (de groottecontrole
hierboven bestaat om een reden), en versies van DCS anders dan de geprobeerde.

## Niet gelezen {#not-read}

- **Gebouwen als vormen** (de modellen zijn `.edm` in `Models/`): alleen dozen, bewust.
  Hun indeling, en die van de scène, staan beschreven in
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); elk geïnstalleerd
  thema wordt gelezen (twee oudere thema's in een variantindeling die de lezer ook kent).
- Bomen, lichten en de andere objecten van de scène: gelezen, niet getekend.
- **Het wegennet als graaf** (`roads/*.rn4`): niet gedecodeerd.
- Texturen, bomen, de golven van de zee, de lagere detailniveaus van het terrein zelf.
