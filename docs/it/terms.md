---
title: Condizioni e licenza
nav_order: 8
lang: "it"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Condizioni e licenza {#terms-and-licence}

## Le condizioni di Eagle Dynamics {#eagle-dynamics-terms}

Lette il 2026-11-07 da `Doc/license_en.txt` dell'installazione (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Il "Programma" concesso in licenza
comprende "THE DATA SUPPLIED WITH IT" (i dati forniti con esso). La clausola 3.1 dice, in
inglese:

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

La clausola 3.1 (a) vieta di "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" senza consenso, e (e) di "exploit this
Program or any of its parts commercially" (sfruttare commercialmente questo
Programma o una sua parte).

Cosa fa questo lettore: legge file di dati sulla tua macchina, dopo che li hai installati, fuori dal
gioco. Non modifica nulla nel gioco, non rompe nessuna cifratura (l'unico file cifrato in una
cartella del terreno viene lasciato stare) e non parla con nessun server. Capire il layout di un file
di dati è ingegneria inversa ai sensi della clausola 3.1 (c), e un livello costruito dal terreno del
gioco è discutibilmente un'opera derivata. Usare il lettore è una tua decisione, per uso personale; i
livelli che scrive sono tuoi da visualizzare, non da condividere o pubblicare. Per questo è un
pacchetto separato.

L'alternativa autorizzata, che non legge nessun file: gli script di missione del simulatore possono
campionare il terreno (`land.getHeight`, `land.getSurfaceType`) ed elencare gli aeroporti
(`world.getAirbases`) mentre una missione è in corso. Richiede DCS in esecuzione per ore per ogni
teatro e dà una griglia più grossolana; non è stata realizzata, perché i file si sono rivelati
leggibili.

## Licenza e fonti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Richiede numpy
(BSD-3-Clause); `fit` su un `.parquet` richiede pyarrow (Apache-2.0). Scritto per questo progetto. Le
costanti di proiezione sono dati pubblicati da pydcs (github.com/pydcs/dcs,
`dcs/terrain/*/projection.py`); sono stati presi solo i numeri. La proiezione è la serie di Krüger
come la dà C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nessun codice è stato preso da altri progetti.
