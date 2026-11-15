---
title: "Proyecciones: fit"
nav_order: 6
lang: es
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Proyecciones: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Cada teatro es una proyección Transversal de Mercator con sus propias constantes. La
herramienta las conoce para los teatros con los que se comprobó; para uno que no conoce,
`fit` las encuentra a partir de cualquier grabación que contenga latitud/longitud y metros
de DCS, como una sesión de un vuelo grabada con 3DHeat Watcher.

1. Graba un vuelo en el teatro con 3DHeat Watcher (o haz cualquier grabación con las columnas
   `lat`, `lon`, `x`, `z` en metros de DCS: x son metros al norte, z metros al este, como en
   todo DCS).
2. Ejecuta `heat3d-dcs-maps fit "<session>/heat.parquet"` (o un `.jsonl` o `.csv`).
3. Imprime la proyección ajustada como JSON, el error cuadrático medio de la raíz sobre los
   puntos, y los argumentos `--projection` que hay que usar.
4. Construye el nivel con ellos:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit sobre una grabación sintética](../assets/img/fit.svg)

La grabación de la imagen son nueve puntos hechos con una proyección conocida, que `fit`
recupera hasta el milímetro.

| Argumento | Qué hace |
|---|---|
| `recording` | `.parquet`, `.jsonl` o `.csv` con las columnas `lat`, `lon`, `x`, `z` (metros de DCS); las filas que no se leen se saltan |

La proyección es la serie de Krüger tal como la da C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Estado de salida: 0 un buen ajuste (raíz del error cuadrático medio menor de 5 m); 1 un
ajuste pobre, o menos de tres filas útiles; 2 no se encontró el archivo.
