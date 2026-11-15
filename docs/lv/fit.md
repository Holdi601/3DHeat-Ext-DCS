---
title: "Projekcijas: fit"
nav_order: 6
lang: "lv"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projekcijas: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Katrs teātris ir Transversālā Merkatora projekcija ar savām konstantēm. Rīks tās zina
teātriem, uz kuriem tas ir pārbaudīts; citam, kuru tas nezina, `fit` tās atrod no jebkura
ieraksta, kurā ir gan platuma/garuma, gan DCS metri, piemēram, 3DHeat Watcher sesija vienam lidojumam.

1. Ierakstiet lidojumu uz šā teātra ar 3DHeat Watcher (vai izveidojiet jebkuru ierakstu
   ar kolonnām `lat`, `lon`, `x`, `z` DCS metros: x ir metri uz ziemeļiem, z metri uz austrumiem,
   kā visur DCS).
2. Palaidiet `heat3d-dcs-maps fit "<session>/heat.parquet"` (vai `.jsonl` vai `.csv`).
3. Tas izdrukā atrasto projekciju kā JSON, punktu vidējo kvadrātisko kļūdu (root mean square)
   un `--projection` argumentus, ko izmantot.
4. Izveidojiet līmeni ar tiem:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit uz sintētiska ieraksta](../assets/img/fit.svg)

Attēla ieraksts ir deviņi punkti, kas izveidoti no zināmas projekcijas, un `fit` tos atrod
atpakaļ līdz milimetram.

| Arguments | Ko dara |
|---|---|
| `recording` | `.parquet`, `.jsonl` vai `.csv` ar kolonnām `lat`, `lon`, `x`, `z` (DCS metri); rindas, kuras nevar nolasīt, tiek izlaistas |

Projekcija ir Krīgera rinda, kā to dod C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Izejas statuss: 0 laba atbilstība (zem 5 m vidējā kvadrātiskā kļūda); 1 slikta atbilstība vai mazāk nekā trīs izmantojamas rindas; 2 fails nav atrasts.
