---
title: "Comment les fichiers sont lus"
nav_order: 7
lang: "fr"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Comment les fichiers sont lus {#how-the-files-are-read}

Seuls `Mods/terrains/<théâtre>/surface/*.surface5` (le maillage du sol),
`Scenes/*.scn5` (où se posent les objets, et la boîte de chaque modèle),
`AirfieldsTaxiways/*.rn4` et `map/towns.lua` (noms de lieux, lus comme du texte,
jamais exécutés) sont lus. Pas le fichier chiffré
`terrain.cfg.lua.pak.crypt`, ni `manifest.bin`, rien du programme.

Le format `.surface5` n'est pas documenté ; sa disposition, telle qu'elle se lit dans les fichiers,
est décrite dans [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
En bref : un index d'enregistrements de tuiles (une transformation, des limites, et des listes de flux
d'octets typés, chaque liste suivie du shader et du matériau avec lesquels elle est dessinée), puis les
données brutes. Il n'est ni compressé ni chiffré. Le flux `Pbase` d'une tuile contient ses
sommets ; le groupe dessiné comme `Land` contient les triangles et un `TRITYPE` par triangle, dont le bit de poids faible
marque la mer ; les autres groupes sont les superpositions qui donnent les classes ci-dessus.

## Vérifié {#verified}

- `list` a lu l'index de chaque théâtre installé (de quelques millions à plusieurs dizaines de millions de sommets
  de sol chacun), chaque tuile échantillonnée se décodant en mètres plausibles.
- Sur des régions de deux théâtres, les villes de `towns.lua` tombaient à quelques mètres
  d'un sommet du sol, sur la terre, N sur N ; le point le plus haut correspondait au vrai sommet à dix mètres près ;
  aérodromes, rivières, villages et routes apparaissaient dans leurs classes. Les deux niveaux se sont chargés dans le
  visualiseur, avec des repères de villes aux mêmes mètres DCS posés sur le sol.
- Sur une région de scène, les placements de bâtiments tombaient sur leur sol ; les feux de piste suivaient la
  piste du jeu, et les wagons et segments de mur s'alignaient sur le cap décodé, tous.
- `tests/` construit des fichiers `.surface5` selon la même disposition, donc aucune donnée du jeu n'est
  conservée ici ; `tests/test_real_install.py` tourne sur l'installation de la machine qui exécute les tests, et est
  ignoré sans installation.

**Non vérifié :** l'ensemble d'un grand théâtre dans un seul niveau (la limite de taille
ci-dessus existe pour une raison), et les versions de DCS autres que celle essayée.

## Non lu {#not-read}

- **Les bâtiments comme formes** (les modèles sont des `.edm` dans `Models/`) : des boîtes seulement,
  volontairement. Leur disposition, et celle de la scène, sont décrites dans
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py) ; chaque théâtre
  installé se lit (deux théâtres plus anciens dans une variante de disposition que le lecteur connaît aussi).
- Arbres, lumières et les autres objets de la scène : lus, non dessinés.
- **Le réseau routier sous forme de graphe** (`roads/*.rn4`) : non décodé.
- Textures, arbres, vagues de la mer, les niveaux de détail inférieurs du terrain.
