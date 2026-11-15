---
title: "Plaatsnamen: towns"
nav_order: 5
lang: "nl"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Plaatsnamen: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Drukt de plaatsnamen van het thema af, uit zijn `map/towns.lua` (als tekst gelezen,
nooit uitgevoerd), als JSON: de naam van elke stad, haar breedte- en lengtegraad, en
haar DCS-`x` (noord) en `z` (oost) in meters, via de projectie van het thema.

1. Zoek de mapnaam van het thema op met [`list`](list.md).
2. Voer `heat3d-dcs-maps towns <theatre> > towns.json` uit.
3. Gebruik de `x`/`z` om een level te labelen, of om de posities in een opname te controleren.

![steden op een synthetische installatie](../assets/img/towns.svg)

| Optie | Doet |
|---|---|
| `theatre` | de mapnaam onder `Mods\terrains` |
| `--dcs FOLDER` | de map van DCS World |

De steden binnen het gebied van een level staan ook in zijn `<name>.json`, met de hoogte
van de grond onder elke stad ([De levelbestanden](output.md)).
