---
title: "Noms de lieux : towns"
nav_order: 5
lang: fr
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Noms de lieux : `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <théâtre> [--dcs DOSSIER]
```

Affiche les noms de lieux du théâtre, tirés de son `map/towns.lua` (lu comme du texte,
jamais exécuté), en JSON : le nom de chaque ville, sa latitude et sa longitude, et ses
`x` (nord) et `z` (est) DCS en mètres, par la projection du théâtre.

1. Trouvez le nom du dossier du théâtre avec [`list`](list.md).
2. Lancez `heat3d-dcs-maps towns <théâtre> > towns.json`.
3. Utilisez les `x`/`z` pour étiqueter un niveau, ou pour vérifier les positions d'un enregistrement.

![towns sur une installation synthétique](../assets/img/towns.svg)

| Option | Effet |
|---|---|
| `théâtre` | le nom du dossier sous `Mods\terrains` |
| `--dcs DOSSIER` | le dossier de DCS World |

Les villes situées dans la région d'un niveau figurent aussi dans son `<nom>.json`, avec la
hauteur du sol sous chacune ([Les fichiers de niveau](output.md)).
