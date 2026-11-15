---
title: "Teātru meklēšana: list"
nav_order: 2
lang: "lv"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Teātru meklēšana: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nekad neesat strādājis ar komandrindu? Vispirms izlasiet [Pirms sākat](before-you-start.md).

1. Uzstādiet vienreiz: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, atveriet
   termināli šajā mapē un palaidiet `python -m pip install -e .` (Python 3.10
   vai jaunāks; tas atnes numpy un pyarrow priekš `fit` ar `.parquet`).
2. Palaidiet `heat3d-dcs-maps list`.
3. Katrs uzstādītais teātris izdrukā vienu rindu: tā mapes nosaukumu (nosaukumu, ko pieņem citas komandas), tā zemes faila izmēru, tā flīzes un virsotnes, to, vai tā platuma/garuma projekcija ir zināma, un vai tas ir nolasāms.
   Katras rindas beigās vajadzētu redzēt `readable`.

![list uz sintētiska uzstādījuma](../assets/img/list.svg)

Attēls ir palaišana uz uzstādījuma, ko veido testi (`tests/synth.py`), nevis uz pašas spēles.

## Kur tiek atrasts uzstādījums {#where-the-install-is-found}

`--dcs <folder>` (mape, kurā ir `Mods\terrains`) vai vides mainīgais `DCS_PATH`; citādi tiek meklēts reģistrs, Steam bibliotēkas un parastās mapes.

| Iespēja | Ko dara |
|---|---|
| `--dcs FOLDER` | DCS World mape, tā, kurā ir `Mods\terrains` |

Izejas statuss: 0 pabeigts; 2 uzstādījums vai teātris nav atrasts.
