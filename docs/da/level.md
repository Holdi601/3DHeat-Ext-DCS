---
title: "Byg en bane: level"
nav_order: 3
lang: da
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Byg en bane: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Trin for trin {#step-by-step}

Ny til kommandolinjen? Læs [Før du går i gang](before-you-start.md) først.

1. Find teatrets mappenavn med [`list`](list.md).
2. For et lille teater bygges det hele: `heat3d-dcs-maps level <theatre> -o levels`.
3. For et stort et vælger du en region: `--around <lat> <lon> <km>` (et kvadrat
   så mange km til hver side af et punkt) eller `--bounds X0 Z0 X1 Z1` i DCS-meter.
   Giv den et navn med `--name`.
4. Kommandoen udskriver flagene, mens den læser dem, antallet af trekanter, den
   skrevne fil, og hvor mange af teatrets byer der lander på jorden - en kontrol
   af projektionen, som bør stå "N af N".
5. Indlæs `<folder>/<name>.glb` i fremviserens Baggrund / bane-panel, og slå
   **Optaget farve** til for at se jordklasserne.

![level på en syntetisk installation](../assets/img/level.svg)

En region af det samme syntetiske teater, efter DCS-meter:

![level med --bounds og --name](../assets/img/level-bounds.svg)

## Valgmuligheder {#options}

| Valgmulighed | Standard | Gør |
|---|---|---|
| `theatre` | - | mappenavnet under `Mods\terrains`, som `list` udskriver det (store eller små bogstaver) |
| `-o`, `--out` | påkrævet | mappen, hvor `<name>.glb` og `<name>.json` skrives |
| `--dcs FOLDER` | fundet | DCS World-mappen ([hvor den findes](list.md#where-the-install-is-found)) |
| `--name NAME` | teatrets | banens navn, og dens filers |
| `--around LAT LON KM` | - | kun et kvadrat så mange km til hver side af et punkt |
| `--bounds X0 Z0 X1 Z1` | - | kun denne boks, i DCS-meter (x nord, z øst) |
| `--cell M` | `0` | tynd nettet ud: hver vertex inden for *M* meter bliver til én (0: spillets egne trekanter) |
| `--seabed` | fra | behold havbunden som jord (som standard udelades den) |
| `--no-water` | fra | udelad det flade hav |
| `--no-buildings` | fra | udelad teatrets bygninger i scenen |
| `--force` | fra | eksportér et meget stort kort helt i fuld detalje |
| `--projection LON0 FE FN` | teatrets | Transverse Mercator-konstanter for et teater, dette værktøj ikke kender ([fit](fit.md)) |

Hver valgmulighed, som programmet udskriver den: [Kommandoreference](../cli-reference.md).

## Størrelse {#size}

Spillets net er adaptivt - åbent hav i trekanter flere kilometer på tværs, kyster
og veje i få meter. Et lille teater er nogle få millioner trekanter; de store
er titalls millioner vertices. Over 30 millioner vertices at læse stopper `level`
(exit-status 1) og beder om en region, et tyndere net (`--cell 50`) eller
`--force`.

Exit-status: 0 færdig; 1 mislykkedes eller for stor; 2 installationen eller teatret blev ikke
fundet (de fundne teatre listes).

## Eksempler {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Hvad der er i filerne: [Banefilerne](output.md).
