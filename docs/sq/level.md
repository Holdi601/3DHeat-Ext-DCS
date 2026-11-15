---
title: "Ndërtimi i një niveli: level"
nav_order: 3
lang: sq
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Ndërtimi i një niveli: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Hap pas hapi {#step-by-step}

Je i ri me rreshtin e komandave? Lexo së pari [Para se të fillosh](before-you-start.md).

1. Gjej emrin e dosjes së teatrit me [`list`](list.md).
2. Për një teatër të vogël, ndërtoje të tërin: `heat3d-dcs-maps level <theatre> -o levels`.
3. Për një të madh, zgjidh një rajon: `--around <lat> <lon> <km>` (një katror aq
   km në çdo anë të një pike) ose `--bounds X0 Z0 X1 Z1` në metra DCS.
   Emërtoje me `--name`.
4. Komanda shtyp pllakat ndërsa i lexon, numrin e trekëndëshave, skedarin
   e shkruar, dhe sa nga qytetet e teatrit bien mbi tokë - një kontroll
   i projeksionit që duhet të lexohet "N of N".
5. Ngarko `<folder>/<name>.glb` te paneli Sfondi / niveli i shikuesit dhe aktivizo
   **Ngjyra e kapur** për të parë klasat e tokës.

![level mbi një instalim sintetik](../assets/img/level.svg)

Një rajon i të njëjtit teatër sintetik, sipas metrave DCS:

![level me --bounds dhe --name](../assets/img/level-bounds.svg)

## Opsionet {#options}

| Opsioni | Parazgjedhja | Çfarë bën |
|---|---|---|
| `theatre` | - | emri i dosjes nën `Mods\terrains`, siç e shtyp `list` (çdo shkronjë e madhe ose e vogël) |
| `-o`, `--out` | i detyrueshëm | dosja ku shkruhen `<name>.glb` dhe `<name>.json` |
| `--dcs FOLDER` | gjendet | dosja e DCS World ([ku gjendet](list.md#where-the-install-is-found)) |
| `--name NAME` | ai i teatrit | emri i nivelit, dhe i skedarëve të tij |
| `--around LAT LON KM` | - | vetëm një katror aq km në çdo anë të një pike |
| `--bounds X0 Z0 X1 Z1` | - | vetëm kjo kuti, në metra DCS (x veri, z lindje) |
| `--cell M` | `0` | e rrallon rrjetin: çdo kulm brenda *M* metrash bëhet një (0: trekëndëshat e vetë lojës) |
| `--seabed` | joaktiv | e mban shtratin e detit si tokë (si parazgjedhje lihet jashtë) |
| `--no-water` | joaktiv | lë jashtë detin e sheshtë |
| `--no-buildings` | joaktiv | lë jashtë ndërtesat e skenës së teatrit |
| `--force` | joaktiv | eksporton një hartë shumë të madhe të plotë me detaje të plota |
| `--projection LON0 FE FN` | ai i teatrit | konstantet Transverse Mercator për një teatër që ky mjet nuk e njeh ([fit](fit.md)) |

Çdo opsion, ashtu siç e shtyp programi: [Referenca e komandave](../cli-reference.md).

## Madhësia {#size}

Rrjeti i lojës është adaptiv - det i hapur në trekëndësha kilometra të gjerë, bregdete
dhe rrugë në disa metra. Një teatër i vogël është disa milionë trekëndësha; të mëdhenjtë
janë dhjetëra milionë kulme. Mbi 30 milionë kulme për t'u lexuar, `level`
ndalon (statusi i daljes 1) dhe kërkon një rajon, një rrjet më të rrallë (`--cell 50`) ose
`--force`.

Statusi i daljes: 0 u krye; 1 dështoi ose është shumë i madh; 2 instalimi ose teatri nuk u
gjet (teatrot e gjetur listohen).

## Shembuj {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Çfarë ka në skedarë: [Skedarët e nivelit](output.md).
