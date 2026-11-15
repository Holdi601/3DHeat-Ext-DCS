---
title: "Kako se datoteke čitaju"
nav_order: 7
lang: bs
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kako se datoteke čitaju {#how-the-files-are-read}

Samo `Mods/terrains/<theatre>/surface/*.surface5` (mreža tla),
`Scenes/*.scn5` (gdje objekti stoje i okvir svakog modela),
`AirfieldsTaxiways/*.rn4` i `map/towns.lua` (nazivi mjesta, čitaju se kao tekst,
nikad ne izvršavaju). Ne šifrirani
`terrain.cfg.lua.pak.crypt`, ne `manifest.bin`, ništa od programa.

Format `.surface5` nije dokumentiran; raspored, kako je pročitan iz datoteka,
zapisan je u [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Ukratko: indeks zapisa pločica (transformacija, granice i liste tipiziranih
tokova bajtova, svaka lista praćena shaderom i materijalom kojim se
crta), zatim sirovi podaci. Nije ni komprimiran ni šifriran. Tok
`Pbase` pločice drži njene vrhove; grupa crtana kao `Land` drži
trouglove i `TRITYPE` po trouglu, čiji najniži bit označava more; ostale
grupe su preklopi koji daju gornje klase.

## Provjereno {#verified}

- `list` je pročitao indeks svakog instaliranog teatra (od milion do desetaka
  miliona vrhova tla svaki), a svaka uzorkovana pločica dekodira se u prihvatljive
  metre.
- Na regijama dva teatra, gradovi iz `towns.lua` pali su unutar nekoliko metara
  od vrha tla, na kopno, N od N; najviše tlo poklopilo se sa stvarnim
  vrhom unutar deset metara; aerodromi, rijeke, sela i ceste vidjeli su se u
  svojim klasama. Oba nivoa su se učitala u pregledniku, s oznakama gradova u istim
  DCS metrima koje stoje na tlu.
- Na regiji scene, postavljanja zgrada pala su na svoje tlo; svjetla piste
  pratila su pistu igre, a vagoni i segmenti zidova poravnali su se s
  dekodiranim smjerom, svi.
- `tests/` gradi `.surface5` datoteke po istom rasporedu, pa se ovdje ne drže
  podaci igre; `tests/test_real_install.py` radi na instalaciji računara koji
  izvodi testove, a preskače se bez nje.

**Nije provjereno:** cijeli veliki teatar u jednom nivou (zaštita veličine
gore postoji s razlogom) i verzije DCS-a osim one koja je isprobana.

## Ne čita se {#not-read}

- **Zgrade kao oblici** (modeli su `.edm` u `Models/`): samo kutije,
  namjerno. Njihov raspored, i raspored scene, zapisan je u
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); svaki instalirani
  teatar se čita (dva starija teatra u varijantnom rasporedu koji čitač također
  poznaje).
- Drveće, svjetla i ostali objekti scene: čitaju se, ne crtaju.
- **Cestovna mreža kao graf** (`roads/*.rn4`): nije dekodirana.
- Teksture, drveće, valovi mora, vlastiti niži nivoi detalja terena.
