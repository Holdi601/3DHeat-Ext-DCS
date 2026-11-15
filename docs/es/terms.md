---
title: Condiciones y licencia
nav_order: 8
lang: "es"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## Condiciones de Eagle Dynamics {#eagle-dynamics-terms}

Leído el 2026-11-07 de `Doc/license_en.txt` de la instalación (Acuerdo de Licencia de Usuario Final
de DCS World, The Fighter Collection Ltd). El "Programa" licenciado incluye "THE DATA SUPPLIED WITH IT".
Cláusula 3.1 (texto original en inglés):

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

La cláusula 3.1 (a) prohíbe "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" sin consentimiento, y (e) "exploit this
Program or any of its parts commercially".

Lo que hace este lector: lee archivos de datos en tu propia máquina, después de que los instalaste,
fuera del juego. No cambia nada del juego, no rompe ningún cifrado (el único archivo cifrado de una
carpeta de terreno se deja en paz) y no habla con ningún servidor. Averiguar la disposición de un
archivo de datos es ingeniería inversa en el sentido de 3.1 (c), y un nivel construido con el terreno
del juego es discutiblemente una obra derivada. Usar el lector es decisión tuya, para tu propio uso;
los niveles que escribe son tuyos para verlos, no para compartirlos ni publicarlos. Por eso es un
paquete aparte.

La alternativa autorizada, que no lee ningún archivo: el propio guion de misiones del simulador puede
muestrear el terreno (`land.getHeight`, `land.getSurfaceType`) y listar los aeródromos
(`world.getAirbases`) mientras se ejecuta una misión. Necesita DCS funcionando durante horas por
teatro y da una malla más gruesa; no se construyó, porque los archivos resultaron legibles.

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Necesita numpy
(BSD-3-Clause); `fit` con un `.parquet` necesita pyarrow (Apache-2.0). Escrito para este proyecto.
Las constantes de proyección son datos publicados por pydcs (github.com/pydcs/dcs,
`dcs/terrain/*/projection.py`); solo se tomaron los números. La proyección es la serie de Krüger tal
como la da C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No se tomó código de ningún otro proyecto.
