---
title: "Pálya építése: level"
nav_order: 3
lang: hu
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Pálya építése: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Lépésről lépésre {#step-by-step}

Még nem használt parancssort? Előbb olvasd el a [Mielőtt elkezded](before-you-start.md) oldalt.

1. Keresd meg a színház mappanevét a [`list`](list.md) paranccsal.
2. Kis színház esetén építsd egészben: `heat3d-dcs-maps level <theatre> -o levels`.
3. Nagy színháznál válassz egy régiót: `--around <lat> <lon> <km>` (egy négyzet, amely egy pont
   két oldalán ennyi km-re terjed), vagy `--bounds X0 Z0 X1 Z1` DCS-méterben. Nevezd el a
   `--name` kapcsolóval.
4. A parancs kiírja a csempéket, ahogy olvassa őket, a háromszögek számát, a megírt fájlt, és azt,
   hogy a színház városaiból hány esik a talajra – ez a vetítés ellenőrzése, amelynek „N of N”
   értéket kell mutatnia.
5. Töltsd be a `<folder>/<name>.glb` fájlt a megjelenítő Háttér / pálya paneljén, és kapcsold be a
   **Rögzített szín** (Captured colour) lehetőséget, hogy lásd a talajosztályokat.

![level egy szintetikus telepítésen](../assets/img/level.svg)

Ugyanannak a szintetikus színháznak egy régiója, DCS-méterben:

![level --bounds és --name kapcsolóval](../assets/img/level-bounds.svg)

## Kapcsolók {#options}

| Kapcsoló | Alapérték | Mit csinál |
|---|---|---|
| `theatre` | - | a `Mods\terrains` alatti mappanév, ahogy a `list` kiírja (bármely kis- vagy nagybetűvel) |
| `-o`, `--out` | kötelező | a mappa, ahová a `<name>.glb` és `<name>.json` íródik |
| `--dcs FOLDER` | megtalálva | a DCS World mappa ([hol találja](list.md#where-the-install-is-found)) |
| `--name NAME` | a színházé | a pálya neve, és a fájljaié |
| `--around LAT LON KM` | - | csak egy négyzet, amely egy pont két oldalán ennyi km-re terjed |
| `--bounds X0 Z0 X1 Z1` | - | csak ez a doboz, DCS-méterben (x észak, z kelet) |
| `--cell M` | `0` | a háló ritkítása: minden csúcs, amely *M* méteren belül van, egy csúcs lesz (0: a játék saját háromszögei) |
| `--seabed` | ki | a tengerfenék talajként tartása (alapértelmezetten kimarad) |
| `--no-water` | ki | a sík tenger kihagyása |
| `--no-buildings` | ki | a színház jelenetének épületeinek kihagyása |
| `--force` | ki | nagyon nagy térkép egészben, teljes részletességgel való exportálása |
| `--projection LON0 FE FN` | a színházé | Transverse Mercator-állandók egy olyan színházhoz, amelyet ez az eszköz nem ismer ([fit](fit.md)) |

Minden kapcsoló úgy, ahogy a program kiírja: [Parancsleírás](../cli-reference.md).

## Méret {#size}

A játék hálója adaptív: a nyílt tenger kilométer széles háromszögekből áll, a partvonalak és
utak néhány méteresekből. Egy kis színház néhány millió háromszög; a nagyok több tíz millió
csúcsot tartalmaznak. Ha több mint 30 millió csúcsot kell beolvasni, a `level` megáll (kilépési
állapot 1), és kér egy régiót, egy ritkább hálót (`--cell 50`) vagy a `--force` kapcsolót.

Kilépési állapot: 0 kész; 1 sikertelen vagy túl nagy; 2 a telepítés vagy a színház nem található
(a megtalált színházak listázva lesznek).

## Példák {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # egészben, teljes részletesség
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # egy 24 km-es négyzet
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # egy doboz DCS-méterben
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # egészben, 50 m-re ritkítva
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # csak a talaj
```

Mi van a fájlokban: [A pályafájlok](output.md).
