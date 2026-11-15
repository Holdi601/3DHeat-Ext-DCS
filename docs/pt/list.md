---
title: "Encontrar teatros: list"
nav_order: 2
lang: "pt"
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# Encontrar teatros: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs PASTA]
```

Nunca usou a linha de comando? Leia primeiro [Antes de começar](before-you-start.md).

1. Instale uma vez: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, abra
   um terminal nessa pasta e execute `python -m pip install -e .` (Python 3.10
   ou mais recente; ele traz numpy, e pyarrow para `fit` em um `.parquet`).
2. Execute `heat3d-dcs-maps list`.
3. Cada teatro instalado imprime uma linha: o nome da pasta (o nome que os outros
   comandos aceitam), o tamanho do seu arquivo de solo, os seus blocos e vértices,
   se a sua projeção de latitude/longitude é conhecida, e se ele pode ser lido.
   Você deve ver `readable` no fim de cada linha.

![list em uma instalação sintética](../assets/img/list.svg)

A imagem é uma execução em uma instalação que os testes montam (`tests/synth.py`), não no
jogo.

## Onde a instalação é encontrada {#where-the-install-is-found}

`--dcs <pasta>` (a pasta que contém `Mods\terrains`) ou a variável de ambiente `DCS_PATH`;
caso contrário, são pesquisados o registro, as bibliotecas do Steam e as pastas
habituais.

| Opção | Faz |
|---|---|
| `--dcs PASTA` | a pasta do DCS World, a que contém `Mods\terrains` |

Código de saída: 0 pronto, 2 nenhuma instalação ou nenhum teatro encontrado.
