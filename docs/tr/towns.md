---
title: "Yer adları: towns"
nav_order: 5
lang: "tr"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Yer adları: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Tiyatronun yer adlarını, `map/towns.lua` dosyasından (metin olarak okunur, asla çalıştırılmaz) JSON olarak yazar: her kasabanın adı, enlemi ve boylamı ile tiyatronun izdüşümünden geçerek elde edilen, metre cinsinden DCS `x` (kuzey) ve `z` (doğu) değerleri.

1. Tiyatronun klasör adını [`list`](list.md) ile bulun.
2. `heat3d-dcs-maps towns <theatre> > towns.json` çalıştırın.
3. `x`/`z` değerlerini bir seviyeyi etiketlemek ya da bir kaydın konumlarını denetlemek için kullanın.

![Sentetik bir kurulumda kasabalar](../assets/img/towns.svg)

| Seçenek | Ne yapar |
|---|---|
| `theatre` | `Mods\terrains` altındaki klasör adı |
| `--dcs FOLDER` | DCS World klasörü |

Bir seviyenin bölgesindeki kasabalar, altlarındaki zeminin yüksekliğiyle birlikte o seviyenin `<name>.json` dosyasında da bulunur ([Seviye dosyaları](output.md)).
