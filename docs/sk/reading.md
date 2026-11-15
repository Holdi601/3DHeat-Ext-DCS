---
title: "Ako sa čítajú súbory"
nav_order: 7
lang: "sk"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Ako sa čítajú súbory {#how-the-files-are-read}

Číta sa len `Mods/terrains/<theatre>/surface/*.surface5` (sieť zeme),
`Scenes/*.scn5` (kde objekty stoja a škatuľa každého modelu),
`AirfieldsTaxiways/*.rn4` a `map/towns.lua` (názvy miest, čítané ako text,
nikdy nespustené). Nečíta sa zašifrovaný
súbor `terrain.cfg.lua.pak.crypt`, ani `manifest.bin`, ani nič z programu.

Formát `.surface5` nie je zdokumentovaný; rozloženie, ako sa číta zo súborov, je zapísané v
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Stručne: index záznamov dlaždíc (transformácia, hranice a zoznamy typizovaných bajtových
prúdov, z ktorých každý zoznam nasleduje shader a materiál, ktorým sa kreslí), potom surové dáta. Nie je komprimovaný ani šifrovaný. Prúd `Pbase` dlaždice nesie jej vrcholy; skupina kreslená ako `Land` nesie trojuholníky a `TRITYPE` pre každý trojuholník, ktorého najnižší bit označuje more; ostatné skupiny sú prekryvy, ktoré dávajú vyššie uvedené triedy.

## Overené {#verified}

- `list` prečítal index každého nainštalovaného územia (milióny až desiatky miliónov vrcholov zeme každé), každá vzorkovaná dlaždica sa dekódovala na vierohodné metre.
- Na oblastiach dvoch území pristáli mestá z `towns.lua` do niekoľkých metrov od vrcholu zeme, na pevnine, N z N; najvyššia zem sa zhodovala so skutočným vrcholom do desať metrov; letiská, rieky, dediny a cesty sa ukázali vo svojich triedach. Obe úrovne sa načítali v prehliadači, s označeniami miest v rovnakých metroch DCS sediacimi na zemi.
- Na oblasti scény pristáli umiestnenia budov na svojej zemi; svetlá dráhy kopírovali dráhu hry a vagóny a úseky múrov sa zarovnali s dekódovaným smerom, všetky.
- `tests/` vytvára súbory `.surface5` v rovnakom rozložení, takže sa tu nechávajú žiadne herné dáta; `tests/test_real_install.py` beží na inštalácii počítača, na ktorom sa testy spúšťajú, a bez nej sa preskočí.

**Neoverené:** celé veľké územie v jednej úrovni (vyššie uvedená ochrana veľkosti existuje z dôvodu), a verzie DCS iné ako tá vyskúšaná.

## Nečíta sa {#not-read}

- **Budovy ako tvary** (modely sú `.edm` v `Models/`): len škatule, zámerne. Ich rozloženie a rozloženie scény je zapísané v
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); číta sa každé nainštalované územie
  (dve staršie územia vo variantnom rozložení, ktoré čítačka tiež pozná).
- Stromy, svetlá a ostatné objekty scény: prečítané, nekreslené.
- **Sieť ciest ako graf** (`roads/*.rn4`): nedekóduje sa.
- Textúry, stromy, vlny mora, nižšie úrovne detailu terénu samotného.
