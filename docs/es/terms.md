---
title: Condiciones y licencia
nav_order: 8
lang: "es"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## Qué lee el lector {#what-the-reader-reads}

El lector lee archivos de datos de tu propia instalación de DCS World en tu ordenador ([Cómo se leen los archivos](reading.md)). No cambia nada del juego y no se comunica con ningún servidor.

No se incluye ni se redistribuye nada del juego: ningún archivo del juego, ningún código del juego, ninguna DLL; las pruebas generan cada archivo que leen. Los niveles que escribe se quedan en tu equipo.

3DHeat DCS no está afiliado a Eagle Dynamics ni cuenta con su respaldo. DCS World y los nombres y marcas relacionados pertenecen a sus propietarios.

Titulares de derechos: abrid una incidencia en [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - respondemos rápido y retiramos lo que se nos pida.

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Necesita numpy
(BSD-3-Clause); `fit` con un `.parquet` necesita pyarrow (Apache-2.0). Escrito para este proyecto.
Las constantes de proyección son datos publicados por pydcs (github.com/pydcs/dcs,
`dcs/terrain/*/projection.py`); solo se tomaron los números. La proyección es la serie de Krüger tal
como la da C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No se tomó código de ningún otro proyecto.
