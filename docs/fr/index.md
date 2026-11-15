---
title: "Accueil"
nav_order: 1
lang: fr
source: index.md
source_hash: "a6572e6ff335"
nav_exclude: true
search_exclude: true
permalink: /fr/
---
# 3DHeat DCS {#dheat-dcs}

**Qu'est-ce que c'est ?** Un théâtre (theatre) est le mot de DCS World pour une carte : une
région du monde au-dessus de laquelle on vole. Cet outil transforme le sol d'un théâtre, lu depuis
**votre propre installation**, en un niveau 3D - un modèle au-dessus duquel on peut voler - pour la
visionneuse [3DHeat](https://github.com/Holdi601/3DHeat)
([documentation](https://holdi601.github.io/3DHeat/)).

**À quoi ça sert ?** À voir vos vols DCS sur la carte propre au jeu : ses collines, sa côte, ses
aérodromes, ses routes, ses voies ferrées, ses villes et ses bâtiments.

**Exemple :** `heat3d-dcs-maps level <théâtre> -o levels` ->
`levels/<théâtre>.glb` (le niveau) + `levels/<théâtre>.json` (où il se trouve sur
la Terre, ses villes et ses aérodromes).

À quoi il sert :

- **Des vols sur la carte propre au jeu.** Le fond de carte du monde de 3DHeat dessine la Terre
  d'aujourd'hui à partir de données ouvertes ; celui-ci dessine le théâtre tel que DCS le dessine.
- **Aucune étape de placement.** Le niveau est dans les mètres du monde de DCS, donc la télémétrie
  en mètres DCS (le crochet DCS du 3DHeat Watcher écrit exactement cela) s'y pose avec les réglages par défaut
  de la visionneuse.
- **Latitude et longitude.** Chaque niveau porte sa projection, ses coins et ses villes dans les deux repères.

![D'une installation DCS à un niveau 3DHeat](../assets/img/fr/flow.svg)

## Démarrage rapide {#quick-start}

Vous débutez avec la ligne de commande ? Lisez d'abord [Avant de commencer](before-you-start.md).
Lancez ces commandes dans le dossier que vous avez cloné ou décompressé :

```bash
python -m pip install -e .                         # installe la commande heat3d-dcs-maps
heat3d-dcs-maps list                               # les théâtres installés, et si chacun peut être lu
heat3d-dcs-maps level <théâtre> -o levels          # un théâtre entier (petit)
heat3d-dcs-maps level <théâtre> --around <lat> <lon> 12 -o levels --name <nom>   # 12 km de part et d'autre d'un point
```

Vous devez voir une ligne par théâtre avec `list`, se terminant par `readable`.
Chargez ensuite `levels/<nom>.glb` dans le panneau Arrière-plan / niveau de la visionneuse
([Niveaux](https://holdi601.github.io/3DHeat/levels.html)).

Les niveaux écrits sont construits à partir des données du jeu : ils restent **sur votre
ordinateur**, pour les consulter, et non pour les partager ou les publier ([Conditions](terms.md)).

## Pages {#pages}

| Page | Ce qu'elle explique |
|---|---|
| [Avant de commencer](before-you-start.md) | Python, un terminal, un premier essai |
| [Trouver les théâtres : list](list.md) | où l'installation est trouvée, ce qu'affiche `list` |
| [Construire un niveau : level](level.md) | chaque option, les régions, la taille, pas à pas |
| [Les fichiers de niveau](output.md) | les parties `.glb`, les classes de sol et leurs couleurs, le `.json`, les coordonnées |
| [Noms de lieux : towns](towns.md) | les villes d'un théâtre avec leurs coordonnées DCS |
| [Projections : fit](fit.md) | trouver la projection d'un théâtre à partir d'un enregistrement |
| [Comment les fichiers sont lus](reading.md) | les formats, ce qui a été vérifié, ce qui n'est pas lu |
| [Conditions et licence](terms.md) | la licence d'Eagle Dynamics, et pourquoi c'est un paquet séparé |
| [Référence des commandes](../cli-reference.md) | chaque option, générée depuis le code |
| [Maintenir ces documents](maintaining.md) | la liste de contrôle des versions |

## Voir aussi {#related}

- La visionneuse 3DHeat : [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentation sur [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- Télémétrie pour ces niveaux : le [3DHeat Watcher](https://holdi601.github.io/3DHeat-Watcher/)
  enregistre les vols DCS ; les formats de fichiers de la visionneuse, dont son
  conteneur d'un fichier par partie, sont décrits dans
  [Un fichier par partie (.3dheat)](https://holdi601.github.io/3DHeat/container.html).

## Les outils 3DHeat {#the-3dheat-tools}

| Outil | Ce qu'il fait | Code | Documentation |
|---|---|---|---|
| Visionneuse 3DHeat | affiche les données : cartes de chaleur, analyse de course, revue de partie | [3DHeat](https://github.com/Holdi601/3DHeat) | [documentation](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveaux et circuits tirés des fichiers du jeu | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [documentation](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | télémétrie de tour, et niveaux reconstruits à partir de vidéos de jeu | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [documentation](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin de l'éditeur Unreal : un niveau en un seul `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [documentation](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | démos et cartes de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [documentation](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | enregistre ce que les jeux publient pendant que vous jouez | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [documentation](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | replays de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [documentation](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | replays de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [documentation](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | replays de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [documentation](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | démos de serveurs Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [documentation](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | cartes de DCS World sous forme de niveaux 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [documentation](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | cartes d'IL-2 Sturmovik sous forme de niveaux 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [documentation](https://holdi601.github.io/3DHeat-Ext-IL2/) |
