---
title: "Kako se datoteke berejo"
nav_order: 7
lang: "sl"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kako se datoteke berejo {#how-the-files-are-read}

Berejo se samo `Mods/terrains/<teater>/surface/*.surface5` (mreža tal),
`Scenes/*.scn5` (kje objekti stojijo in škatla vsakega modela),
`AirfieldsTaxiways/*.rn4` in `map/towns.lua` (imena krajev, prebrana kot besedilo,
nikoli zagnana). Ne šifrirane datoteke `terrain.cfg.lua.pak.crypt`, ne `manifest.bin`, ne nič iz programa.

Format `.surface5` ni dokumentiran; zgradba, kot je prebrana iz datotek, je zapisana v
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Na kratko: kazalo zapisov ploščic (preoblikovanje, meje in seznami tipiziranih bajtnih tokov, vsak
seznam, za katerim sledi senčilnik in material, s katerima se riše), nato surovi podatki. Ni stisnjen
in ni šifriran. Tok `Pbase` ploščice nosi njene točke; skupina, narisana kot `Land`, nosi trikotnike
in `TRITYPE` na trikotnik, katerega najnižji bit označuje morje; druge skupine so prekrivne plasti, ki
dajo zgoraj navedene razrede.

## Preverjeno {#verified}

- `list` je prebral kazalo vsakega nameščenega teatra (od milijonov do deset milijonov točk tal vsak),
  vsaka vzorčena ploščica se je dekodirala v verjetne metre.
- Na območjih dveh teatrov so mesta iz `towns.lua` pristala v metrih od točke tal, na kopnem, N od N;
  najvišja tla so se ujemala z dejanskim vrhom znotraj desetih metrov; letališča, reke, vasi in ceste so
  se pokazale v svojih razredih. Obe ravni sta se naložili v pregledovalniku, oznake mest v istih metrih
  DCS pa so sedele na tleh.
- Na območju prizora so postavitve stavb pristale na svojih tleh; lučke na stezi so sledile stezi igre,
  vagoni in odseki zidov pa so se poravnali z dekodirano smerjo - vsi.
- `tests/` zgradi datoteke `.surface5` po isti zgradbi, zato tukaj ni ohranjen noben podatek igre;
  `tests/test_real_install.py` teče na namestitvi računalnika, na katerem tečejo testi, in je preskočen,
  če je ni.

**Ni preverjeno:** celoten velik teater v eni ravni (zaščita pred velikostjo zgoraj obstaja z razlogom)
in različice DCS, razen tiste, ki je bila preizkušena.

## Ni prebrano {#not-read}

- **Stavbe kot oblike** (modeli so `.edm` v `Models/`): samo škatle, namenoma. Njihova zgradba in zgradba
  prizora je zapisana v [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  vsak nameščen teater se prebere (dva starejša teatra v različici zgradbe, ki jo bralnik prav tako pozna).
- Drevesa, luči in drugi objekti prizora: prebrani, ne narisani.
- **Cestno omrežje kot graf** (`roads/*.rn4`): ni dekodirano.
- Teksture, drevesa, valovi morja, nižje stopnje podrobnosti terena.
