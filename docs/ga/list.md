---
title: "Téatair a aimsiú: list"
nav_order: 2
lang: ga
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Téatair a aimsiú: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

An bhfuil tú nua leis an líne ordaithe? Léigh [Sula dtosaíonn tú](before-you-start.md) ar dtús.

1. Suiteáil uair amháin: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, oscail
   teirminéal sa fhillteán sin agus rith `python -m pip install -e .` (Python 3.10
   nó níos nuaí; tugann sé numpy leis, agus pyarrow do `fit` ar `.parquet`).
2. Rith `heat3d-dcs-maps list`.
3. Priontálann gach téatar suiteáilte líne amháin: ainm a fhillteáin (an t-ainm a ghlacann na
   horduithe eile), méid a chomhaid talún, a tíleanna agus a rinn,
   an eol an teilgean domhanleithid/domhanfhad aige, agus an léitear é.
   Ba chóir duit `readable` a fheiceáil ag deireadh gach líne.

![list ar shuiteáil sintéiseach](../assets/img/list.svg)

Is rith é an pictiúr ar shuiteáil a thógann na tástálacha (`tests/synth.py`), ní ar
an gcluiche.

## An áit a n-aimsítear an tsuiteáil {#where-the-install-is-found}

`--dcs <folder>` (an fillteán ina bhfuil `Mods\terrains`) nó an athróg
timpeallachta `DCS_PATH`; ar shlí eile cuardaítear an clárlann, leabharlanna Steam agus na
gnáthfhillteáin.

| Rogha | Cad a dhéanann sí |
|---|---|
| `--dcs FOLDER` | fillteán DCS World, an ceann ina bhfuil `Mods\terrains` |

Stádas scoir: 0 déanta, 2 gan suiteáil ná téatar aimsithe.
