---
title: "Construire un niveau : level"
nav_order: 3
lang: fr
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Construire un niveau : `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <théâtre> -o <dossier> [--dcs DOSSIER] [--name NOM]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Pas à pas {#step-by-step}

Vous débutez avec la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).

1. Trouvez le nom du dossier du théâtre avec [`list`](list.md).
2. Pour un petit théâtre, construisez-le en entier : `heat3d-dcs-maps level <théâtre> -o levels`.
3. Pour un grand, choisissez une région : `--around <lat> <lon> <km>` (un carré de
   autant de km de part et d'autre d'un point) ou `--bounds X0 Z0 X1 Z1` en mètres DCS.
   Donnez-lui un nom avec `--name`.
4. La commande affiche les tuiles au fur et à mesure de leur lecture, le nombre de triangles, le
   fichier écrit, et combien des villes du théâtre tombent sur le sol - un contrôle de la
   projection qui doit afficher « N sur N ».
5. Chargez `<dossier>/<nom>.glb` dans le panneau Arrière-plan / niveau de la visionneuse et activez
   **Couleur capturée** pour voir les classes de sol.

![level sur une installation synthétique](../assets/img/level.svg)

Une région du même théâtre synthétique, en mètres DCS :

![level avec --bounds et --name](../assets/img/level-bounds.svg)

## Options {#options}

| Option | Par défaut | Effet |
|---|---|---|
| `théâtre` | - | le nom du dossier sous `Mods\terrains`, tel que `list` l'affiche (quelle que soit la casse) |
| `-o`, `--out` | obligatoire | le dossier où écrire `<nom>.glb` et `<nom>.json` |
| `--dcs DOSSIER` | trouvé | le dossier de DCS World ([où il est trouvé](list.md#où-linstallation-est-trouvée)) |
| `--name NOM` | celui du théâtre | le nom du niveau, et celui de ses fichiers |
| `--around LAT LON KM` | - | seulement un carré de ce nombre de km de part et d'autre d'un point |
| `--bounds X0 Z0 X1 Z1` | - | seulement cette boîte, en mètres DCS (x vers le nord, z vers l'est) |
| `--cell M` | `0` | alléger le maillage : chaque sommet à moins de *M* mètres devient un seul sommet (0 : les triangles du jeu) |
| `--seabed` | désactivé | garder le fond de la mer comme sol (par défaut il est omis) |
| `--no-water` | désactivé | omettre la mer plate |
| `--no-buildings` | désactivé | omettre les bâtiments de la scène du théâtre |
| `--force` | désactivé | exporter une très grande carte en entier, en pleine finesse |
| `--projection LON0 FE FN` | celle du théâtre | constantes de Transverse Mercator pour un théâtre que cet outil ne connaît pas ([fit](fit.md)) |

Chaque option, telle que le programme l'affiche : [Référence des commandes](../cli-reference.md).

## Taille {#size}

Le maillage du jeu est adaptatif : la mer ouverte en triangles de plusieurs kilomètres, les côtes
et les routes en quelques mètres. Un petit théâtre compte quelques millions de triangles ; les grands
comptent des dizaines de millions de sommets. Au-delà de 30 millions de sommets à lire, `level`
s'arrête (code de sortie 1) et demande une région, un maillage plus léger (`--cell 50`) ou
`--force`.

Code de sortie : 0 terminé ; 1 échec ou trop grand ; 2 l'installation ou le théâtre n'a pas été
trouvé (les théâtres trouvés sont listés).

## Exemples {#examples}

```bash
heat3d-dcs-maps level <théâtre> -o levels                                       # en entier, pleine finesse
heat3d-dcs-maps level <théâtre> --around <lat> <lon> 12 -o levels --name Partie # un carré de 24 km
heat3d-dcs-maps level <théâtre> --bounds 1000 2000 1390 2390 -o levels          # une boîte en mètres DCS
heat3d-dcs-maps level <théâtre> --cell 50 -o levels                             # en entier, allégé à 50 m
heat3d-dcs-maps level <théâtre> --no-buildings --no-water -o levels             # le sol seul
```

Ce qui se trouve dans les fichiers : [Les fichiers de niveau](output.md).
