---
title: "Koşullar ve lisans"
nav_order: 8
lang: "tr"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Koşullar ve lisans {#terms-and-licence}

## Eagle Dynamics'in koşulları {#eagle-dynamics-terms}

2026-11-07 tarihinde, kurulumun `Doc/license_en.txt` dosyasından okundu (DCS World Son Kullanıcı Lisans Sözleşmesi, The Fighter Collection Ltd). Lisanslı "Program", "THE DATA SUPPLIED WITH IT" ifadesini içerir. Madde 3.1 şöyledir:

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

Madde 3.1 (a), izin alınmadan "sell, trade, rent, lease, sub-license, merge, adapt, vary, modify the Program" (Programı satmak, takas etmek, kiralamak, birleştirmek, uyarlamak, değiştirmek) eylemlerini yasaklar; (e) ise "exploit this Program or any of its parts commercially" (Programı ya da parçalarını ticari olarak kullanmak) eylemini yasaklar.

Bu okuyucunun yaptığı: kurulumdan sonra, oyunun dışında, kendi makinenizdeki veri dosyalarını okur. Oyunda hiçbir şeyi değiştirmez, hiçbir şifrelemeyi kırmaz (bir zemin klasöründeki tek şifreli dosyaya dokunulmaz) ve hiçbir sunucuyla konuşmaz. Bir veri dosyasının düzenini çıkarmak, 3.1 (c) anlamında tersine mühendisliktir; oyunun zemininden yapılan bir seviye de türev bir çalışma sayılabilir. Okuyucuyu kullanmak sizin kararınızdır, kendi kullanımınız için; yazdığı seviyeleri görüntülemek sizindir, paylaşmak ya da yayımlamak için değil. Bu yüzden ayrı bir pakettir.

Onaylı alternatif hiçbir dosyayı okumaz: simülatörün kendi görev komut dosyası, bir görev çalışırken zemini örnekleyebilir (`land.getHeight`, `land.getSurfaceType`) ve hava alanlarını listeleyebilir (`world.getAirbases`). Bu, tiyatro başına saatlerce DCS'nin çalışmasını gerektirir ve daha kaba bir ızgara verir. Dosyaların okunabilir olduğu anlaşıldığı için kurulmadı.

## Lisans ve kaynaklar {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). numpy (BSD-3-Clause) gerektirir; `.parquet` üzerinde `fit` pyarrow (Apache-2.0) gerektirir. Bu proje için yazıldı. İzdüşüm sabitleri, pydcs tarafından yayımlanmış gerçeklerdir (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); yalnızca sayılar alındı. İzdüşüm, C. F. F. Karney'in verdiği Krüger serisidir ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Başka hiçbir projeden kod alınmadı.
