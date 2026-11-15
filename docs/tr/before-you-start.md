---
title: "Başlamadan önce"
nav_order: 1.5
lang: "tr"
source: before-you-start.md
source_hash: "64346abe88e5"
nav_exclude: true
search_exclude: true
---
# Başlamadan önce {#before-you-start}

Komut satırında yeni misiniz? Bu sayfa sizi hiçbir şeyden ilk çalıştırmaya kadar götürür.
Bir kez yapılır, yaklaşık on dakika sürer.

## 1. Python'u kurun {#install-python}

Bu araç **Python 3.10 veya daha yeni** bir sürüm ister.

- **Windows:** Python'u [python.org/downloads](https://www.python.org/downloads/) adresinden indirin ve kurulum programını çalıştırın. İlk ekranda **Add python.exe to PATH** (PATH'e python.exe ekle) kutusunu işaretleyin, sonra **Install Now** (Şimdi yükle) düğmesine tıklayın.
- **macOS ve Linux:** Python 3 genellikle zaten kuruludur. Bu sayfalarda `python` yazan yerde `python3` yazın.

## 2. Bu aracı alın {#get-this-tool}

[github.com/Holdi601/3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) adresini açın, yeşil **Code** (Türkçe arayüzde **Kod**) düğmesine, sonra **Download ZIP** (ZIP dosyasını indir) seçeneğine tıklayın ve seçtiğiniz bir klasöre açın. Git kullanıyorsanız: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`.

## 3. Bu klasörde bir terminal açın {#open-a-terminal-in-that-folder}

Terminal, komutları yazdığınız bir penceredir.

- **Windows:** klasörü Dosya Gezgini'nde açın, adres çubuğuna tıklayın, `powershell` yazın ve Enter'a basın. Mavi ya da siyah bir pencere açılır ve zaten o klasörde olursunuz.
- **macOS:** **Terminal**'i açın, `cd ` yazın (sonunda bir boşlukla), klasörü pencereye sürükleyin ve Enter'a basın.

`cd` "klasör değiştir" demektir: `cd C:\Tools\3DHeat-Ext-DCS` o klasöre gider.

## 4. Aracı kurun {#install-the-tool}

Bunu yazın ve Enter'a basın:

```bash
python -m pip install -e .
```

Sonunda şunu görmelisiniz: `Successfully installed heat3d-ext-dcs-...`.

## 5. Çalıştırın {#run-it}

```bash
heat3d-dcs-maps list
```

Şuna benzer bir çıktı görmelisiniz:

```text
DCS World at C:\Games\DCS World
  <theatre>    <n> GB    <n> tiles    <n> M vertices  lat/lon    readable
```

Sonraki adım: [Tiyatroları bulma: list](list.md), ardından [Seviye oluşturma: level](level.md).

## Bu sayfalardaki komutları nasıl okursunuz {#how-to-read-the-commands-on-these-pages}

| Gördüğünüz | Anlamı |
|---|---|
| `<folder>` | bir yer tutucu: `< >` işaretleri olmadan kendi değerinizi yazın |
| `[--force]` | isteğe bağlı: bırakın ya da gösterildiği gibi yazın |
| `a\|b` | bir seçim: `a` ya da `b` yazın |
| `# a note` | sizin için bir açıklama: yazmayın |
| `"C:\My Files\x"` | boşluk içeren bir yolu tırnak içine alın |
| `D:\Demos` | örnek bir Windows klasörü: kendinizinkini kullanın |

## Bir şey ters giderse {#when-something-goes-wrong}

| Mesaj | Ne yapmalı |
|---|---|
| `'python' is not recognized` | Python kurulu değil ya da PATH kutusu işaretlenmedi: yeniden kurun ve kutuyu işaretleyin (ya da `python` yerine `py` yazın). |
| `'heat3d-dcs-maps' is not recognized` | Aracın klasöründe 4. adımı yeniden çalıştırın ya da `heat3d-dcs-maps` yerine `python -m heat3d_ext_dcs` yazın: aynı işi yapar. |
| `No module named heat3d_ext_dcs` | Aracın klasöründe değilsiniz ya da 4. adım başarısız oldu: oraya `cd` ile gidin ve 4. adımı çalıştırın. |
| `No module named pip` | `python -m ensurepip` çalıştırın, sonra 4. adımı yapın. |
| başka bir şey | Mesajın son satırını okuyun, sonra onunla GitHub'da bir sorun (issue) açın. |

Her komut ayrıca bir **çıkış durumu** ile biter: 0 başarılı olduğu anlamına gelir. Bunu görmek için PowerShell'de `echo $LASTEXITCODE`, macOS ve Linux'ta `echo $?` yazın.
