---
title: "Gradnja ravni: level"
nav_order: 3
lang: sl
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Gradnja ravni: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <teater> -o <mapa> [--dcs MAPA] [--name IME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Korak za korakom {#step-by-step}

Še nisi vajen ukazne vrstice? Najprej preberi [Preden začneš](before-you-start.md).

1. Poišči ime mape teatra z [`list`](list.md).
2. Za majhen teater ga zgradi celega: `heat3d-dcs-maps level <teater> -o levels`.
3. Za velikega izberi območje: `--around <lat> <lon> <km>` (kvadrat, ki sega toliko km na vse
   strani od točke) ali `--bounds X0 Z0 X1 Z1` v metrih DCS. Ime mu daj z `--name`.
4. Ukaz med branjem izpisuje ploščice, število trikotnikov, zapisano datoteko in koliko mest
   teatra pristane na tleh - preverjanje projekcije, ki bi moralo pisati »N od N«.
5. Naloži `<mapa>/<ime>.glb` na plošči Ozadje / nivo pregledovalnika in vklopi **Zajeta barva**, da
   vidiš razrede tal.

![raven na sintetični namestitvi](../assets/img/level.svg)

Območje istega sintetičnega teatra, po metrih DCS:

![raven z --bounds in --name](../assets/img/level-bounds.svg)

## Možnosti {#options}

| Možnost | Privzeto | Naredi |
|---|---|---|
| `teater` | - | ime mape pod `Mods\terrains`, kot ga izpiše `list` (katerakoli pisava) |
| `-o`, `--out` | obvezno | mapa, v katero se zapišeta `<ime>.glb` in `<ime>.json` |
| `--dcs MAPA` | najdeno | mapa DCS World ([kje je najdena](list.md#where-the-install-is-found)) |
| `--name IME` | imena teatra | ime ravni in njenih datotek |
| `--around LAT LON KM` | - | samo kvadrat, ki sega toliko km na vse strani od točke |
| `--bounds X0 Z0 X1 Z1` | - | samo ta škatla, v metrih DCS (x proti severu, z proti vzhodu) |
| `--cell M` | `0` | redčenje mreže: vsaka točka znotraj *M* metrov postane ena (0: igrini lastni trikotniki) |
| `--seabed` | izklopljeno | ohrani morsko dno kot tla (privzeto je izpuščeno) |
| `--no-water` | izklopljeno | izpusti ravno morje |
| `--no-buildings` | izklopljeno | izpusti stavbe iz prizora teatra |
| `--force` | izklopljeno | izvozi zelo velik zemljevid celega v polni podrobnosti |
| `--projection LON0 FE FN` | teatra | konstante Transverse Mercator za teater, ki ga to orodje ne pozna ([fit](fit.md)) |

Vsaka možnost, kot jo izpiše program: [Priročnik ukazov](../cli-reference.md).

## Velikost {#size}

Igrina mreža je prilagodljiva - odprto morje v trikotnikih širine kilometrov, obale in ceste
pa v nekaj metrih. Majhen teater ima nekaj milijonov trikotnikov; veliki imajo deset milijonov
točk ali več. Če je za branje več kot 30 milijonov točk, se `level` ustavi (izhodna koda 1) in
zahteva območje, redkejšo mrežo (`--cell 50`) ali `--force`.

Izhodna koda: 0 opravljeno; 1 neuspeh ali preveliko; 2 namestitev ali teater ni najden (izpišejo
se najdeni teatri).

## Primeri {#examples}

```bash
heat3d-dcs-maps level <teater> -o levels                                       # celoten, polna podrobnost
heat3d-dcs-maps level <teater> --around <lat> <lon> 12 -o levels --name Del   # kvadrat 24 km
heat3d-dcs-maps level <teater> --bounds 1000 2000 1390 2390 -o levels          # škatla v metrih DCS
heat3d-dcs-maps level <teater> --cell 50 -o levels                             # celoten, zredčen na 50 m
heat3d-dcs-maps level <teater> --no-buildings --no-water -o levels             # samo tla
```

Kaj je v datotekah: [Datoteke ravni](output.md).
