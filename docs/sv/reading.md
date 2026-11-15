---
title: Så läses filerna
nav_order: 7
lang: sv
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Så läses filerna {#how-the-files-are-read}

Bara `Mods/terrains/<theatre>/surface/*.surface5` (markens nät),
`Scenes/*.scn5` (var objekt står, och varje modells låda),
`AirfieldsTaxiways/*.rn4` och `map/towns.lua` (ortnamn, läst som text,
aldrig körd). Inte den krypterade `terrain.cfg.lua.pak.crypt`, inte `manifest.bin`, inget av programmet.

`.surface5`-formatet är odokumenterat; layouten, så som den lästs från filerna, är nedskriven i [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kort sagt: ett index av kakelposter (en transform, gränser och listor med typade byteströmmar, var och en följd av shadern och materialet den ritas med), sedan rådatan. Den är varken komprimerad eller krypterad. Kakelns `Pbase`-ström innehåller dess hörn; gruppen som ritas som `Land` innehåller trianglarna och en `TRITYPE` per triangel, vars lägsta bit markerar havet; de andra grupperna är överlagringarna som ger klasserna ovan.

## Kontrollerat {#verified}

- `list` läste indexet för varje installerad teater (miljoner till tiotals miljoner markhörn vardera), och varje stickprovskakel avkodades till rimliga meter.
- På regioner i två teatrar hamnade städerna från `towns.lua` inom meter från ett markhörn, på land, N av N; den högsta marken stämde med den verkliga toppen inom tio meter; flygfält, floder, byar och vägar syntes i sina klasser. Båda nivåerna lästes in i visaren, med stadsmarkörer i samma DCS-meter som satt på marken.
- På en scenregion hamnade byggnadsplaceringarna på sin mark; landningsbanornas lampor följde spelets startbana, och vagnar och murstycken stämde med den avkodade riktningen, alla.
- `tests/` bygger `.surface5`-filer i samma layout, så ingen speldata sparas här; `tests/test_real_install.py` körs på installationen på datorn som kör testerna, och hoppas över utan en.

**Inte kontrollerat:** en hel stor teater i en nivå (storlekskyddet ovan finns av en anledning), och andra versioner av DCS än den som prövats.

## Inte läst {#not-read}

- **Byggnader som former** (modellerna är `.edm` i `Models/`): bara lådor, med avsikt. Deras layout, och scenens, är nedskriven i [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); varje installerad teater läses (två äldre teatrar i en variantlayout som läsaren också känner).
- Träd, lampor och de andra objekten i scenen: lästa, inte ritade.
- **Vägnätet som graf** (`roads/*.rn4`): inte avkodat.
- Texturer, träd, havets vågor, terrängens egna lägre detaljnivåer.
