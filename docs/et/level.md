---
title: "Taseme ehitamine: level"
nav_order: 3
lang: et
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# Taseme ehitamine: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Samm-sammult {#step-by-step}

Pole sul käsurealt kogemust? Loe enne [Enne alustamist](before-you-start.md).

1. Leia teatri kausta nimi käsuga [`list`](list.md).
2. Väikese teatri puhul ehita see tervena: `heat3d-dcs-maps level <theatre> -o levels`.
3. Suure puhul vali piirkond: `--around <lat> <lon> <km>` (ruut nii mitme km kaugusel punktist mõlemal pool) või `--bounds X0 Z0 X1 Z1` DCS-i meetrites.
   Nimeta see valikuga `--name`.
4. Käsk prindib kahhelid nende lugemisel, kolmnurkade arvu, kirjutatud faili ja selle, mitu teatri linna jääb maapinnale — projektsiooni kontroll, mis peaks ütlema "N of N".
5. Laadi `<folder>/<name>.glb` vaataja Taseme paneelis ja lülita sisse
   **Jäädvustatud värv**, et näha maapinna klasse.

![level sünteetilisel installil](../assets/img/level.svg)

Sama sünteetilise teatri piirkond DCS-i meetrites:

![level valikutega --bounds ja --name](../assets/img/level-bounds.svg)

## Valikud {#options}

| Valik | Vaikimisi | Teeb |
|---|---|---|
| `theatre` | - | kaustanimi kaustas `Mods\terrains`, nii nagu `list` prindib (suurtähtedega või väikestega) |
| `-o`, `--out` | nõutud | kaust, kuhu kirjutada `<name>.glb` ja `<name>.json` |
| `--dcs FOLDER` | leitakse | DCS World'i kaust ([kust see leitakse](list.md#where-the-install-is-found)) |
| `--name NAME` | teatri oma | taseme nimi ja tema failide nimi |
| `--around LAT LON KM` | - | ainult ruut nii mitme km kaugusel punktist mõlemal pool |
| `--bounds X0 Z0 X1 Z1` | - | ainult see kast DCS-i meetrites (x põhja, z ida) |
| `--cell M` | `0` | võrgu hõrendamine: iga tipp *M* meetri piires muutub üheks (0: mängu enda kolmnurgad) |
| `--seabed` | väljas | hoia merepõhi maapinnana (vaikimisi jäetakse see välja) |
| `--no-water` | väljas | jäta lame meri välja |
| `--no-buildings` | väljas | jäta teatri stseeni hooned välja |
| `--force` | väljas | ekspordi väga suur kaart tervena täistäpsusega |
| `--projection LON0 FE FN` | teatri oma | Transverse Mercatori konstandid teatrile, mida see tööriist ei tunne ([fit](fit.md)) |

Iga valik, nii nagu programm selle prindib: [Käsu viide](../cli-reference.md).

## Suurus {#size}

Mängu võrk on adaptiivne — avamerel kolmnurgad kilomeetri laiused, rannajoontes ja teedel mõne meetri laiused. Väike teater on mõni miljon kolmnurka; suured on kümneid miljoneid tippe. Kui lugemisele tuleks üle 30 miljoni tipu, peatub `level` (väljumisolek 1) ja küsib piirkonda, hõredamat võrku (`--cell 50`) või `--force`.

Väljumisolek: 0 valmis; 1 ebaõnnestus või liiga suur; 2 installi või teatrit ei leitud (leitud teatrid on loetletud).

## Näited {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # terve, täistäpsus
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24 km ruut
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # kast DCS-i meetrites
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # terve, 50 m-ni hõrendatud
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # ainult maapind
```

Mis failides on: [Tasemefailid](output.md).
