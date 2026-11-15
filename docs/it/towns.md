---
title: "Nomi di luoghi: towns"
nav_order: 5
lang: "it"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nomi di luoghi: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <teatro> [--dcs CARTELLA]
```

Stampa i nomi dei luoghi del teatro, dal suo `map/towns.lua` (letto come testo, mai eseguito),
come JSON: il nome di ogni città, la sua latitudine e longitudine, e la sua `x` (nord) e `z` (est)
DCS in metri, attraverso la proiezione del teatro.

1. Trova il nome della cartella del teatro con [`list`](list.md).
2. Esegui `heat3d-dcs-maps towns <teatro> > towns.json`.
3. Usa le `x`/`z` per dare un'etichetta a un livello, o per controllare le posizioni di una
   registrazione.

![towns su un'installazione sintetica](../assets/img/towns.svg)

| Opzione | Cosa fa |
|---|---|
| `teatro` | il nome della cartella sotto `Mods\terrains` |
| `--dcs CARTELLA` | la cartella di DCS World |

Le città nella regione di un livello sono anche nel suo `<nome>.json`, con l'altezza del terreno
sotto ciascuna ([I file del livello](output.md)).
