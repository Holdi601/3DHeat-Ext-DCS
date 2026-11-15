---
title: "Vytvorenie úrovne: level"
nav_order: 3
lang: "sk"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Vytvorenie úrovne: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Krok za krokom {#step-by-step}

Nikdy ste nepracovali s príkazovým riadkom? Najprv si prečítajte [Ako začať](before-you-start.md).

1. Názov priečinka územia zistite príkazom [`list`](list.md).
2. Pre malé územie ho vytvorte celé: `heat3d-dcs-maps level <theatre> -o levels`.
3. Pre veľké vyberte oblasť: `--around <lat> <lon> <km>` (štvorec takto veľký na každú stranu od bodu)
   alebo `--bounds X0 Z0 X1 Z1` v metroch DCS. Pomenujte ju pomocou `--name`.
4. Príkaz vypisuje dlaždice pri ich čítaní, počet trojuholníkov, zapísaný súbor
   a koľko miest územia leží na zemi – kontrolu projekcie, ktorá by mala ukázať „N z N“.
5. Načítajte `<folder>/<name>.glb` do panela Pozadie / level prehliadača a zapnite
   **Zachytená farba**, aby ste videli triedy zeme.

![úroveň na syntetickej inštalácii](../assets/img/level.svg)

Oblasť toho istého syntetického územia v metroch DCS:

![úroveň s --bounds a --name](../assets/img/level-bounds.svg)

## Možnosti {#options}

| Možnosť | Predvolené | Čo robí |
|---|---|---|
| `theatre` | - | názov priečinka pod `Mods\terrains`, tak ako ho vypisuje `list` (ľubovoľné veľkosti písmen) |
| `-o`, `--out` | povinné | priečinok, do ktorého sa zapíšu `<name>.glb` a `<name>.json` |
| `--dcs FOLDER` | nájdené | priečinok DCS World ([kde sa nachádza](list.md#where-the-install-is-found)) |
| `--name NAME` | názov územia | názov úrovne a jej súborov |
| `--around LAT LON KM` | - | len štvorec takto veľký na každú stranu od bodu |
| `--bounds X0 Z0 X1 Z1` | - | len tento obdĺžnik v metroch DCS (x na sever, z na východ) |
| `--cell M` | `0` | zredukuje sieť: každý vrchol do *M* metrov sa stane jedným (0: trojuholníky samotnej hry) |
| `--seabed` | vypnuté | ponechá morské dno ako zem (predvolene sa vynechá) |
| `--no-water` | vypnuté | vynechá plochú hladinu mora |
| `--no-buildings` | vypnuté | vynechá budovy zo scény územia |
| `--force` | vypnuté | exportuje veľmi veľkú mapu celú v plnom detaile |
| `--projection LON0 FE FN` | územia | konštanty Transverse Mercator pre územie, ktoré tento nástroj nepozná ([fit](fit.md)) |

Každá možnosť tak, ako ju program vypisuje: [Referencia príkazov](../cli-reference.md).

## Veľkosť {#size}

Sieť hry je adaptívna – otvorené more v trojuholníkoch vysokých na kilometre, pobrežia
a cesty na niekoľko metrov. Malé územie je niekoľko miliónov trojuholníkov; veľké majú desiatky miliónov vrcholov. Nad 30 miliónov vrcholov na čítanie sa `level`
zastaví (stavový kód 1) a požiada o oblasť, redšiu sieť (`--cell 50`) alebo `--force`.

Stavový kód: 0 hotovo; 1 zlyhalo alebo je príliš veľké; 2 inštalácia alebo územie sa nenašli
(vypíšu sa nájdené územia).

## Príklady {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # celé, plný detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # štvorec 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # obdĺžnik v metroch DCS
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # celé, zredukované na 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # samotná zem
```

Čo je v súboroch: [Súbory úrovne](output.md).
