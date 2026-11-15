---
title: "Að finna leiksvæði: list"
nav_order: 2
lang: is
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Að finna leiksvæði: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Ertu ný/r í skipanalínunni? Lestu fyrst [Áður en þú byrjar](before-you-start.md).

1. Settu upp einu sinni: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, opnaðu
   skipanalínu í þeirri möppu og keyrðu `python -m pip install -e .` (Python 3.10
   eða nýrra; það kemur með numpy, og pyarrow fyrir `fit` á `.parquet`).
2. Keyrðu `heat3d-dcs-maps list`.
3. Hvert uppsett leiksvæði prentar eina línu: möppuheiti þess (nafnið sem hinar
   skipanirnar taka), stærð landskrárinnar, flísar og hnúta,
   hvort breiddar-/lengdargráðuvörpun þess er þekkt, og hvort það les.
   Þú ættir að sjá `readable` í lok hverrar línu.

![list á gerviuppsetningu](../assets/img/list.svg)

Myndin er keyrsla á uppsetningu sem prófanirnar smíða (`tests/synth.py`), ekki á
leiknum.

## Hvar uppsetningin finnst {#where-the-install-is-found}

`--dcs <folder>` (mappan sem geymir `Mods\terrains`) eða umhverfisbreytan `DCS_PATH`;
annars er leitað í registry, Steam-söfnum og
venjulegum möppum.

| Valkostur | Gerir |
|---|---|
| `--dcs FOLDER` | DCS World mappan, sú sem geymir `Mods\terrains` |

Útgöngustaða: 0 búið, 2 engin uppsetning eða ekkert leiksvæði fannst.
