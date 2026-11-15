---
title: "Conditions et licence"
nav_order: 8
lang: fr
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Les conditions d'Eagle Dynamics {#eagle-dynamics-terms}

Lues le 2026-11-07 dans `Doc/license_en.txt` de l'installation (contrat de licence utilisateur final de DCS World,
The Fighter Collection Ltd). Le « Programme » sous licence comprend « LES DONNÉES FOURNIES AVEC LUI ». Clause 3.1 :

> Sauf dispositions expressément prévues dans la présente Licence ou aux clauses 4.1 et 4.2
> ci-dessous, ou autorisées par toute loi locale, vous vous engagez à utiliser le Programme
> pour votre usage personnel, et vous ne devez pas : [...]
>
> (c) désassembler, décompiler, rétro-concevoir ou créer des œuvres dérivées à partir de tout
> ou partie du Programme, ni tenter de le faire, sauf dans la mesure où (en vertu de l'article 296A de la
> loi britannique Copyright, Designs and Patents Act 1988) ces actes ne peuvent être interdits
> parce qu'ils sont essentiels pour atteindre l'interopérabilité du Programme avec un autre
> programme logiciel, et à condition que les informations obtenues à cette occasion : (i) ne soient
> utilisées que pour atteindre cette interopérabilité ; (ii) ne soient pas divulguées ou communiquées
> sans nécessité à un tiers sans le consentement écrit préalable du TFC ; et (iii) ne soient
> pas utilisées pour créer un logiciel substantiellement semblable au Programme.

La clause 3.1 (a) interdit de « vendre, échanger, louer, donner en sous-licence, fusionner,
adapter, modifier le Programme » sans consentement, et (e) d'« exploiter ce Programme ou une de ses parties à des fins commerciales ».

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
