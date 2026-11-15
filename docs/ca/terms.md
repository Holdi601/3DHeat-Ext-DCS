---
title: Condicions i llicència
nav_order: 8
lang: ca
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Condicions i llicència {#terms-and-licence}

## Les condicions d'Eagle Dynamics {#eagle-dynamics-terms}

Llegit el 2026-11-07 de `Doc/license_en.txt` de la instal·lació (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). El
«Programa» inclòs en la llicència inclou «THE DATA SUPPLIED WITH IT». Clàusula 3.1:

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

La clàusula 3.1 (a) prohibeix «sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program» sense consentiment, i (e) prohibeix «exploit this
Program or any of its parts commercially».

Què fa aquest lector: llegeix fitxers de dades a la seva pròpia màquina, després que els
hàgiu instal·lat, fora del joc. No canvia res del joc, no trenca cap xifratge (l'únic fitxer
xifrat d'una carpeta de terreny es deixa en pau) i no parla amb cap servidor. Esbrinar la
disposició d'un fitxer de dades és enginyeria inversa en el sentit de 3.1 (c), i un nivell
construït a partir del terreny del joc es pot considerar una obra derivada. Usar el lector és
una decisió vostra, per al vostre propi ús; els nivells que escriu són vostres per veure'ls, no per
compartir-los ni publicar-los. Per això és un paquet separat.

L'alternativa autoritzada, que no llegeix cap fitxer: el propi scripting de missions del simulador
pot mostrejar el terreny (`land.getHeight`, `land.getSurfaceType`) i enumerar les bases aèries
(`world.getAirbases`) mentre s'executa una missió. Necessita DCS en marxa durant hores per
teatre i dona una quadrícula més grollera; no es va construir, perquè els fitxers van resultar
llegibles.

## Llicència i fonts {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Necessita numpy (BSD-3-Clause); `fit` sobre un
`.parquet` necessita pyarrow (Apache-2.0). Escrit per a aquest projecte. Les
constants de projecció són dades publicades per pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); només se n'han pres els números. La
projecció és la sèrie de Krüger tal com la va donar C. F. F. Karney
(«Transverse Mercator with an accuracy of a few nanometers», Journal of
Geodesy 85, 2011). No s'ha pres cap codi de cap altre projecte.
