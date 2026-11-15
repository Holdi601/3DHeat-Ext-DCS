---
title: "Hogyan olvasódnak be a fájlok"
nav_order: 7
lang: "hu"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Hogyan olvasódnak be a fájlok {#how-the-files-are-read}

Csak ezek olvasódnak: `Mods/terrains/<theatre>/surface/*.surface5` (a talajháló),
`Scenes/*.scn5` (hol állnak az objektumok, és minden modell doboza), `AirfieldsTaxiways/*.rn4`
és `map/towns.lua` (helynevek, szövegként olvasva, sosem futtatva). Nem olvasódik a titkosított
`terrain.cfg.lua.pak.crypt`, nem a `manifest.bin`, és a program semmi más része sem.

A `.surface5` formátum nincs dokumentálva; az elrendezés, a fájlokból olvasva, le van írva itt:
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Röviden: csempe-bejegyzések indexe (egy transzformáció, határok, és típusos bájtfolyamok listái, mindegyik
lista után az árnyaló és az anyag, amellyel rajzolják), majd a nyers adat. Nincs tömörítve és nincs titkosítva.
A csempe `Pbase` folyama tartalmazza a csúcsait; a `Land`-ként rajzolt csoport a háromszögeket és háromszögenként
egy `TRITYPE`-ot, amelynek legalacsonyabb bitje jelzi a tengert; a többi csoport az átfedés, amely a fenti
osztályokat adja.

## Ellenőrizve {#verified}

- A `list` beolvasta minden telepített színház indexét (több millió, akár több tíz millió talaj-csúcs
  színházanként), és minden mintavételezett csempe ésszerű méterekre dekódolódott.
- Két színház régióin a `towns.lua` városai egy talajcsúcs méterein belül, szárazföldön estek, N of N;
  a legmagasabb talaj a valódi csúcshoz tíz méteren belül egyezett; a repülőterek, folyók, falvak és utak
  a saját osztályukban jelentek meg. Mindkét pálya betöltődött a megjelenítőben, a városjelölők ugyanabban
  a DCS-méterben a talajon ültek.
- Egy jelenetrégión az épület-elhelyezések a saját talajukra estek; a kifutópálya-fények a játék kifutópályáját
  követték, a vagonok és a falszakaszok pedig mindegyik dekódolt irányához illeszkedtek.
- A `tests/` a `.surface5` fájlokat ugyanebben az elrendezésben építi, így nincs játékadat tárolva itt;
  a `tests/test_real_install.py` a tesztelő gép telepítésén fut, és telepítés nélkül kimarad.

**Nem ellenőrizve:** egy nagy színház egészen egy pályában (a fenti méretvédelem nem véletlenül van),
és a DCS más verziói, mint amelyiket kipróbálták.

## Nem olvasódik be {#not-read}

- **Az épületek alakzatként** (a modellek `.edm` fájlok a `Models/` mappában): csak dobozok, szándékosan.
  Ezek elrendezése, és a jelenetéé, le van írva itt:
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  minden telepített színház olvasódik (két régebbi színház egy másik elrendezésben, amelyet az olvasó szintén ismer).
- Fák, lámpák és a jelenet többi objektuma: beolvasva, de nem rajzolva.
- **Az úthálózat gráfként** (`roads/*.rn4`): nincs dekódolva.
- Textúrák, fák, a tenger hullámai, a terep alacsonyabb részletességi szintjei.
