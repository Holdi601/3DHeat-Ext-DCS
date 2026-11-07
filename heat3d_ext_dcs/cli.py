"""
heat3d-dcs-maps list                     the theatres installed, and whether each can be read
heat3d-dcs-maps level <theatre> -o <out> one theatre's ground and sea as a 3DHeat level
heat3d-dcs-maps towns <theatre>          its place names, with DCS coordinates
heat3d-dcs-maps fit <recording>          a theatre's projection from a flight that recorded x, z, lat and lon

`level` writes `<out>/<name>.glb` and `<name>.json` beside it (what was read,
the projection, the bounds, the towns and how many sit on land).
Exit status: 0 done, 1 failed, 2 nothing found (no DCS install, no such theatre).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from . import __version__
from . import glb, install, projection, towns
from .level import COLOURS, Region, around, build, estimate_vertices, fmt_bounds, ground_height
from .surface5 import FormatError, Surface5

#: Above this many vertices to read, a whole-map export asks for --cell, a region or --force.
LARGE = 30_000_000


def _dcs(args) -> Path | None:
    dcs = install.find(args.dcs)
    if dcs is None:
        print("no DCS World install found: give it with --dcs <folder> (the one holding Mods\\terrains)", file=sys.stderr)
    return dcs


def cmd_list(args) -> int:
    dcs = _dcs(args)
    if dcs is None:
        return 2
    print(f"DCS World at {dcs}")
    for t in install.theatres(dcs):
        if t.surface is None:
            print(f"  {t.name:16s} no .surface5 (not a version-5 terrain)")
            continue
        state = "readable"
        n = tiles = 0
        try:
            with Surface5(t.surface) as s:
                ground = s.ground_tiles
                tiles = len(ground)
                n = sum(x.vertex_count for x in ground)
        except (FormatError, OSError) as e:
            state = f"not readable: {e}"
        p = "lat/lon" if projection.for_theatre(t.name) else "no lat/lon"
        print(f"  {t.name:16s} {t.size / 1e9:6.1f} GB  {tiles:6d} tiles  {n / 1e6:6.1f} M vertices  {p:10s}  {state}")
    return 0


def _projection(args, name: str):
    if getattr(args, "projection", None):
        lon0, fe, fn = args.projection
        return projection.Projection(lon0, fe, fn, source="given on the command line")
    return projection.for_theatre(name)


def _region(args, proj) -> Region | None:
    if args.bounds:
        return Region(*args.bounds)
    if args.around:
        if proj is None:
            raise SystemExit("--around needs latitude/longitude, which this theatre has no projection for: use --bounds")
        return around(proj, *args.around)
    return None


def cmd_level(args) -> int:
    dcs = _dcs(args)
    if dcs is None:
        return 2
    t = install.theatre(dcs, args.theatre)
    if t is None or t.surface is None:
        names = ", ".join(x.name for x in install.theatres(dcs) if x.surface)
        print(f"no theatre {args.theatre!r} with a .surface5; installed: {names}", file=sys.stderr)
        return 2
    proj = _projection(args, t.name)
    region = _region(args, proj)
    name = args.name or t.name
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        with Surface5(t.surface) as s:
            need = estimate_vertices(s, region)
            if need > LARGE and not args.cell and not args.force:
                print(
                    f"{t.name}: {need / 1e6:.0f} M vertices to read for the whole map at full detail; "
                    "pick a region (--around LAT LON KM or --bounds), thin it (--cell 50), or --force",
                    file=sys.stderr,
                )
                return 1
            last = [0.0]

            def progress(i: int, n: int) -> None:
                now = time.monotonic()
                if now - last[0] > 5 or i == n:
                    last[0] = now
                    print(f"  tile {i} of {n}", flush=True)

            level = build(s, name, region=region, cell=args.cell, seabed=args.seabed, water=not args.no_water,
                          progress=progress)
    except FormatError as e:
        print(f"{t.name}: not readable: {e}", file=sys.stderr)
        return 1
    if not level.triangle_count:
        print(f"{t.name}: nothing inside the region", file=sys.stderr)
        return 1
    path = out / f"{name}.glb"
    size = glb.write(path, level.parts())

    places = []
    on_land = 0
    for town in towns.read(t.towns):
        row = {"name": town.display, "lat": town.lat, "lon": town.lon}
        if proj is not None:
            x, z = proj.to_dcs(town.lat, town.lon)
            if region is not None and not region.holds(x, z):
                continue
            y = ground_height(level, x, z)
            row.update(x=round(x, 1), z=round(z, 1), ground=None if y is None else round(y, 1))
            on_land += y is not None and y > -1.0
        places.append(row)
    bounds = fmt_bounds(level)
    corners = None
    if proj is not None and bounds:
        corners = {
            "south_west": proj.to_latlon(bounds["x"][0], bounds["z"][0]),
            "north_east": proj.to_latlon(bounds["x"][1], bounds["z"][1]),
        }
    st = t.surface.stat()
    meta = {
        "tool": "heat3d_ext_dcs",
        "version": __version__,
        "written": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "theatre": t.name,
        "level": name,
        "source": {
            "surface5": str(t.surface),
            "bytes": st.st_size,
            "modified": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec="seconds"),
        },
        "coordinates": "DCS world metres: x north, y up, z east. The glTF axes are the same (X = x, Y = y, Z = z), "
        "so DCS telemetry in its own metres (Y up, scale 1) lands on the level with no placement step.",
        "projection": proj.as_dict() if proj else None,
        "bounds": bounds,
        "bounds_latlon": corners,
        "region": None if region is None else {"x": [region.x0, region.x1], "z": [region.z0, region.z1]},
        "cell": args.cell,
        "seabed": args.seabed,
        "tiles": level.tiles,
        "triangles": {"ground": sum(len(p.triangles) for p in level.ground),
                      "water": sum(len(p.triangles) for p in level.water)},
        "classes": level.classes,
        "colours": {k: list(v) for k, v in COLOURS.items()},
        "towns_on_land": f"{on_land} of {len(places)}" if proj else None,
        "towns": places,
        "glb_bytes": size,
        "seconds": round(time.monotonic() - started, 1),
    }
    (out / f"{name}.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False), encoding="utf-8")
    print(
        f"{t.name}: {level.triangle_count:,} triangles ({meta['triangles']['ground']:,} ground, "
        f"{meta['triangles']['water']:,} sea) from {level.tiles} tiles, {size / 1e6:.0f} MB -> {path}"
    )
    if proj is not None:
        print(f"  towns on land: {meta['towns_on_land']} (a check of the projection)")
    return 0


def cmd_towns(args) -> int:
    dcs = _dcs(args)
    if dcs is None:
        return 2
    t = install.theatre(dcs, args.theatre)
    if t is None:
        print(f"no theatre {args.theatre!r}", file=sys.stderr)
        return 2
    proj = projection.for_theatre(t.name)
    rows = []
    for town in towns.read(t.towns):
        row = {"name": town.display, "lat": town.lat, "lon": town.lon}
        if proj:
            x, z = proj.to_dcs(town.lat, town.lon)
            row.update(x=round(x, 1), z=round(z, 1))
        rows.append(row)
    print(json.dumps(rows, indent=1, ensure_ascii=False))
    return 0


def samples(path: Path, limit: int = 5000) -> list[tuple[float, float, float, float]]:
    """(lat, lon, x, z) rows from a .csv, .jsonl or .parquet that has all four columns."""
    rows: list[dict] = []
    if path.suffix == ".parquet":
        import pyarrow.parquet as pq  # optional: only this verb needs it

        rows = pq.read_table(path, columns=["lat", "lon", "x", "z"]).to_pylist()
    elif path.suffix == ".jsonl":
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    else:
        import csv

        with open(path, newline="", encoding="utf-8", errors="replace") as f:
            rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        try:
            v = tuple(float(r[k]) for k in ("lat", "lon", "x", "z"))
        except (KeyError, TypeError, ValueError):
            continue
        if all(map(math.isfinite, v)):
            out.append(v)
    step = max(1, len(out) // limit)
    return out[::step]


def cmd_fit(args) -> int:
    path = Path(args.recording)
    if not path.is_file():
        print(f"no file {path}", file=sys.stderr)
        return 2
    pts = samples(path)
    if len(pts) < 3:
        print(f"{path.name}: fewer than three rows with lat, lon, x and z", file=sys.stderr)
        return 1
    proj, err = projection.fit(pts)
    print(json.dumps({**proj.as_dict(), "points": len(pts), "rms_metres": round(err, 3)}, indent=1))
    verdict = "a good fit" if err < 5 else "a poor fit: the points may not be from one theatre"
    print(f"{verdict} ({err:.2f} m rms over {len(pts)} points); use it with:")
    print(f"  heat3d-dcs-maps level <theatre> --projection {proj.central_meridian} "
          f"{proj.false_easting:.3f} {proj.false_northing:.3f} -o <out>")
    return 0 if err < 5 else 1


def main(argv: list[str] | None = None) -> int:
    try:
        import heat3d_update

        heat3d_update.startup("heat3d_ext_dcs")
    except Exception:  # an update check never stops an export
        pass
    ap = argparse.ArgumentParser(prog="heat3d-dcs-maps", description="DCS World theatres into 3DHeat levels")
    ap.add_argument("--version", action="version", version=__version__)
    sub = ap.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", help="the theatres installed, and whether each can be read")
    p.add_argument("--dcs", help="the DCS World folder (the one holding Mods\\terrains)")
    p.set_defaults(run=cmd_list)

    p = sub.add_parser("level", help="one theatre's ground and sea as a .glb level")
    p.add_argument("theatre", help="the folder name under Mods\\terrains, e.g. MarianasWWII")
    p.add_argument("-o", "--out", required=True, help="folder to write <name>.glb and <name>.json into")
    p.add_argument("--dcs", help="the DCS World folder")
    p.add_argument("--name", help="the level's name (default: the theatre's)")
    p.add_argument("--cell", type=float, default=0.0, help="thin the mesh to this many metres (default 0: the game's own triangles)")
    where = p.add_mutually_exclusive_group()
    where.add_argument("--around", nargs=3, type=float, metavar=("LAT", "LON", "KM"),
                       help="only a square this many km either side of a point")
    where.add_argument("--bounds", nargs=4, type=float, metavar=("X0", "Z0", "X1", "Z1"),
                       help="only this box, in DCS metres (x north, z east)")
    p.add_argument("--seabed", action="store_true", help="keep the sea floor as ground (default: left out)")
    p.add_argument("--no-water", action="store_true", help="leave out the flat sea")
    p.add_argument("--force", action="store_true", help="export a very large map whole at full detail")
    p.add_argument("--projection", nargs=3, type=float, metavar=("LON0", "FE", "FN"),
                   help="the theatre's Transverse Mercator constants, for one this tool does not know (see fit)")
    p.set_defaults(run=cmd_level)

    p = sub.add_parser("towns", help="a theatre's place names with DCS coordinates, as JSON")
    p.add_argument("theatre")
    p.add_argument("--dcs", help="the DCS World folder")
    p.set_defaults(run=cmd_towns)

    p = sub.add_parser("fit", help="a theatre's projection from a recording holding x, z, lat and lon")
    p.add_argument("recording", help=".parquet, .jsonl or .csv with columns lat, lon, x, z (DCS metres)")
    p.set_defaults(run=cmd_fit)

    args = ap.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    sys.exit(main())
