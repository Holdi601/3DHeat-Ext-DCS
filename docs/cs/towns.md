---
title: "Názvy míst: towns"
nav_order: 5
lang: cs
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Názvy míst: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Vypíše názvy míst území z jeho `map/towns.lua` (čteno jako text,
nikdy nespouštěno) jako JSON: název každého města, jeho zeměpisnou šířku a délku
a jeho `x` (sever) a `z` (východ) v DCS v metrech, přes projekci území.

1. Zjistěte název složky území pomocí [`list`](list.md).
2. Spusťte `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Použijte `x`/`z` k popsání úrovně nebo ke kontrole pozic v záznamu.

![města na syntetické instalaci](../assets/img/towns.svg)

| Možnost | Co dělá |
|---|---|
| `theatre` | název složky pod `Mods\terrains` |
| `--dcs FOLDER` | složka DCS World |

Města uvnitř oblasti úrovně jsou také v jejím `<name>.json`, s výškou terénu pod každým
([Soubory úrovně](output.md)).
