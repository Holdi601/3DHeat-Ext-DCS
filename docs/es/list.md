---
title: "Buscar teatros: list"
nav_order: 2
lang: es
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Buscar teatros: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

¿Nuevo en la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).

1. Instálala una vez: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, abre una terminal en
   esa carpeta y ejecuta `python -m pip install -e .` (Python 3.10 o posterior; trae numpy, y pyarrow
   para `fit` con un `.parquet`).
2. Ejecuta `heat3d-dcs-maps list`.
3. Cada teatro instalado imprime una línea: su nombre de carpeta (el nombre que usan los demás
   comandos), el tamaño de su archivo de terreno, sus teselas y vértices, si se conoce su proyección
   de latitud/longitud, y si se puede leer. Debes ver `readable` al final de cada línea.

![list en una instalación sintética](../assets/img/list.svg)

La imagen es una ejecución sobre una instalación que construyen las pruebas (`tests/synth.py`), no
sobre el juego.

## Dónde se encuentra la instalación {#where-the-install-is-found}

`--dcs <folder>` (la carpeta que contiene `Mods\terrains`) o la variable de entorno `DCS_PATH`; si no,
se busca en el registro, en las bibliotecas de Steam y en las carpetas habituales.

| Opción | Qué hace |
|---|---|
| `--dcs FOLDER` | la carpeta de DCS World, la que contiene `Mods\terrains` |

Estado de salida: 0 terminado; 2 no se encontró ninguna instalación o ningún teatro.
