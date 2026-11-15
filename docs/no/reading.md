---
title: Slik leses filene
nav_order: 7
lang: no
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Slik leses filene {#how-the-files-are-read}

Bare `Mods/terrains/<theatre>/surface/*.surface5` (bakkenettet),
`Scenes/*.scn5` (der objekter står, og hver modells boks),
`AirfieldsTaxiways/*.rn4` og `map/towns.lua` (stedsnavn, lest som tekst,
aldri kjørt). Ikke den krypterte
`terrain.cfg.lua.pak.crypt`, ikke `manifest.bin`, ingenting av programmet.

`.surface5`-formatet er ikke dokumentert; oppsettet, slik det er lest fra
filene, er skrevet ned i [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kort sagt: en indeks av flisposter (en transformasjon, grenser, og lister av typede
bytestrømmer, hver liste etterfulgt av shaderen og materialet den tegnes med),
deretter de rå dataene. Det er verken komprimert eller kryptert. Flisens
`Pbase`-strøm holder dens toppunkter; gruppen som tegnes som `Land` holder
trekantene og en `TRITYPE` per trekant, der den laveste biten markerer havet; de
andre gruppene er overleggene som gir klassene over.

## Kontrollert {#verified}

- `list` leste indeksen til hvert installert teater (millioner til titalls millioner
  bakketoppunkter hver), og hver stikkprøvet flis dekodet til plausible
  meter.
- På regioner av to teatre landet byene fra `towns.lua` innen meter
  fra et bakketoppunkt, på land, N av N; den høyeste bakken traff den virkelige
  toppen innen ti meter; flyplasser, elver, landsbyer og veier viste seg i
  sine klasser. Begge nivåene lastet i visningsprogrammet, med bymarkører i de
  samme DCS-meterne som sitter på bakken.
- På en scene-region landet bygningsplasseringene på sin bakke; rullebanelys
  fulgte spillets rullebane, og vogner og murseksjoner stemte overens med den
  dekodede retningen, alle sammen.
- `tests/` bygger `.surface5`-filer i samme oppsett, så ingen spilldata
  lagres her; `tests/test_real_install.py` kjører på installasjonen på maskinen
  som kjører testene, og hoppes over uten en.

**Ikke kontrollert:** et helt stort teater i ett nivå (størrelsesvakten
over finnes av en grunn), og versjoner av DCS annet enn den som ble prøvd.

## Ikke lest {#not-read}

- **Bygninger som former** (modellene er `.edm` i `Models/`): bare bokser,
  med vilje. Deres oppsett, og scenens, er skrevet ned i
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); hvert installerte
  teater leses (to eldre teatre i et variantoppsett som leseren også kjenner).
- Trær, lys og de andre objektene i scenen: lest, ikke tegnet.
- **Veinettet som graf** (`roads/*.rn4`): ikke dekodet.
- Teksturer, trær, havets bølger, terrengets egne lavere detaljnivåer.
