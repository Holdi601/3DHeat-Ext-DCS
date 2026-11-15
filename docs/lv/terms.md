---
title: Noteikumi un licence
nav_order: 8
lang: lv
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Noteikumi un licence {#terms-and-licence}

## Eagle Dynamics noteikumi {#eagle-dynamics-terms}

Nolasīts 2026-11-07 no uzstādījuma faila `Doc/license_en.txt` (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). Licencētajā "Program" ietilpst
"THE DATA SUPPLIED WITH IT". 3.1. punkts:

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

3.1. punkta (a) apakšpunkts aizliedz "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" bez atļaujas, un (e) apakšpunkts - "exploit this
Program or any of its parts commercially".

Ko dara šis lasītājs: tas nolasa datu failus jūsu datorā, pēc tam, kad tie ir uzstādīti,
ārpus spēles. Tas nemaina neko spēlē, nelauž šifrējumu (vienīgais šifrētais
fails teātra mapē tiek atstāts neskarts) un nesazinās ar serveri. Datu faila izkārtojuma
noskaidrošana ir reversā inženierija 3.1. punkta (c) izpratnē, un līmenis, kas veidots no
spēles teātra, iespējams ir atvasināts darbs. Lasītāja izmantošana ir jūsu lēmums, jūsu pašu
lietojumam; līmeņi, ko tas raksta, ir jūsu, lai tos skatītu, nevis lai kopīgotu vai publicētu.
Tāpēc tas ir atsevišķa pakotne.

Sankcionētā alternatīva, kas nelasa nevienu failu: pašas simulatora misiju skriptēšana var paraugot zemi (`land.getHeight`, `land.getSurfaceType`) un uzskaitīt lidlaukus (`world.getAirbases`), kamēr darbojas misija. Tam vajag DCS darbību stundām katram teātrim un tas dod rupjāku režģi; tas netika veidots, jo faili izrādījās lasāmi.

## Licence un avoti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Vajag numpy (BSD-3-Clause); `fit` ar
`.parquet` vajag pyarrow (Apache-2.0). Rakstīts šim projektam. Projekcijas konstantes ir fakti, ko publicējis pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); ņemti tikai skaitļi. Projekcija ir Krīgera rinda, kā to dod C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). Kods no citiem projektiem nav ņemts.
