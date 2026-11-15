---
title: "Ein Level bauen: level"
nav_order: 3
lang: "de"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Ein Level bauen: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Schritt für Schritt {#step-by-step}

Neu in der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).

1. Finde den Ordnernamen des Schauplatzes mit [`list`](list.md).
2. Bei einem kleinen Schauplatz baust du ihn ganz: `heat3d-dcs-maps level <theatre> -o levels`.
3. Bei einem großen wählst du eine Region: `--around <lat> <lon> <km>` (ein Quadrat so vieler km
   auf jeder Seite eines Punkts) oder `--bounds X0 Z0 X1 Z1` in DCS-Metern.
   Benenne sie mit `--name`.
4. Der Befehl gibt die Kacheln aus, während er sie liest, die Anzahl der Dreiecke, die geschriebene
   Datei und wie viele Städte des Schauplatzes auf dem Boden landen - eine Prüfung der Projektion, die
   "N von N" anzeigen sollte.
5. Lade `<folder>/<name>.glb` im Panel „Hintergrund / Level“ des Viewers und schalte
   **Erfasste Farbe** ein, um die Bodenklassen zu sehen.

![level auf einer synthetischen Installation](../assets/img/level.svg)

Eine Region desselben synthetischen Schauplatzes, in DCS-Metern:

![level mit --bounds und --name](../assets/img/level-bounds.svg)

## Optionen {#options}

| Option | Standard | Wirkung |
|---|---|---|
| `theatre` | - | der Ordnername unter `Mods\terrains`, so wie `list` ihn ausgibt (Groß-/Kleinschreibung egal) |
| `-o`, `--out` | erforderlich | der Ordner, in den `<name>.glb` und `<name>.json` geschrieben werden |
| `--dcs FOLDER` | gefunden | der DCS-World-Ordner ([wo er gefunden wird](list.md#where-the-install-is-found)) |
| `--name NAME` | der des Schauplatzes | der Name des Levels und seiner Dateien |
| `--around LAT LON KM` | - | nur ein Quadrat so vieler km auf jeder Seite eines Punkts |
| `--bounds X0 Z0 X1 Z1` | - | nur dieser Kasten, in DCS-Metern (x Nord, z Ost) |
| `--cell M` | `0` | das Netz ausdünnen: jeder Eckpunkt innerhalb von *M* Metern wird zu einem (0: die eigenen Dreiecke des Spiels) |
| `--seabed` | aus | den Meeresboden als Boden behalten (standardmäßig weggelassen) |
| `--no-water` | aus | das flache Meer weglassen |
| `--no-buildings` | aus | die Gebäude der Szene des Schauplatzes weglassen |
| `--force` | aus | eine sehr große Karte ganz in voller Auflösung exportieren |
| `--projection LON0 FE FN` | der des Schauplatzes | Transversale-Mercator-Konstanten für einen Schauplatz, den dieses Werkzeug nicht kennt ([fit](fit.md)) |

Jede Option, so wie das Programm sie ausgibt: [Befehlsreferenz](../cli-reference.md).

## Größe {#size}

Das Netz des Spiels ist adaptiv - offenes Meer in Dreiecken von Kilometern Breite, Küsten
und Straßen in wenigen Metern. Ein kleiner Schauplatz hat einige Millionen Dreiecke; die großen
haben Dutzende Millionen Eckpunkte. Ab 30 Millionen zu lesender Eckpunkte hört `level` auf
(Exit-Status 1) und fragt nach einer Region, einem dünneren Netz (`--cell 50`) oder `--force`.

Exit-Status: 0 fertig; 1 fehlgeschlagen oder zu groß; 2 die Installation oder der Schauplatz wurde nicht
gefunden (die gefundenen Schauplätze werden aufgelistet).

## Beispiele {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # whole, full detail
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # a 24 km square
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # a box in DCS metres
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # whole, thinned to 50 m
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # the ground alone
```

Was in den Dateien steckt: [Die Level-Dateien](output.md).
