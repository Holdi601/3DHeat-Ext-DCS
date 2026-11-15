---
title: "Hvernig skrárnar eru lesnar"
nav_order: 7
lang: "is"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Hvernig skrárnar eru lesnar {#how-the-files-are-read}

Aðeins `Mods/terrains/<theatre>/surface/*.surface5` (landnetið),
`Scenes/*.scn5` (hvar hlutir standa, og kassi hvers líkans),
`AirfieldsTaxiways/*.rn4` og `map/towns.lua` (staðarnöfn, lesin sem texti,
aldrei keyrð). Ekki dulkóðaða
`terrain.cfg.lua.pak.crypt`, ekki `manifest.bin`, ekkert af forritinu.

Sniðið `.surface5` er óskjalfest; uppbyggingin, eins og hún er lesin úr skránum,
er skráð í [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Í stuttu máli: skrá yfir flísafærslur (umbreyting, mörk, og listar af gerðum
bætastraumum, hver listi fylgdur af shader og efni sem hann er teiknaður
með), síðan hrágögnin. Það er hvorki þjappað né dulkóðað. `Pbase` straumur flísarinnar
geymir hnúta hennar; hópurinn sem er teiknaður sem `Land` geymir
þríhyrningana og `TRITYPE` fyrir hvern þríhyrning, þar sem lægsti bitinn merkir sjó; hinir
hóparnir eru yfirlögin sem gefa flokkana hér að ofan.

## Staðfest {#verified}

- `list` las skrána yfir sérhvert uppsett leiksvæði (milljónir upp í tugi
  milljóna landhnúta hvert), og sérhver sýnatekin flís afkóðaðist í trúverðuga
  metra.
- Á svæðum tveggja leiksvæða lentu bæirnir úr `towns.lua` innan metra
  frá landhnúti, á landi, N af N; hæsta landið passaði við raunverulegan
  tind innan tíu metra; flugvellir, ár, þorp og vegir sáust í
  flokkum sínum. Bæði borðin hlóðust í skoðaranum, með bæjarmerkjum í sömu
  DCS-metrum sitjandi á landinu.
- Á svæði í senu lentu byggingastaðsetningarnar á landi sínu; flugbrautarljós
  röktu flugbraut leiksins, og vagnar og veggjaútlínur röðuðust upp með
  afkóðuðu stefnunni, öll saman.
- `tests/` smíðar `.surface5` skrár með sömu uppbyggingu, svo engin leikjagögn
  eru geymd hér; `tests/test_real_install.py` keyrir á uppsetningu vélarinnar
  sem keyrir prófanirnar og er sleppt án hennar.

**Ekki athugað:** allt stórt leiksvæði í einu borði (stærðarvörnin hér
að ofan er ekki að ástæðulausu), og aðrar útgáfur DCS en sú sem var prófuð.

## Ekki lesið {#not-read}

- **Byggingar sem form** (líkönin eru `.edm` í `Models/`): aðeins kassar,
  viljandi. Uppbygging þeirra, og senunnar, er skráð í
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); sérhvert uppsett
  leiksvæði les (tvö eldri leiksvæði í afbrigði af uppbyggingu sem lesarinn þekkir
  líka).
- Tré, ljós og aðrir hlutir senunnar: lesið, ekki teiknað.
- **Vegakerfið sem graf** (`roads/*.rn4`): ekki afkóðað.
- Áferðir, tré, öldur sjávar, eigin lægri smáatriðastig landsins.
