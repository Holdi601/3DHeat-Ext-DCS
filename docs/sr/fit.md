---
title: "Пројекције: fit"
nav_order: 6
lang: "sr"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Пројекције: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Сваки театар је Transverse Mercator пројекција са сопственим константама. Алат их
зна за театре на којима је провераван; за онај који не зна, `fit` их налази из
било ког снимка који садржи и географску ширину/дужину и DCS метре, на пример
сесију 3DHeat Watcher-а једног лета.

1. Снимите лет над театром помоћу 3DHeat Watcher-а (или направите било који снимак
   са колонама `lat`, `lon`, `x`, `z` у DCS метрима: x су метри на север, z метри
   на исток, као и свуда у DCS-у).
2. Покрените `heat3d-dcs-maps fit "<session>/heat.parquet"` (или `.jsonl` или `.csv`).
3. Исписује уклопљену пројекцију као JSON, корену средње квадратне грешке по
   тачкама, и аргументе `--projection` за употребу.
4. Направите ниво с њима:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit над синтетичким снимком](../assets/img/fit.svg)

Снимак на слици има девет тачака направљених из познате пројекције, коју `fit`
враћа до милиметра.

| Аргумент | Шта ради |
|---|---|
| `recording` | `.parquet`, `.jsonl` или `.csv` са колонама `lat`, `lon`, `x`, `z` (DCS метри); редови који се не читају се прескачу |

Пројекција је Krüger-ов ред, онако како га даје C. F. F. Karney („Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Излазни статус: 0 добро уклапање (испод 5 m корен средње квадратне грешке); 1 лоше
уклапање, или мање од три употребљива реда; 2 датотека није нађена.
