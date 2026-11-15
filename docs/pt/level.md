---
title: "Montar um nível: level"
nav_order: 3
lang: "pt"
source: level.md
source_hash: "994b156c7213"
nav_exclude: true
search_exclude: true
---
# Montar um nível: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <teatro> -o <pasta> [--dcs PASTA] [--name NOME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## Passo a passo {#step-by-step}

Nunca usou a linha de comando? Leia primeiro [Antes de começar](before-you-start.md).

1. Encontre o nome da pasta do teatro com [`list`](list.md).
2. Para um teatro pequeno, monte-o inteiro: `heat3d-dcs-maps level <teatro> -o levels`.
3. Para um grande, escolha uma região: `--around <lat> <lon> <km>` (um quadrado com
   tantos km para cada lado de um ponto) ou `--bounds X0 Z0 X1 Z1` em metros do DCS.
   Dê um nome com `--name`.
4. O comando imprime os blocos à medida que os lê, a contagem de triângulos, o arquivo
   gravado, e quantas cidades do teatro caem no solo - uma verificação da projeção que deve
   mostrar "N de N".
5. Carregue `<pasta>/<nome>.glb` no painel Fundo / nível do visualizador e ligue
   **Cor capturada** para ver as classes do solo.

![level em uma instalação sintética](../assets/img/level.svg)

Uma região do mesmo teatro sintético, em metros do DCS:

![level com --bounds e --name](../assets/img/level-bounds.svg)

## Opções {#options}

| Opção | Padrão | Faz |
|---|---|---|
| `teatro` | - | o nome da pasta em `Mods\terrains`, como `list` o mostra (qualquer capitalização) |
| `-o`, `--out` | obrigatória | a pasta onde gravar `<nome>.glb` e `<nome>.json` |
| `--dcs PASTA` | encontrada | a pasta do DCS World ([onde é encontrada](list.md#onde-a-instalação-é-encontrada)) |
| `--name NOME` | o do teatro | o nome do nível, e o dos seus arquivos |
| `--around LAT LON KM` | - | só um quadrado com tantos km para cada lado de um ponto |
| `--bounds X0 Z0 X1 Z1` | - | só esta caixa, em metros do DCS (x norte, z leste) |
| `--cell M` | `0` | afina a malha: cada vértice a até *M* metros vira um só (0: os triângulos do próprio jogo) |
| `--seabed` | desligada | mantém o fundo do mar como solo (por padrão ele fica de fora) |
| `--no-water` | desligada | deixa de fora o mar plano |
| `--no-buildings` | desligada | deixa de fora os edifícios da cena do teatro |
| `--force` | desligada | exporta um mapa muito grande inteiro, em detalhe total |
| `--projection LON0 FE FN` | a do teatro | constantes da projeção Transversa de Mercator para um teatro que esta ferramenta não conhece ([fit](fit.md)) |

Todas as opções, como o programa as mostra: [Referência de comandos](../cli-reference.md).

## Tamanho {#size}

A malha do jogo é adaptativa - mar aberto em triângulos de quilômetros, costas
e estradas em alguns metros. Um teatro pequeno tem alguns milhões de triângulos; os
grandes têm dezenas de milhões de vértices. Acima de 30 milhões de vértices a ler, `level`
para (código de saída 1) e pede uma região, uma malha mais fina (`--cell 50`) ou
`--force`.

Código de saída: 0 pronto; 1 falhou ou grande demais; 2 a instalação ou o teatro não foi
encontrado (os teatros encontrados são listados).

## Exemplos {#examples}

```bash
heat3d-dcs-maps level <teatro> -o levels                                       # inteiro, em detalhe total
heat3d-dcs-maps level <teatro> --around <lat> <lon> 12 -o levels --name Parte  # um quadrado de 24 km
heat3d-dcs-maps level <teatro> --bounds 1000 2000 1390 2390 -o levels          # uma caixa em metros do DCS
heat3d-dcs-maps level <teatro> --cell 50 -o levels                             # inteiro, afinado para 50 m
heat3d-dcs-maps level <teatro> --no-buildings --no-water -o levels             # só o solo
```

O que há nos arquivos: [Os arquivos do nível](output.md).
