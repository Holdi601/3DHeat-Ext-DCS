"""Transverse Mercator: DCS metres <-> latitude and longitude."""

import math

import pytest

from heat3d_ext_dcs.projection import THEATRES, Projection, fit, for_theatre

P = Projection(0, 0.0, 0.0)


def test_origin_and_meridian_arc():
    assert P.to_dcs(0.0, 0.0) == pytest.approx((0.0, 0.0), abs=1e-6)
    # The WGS84 meridian arc from the equator to 1 degree north is 110574.39 m; times the scale 0.9996.
    x, z = P.to_dcs(1.0, 0.0)
    assert x == pytest.approx(110574.39 * 0.9996, abs=0.05)
    assert z == pytest.approx(0.0, abs=1e-6)


def test_east_is_positive_z_north_is_positive_x():
    x, z = P.to_dcs(45.0, 1.0)
    assert z > 0 and x > 0
    x2, z2 = P.to_dcs(45.0, -1.0)
    assert z2 == pytest.approx(-z) and x2 == pytest.approx(x)


@pytest.mark.parametrize("name", sorted(THEATRES))
def test_round_trip_every_theatre(name):
    p = THEATRES[name]
    lon0 = p.central_meridian
    for lat in (-52.0, -10.0, 0.5, 15.2, 36.2, 50.9, 69.0):
        for dlon in (-4.0, -0.3, 0.0, 2.7, 5.0):
            x, z = p.to_dcs(lat, lon0 + dlon)
            la, lo = p.to_latlon(x, z)
            assert la == pytest.approx(lat, abs=1e-8) and lo == pytest.approx(lon0 + dlon, abs=1e-8)


def test_false_origin_is_applied():
    p = for_theatre("MarianasWWII")
    x, z = p.to_dcs(13.48, 144.8)  # Guam lies near the theatre's origin
    assert abs(x) < 20_000 and abs(z) < 20_000


def test_iraq_fitted_to_its_beacons():
    # Al Asad's TACAN as the theatre's beacons.lua gives it both ways.
    lat, lon = for_theatre("Iraq").to_latlon(61461.03125, -164405.296875)
    assert abs(lat - 33.787370) < 1e-6 and abs(lon - 42.443594) < 1e-6


def test_as_dict_names_the_source():
    d = for_theatre("Nevada").as_dict()
    assert d["central_meridian"] == -117 and "pydcs" in d["constants_from"]
    assert math.isclose(d["scale_factor"], 0.9996)


def test_fit_recovers_the_constants():
    true = THEATRES["Syria"]
    pts = []
    for lat in (33.0, 34.1, 35.7):
        for lon in (35.2, 36.5, 38.9, 41.0):
            x, z = true.to_dcs(lat, lon)
            pts.append((lat, lon, round(x, 2), round(z, 2)))  # the hook writes centimetres
    got, err = fit(pts)
    assert got.central_meridian == 39 and err < 0.05
    assert got.false_easting == pytest.approx(true.false_easting, abs=0.05)
    assert got.false_northing == pytest.approx(true.false_northing, abs=0.05)
    with pytest.raises(ValueError):
        fit(pts[:2])
