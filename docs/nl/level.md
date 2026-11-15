---
title: "Een level bouwen: level"
nav_order: 3
lang: nl
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Een level bouwen: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Stap voor stap {#step-by-step}

Nog nooit met de opdrachtregel gewerkt? Lees eerst [Voordat je begint](before-you-start.md).

1. Zoek de mapnaam van het thema op met [`list`](list.md).
2. Bij een klein thema bouw je het geheel: `heat3d-dcs-maps level <theatre> -o levels`.
3. Bij een groot thema kies je een gebied: `--around <lat> <lon> <km>` (een vierkant zoveel km
   aan elke kant van een punt) of `--bounds X0 Z0 X1 Z1` in DCS-meters.
   Geef het een naam met `--name`.
4. De opdracht drukt de tegels af terwijl hij ze leest, het aantal driehoeken, het geschreven
   bestand, en hoeveel steden van het thema op de grond terechtkomen - een controle van de
   projectie die "N van N" moet aangeven.
5. Laad `<folder>/<name>.glb` in het paneel Achtergrond / level van de viewer en zet
   **Vastgelegde kleur** aan om de grondklassen te zien.

![level op een synthetische installatie](../assets/img/level.svg)

Een gebied van hetzelfde synthetische thema, in DCS-meters:

![level met --bounds en --name](../assets/img/level-bounds.svg)

## Opties {#options}

| Optie | Standaard | Doet |
|---|---|---|
| `theatre` | - | de mapnaam onder `Mods\terrains`, zoals `list` die afdrukt (elk hoofdletterbeeld) |
| `-o`, `--out` | verplicht | de map waarin `<name>.glb` en `<name>.json` worden geschreven |
| `--dcs FOLDER` | gevonden | de map van DCS World ([waar die wordt gevonden](list.md#where-the-install-is-found)) |
| `--name NAME` | die van het thema | de naam van het level, en van de bestanden ervan |
| `--around LAT LON KM` | - | alleen een vierkant zoveel km aan elke kant van een punt |
| `--bounds X0 Z0 X1 Z1` | - | alleen deze doos, in DCS-meters (x noord, z oost) |
| `--cell M` | `0` | dun het mesh uit: elk hoekpunt binnen *M* meter wordt er één (0: de eigen driehoeken van het spel) |
| `--seabed` | uit | houd de zeebodem als grond (standaard wordt hij weggelaten) |
| `--no-water` | uit | laat de vlakke zee weg |
| `--no-buildings` | uit | laat de gebouwen van de scène van het thema weg |
| `--force` | uit | exporteer een heel groot kaart in één keer op volle detail |
| `--projection LON0 FE FN` | die van het thema | Transverse Mercator-constanten voor een thema dat deze tool niet kent ([fit](fit.md)) |

Elke optie, zoals het programma ze afdrukt: [Commandoreferentie](../cli-reference.md).

## Grootte {#size}

Het mesh van het spel is adaptief - open zee in driehoeken van kilometers, kusten en wegen
in een paar meter. Een klein thema is een paar miljoen driehoeken; de grote hebben tientallen
miljoenen hoekpunten. Boven 30 miljoen te lezen hoekpunten stopt `level` (exitstatus 1) en vraagt
om een gebied, een dunner mesh (`--cell 50`) of `--force`.

Exitstatus: 0 klaar; 1 mislukt of te groot; 2 de installatie of het thema is niet gevonden
(de gevonden thema's worden opgesomd).

## Voorbeelden {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # heel, volledig detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # een vierkant van 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # een doos in DCS-meters
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # heel, uitgedund tot 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # alleen de grond
```

Wat er in de bestanden zit: [De levelbestanden](output.md).
