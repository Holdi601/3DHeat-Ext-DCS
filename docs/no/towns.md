---
title: "Stedsnavn: towns"
nav_order: 5
lang: no
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Stedsnavn: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Skriver ut teaterets stedsnavn, fra dets `map/towns.lua` (lest som tekst,
aldri kjørt), som JSON: hver bys navn, dens breddegrad og lengdegrad, og dens
DCS-`x` (nord) og `z` (øst) i meter, gjennom teaterets projeksjon.

1. Finn teaterets mappenavn med [`list`](list.md).
2. Kjør `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Bruk `x`/`z` til å merke et nivå, eller til å kontrollere et opptaks posisjoner.

![byer på en syntetisk installasjon](../assets/img/towns.svg)

| Alternativ | Gjør |
|---|---|
| `theatre` | mappenavnet under `Mods\terrains` |
| `--dcs FOLDER` | DCS World-mappen |

Byene innenfor et nivås område står også i dens `<name>.json`, med
høyden på bakken under hver ([Nivåfilene](output.md)).
