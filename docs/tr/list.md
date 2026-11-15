---
title: "Tiyatroları bulma: list"
nav_order: 2
lang: "tr"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Tiyatroları bulma: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

Komut satırında yeni misiniz? Önce [Başlamadan önce](before-you-start.md) sayfasını okuyun.

1. Bir kez kurun: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, o klasörde bir terminal açın ve `python -m pip install -e .` çalıştırın (Python 3.10 veya daha yeni; numpy'yi getirir, `.parquet` üzerinde `fit` için pyarrow'u da).
2. `heat3d-dcs-maps list` çalıştırın.
3. Kurulu her tiyatro bir satır yazar: klasör adı (diğer komutların aldığı ad), zemin dosyasının boyutu, karoları ve köşeleri, enlem/boylam izdüşümünün bilinip bilinmediği ve okunup okunmadığı. Her satırın sonunda `readable` görmelisiniz.

![Sentetik bir kurulumda list](../assets/img/list.svg)

Resim, oyunda değil, testlerin oluşturduğu bir kurulumda (`tests/synth.py`) yapılan bir çalıştırmadır.

## Kurulumun nerede bulunduğu {#where-the-install-is-found}

`--dcs <folder>` (`Mods\terrains` klasörünü tutan klasör) ya da `DCS_PATH` ortam değişkeni; aksi halde kayıt defteri, Steam kitaplıkları ve olağan klasörler aranır.

| Seçenek | Ne yapar |
|---|---|
| `--dcs FOLDER` | DCS World klasörü, `Mods\terrains` klasörünü tutan |

Çıkış durumu: 0 tamam; 2 kurulum ya da tiyatro bulunamadı.
