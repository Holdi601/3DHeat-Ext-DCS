---
title: "Kentän rakentaminen: level"
nav_order: 3
lang: "fi"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Kentän rakentaminen: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Vaihe vaiheelta {#step-by-step}

Uusi komentorivin kanssa? Lue ensin [Ennen aloittamista](before-you-start.md).

1. Selvitä teatterin kansion nimi komennolla [`list`](list.md).
2. Pienelle teatterille rakenna se kokonaisena: `heat3d-dcs-maps level <theatre> -o levels`.
3. Suurelle valitse alue: `--around <lat> <lon> <km>` (neliö näin monen km:n päässä pisteestä
   kumpaankin suuntaan) tai `--bounds X0 Z0 X1 Z1` DCS-metreinä. Anna sille nimi `--name`-asetuksella.
4. Komento tulostaa ruudut lukiessaan, kolmioiden määrän, kirjoitetun tiedoston ja sen, montako
   teatterin kaupunkia osuu maastoon – projektion tarkistus, jonka pitäisi näyttää "N of N".
5. Lataa `<folder>/<name>.glb` katselimen Tausta / kenttä -paneeliin ja kytke päälle
   **Tallennettu väri** nähdäksesi maaluokat.

![kenttä synteettisessä asennuksessa](../assets/img/level.svg)

Sama synteettinen teatteri, alue DCS-metreinä:

![kenttä --bounds- ja --name-asetuksilla](../assets/img/level-bounds.svg)

## Asetukset {#options}

| Asetus | Oletus | Tekee |
|---|---|---|
| `theatre` | - | kansion nimi kohdassa `Mods\terrains`, kuten `list` sen tulostaa (kirjainkoolla ei väliä) |
| `-o`, `--out` | pakollinen | kansio, johon `<name>.glb` ja `<name>.json` kirjoitetaan |
| `--dcs FOLDER` | löytyy | DCS World -kansio ([missä se löytyy](list.md#where-the-install-is-found)) |
| `--name NAME` | teatterin | kentän nimi ja sen tiedostojen nimi |
| `--around LAT LON KM` | - | vain neliö näin monen km:n päässä pisteestä kumpaankin suuntaan |
| `--bounds X0 Z0 X1 Z1` | - | vain tämä laatikko DCS-metreinä (x pohjoiseen, z itään) |
| `--cell M` | `0` | harvenna verkkoa: jokainen kärki *M* metrin säteellä muuttuu yhdeksi (0: pelin omat kolmiot) |
| `--seabed` | pois | pidä merenpohja maana (oletuksena se jätetään pois) |
| `--no-water` | pois | jätä tasainen meri pois |
| `--no-buildings` | pois | jätä teatterin maiseman rakennukset pois |
| `--force` | pois | vie hyvin suuri kartta kokonaisena täydellä tarkkuudella |
| `--projection LON0 FE FN` | teatterin | Transverse Mercator -vakiot teatterille, jota tämä työkalu ei tunne ([fit](fit.md)) |

Jokainen asetus sellaisena kuin ohjelma ne tulostaa: [Komentoviite](../cli-reference.md).

## Koko {#size}

Pelin verkko on mukautuva: avoin meri kolmioina, joiden sivu on kilometrejä, rannikot ja tiet
muutamassa metrissä. Pieni teatteri on muutama miljoona kolmiota; suuret ovat kymmeniä miljoonia
kärkiä. Yli 30 miljoonan luettavan kärjen kohdalla `level` pysähtyy (poistumistila 1) ja pyytää
aluetta, harvempaa verkkoa (`--cell 50`) tai `--force`-asetusta.

Poistumistila: 0 valmis; 1 epäonnistui tai liian suuri; 2 asennusta tai teatteria ei löytynyt
(löydetyt teatterit luetellaan).

## Esimerkit {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # kokonaan, täysi tarkkuus
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24 km:n neliö
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # laatikko DCS-metreinä
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # kokonaan, harvennettuna 50 m:iin
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # pelkkä maa
```

Mitä tiedostoissa on: [Kenttätiedostot](output.md).
