---
title: "Teatrų paieška: list"
nav_order: 2
lang: lt
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Teatrų paieška: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nesate įpratę prie komandinės eilutės? Pirmiausia perskaitykite [Prieš pradedant](before-you-start.md).

1. Įdiekite vieną kartą: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, atidarykite
   terminalą tame aplanke ir vykdykite `python -m pip install -e .` (Python 3.10 ar naujesnė; kartu
   įdiegiama numpy, o `fit` su `.parquet` – pyarrow).
2. Vykdykite `heat3d-dcs-maps list`.
3. Kiekvienas įdiegtas teatras išveda po vieną eilutę: jo aplanko pavadinimą (pavadinimą, kurį priima kitos
   komandos), jo žemės failo dydį, jo plytelių ir viršūnių skaičių, ar žinoma jo platumos/ilgumos projekcija, ir ar jis nuskaitomas.
   Kiekvienos eilutės pabaigoje turėtumėte matyti `readable`.

![list ant sintetinio įdiegimo](../assets/img/list.svg)

Paveikslėlis – paleidimas ant įdiegimo, kurį sukuria testai (`tests/synth.py`), o ne ant žaidimo.

## Kur randamas įdiegimas {#where-the-install-is-found}

`--dcs <folder>` (aplankas, kuriame yra `Mods\terrains`) arba aplinkos kintamasis `DCS_PATH`; kitu atveju
ieškoma registre, Steam bibliotekose ir įprastuose aplankuose.

| Parinktis | Ką daro |
|---|---|
| `--dcs FOLDER` | DCS World aplankas, tas, kuriame yra `Mods\terrains` |

Išeities kodas: 0 – baigta; 2 – įdiegimas ar teatras nerastas.
