---
title: "Bygge et nivå: level"
nav_order: 3
lang: "no"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Bygge et nivå: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Steg for steg {#step-by-step}

Ny til kommandolinjen? Les [Før du starter](before-you-start.md) først.

1. Finn teaterets mappenavn med [`list`](list.md).
2. For et lite teater, bygg det helt: `heat3d-dcs-maps level <theatre> -o levels`.
3. For et stort, velg en region: `--around <lat> <lon> <km>` (et kvadrat så mange km
   til hver side av et punkt) eller `--bounds X0 Z0 X1 Z1` i DCS-meter.
   Gi den navn med `--name`.
4. Kommandoen skriver ut flisene mens den leser dem, antall trekanter, filen
   som ble skrevet, og hvor mange av teaterets byer som havner på bakken - en
   kontroll av projeksjonen som bør si «N av N».
5. Last inn `<folder>/<name>.glb` i visningsprogrammets Bakgrunn / nivå-panel og slå på
   **Registrert farge** for å se bakkeklassene.

![nivå på en syntetisk installasjon](../assets/img/level.svg)

En region av det samme syntetiske teateret, i DCS-meter:

![nivå med --bounds og --name](../assets/img/level-bounds.svg)

## Alternativer {#options}

| Alternativ | Standard | Gjør |
|---|---|---|
| `theatre` | - | mappenavnet under `Mods\terrains`, slik `list` skriver det (alle bokstaver) |
| `-o`, `--out` | påkrevd | mappen å skrive `<name>.glb` og `<name>.json` inn i |
| `--dcs FOLDER` | funnet | DCS World-mappen ([hvor den finnes](list.md#where-the-install-is-found)) |
| `--name NAME` | teaterets | nivåets navn, og filenes |
| `--around LAT LON KM` | - | bare et kvadrat så mange km til hver side av et punkt |
| `--bounds X0 Z0 X1 Z1` | - | bare denne boksen, i DCS-meter (x nord, z øst) |
| `--cell M` | `0` | tynn ut nettet: hver toppunkt innen *M* meter blir ett (0: spillets egne trekanter) |
| `--seabed` | av | behold havbunnen som bakke (som standard utelates den) |
| `--no-water` | av | utelat det flate havet |
| `--no-buildings` | av | utelat teaterets bygninger i scenen |
| `--force` | av | eksporter et veldig stort kart helt, i full detaljgrad |
| `--projection LON0 FE FN` | teaterets | Transverse Mercator-konstanter for et teater dette verktøyet ikke kjenner ([fit](fit.md)) |

Alle alternativene, slik programmet skriver dem ut: [Kommandoreferanse](../cli-reference.md).

## Størrelse {#size}

Spillets nett er adaptivt - åpent hav i trekanter kilometer brede, kyster
og veier i noen få meter. Et lite teater er noen få millioner trekanter; de store
er titalls millioner toppunkter. Over 30 millioner toppunkter å lese stopper `level`
(avslutningsstatus 1) og ber om en region, et tynnere nett (`--cell 50`) eller
`--force`.

Avslutningsstatus: 0 ferdig; 1 mislyktes eller for stor; 2 installasjonen eller teateret ble
ikke funnet (teatrene som ble funnet, listes).

## Eksempler {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # hele, full detalj
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # et kvadrat på 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # en boks i DCS-meter
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # hele, tynnet ut til 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # bare bakken
```

Hva som er i filene: [Nivåfilene](output.md).
