---
title: "Bedingungen und Lizenz"
nav_order: 8
lang: "de"
source: terms.md
source_hash: "ec853e6890da"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Was der Leser liest {#what-the-reader-reads}

Der Leser liest Datendateien deiner eigenen DCS-World-Installation auf deinem Rechner ([Wie die Dateien gelesen werden](reading.md)). Er verändert nichts am Spiel und spricht mit keinem Server.

Nichts aus dem Spiel wird mitgeliefert oder weitergegeben: keine Spieldateien, kein Spielcode, keine DLLs; die Tests bauen jede Datei, die sie lesen, selbst. Die Levels, die es schreibt, bleiben auf deinem Rechner, ebenso der Katalog, den `ranges` aus deiner eigenen Installation baut.

3DHeat DCS steht in keiner Verbindung zu Eagle Dynamics und wird von dort weder unterstützt noch empfohlen. DCS World und zugehörige Namen und Marken gehören ihren Inhabern.

Rechteinhaber: Eröffnet ein Issue unter [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - wir antworten schnell und entfernen auf Anfrage alles.

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Braucht numpy (BSD-3-Clause); `fit` auf einer
`.parquet`-Datei braucht pyarrow (Apache-2.0). Für dieses Projekt geschrieben. Die Projektionskonstanten sind Fakten,
die pydcs veröffentlicht (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); übernommen wurden nur die Zahlen.
Die Projektion ist Krügers Reihe, so wie C. F. F. Karney sie angibt ("Transverse Mercator with an accuracy of a few
nanometers", Journal of Geodesy 85, 2011). Kein Code wurde aus einem anderen Projekt übernommen.
