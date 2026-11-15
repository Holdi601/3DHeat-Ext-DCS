---
title: "Dosyalar nasıl okunur"
nav_order: 7
lang: "tr"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Dosyalar nasıl okunur {#how-the-files-are-read}

Yalnızca `Mods/terrains/<theatre>/surface/*.surface5` (zemin ağı), `Scenes/*.scn5` (nesnelerin durduğu yer ve her modelin kutusu), `AirfieldsTaxiways/*.rn4` ve `map/towns.lua` (yer adları, metin olarak okunur, asla çalıştırılmaz) okunur. Şifreli `terrain.cfg.lua.pak.crypt`, `manifest.bin` ve programın hiçbir parçası okunmaz.

`.surface5` biçimi belgelenmemiştir; dosyalardan okunan düzen [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py) içinde yazılıdır. Kısaca: karo kayıtlarının bir dizini (bir dönüşüm, sınırlar ve türlü bayt akışlarının listeleri; her liste, çizildiği gölgelendirici ve malzemeyle birlikte gelir), ardından ham veriler. Ne sıkıştırılmıştır ne de şifrelenmiştir. Karonun `Pbase` akışı köşelerini tutar; `Land` olarak çizilen grup üçgenleri ve her üçgen için bir `TRITYPE` tutar, en düşük biti denizi işaretler. Diğer gruplar, yukarıdaki sınıfları veren katmanlardır.

## Doğrulananlar {#verified}

- `list`, kurulu her tiyatronun dizinini okudu (her biri milyonlarca ila on milyonlarca zemin köşesi); örneklenen her karo makul metrelere çözüldü.
- İki tiyatronun bölgelerinde, `towns.lua` dosyasındaki kasabalar bir zemin köşesinin metreleri içine düştü, karada, "N of N"; en yüksek zemin gerçek zirveyle on metre içinde eşleşti; hava alanları, nehirler, köyler ve yollar kendi sınıflarında göründü. İki seviye de görüntüleyicide yüklendi; aynı DCS metrelerindeki kasaba işaretleri zeminde duruyor.
- Bir sahne bölgesinde, bina yerleşimleri kendi zeminlerine oturdu; pist ışıkları oyunun pistini izledi; vagonlar ve duvar parçaları çözülen yönle hizalandı; hepsi.
- `tests/` `.surface5` dosyalarını aynı düzende oluşturur; bu yüzden burada oyun verisi tutulmaz. `tests/test_real_install.py` testleri çalıştıran makinedeki kurulumda çalışır; kurulum yoksa atlanır.

**Denenmedi:** büyük bir tiyatronun tamamı tek bir seviyede (yukarıdaki boyut koruması bir nedenle var) ve denenenlerden başka DCS sürümleri.

## Okunmayanlar {#not-read}

- **Şekil olarak binalar** (modeller `Models/` içinde `.edm` dosyalarıdır): yalnızca kutular, bilerek. Onların düzeni ve sahnenin düzeni [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py) içinde yazılıdır; kurulu her tiyatro okunur (iki eski tiyatro da bilinen bir varyant düzeninde).
- Ağaçlar, ışıklar ve sahnenin diğer nesneleri: okunur, çizilmez.
- **Bir grafik olarak yol ağı** (`roads/*.rn4`): çözülmedi.
- Dokular, ağaçlar, denizin dalgaları, zeminin kendi düşük ayrıntı düzeyleri.
