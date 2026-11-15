---
title: "Trouver les théâtres : list"
nav_order: 2
lang: "fr"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Trouver les théâtres : `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Vous débutez avec la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).

1. Installez une fois : `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, ouvrez
   un terminal dans ce dossier et lancez `python -m pip install -e .` (Python 3.10
   ou plus récent ; cela installe numpy, et pyarrow pour `fit` sur un `.parquet`).
2. Lancez `heat3d-dcs-maps list`.
3. Chaque théâtre installé affiche une ligne : son nom de dossier (le nom que prennent les autres
   commandes), la taille de son fichier de sol, ses tuiles et ses sommets, si sa projection
   latitude/longitude est connue, et s'il peut être lu. Vous devez voir `readable` à la fin de chaque ligne.

![list sur une installation synthétique](../assets/img/list.svg)

L'image est une exécution sur une installation que construisent les tests (`tests/synth.py`), et non sur
le jeu.

## Où l'installation est trouvée {#where-the-install-is-found}

`--dcs <dossier>` (le dossier qui contient `Mods\terrains`) ou la variable d'environnement `DCS_PATH` ;
sinon, le registre, les bibliothèques Steam et les dossiers habituels sont cherchés.

| Option | Effet |
|---|---|
| `--dcs FOLDER` | le dossier de DCS World, celui qui contient `Mods\terrains` |

Code de sortie : 0 terminé, 2 aucune installation ou aucun théâtre trouvé.
