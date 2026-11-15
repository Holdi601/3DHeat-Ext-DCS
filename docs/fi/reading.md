---
title: "Miten tiedostot luetaan"
nav_order: 7
lang: "fi"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Miten tiedostot luetaan {#how-the-files-are-read}

Luetaan vain `Mods/terrains/<theatre>/surface/*.surface5` (maaston verkko),
`Scenes/*.scn5` (missä kohteet seisovat ja jokaisen mallin laatikko),
`AirfieldsTaxiways/*.rn4` ja `map/towns.lua` (paikannimet, luettuna tekstinä,
ei koskaan suoritettuna). Ei salattua
`terrain.cfg.lua.pak.crypt`-tiedostoa, ei `manifest.bin`-tiedostoa, eikä mitään ohjelman
osaa.

`.surface5`-muoto ei ole dokumentoitu; asettelu, sellaisena kuin se luettiin tiedostoista,
on kirjoitettu muistiin tiedostoon [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Lyhyesti: laatikkotietueiden hakemisto (muunnos, rajat ja tyypitettyjen tavuvirtojen listat, joista
jokaisen perässä on varjostin ja materiaali, jolla se piirretään), sitten raakadata. Se ei ole pakattu
eikä salattu. Laatan `Pbase`-virta kantaa sen kärjet; `Land`-nimellä piirretty ryhmä kantaa kolmiot ja
jokaiselle kolmiolle `TRITYPE`-arvon, jonka alin bitti merkitsee meren; muut ryhmät ovat edellä mainitut
luokat antavat peittokuvat.

## Todennettu {#verified}

- `list` luki jokaisen asennetun teatterin hakemiston (miljoonista kymmeniin miljooniin maaston kärkiin
  teatteria kohden), ja jokainen tarkistettu laatta dekoodautui uskottaviksi metreiksi.
- Kahden teatterin alueilla `towns.lua`:n kaupungit osuivat metrien päähän maakärjestä, maalla, N of N;
  korkein maasto osui todelliseen huippuun kymmenen metrin tarkkuudella; lentokentät, joet, kylät ja tiet
  näkyivät luokissaan. Molemmat kentät latautuivat katselimeen, ja kaupunkimerkit samoissa DCS-metreissä
  istuivat maassa.
- Maisemalueella rakennussijoitukset osuivat maahansa; kiitotievalot seurasivat pelin kiitorataa, ja vaunut
  ja seinäosat asettuivat luetun suunnan mukaan, kaikki.
- `tests/` rakentaa `.surface5`-tiedostoja samaan asetteluun, joten pelin dataa ei säilytetä täällä;
  `tests/test_real_install.py` ajaa testikoneen asennuksella, ja se ohitetaan ilman sitä.

**Ei tarkistettu:** koko suurta teatteria yhdessä kentässä (koon suoja yllä on olemassa syystä), ja
muut DCS-versiot kuin kokeiltu.

## Ei luettu {#not-read}

- **Rakennukset muotoina** (mallit ovat `.edm`-tiedostoja kansiossa `Models/`): vain laatikot, tarkoituksella.
  Niiden asettelu ja maiseman asettelu on kirjoitettu muistiin tiedostoon
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  jokainen asennettu teatteri luetaan (kaksi vanhempaa teatteria muunnelmalla, jonka lukija myös tuntee).
- Puut, valot ja muut maiseman kohteet: luetaan, ei piirretä.
- **Tieverkko graafina** (`roads/*.rn4`): ei dekoodattu.
- Tekstuurit, puut, meren aallot, maaston alemmat yksityiskohtaisuustasot.
