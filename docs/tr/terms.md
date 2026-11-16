---
title: "Koşullar ve lisans"
nav_order: 8
lang: "tr"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Koşullar ve lisans {#terms-and-licence}

## Okuyucu neyi okur {#what-the-reader-reads}

Okuyucu, bilgisayarınızdaki kendi DCS World kurulumunuzun veri dosyalarını okur ([Dosyalar nasıl okunur](reading.md)). Oyunda hiçbir şeyi değiştirmez ve hiçbir sunucuyla konuşmaz.

Oyundan hiçbir şey birlikte gönderilmez veya yeniden dağıtılmaz: oyun dosyası yok, oyun kodu yok, DLL yok; testler okudukları her dosyayı kendileri oluşturur. Yazdığı seviyeler sizin makinenizde kalır.

3DHeat DCS, Eagle Dynamics ile bağlantılı değildir ve onun tarafından onaylanmamıştır. DCS World ve ilgili adlar ile ticari markalar sahiplerine aittir.

Hak sahipleri: [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) adresinde bir kayıt açın - hızlı yanıt veriyor ve istek üzerine her şeyi kaldırıyoruz.

## Lisans ve kaynaklar {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). numpy (BSD-3-Clause) gerektirir; `.parquet` üzerinde `fit` pyarrow (Apache-2.0) gerektirir. Bu proje için yazıldı. İzdüşüm sabitleri, pydcs tarafından yayımlanmış gerçeklerdir (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); yalnızca sayılar alındı. İzdüşüm, C. F. F. Karney'in verdiği Krüger serisidir ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Başka hiçbir projeden kod alınmadı.
