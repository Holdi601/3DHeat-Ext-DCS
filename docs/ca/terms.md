---
title: Condicions i llicència
nav_order: 8
lang: "ca"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Condicions i llicència {#terms-and-licence}

## Què llegeix el lector {#what-the-reader-reads}

El lector llegeix fitxers de dades de la teva pròpia instal·lació de DCS World a l'ordinador ([Com es llegeixen els fitxers](reading.md)). No canvia res del joc i no es comunica amb cap servidor.

No s'inclou ni es redistribueix res del joc: cap fitxer del joc, cap codi del joc, cap DLL; les proves generen elles mateixes cada fitxer que llegeixen. Els nivells que escriu es queden al teu equip.

3DHeat DCS no està afiliat a Eagle Dynamics ni té el seu aval. DCS World i els noms i marques relacionats pertanyen als seus propietaris.

Titulars de drets: obriu una incidència a [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - responem ràpidament i retirem qualsevol cosa que se'ns demani.

## Llicència i fonts {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Necessita numpy (BSD-3-Clause); `fit` sobre un
`.parquet` necessita pyarrow (Apache-2.0). Escrit per a aquest projecte. Les
constants de projecció són dades publicades per pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); només se n'han pres els números. La
projecció és la sèrie de Krüger tal com la va donar C. F. F. Karney
(«Transverse Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). No s'ha pres cap codi de cap altre projecte.
