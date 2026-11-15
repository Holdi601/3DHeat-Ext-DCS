---
title: "Staðarnöfn: towns"
nav_order: 5
lang: "is"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Staðarnöfn: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Prentar staðarnöfn leiksvæðisins, úr `map/towns.lua` þess (lesið sem texti,
aldrei keyrt), sem JSON: nafn hvers bæjar, breiddar- og lengdargráðu hans, og
DCS `x` (norður) og `z` (austur) í metrum, gegnum vörpun leiksvæðisins.

1. Finndu möppuheiti leiksvæðisins með [`list`](list.md).
2. Keyrðu `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Notaðu `x`/`z` til að merkja borð, eða til að athuga staðsetningar upptöku.

![towns á gerviuppsetningu](../assets/img/towns.svg)

| Valkostur | Gerir |
|---|---|
| `theatre` | möppuheitið undir `Mods\terrains` |
| `--dcs FOLDER` | DCS World mappan |

Bæirnir innan svæðis borðs eru líka í `<name>.json` þess, með
hæð landsins undir hverjum ([Borðaskrárnar](output.md)).
