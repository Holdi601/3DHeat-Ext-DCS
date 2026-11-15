---
title: "Nomes de lugares: towns"
nav_order: 5
lang: pt
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# Nomes de lugares: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <teatro> [--dcs PASTA]
```

Imprime os nomes de lugares do teatro, a partir do seu `map/towns.lua` (lido como texto,
nunca executado), como JSON: o nome de cada cidade, a sua latitude e longitude, e o seu
`x` (norte) e `z` (leste) do DCS em metros, pela projeção do teatro.

1. Encontre o nome da pasta do teatro com [`list`](list.md).
2. Execute `heat3d-dcs-maps towns <teatro> > towns.json`.
3. Use o `x`/`z` para rotular um nível, ou para conferir as posições de uma gravação.

![cidades em uma instalação sintética](../assets/img/towns.svg)

| Opção | Faz |
|---|---|
| `teatro` | o nome da pasta em `Mods\terrains` |
| `--dcs PASTA` | a pasta do DCS World |

As cidades dentro da região de um nível também estão no seu `<nome>.json`, com a
altura do solo sob cada uma ([Os arquivos do nível](output.md)).
