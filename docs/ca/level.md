---
title: "Construir un nivell: level"
nav_order: 3
lang: ca
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Construir un nivell: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <teatre> -o <carpeta> [--dcs CARPETA] [--name NOM]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Pas a pas {#step-by-step}

Si ets nou amb la línia d'ordres, llegeix primer [Abans de començar](before-you-start.md).

1. Troba el nom de la carpeta del teatre amb [`list`](list.md).
2. Per a un teatre petit, construeix-lo sencer: `heat3d-dcs-maps level <teatre> -o levels`.
3. Per a un de gran, tria una regió: `--around <lat> <lon> <km>` (un quadrat de tants km a
   cada costat d'un punt) o `--bounds X0 Z0 X1 Z1` en metres de DCS.
   Dona-li un nom amb `--name`.
4. L'ordre imprimeix els mosaics a mesura que els llegeix, el recompte de triangles, el
   fitxer escrit, i quants dels pobles del teatre cauen sobre el terreny: una comprovació
   de la projecció que hauria de dir «N de N».
5. Carrega `<carpeta>/<nom>.glb` al panell Fons / nivell del visualitzador i activa
   **Color capturat** per veure les classes de terreny.

![level sobre una instal·lació sintètica](../assets/img/level.svg)

Una regió del mateix teatre sintètic, en metres de DCS:

![level amb --bounds i --name](../assets/img/level-bounds.svg)

## Opcions {#options}

| Opció | Per defecte | Què fa |
|---|---|---|
| `teatre` | - | el nom de la carpeta sota `Mods\terrains`, tal com l'imprimeix `list` (qualsevol majúscula o minúscula) |
| `-o`, `--out` | obligatòria | la carpeta on escriure `<nom>.glb` i `<nom>.json` |
| `--dcs CARPETA` | trobada | la carpeta de DCS World ([on es troba](list.md#where-the-install-is-found)) |
| `--name NOM` | el del teatre | el nom del nivell, i el dels seus fitxers |
| `--around LAT LON KM` | - | només un quadrat d'aquests km a cada costat d'un punt |
| `--bounds X0 Z0 X1 Z1` | - | només aquesta caixa, en metres de DCS (x nord, z est) |
| `--cell M` | `0` | aclarir la malla: cada vèrtex dins de *M* metres es converteix en un (0: els triangles propis del joc) |
| `--seabed` | desactivada | conservar el fons del mar com a terreny (per defecte se'n deixa fora) |
| `--no-water` | desactivada | deixar fora el mar pla |
| `--no-buildings` | desactivada | deixar fora els edificis de l'escena del teatre |
| `--force` | desactivada | exportar un mapa molt gran sencer a detall complet |
| `--projection LON0 FE FN` | la del teatre | constants de Transverse Mercator per a un teatre que aquesta eina no coneix ([fit](fit.md)) |

Totes les opcions, tal com les imprimeix el programa: [Referència de l'ordre](../cli-reference.md).

## Mida {#size}

La malla del joc és adaptativa: el mar obert en triangles de quilòmetres, les costes
i les carreteres en pocs metres. Un teatre petit són uns quants milions de triangles; els
grans són desenes de milions de vèrtexs. Per sobre de 30 milions de vèrtexs a llegir, `level`
s'atura (estat de sortida 1) i demana una regió, una malla més clara (`--cell 50`) o
`--force`.

Estat de sortida: 0 fet; 1 ha fallat o és massa gran; 2 no s'ha trobat la instal·lació o el
teatre (s'enumeren els teatres trobats).

## Exemples {#examples}

```bash
heat3d-dcs-maps level <teatre> -o levels                                       # sencer, detall complet
heat3d-dcs-maps level <teatre> --around <lat> <lon> 12 -o levels --name Part   # un quadrat de 24 km
heat3d-dcs-maps level <teatre> --bounds 1000 2000 1390 2390 -o levels          # una caixa en metres de DCS
heat3d-dcs-maps level <teatre> --cell 50 -o levels                             # sencer, aclarit a 50 m
heat3d-dcs-maps level <teatre> --no-buildings --no-water -o levels             # només el terreny
```

Què hi ha als fitxers: [Els fitxers del nivell](output.md).
