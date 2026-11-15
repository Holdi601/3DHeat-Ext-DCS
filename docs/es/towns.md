---
title: "Nombres de lugares: towns"
nav_order: 5
lang: es
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nombres de lugares: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Imprime los nombres de lugares del teatro, a partir de su `map/towns.lua` (leído como texto,
nunca ejecutado), como JSON: el nombre de cada pueblo, su latitud y longitud, y su `x` (norte) y
`z` (este) de DCS en metros, mediante la proyección del teatro.

1. Busca el nombre de carpeta del teatro con [`list`](list.md).
2. Ejecuta `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Usa el `x`/`z` para etiquetar un nivel, o para comprobar las posiciones de una grabación.

![pueblos en una instalación sintética](../assets/img/towns.svg)

| Opción | Qué hace |
|---|---|
| `theatre` | el nombre de carpeta bajo `Mods\terrains` |
| `--dcs FOLDER` | la carpeta de DCS World |

Los pueblos dentro de la región de un nivel también están en su `<name>.json`, con la altura del
terreno bajo cada uno ([Los archivos del nivel](output.md)).
