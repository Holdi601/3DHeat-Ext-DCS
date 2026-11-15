---
title: "Emrat e vendeve: towns"
nav_order: 5
lang: sq
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Emrat e vendeve: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Shtyp emrat e vendeve të teatrit, nga `map/towns.lua` i tij (lexuar si tekst,
kurrë i ekzekutuar), si JSON: emrin e çdo qyteti, gjerësinë dhe gjatësinë e tij gjeografike, dhe
`x` (veri) dhe `z` (lindje) të tij DCS në metra, përmes projeksionit të teatrit.

1. Gjej emrin e dosjes së teatrit me [`list`](list.md).
2. Ekzekuto `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Përdor `x`/`z` për të etiketuar një nivel, ose për të kontrolluar pozicionet e një regjistrimi.

![towns mbi një instalim sintetik](../assets/img/towns.svg)

| Opsioni | Çfarë bën |
|---|---|
| `theatre` | emri i dosjes nën `Mods\terrains` |
| `--dcs FOLDER` | dosja e DCS World |

Qytetet brenda rajonit të një niveli janë edhe në `<name>.json` të tij, me
lartësinë e tokës nën secilin ([Skedarët e nivelit](output.md)).
