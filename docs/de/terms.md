---
title: "Bedingungen und Lizenz"
nav_order: 8
lang: "de"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Bedingungen und Lizenz {#terms-and-licence}

## Die Bedingungen von Eagle Dynamics {#eagle-dynamics-terms}

Gelesen am 07.11.2026 aus `Doc/license_en.txt` der Installation (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Das lizenzierte
"Programm" umfasst "THE DATA SUPPLIED WITH IT" (die mitgelieferten Daten). Klausel 3.1:

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

Klausel 3.1 (a) verbietet es, das Programm ohne Zustimmung zu "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" (verkaufen, handeln, vermieten, verleasen, unterlizenzieren, zusammenführen, anpassen, ändern oder modifizieren), und (e),
es "exploit this Program or any of its parts commercially" (kommerziell zu verwerten).

Was dieser Leser tut: Er liest Datendateien auf deinem eigenen Rechner, nachdem du sie installiert hast, außerhalb des Spiels.
Er verändert nichts am Spiel, bricht keine Verschlüsselung (die eine verschlüsselte Datei in einem Terrainordner
bleibt unberührt) und spricht mit keinem Server. Den Aufbau einer Datendatei zu ermitteln ist Reverse Engineering im Sinne
von 3.1 (c), und ein Level, das aus dem Terrain des Spiels gebaut wird, gilt womöglich als abgeleitetes Werk. Die Nutzung des
Lesers ist deine Entscheidung, für deinen eigenen Gebrauch; die Levels, die er schreibt, gehören dir zum Ansehen,
nicht zum Teilen oder Veröffentlichen. Deshalb ist es ein eigenes Paket.

Die zulässige Alternative, die keine Datei liest: Die eigene Missionsskripterstellung des Simulators kann den Boden abtasten
(`land.getHeight`, `land.getSurfaceType`) und Flugplätze auflisten (`world.getAirbases`), während eine Mission läuft. Dafür
braucht DCS pro Schauplatz stundenlang Laufzeit, und das Raster ist gröber; sie wurde nicht gebaut,
weil sich die Dateien als lesbar erwiesen.

## Lizenz und Quellen {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Braucht numpy (BSD-3-Clause); `fit` auf einer
`.parquet`-Datei braucht pyarrow (Apache-2.0). Für dieses Projekt geschrieben. Die Projektionskonstanten sind Fakten,
die pydcs veröffentlicht (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); übernommen wurden nur die Zahlen.
Die Projektion ist Krügers Reihe, so wie C. F. F. Karney sie angibt ("Transverse Mercator with an accuracy of a few
nanometers", Journal of Geodesy 85, 2011). Kein Code wurde aus einem anderen Projekt übernommen.
