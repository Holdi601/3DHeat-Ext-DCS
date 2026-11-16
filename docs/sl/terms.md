---
title: "Pogoji in licenca"
nav_order: 8
lang: "sl"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Pogoji in licenca {#terms-and-licence}

## Kaj bere bralnik {#what-the-reader-reads}

Bralnik bere podatkovne datoteke tvoje lastne namestitve DCS World na tvojem računalniku ([Kako se datoteke berejo](reading.md)). V igri ničesar ne spremeni in se ne povezuje z nobenim strežnikom.

Nič iz igre se ne priloži ali naprej razširja: nobenih datotek igre, nobene kode igre, nobenih DLL; testi sami zgradijo vsako datoteko, ki jo berejo. Ravni, ki jih zapiše, ostanejo na tvojem računalniku.

3DHeat DCS ni povezan s Eagle Dynamics niti ga ta ne podpira. DCS World ter povezana imena in blagovne znamke pripadajo svojim lastnikom.

Imetniki pravic: odprite zahtevek na [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - odgovorimo hitro in na zahtevo odstranimo karkoli.

## Licenca in viri {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Potrebuje numpy
(BSD-3-Clause); `fit` na `.parquet` potrebuje pyarrow (Apache-2.0). Napisano za ta projekt. Konstante
projekcij so dejstva, ki jih objavlja pydcs (github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); vzete
so bile samo številke. Projekcija je Krügerjeva vrsta, kot jo podaja C. F. F. Karney ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Nobena koda ni vzeta iz
drugega projekta.
