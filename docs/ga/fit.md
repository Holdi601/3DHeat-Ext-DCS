---
title: "Teilgeanna: fit"
nav_order: 6
lang: ga
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Teilgeanna: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Is teilgean Transverse Mercator é gach téatar lena sheasmhachtaí féin. Tá aithne ag an
uirlis orthu do na téatair ar seiceáladh í orthu; do cheann nach bhfuil aithne aici air,
aimsíonn `fit` iad ó aon taifeadadh a bhfuil domhanleithead/domhanfhad agus
méadair DCS araon ann, mar shuíomh de chuid 3DHeat Watcher d'eitilt amháin.

1. Taifead eitilt ar an téatar le 3DHeat Watcher (nó déan aon
   taifeadadh le colúin `lat`, `lon`, `x`, `z` i méadair DCS: is é x méadair
   ó thuaidh, z méadair soir, mar atá i ngach áit i DCS).
2. Rith `heat3d-dcs-maps fit "<session>/heat.parquet"` (nó `.jsonl` nó `.csv`).
3. Priontálann sé an teilgean feistithe mar JSON, an earráid fhréamh-mheánchearnach thar
   na pointí, agus na hargóintí `--projection` le húsáid.
4. Tóg an leibhéal leo:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit ar thaifeadadh sintéiseach](../assets/img/fit.svg)

Is naoi bpointe an taifeadadh sa phictiúr a rinneadh ó theilgean aitheanta,
a aimsíonn `fit` ar ais go dtí an milliméadar.

| Argóint | Cad a dhéanann sí |
|---|---|
| `recording` | `.parquet`, `.jsonl` nó `.csv` le colúin `lat`, `lon`, `x`, `z` (méadair DCS); scipeáiltear sraitheanna nach léitear |

Is sraith Krüger an teilgean mar a thugann C. F. F. Karney í ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Stádas scoir: 0 feistiú maith (faoi 5 m fréamh-mheánchearnach); 1 feistiú lag, nó
níos lú ná trí shraith in-úsáidte; 2 níor aimsíodh an comhad.
