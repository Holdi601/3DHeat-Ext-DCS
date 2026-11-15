---
title: "Mielőtt elkezded"
nav_order: 1.5
lang: hu
source: before-you-start.md
source_hash: "64346abe88e5"
nav_exclude: true
search_exclude: true
---
# Mielőtt elkezded {#before-you-start}

Még nem használt parancssort? Ez az oldal a semmitől az első futtatásig vezet el.
Egyszer tart, nagyjából tíz percig.

## 1. Telepítsd a Pythont {#install-python}

Ehhez az eszközhöz **Python 3.10 vagy újabb** kell.

- **Windows:** töltsd le a Pythont a [python.org/downloads](https://www.python.org/downloads/)
  oldalról, és futtasd a telepítőt. Az első képernyőn pipáld be a **Add python.exe to PATH**
  lehetőséget, majd kattints az **Install Now** gombra.
- **macOS és Linux:** a Python 3 gyakran már fent van. Ahol ezek az oldalak `python`-t írnak,
  ott gépeld be a `python3`-at.

## 2. Szerezd meg ezt az eszközt {#get-this-tool}

Nyisd meg a [github.com/Holdi601/3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS)
oldalt, kattints a zöld **Code** gombra, majd a **Download ZIP** lehetőségre, és csomagold
ki egy tetszőleges mappába. Ha git-et használsz: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`.

## 3. Nyiss terminált abban a mappában {#open-a-terminal-in-that-folder}

A terminál olyan ablak, ahová parancsokat gépelsz.

- **Windows:** nyisd meg a mappát a Fájlkezelőben, kattints a címsorba, gépeld be
  a `powershell`-t, és nyomj Entert. Egy kék vagy fekete ablak nyílik meg, már abban a
  mappában.
- **macOS:** nyisd meg a **Terminal** alkalmazást, gépeld be a `cd `-t (szóközzel), húzd
  a mappát az ablakba, és nyomj Entert.

A `cd` azt jelenti: „mappát vált”. A `cd C:\Tools\3DHeat-Ext-DCS` ebbe a mappába visz.

## 4. Telepítsd az eszközt {#install-the-tool}

Gépeld be ezt, és nyomj Entert:

```bash
python -m pip install -e .
```

A végén ezt kell látnod: `Successfully installed heat3d-ext-dcs-...`.

## 5. Futtasd {#run-it}

```bash
heat3d-dcs-maps list
```

Valami ilyesmit kell látnod:

```text
DCS World at C:\Games\DCS World
  <theatre>    <n> GB    <n> tiles    <n> M vertices  lat/lon    readable
```

Következő: [Színházak keresése: list](list.md), majd [Pálya építése: level](level.md).

## Hogyan olvasd a parancsokat ezeken az oldalakon {#how-to-read-the-commands-on-these-pages}

| Amit látsz | Jelentése |
|---|---|
| `<folder>` | helyőrző: írd be a saját értékedet, a `< >` jelek nélkül |
| `[--force]` | nem kötelező: hagyd ki, vagy írd be úgy, ahogy látod |
| `a\|b` | választás: írd be az `a`-t vagy a `b`-t |
| `# a note` | megjegyzés neked: ne írd be |
| `"C:\My Files\x"` | a szóközöket tartalmazó útvonalat tedd idézőjelek közé |
| `D:\Demos` | példa Windows-mappa: használd a sajátodat |

## Ha valami nem jól működik {#when-something-goes-wrong}

| Az üzenet | Mit tegyél |
|---|---|
| `'python' is not recognized` | A Python nincs telepítve, vagy nem volt bepipálva a PATH mező: telepítsd újra, és pipáld be (vagy `python` helyett írd be a `py`-t). |
| `'heat3d-dcs-maps' is not recognized` | Futtasd újra a 4. lépést az eszköz mappájában, vagy a `heat3d-dcs-maps` helyett írd be a `python -m heat3d_ext_dcs`-t: ugyanazt csinálja. |
| `No module named heat3d_ext_dcs` | Nem az eszköz mappájában vagy, vagy a 4. lépés nem sikerült: lépj oda a `cd` paranccsal, és futtasd a 4. lépést. |
| `No module named pip` | Futtasd a `python -m ensurepip` parancsot, majd a 4. lépést. |
| minden más | Olvasd el az üzenet utolsó sorát, és nyiss róla egy hibajegyet (issue) a GitHubon. |

Minden parancs egy **kilépési állapottal** (exit status) is végződik: a 0 azt jelenti, hogy
sikerült. Ennek megtekintéséhez gépeld be az `echo $LASTEXITCODE` parancsot PowerShellben,
vagy az `echo $?` parancsot macOS-en és Linuxon.
