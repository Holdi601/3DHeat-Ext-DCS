---
title: Prima di iniziare
nav_order: 1.5
lang: "it"
source: before-you-start.md
source_hash: "64346abe88e5"
nav_exclude: true
search_exclude: true
---
# Prima di iniziare {#before-you-start}

Non hai mai usato la riga di comando? Questa pagina ti porta dal nulla a una prima esecuzione.
Richiede circa dieci minuti, una volta sola.

## 1. Installa Python {#install-python}

Questo strumento richiede **Python 3.10 o successivo**.

- **Windows:** scarica Python da [python.org/downloads](https://www.python.org/downloads/)
  ed esegui il programma di installazione. Nella prima schermata spunta **Add python.exe to PATH**,
  poi clicca su **Install Now**.
- **macOS e Linux:** Python 3 è spesso già presente. Dove queste pagine scrivono `python`,
  digita `python3`.

## 2. Scarica questo strumento {#get-this-tool}

Apri [github.com/Holdi601/3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS), clicca sul
pulsante verde **Code**, poi su **Download ZIP**, e decomprimilo in una cartella a tua scelta.
Se usi git: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`.

## 3. Apri un terminale in quella cartella {#open-a-terminal-in-that-folder}

Un terminale è una finestra in cui digiti i comandi.

- **Windows:** apri la cartella in Esplora file, clicca nella barra degli indirizzi, digita
  `powershell` e premi Invio. Si apre una finestra blu o nera, già posizionata in quella cartella.
- **macOS:** apri **Terminale**, digita `cd ` (con uno spazio), trascina la cartella nella
  finestra e premi Invio.

`cd` significa "cambia cartella": `cd C:\Tools\3DHeat-Ext-DCS` va in quella cartella.

## 4. Installa lo strumento {#install-the-tool}

Digita questo e premi Invio:

```bash
python -m pip install -e .
```

Alla fine dovresti vedere: `Successfully installed heat3d-ext-dcs-...`.

## 5. Eseguilo {#run-it}

```bash
heat3d-dcs-maps list
```

Dovresti vedere qualcosa come:

```text
DCS World at C:\Games\DCS World
  <theatre>    <n> GB    <n> tiles    <n> M vertices  lat/lon    readable
```

Poi: [Trovare i teatri: list](list.md), quindi [Costruire un livello: level](level.md).

## Come leggere i comandi di queste pagine {#how-to-read-the-commands-on-these-pages}

| Cosa vedi | Significa |
|---|---|
| `<folder>` | un segnaposto: al suo posto scrivi il tuo valore, senza i `< >` |
| `[--force]` | facoltativo: omettilo, oppure scrivilo come mostrato |
| `a\|b` | una scelta: scrivi `a` oppure `b` |
| `# a note` | un commento per te: non va digitato |
| `"C:\My Files\x"` | scrivi un percorso con spazi tra virgolette |
| `D:\Demos` | un esempio di cartella Windows: usa la tua |

## Quando qualcosa non va {#when-something-goes-wrong}

| Il messaggio | Cosa fare |
|---|---|
| `'python' is not recognized` | Python non è installato, oppure non è stata spuntata la casella PATH: installalo di nuovo e spuntala (oppure scrivi `py` invece di `python`). |
| `'heat3d-dcs-maps' is not recognized` | Esegui di nuovo il passo 4 nella cartella dello strumento, oppure scrivi `python -m heat3d_ext_dcs` al posto di `heat3d-dcs-maps`: fa la stessa cosa. |
| `No module named heat3d_ext_dcs` | Non sei nella cartella dello strumento, oppure il passo 4 non è riuscito: entra lì con `cd` ed esegui il passo 4. |
| `No module named pip` | Esegui `python -m ensurepip`, poi il passo 4. |
| qualsiasi altro messaggio | Leggi l'ultima riga del messaggio, poi apri una segnalazione su GitHub con quella riga. |

Ogni comando termina anche con uno **stato di uscita**: 0 significa che ha funzionato. Per vederlo,
digita `echo $LASTEXITCODE` in PowerShell oppure `echo $?` su macOS e Linux.
