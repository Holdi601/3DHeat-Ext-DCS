---
title: "Budowanie poziomu: level"
nav_order: 3
lang: "pl"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Budowanie poziomu: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Krok po kroku {#step-by-step}

Nigdy nie używałeś wiersza poleceń? Najpierw przeczytaj [Zanim zaczniesz](before-you-start.md).

1. Znajdź nazwę folderu teatru poleceniem [`list`](list.md).
2. Dla małego teatru zbuduj go w całości: `heat3d-dcs-maps level <theatre> -o levels`.
3. Dla dużego wybierz region: `--around <lat> <lon> <km>` (kwadrat tylu km w każdą stronę od punktu)
   albo `--bounds X0 Z0 X1 Z1` w metrach DCS. Nazwij go opcją `--name`.
4. Polecenie wypisuje kafle, gdy je odczytuje, liczbę trójkątów, zapisany plik
   oraz to, ile miast teatru trafia na ziemię - sprawdzenie projekcji, które powinno
   pokazać „N z N”.
5. Wczytaj `<folder>/<name>.glb` w panelu **Tło / poziom** przeglądarki i włącz
   **Zarejestrowany kolor**, aby zobaczyć klasy terenu.

![level na syntetycznej instalacji](../assets/img/level.svg)

Region tego samego syntetycznego teatru, w metrach DCS:

![level z --bounds i --name](../assets/img/level-bounds.svg)

## Opcje {#options}

| Opcja | Domyślnie | Co robi |
|---|---|---|
| `theatre` | - | nazwa folderu w `Mods\terrains`, tak jak wypisuje ją `list` (dowolna wielkość liter) |
| `-o`, `--out` | wymagane | folder, do którego zapisać `<name>.glb` i `<name>.json` |
| `--dcs FOLDER` | znajdowany | folder DCS World ([gdzie jest szukany](list.md#where-the-install-is-found)) |
| `--name NAME` | nazwa teatru | nazwa poziomu i jego plików |
| `--around LAT LON KM` | - | tylko kwadrat tylu km w każdą stronę od punktu |
| `--bounds X0 Z0 X1 Z1` | - | tylko ten prostokąt, w metrach DCS (x na północ, z na wschód) |
| `--cell M` | `0` | przerzedza siatkę: każdy wierzchołek w odległości *M* metrów staje się jednym (0: własne trójkąty gry) |
| `--seabed` | wyłączone | zachowuje dno morskie jako teren (domyślnie jest pomijane) |
| `--no-water` | wyłączone | pomija płaskie morze |
| `--no-buildings` | wyłączone | pomija budynki ze sceny teatru |
| `--force` | wyłączone | eksportuje bardzo dużą mapę w całości, w pełnym detalu |
| `--projection LON0 FE FN` | teatru | stałe Transverse Mercator dla teatru, którego to narzędzie nie zna ([fit](fit.md)) |

Każda opcja, tak jak ją wypisuje program: [Opis poleceń](../cli-reference.md).

## Rozmiar {#size}

Siatka gry jest adaptacyjna - otwarte morze to trójkąty o kilometrowych bokach,
a wybrzeża i drogi o kilkumetrowych. Mały teatr to kilka milionów trójkątów; duże mają dziesiątki
milionów wierzchołków. Powyżej 30 milionów wierzchołków do odczytania `level` się zatrzymuje
(kod wyjścia 1) i prosi o region, rzadszą siatkę (`--cell 50`) albo `--force`.

Kod wyjścia: 0 gotowe; 1 nie udało się albo jest za duże; 2 nie znaleziono instalacji lub teatru
(wypisywane są znalezione teatry).

## Przykłady {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # cały, w pełnym detalu
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # kwadrat 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # prostokąt w metrach DCS
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # cały, przerzedzony do 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # sam teren
```

Co jest w plikach: [Pliki poziomu](output.md).
