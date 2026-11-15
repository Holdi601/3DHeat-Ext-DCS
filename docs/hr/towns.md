---
title: "Nazivi mjesta: towns"
nav_order: 5
lang: "hr"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nazivi mjesta: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Ispisuje nazive mjesta karte, iz njezina `map/towns.lua` (čitano kao tekst, nikad se ne izvršava), kao JSON: ime svakog grada, njegovu geografsku širinu i dužinu te njegov DCS `x` (sjever) i `z` (istok) u metrima, kroz projekciju karte.

1. Pronađite ime mape karte pomoću [`list`](list.md).
2. Pokrenite `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Upotrijebite `x`/`z` da označite razinu ili da provjerite položaje iz snimke.

![gradovi na sintetičkoj instalaciji](../assets/img/towns.svg)

| Opcija | Što radi |
|---|---|
| `theatre` | ime mape pod `Mods\terrains` |
| `--dcs FOLDER` | mapa DCS Worlda |

Gradovi unutar regije razine također su u njezinu `<name>.json`, s visinom tla ispod svakog ([Datoteke razine](output.md)).
