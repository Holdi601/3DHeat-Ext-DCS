---
title: "Projekcijos: fit"
nav_order: 6
lang: "lt"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcijos: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Kiekvienas teatras yra Transverse Mercator projekcija su savo konstantomis. Įrankis žino jas
teatrams, kuriuose buvo patikrintas; jeigu teatro nepažįsta, `fit` randa jas iš bet kurio įrašo, kuriame yra
ir platuma/ilguma, ir DCS metrai, pavyzdžiui, vieno skrydžio 3DHeat Watcher sesija.

1. Įrašykite skrydį teatre su 3DHeat Watcher (arba padarykite bet kokį įrašą su stulpeliais `lat`, `lon`, `x`, `z`
   DCS metrais: x – metrai į šiaurę, z – metrai į rytus, kaip ir visame DCS).
2. Vykdykite `heat3d-dcs-maps fit "<session>/heat.parquet"` (arba `.jsonl` ar `.csv`).
3. Jis išveda rastą projekciją JSON formatu, vidutinę kvadratinę paklaidą per taškus
   (root mean square) ir `--projection` argumentus, kuriuos reikia naudoti.
4. Sukurkite lygį su jais:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit ant sintetinio įrašo](../assets/img/fit.svg)

Paveikslėlio įraše yra devyni taškai, sukurti pagal žinomą projekciją; `fit` iš jų atkuria ją iki milimetro.

| Argumentas | Ką daro |
|---|---|
| `recording` | `.parquet`, `.jsonl` ar `.csv` su stulpeliais `lat`, `lon`, `x`, `z` (DCS metrais); eilutės, kurių nepavyksta nuskaityti, praleidžiamos |

Projekcija yra C. F. F. Karney pateikta Krüger eilutė („Transverse
Mercator with an accuracy of a few nanometers“, Journal of Geodesy 85, 2011).

Išeities kodas: 0 – geras atitikimas (mažiau nei 5 m vidutinė kvadratinė paklaida); 1 – prastas atitikimas arba mažiau
nei trys tinkamos eilutės; 2 – failas nerastas.
