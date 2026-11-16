---
title: "Condiții și licență"
nav_order: 8
lang: "ro"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Condiții și licență {#terms-and-licence}

## Ce citește cititorul {#what-the-reader-reads}

Cititorul citește fișiere de date din propria dumneavoastră instalare DCS World, de pe calculatorul dumneavoastră ([Cum se citesc fișierele](reading.md)). Nu schimbă nimic în joc și nu comunică cu niciun server.

Nimic din joc nu este livrat sau redistribuit: niciun fișier al jocului, niciun cod al jocului, niciun DLL; testele construiesc singure fiecare fișier pe care îl citesc. Nivelurile pe care le scrie rămân pe calculatorul dumneavoastră.

3DHeat DCS nu este afiliat cu Eagle Dynamics și nu este aprobat de aceasta. DCS World și numele și mărcile asociate aparțin proprietarilor lor.

Deținători de drepturi: deschideți un tichet la [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - răspundem repede și eliminăm orice la cerere.

## Licență și surse {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Are nevoie de numpy (BSD-3-Clause); `fit` pe un
`.parquet` are nevoie de pyarrow (Apache-2.0). Scris pentru acest proiect. Constantele de proiecție sunt
fapte publicate de pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); s-au luat doar
numerele. Proiecția este seria lui Krüger, așa cum o dă C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers”, Journal of Geodesy 85, 2011). Niciun cod nu a
fost luat din alt proiect.
