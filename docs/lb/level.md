---
title: "E Level bauen: level"
nav_order: 3
lang: "lb"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# E Level bauen: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Schrëtt fir Schrëtt {#step-by-step}

Nei op der Kommandozeil? Liest fir d'éischt [Ier Dir ufänkt](before-you-start.md).

1. Fannt den Dossiernumm vum Theater mat [`list`](list.md).
2. Fir e klengt Theater: ganz bauen: `heat3d-dcs-maps level <theatre> -o levels`.
3. Fir e grousst: eng Regioun auswielen: `--around <lat> <lon> <km>` (e Quadrat, dat
   sou vill km op all Säit vun engem Punkt geet) oder `--bounds X0 Z0 X1 Z1` a DCS-Meter.
   Benannt et mat `--name`.
4. De Kommando gëtt d'Kachele aus, wéi en se liest, d'Dräieckszuel, d'Datei,
   déi geschriwwe gouf, a wéi vill vun de Stied vum Theater um Buedem landen - e
   Check vun der Projektioun, dee "N of N" soe soll.
5. Lued `<folder>/<name>.glb` am Panel „Hannergrond / Level“ vum Viewer a schalt
   **Captured colour** un, fir d'Buedemklassen ze gesinn.

![level op enger syntheteschen Installatioun](../assets/img/level.svg)

Eng Regioun vum selwechte syntheteschen Theater, no DCS-Meter:

![level mat --bounds an --name](../assets/img/level-bounds.svg)

## Optiounen {#options}

| Optioun | Standard | Mécht |
|---|---|---|
| `theatre` | - | den Dossiernumm ënner `Mods\terrains`, wéi `list` en ausgëtt (all Schreifweis) |
| `-o`, `--out` | erfuerderlech | den Dossier, an deen `<name>.glb` an `<name>.json` geschriwwe ginn |
| `--dcs FOLDER` | fonnt | den DCS-World-Dossier ([wou en fonnt gëtt](list.md#where-the-install-is-found)) |
| `--name NAME` | dee vum Theater | den Numm vum Level, a vu senge Dateien |
| `--around LAT LON KM` | - | nëmmen e Quadrat, dat sou vill km op all Säit vun engem Punkt geet |
| `--bounds X0 Z0 X1 Z1` | - | nëmmen dës Këscht, a DCS-Meter (x Norden, z Ouschten) |
| `--cell M` | `0` | d'Mesh verdënnen: all Vertex bannent *M* Meter gëtt een (0: dem Spill seng eegen Dräiecker) |
| `--seabed` | aus | de Mieresbuedem als Buedem halen (standardméisseg gëtt en ausgelooss) |
| `--no-water` | aus | dat flaacht Mier auslooss |
| `--no-buildings` | aus | d'Gebaier vun der Szen vum Theater auslooss |
| `--force` | aus | eng ganz grouss Map ganz a mat vollem Detail exportéieren |
| `--projection LON0 FE FN` | dat vum Theater | Transverse-Mercator-Konstanten fir en Theater, dat dëst Tool net kennt ([fit](fit.md)) |

All Optioun, esou wéi de Programm se ausgëtt: [Kommando-Referenz](../cli-reference.md).

## Gréisst {#size}

Dem Spill seng Mesh ass adaptiv - oppent Mier a Dräiecker, kilometerbreet, Küsten
a Stroossen a puer Meter. E klengt Theater sinn e puer Millioune Dräiecker; déi grouss
si Zéngerte vu Millioune Vertices. Iwwer 30 Millioune Vertices, déi ze liesen sinn, hält `level`
un (Exit-Status 1) a freet no enger Regioun, enger dënnerer Mesh (`--cell 50`) oder
`--force`.

Exit-Status: 0 fäerdeg; 1 feelgeschloen oder ze grouss; 2 d'Installatioun oder d'Theater
gouf net fonnt (déi fonnte Theatere ginn opgelëscht).

## Beispiller {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Wat an den Dateie steet: [D'Level-Dateien](output.md).
