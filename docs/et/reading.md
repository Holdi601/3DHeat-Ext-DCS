---
title: "Kuidas faile loetakse"
nav_order: 7
lang: "et"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kuidas faile loetakse {#how-the-files-are-read}

Loetakse ainult `Mods/terrains/<theatre>/surface/*.surface5` (maapinna võrk),
`Scenes/*.scn5` (kus objektid seisavad ja iga mudeli kast),
`AirfieldsTaxiways/*.rn4` ja `map/towns.lua` (kohanimed, loetud tekstina,
mitte käivitatuna). Mitte krüpteeritud
`terrain.cfg.lua.pak.crypt`, mitte `manifest.bin`, mitte midagi programmist.

`.surface5` vorming ei ole dokumenteeritud; paigutus, nagu see failidest loetakse, on kirjas
failis [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Lühidalt: kahhelkirjete indeks (teisendus, piirid ja tüübitud baidivoogude loendid, iga loendile
järgneb varjundaja ja materjal, millega seda joonistatakse), seejärel toorandmed. See ei ole
tihendatud ega krüpteeritud. Kahheli `Pbase` voog hoiab selle tippe; rühm, mida joonistatakse
kui `Land`, hoiab kolmnurki ja iga kolmnurga `TRITYPE`, mille madalaim bitt märgib mere; teised
rühmad on kattekihid, mis annavad ülal olevad klassid.

## Kontrollitud {#verified}

- `list` luges iga paigaldatud teatri indeksi (miljonid kuni kümneid miljoneid maapinna tippe kummaski), iga proovitud kahhel dekodeeritud mõistlikeks meetriteks.
- Kahe teatri piirkondades maandusid `towns.lua` linnad meetri piires maapinna tipust, maal, N of N; kõrgeim maa klappis tegeliku tipuga kümne meetri piires; lennuväljad, jõed, külad ja teed ilmusid oma klassides. Mõlemad tasemed laadisid vaatajasse, linnamärgid samades DCS-i meetrites maapinnal.
- Stseeni piirkonnas maandusid hoonete paigutused oma maapinnale; lennurajatuled jälgisid mängu lennurada ning vagunid ja müürilõigud joondusid dekodeeritud suunaga, kõik.
- `tests/` koostab `.surface5` failid samasse paigutusse, nii et mängu andmeid siin ei hoita; `tests/test_real_install.py` töötab teste käivitava masina installil ja jäetakse ilma selleta vahele.

**Kontrollimata:** suure teatri tervik ühel tasemel (ülal olev suuruse kaitse on selle jaoks olemas) ja DCS-i versioonid peale selle, mida prooviti.

## Ei loeta {#not-read}

- **Hooned kujunditena** (mudelid on `.edm` failid kaustas `Models/`): ainult kastid, meelega. Nende paigutus ja stseeni oma on kirjas failis
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); iga paigaldatud teater loetakse (kaks vanemat teatrit variantpaigutuses, mida lugeja samuti tunneb).
- Puud, tuled ja stseeni teised objektid: loetud, mitte joonistatud.
- **Teedevõrk graafina** (`roads/*.rn4`): ei ole dekodeeritud.
- Tekstuurid, puud, mere lained, maastiku oma madalamad detailitasemed.
