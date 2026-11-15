---
title: "Að smíða borð: level"
nav_order: 3
lang: is
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Að smíða borð: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Skref fyrir skref {#step-by-step}

Hefurðu aldrei notað skipanalínu? Lestu fyrst [Áður en þú byrjar](before-you-start.md).

1. Finndu möppuheiti leiksvæðisins með [`list`](list.md).
2. Fyrir lítið leiksvæði, smíðaðu það í heild: `heat3d-dcs-maps level <theatre> -o levels`.
3. Fyrir stórt, veldu svæði: `--around <lat> <lon> <km>` (ferningur sem nær
   svo marga km til hvorrar hliðar frá punkti) eða `--bounds X0 Z0 X1 Z1` í DCS-metrum.
   Nefndu það með `--name`.
4. Skipunin prentar flísarnar um leið og hún les þær, fjölda þríhyrninga, skrána
   sem var skrifuð, og hversu margir bæir leiksvæðisins lenda á landinu - 
   athugun á vörpuninni sem ætti að sýna „N of N“.
5. Hladdu `<folder>/<name>.glb` í spjaldið Bakgrunnur / borð í skoðaranum og kveiktu á
   **Skráður litur** til að sjá landflokkana.

![level á gerviuppsetningu](../assets/img/level.svg)

Svæði af sama gervileiksvæði, eftir DCS-metrum:

![level með --bounds og --name](../assets/img/level-bounds.svg)

## Valkostir {#options}

| Valkostur | Sjálfgefið | Gerir |
|---|---|---|
| `theatre` | - | möppuheitið undir `Mods\terrains`, eins og `list` prentar það (hvaða há-/lágstafir sem er) |
| `-o`, `--out` | nauðsynlegt | mappan sem `<name>.glb` og `<name>.json` eru skrifuð í |
| `--dcs FOLDER` | fundin | DCS World mappan ([hvar hún finnst](list.md#where-the-install-is-found)) |
| `--name NAME` | nafn leiksvæðisins | nafn borðsins og skráa þess |
| `--around LAT LON KM` | - | aðeins ferningur svo marga km til hvorrar hliðar frá punkti |
| `--bounds X0 Z0 X1 Z1` | - | aðeins þessi kassi, í DCS-metrum (x norður, z austur) |
| `--cell M` | `0` | grisja netið: sérhver hnútur innan *M* metra verður einn (0: eigin þríhyrningar leiksins) |
| `--seabed` | af | halda hafsbotninum sem landi (sjálfgefið er hann sleppt) |
| `--no-water` | af | sleppa flata sjónum |
| `--no-buildings` | af | sleppa byggingum senu leiksvæðisins |
| `--force` | af | flytja út mjög stórt kort í heild í fullum smáatriðum |
| `--projection LON0 FE FN` | leiksvæðisins | Transverse Mercator fastar fyrir leiksvæði sem þetta verkfæri þekkir ekki ([fit](fit.md)) |

Hver valkostur, eins og forritið prentar hann: [Skipanayfirlit](../cli-reference.md).

## Stærð {#size}

Net leiksins er aðlagandi - opið haf í þríhyrningum sem eru kílómetrar á breidd, strendur
og vegir í nokkrum metrum. Lítið leiksvæði eru nokkrar milljónir þríhyrninga; þau stóru
eru tugir milljóna hnúta. Yfir 30 milljónum hnúta til að lesa stöðvast `level`
(útgöngustaða 1) og biður um svæði, grennra net (`--cell 50`) eða
`--force`.

Útgöngustaða: 0 búið; 1 mistókst eða of stórt; 2 uppsetningin eða leiksvæðið
fannst ekki (leiksvæðin sem fundust eru talin upp).

## Dæmi {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Hvað er í skránum: [Borðaskrárnar](output.md).
