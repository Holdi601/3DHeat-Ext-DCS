---
title: "Cum se citesc fișierele"
nav_order: 7
lang: ro
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Cum se citesc fișierele {#how-the-files-are-read}

Doar `Mods/terrains/<theatre>/surface/*.surface5` (plasa solului),
`Scenes/*.scn5` (unde stau obiectele și caseta fiecărui model),
`AirfieldsTaxiways/*.rn4` și `map/towns.lua` (nume de locuri, citite ca text,
niciodată rulate) sunt citite. Nu fișierul criptat
`terrain.cfg.lua.pak.crypt`, nu `manifest.bin`, nimic din program.

Formatul `.surface5` nu este documentat; aspectul său, așa cum se citește din fișiere, este descris în
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Pe scurt: un index de înregistrări de plăci (o transformare, limite și liste de fluxuri de octeți tipizate,
fiecare listă urmată de shader-ul și materialul cu care este desenată), apoi datele brute. Nu este nici
comprimat, nici criptat. Fluxul `Pbase` al plăcii conține vârfurile sale; grupul desenat ca `Land`
conține triunghiurile și un `TRITYPE` pentru fiecare triunghi, al cărui bit cel mai puțin semnificativ
marchează marea; celelalte grupuri sunt straturile suprapuse care dau clasele de mai sus.

## Verificat {#verified}

- `list` a citit indexul fiecărui teatru instalat (de la milioane până la zeci de milioane de vârfuri de sol
  fiecare), fiecare placă eșantionată decodându-se în metri plauzibili.
- Pe regiuni din două teatre, orașele din `towns.lua` au nimerit la metri de un vârf al solului, pe uscat,
  N din N; cel mai înalt sol a corespuns vârfului real la zece metri; aerodromurile, râurile, satele și
  drumurile au apărut în clasele lor. Ambele niveluri s-au încărcat în vizualizator, cu marcajele orașelor în
  aceiași metri DCS, așezate pe sol.
- Pe o regiune de scenă, plasările clădirilor au nimerit pe solul lor; luminile pistei urmăresc pista jocului,
  iar vagoanele și segmentele de zid s-au aliniat cu direcția decodată, toate.
- `tests/` construiește fișiere `.surface5` în același aspect, deci nu se păstrează aici date de joc;
  `tests/test_real_install.py` rulează pe instalarea mașinii care rulează testele și este sărit fără una.

**Nu s-a verificat:** întregul unui teatru mare într-un singur nivel (limita de dimensiune de mai sus
există dintr-un motiv), și versiuni ale DCS altele decât cea încercată.

## Nu se citește {#not-read}

- **Clădirile ca forme** (modelele sunt `.edm` în `Models/`): doar cutii, intenționat. Aspectul lor și al
  scenei este descris în [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  fiecare teatru instalat se citește (și două teatre mai vechi, într-un aspect variant pe care cititorul îl cunoaște).
- Copacii, luminile și celelalte obiecte ale scenei: citite, nedesenate.
- **Rețeaua de drumuri ca graf** (`roads/*.rn4`): nedecodată.
- Texturi, copaci, valurile mării, nivelurile inferioare de detaliu ale terenului.
