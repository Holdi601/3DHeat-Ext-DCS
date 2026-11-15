---
title: "Construirea unui nivel: level"
nav_order: 3
lang: ro
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Construirea unui nivel: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Pas cu pas {#step-by-step}

Nu ați mai lucrat în linia de comandă? Citiți mai întâi [Înainte de a începe](before-you-start.md).

1. Aflați numele dosarului teatrului cu [`list`](list.md).
2. Pentru un teatru mic, construiți-l întreg: `heat3d-dcs-maps level <theatre> -o levels`.
3. Pentru unul mare, alegeți o regiune: `--around <lat> <lon> <km>` (un pătrat de atâția km
   de fiecare parte a unui punct) sau `--bounds X0 Z0 X1 Z1` în metri DCS.
   Dați-i un nume cu `--name`.
4. Comanda afișează plăcile pe măsură ce le citește, numărul de triunghiuri, fișierul scris și
   câte dintre orașele teatrului ajung pe sol - o verificare a proiecției, care ar trebui să
   spună „N din N”.
5. Încărcați `<folder>/<name>.glb` în panoul Fundal / nivel al vizualizatorului și activați
   **Culoare capturată** ca să vedeți clasele de sol.

![level pe o instalare sintetică](../assets/img/level.svg)

O regiune din același teatru sintetic, în metri DCS:

![level cu --bounds și --name](../assets/img/level-bounds.svg)

## Opțiuni {#options}

| Opțiune | Implicit | Ce face |
|---|---|---|
| `theatre` | - | numele dosarului din `Mods\terrains`, cum îl afișează `list` (orice literă) |
| `-o`, `--out` | obligatorie | dosarul în care se scriu `<name>.glb` și `<name>.json` |
| `--dcs FOLDER` | găsit | dosarul DCS World ([unde se găsește](list.md#where-the-install-is-found)) |
| `--name NAME` | al teatrului | numele nivelului și al fișierelor sale |
| `--around LAT LON KM` | - | doar un pătrat de atâția km de fiecare parte a unui punct |
| `--bounds X0 Z0 X1 Z1` | - | doar această casetă, în metri DCS (x nord, z est) |
| `--cell M` | `0` | rărește plasa: fiecare vârf aflat la mai puțin de *M* metri devine unul singur (0: triunghiurile jocului) |
| `--seabed` | dezactivată | păstrează fundul mării ca sol (implicit este lăsat deoparte) |
| `--no-water` | dezactivată | lasă deoparte marea plată |
| `--no-buildings` | dezactivată | lasă deoparte clădirile din scena teatrului |
| `--force` | dezactivată | exportă o hartă foarte mare întreagă, la detaliu complet |
| `--projection LON0 FE FN` | al teatrului | constantele Transverse Mercator pentru un teatru pe care acest instrument nu îl cunoaște ([fit](fit.md)) |

Fiecare opțiune, așa cum o afișează programul: [Referința comenzilor](../cli-reference.md).

## Dimensiune {#size}

Plasa jocului este adaptivă - mare deschisă în triunghiuri de kilometri, coaste și drumuri
în câțiva metri. Un teatru mic are câteva milioane de triunghiuri; cele mari au zeci de milioane
de vârfuri. Peste 30 de milioane de vârfuri de citit, `level` se oprește (cod de stare 1) și cere
o regiune, o plasă mai rară (`--cell 50`) sau `--force`.

Codul de stare: 0 gata; 1 eșec sau prea mare; 2 instalarea sau teatrul nu au fost găsite
(se listează teatrele găsite).

## Exemple {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Ce este în fișiere: [Fișierele nivelului](output.md).
