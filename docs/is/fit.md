---
title: "Vörpun: fit"
nav_order: 6
lang: is
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Vörpun: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Sérhvert leiksvæði er Transverse Mercator vörpun með eigin fasta. Tólið
þekkir þá fyrir leiksvæðin sem það var prófað á; fyrir svæði sem það þekkir ekki
finnur `fit` þá úr hvaða upptöku sem er sem geymir bæði breiddar-/lengdargráðu
og DCS-metra, til dæmis 3DHeat Watcher lotu af einu flugi.

1. Taktu upp flug á leiksvæðinu með 3DHeat Watcher (eða gerðu hvaða
   upptöku sem er með dálkana `lat`, `lon`, `x`, `z` í DCS-metrum: x er metrar
   til norðurs, z metrar til austurs, eins og alls staðar í DCS).
2. Keyrðu `heat3d-dcs-maps fit "<session>/heat.parquet"` (eða `.jsonl` eða `.csv`).
3. Það prentar fittuðu vörpunina sem JSON, kvaðratmeðaltalsskekkjuna (root mean
   square error) yfir punktana, og `--projection` færibreyturnar sem á að nota.
4. Smíðaðu borðið með þeim:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit á gerviupptöku](../assets/img/fit.svg)

Upptakan á myndinni eru níu punktar búnir til úr þekktri vörpun,
sem `fit` finnur aftur upp á millimetra.

| Færibreyta | Gerir |
|---|---|
| `recording` | `.parquet`, `.jsonl` eða `.csv` með dálkunum `lat`, `lon`, `x`, `z` (DCS-metrar); raðir sem ekki lesast eru sniðgengnar |

Vörpunin er Krüger-röð eins og C. F. F. Karney gefur hana ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Útgöngustaða: 0 góð passun (undir 5 m kvaðratmeðaltal); 1 léleg passun, eða
færri en þrjár nothæfar raðir; 2 skráin fannst ekki.
