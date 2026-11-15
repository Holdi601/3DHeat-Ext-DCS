---
title: "Construir un nivel: level"
nav_order: 3
lang: es
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Construir un nivel: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Paso a paso {#step-by-step}

¿Nuevo en la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).

1. Busca el nombre de carpeta del teatro con [`list`](list.md).
2. Para un teatro pequeño, constrúyelo entero: `heat3d-dcs-maps level <theatre> -o levels`.
3. Para uno grande, elige una región: `--around <lat> <lon> <km>` (un cuadrado de tantos km a cada
   lado de un punto) o `--bounds X0 Z0 X1 Z1` en metros de DCS. Ponle nombre con `--name`.
4. El comando imprime las teselas según las lee, el número de triángulos, el archivo escrito, y
   cuántos pueblos del teatro caen sobre el terreno: una comprobación de la proyección que debe
   decir "N de N".
5. Carga `<folder>/<name>.glb` en el panel Fondo / nivel del visor y activa **Color capturado** para ver
   las clases de terreno.

![level en una instalación sintética](../assets/img/level.svg)

Una región del mismo teatro sintético, por metros de DCS:

![level con --bounds y --name](../assets/img/level-bounds.svg)

## Opciones {#options}

| Opción | Por defecto | Qué hace |
|---|---|---|
| `theatre` | - | el nombre de carpeta bajo `Mods\terrains`, tal como lo imprime `list` (en cualquier mayúscula o minúscula) |
| `-o`, `--out` | obligatoria | la carpeta donde escribir `<name>.glb` y `<name>.json` |
| `--dcs FOLDER` | encontrada | la carpeta de DCS World ([dónde se encuentra](list.md#where-the-install-is-found)) |
| `--name NAME` | la del teatro | el nombre del nivel, y el de sus archivos |
| `--around LAT LON KM` | - | solo un cuadrado de tantos km a cada lado de un punto |
| `--bounds X0 Z0 X1 Z1` | - | solo esta caja, en metros de DCS (x norte, z este) |
| `--cell M` | `0` | aclara la malla: cada vértice a menos de *M* metros se convierte en uno (0: los triángulos propios del juego) |
| `--seabed` | desactivada | conserva el fondo del mar como terreno (por defecto se deja fuera) |
| `--no-water` | desactivada | deja fuera el mar plano |
| `--no-buildings` | desactivada | deja fuera los edificios de la escena del teatro |
| `--force` | desactivada | exporta un mapa muy grande entero con todo el detalle |
| `--projection LON0 FE FN` | la del teatro | constantes de Transversal de Mercator para un teatro que esta herramienta no conoce ([fit](fit.md)) |

Cada opción, tal como la muestra el programa: [Referencia de comandos](../cli-reference.md).

## Tamaño {#size}

La malla del juego es adaptativa: mar abierto en triángulos de kilómetros, costas y carreteras
en unos pocos metros. Un teatro pequeño son unos pocos millones de triángulos; los grandes son
decenas de millones de vértices. Por encima de 30 millones de vértices a leer, `level` se detiene
(código de salida 1) y pide una región, una malla más clara (`--cell 50`) o `--force`.

Estado de salida: 0 terminado; 1 fallido o demasiado grande; 2 no se encontró la instalación o el
teatro (se listan los teatros encontrados).

## Ejemplos {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # entero, detalle completo
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # un cuadrado de 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # una caja en metros de DCS
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # entero, aclarado a 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # solo el terreno
```

Qué hay en los archivos: [Los archivos del nivel](output.md).
