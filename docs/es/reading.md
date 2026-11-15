---
title: Cómo se leen los archivos
nav_order: 7
lang: "es"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Cómo se leen los archivos {#how-the-files-are-read}

Solo `Mods/terrains/<theatre>/surface/*.surface5` (la malla del terreno),
`Scenes/*.scn5` (dónde están los objetos, y la caja de cada modelo),
`AirfieldsTaxiways/*.rn4` y `map/towns.lua` (nombres de lugares, leídos como texto,
nunca ejecutados). No el `terrain.cfg.lua.pak.crypt` cifrado, no `manifest.bin`, nada del programa.

El formato `.surface5` no está documentado; la disposición, tal como se lee de los archivos, está
escrita en [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
En resumen: un índice de registros de tesela (una transformación, los límites, y listas de flujos
de bytes con tipo, cada lista seguida del sombreador y el material con que se dibuja), y luego los
datos en bruto. No está comprimido ni cifrado. El flujo `Pbase` de la tesela contiene sus vértices;
el grupo dibujado como `Land` contiene los triángulos y un `TRITYPE` por triángulo, cuyo bit más bajo
marca el mar; los demás grupos son las capas que dan las clases de arriba.

## Verificado {#verified}

- `list` leyó el índice de cada teatro instalado (de millones a decenas de millones de vértices de
  terreno cada uno), y cada tesela muestreada se decodificó a metros plausibles.
- En regiones de dos teatros, los pueblos de `towns.lua` cayeron a metros de un vértice del terreno,
  sobre tierra, N de N; la cota más alta coincidió con la cumbre real a diez metros; aeródromos, ríos,
  pueblos y carreteras aparecieron en sus clases. Ambos niveles se cargaron en el visor, con marcadores
  de pueblos en los mismos metros de DCS, sobre el terreno.
- En una región de escena, las colocaciones de edificios cayeron sobre su terreno; las luces de pista
  trazaron la pista del juego, y los vagones y segmentos de muro se alinearon con el rumbo decodificado,
  todos.
- `tests/` construye archivos `.surface5` con la misma disposición, así que aquí no se guarda ningún
  dato del juego; `tests/test_real_install.py` se ejecuta sobre la instalación de la máquina que hace
  las pruebas, y se omite si no hay ninguna.

**No comprobado:** el conjunto de un teatro grande en un solo nivel (la protección de tamaño de arriba
existe por algo), y versiones de DCS distintas de la probada.

## No se lee {#not-read}

- **Edificios como formas** (los modelos son `.edm` en `Models/`): solo cajas, a propósito. Su
  disposición, y la de la escena, están escritas en
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  se lee cada teatro instalado (dos teatros más antiguos en una variante de disposición que el lector
  también conoce).
- Árboles, luces y los demás objetos de la escena: se leen, no se dibujan.
- **La red de carreteras como grafo** (`roads/*.rn4`): no se decodifica.
- Texturas, árboles, las olas del mar, los niveles de detalle inferiores del terreno.
