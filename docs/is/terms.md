---
title: "Skilmálar og leyfi"
nav_order: 8
lang: "is"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Skilmálar og leyfi {#terms-and-licence}

## Hvað lesarinn les {#what-the-reader-reads}

Lesarinn les gagnaskrár úr þinni eigin uppsetningu á DCS World á tölvunni þinni ([Hvernig skrárnar eru lesnar](reading.md)). Hann breytir engu í leiknum og talar ekki við neinn netþjón.

Ekkert úr leiknum fylgir með eða er dreift áfram: engar leikjaskrár, enginn leikjakóði, engin DLL-söfn; prófanirnar búa sjálfar til hverja skrá sem þær lesa. Borðin sem það skrifar verða eftir á tölvunni þinni.

3DHeat DCS tengist ekki Eagle Dynamics og er ekki stutt af þeim. DCS World og tengd heiti og vörumerki tilheyra eigendum sínum.

Rétthafar: stofnið verkbeiðni á [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - við svörum fljótt og fjarlægjum hvað sem er að beiðni.

## Leyfi og heimildir {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Þarf numpy (BSD-3-Clause); `fit` á
`.parquet` þarf pyarrow (Apache-2.0). Skrifað fyrir þetta verkefni. Fastar
vörpunarinnar eru staðreyndir birtar af pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); aðeins tölurnar
voru teknar. Vörpunin er Krüger-röð eins og C. F. F. Karney gefur hana
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Enginn kóði var tekinn úr neinu öðru verkefni.
