---
title: "Wéi d'Dateie gelies ginn"
nav_order: 7
lang: lb
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Wéi d'Dateie gelies ginn {#how-the-files-are-read}

Nëmmen `Mods/terrains/<theatre>/surface/*.surface5` (d'Buedem-Mesh),
`Scenes/*.scn5` (wou Objeten stinn, an d'Këscht vun all Modell),
`AirfieldsTaxiways/*.rn4` an `map/towns.lua` (Uertsnimm, als Text gelies,
ni ausgeféiert). Net déi verschlësselt
`terrain.cfg.lua.pak.crypt`, net `manifest.bin`, näischt vum Programm.

D'`.surface5`-Format ass net dokumentéiert; d'Layout, wéi aus den Dateie gelies,
steet an [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kuerz: en Index vu Kachel-Records (eng Transformatioun, Grenzen, a Lëschte vun typiséierte
Byte-Streams, jidd Lëscht gefollegt vum Shader a Material, mat deem se gezeechent
gëtt), dann d'Rohdaten. Et ass weder komprimiert nach verschlësselt. Dem Kachel säi
`Pbase`-Stream hält seng Vertices; d'Grupp, déi als `Land` gezeechent gëtt, hält d'
Dräiecker an en `TRITYPE` pro Dräieck, deem säin niddregst Bit d'Mier markéiert; déi
aner Gruppen sinn d'Overlays, déi d'Klassen hei uewen ginn.

## Gepréift {#verified}

- `list` huet den Index vun all installéiertem Theater gelies (Millioune bis Zéngerte vu
  Millioune Buedem-Vertices pro Theater), all gesampelt Kachel huet sech zu plausibelen
  Meter dekodéiert.
- Op Regioune vun zwee Theatere sinn d'Stied aus `towns.lua` bannent Meter
  vun engem Buedem-Vertex, op Land, gelant, N vun N; dee héchste Buedem huet mam richtege
  Gipfel bannent zéng Meter iwwereneggestëmmt; Fluchhäfen, Flëss, Dierfer a Stroossen hunn sech an
  hire Klasse gewisen. Béid Levelen hu sech am Viewer gelueden, mat Stad-Markéierungen a
  selwechte DCS-Meter um Buedem.
- Op enger Szeregioun sinn d'Gebai-Placementer op hirem Buedem gelant; Pistluuchten
  hunn dem Spill seng Piste nogezeechent, a Wagonen a Maueresegmenter hu mam
  dekodéierten Heading iwwereneggestëmmt, all vun hinnen.
- `tests/` baut `.surface5`-Dateien mam selwechte Layout, sou datt hei keng Spilldaten
  gehale ginn; `tests/test_real_install.py` leeft op der Installatioun vum Rechner,
  op deem d'Tester lafen, a gëtt ouni eng iwwersprong.

**Net gepréift:** dat ganzt vun engem grousse Theater an engem Level (d'Gréisstewuecht
hei uewen ass net ouni Grond do), a Versioune vun DCS ausser deer, déi probéiert gouf.

## Net gelies {#not-read}

- **Gebaier als Formen** (d'Modeller sinn `.edm` an `Models/`): nëmmen Këschten,
  mat Absicht. Hiert Layout, an dat vun der Szen, steet an
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); all installéiert
  Theater liest sech (zwee eeler Theatere an enger Variant vum Layout, déi de Reader
  och kennt).
- Beem, Luuchten an déi aner Objete vun der Szen: gelies, net gezeechent.
- **D'Stroossennetz als Graph** (`roads/*.rn4`): net dekodéiert.
- Texturen, Beem, d'Wellen vum Mier, déi méi niddreg Detailstufe vum Terrain selwer.
