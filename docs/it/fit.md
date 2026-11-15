---
title: "Proiezioni: fit"
nav_order: 6
lang: "it"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Proiezioni: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <registrazione>
```

Ogni teatro è una proiezione di Mercatore trasversa con le sue costanti. Lo strumento le conosce per
i teatri su cui è stato verificato; per uno che non conosce, `fit` le trova da una qualsiasi
registrazione che contenga sia latitudine/longitudine sia metri DCS, come una sessione di 3DHeat
Watcher di un solo volo.

1. Registra un volo sul teatro con 3DHeat Watcher (oppure crea una registrazione qualsiasi con le
   colonne `lat`, `lon`, `x`, `z` in metri DCS: x sono metri verso nord, z metri verso est, come in
   tutto DCS).
2. Esegui `heat3d-dcs-maps fit "<sessione>/heat.parquet"` (oppure un file `.jsonl` o `.csv`).
3. Stampa la proiezione trovata come JSON, l'errore quadratico medio sui punti, e gli argomenti
   `--projection` da usare.
4. Costruisci il livello con quelli:
   `heat3d-dcs-maps level <teatro> --projection <LON0> <FE> <FN> -o levels`.

![fit su una registrazione sintetica](../assets/img/fit.svg)

La registrazione nell'immagine è composta da nove punti creati da una proiezione nota, che `fit`
ritrova fino al millimetro.

| Argomento | Cosa fa |
|---|---|
| `recording` | `.parquet`, `.jsonl` o `.csv` con le colonne `lat`, `lon`, `x`, `z` (metri DCS); le righe che non si leggono vengono saltate |

La proiezione è la serie di Krüger come la dà C. F. F. Karney ("Transverse Mercator with an
accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Stato di uscita: 0 un buon adattamento (sotto 5 m di errore quadratico medio); 1 un adattamento
scarso, o meno di tre righe utilizzabili; 2 il file non è stato trovato.
