---
title: "Warunki i licencja"
nav_order: 8
lang: "pl"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Warunki i licencja {#terms-and-licence}

## Co czyta czytnik {#what-the-reader-reads}

Czytnik odczytuje pliki danych twojej własnej instalacji DCS World na twoim komputerze ([Jak czytane są pliki](reading.md)). Niczego nie zmienia w grze i nie łączy się z żadnym serwerem.

Nic z gry nie jest dołączane ani rozpowszechniane: żadnych plików gry, żadnego kodu gry, żadnych bibliotek DLL; testy same budują każdy plik, który czytają. Zapisane poziomy zostają na twoim komputerze.

3DHeat DCS nie jest powiązany z Eagle Dynamics ani przez nią wspierany. DCS World oraz powiązane nazwy i znaki towarowe należą do ich właścicieli.

Właściciele praw: otwórzcie zgłoszenie pod adresem [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odpowiadamy szybko i na prośbę usuwamy wszystko.

## Licencja i źródła {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Wymaga numpy (BSD-3-Clause); `fit` na pliku
`.parquet` wymaga pyarrow (Apache-2.0). Napisane na potrzeby tego projektu. Stałe projekcji to fakty opublikowane przez pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); wzięto tylko liczby. Projekcja to szereg Krügera w ujęciu
C. F. F. Karneya („Transverse Mercator with an accuracy of a few nanometers”, Journal of
Geodesy 85, 2011). Żaden kod nie został wzięty z żadnego innego projektu.
