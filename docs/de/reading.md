---
title: "Wie die Dateien gelesen werden"
nav_order: 7
lang: "de"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Wie die Dateien gelesen werden {#how-the-files-are-read}

Nur `Mods/terrains/<theatre>/surface/*.surface5` (das Bodennetz),
`Scenes/*.scn5` (wo Objekte stehen, und die Box jedes Modells),
`AirfieldsTaxiways/*.rn4` und `map/towns.lua` (Ortsnamen, als Text gelesen,
nie ausgeführt). Nicht die verschlüsselte
`terrain.cfg.lua.pak.crypt`, nicht `manifest.bin`, nichts vom Programm.

Das `.surface5`-Format ist nicht dokumentiert; der Aufbau, wie er aus den Dateien gelesen wurde,
ist beschrieben in [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Kurz: ein Index von Kachel-Datensätzen (eine Transformation, Grenzen und Listen typisierter
Byte-Ströme, jede Liste gefolgt von dem Shader und Material, mit dem sie gezeichnet wird), dann die Rohdaten.
Sie ist weder komprimiert noch verschlüsselt. Der `Pbase`-Strom der Kachel
enthält ihre Eckpunkte; die Gruppe, die als `Land` gezeichnet wird, enthält die
Dreiecke und einen `TRITYPE` pro Dreieck, dessen niedrigstes Bit das Meer markiert; die
anderen Gruppen sind die Überlagerungen, die die Klassen oben ergeben.

## Geprüft {#verified}

- `list` las den Index jedes installierten Schauplatzes (Millionen bis Dutzende Millionen Bodeneckpunkte je),
  wobei jede stichprobenartig gelesene Kachel plausible Meter ergab.
- In Regionen zweier Schauplätze landeten die Städte aus `towns.lua` innerhalb von Metern bei einem
  Bodeneckpunkt, an Land, N von N; die höchste Erhebung traf den echten Gipfel bis auf zehn Meter; Flugplätze, Flüsse,
  Dörfer und Straßen erschienen in ihren Klassen. Beide Levels luden im Viewer, mit Stadtmarkierungen in denselben
  DCS-Metern, die auf dem Boden sitzen.
- In einer Szenen-Region lagen die Gebäudeplatzierungen auf ihrem Boden; Landebahnlichter zeichneten die
  Landebahn des Spiels nach, und Waggons und Mauersegmente richteten sich alle nach der dekodierten Richtung aus.
- `tests/` baut `.surface5`-Dateien im selben Aufbau, daher werden hier keine Spieldaten aufbewahrt;
  `tests/test_real_install.py` läuft auf der Installation des Rechners, auf dem die Tests laufen, und wird ohne eine übersprungen.

**Nicht geprüft:** ein großer Schauplatz als ganzes Level in einem Stück (die Größengrenze
oben gibt es aus gutem Grund), und andere DCS-Versionen als die getestete.

## Nicht gelesen {#not-read}

- **Gebäude als Formen** (die Modelle sind `.edm` in `Models/`): nur Boxen, mit Absicht. Ihr Aufbau und der der Szene
  steht in [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); jeder
  installierte Schauplatz wird gelesen (zwei ältere Schauplätze in einer Variante des Aufbaus, die der Leser ebenfalls kennt).
- Bäume, Lichter und die anderen Objekte der Szene: gelesen, nicht gezeichnet.
- **Das Straßennetz als Graph** (`roads/*.rn4`): nicht dekodiert.
- Texturen, Bäume, die Wellen des Meeres, die niedrigeren Detailstufen des Geländes.
