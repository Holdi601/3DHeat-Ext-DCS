---
title: "Projeções: fit"
nav_order: 6
lang: pt
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# Projeções: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <gravação>
```

Cada teatro é uma projeção Transversa de Mercator com as suas próprias constantes. A
ferramenta conhece as dos teatros em que foi verificada; para um que ela não conhece,
`fit` as encontra a partir de qualquer gravação que tenha latitude/longitude e
metros do DCS, como uma sessão do 3DHeat Watcher de um voo.

1. Grave um voo no teatro com o 3DHeat Watcher (ou faça qualquer gravação com as colunas
   `lat`, `lon`, `x`, `z` em metros do DCS: x são metros para o norte, z metros para o leste,
   como em todo o DCS).
2. Execute `heat3d-dcs-maps fit "<sessão>/heat.parquet"` (ou um `.jsonl` ou `.csv`).
3. Ele imprime a projeção ajustada em JSON, o erro quadrático médio da raiz sobre
   os pontos, e os argumentos `--projection` a usar.
4. Monte o nível com eles:
   `heat3d-dcs-maps level <teatro> --projection <LON0> <FE> <FN> -o levels`.

![fit em uma gravação sintética](../assets/img/fit.svg)

A gravação da imagem tem nove pontos feitos a partir de uma projeção conhecida,
que `fit` recupera até o milímetro.

| Argumento | Faz |
|---|---|
| `gravação` | `.parquet`, `.jsonl` ou `.csv` com as colunas `lat`, `lon`, `x`, `z` (metros do DCS); linhas que não podem ser lidas são ignoradas |

A projeção é a série de Krüger, como a dá C. F. F. Karney ("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

Código de saída: 0 um bom ajuste (abaixo de 5 m de erro quadrático médio da raiz); 1 um ajuste ruim, ou
menos de três linhas utilizáveis; 2 o arquivo não foi encontrado.
