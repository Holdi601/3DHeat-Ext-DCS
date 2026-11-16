---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Ce que lit le lecteur {#what-the-reader-reads}

Le lecteur lit des fichiers de données de votre propre installation de DCS World, sur votre ordinateur ([Comment les fichiers sont lus](reading.md)). Il ne modifie rien dans le jeu et ne contacte aucun serveur.

Rien du jeu n'est livré ni redistribué : aucun fichier du jeu, aucun code du jeu, aucune DLL ; les tests construisent eux-mêmes chaque fichier qu'ils lisent. Les niveaux qu'il écrit restent sur votre machine.

3DHeat DCS n'est ni affilié à Eagle Dynamics ni approuvé par celui-ci. DCS World ainsi que les noms et marques associés appartiennent à leurs propriétaires.

Ayants droit : ouvrez un ticket sur [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - nous répondons rapidement et retirons tout élément sur demande.

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Nécessite numpy (BSD-3-Clause) ; `fit` sur un
`.parquet` nécessite pyarrow (Apache-2.0). Écrit pour ce projet. Les constantes de projection sont des faits publiés par pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`) ; seuls les nombres ont été repris. La projection est la série de Krüger
telle que la donne C. F. F. Karney (« Transverse Mercator with an accuracy of a few nanometers », Journal of
Geodesy 85, 2011). Aucun code n'a été repris d'un autre projet.
