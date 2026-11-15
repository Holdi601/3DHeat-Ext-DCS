---
title: "Trobar teatres: list"
nav_order: 2
lang: "ca"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Trobar teatres: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs CARPETA]
```

Si ets nou amb la línia d'ordres, llegeix primer [Abans de començar](before-you-start.md).

1. Instal·la-la una vegada: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, obre
   una terminal en aquesta carpeta i executa `python -m pip install -e .` (Python 3.10
   o posterior; porta numpy, i pyarrow per a `fit` amb un `.parquet`).
2. Executa `heat3d-dcs-maps list`.
3. Cada teatre instal·lat imprimeix una línia: el nom de la seva carpeta (el nom que
   prenen les altres ordres), la mida del seu fitxer de terreny, els seus mosaics i vèrtexs,
   si es coneix la seva projecció de latitud/longitud, i si es pot llegir. Hauries de veure
   `readable` al final de cada línia.

![list sobre una instal·lació sintètica](../assets/img/list.svg)

La imatge és una execució sobre una instal·lació que construeixen les proves (`tests/synth.py`), no
sobre el joc.

## On es troba la instal·lació {#where-the-install-is-found}

`--dcs <carpeta>` (la carpeta que conté `Mods\terrains`) o la variable d'entorn `DCS_PATH`;
si no, s'hi busca al registre, a les biblioteques de Steam i a les carpetes habituals.

| Opció | Què fa |
|---|---|
| `--dcs CARPETA` | la carpeta de DCS World, la que conté `Mods\terrains` |

Estat de sortida: 0 fet; 2 no s'ha trobat cap instal·lació ni cap teatre.
