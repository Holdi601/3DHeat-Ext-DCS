---
title: Conas a léitear na comhaid
nav_order: 7
lang: ga
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Conas a léitear na comhaid {#how-the-files-are-read}

Ní léitear ach `Mods/terrains/<theatre>/surface/*.surface5` (mogall na talún),
`Scenes/*.scn5` (an áit a seasann rudaí, agus bosca gach samhla),
`AirfieldsTaxiways/*.rn4` agus `map/towns.lua` (logainmneacha, léite mar théacs,
gan a rith riamh). Ní léitear an
`terrain.cfg.lua.pak.crypt` criptithe, ná `manifest.bin`, ná aon rud den chlár.

Tá an fhormáid `.surface5` gan doiciméadú; tá an leagan amach, mar a léadh ó na comhaid,
scríofa síos in [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Go hachomair: innéacs de thaifid tíle (claochlú, teorainneacha, agus liostaí de
shruthanna beart clóscríofa, gach liosta á leanúint ag an scáthaitheoir agus an t-ábhar lena dtarraingítear é),
ansin na sonraí amha. Níl sé comhbhrúite ná criptithe. Coinníonn sruth `Pbase` na tíle a rinn;
coinníonn an grúpa a tarraingítear mar `Land` na triantáin agus `TRITYPE` in aghaidh an triantáin,
a mharcálann a ghiotán is ísle an fharraige; is iad na grúpaí eile na forleagain a thugann na haicmí thuas.

## Fíoraithe {#verified}

- Léigh `list` innéacs gach téatair suiteáilte (milliúin go deich milliúin
  rinn talún an ceann), gach tíle samplaithe ag díchódú go méadair inchreidte.
- Ar réigiúin de dhá théatar, thuirling na bailte ó `towns.lua` laistigh de mhéadair
  de rinn talún, ar thalamh, N de N; mheaitseáil an talamh is airde an
  bhuaic fhíor laistigh de dheich méadar; léirigh aerpháirceanna, aibhneacha, sráidbhailte agus bóithre
  ina n-aicmí. Lódáladh an dá leibhéal san amharcán, le marcóirí bailte sna
  méadair DCS chéanna ina suí ar an talamh.
- Ar réigiún radhairc, thuirling na cuir foirgneamh ar a dtalamh; lorg soilse rúidbhealaigh
  rúidbhealach an chluiche, agus rinne vaigíní agus ballphíosaí
  ailíniú leis an treo díchódaithe, iad go léir.
- Tógann `tests/` comhaid `.surface5` leis an leagan amach céanna, mar sin ní choinnítear aon sonraí cluiche
  anseo; ritheann `tests/test_real_install.py` ar shuiteáil an mheaisín
  a ritheann na tástálacha, agus scipeáiltear é gan ceann.

**Gan seiceáil:** an téatar mór ar fad in aon leibhéal amháin (tá an garda méide
thuas ar chúis), agus leaganacha de DCS seachas an ceann a triaileadh.

## Gan léamh {#not-read}

- **Foirgnimh mar chruthanna** (is `.edm` iad na samhlacha i `Models/`): boscaí amháin,
  d'aon ghnó. Tá a leagan amach, agus leagan amach an radhairc, scríofa síos in
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); léitear gach téatar
  suiteáilte (dhá théatar níos sine i leagan amach malartach a bhfuil aithne ag an léitheoir air
  freisin).
- Crainn, soilse agus rudaí eile an radhairc: léite, gan tarraingt.
- **An líonra bóithre mar ghraf** (`roads/*.rn4`): gan díchódú.
- Uigeachtaí, crainn, tonnta na farraige, leibhéil mionsonraí níos ísle an tír-raoin féin.
