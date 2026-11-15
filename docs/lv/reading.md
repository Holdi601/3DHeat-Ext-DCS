---
title: Kā tiek nolasīti faili
nav_order: 7
lang: "lv"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Kā tiek nolasīti faili {#how-the-files-are-read}

Tiek lasīti tikai `Mods/terrains/<theatre>/surface/*.surface5` (zemes tīkls),
`Scenes/*.scn5` (kur stāv objekti un katra modeļa kaste), `AirfieldsTaxiways/*.rn4` un
`map/towns.lua` (vietu nosaukumi, lasīti kā teksts, nekad nepalaisti). Ne šifrētais
`terrain.cfg.lua.pak.crypt`, ne `manifest.bin`, nekas no programmas.

`.surface5` formāts nav dokumentēts; izkārtojums, kā tas nolasīts no failiem, ir uzrakstīts
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Īsumā: flīzes ierakstu rādītājs (transformācija, robežas un tipizētu baitu straumju saraksti, katrs saraksts seko
ēnotājam un materiālam, ar kādu tas tiek zīmēts), tad neapstrādātie dati. Tas nav ne saspiests, ne šifrēts. Flīzes
`Pbase` straumē ir tās virsotnes; grupā, kas tiek zīmēta kā `Land`, ir trijstūri un `TRITYPE` katram trijstūrim, kura
zemākais bits atzīmē jūru; pārējās grupas ir pārklājumi, kas dod iepriekš minētās klases.

## Pārbaudīts {#verified}

- `list` nolasīja katra uzstādītā teātra rādītāju (miljoni līdz desmiti miljonu zemes virsotņu katrā), un katra paraugā ņemtā flīze atkodējās par ticamiem metriem.
- Diviem teātru reģioniem pilsētas no `towns.lua` nokrita dažu metru attālumā no zemes virsotnes, uz sauszemes, N no N; augstākā zeme sakrita ar īsto virsotni desmit metru robežās; lidlauki, upes, ciemi un ceļi parādījās savās klasēs. Abi līmeņi ielādējās skatītājā, ar pilsētu marķieriem tajos pašos DCS metros, kas atrodas uz zemes.
- Uz skatuves reģiona ēku novietojumi nokrita uz savas zemes; skrejceļa gaismas izsekoja spēles skrejceļam, un vagoni un sienu segmenti sakrita ar atkodēto virzienu - visi.
- `tests/` veido `.surface5` failus tādā pašā izkārtojumā, tāpēc šeit nav glabāti spēles dati; `tests/test_real_install.py` darbojas uz uzstādījuma mašīnā, kur tiek palaisti testi, un tiek izlaists, ja tāda nav.

**Nav pārbaudīts:** viss liels teātris vienā līmenī (iepriekš minētā izmēra aizsardzība pastāv ar iemeslu) un citas DCS versijas, nevis tā, kas tika izmēģināta.

## Nav nolasīts {#not-read}

- **Ēkas kā formas** (modeļi ir `.edm` failos `Models/`): tikai kastes, apzināti. To izkārtojums un skatuves izkārtojums ir uzrakstīts [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); katrs uzstādītais teātris tiek nolasīts (divi vecāki teātri vienā variantā izkārtojumā, ko lasītājs arī zina).
- Koki, gaismas un pārējie skatuves objekti: nolasīti, bet nezīmēti.
- **Ceļu tīkls kā grafs** (`roads/*.rn4`): nav dekodēts.
- Tekstūras, koki, jūras viļņi, reljefa zemākie detalizācijas līmeņi.
