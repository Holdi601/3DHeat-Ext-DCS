---
title: "Teatterien etsiminen: list"
nav_order: 2
lang: fi
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Teatterien etsiminen: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Uusi komentorivin kanssa? Lue ensin [Ennen aloittamista](before-you-start.md).

1. Asenna kerran: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, avaa pääte
   kyseisessä kansiossa ja suorita `python -m pip install -e .` (Python 3.10 tai uudempi;
   se tuo mukanaan numpy-kirjaston ja pyarrow-kirjaston `fit`-komentoa varten `.parquet`-tiedostolle).
2. Suorita `heat3d-dcs-maps list`.
3. Jokainen asennettu teatteri tulostaa yhden rivin: sen kansion nimen (nimen, jonka muut
   komennot ottavat), maatiedoston koon, sen ruudut ja kärjet, onko sen leveys- ja
   pituusastejärjestelmä tunnettu, ja voidaanko se lukea. Rivin lopussa pitäisi näkyä `readable`.

![list synteettisessä asennuksessa](../assets/img/list.svg)

Kuva on ajo asennuksella, jonka testit rakentavat (`tests/synth.py`), ei itse pelillä.

## Mistä asennus löytyy {#where-the-install-is-found}

`--dcs <folder>` (kansio, jossa on `Mods\terrains`) tai ympäristömuuttuja `DCS_PATH`; muuten etsitään
rekisteristä, Steam-kirjastoista ja tavallisista kansioista.

| Asetus | Tekee |
|---|---|
| `--dcs FOLDER` | DCS World -kansio, se jossa on `Mods\terrains` |

Poistumistila: 0 valmis, 2 asennusta tai teatteria ei löytynyt.
