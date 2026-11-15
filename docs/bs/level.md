---
title: "Gradnja nivoa: level"
nav_order: 3
lang: bs
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Gradnja nivoa: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Korak po korak {#step-by-step}

Komandna linija ti je nova? Prvo pročitaj [Prije nego počneš](before-you-start.md).

1. Nađi naziv foldera teatra pomoću [`list`](list.md).
2. Za mali teatar izgradi ga cijelog: `heat3d-dcs-maps level <theatre> -o levels`.
3. Za veliki odaberi regiju: `--around <lat> <lon> <km>` (kvadrat koji se
   toliko km proteže na svaku stranu od tačke) ili `--bounds X0 Z0 X1 Z1` u DCS metrima.
   Imenuj je pomoću `--name`.
4. Naredba ispisuje pločice (tiles) dok ih čita, broj trouglova,
   napisanu datoteku i koliko gradova teatra pada na tlo - provjeru
   projekcije koja bi trebala glasiti "N of N".
5. Učitaj `<folder>/<name>.glb` u panelu Pozadina / nivo preglednika i uključi
   **Snimljena boja** da vidiš klase tla.

![level na sintetičkoj instalaciji](../assets/img/level.svg)

Regija istog sintetičkog teatra, po DCS metrima:

![level s --bounds i --name](../assets/img/level-bounds.svg)

## Opcije {#options}

| Opcija | Zadano | Radi |
|---|---|---|
| `theatre` | - | naziv foldera pod `Mods\terrains`, kako ga ispisuje `list` (bilo koja velika/mala slova) |
| `-o`, `--out` | obavezno | folder u koji se pišu `<name>.glb` i `<name>.json` |
| `--dcs FOLDER` | pronađeno | folder DCS Worlda ([gdje se nalazi](list.md#where-the-install-is-found)) |
| `--name NAME` | naziv teatra | ime nivoa i njegovih datoteka |
| `--around LAT LON KM` | - | samo kvadrat koji se toliko km proteže na svaku stranu od tačke |
| `--bounds X0 Z0 X1 Z1` | - | samo ovaj okvir, u DCS metrima (x sjever, z istok) |
| `--cell M` | `0` | prorijedi mrežu: svaki vrh unutar *M* metara postaje jedan (0: vlastiti trouglovi igre) |
| `--seabed` | isključeno | zadrži morsko dno kao tlo (zadano se izostavlja) |
| `--no-water` | isključeno | izostavi ravno more |
| `--no-buildings` | isključeno | izostavi zgrade scene teatra |
| `--force` | isključeno | izvezi vrlo veliku mapu cijelu u punom detalju |
| `--projection LON0 FE FN` | od teatra | Transverse Mercator konstante za teatar koji ovaj alat ne zna ([fit](fit.md)) |

Sve opcije, onako kako ih program ispisuje: [Referenca naredbi](../cli-reference.md).

## Veličina {#size}

Mreža igre je prilagodljiva - otvoreno more u trouglovima širokim kilometrima, obale
i ceste u nekoliko metara. Mali teatar ima nekoliko miliona trouglova; veliki
imaju desetine miliona vrhova. Iznad 30 miliona vrhova za čitanje `level`
staje (izlazni status 1) i traži regiju, rjeđu mrežu (`--cell 50`) ili
`--force`.

Izlazni status: 0 gotovo; 1 neuspjeh ili preveliko; 2 instalacija ili teatar
nisu pronađeni (pronađeni teatri su navedeni).

## Primjeri {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Šta je u datotekama: [Datoteke nivoa](output.md).
