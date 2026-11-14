---
title: Terms and licence
nav_order: 8
---

# Terms and licence

## Eagle Dynamics' terms

Read on 2026-11-07 from `Doc/license_en.txt` of the install (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). The licensed
"Program" includes "THE DATA SUPPLIED WITH IT". Clause 3.1:

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

Clause 3.1 (a) forbids to "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" without consent, and (e) to "exploit this
Program or any of its parts commercially".

What this reader does: it reads data files on your own machine, after you
installed them, outside the game. It changes nothing in the game, breaks no
encryption (the one enciphered file in a terrain folder is left alone) and
talks to no server. Working out the layout of a data file is reverse
engineering in the sense of 3.1 (c), and a level built from the game's
terrain is arguably a derivative work. Using the reader is your decision,
for your own use; the levels it writes are yours to view, not to share or
publish. That is why it is a separate package.

The sanctioned alternative, which reads no file: the sim's own mission
scripting can sample the ground (`land.getHeight`, `land.getSurfaceType`)
and list airbases (`world.getAirbases`) while a mission runs. It needs DCS
running for hours per theatre and gives a coarser grid; it was not built,
because the files proved readable.

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Needs numpy (BSD-3-Clause); `fit` on a
`.parquet` needs pyarrow (Apache-2.0). Written for this project. The
projection constants are facts published by pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); only the numbers were
taken. The projection is Krüger's series as C. F. F. Karney gives it
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No code was taken from any other project.
