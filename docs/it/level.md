---
title: "Costruire un livello: level"
nav_order: 3
lang: "it"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Costruire un livello: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <teatro> -o <cartella> [--dcs CARTELLA] [--name NOME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Passo per passo {#step-by-step}

Non hai mai usato la riga di comando? Leggi prima [Prima di iniziare](before-you-start.md).

1. Trova il nome della cartella del teatro con [`list`](list.md).
2. Per un teatro piccolo, costruiscilo intero: `heat3d-dcs-maps level <teatro> -o levels`.
3. Per uno grande, scegli una regione: `--around <lat> <lon> <km>` (un quadrato di tanti km per
   lato da un punto) oppure `--bounds X0 Z0 X1 Z1` in metri DCS. Dagli un nome con `--name`.
4. Il comando stampa le tessere man mano che le legge, il numero dei triangoli, il file scritto, e
   quante città del teatro cadono sul terreno - un controllo della proiezione che dovrebbe dire
   "N di N".
5. Carica `<cartella>/<nome>.glb` nel pannello Sfondo / livello del visualizzatore e attiva
   **Colore acquisito** per vedere le classi di terreno.

![level su un'installazione sintetica](../assets/img/level.svg)

Una regione dello stesso teatro sintetico, in metri DCS:

![level con --bounds e --name](../assets/img/level-bounds.svg)

## Opzioni {#options}

| Opzione | Predefinito | Cosa fa |
|---|---|---|
| `theatre` | - | il nome della cartella sotto `Mods\terrains`, come lo stampa `list` (qualsiasi maiuscola o minuscola) |
| `-o`, `--out` | obbligatoria | la cartella in cui scrivere `<nome>.glb` e `<nome>.json` |
| `--dcs CARTELLA` | trovata | la cartella di DCS World ([dove viene trovata](list.md#where-the-install-is-found)) |
| `--name NOME` | quello del teatro | il nome del livello, e dei suoi file |
| `--around LAT LON KM` | - | solo un quadrato di tanti km per lato da un punto |
| `--bounds X0 Z0 X1 Z1` | - | solo questo riquadro, in metri DCS (x verso nord, z verso est) |
| `--cell M` | `0` | sfolta la maglia: ogni vertice entro *M* metri diventa uno solo (0: i triangoli stessi del gioco) |
| `--seabed` | disattivata | conserva il fondale marino come terreno (per impostazione predefinita viene lasciato fuori) |
| `--no-water` | disattivata | lascia fuori il mare piatto |
| `--no-buildings` | disattivata | lascia fuori gli edifici della scena del teatro |
| `--force` | disattivata | esporta una mappa molto grande intera, al pieno dettaglio |
| `--projection LON0 FE FN` | quella del teatro | costanti di Mercatore trasversa per un teatro che questo strumento non conosce ([fit](fit.md)) |

Ogni opzione, come la stampa il programma: [Riferimento dei comandi](../cli-reference.md).

## Dimensione {#size}

La maglia del gioco è adattiva: il mare aperto in triangoli di chilometri, coste e strade in pochi
metri. Un teatro piccolo sono alcuni milioni di triangoli; quelli grandi sono decine di milioni di
vertici. Sopra i 30 milioni di vertici da leggere, `level` si ferma (stato di uscita 1) e chiede una
regione, una maglia più sottile (`--cell 50`) o `--force`.

Stato di uscita: 0 fatto; 1 fallito o troppo grande; 2 l'installazione o il teatro non sono stati
trovati (vengono elencati i teatri trovati).

## Esempi {#examples}

```bash
heat3d-dcs-maps level <teatro> -o levels                                       # intero, pieno dettaglio
heat3d-dcs-maps level <teatro> --around <lat> <lon> 12 -o levels --name Parte  # un quadrato da 24 km
heat3d-dcs-maps level <teatro> --bounds 1000 2000 1390 2390 -o levels          # un riquadro in metri DCS
heat3d-dcs-maps level <teatro> --cell 50 -o levels                             # intero, sfoltito a 50 m
heat3d-dcs-maps level <teatro> --no-buildings --no-water -o levels             # solo il terreno
```

Cosa c'è nei file: [I file del livello](output.md).
