---
title: "İzdüşümler: fit"
nav_order: 6
lang: tr
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# İzdüşümler: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

Her tiyatro, kendi sabitleriyle bir Transverse Mercator izdüşümüdür. Araç, test edildiği tiyatroların sabitlerini bilir; bilmediği bir tiyatro için `fit`, hem enlem/boylam hem DCS metrelerini içeren herhangi bir kayıttan sabitleri bulur. Örneğin tek bir uçuşun 3DHeat Watcher oturumu gibi.

1. Tiyatroda 3DHeat Watcher ile bir uçuş kaydedin (ya da `lat`, `lon`, `x`, `z` sütunları olan, DCS metrelerinde herhangi bir kayıt yapın: x metre kuzey, z metre doğu; DCS'de her yerde olduğu gibi).
2. `heat3d-dcs-maps fit "<session>/heat.parquet"` çalıştırın (ya da bir `.jsonl` ya da `.csv`).
3. Bulunan izdüşümü JSON olarak, noktalar üzerindeki kök ortalama kare hatasını ve kullanacağınız `--projection` argümanlarını yazar.
4. Seviyeyi bunlarla oluşturun: `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![Sentetik bir kayıt üzerinde fit](../assets/img/fit.svg)

Resimdeki kayıt, bilinen bir izdüşümden yapılmış dokuz noktadır; `fit` bunu milimetreye kadar geri bulur.

| Argüman | Ne yapar |
|---|---|
| `recording` | `lat`, `lon`, `x`, `z` sütunlarına sahip `.parquet`, `.jsonl` ya da `.csv` (DCS metreleri); okunmayan satırlar atlanır |

İzdüşüm, C. F. F. Karney'in verdiği Krüger serisidir ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Çıkış durumu: 0 iyi bir uyum (kök ortalama kare 5 m'nin altında); 1 zayıf bir uyum ya da üçten az kullanılabilir satır; 2 dosya bulunamadı.
