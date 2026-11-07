"""
On the DCS install of the machine running the tests, when there is one: every
version-5 theatre's index is read, and on a small piece of one theatre the
place names the game lists land on its ground. Skipped without DCS.
"""

from __future__ import annotations

import pytest

from heat3d_ext_dcs import install, projection, towns
from heat3d_ext_dcs.level import around, build, ground_height
from heat3d_ext_dcs.surface5 import Surface5

DCS = install.find()
pytestmark = pytest.mark.skipif(DCS is None, reason="no DCS World install on this machine")


def _theatres():
    return [t for t in install.theatres(DCS) if t.surface] if DCS else []


@pytest.mark.parametrize("t", _theatres(), ids=lambda t: t.name)
def test_index_reads(t):
    with Surface5(t.surface) as s:
        ground = s.ground_tiles
        assert ground and all(g.vertex_count > 0 for g in ground)
        first = s.positions(ground[0])
        assert abs(first).max() < 5e6  # metres, not noise


def test_towns_land_on_the_ground():
    # The smallest theatre with towns and a projection, read around its first town only.
    ts = [t for t in _theatres() if projection.for_theatre(t.name) and towns.read(t.towns)]
    if not ts:
        pytest.skip("no theatre with towns and a known projection")
    t = min(ts, key=lambda t: t.size)
    proj = projection.for_theatre(t.name)
    places = towns.read(t.towns)
    with Surface5(t.surface) as s:
        lv = build(s, t.name, region=around(proj, places[0].lat, places[0].lon, 3.0))
    inside = [p for p in places if abs(proj.to_dcs(p.lat, p.lon)[0] - proj.to_dcs(places[0].lat, places[0].lon)[0]) < 2500
              and abs(proj.to_dcs(p.lat, p.lon)[1] - proj.to_dcs(places[0].lat, places[0].lon)[1]) < 2500]
    heights = [ground_height(lv, *proj.to_dcs(p.lat, p.lon), reach=200.0) for p in inside]
    assert all(h is not None and h > -2.0 for h in heights), (t.name, heights)
