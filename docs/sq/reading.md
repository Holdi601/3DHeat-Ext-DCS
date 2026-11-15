---
title: "Si lexohen skedarët"
nav_order: 7
lang: sq
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Si lexohen skedarët {#how-the-files-are-read}

Vetëm `Mods/terrains/<theatre>/surface/*.surface5` (rrjeti i tokës),
`Scenes/*.scn5` (ku qëndrojnë objektet, dhe kutia e çdo modeli),
`AirfieldsTaxiways/*.rn4` dhe `map/towns.lua` (emrat e vendeve, lexuar si tekst,
kurrë i ekzekutuar). Jo
`terrain.cfg.lua.pak.crypt` e enkriptuar, jo `manifest.bin`, asgjë nga programi.

Formati `.surface5` nuk është i dokumentuar; skema, siç u lexua nga skedarët,
është shënuar te [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Shkurt: një indeks regjistrash pllakash (një transformim, kufij, dhe lista rrjedhash
bajtesh të tipizuara, secila listë e ndjekur nga shader-i dhe materiali me të cilin
vizatohet), pastaj të dhënat e papërpunuara. Nuk është as i ngjeshur, as i enkriptuar. Rrjedha
`Pbase` e pllakës mban kulmet e saj; grupi i vizatuar si `Land` mban
trekëndëshat dhe një `TRITYPE` për trekëndësh, bit-i më i ulët i të cilit shënon detin; grupet e
tjera janë mbivendosjet që japin klasat e mësipërme.

## Çfarë u verifikua {#verified}

- `list` lexoi indeksin e çdo teatri të instaluar (nga miliona në dhjetëra
  milionë kulme toke secili), çdo pllakë e mostruar dekodohej në metra të
  besueshëm.
- Në rajone të dy teatrove, qytetet nga `towns.lua` ranë brenda metrash
  nga një kulm toke, mbi tokë, N of N; toka më e lartë përputhej me majën
  e vërtetë brenda dhjetë metrash; aeroportet, lumenjtë, fshatrat dhe rrugët shfaqeshin në
  klasat e tyre. Të dy nivelet u ngarkuan në shikues, me shënuesit e qyteteve në të
  njëjtat metra DCS të ulur mbi tokë.
- Në një rajon skene, vendosjet e ndërtesave ranë mbi tokën e tyre; dritat e pistës
  ndoqën pistën e lojës, dhe vagonët e segmentet e mureve përputheshin me
  drejtimin e dekoduar, të gjithë.
- `tests/` ndërton skedarë `.surface5` me të njëjtën skemë, kështu që këtu nuk mbahen
  të dhëna loje; `tests/test_real_install.py` ekzekutohet mbi instalimin e kompjuterit
  që i ekzekuton testet, dhe anashkalohet pa të.

**Nuk u kontrollua:** një teatër i madh i tërë në një nivel të vetëm (mbrojtja e
madhësisë më sipër ekziston për një arsye), dhe versione të DCS të ndryshme nga ai i provuar.

## Çfarë nuk lexohet {#not-read}

- **Ndërtesat si forma** (modelet janë `.edm` në `Models/`): vetëm kuti,
  me qëllim. Skema e tyre, dhe ajo e skenës, është shënuar te
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); çdo teatër
  i instaluar lexohet (dy teatro më të vjetër me një skemë variante që e njeh edhe lexuesi).
- Pemët, dritat dhe objektet e tjera të skenës: lexohen, nuk vizatohen.
- **Rrjeti rrugor si graf** (`roads/*.rn4`): nuk dekodohet.
- Teksturat, pemët, valët e detit, nivelet e ulëta të detajeve të vetë terrenit.
