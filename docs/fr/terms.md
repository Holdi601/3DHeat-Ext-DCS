---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Les conditions d'Eagle Dynamics {#eagle-dynamics-terms}

Lues le 2026-11-07 dans `Doc/license_en.txt` de l'installation (contrat de licence utilisateur final de DCS World,
The Fighter Collection Ltd). Le « Programme » sous licence comprend « THE DATA SUPPLIED WITH IT ». Clause 3.1 :

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

La clause 3.1 (a) interdit, sans consentement, de « sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program », et (e) de « exploit this Program or any of its parts commercially ».

Ce que fait ce lecteur : il lit des fichiers de données sur votre propre ordinateur, après leur installation,
en dehors du jeu. Il ne modifie rien dans le jeu, ne casse aucun chiffrement (l'unique fichier chiffré d'un
dossier de terrain est laissé de côté) et ne communique avec aucun serveur. Déterminer la disposition d'un
fichier de données relève de la rétro-ingénierie au sens de 3.1 (c), et un niveau construit à partir du
terrain du jeu peut être considéré comme une œuvre dérivée. Utiliser le lecteur relève de votre décision,
pour votre usage ; les niveaux qu'il écrit sont à vous pour les consulter, non pour les partager ou les publier.
C'est pourquoi il s'agit d'un paquet séparé.

L'alternative autorisée, qui ne lit aucun fichier : le script de mission du simulateur peut échantillonner le sol
(`land.getHeight`, `land.getSurfaceType`) et lister les aérodromes (`world.getAirbases`) pendant qu'une mission tourne.
Elle exige que DCS tourne pendant des heures par théâtre et donne une grille plus grossière ; elle n'a pas été
construite, car les fichiers se sont révélés lisibles.

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Nécessite numpy (BSD-3-Clause) ; `fit` sur un
`.parquet` nécessite pyarrow (Apache-2.0). Écrit pour ce projet. Les constantes de projection sont des faits publiés par pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`) ; seuls les nombres ont été repris. La projection est la série de Krüger
telle que la donne C. F. F. Karney (« Transverse Mercator with an accuracy of a few nanometers », Journal of
Geodesy 85, 2011). Aucun code n'a été repris d'un autre projet.
