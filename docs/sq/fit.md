---
title: "Projeksionet: fit"
nav_order: 6
lang: sq
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projeksionet: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Çdo teatër është një projeksion Transverse Mercator me konstantet e veta. Mjeti
i njeh për teatrot mbi të cilat u kontrollua; për një që nuk e njeh,
`fit` i gjen nga çdo regjistrim që mban si gjerësi/gjatësi gjeografike ashtu edhe
metra DCS, si një seancë e 3DHeat Watcher për një fluturim.

1. Regjistro një fluturim në teatër me 3DHeat Watcher (ose bëj çdo
   regjistrim me kolona `lat`, `lon`, `x`, `z` në metra DCS: x është metra
   drejt veriut, z metra drejt lindjes, si kudo në DCS).
2. Ekzekuto `heat3d-dcs-maps fit "<session>/heat.parquet"` (ose një `.jsonl` ose `.csv`).
3. Shtyp projeksionin e përshtatur si JSON, gabimin mesatar katror (root mean square)
   mbi pikat, dhe argumentet `--projection` që duhen përdorur.
4. Ndërto nivelin me to:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit mbi një regjistrim sintetik](../assets/img/fit.svg)

Regjistrimi në pamje është nëntë pika të bëra nga një projeksion i njohur,
të cilin `fit` e gjen prapë deri në milimetër.

| Argumenti | Çfarë bën |
|---|---|
| `recording` | `.parquet`, `.jsonl` ose `.csv` me kolona `lat`, `lon`, `x`, `z` (metra DCS); rreshtat që nuk lexohen anashkalohen |

Projeksioni është seria e Krüger-it siç e jep C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Statusi i daljes: 0 përshtatje e mirë (nën 5 m gabim mesatar katror); 1 përshtatje e dobët, ose
më pak se tre rreshta të përdorshëm; 2 skedari nuk u gjet.
