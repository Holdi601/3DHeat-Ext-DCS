---
title: Kako se datoteke čitaju
nav_order: 7
lang: hr
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kako se datoteke čitaju {#how-the-files-are-read}

Čitaju se samo `Mods/terrains/<theatre>/surface/*.surface5` (mreža tla), `Scenes/*.scn5` (gdje objekti stoje i okviri svakog modela), `AirfieldsTaxiways/*.rn4` i `map/towns.lua` (nazivi mjesta, čitani kao tekst, nikad se ne izvršavaju). Ne čita se šifrirana `terrain.cfg.lua.pak.crypt`, ne `manifest.bin`, ništa iz samog programa.

Format `.surface5` nije dokumentiran; raspored, kako je pročitan iz datoteka, zapisan je u [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Ukratko: indeks zapisa pločica (transformacija, granice i popisi tipiziranih nizova bajtova, svaki popis slijedi shader i materijal kojim se crta), zatim sirovi podaci. Nije ni komprimiran ni šifriran. Niz `Pbase` pločice sadrži njezine vrhove; grupa koja se crta kao `Land` sadrži trokute i `TRITYPE` po trokutu, čiji najniži bit označava more; ostale grupe su slojevi koji daju gore navedene klase.

## Provjereno {#verified}

- `list` je pročitao indeks svake instalirane karte (od milijuna do desetaka milijuna vrhova tla svaka), a svaka uzorkovana pločica dekodirala se u vjerojatne metre.
- Na regijama dviju karata gradovi iz `towns.lua` pali su unutar metara od vrha tla, na kopnu, N od N; najviše tlo se podudaralo sa stvarnim vrhom unutar deset metara; zračne luke, rijeke, sela i ceste pokazale su se u svojim klasama. Obje razine su se učitale u preglednik, s oznakama gradova u istim DCS metrima koje sjede na tlu.
- Na regiji scene, postavljanja zgrada pala su na svoje tlo; svjetla piste prate pistu igre, a vagoni i segmenti zidova poredali su se prema dekodiranom smjeru, svi do jednog.
- `tests/` gradi `.surface5` datoteke po istom rasporedu, pa se ovdje ne čuva nikakav podatak igre; `tests/test_real_install.py` se pokreće na instalaciji računala na kojem se testovi izvode i preskače se bez nje.

**Nije provjereno:** cijela velika karta u jednoj razini (zaštita veličine iznad postoji iz razloga), i verzije DCS-a osim one koja je isprobana.

## Nije pročitano {#not-read}

- **Zgrade kao oblici** (modeli su `.edm` u `Models/`): samo kvadri, namjerno. Njihov raspored, kao i rasporeda scene, zapisan je u [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); čita ga svaka instalirana karta (dvije starije karte u varijantnom rasporedu koji čitač također poznaje).
- Drveće, svjetla i ostali objekti scene: pročitani, ali ne crtaju se.
- **Cestovna mreža kao graf** (`roads/*.rn4`): nije dekodirana.
- Teksture, drveće, valovi mora, niže razine detalja samog terena.
