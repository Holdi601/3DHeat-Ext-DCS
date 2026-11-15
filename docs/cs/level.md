---
title: "Sestavení úrovně: level"
nav_order: 3
lang: "cs"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Sestavení úrovně: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Krok za krokem {#step-by-step}

Nikdy jste nepracovali s příkazovým řádkem? Nejdřív si přečtěte [Než začnete](before-you-start.md).

1. Zjistěte název složky území pomocí [`list`](list.md).
2. U malého území ho sestavte celé: `heat3d-dcs-maps level <theatre> -o levels`.
3. U velkého vyberte oblast: `--around <lat> <lon> <km>` (čtverec tolik km na každou stranu
   od bodu) nebo `--bounds X0 Z0 X1 Z1` v metrech DCS.
   Pojmenujte ji pomocí `--name`.
4. Příkaz vypisuje dlaždice, jak je čte, počet trojúhelníků, zapsaný soubor
   a kolik měst území leží na zemi – kontrola projekce, která by měla ukázat „N z N“.
5. Načtěte `<folder>/<name>.glb` do panelu Pozadí / úroveň v prohlížeči a zapněte
   **Zachycená barva**, abyste viděli třídy terénu.

![level na syntetické instalaci](../assets/img/level.svg)

Oblast téhož syntetického území v metrech DCS:

![level s --bounds a --name](../assets/img/level-bounds.svg)

## Možnosti {#options}

| Možnost | Výchozí | Co dělá |
|---|---|---|
| `theatre` | - | název složky pod `Mods\terrains`, tak jak ho vypisuje `list` (bez ohledu na velikost písmen) |
| `-o`, `--out` | povinné | složka, do které se zapíšou `<name>.glb` a `<name>.json` |
| `--dcs FOLDER` | nalezeno | složka DCS World ([kde se hledá](list.md#where-the-install-is-found)) |
| `--name NAME` | název území | název úrovně a jejích souborů |
| `--around LAT LON KM` | - | jen čtverec tolika km na každou stranu od bodu |
| `--bounds X0 Z0 X1 Z1` | - | jen tento kvádr v metrech DCS (x na sever, z na východ) |
| `--cell M` | `0` | proředí síť: každý vrchol do *M* metrů se stane jedním (0: trojúhelníky samotné hry) |
| `--seabed` | vypnuto | zachová mořské dno jako zemi (ve výchozím stavu se vynechá) |
| `--no-water` | vypnuto | vynechá rovnou hladinu moře |
| `--no-buildings` | vypnuto | vynechá budovy ze scény území |
| `--force` | vypnuto | vyexportuje velmi velkou mapu celou v plných detailech |
| `--projection LON0 FE FN` | území | konstanty Transverse Mercator pro území, které tento nástroj nezná ([fit](fit.md)) |

Každá možnost tak, jak ji program vypisuje: [Přehled příkazů](../cli-reference.md).

## Velikost {#size}

Síť hry je adaptivní – otevřené moře tvoří trojúhelníky o kilometrových rozměrech, pobřeží
a silnice o několika metrech. Malé území má několik milionů trojúhelníků; velká mají desítky
milionů vrcholů. Nad 30 milionů vrcholů ke čtení se `level` zastaví (stavový kód 1)
a požádá o oblast, řidší síť (`--cell 50`) nebo `--force`.

Stavový kód: 0 hotovo; 1 selhalo nebo je příliš velké; 2 instalace nebo území nebyly nalezeny
(vypíšou se nalezená území).

## Příklady {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Co je v souborech: [Soubory úrovně](output.md).
