---
title: "Nibnu livell: level"
nav_order: 3
lang: mt
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Nibnu livell: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Pass b'pass {#step-by-step}

Ġdid mal-linja tal-kmandi? Aqra [Qabel ma tibda](before-you-start.md) l-ewwel.

1. Sib l-isem tal-folder tat-teatru b'[`list`](list.md).
2. Għal teatru żgħir, ibnih sħiħ: `heat3d-dcs-maps level <theatre> -o levels`.
3. Għal wieħed kbir, agħżel reġjun: `--around <lat> <lon> <km>` (kwadru ta' dawk
   il-km kull naħa ta' punt) jew `--bounds X0 Z0 X1 Z1` f'metri ta' DCS.
   Semmih b'`--name`.
4. Il-kmand jistampa t-tiles waqt li jaqrahom, l-għadd tat-trijangoli, il-fajl
   miktub, u kemm mill-irħula tat-teatru jaqgħu fuq l-art - kontroll tal-
   projezzjoni li għandu jaqra "N of N".
5. Tgħabbi `<folder>/<name>.glb` fil-pannell Sfond / livell tal-viewer u ixgħel
   **Kulur maqbud** biex tara l-klassijiet tal-art.

![level fuq installazzjoni sintetika](../assets/img/level.svg)

Reġjun tal-istess teatru sintetiku, f'metri ta' DCS:

![level b'--bounds u --name](../assets/img/level-bounds.svg)

## Għażliet {#options}

| Għażla | Default | X'jagħmel |
|---|---|---|
| `theatre` | - | l-isem tal-folder taħt `Mods\terrains`, kif jistampah `list` (kwalunkwe każ) |
| `-o`, `--out` | meħtieġa | il-folder fejn jinkitbu `<name>.glb` u `<name>.json` |
| `--dcs FOLDER` | misjub | il-folder ta' DCS World ([fejn jinstab](list.md#where-the-install-is-found)) |
| `--name NAME` | dak tat-teatru | l-isem tal-livell, u tal-fajls tiegħu |
| `--around LAT LON KM` | - | kwadru biss ta' dawn il-km kull naħa ta' punt |
| `--bounds X0 Z0 X1 Z1` | - | dan il-kaxxa biss, f'metri ta' DCS (x tramuntana, z lvant) |
| `--cell M` | `0` | irqaq il-mesh: kull vertiċi fi *M* metri jsir wieħed (0: it-trijangoli proprji tal-logħba) |
| `--seabed` | mitfi | żomm il-qiegħ tal-baħar bħala art (b'mod awtomatiku jitħalla barra) |
| `--no-water` | mitfi | ħalli barra l-baħar ċatt |
| `--no-buildings` | mitfi | ħalli barra l-bini tax-xena tat-teatru |
| `--force` | mitfi | esporta mappa kbira ħafna sħiħa b'dettall sħiħ |
| `--projection LON0 FE FN` | dik tat-teatru | kostanti Transverse Mercator għal teatru li din l-għodda ma tafux ([fit](fit.md)) |

Kull għażla, kif jistampaha l-programm: [Referenza tal-kmandi](../cli-reference.md).

## Daqs {#size}

Il-mesh tal-logħba huwa adattiv - baħar miftuħ f'trijangoli kilometri wiesgħa, kosti
u toroq ftit metri. Teatru żgħir huwa ftit miljuni ta' trijangoli; il-kbar
huma għexieren ta' miljuni ta' vertiċi. 'Il fuq minn 30 miljun vertiċi biex jinqraw, `level`
jieqaf (exit status 1) u jitlob reġjun, mesh irqaq (`--cell 50`) jew
`--force`.

Status tal-ħruġ: 0 lest; 1 falla jew kbir wisq; 2 l-installazzjoni jew it-teatru
ma nstabux (it-teatri misjuba jiġu elenkati).

## Eżempji {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

X'hemm fil-fajls: [Il-fajls tal-livell](output.md).
