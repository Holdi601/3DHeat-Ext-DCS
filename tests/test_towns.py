from heat3d_ext_dcs.towns import parse

TEXT = r"""local gettext = require("i_18n")
local       _ = gettext.translate

towns = {
["Garapan"] = { latitude = 15.207571, longitude = 145.719597, display_name = _("Garapan")},
["Saint-Lo"] = {longitude = -1.0904, latitude = 49.1157, display_name = _("Saint-Lo (1944)")},
["Nameless"] = { latitude = -51.69, longitude = -57.85 },
["Broken"] = { latitude = 1.0 },
}
"""


def test_parse():
    t = parse(TEXT)
    assert [x.name for x in t] == ["Garapan", "Saint-Lo", "Nameless"]
    assert t[0].lat == 15.207571 and t[0].lon == 145.719597 and t[0].display == "Garapan"
    assert t[1].lat == 49.1157 and t[1].lon == -1.0904  # keys in either order
    assert t[1].display == "Saint-Lo (1944)"
    assert t[2].display == "Nameless" and t[2].lat == -51.69
