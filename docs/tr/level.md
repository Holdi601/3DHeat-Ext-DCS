---
title: "Seviye oluşturma: level"
nav_order: 3
lang: tr
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Seviye oluşturma: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Adım adım {#step-by-step}

Komut satırında yeni misiniz? Önce [Başlamadan önce](before-you-start.md) sayfasını okuyun.

1. Tiyatronun klasör adını [`list`](list.md) ile bulun.
2. Küçük bir tiyatroysa tamamını oluşturun: `heat3d-dcs-maps level <theatre> -o levels`.
3. Büyük bir tiyatroysa bir bölge seçin: `--around <lat> <lon> <km>` (bir noktanın her iki yanında o kadar km'lik bir kare) ya da DCS metreleriyle `--bounds X0 Z0 X1 Z1`. Adını `--name` ile verin.
4. Komut, okurken karoları, üçgen sayısını, yazılan dosyayı ve tiyatronun kaç kasabasının zemine düştüğünü yazar. Bu, izdüşümün bir denetimidir ve "N of N" okunmalıdır.
5. `<folder>/<name>.glb` dosyasını görüntüleyicinin Arka plan / bölüm panelinde yükleyin ve zemin sınıflarını görmek için **Yakalanan renk** (Captured colour) seçeneğini açın.

![Sentetik bir kurulumda seviye](../assets/img/level.svg)

Aynı sentetik tiyatronun bir bölgesi, DCS metreleriyle:

![--bounds ve --name ile seviye](../assets/img/level-bounds.svg)

## Seçenekler {#options}

| Seçenek | Varsayılan | Ne yapar |
|---|---|---|
| `theatre` | - | `list`'in yazdığı gibi `Mods\terrains` altındaki klasör adı (büyük/küçük harf farketmez) |
| `-o`, `--out` | gerekli | `<name>.glb` ve `<name>.json` dosyalarının yazılacağı klasör |
| `--dcs FOLDER` | bulunur | DCS World klasörü ([nerede bulunduğu](list.md#where-the-install-is-found)) |
| `--name NAME` | tiyatronun adı | seviyenin adı ve dosyalarının adı |
| `--around LAT LON KM` | - | yalnızca bir noktanın her iki yanında bu kadar km'lik bir kare |
| `--bounds X0 Z0 X1 Z1` | - | yalnızca bu kutu, DCS metrelerinde (x kuzey, z doğu) |
| `--cell M` | `0` | ağı seyrekleştir: *M* metre içindeki her köşe tek bir köşe olur (0: oyunun kendi üçgenleri) |
| `--seabed` | kapalı | deniz tabanını zemin olarak tut (varsayılan olarak dışarıda bırakılır) |
| `--no-water` | kapalı | düz denizi dışarıda bırak |
| `--no-buildings` | kapalı | tiyatro sahnesinin binalarını dışarıda bırak |
| `--force` | kapalı | çok büyük bir haritayı tam ayrıntıyla, tamamen dışa aktar |
| `--projection LON0 FE FN` | tiyatronun | bu aracın bilmediği bir tiyatro için Transverse Mercator sabitleri ([fit](fit.md)) |

Her seçenek, programın yazdığı gibi: [Komut başvurusu](../cli-reference.md).

## Boyut {#size}

Oyunun ağı uyarlanabilirdir: açık denizde kilometrelerce üçgenler, kıyılarda ve yollarda birkaç metre. Küçük bir tiyatro birkaç milyon üçgendir; büyük olanlar on milyonlarca köşedir. Okunacak 30 milyon köşenin üzerinde `level` durur (çıkış durumu 1) ve bir bölge, daha seyrek bir ağ (`--cell 50`) ya da `--force` ister.

Çıkış durumu: 0 tamam; 1 başarısız ya da çok büyük; 2 kurulum ya da tiyatro bulunamadı (bulunan tiyatrolar listelenir).

## Örnekler {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # tamamı, tam ayrıntıyla
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24 km'lik bir kare
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # DCS metrelerinde bir kutu
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # tamamı, 50 m'ye seyreltilmiş
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # yalnızca zemin
```

Dosyalarda ne var: [Seviye dosyaları](output.md).
