"""
DCS world metres <-> WGS84 latitude and longitude.

Each theatre is a Transverse Mercator projection (WGS84 ellipsoid, latitude of
origin 0, scale 0.9996) with its own central meridian and false origin; DCS's
x is the northing and z the easting:

    x = northing + false_northing        z = easting + false_easting

The constants are facts published by the pydcs project
(https://github.com/pydcs/dcs, `dcs/terrain/<name>/projection.py`, generated
there from the sim itself); only the numbers are taken. The projection is
Krueger's series to sixth order as C. F. F. Karney gives it ("Transverse
Mercator with an accuracy of a few nanometers", J. Geodesy 85, 2011), written
here: accurate to well under a millimetre far further from the central
meridian than any theatre reaches - the same answer PROJ's `tmerc` gives,
which is what pydcs uses.

Iraq is not in pydcs: its levels come out in DCS metres without latitude and
longitude, until `fit` has found its constants from a flight that recorded
both (the 3DHeat Watcher's DCS hook writes x, z, lat and lon for every fix).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

_A = 6378137.0
_F = 1 / 298.257223563
_E2 = _F * (2 - _F)


@dataclass(frozen=True)
class Projection:
    central_meridian: float
    false_easting: float
    false_northing: float
    scale: float = 0.9996
    source: str = "pydcs (github.com/pydcs/dcs), dcs/terrain/*/projection.py"

    def to_dcs(self, lat: float, lon: float) -> tuple[float, float]:
        """Latitude, longitude (degrees) -> DCS x (north), z (east), metres."""
        e, n = _forward(lat, lon - self.central_meridian, self.scale)
        return n + self.false_northing, e + self.false_easting

    def to_latlon(self, x: float, z: float) -> tuple[float, float]:
        """DCS x (north), z (east), metres -> latitude, longitude (degrees)."""
        lat, dlon = _inverse(z - self.false_easting, x - self.false_northing, self.scale)
        return lat, dlon + self.central_meridian

    def as_dict(self) -> dict:
        return {
            "type": "transverse_mercator",
            "ellipsoid": "WGS84",
            "latitude_of_origin": 0,
            "central_meridian": self.central_meridian,
            "scale_factor": self.scale,
            "false_easting": self.false_easting,
            "false_northing": self.false_northing,
            "axes": "DCS x = northing + false_northing, z = easting + false_easting",
            "constants_from": self.source,
        }


#: Theatre folder name (Mods/terrains/<folder>) -> projection.
THEATRES: dict[str, Projection] = {
    "Afghanistan": Projection(63, -300150.0, -3759657.0),
    "Caucasus": Projection(33, -99516.9999999732, -4998114.999999984),
    "Falklands": Projection(-57, 147639.99999997593, 5815417.000000032),
    "GermanyColdWar": Projection(21, 35427.619999985734, -6061633.128000011),
    "Kola": Projection(21, -62702.00000000087, -7543624.999999979),
    "MarianaIslands": Projection(147, 238417.99999989968, -1491840.000000048),
    # The 1944 Marianas share the modern map's ground and origin (checked: the
    # 1944 towns land on the coast of the same islands).
    "MarianasWWII": Projection(147, 238417.99999989968, -1491840.000000048),
    "Nevada": Projection(-117, -193996.80999964548, -4410028.063999966),
    "Normandy": Projection(-3, -195526.00000000204, -5484812.999999951),
    "PersianGulf": Projection(57, 75755.99999999645, -2894933.0000000377),
    "Sinai": Projection(33, 169221.9999999585, -3325312.9999999693),
    "Syria": Projection(39, 282801.00000003993, -3879865.9999999935),
    "TheChannel": Projection(3, 99376.00000000288, -5636889.00000001),
}


def for_theatre(name: str) -> Projection | None:
    return THEATRES.get(name)


def fit(samples: list[tuple[float, float, float, float]], scale: float = 0.9996) -> tuple[Projection, float]:
    """
    A theatre's constants from points the sim gave both ways: (lat, lon, x, z).

    The central meridian is a whole degree in every theatre known; each one
    within 8 degrees of the points is tried, the false origin is the mean
    offset, and the meridian that leaves the smallest error wins. Returns the
    projection and that error (root mean square, metres).
    """
    if len(samples) < 3:
        raise ValueError("at least three points are needed")
    lons = sorted(s[1] for s in samples)
    mid = round(lons[len(lons) // 2])
    best: tuple[Projection, float] | None = None
    for lon0 in range(mid - 8, mid + 9):
        en = [_forward(lat, lon - lon0, scale) for lat, lon, _x, _z in samples]
        fe = sum(z - e for (e, _n), (_la, _lo, _x, z) in zip(en, samples)) / len(samples)
        fn = sum(x - n for (_e, n), (_la, _lo, x, _z) in zip(en, samples)) / len(samples)
        err = math.sqrt(sum((z - e - fe) ** 2 + (x - n - fn) ** 2 for (e, n), (_la, _lo, x, z) in zip(en, samples))
                        / len(samples))
        if best is None or err < best[1]:
            best = (Projection(lon0, fe, fn, scale, source="fitted to a recording that held both"), err)
    assert best is not None
    return best


_N = _F / (2 - _F)
_E = math.sqrt(_E2)
#: The rectifying radius and Krueger's series to sixth order in n (Karney 2011, eqs. 14, 35, 36).
_RA = _A / (1 + _N) * (1 + _N**2 / 4 + _N**4 / 64 + _N**6 / 256)
_ALPHA = (
    _N / 2 - 2 * _N**2 / 3 + 5 * _N**3 / 16 + 41 * _N**4 / 180 - 127 * _N**5 / 288 + 7891 * _N**6 / 37800,
    13 * _N**2 / 48 - 3 * _N**3 / 5 + 557 * _N**4 / 1440 + 281 * _N**5 / 630 - 1983433 * _N**6 / 1935360,
    61 * _N**3 / 240 - 103 * _N**4 / 140 + 15061 * _N**5 / 26880 + 167603 * _N**6 / 181440,
    49561 * _N**4 / 161280 - 179 * _N**5 / 168 + 6601661 * _N**6 / 7257600,
    34729 * _N**5 / 80640 - 3418889 * _N**6 / 1995840,
    212378941 * _N**6 / 319334400,
)
_BETA = (
    _N / 2 - 2 * _N**2 / 3 + 37 * _N**3 / 96 - _N**4 / 360 - 81 * _N**5 / 512 + 96199 * _N**6 / 604800,
    _N**2 / 48 + _N**3 / 15 - 437 * _N**4 / 1440 + 46 * _N**5 / 105 - 1118711 * _N**6 / 3870720,
    17 * _N**3 / 480 - 37 * _N**4 / 840 - 209 * _N**5 / 4480 + 5569 * _N**6 / 90720,
    4397 * _N**4 / 161280 - 11 * _N**5 / 504 - 830251 * _N**6 / 7257600,
    4583 * _N**5 / 161280 - 108847 * _N**6 / 3991680,
    20648693 * _N**6 / 638668800,
)


def _conformal(tau: float) -> float:
    """tan of the conformal latitude from tan of the latitude (Karney eq. 7)."""
    sigma = math.sinh(_E * math.atanh(_E * tau / math.hypot(1.0, tau)))
    return tau * math.hypot(1.0, sigma) - sigma * math.hypot(1.0, tau)


def _forward(lat: float, dlon: float, k0: float) -> tuple[float, float]:
    """Easting and northing (metres, no false origin): Krueger's series, Karney eqs. 7-11."""
    lam = math.radians(dlon)
    tp = _conformal(math.tan(math.radians(lat)))
    xi = math.atan2(tp, math.cos(lam))
    eta = math.asinh(math.sin(lam) / math.hypot(tp, math.cos(lam)))
    x, y = eta, xi
    for j, a in enumerate(_ALPHA, 1):
        x += a * math.cos(2 * j * xi) * math.sinh(2 * j * eta)
        y += a * math.sin(2 * j * xi) * math.cosh(2 * j * eta)
    return k0 * _RA * x, k0 * _RA * y


def _inverse(x: float, y: float, k0: float) -> tuple[float, float]:
    """Latitude and longitude offset (degrees) from easting, northing: Karney eqs. 11, 15-21."""
    xi, eta = y / (k0 * _RA), x / (k0 * _RA)
    xp, ep = xi, eta
    for j, b in enumerate(_BETA, 1):
        xp -= b * math.sin(2 * j * xi) * math.cosh(2 * j * eta)
        ep -= b * math.cos(2 * j * xi) * math.sinh(2 * j * eta)
    tp = math.sin(xp) / math.hypot(math.sinh(ep), math.cos(xp))
    lam = math.atan2(math.sinh(ep), math.cos(xp))
    tau = tp / (1 - _E2)
    for _ in range(8):  # Newton on eq. 7; converges in two or three steps
        d = (tp - _conformal(tau)) * (1 + (1 - _E2) * tau * tau) / (
            (1 - _E2) * math.hypot(1.0, _conformal(tau)) * math.hypot(1.0, tau)
        )
        tau += d
        if abs(d) < 1e-14 * max(1.0, abs(tau)):
            break
    return math.degrees(math.atan(tau)), math.degrees(lam)
