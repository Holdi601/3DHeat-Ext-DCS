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


def test_static_objects():
    from heat3d_ext_dcs.gear import is_static
    from heat3d_ext_dcs.lua import LuaTable, Ref

    def table(category=None, attribute=()):
        t = LuaTable()
        if category:
            t.set("category", category)
        att = LuaTable()
        for i, a in enumerate(attribute, 1):
            att.set(i, a)
        t.set("attribute", att)
        return t

    assert is_static(table("Fortification", [5, 9]), [])
    assert is_static(table("Warehouses"), [])
    assert is_static(table(None, [Ref("wsType_Static"), Ref("wsType_Standing")]), [])
    assert is_static(table("Cargo", ["Cargos"]), ["cargos"])
    assert is_static(table("Personnel", [5, 9]), [])  # deck crew placed as statics
    assert not is_static(table("Carriage", [2, 17, 27]), [])  # a railway car is a unit
    assert not is_static(table("Air Defence", [2, 16, 26, "AA_flak"]), ["aa_flak"])
    assert not is_static(table("Unarmed", [2, 17, 25, "Trucks"]), ["trucks"])
