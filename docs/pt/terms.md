---
title: Termos e licença
nav_order: 8
lang: "pt"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# Termos e licença {#terms-and-licence}

## O que o leitor lê {#what-the-reader-reads}

O leitor lê arquivos de dados da sua própria instalação do DCS World no seu computador ([Como os arquivos são lidos](reading.md)). Ele não altera nada no jogo e não se comunica com nenhum servidor.

Nada do jogo é incluído nem redistribuído: nenhum arquivo do jogo, nenhum código do jogo, nenhuma DLL; os testes geram cada arquivo que leem. Os níveis que ele escreve ficam na sua máquina.

3DHeat DCS não é afiliado a Eagle Dynamics nem endossado por ela. DCS World e os nomes e marcas relacionados pertencem aos seus donos.

Titulares de direitos: abram uma issue em [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues) - respondemos rápido e removemos qualquer coisa a pedido.

## Licença e fontes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Precisa de numpy (BSD-3-Clause); `fit` em um
`.parquet` precisa de pyarrow (Apache-2.0). Escrito para este projeto. As constantes de
projeção são fatos publicados pelo pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); só os números foram
tirados. A projeção é a série de Krüger, como a dá C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nenhum código foi tirado de outro projeto.
