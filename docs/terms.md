---
title: Terms and licence
nav_order: 8
---

# Terms and licence

## What the reader reads

The reader reads data files of your own DCS World installation on your
computer ([How the files are read](reading.md)). It changes nothing in the
game and talks to no server.

Nothing from the game is shipped or redistributed: no game files, no game
code, no DLLs; the tests build every file they read. The levels it writes stay
on your machine, and so does the catalogue `ranges` builds from your own
installation.

3DHeat DCS is not affiliated with or endorsed by Eagle Dynamics. DCS World and
related names and trademarks belong to their owners.

Rights holders: open an issue at
[github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) -
we respond quickly and remove anything on request.

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Needs numpy (BSD-3-Clause); `fit` on a
`.parquet` needs pyarrow (Apache-2.0). Written for this project. The
projection constants are facts published by pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); only the numbers were
taken. The projection is Krüger's series as C. F. F. Karney gives it
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). No code was taken from any other project.
