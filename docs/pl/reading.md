---
title: "Jak czytane są pliki"
nav_order: 7
lang: "pl"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Jak czytane są pliki {#how-the-files-are-read}

Tylko `Mods/terrains/<theatre>/surface/*.surface5` (siatka terenu),
`Scenes/*.scn5` (gdzie stoją obiekty i pudełko każdego modelu),
`AirfieldsTaxiways/*.rn4` oraz `map/towns.lua` (nazwy miejsc, czytane jako tekst,
nigdy nieuruchamiane). Nie czyta się zaszyfrowanego
`terrain.cfg.lua.pak.crypt`, nie `manifest.bin` i niczego z samego programu.

Format `.surface5` nie jest udokumentowany; jego układ, odczytany z plików, jest opisany w
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Krótko: indeks rekordów kafli (przekształcenie, granice i listy typowanych strumieni bajtów, a po każdej liście
shader i materiał, którymi jest rysowana), a potem surowe dane. Nie jest skompresowany ani zaszyfrowany. Strumień
`Pbase` kafla niesie jego wierzchołki; grupa rysowana jako `Land` niesie trójkąty i `TRITYPE` dla każdego trójkąta,
którego najmłodszy bit oznacza morze; pozostałe grupy to nakładki, które dają wyżej wymienione klasy.

## Sprawdzone {#verified}

- `list` odczytał indeks każdego zainstalowanego teatru (od milionów do dziesiątek milionów wierzchołków terenu każdy),
  a każdy próbkowany kafel zdekodował się do wiarygodnych metrów.
- Na regionach dwóch teatrów miasta z `towns.lua` trafiły w odległości metrów od wierzchołka terenu,
  na lądzie, „N z N”; najwyższy teren pasował do prawdziwego szczytu z dokładnością do dziesięciu metrów;
  lotniska, rzeki, wsie i drogi pokazały się w swoich klasach. Oba poziomy wczytały się w przeglądarce, a znaczniki
  miast we współrzędnych metrów DCS leżały na ziemi.
- Na regionie sceny umieszczenia budynków trafiły na swój teren; światła pasa startowego odtworzyły pas gry,
  a wagony i odcinki murów ustawiły się zgodnie z odczytanym kierunkiem - wszystkie.
- `tests/` buduje pliki `.surface5` w tym samym układzie, więc żadne dane gry nie są tu przechowywane;
  `tests/test_real_install.py` działa na instalacji komputera, na którym uruchamiane są testy, i jest pomijany bez niej.

**Nie sprawdzono:** całego dużego teatru w jednym poziomie (zabezpieczenie rozmiaru powyżej istnieje z powodu),
oraz wersji DCS innych niż ta, na której próbowano.

## Nieodczytane {#not-read}

- **Budynki jako kształty** (modele to `.edm` w `Models/`): tylko pudełka, celowo. Ich układ oraz układ sceny
  są opisane w [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  odczytuje je każdy zainstalowany teatr (dwa starsze teatry w wariancie układu, który czytnik też zna).
- Drzewa, światła i pozostałe obiekty sceny: odczytane, nie rysowane.
- **Sieć dróg jako graf** (`roads/*.rn4`): nie zdekodowana.
- Tekstury, drzewa, fale morza, niższe poziomy szczegółowości terenu samego w sobie.
