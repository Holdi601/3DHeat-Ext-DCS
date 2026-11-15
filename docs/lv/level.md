---
title: "Līmeņa veidošana: level"
nav_order: 3
lang: lv
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Līmeņa veidošana: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Soli pa solim {#step-by-step}

Nekad nav strādāts ar komandrindu? Vispirms izlasi [Pirms sākat](before-you-start.md).

1. Atrodi teātra mapes nosaukumu ar [`list`](list.md).
2. Mazam teātrim izveido visu: `heat3d-dcs-maps level <theatre> -o levels`.
3. Lielam izvēlies reģionu: `--around <lat> <lon> <km>` (kvadrāts, cik km uz katru pusi no punkta) vai `--bounds X0 Z0 X1 Z1` DCS metros. Nosauc to ar `--name`.
4. Komanda izdrukā trīsstūrus, kad tos nolasa, trijstūru skaitu, saglabāto failu un to, cik no teātra pilsētām nokrīt uz zemes - projekcijas pārbaude, kurai vajadzētu rādīt "N no N".
5. Ielādē `<folder>/<name>.glb` skatītāja Līmeņa panelī un ieslēdz **Captured colour**, lai redzētu zemes klases.

![level uz sintētiska uzstādījuma](../assets/img/level.svg)

Tā paša sintētiskā teātra reģions DCS metros:

![level ar --bounds un --name](../assets/img/level-bounds.svg)

## Iespējas {#options}

| Iespēja | Noklusējums | Ko dara |
|---|---|---|
| `theatre` | - | mapes nosaukums zem `Mods\terrains`, kā to izdrukā `list` (jebkurš reģistrs) |
| `-o`, `--out` | obligāta | mape, kurā rakstīt `<name>.glb` un `<name>.json` |
| `--dcs FOLDER` | atrasts | DCS World mape ([kur tā tiek atrasta](list.md#where-the-install-is-found)) |
| `--name NAME` | teātra | līmeņa nosaukums un tā failu nosaukumi |
| `--around LAT LON KM` | - | tikai kvadrāts, cik km uz katru pusi no punkta |
| `--bounds X0 Z0 X1 Z1` | - | tikai šī kaste DCS metros (x ziemeļi, z austrumi) |
| `--cell M` | `0` | retināt tīklu: katrs virsotnes punkts, kas atrodas tuvāk par *M* metriem, kļūst par vienu (0: spēles pašu trijstūri) |
| `--seabed` | izslēgts | paturēt jūras dibenu kā zemi (pēc noklusējuma tas tiek izlaists) |
| `--no-water` | izslēgts | izlaist plakano jūru |
| `--no-buildings` | izslēgts | izlaist teātra skatuves ēkas |
| `--force` | izslēgts | eksportēt ļoti lielu karti veselu pilnā detalizācijā |
| `--projection LON0 FE FN` | teātra | Transversālā Merkatora konstantes teātrim, ko šis rīks nezina ([fit](fit.md)) |

Visas iespējas, kā tās izdrukā programma: [Komandu atsauce](../cli-reference.md).

## Izmērs {#size}

Spēles tīkls ir adaptīvs - atklāta jūra trijstūros, kas ir kilometrus lieli, krasti un ceļi dažu metru lielumā. Mazs teātris ir dažus miljonus trijstūru; lielie ir desmitiem miljonu virsotņu. Ja nolasāmas virsotnes ir vairāk nekā 30 miljoni, `level` apstājas (izejas statuss 1) un prasa reģionu, retāku tīklu (`--cell 50`) vai `--force`.

Izejas statuss: 0 pabeigts; 1 neizdevās vai pārāk liels; 2 uzstādījums vai teātris nav atrasts (tiek parādīti atrastie teātri).

## Piemēri {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # viss, pilna detalizācija
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24 km kvadrāts
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # kaste DCS metros
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # viss, retināts līdz 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # tikai zeme
```

Kas ir failos: [Līmeņa faili](output.md).
