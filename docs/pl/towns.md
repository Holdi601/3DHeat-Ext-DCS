---
title: "Nazwy miejsc: towns"
nav_order: 5
lang: "pl"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nazwy miejsc: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Wypisuje nazwy miejsc teatru z jego pliku `map/towns.lua` (czytanego jako tekst,
nigdy nieuruchamianego) jako JSON: nazwę każdego miasta, jego szerokość i długość geograficzną
oraz jego `x` (północ) i `z` (wschód) w metrach DCS, przez projekcję teatru.

1. Znajdź nazwę folderu teatru poleceniem [`list`](list.md).
2. Uruchom `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Użyj `x`/`z`, by opisać poziom albo sprawdzić pozycje z nagrania.

![miasta na syntetycznej instalacji](../assets/img/towns.svg)

| Opcja | Co robi |
|---|---|
| `theatre` | nazwa folderu w `Mods\terrains` |
| `--dcs FOLDER` | folder DCS World |

Miasta w obszarze poziomu są też w jego `<name>.json`, wraz z wysokością terenu pod każdym z nich
([Pliki poziomu](output.md)).
