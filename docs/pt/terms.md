---
title: Termos e licença
nav_order: 8
lang: pt
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# Termos e licença {#terms-and-licence}

## Os termos da Eagle Dynamics {#eagle-dynamics-terms}

Lidos em 2026-11-07 de `Doc/license_en.txt` da instalação (DCS World
End-User Licence Agreement, The Fighter Collection Ltd). O
"Program" licenciado inclui "THE DATA SUPPLIED WITH IT". Cláusula 3.1:

> Except as expressly set out in this Licence or in clauses 4.1 and 4.2
> below, or as permitted by any local law, you undertake to use the Program
> for your own personal use, and you shall not: [...]
>
> (c) not to disassemble, decompile, reverse engineer or create derivative
> works based on the whole, or any part, of the Program nor attempt to do any
> such things except to the extent that (by virtue of section 296A of the
> Copyright, Designs and Patents Act 1988) such actions cannot be prohibited
> because they are essential for the purpose of achieving inter-operability
> of the Program with another software program, and provided that the
> information obtained by you during such activities: (i) is used only for
> the purpose of achieving inter-operability of the Program with another
> software program; and (ii) is not unnecessarily disclosed or communicated
> to any third party without the TFC's prior written consent; and (iii) is
> not used to create any software which is substantially similar to the
> Program.

A cláusula 3.1 (a) proíbe "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program" sem consentimento, e (e) proíbe "exploit this
Program or any of its parts commercially".

O que este leitor faz: ele lê arquivos de dados na sua própria máquina, depois de você
tê-los instalado, fora do jogo. Não altera nada no jogo, não quebra nenhuma cifra (o único
arquivo cifrado de uma pasta de terreno é deixado em paz) e não fala com servidor algum. Descobrir
o layout de um arquivo de dados é engenharia reversa no sentido de 3.1 (c), e um nível montado
a partir do terreno do jogo é, por assim dizer, uma obra derivada. Usar o leitor é uma decisão sua,
para uso próprio; os níveis que ele grava são seus para ver, não para compartilhar ou
publicar. Por isso ele é um pacote separado.

A alternativa autorizada, que não lê arquivo algum: o próprio script de missões do simulador
pode amostrar o solo (`land.getHeight`, `land.getSurfaceType`) e listar as bases aéreas
(`world.getAirbases`) enquanto uma missão roda. Ela precisa de horas com o DCS aberto por
teatro e dá uma grade mais grosseira; não foi construída, porque os arquivos se mostraram legíveis.

## Licença e fontes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE)). Precisa de numpy (BSD-3-Clause); `fit` em um
`.parquet` precisa de pyarrow (Apache-2.0). Escrito para este projeto. As constantes de
projeção são fatos publicados pelo pydcs
(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`); só os números foram
tirados. A projeção é a série de Krüger, como a dá C. F. F. Karney
("Transverse Mercator with an accuracy of a few nanometers", Journal of
Geodesy 85, 2011). Nenhum código foi tirado de outro projeto.
