"""
The standalone app's description of this tool (app/spec.py): the DCS World
install it reads, its theatres as maps (new ones after an update or a new
terrain module are found by app/manifest.py), and how one theatre becomes a
level. `python -m heat3d_ext_dcs.standalone_spec` runs the app from a
checkout; the release executables run the same.
"""

from __future__ import annotations

import re
from pathlib import Path

from . import __version__
from .app.spec import Check, GameSpec, MapSource, Spec

#: A theatre above this many vertices at full detail is thinned to `THIN` metres for a one-click export.
THIN = 50.0


def _find(given: str | None) -> Path | None:
    from .install import find

    return find(given)


def _theatres(dcs: Path):
    from .install import theatres

    return [t for t in theatres(dcs) if t.surface is not None]


def _maps(dcs: Path) -> list[MapSource]:
    out = []
    for t in _theatres(dcs):
        sources = [t.surface] + [p for p in (t.scene, t.towns) if p is not None and p.is_file()]
        out.append(MapSource(t.name, t.name, sources))
    return out


def _extract(dcs: Path, m: MapSource, out: Path, log) -> list[Path]:
    from . import cli
    from .level import estimate_vertices
    from .surface5 import Surface5

    argv = ["level", m.id, "-o", str(out), "--dcs", str(dcs)]
    with Surface5(m.sources[0]) as s:
        need = estimate_vertices(s, None)
    if need > cli.LARGE:
        log(f"{m.id}: {need / 1e6:.0f} M vertices at full detail; thinned to {THIN:g} m cells")
        argv += ["--cell", str(THIN)]
    code = cli.main(argv)
    if code != 0:
        raise RuntimeError(f"heat3d-dcs-maps level exited {code}")
    # The theatre's airbases, runways and parking stands; a theatre without any is not an error.
    cli.main(["layouts", m.id, "-o", str(out), "--dcs", str(dcs)])
    return [p for p in (out / f"{m.id}.glb", out / f"{m.id}.json", out / f"{m.id}.layouts.json") if p.is_file()]


def _build(dcs: Path) -> str | None:
    try:
        text = (dcs / "autoupdate.cfg").read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    found = re.search(r'"version"\s*:\s*"([^"]+)"', text)
    return found.group(1)[:40] if found else None


def _checks(found: dict, levels: Path) -> list[Check]:
    dcs = found.get("dcs")
    if dcs is None:
        return []
    n = len(_theatres(dcs))
    return [Check(
        "theatres", "Theatres with a version-5 terrain", n > 0,
        f"{n} found under Mods/terrains" if n else "none found under Mods/terrains (no terrain this reader reads)",
    )]


SPEC = Spec(
    id="heat3d-dcs",
    name="3DHeat DCS",
    repo="Holdi601/3DHeat-Ext-DCS",
    version=__version__,
    tools={"heat3d-dcs-maps": "heat3d_ext_dcs.cli:main"},
    default_tool="heat3d-dcs-maps",
    description="DCS World theatres as 3D levels for the 3DHeat viewer",
    module="heat3d_ext_dcs.standalone_spec",
    games=[GameSpec(
        key="dcs", label="DCS World", find=_find, subdir="dcs", build=_build,
        maps=_maps, extract=_extract,
        existing_outputs=lambda out, m: [out / f"{m.id}.glb"],
        output_version="0.3.0",
        platforms=("windows-x64", "linux-x64"),
    )],
    checks=_checks,
    min_free_gb=5.0,
    notice="Not affiliated with or endorsed by Eagle Dynamics.",
)

if __name__ == "__main__":
    from . import update
    from .app.entry import main

    raise SystemExit(main(SPEC, apply_source=update.apply))
