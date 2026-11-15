---
title: "Kaip skaitomi failai"
nav_order: 7
lang: lt
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kaip skaitomi failai {#how-the-files-are-read}

Skaitomi tik `Mods/terrains/<theatre>/surface/*.surface5` (reljefo tinklas), `Scenes/*.scn5` (kur stovi objektai ir kiekvieno modelio
dėžutė), `AirfieldsTaxiways/*.rn4` ir `map/towns.lua` (vietovardžiai, skaitomi kaip tekstas, niekada nevykdomi).
Neskaitomas užšifruotas `terrain.cfg.lua.pak.crypt`, nei `manifest.bin`, nei kas nors iš programos.

`.surface5` formatas nedokumentuotas; išdėstymas, perskaitytas iš failų, aprašytas
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Trumpai: plytelių įrašų indeksas (transformacija, ribos ir tipizuotų baitų srautų sąrašai, kiekvienas sąrašas
seka shader ir medžiagą, kuria jis piešiamas), o tada neapdoroti duomenys. Jis nei suspaustas, nei užšifruotas. Plytelės
`Pbase` srautas laiko jos viršūnes; grupė, piešiama kaip `Land`, laiko trikampius ir `TRITYPE` kiekvienam trikampiui, kurio
mažiausias bitas žymi jūrą; kitos grupės yra perdangos, kurios suteikia aukščiau nurodytas klases.

## Patikrinta {#verified}

- `list` perskaitė kiekvieno įdiegto teatro indeksą (kiekvienas – nuo milijonų iki dešimčių milijonų reljefo viršūnių),
  kiekviena pavyzdinė plytelė iškoduota į tikėtinus metrus.
- Dviejų teatrų regionuose miestai iš `towns.lua` atsidūrė per kelis metrus nuo reljefo viršūnės, sausumoje, N iš N;
  aukščiausias reljefas sutapo su tikra viršūne iki dešimties metrų; oro uostai, upės, kaimai ir keliai atsirado savo klasėse.
  Abu lygiai buvo įkelti žiūryklėje, o miestų žymekliai tose pačiose DCS metrų vietose stovėjo ant žemės.
- Scenos regione pastatų vietos atsidūrė ant savo žemės; kilimo tako šviesos atkartojo žaidimo kilimo taką, o vagonai ir sienų
  atkarpos sulygiavo su iškoduota kryptimi – visi.
- `tests/` sukuria `.surface5` failus tokiu pačiu išdėstymu, todėl žaidimo duomenys čia nelaikomi; `tests/test_real_install.py`
  veikia ant įdiegimo kompiuteryje, kuriame vykdomi testai, ir praleidžiamas, jei jo nėra.

**Nepatikrinta:** visas didelis teatras viename lygyje (aukščiau minėtas dydžio apribojimas egzistuoja ne be priežasties)
ir DCS versijos, kitos nei išbandyta.

## Neskaitoma {#not-read}

- **Pastatai kaip formos** (modeliai yra `.edm` faile `Models/`): tik dėžutės, tyčia. Jų išdėstymas ir scenos išdėstymas aprašyti
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); skaitomi visi
  įdiegti teatrai (ir du senesni teatrai kitokiu išdėstymu, kurį skaitytuvas taip pat žino).
- Medžiai, šviesos ir kiti scenos objektai: perskaityti, bet nepiešiami.
- **Kelių tinklas kaip grafas** (`roads/*.rn4`): neiškoduotas.
- Tekstūros, medžiai, jūros bangos, reljefo žemesni detalumo lygiai.
