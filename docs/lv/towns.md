---
title: "Vietu nosaukumi: towns"
nav_order: 5
lang: lv
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Vietu nosaukumi: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Izdrukā teātra vietu nosaukumus no tā `map/towns.lua` (lasīts kā teksts, nekad nepalaists) kā JSON: katras pilsētas nosaukumu, tās platumu un garumu un DCS `x` (ziemeļi) un `z` (austrumi) metros caur teātra projekciju.

1. Atrodiet teātra mapes nosaukumu ar [`list`](list.md).
2. Palaidiet `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Izmantojiet `x`/`z`, lai marķētu līmeni vai pārbaudītu ieraksta pozīcijas.

![pilsētas uz sintētiska uzstādījuma](../assets/img/towns.svg)

| Iespēja | Ko dara |
|---|---|
| `theatre` | mapes nosaukums zem `Mods\terrains` |
| `--dcs FOLDER` | DCS World mape |

Pilsētas līmeņa reģionā ir arī tā `<name>.json`, ar zemes augstumu zem katras ([Līmeņa faili](output.md)).
