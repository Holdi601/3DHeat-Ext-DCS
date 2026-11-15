---
title: "Jak se soubory čtou"
nav_order: 7
lang: cs
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Jak se soubory čtou {#how-the-files-are-read}

Čtou se jen `Mods/terrains/<theatre>/surface/*.surface5` (síť terénu),
`Scenes/*.scn5` (kde objekty stojí a kvádr každého modelu),
`AirfieldsTaxiways/*.rn4` a `map/towns.lua` (názvy míst, čtené jako text,
nikdy nespouštěné). Ne šifrovaný
`terrain.cfg.lua.pak.crypt`, ne `manifest.bin`, nic z programu.

Formát `.surface5` není zdokumentovaný; jeho rozložení, jak je čteno ze souborů, je zapsáno
v [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Stručně: rejstřík záznamů dlaždic (transformace, hranice a seznamy typovaných bajtových
proudů, každý seznam následovaný shaderem a materiálem, kterým se kreslí), pak surová data.
Není komprimovaný ani šifrovaný. Proud `Pbase` dlaždice drží její vrcholy; skupina kreslená
jako `Land` drží trojúhelníky a `TRITYPE` pro každý trojúhelník, jehož nejnižší bit značí moře;
ostatní skupiny jsou překryvy, které dávají výše uvedené třídy.

## Ověřeno {#verified}

- `list` přečetl rejstřík každého nainstalovaného území (miliony až desítky milionů vrcholů
  terénu na každé), každá vzorkovaná dlaždice se dekódovala na věrohodné metry.
- Na oblastech dvou území se města z `towns.lua` objevila v řádu metrů od vrcholu terénu, na
  souši, N z N; nejvyšší terén se shodl se skutečným vrcholem do deseti metrů; letiště, řeky,
  vesnice a silnice se objevily ve svých třídách. Obě úrovně se načetly v prohlížeči se značkami
  měst ve stejných metrech DCS, ležícími na zemi.
- Na oblasti scény dopadla umístění budov na svůj terén; světla dráhy vykreslila dráhu hry
  a vagóny a segmenty zdí se zarovnaly s dekódovaným směrem, všechny.
- `tests/` vytváří soubory `.surface5` ve stejném rozložení, takže zde se nechová žádná data
  hry; `tests/test_real_install.py` běží na instalaci stroje, na kterém se testy spouštějí,
  a bez ní se přeskočí.

**Neověřeno:** celé velké území v jedné úrovni (ochrana velikosti výše je tu z dobrého důvodu) a verze
DCS jiné než ta vyzkoušená.

## Nečte se {#not-read}

- **Budovy jako tvary** (modely jsou `.edm` v `Models/`): jen krabice, záměrně. Jejich
  rozložení a rozložení scény je zapsáno v
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); čtou se všechna
  nainstalovaná území (dvě starší území v jiném rozložení, které čtečka také zná).
- Stromy, světla a ostatní objekty scény: přečteny, nekresleny.
- **Silniční síť jako graf** (`roads/*.rn4`): nedekódováno.
- Textury, stromy, vlny moře, nižší úrovně detailu terénu.
