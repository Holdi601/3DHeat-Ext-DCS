---
title: Com es llegeixen els fitxers
nav_order: 7
lang: ca
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Com es llegeixen els fitxers {#how-the-files-are-read}

Només `Mods/terrains/<teatre>/surface/*.surface5` (la malla del terreny),
`Scenes/*.scn5` (on es troben els objectes, i la caixa de cada model),
`AirfieldsTaxiways/*.rn4` i `map/towns.lua` (els noms dels llocs, llegits com a text,
mai executats). No el fitxer xifrat `terrain.cfg.lua.pak.crypt`, ni `manifest.bin`, ni res del
programa.

El format `.surface5` no està documentat; la disposició, tal com es llegeix dels fitxers,
està escrita a [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
En resum: un índex de registres de mosaic (una transformació, els límits, i llistes de
fluxos de bytes tipats, cada llista seguida de l'shader i del material amb què es dibuixa),
i després les dades crues. No està comprimit ni xifrat. El flux `Pbase` del mosaic
conté els seus vèrtexs; el grup que es dibuixa com a `Land` conté els triangles i un
`TRITYPE` per triangle, el bit més baix del qual marca el mar; els altres grups són les
capes que donen les classes de dalt.

## Verificat {#verified}

- `list` va llegir l'índex de cada teatre instal·lat (de milions a desenes de milions de vèrtexs
  de terreny cadascun), cada mosaic mostrat descodificat en metres plausibles.
- En regions de dos teatres, els pobles de `towns.lua` van caure a menys de metres
  d'un vèrtex de terreny, sobre terra ferma, N de N; la zona més alta va coincidir amb el cim
  real a menys de deu metres; els aeròdroms, rius, pobles i carreteres apareixien
  a les seves classes. Els dos nivells es van carregar al visualitzador, amb marcadors de
  poble en els mateixos metres de DCS, damunt del terreny.
- En una regió d'escena, les col·locacions d'edificis van caure sobre el seu terreny; les llums de pista
  seguien la pista del joc, i els vagons i els segments de mur s'alineaven amb el rumb descodificat, tots.
- `tests/` construeix fitxers `.surface5` amb la mateixa disposició, de manera que aquí no es guarda
  cap dada del joc; `tests/test_real_install.py` s'executa sobre la instal·lació de la màquina
  que fa les proves, i s'omet si no n'hi ha cap.

**No comprovat:** tot un teatre gran en un sol nivell (la protecció per mida de dalt
existeix per una raó), i versions de DCS diferents de la provada.

## No llegit {#not-read}

- **Edificis com a formes** (els models són `.edm` a `Models/`): només caixes,
  a propòsit. La seva disposició, i la de l'escena, està escrita a
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); cada teatre
  instal·lat es llegeix (dos teatres més antics en una variant de disposició que el lector també coneix).
- Arbres, llums i els altres objectes de l'escena: llegits, no dibuixats.
- **La xarxa de carreteres com a graf** (`roads/*.rn4`): no descodificada.
- Textures, arbres, les ones del mar, els nivells inferiors de detall propis del terreny.
