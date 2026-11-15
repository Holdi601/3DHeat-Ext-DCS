---
title: "Hledání území: list"
nav_order: 2
lang: cs
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Hledání území: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Nikdy jste nepracovali s příkazovým řádkem? Nejdřív si přečtěte [Než začnete](before-you-start.md).

1. Nainstalujte jednou: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, otevřete
   terminál v této složce a spusťte `python -m pip install -e .` (Python 3.10
   nebo novější; přinese numpy a pro `fit` na `.parquet` také pyarrow).
2. Spusťte `heat3d-dcs-maps list`.
3. Každé nainstalované území vypíše jeden řádek: název jeho složky (ten, který berou
   ostatní příkazy), velikost souboru terénu, jeho dlaždice a vrcholy,
   zda je známá jeho projekce zeměpisné šířky a délky, a zda se dá číst.
   Na konci každého řádku byste měli vidět `readable`.

![list na syntetické instalaci](../assets/img/list.svg)

Obrázek je běh na instalaci, kterou vytvářejí testy (`tests/synth.py`), ne na hře.

## Kde se instalace hledá {#where-the-install-is-found}

`--dcs <folder>` (složka obsahující `Mods\terrains`) nebo proměnná prostředí `DCS_PATH`;
jinak se prohledá registr, knihovny Steamu a obvyklé složky.

| Možnost | Co dělá |
|---|---|
| `--dcs FOLDER` | složka DCS World, ta, která obsahuje `Mods\terrains` |

Stavový kód: 0 hotovo, 2 nenalezena instalace ani území.
