---
title: "Projeksjoner: fit"
nav_order: 6
lang: "no"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projeksjoner: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Hvert teater er en Transverse Mercator-projeksjon med sine egne konstanter. Verktøyet
kjenner dem for teatrene det ble kontrollert på; for et det ikke kjenner, finner `fit`
dem fra et hvilket som helst opptak som har både breddegrad/lengdegrad og
DCS-meter, for eksempel en 3DHeat Watcher-økt med én flyvning.

1. Ta opp en flyvning på teateret med 3DHeat Watcher (eller lag et hvilket som helst opptak
   med kolonnene `lat`, `lon`, `x`, `z` i DCS-meter: x er meter nord, z meter øst, slik
   som overalt i DCS).
2. Kjør `heat3d-dcs-maps fit "<session>/heat.parquet"` (eller en `.jsonl`- eller `.csv`-fil).
3. Den skriver ut den tilpassede projeksjonen som JSON, rotmiddelkvadratfeilen over
   punktene, og `--projection`-argumentene å bruke.
4. Bygg nivået med dem:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit på et syntetisk opptak](../assets/img/fit.svg)

Opptaket på bildet er ni punkter laget fra en kjent projeksjon, som `fit` finner tilbake
til millimeteren.

| Argument | Gjør |
|---|---|
| `recording` | `.parquet`, `.jsonl` eller `.csv` med kolonnene `lat`, `lon`, `x`, `z` (DCS-meter); rader som ikke kan leses, hoppes over |

Projeksjonen er Krügers serie slik C. F. F. Karney gir den («Transverse
Mercator with an accuracy of a few nanometers», Journal of Geodesy 85, 2011).

Avslutningsstatus: 0 en god tilpasning (under 5 m rotmiddelkvadrat); 1 en dårlig tilpasning, eller
færre enn tre brukbare rader; 2 filen ble ikke funnet.
