---
title: "Szukanie teatrów: list"
nav_order: 2
lang: "pl"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Szukanie teatrów: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nigdy nie używałeś wiersza poleceń? Najpierw przeczytaj [Zanim zaczniesz](before-you-start.md).

1. Zainstaluj raz: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, otwórz
   terminal w tym folderze i uruchom `python -m pip install -e .` (Python 3.10
   lub nowszy; instaluje numpy, a dla `fit` na pliku `.parquet` także pyarrow).
2. Uruchom `heat3d-dcs-maps list`.
3. Każdy zainstalowany teatr wypisuje jedną linię: nazwę folderu (nazwę, której używają
   pozostałe polecenia), rozmiar jego pliku terenu, kafle i wierzchołki, to, czy znana jest jego
   projekcja szerokości/długości geograficznej, i to, czy się go da odczytać.
   Na końcu każdej linii powinno być `readable`.

![list na syntetycznej instalacji](../assets/img/list.svg)

Obrazek to przebieg na instalacji, którą budują testy (`tests/synth.py`), a nie na samej grze.

## Gdzie jest szukana instalacja {#where-the-install-is-found}

`--dcs <folder>` (folder zawierający `Mods\terrains`) albo zmienna środowiskowa `DCS_PATH`;
w przeciwnym razie przeszukiwany jest rejestr, biblioteki Steam i typowe foldery.

| Opcja | Co robi |
|---|---|
| `--dcs FOLDER` | folder DCS World, ten, w którym leży `Mods\terrains` |

Kod wyjścia: 0 gotowe, 2 nie znaleziono instalacji ani teatru.
