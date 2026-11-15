---
title: "Logainmneacha: towns"
nav_order: 5
lang: ga
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Logainmneacha: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Priontálann sé logainmneacha an téatair, óna `map/towns.lua` (léite mar théacs,
gan a rith riamh), mar JSON: ainm gach baile, a dhomhanleithead agus a dhomhanfhad, agus a
`x` (ó thuaidh) agus `z` (soir) DCS i méadair, tríd an teilgean ag an téatar.

1. Aimsigh ainm fhillteán an téatair le [`list`](list.md).
2. Rith `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Úsáid an `x`/`z` chun leibhéal a lipéadú, nó chun suíomhanna taifeadta a sheiceáil.

![towns ar shuiteáil sintéiseach](../assets/img/towns.svg)

| Rogha | Cad a dhéanann sí |
|---|---|
| `theatre` | ainm an fhillteáin faoi `Mods\terrains` |
| `--dcs FOLDER` | fillteán DCS World |

Tá na bailte laistigh de réigiún leibhéil ina `<name>.json` freisin, le
hairde na talún faoi gach ceann ([Comhaid an leibhéil](output.md)).
