---
title: "Waffen- und Sensorreichweiten: ranges"
nav_order: 5.5
lang: "de"
source: ranges.md
source_hash: "6815981b222e"
nav_exclude: true
search_exclude: true
---
# Waffen- und Sensorreichweiten: `ranges` {#weapon-and-sensor-ranges-ranges}

```text
heat3d-dcs-maps ranges [-o FILE] [--dcs FOLDER] [--saved-games FOLDER | --no-saved-games]
```

Baut einen Katalog aus deiner eigenen Installation: wie weit jede Waffe
reicht, wie weit und wie breit jeder Sensor sieht und welche Einheiten sie
tragen. Die Match-Wiedergabe des 3DHeat-Viewers liest ihn, um für
DCS-World-Aufnahmen Einsatzreichweiten, Sichtkegel und Sensorsektoren zu
zeichnen, statt ihrer eigenen allgemeinen Werte.

1. Führe `heat3d-dcs-maps ranges -o ranges.json` aus.
2. Lege `ranges.json` dorthin, wo der Viewer danach sucht (seine
   Dokumentation sagt, wo). Sie bleibt auf deinem Rechner.

| Option | Macht |
|---|---|
| `-o`, `--out FILE` | die `.json`, die geschrieben wird (Standard: `ranges.json` im aktuellen Ordner) |
| `--dcs FOLDER` | der DCS-World-Ordner |
| `--saved-games FOLDER` | der DCS-Ordner unter Gespeicherte Spiele, dessen `Mods` mitgelesen werden (Standard: gefunden) |
| `--no-saved-games` | nur die Installation lesen |

Es dauert ein paar Sekunden. Exit-Status: 0 fertig; 1 nichts zum Schreiben
gefunden; 2 keine Installation.

## Was hineinkommt {#what-goes-in}

Die Definitionen der Module und Asset-Pakete (`CoreMods`, `Mods` und die Mods
unter Gespeicherte Spiele), jeweils ab ihrer `entry.lua` gelesen, so wie das
Spiel sie lädt:

- **Waffen**: Raketen, gelenkte Bomben und Torpedos mit ihren angegebenen
  Reichweiten (`D_min`, `D_max`, `Range_max`), Zielhöhen, Suchkopf,
  Abschusswinkel, Lastvielfachem und Geschwindigkeit; die Geschütze von
  Bodeneinheiten und Schiffen mit der Entfernung, ab der sie feuern, ihrem
  höchsten Ziel und ihrer Mündungsgeschwindigkeit. Eine Waffe, deren Dateien
  keine Reichweite angeben (die meisten ungelenkten Bomben und Raketen),
  bleibt weg.
- **Sensoren**: Radare mit ihrer Erfassungsreichweite je Halbkugel und
  Aspekt, ihrem Suchbereich und der Bodenkartierung; Kameras und
  Zielbehälter mit ihrem Sichtfeld und Zoom.
- **Einheiten**: Flugzeuge, Hubschrauber, Bodeneinheiten und Schiffe, unter
  den Namen, die eine Aufnahme verwendet (der Typname und
  der Anzeigename), mit den Waffen an ihren Stationen oder Startern und den
  Sensoren, die sie nennen.

Die Kerndatenbank, die das Spiel gepackt hält, wird nicht gelesen. Ein
Sensor, den nur sie definiert, erscheint mit Name und Art, ohne Zahlen
(`"declared": false`).

## Die Datei {#the-file}

Eine Zeile JSON (`version` 1): `weapons` (jede mit `id`, `cls`, `name`,
`range` als Minimum, typischer und maximaler Wert in Metern, `shape`, `cone`,
`elev`, `alt`, `los`, den `labels`, die eine Aufnahme verwenden kann, und
`detail`), `sensors` (nach ID: `kind`, `name`, `range`, `az`, `el`, `rcsRef`,
`modes`, `mount`, `detail`) und `units` (`names`, `weapons`, `sensors`,
`optics`). Durchgehend Meter und Grad. Ein Wert, den die Dateien nicht
angeben, bleibt weg und wird nie geschätzt.
