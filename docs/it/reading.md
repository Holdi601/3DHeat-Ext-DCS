---
title: Come vengono letti i file
nav_order: 7
lang: it
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Come vengono letti i file {#how-the-files-are-read}

Vengono letti solo `Mods/terrains/<teatro>/surface/*.surface5` (la maglia del terreno),
`Scenes/*.scn5` (dove stanno gli oggetti, e il riquadro di ogni modello),
`AirfieldsTaxiways/*.rn4` e `map/towns.lua` (i nomi dei luoghi, letti come testo, mai eseguiti). Non
il file cifrato `terrain.cfg.lua.pak.crypt`, non `manifest.bin`, nulla del programma.

Il formato `.surface5` non è documentato; il layout, come si legge dai file, è scritto in
[`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
In breve: un indice di record di tessere (una trasformazione, i limiti, e liste di flussi di byte
tipizzati, ognuna seguita dallo shader e dal materiale con cui viene disegnata), poi i dati grezzi.
Non è compresso né cifrato. Il flusso `Pbase` della tessera contiene i suoi vertici; il gruppo
disegnato come `Land` contiene i triangoli e un `TRITYPE` per triangolo, il cui bit più basso segna
il mare; gli altri gruppi sono le sovrapposizioni che danno le classi qui sopra.

## Verificato {#verified}

- `list` ha letto l'indice di ogni teatro installato (da milioni a decine di milioni di vertici del
  terreno ciascuno), ogni tessera campionata decodificata in metri plausibili.
- Su regioni di due teatri, le città di `towns.lua` sono cadute entro metri da un vertice del
  terreno, su terra, N di N; il terreno più alto corrispondeva alla vetta reale entro dieci metri;
  aeroporti, fiumi, villaggi e strade si vedevano nelle loro classi. Entrambi i livelli si sono
  caricati nel visualizzatore, con i segnalini delle città nelle stesse metri DCS posati sul terreno.
- Su una regione di scena, le collocazioni degli edifici sono cadute sul loro terreno; le luci della
  pista hanno tracciato la pista del gioco, e vagoni e tratti di muro si sono allineati con
  l'orientamento decodificato, tutti.
- `tests/` costruisce file `.surface5` con lo stesso layout, quindi non viene conservato alcun dato
  del gioco qui; `tests/test_real_install.py` gira sull'installazione della macchina che esegue i
  test, e viene saltato senza di essa.

**Non verificato:** un intero grande teatro in un solo livello (la protezione sulla dimensione sopra
esiste per una ragione), e versioni di DCS diverse da quella provata.

## Non letto {#not-read}

- **Gli edifici come forme** (i modelli sono `.edm` in `Models/`): solo scatole, di proposito. Il
  loro layout, e quello della scena, sono scritti in
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py);
  ogni teatro installato si legge (due teatri più vecchi in un layout variante che il lettore conosce).
- Alberi, luci e gli altri oggetti della scena: letti, non disegnati.
- **La rete stradale come grafo** (`roads/*.rn4`): non decodificata.
- Trame, alberi, le onde del mare, i livelli di dettaglio inferiori del terreno.
