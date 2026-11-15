---
title: "Bygga en nivå: level"
nav_order: 3
lang: sv
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Bygga en nivå: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Steg för steg {#step-by-step}

Har du aldrig använt kommandoraden förut? Läs [Innan du börjar](before-you-start.md) först.

1. Hitta teaterns mappnamn med [`list`](list.md).
2. För en liten teater, bygg den hel: `heat3d-dcs-maps level <theatre> -o levels`.
3. För en stor, välj en region: `--around <lat> <lon> <km>` (en kvadrat så många km åt vardera hållet från en punkt) eller `--bounds X0 Z0 X1 Z1` i DCS-meter.
   Ge den ett namn med `--name`.
4. Kommandot skriver ut kakelrutorna när det läser dem, antalet trianglar, filen som skrivs, och hur många av teaterns städer som hamnar på marken - en kontroll av projektionen som bör visa "N av N".
5. Läs in `<folder>/<name>.glb` i visarens panel Bakgrund / nivå och slå på **Fångad färg** för att se markklasserna.

![level på en syntetisk installation](../assets/img/level.svg)

En region av samma syntetiska teater, i DCS-meter:

![level med --bounds och --name](../assets/img/level-bounds.svg)

## Alternativ {#options}

| Alternativ | Standard | Gör |
|---|---|---|
| `theatre` | - | mappnamnet under `Mods\terrains`, så som `list` skriver ut det (vilka versaler som helst) |
| `-o`, `--out` | krävs | mappen att skriva `<name>.glb` och `<name>.json` i |
| `--dcs FOLDER` | hittas | DCS World-mappen ([var den hittas](list.md#where-the-install-is-found)) |
| `--name NAME` | teaterns | nivåns namn, och dess filers |
| `--around LAT LON KM` | - | bara en kvadrat så många km åt vardera hållet från en punkt |
| `--bounds X0 Z0 X1 Z1` | - | bara den här rutan, i DCS-meter (x norrut, z österut) |
| `--cell M` | `0` | gallra nätet: varje hörn inom *M* meter blir ett (0: spelets egna trianglar) |
| `--seabed` | av | behåll havsbotten som mark (som standard utelämnas den) |
| `--no-water` | av | utelämna det platta havet |
| `--no-buildings` | av | utelämna teaterns scenbyggnader |
| `--force` | av | exportera en mycket stor karta hel i full detalj |
| `--projection LON0 FE FN` | teaterns | Transversal Mercator-konstanter för en teater som verktyget inte känner till ([fit](fit.md)) |

Alla alternativ, så som programmet skriver ut dem: [Kommandoreferens](../cli-reference.md).

## Storlek {#size}

Spelets nät är adaptivt - öppet hav i trianglar kilometer breda, kuster och vägar i några meter. En liten teater är några miljoner trianglar; de stora har tiotals miljoner hörn. Över 30 miljoner hörn att läsa slutar `level` (avslutskod 1) och ber om en region, ett tunnare nät (`--cell 50`) eller `--force`.

Avslutskod: 0 klart; 1 misslyckades eller för stort; 2 installationen eller teatern hittades inte (de hittade teatrarna listas).

## Exempel {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # hel, full detalj
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # en kvadrat på 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # en ruta i DCS-meter
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # hel, gallrad till 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # bara marken
```

Vad som finns i filerna: [Nivåfilerna](output.md).
