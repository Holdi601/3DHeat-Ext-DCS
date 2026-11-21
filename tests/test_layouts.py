"""Airbases, runways and stands (layouts.py) from hand-made terrain and mission text."""

from heat3d_ext_dcs import layouts as L

MISSION = '''
mission = {
    ["theatre"] = "Testland",
    ["coalition"] = { ["blue"] = { ["country"] = { [1] = { ["plane"] = { ["group"] = {
        [1] = {
            ["route"] = { ["points"] = { [1] = { ["type"] = "TakeOffParking", ["airdromeId"] = 22, ["x"] = 1, ["y"] = 2 } } },
            ["units"] = {
                [1] = { ["alt"] = 10, ["type"] = "F-16C_50", ["payload"] = { ["x"] = 999 }, ["parking_id"] = "D12",
                        ["parking"] = "21", ["x"] = -356000.5, ["y"] = 617800.25 },
                [2] = { ["type"] = "F-16C_50", ["x"] = -356010, ["y"] = 617810 },
            },
        },
    } } } } } },
}
'''

BEACONS = """
beacons = {
\t{
\t\tdisplay_name = _('Testfield');
\t\tbeaconId = 'airfield22_0';
\t\ttype = BEACON_TYPE_ILS_LOCALIZER;
\t\tposition = { 0.0, 10.0, -1300.0 };
\t\tdirection = 90.0;
\t};
\t{
\t\tdisplay_name = _('Testfield');
\t\tbeaconId = 'airfield22_1';
\t\ttype = BEACON_TYPE_ILS_LOCALIZER;
\t\tposition = { 0.0, 10.0, 1300.0 };
\t\tdirection = -90.0;
\t};
}
"""


def test_stands_from_a_mission():
    theatre, found = L.mission_stands(MISSION)
    assert theatre == "Testland"
    assert found == [{"airdrome": 22, "stand": "D12", "x": -356000.5, "z": 617800.25, "y": 10.0, "type": "F-16C_50"}]


def test_names_and_runways_from_beacons():
    bs = L.beacons(BEACONS)
    assert [(b["name"], b["id"], b["type"]) for b in bs] == [("Testfield", 22, "BEACON_TYPE_ILS_LOCALIZER")] * 2
    (rw,) = L.runways(bs)
    assert round(rw["length"]) == 2000 and round(rw["heading"]) == 90
    assert L.radio_names("\t\t-- Testfield\n\t\tradioId = 'airfield22_0';") == {22: "Testfield"}
