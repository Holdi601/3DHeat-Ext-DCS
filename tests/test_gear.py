from heat3d_ext_dcs.gear import PREFIX, TAG, _classify


def test_classes_from_attributes():
    assert _classify(["ground units", "tanks", "modern tanks"], "ground") == ("ground", "mbt")
    assert _classify(["air", "attack helicopters"], "air") == ("air", "heli-attack")
    assert _classify(["air", "multirole fighters"], "air") == ("air", "fighter")
    assert _classify(["ships", "heavy armed ships"], "ground") == ("sea", "warship")
    # an aircraft never becomes a ground class
    assert _classify(["infantry"], "air")[0] == "air"


def test_real_vehicle_name_from_the_display_name():
    assert TAG.sub("", PREFIX.sub("", "MBT T-90M [CH]")).strip() == "T-90M"
    assert PREFIX.sub("", "SAM SA-11 Buk LN 9A310M1") == "SA-11 Buk LN 9A310M1"
