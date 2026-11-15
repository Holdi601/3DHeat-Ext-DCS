---
title: "Projektsioonid: fit"
nav_order: 6
lang: et
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projektsioonid: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Iga teater on Transverse Mercatori projektsioon oma konstantidega. Tööriist teab neid
teatrite puhul, mille peal see on kontrollitud; kui teatrit ei tunta, leiab `fit` need
iga salvestuse põhjal, mis sisaldab nii laiuskraadi/pikkuskraadi kui ka DCS-i meetreid,
näiteks ühe lennu 3DHeat Watcheri seanssi.

1. Salvesta lend teatril 3DHeat Watcheriga (või tee mis tahes salvestus veergudega `lat`, `lon`, `x`, `z` DCS-i meetrites: x on meetrit põhja, z meetrit ida, nagu kõikjal DCS-is).
2. Käivita `heat3d-dcs-maps fit "<session>/heat.parquet"` (või `.jsonl` või `.csv`).
3. See prindib sobitatud projektsiooni JSON-ina, punktide ruutkeskmise vea ja argumendid `--projection`, mida kasutada.
4. Ehita nendega tase:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit sünteetilisel salvestusel](../assets/img/fit.svg)

Pildil olev salvestus on üheksa punkti, mis on tehtud teadaolevast projektsioonist;
`fit` leiab selle tagasi millimeetri täpsusega.

| Argument | Teeb |
|---|---|
| `recording` | `.parquet`, `.jsonl` või `.csv` veergudega `lat`, `lon`, `x`, `z` (DCS-i meetrites); read, mida ei saa lugeda, jäetakse vahele |

Projektsioon on Krügeri rida, nagu seda annab C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Väljumisolek: 0 hea sobitus (alla 5 m ruutkeskmise vea); 1 halb sobitus või
alla kolme kasutatava rea; 2 faili ei leitud.
