---
title: "Izrada razine: level"
nav_order: 3
lang: hr
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Izrada razine: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Korak po korak {#step-by-step}

Ne znate ništa o naredbenom retku? Prvo pročitajte [Prije nego što počnete](before-you-start.md).

1. Pronađite ime mape karte pomoću [`list`](list.md).
2. Za malu kartu izradite je cijelu: `heat3d-dcs-maps level <theatre> -o levels`.
3. Za veliku odaberite regiju: `--around <lat> <lon> <km>` (kvadrat toliko km na obje strane točke) ili `--bounds X0 Z0 X1 Z1` u DCS metrima. Imenujte je s `--name`.
4. Naredba ispisuje pločice dok ih čita, broj trokuta, datoteku koja je zapisana i koliko gradova karte leži na tlu - provjera projekcije na kojoj piše "N od N".
5. Učitajte `<folder>/<name>.glb` u panel Pozadina / razina preglednika i uključite **Snimljena boja** da vidite klase tla.

![razina na sintetičkoj instalaciji](../assets/img/level.svg)

Regija iste sintetičke karte, u DCS metrima:

![razina s --bounds i --name](../assets/img/level-bounds.svg)

## Opcije {#options}

| Opcija | Zadano | Što radi |
|---|---|---|
| `theatre` | - | ime mape pod `Mods\terrains`, kako ga ispisuje `list` (bilo koje velike ili male slove) |
| `-o`, `--out` | obavezno | mapa u koju se pišu `<name>.glb` i `<name>.json` |
| `--dcs FOLDER` | pronađeno | mapa DCS Worlda ([gdje se nalazi](list.md#where-the-install-is-found)) |
| `--name NAME` | ime karte | ime razine i njezinih datoteka |
| `--around LAT LON KM` | - | samo kvadrat toliko km na obje strane točke |
| `--bounds X0 Z0 X1 Z1` | - | samo ovaj okvir, u DCS metrima (x sjever, z istok) |
| `--cell M` | `0` | prorijedi mrežu: svaki vrh unutar *M* metara postaje jedan (0: vlastiti trokuti igre) |
| `--seabed` | isključeno | zadrži morsko dno kao tlo (inače se izostavlja) |
| `--no-water` | isključeno | izostavi ravno more |
| `--no-buildings` | isključeno | izostavi zgrade iz scene karte |
| `--force` | isključeno | izvezi vrlo veliku kartu cijelu, u punoj razini detalja |
| `--projection LON0 FE FN` | karte | konstante Transverzalne Mercatorove projekcije za kartu koju ovaj alat ne poznaje ([fit](fit.md)) |

Svaka opcija, onako kako je program ispisuje: [Referenca naredbi](../cli-reference.md).

## Veličina {#size}

Igrina mreža je prilagodljiva - otvoreno more u trokutima dugim kilometrima, obale i ceste u nekoliko metara. Mala karta ima nekoliko milijuna trokuta; velike imaju desetke milijuna vrhova. Iznad 30 milijuna vrhova za čitanje `level` staje (izlazni status 1) i traži regiju, rjeđu mrežu (`--cell 50`) ili `--force`.

Izlazni status: 0 gotovo; 1 neuspjeh ili prevelika; 2 instalacija ili karta nije pronađena (ispisuju se pronađene karte).

## Primjeri {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # cijela, puni detalj
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # kvadrat od 24 km
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # okvir u DCS metrima
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # cijela, prorijeđena na 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # samo tlo
```

Što je u datotekama: [Datoteke razine](output.md).
