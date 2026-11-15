---
title: "Paikannimet: towns"
nav_order: 5
lang: "fi"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Paikannimet: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

Tulostaa teatterin paikannimet tiedostosta `map/towns.lua` (luettuna tekstinä, ei koskaan
suoritettuna) JSON-muodossa: jokaisen kaupungin nimen, sen leveys- ja pituusasteen sekä DCS:n
`x`-arvon (pohjoinen) ja `z`-arvon (itä) metreinä teatterin projektion kautta.

1. Selvitä teatterin kansion nimi komennolla [`list`](list.md).
2. Suorita `heat3d-dcs-maps towns <theatre> > towns.json`.
3. Käytä `x`/`z`-arvoja nimeämään kenttä tai tarkistamaan tallenteen sijainteja.

![kaupungit synteettisessä asennuksessa](../assets/img/towns.svg)

| Asetus | Tekee |
|---|---|
| `theatre` | kansion nimi kohdassa `Mods\terrains` |
| `--dcs FOLDER` | DCS World -kansio |

Kentän alueen sisällä olevat kaupungit ovat myös sen `<name>.json`-tiedostossa, kunkin alla olevan
maan korkeuden kanssa ([Kenttätiedostot](output.md)).
