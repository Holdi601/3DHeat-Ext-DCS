---
title: "Nazivi mjesta: towns"
nav_order: 5
lang: "bs"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nazivi mjesta: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Ispisuje nazive mjesta teatra, iz njegovog `map/towns.lua` (čita se kao tekst,
nikad ne izvršava), kao JSON: ime svakog grada, njegovu geografsku širinu i dužinu te njegove
DCS `x` (sjever) i `z` (istok) u metrima, kroz projekciju teatra.

1. Nađi naziv foldera teatra pomoću [`list`](list.md).
2. Pokreni `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Koristi `x`/`z` da označiš nivo ili da provjeriš pozicije iz snimka.

![towns na sintetičkoj instalaciji](../assets/img/towns.svg)

| Opcija | Šta radi |
|---|---|
| `theatre` | naziv foldera pod `Mods\terrains` |
| `--dcs FOLDER` | folder DCS Worlda |

Gradovi unutar regije nivoa nalaze se i u njegovom `<name>.json`, s
visinom tla ispod svakog ([Datoteke nivoa](output.md)).
