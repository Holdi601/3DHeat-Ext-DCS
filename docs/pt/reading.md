---
title: Como os arquivos são lidos
nav_order: 7
lang: "pt"
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# Como os arquivos são lidos {#how-the-files-are-read}

Só `Mods/terrains/<teatro>/surface/*.surface5` (a malha do solo),
`Scenes/*.scn5` (onde os objetos ficam, e a caixa de cada modelo),
`AirfieldsTaxiways/*.rn4` e `map/towns.lua` (nomes de lugares, lidos como texto,
nunca executados). Não o `terrain.cfg.lua.pak.crypt` cifrado, não o
`manifest.bin`, nada do programa.

O formato `.surface5` não é documentado; o layout, como lido dos arquivos,
está descrito em [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py).
Em resumo: um índice de registros de blocos (uma transformação, limites, e listas de
fluxos de bytes tipados, cada lista seguida do sombreador e do material com que é desenhada),
depois os dados brutos. Não é comprimido nem cifrado. O fluxo `Pbase` do bloco
guarda os seus vértices; o grupo desenhado como `Land` guarda os triângulos e um `TRITYPE` por triângulo, cujo bit
mais baixo marca o mar; os outros grupos são as sobreposições que dão as classes acima.

## Verificado {#verified}

- `list` leu o índice de todos os teatros instalados (de milhões a dezenas de milhões de
  vértices de solo cada), cada bloco amostrado decodificando para metros plausíveis.
- Em regiões de dois teatros, as cidades de `towns.lua` caíram a poucos metros de um
  vértice do solo, em terra, N de N; o ponto mais alto do solo casou com o cume real
  a dez metros; aeródromos, rios, vilarejos e estradas apareceram nas suas classes. Os dois níveis
  carregaram no visualizador, com marcadores de cidade nos mesmos metros do DCS
  assentados no solo.
- Em uma região de cena, os posicionamentos de edifícios caíram sobre o seu solo; as luzes de pista
  seguiram a pista do jogo, e os vagões e segmentos de muro alinharam-se com o rumo
  decodificado, todos eles.
- `tests/` monta arquivos `.surface5` no mesmo layout, então nenhum dado do jogo é
  guardado aqui; `tests/test_real_install.py` roda na instalação da máquina
  que executa os testes, e é pulado sem uma.

**Não verificado:** o teatro grande inteiro em um só nível (a proteção de tamanho
acima existe por um motivo), e versões do DCS diferentes da testada.

## Não lido {#not-read}

- **Edifícios como formas** (os modelos são `.edm` em `Models/`): só caixas, de propósito.
  O seu layout, e o da cena, estão descritos em
  [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py); todo teatro
  instalado é lido (dois teatros mais antigos em um layout variante que o leitor conhece
  também).
- Árvores, luzes e os outros objetos da cena: lidos, não desenhados.
- **A rede de estradas como grafo** (`roads/*.rn4`): não decodificada.
- Texturas, árvores, as ondas do mar, os níveis de detalhe inferiores do terreno.
