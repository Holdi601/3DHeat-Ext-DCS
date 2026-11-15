---
title: "Lygio kūrimas: level"
nav_order: 3
lang: "lt"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Lygio kūrimas: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Žingsnis po žingsnio {#step-by-step}

Nesate įpratę prie komandinės eilutės? Pirmiausia perskaitykite [Prieš pradedant](before-you-start.md).

1. Raskite teatro aplanko pavadinimą su [`list`](list.md).
2. Mažam teatrui sukurkite jį visą: `heat3d-dcs-maps level <theatre> -o levels`.
3. Dideliam pasirinkite regioną: `--around <lat> <lon> <km>` (kvadratas tiek km į abi puses nuo taško)
   arba `--bounds X0 Z0 X1 Z1` DCS metrais. Pavadinkite jį `--name`.
4. Komanda rodo plytelės, kai jas skaito, trikampių skaičių, įrašytą failą ir kiek teatro miestų
   patenka ant žemės – projekcijos patikrinimas, kuris turėtų rodyti „N iš N“.
5. Įkelkite `<folder>/<name>.glb` žiūryklės Lygio skydelyje ir įjunkite **Captured colour**, kad matytumėte žemės klases.

![level ant sintetinio įdiegimo](../assets/img/level.svg)

To paties sintetinio teatro regionas DCS metrais:

![level su --bounds ir --name](../assets/img/level-bounds.svg)

## Parinktys {#options}

| Parinktis | Numatyta | Ką daro |
|---|---|---|
| `theatre` | - | aplanko pavadinimas `Mods\terrains` viduje, kaip rodo `list` (bet kokia raidžių forma) |
| `-o`, `--out` | privaloma | aplankas, į kurį įrašyti `<name>.glb` ir `<name>.json` |
| `--dcs FOLDER` | randama | DCS World aplankas ([kur jis randamas](list.md#where-the-install-is-found)) |
| `--name NAME` | teatro | lygio pavadinimas ir jo failų |
| `--around LAT LON KM` | - | tik kvadratas tiek km į abi puses nuo taško |
| `--bounds X0 Z0 X1 Z1` | - | tik ši dėžė DCS metrais (x – į šiaurę, z – į rytus) |
| `--cell M` | `0` | retinti tinklą: kiekviena viršūnė per *M* metrų tampa viena (0: paties žaidimo trikampiai) |
| `--seabed` | išjungta | palikti jūros dugną kaip žemę (pagal numatymą jis praleidžiamas) |
| `--no-water` | išjungta | nepaisyti plokščios jūros |
| `--no-buildings` | išjungta | nepaisyti teatro scenos pastatų |
| `--force` | išjungta | eksportuoti labai didelį žemėlapį visą pilna detale |
| `--projection LON0 FE FN` | teatro | Transverse Mercator konstantos teatrui, kurio šis įrankis nepažįsta ([fit](fit.md)) |

Kiekviena parinktis, kaip ją rodo programa: [Komandų nuoroda](../cli-reference.md).

## Dydis {#size}

Žaidimo tinklas yra adaptyvus: atviroje jūroje trikampiai kilometrų dydžio, pakrantėse ir keliuose – keli metrai.
Mažas teatras – keli milijonai trikampių; dideli – dešimtys milijonų viršūnių. Kai reikia nuskaityti daugiau nei
30 milijonų viršūnių, `level` sustoja (išeities kodas 1) ir prašo regiono, retesnio tinklo (`--cell 50`) arba `--force`.

Išeities kodas: 0 – baigta; 1 – nepavyko arba per didelis; 2 – įdiegimas ar teatras nerastas (išvardijami rasti teatrai).

## Pavyzdžiai {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # visas, pilna detale
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24 km kvadratas
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # dėžė DCS metrais
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # visas, retintas iki 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # vien žemė
```

Kas yra failuose: [Lygio failai](output.md).
