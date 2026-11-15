---
title: "Trovare i teatri: list"
nav_order: 2
lang: "it"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Trovare i teatri: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs CARTELLA]
```

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).

1. Installa una volta sola: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, apri un
   terminale in quella cartella ed esegui `python -m pip install -e .` (Python 3.10 o successivo;
   porta con sé numpy, e pyarrow per `fit` su un `.parquet`).
2. Esegui `heat3d-dcs-maps list`.
3. Ogni teatro installato stampa una riga: il nome della sua cartella (il nome che accettano gli
   altri comandi), la dimensione del suo file del terreno, le sue tessere e i suoi vertici, se la
   sua proiezione di latitudine/longitudine è nota, e se può essere letto. Dovresti vedere
   `readable` alla fine di ogni riga.

![list su un'installazione sintetica](../assets/img/list.svg)

L'immagine è un'esecuzione su un'installazione creata dai test (`tests/synth.py`), non sul gioco.

## Dove viene trovata l'installazione {#where-the-install-is-found}

`--dcs <cartella>` (la cartella che contiene `Mods\terrains`) oppure la variabile d'ambiente
`DCS_PATH`; altrimenti vengono cercati il registro di sistema, le librerie di Steam e le cartelle
abituali.

| Opzione | Cosa fa |
|---|---|
| `--dcs CARTELLA` | la cartella di DCS World, quella che contiene `Mods\terrains` |

Stato di uscita: 0 fatto, 2 nessuna installazione o nessun teatro trovato.
