---
title: "Gjetja e teatrove: list"
nav_order: 2
lang: "sq"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Gjetja e teatrove: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Je i ri me rreshtin e komandave? Lexo së pari [Para se të fillosh](before-you-start.md).

1. Instalo një herë: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, hap
   një terminal në atë dosje dhe ekzekuto `python -m pip install -e .` (Python 3.10
   ose më i ri; sjell numpy, dhe pyarrow për `fit` mbi një `.parquet`).
2. Ekzekuto `heat3d-dcs-maps list`.
3. Çdo teatër i instaluar shtyp një rresht: emrin e dosjes së tij (emri që e marrin
   komandat e tjera), madhësinë e skedarit të tokës, pllakat dhe kulmet e tij,
   nëse projeksioni i tij i gjerësisë/gjatësisë gjeografike njihet, dhe nëse lexohet.
   Në fund të çdo rreshti duhet të shohësh `readable`.

![list mbi një instalim sintetik](../assets/img/list.svg)

Pamja është një ekzekutim mbi një instalim që e ndërtojnë testet (`tests/synth.py`), jo mbi
lojën.

## Ku gjendet instalimi {#where-the-install-is-found}

`--dcs <folder>` (dosja që mban `Mods\terrains`) ose ndryshorja e mjedisit
`DCS_PATH`; përndryshe kërkohen regjistri, bibliotekat e Steam dhe
dosjet e zakonshme.

| Opsioni | Çfarë bën |
|---|---|
| `--dcs FOLDER` | dosja e DCS World, ajo që mban `Mods\terrains` |

Statusi i daljes: 0 u krye, 2 nuk u gjet instalim ose teatër.
