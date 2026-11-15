---
title: "Projections: fit"
nav_order: 6
---

# Projections: `fit`

```text
heat3d-dcs-maps fit <recording>
```

Every theatre is a Transverse Mercator projection with its own constants. The
tool knows them for the theatres it was checked on; for one it does not know,
`fit` finds them from any recording that holds both latitude/longitude and
DCS metres, such as a 3DHeat Watcher session of one flight.

1. Record a flight on the theatre with the 3DHeat Watcher (or make any
   recording with columns `lat`, `lon`, `x`, `z` in DCS metres: x is metres
   north, z metres east, as everywhere in DCS).
2. Run `heat3d-dcs-maps fit "<session>/heat.parquet"` (or a `.jsonl` or `.csv`).
3. It prints the fitted projection as JSON, the root mean square error over
   the points, and the `--projection` arguments to use.
4. Build the level with them:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![fit on a synthetic recording](assets/img/fit.svg)

The recording in the picture is nine points made from a known projection,
which `fit` finds back to the millimetre.

| Argument | Does |
|---|---|
| `recording` | `.parquet`, `.jsonl` or `.csv` with columns `lat`, `lon`, `x`, `z` (DCS metres); rows that do not read are skipped |

The projection is Krüger's series as C. F. F. Karney gives it ("Transverse
Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Exit status: 0 a good fit (under 5 m root mean square); 1 a poor fit, or
fewer than three usable rows; 2 the file was not found.
