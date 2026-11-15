---
title: Sådan læses filerne
nav_order: 7
lang: da
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Sådan læses filerne {#how-the-files-are-read}

Kun `Mods/terrains/<theatre>/surface/*.surface5` (jordnettet),
`Scenes/*.scn5` (hvor objekter står, og hver models kasse),
`AirfieldsTaxiways/*.rn4` og `map/towns.lua` (stednavne, læst som tekst,
aldrig kørt). Ikke den krypterede
`terrain.cfg.lua.pak.crypt`, ikke `manifest.bin`, intet af programmet.

`.surface5`-formatet er ikke dokumenteret; layoutet, som det er læst fra
filerne, er nedskrevet i [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kort fortalt: et indeks af flisepost (en transformation, grænser og lister af typede
bytestrømme, hver liste efterfulgt af den shader og det materiale, den tegnes
med), derefter de rå data. Det er hverken komprimeret eller krypteret. Flisens
`Pbase`-strøm holder dens hjørnepunkter; gruppen tegnet som `Land` holder
trekanterne og en `TRITYPE` pr. trekant, hvis laveste bit markerer havet; de
andre grupper er overlays, der giver klasserne ovenfor.

## Verificeret {#verified}

- `list` læste indekset for hvert installeret teater (millioner til titalsmillioner
  jordhjørnepunkter hver), hver stikprøvet flise afkodet til plausible meter.
- På områder i to teatre landede byerne fra `towns.lua` inden for meter
  fra en jordhjørnepunkt, på land, N af N; den højeste jord passede med den rigtige
  top inden for ti meter; flyvepladser, floder, landsbyer og veje viste sig
  i deres klasser. Begge baner blev indlæst i vieweren, med bymarkører i
  de samme DCS-meter, siddende på jorden.
- På et scene-område landede bygningsplaceringerne på deres jord; banelys fulgte
  spillets start- og landingsbane, og vogne og muresegmenter flugtede med den
  afkodede retning, alle sammen.
- `tests/` bygger `.surface5`-filer i det samme layout, så der gemmes ingen spildata her;
  `tests/test_real_install.py` kører på installationen på den maskine, der kører testene,
  og springes over uden en.

**Ikke kontrolleret:** hele et stort teater i én bane (størrelsesvagten
ovenfor findes af en grund), og andre versioner af DCS end den, der blev testet.

## Ikke læst {#not-read}

- **Bygninger som former** (modellerne er `.edm` i `Models/`): kun kasser,
  med vilje. Deres layout, og scenens, er nedskrevet i
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); hvert installerede
  teater læses (to ældre teatre i en variant-layout, som læseren også kender).
- Træer, lys og de andre objekter i scenen: læst, ikke tegnet.
- **Vejnettet som graf** (`roads/*.rn4`): ikke afkodet.
- Teksturer, træer, havets bølger, terrænets egne lavere detaljeniveauer.
