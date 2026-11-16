---
title: "Kushtet dhe licenca"
nav_order: 8
lang: "sq"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Kushtet dhe licenca {#terms-and-licence}

## Çfarë lexon lexuesi {#what-the-reader-reads}

Lexuesi lexon skedarë të dhënash nga instalimi yt i DCS World në kompjuterin tënd ([Si lexohen skedarët](reading.md)). Nuk ndryshon asgjë në lojë dhe nuk flet me asnjë server.

Asgjë nga loja nuk shpërndahet as nuk rishpërndahet: asnjë skedar loje, asnjë kod loje, asnjë DLL; testet e ndërtojnë vetë çdo skedar që lexojnë. Nivelet që shkruan mbeten në kompjuterin tënd.

3DHeat DCS nuk është i lidhur me Eagle Dynamics dhe nuk miratohet prej saj. DCS World dhe emrat e markat tregtare përkatëse u përkasin pronarëve të tyre.

Mbajtës të drejtash: hapni një çështje në [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - përgjigjemi shpejt dhe heqim çdo gjë me kërkesë.

## Licenca dhe burimet {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Kërkon numpy (BSD-3-Clause); `fit` mbi një
`.parquet` kërkon pyarrow (Apache-2.0). Shkruar për këtë projekt. Konstantet e
projeksionit janë fakte të botuara nga pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); u morën vetëm numrat. Projeksioni
është seria e Krüger-it siç e jep C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nuk u mor kod nga asnjë projekt tjetër.
