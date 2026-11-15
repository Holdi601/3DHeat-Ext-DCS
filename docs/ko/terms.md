---
title: "약관과 라이선스"
nav_order: 8
lang: "ko"
source: terms.md
source_hash: "677b443e2bb8"
nav_exclude: true
search_exclude: true
---
# 약관과 라이선스 {#terms-and-licence}

## Eagle Dynamics의 약관 {#eagle-dynamics-terms}

2026-11-07에 설치본의 `Doc/license_en.txt`에서 읽었습니다(DCS World End-User Licence Agreement, The Fighter Collection Ltd). 라이선스가 허락하는 "Program"에는 "THE DATA SUPPLIED WITH IT"(이것과 함께 제공되는 데이터)이 포함됩니다. 3.1조는 다음과 같습니다:

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

3.1조 (a)는 동의 없이 "sell, trade, rent, lease, sub-license, merge,
adapt, vary, modify the Program"(프로그램을 팔거나, 교환하거나, 임대하거나, 재라이선스하거나, 합병하거나, 개조하거나, 변경하거나, 수정하는 것)을 금지하고, (e)는 "exploit this
Program or any of its parts commercially"(이 프로그램이나 그 일부를 상업적으로 이용하는 것)을 금지합니다.

이 리더가 하는 일: 설치를 마친 뒤, 게임 밖에서, 본인의 컴퓨터에 있는 데이터 파일을 읽습니다. 게임은 전혀 바꾸지 않고, 암호화를 깨지 않으며(지형 폴더의 암호화된 파일 하나는 건드리지 않습니다), 어떤 서버와도 통신하지 않습니다. 데이터 파일의 구조를 알아내는 것은 3.1조 (c)의 의미에서 리버스 엔지니어링이며, 게임 지형으로 만든 레벨은 파생 저작물로 볼 여지가 있습니다. 이 리더를 쓰는 것은 본인의 결정이며, 본인의 사용을 위한 것입니다. 이 리더가 쓰는 레벨은 본인이 보기 위한 것이지, 공유하거나 게시하기 위한 것이 아닙니다. 그래서 이것은 별도의 패키지입니다.

파일을 전혀 읽지 않는 허용된 대안도 있습니다. 시뮬레이터 자체의 미션 스크립팅은, 미션이 도는 동안 지면을 샘플링하고(`land.getHeight`, `land.getSurfaceType`) 비행장 목록을(`world.getAirbases`) 얻을 수 있습니다. 하지만 맵마다 DCS를 몇 시간 돌려야 하고 격자도 더 성깁니다. 파일을 읽을 수 있다는 것이 확인되었으므로 이것은 만들지 않았습니다.

## 라이선스와 출처 {#licence-and-sources}

MIT 라이선스([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE))입니다. numpy(BSD-3-Clause)가 필요하며, `.parquet`에 대한 `fit`은 pyarrow(Apache-2.0)가 필요합니다. 이 프로젝트를 위해 작성되었습니다. 투영 상수는 pydcs(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`)가 공개한 사실이며, 그 숫자만 가져왔습니다. 투영은 C. F. F. Karney가 제시한 Krüger 급수입니다("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). 다른 프로젝트의 코드는 한 줄도 가져오지 않았습니다.
