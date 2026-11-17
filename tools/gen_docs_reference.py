"""Write docs/cli-reference.md from the code itself, so the reference cannot drift.

The options come from the program's own `--help`; the level's parts, ground
classes and `.json` keys from a level built from the synthetic install the
tests make.

    python tools/gen_docs_reference.py          # rewrite the page
    python tools/gen_docs_reference.py --check  # exit 1 when the page is stale
"""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "cli-reference.md"
COMMAND = "heat3d-dcs-maps"
VERBS = ["list", "level", "towns", "fit", "ranges"]


def run(args):
    env = dict(os.environ, HEAT3D_NO_UPDATE="1", COLUMNS="88", PYTHONIOENCODING="utf-8",
               PYTHONPATH=str(ROOT) + os.pathsep + os.environ.get("PYTHONPATH", ""))
    r = subprocess.run([sys.executable, "-m", "heat3d_ext_dcs"] + args, capture_output=True, text=True,
                       env=env, encoding="utf-8", cwd=ROOT)
    return (r.stdout or r.stderr).rstrip()


def outputs():
    sys.path[:0] = [str(ROOT), str(ROOT / "tests")]
    os.environ["HEAT3D_NO_UPDATE"] = "1"
    import synth
    from heat3d_ext_dcs import cli, projection
    from heat3d_ext_dcs import level as lv
    from heat3d_ext_dcs.projection import Projection
    projection.THEATRES.setdefault("TestTheatre", Projection(0, 0.0, 0.0))
    lines = ["### Ground classes", "", "The colour each class is drawn with (Captured colour in the viewer).", "",
             "| Class | Colour (sRGB) |", "|---|---|"]
    lines += [f"| `{k}` | `#{''.join(f'{int(c * 255):02x}' for c in v)}` |" for k, v in lv.COLOURS.items()]
    with tempfile.TemporaryDirectory() as tmp:
        synth.theatre(Path(tmp) / "DCS")
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            cli.main(["level", "TestTheatre", "--dcs", str(Path(tmp) / "DCS"), "-o", str(Path(tmp) / "levels")])
        doc = json.loads((Path(tmp) / "levels" / "TestTheatre.json").read_text(encoding="utf-8"))
        raw = (Path(tmp) / "levels" / "TestTheatre.glb").read_bytes()
        n = int.from_bytes(raw[12:16], "little")
        nodes = [x.get("name", "") for x in json.loads(raw[20:20 + n])["nodes"]]
    lines += ["", "### `<name>.glb` parts", "", "Parts of the test level (each named `<part>:<Level>`): "
              + ", ".join(sorted({f"`{x.split(':')[0]}`" for x in nodes if ':' in x}))
              + " (a theatre whose scene has buildings adds `structure`).", "",
              "### `<name>.json`", "", "Top-level keys: " + ", ".join(f"`{k}`" for k in doc) + ".", ""]
    return lines


def build():
    out = ["---", "title: Command reference", "nav_order: 90", "---", "", "# Command reference", "",
           "Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.",
           "The other pages explain each command step by step.", "",
           f"## `{COMMAND}`", "", "```text", run(["--help"]), "```", ""]
    for v in VERBS:
        out += [f"## `{v}`", "", "```text", run([v, "--help"]), "```", ""]
    out += ["## Output", ""]
    return "\n".join(out + outputs())


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        sys.exit(0 if OUT.exists() and OUT.read_text(encoding="utf-8") == text else 1)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT.relative_to(ROOT))
