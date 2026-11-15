---
title: Kif jinqraw il-fajls
nav_order: 7
lang: "mt"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kif jinqraw il-fajls {#how-the-files-are-read}

Biss `Mods/terrains/<theatre>/surface/*.surface5` (il-mesh tal-art),
`Scenes/*.scn5` (fejn joqgħodu l-oġġetti, u l-kaxxa ta' kull mudell),
`AirfieldsTaxiways/*.rn4` u `map/towns.lua` (ismijiet tal-postijiet, moqrija bħala test,
qatt ma jitħaddmu). Mhux il-`terrain.cfg.lua.pak.crypt`
ikkriptat, mhux `manifest.bin`, xejn mill-programm.

Il-format `.surface5` mhuwiex dokumentat; il-layout, kif moqri mill-fajls,
huwa miktub f'[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Fil-qosor: indiċi ta' records tat-tiles (trasformazzjoni, limiti, u listi ta'
byte streams tipizzati, kull lista segwita mill-shader u l-materjal li bih jitpinġu),
imbagħad id-dejta raw. Mhuwiex ikkompressat u lanqas ikkriptat. L-istream
`Pbase` tat-tile iżomm il-vertiċi tiegħu; il-grupp imfassal bħala `Land` iżomm
it-trijangoli u `TRITYPE` għal kull trijangolu, li l-bit l-iżgħar tiegħu jimmarka l-baħar; il-gruppi
l-oħra huma l-overlays li jagħtu l-klassijiet ta' hawn fuq.

## Ivverifikat {#verified}

- `list` qara l-indiċi ta' kull teatru installat (miljuni sa għexieren
  ta' miljuni ta' vertiċi tal-art kull wieħed), kull tile kampjun jiddekodifika
  f'metri plawżibbli.
- Fuq reġjuni ta' żewġ teatri, l-irħula minn `towns.lua` waqgħu fi metri
  minn vertiċi tal-art, fuq l-art, N of N; l-ogħla art qabbel is-summit
  vera sa għaxar metri; ajrudromi, xmajjar, rħula u toroq dehru fil-
  klassijiet tagħhom. Iż-żewġ livelli tgħabbew fil-viewer, b'markaturi tal-irħula fl-
  istess metri ta' DCS bilqiegħda fuq l-art.
- Fuq reġjun tax-xena, it-tqegħid tal-bini waqa' fuq l-art tiegħu; dwal
  tar-runway traċċaw ir-runway tal-logħba, u vagons u segmenti tal-ħitan ġew f'linja mad-
  direzzjoni ddekodifikata, kollha.
- `tests/` jibni fajls `.surface5` bl-istess layout, għalhekk ebda dejta tal-logħba
  ma tinżamm hawn; `tests/test_real_install.py` jaħdem fuq l-installazzjoni tal-magna
  li tħaddem it-testijiet, u jitqabbeż mingħajrha.

**Mhux ikkontrollat:** it-teatru kbir kollu f'livell wieħed (il-protezzjoni tad-daqs
ta' hawn fuq teżisti għal raġuni), u verżjonijiet ta' DCS differenti minn dik ittestjata.

## Ma jinqarax {#not-read}

- **Bini bħala forom** (il-mudelli huma `.edm` f'`Models/`): kaxxi biss,
  apposta. Il-layout tagħhom, u tax-xena, huwa miktub f'
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); kull teatru
  installat jinqara (żewġ teatri eqdem f'layout varjant li l-qarrej jaf
  ukoll).
- Siġar, dwal u l-oġġetti l-oħra tax-xena: moqrija, mhux imfassla.
- **In-netwerk tat-toroq bħala graff** (`roads/*.rn4`): mhux iddekodifikat.
- Texturi, siġar, mewġ tal-baħar, il-livelli aktar baxxi ta' dettall tat-terren.
