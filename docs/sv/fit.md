---
title: "Projektioner: fit"
nav_order: 6
lang: "sv"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektioner: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Varje teater är en Transversal Mercator-projektion med egna konstanter. Verktyget känner till dem för de teatrar det har kontrollerats mot; för ett som det inte känner till hittar `fit` dem från en inspelning som innehåller både latitud/longitud och DCS-meter, till exempel en 3DHeat Watcher-session från en flygning.

1. Spela in en flygning över teatern med 3DHeat Watcher (eller gör en inspelning med kolumnerna `lat`, `lon`, `x`, `z` i DCS-meter: x är meter norrut, z meter österut, som överallt i DCS).
2. Kör `heat3d-dcs-maps fit "<session>/heat.parquet"` (eller en `.jsonl`- eller `.csv`-fil).
3. Den skriver ut den anpassade projektionen som JSON, medelkvadratfelet över punkterna, och argumenten `--projection` att använda.
4. Bygg nivån med dem:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit på en syntetisk inspelning](../assets/img/fit.svg)

Inspelningen på bilden är nio punkter gjorda från en känd projektion, som `fit` hittar tillbaka till millimetern.

| Argument | Gör |
|---|---|
| `recording` | `.parquet`, `.jsonl` eller `.csv` med kolumnerna `lat`, `lon`, `x`, `z` (DCS-meter); rader som inte går att läsa hoppas över |

Projektionen är Krügers serie så som C. F. F. Karney ger den ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Avslutskod: 0 en bra anpassning (under 5 m medelkvadratfel); 1 en dålig anpassning, eller färre än tre användbara rader; 2 filen hittades inte.
