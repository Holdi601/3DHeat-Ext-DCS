---
title: "약관과 라이선스"
nav_order: 8
lang: "ko"
source: terms.md
source_hash: "5b8e45352dae"
nav_exclude: true
search_exclude: true
---
# 약관과 라이선스 {#terms-and-licence}

## 리더가 읽는 것 {#what-the-reader-reads}

리더는 여러분의 컴퓨터에 있는 여러분 자신의 DCS World 설치본의 데이터 파일을 읽습니다([파일을 읽는 방법](reading.md)). 게임의 어떤 것도 바꾸지 않으며 어떤 서버와도 통신하지 않습니다.

게임의 어떤 것도 함께 배포되거나 재배포되지 않습니다. 게임 파일도, 게임 코드도, DLL도 없습니다. 테스트는 읽는 모든 파일을 직접 만듭니다. 이 도구가 쓰는 레벨은 여러분의 컴퓨터에 남습니다.

3DHeat DCS은(는) Eagle Dynamics와(과) 제휴 관계가 없으며 승인을 받지 않았습니다. DCS World 및 관련 이름과 상표는 각 소유자에게 있습니다.

권리자분들께: [github.com/Holdi601/3DHeat-Ext-DCS/issues](https://github.com/Holdi601/3DHeat-Ext-DCS/issues)에서 이슈를 열어 주세요. 빠르게 답하고 요청하시면 무엇이든 삭제합니다.

## 라이선스와 출처 {#licence-and-sources}

MIT 라이선스([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/LICENSE))입니다. numpy(BSD-3-Clause)가 필요하며, `.parquet`에 대한 `fit`은 pyarrow(Apache-2.0)가 필요합니다. 이 프로젝트를 위해 작성되었습니다. 투영 상수는 pydcs(github.com/pydcs/dcs, `dcs/terrain/*/projection.py`)가 공개한 사실이며, 그 숫자만 가져왔습니다. 투영은 C. F. F. Karney가 제시한 Krüger 급수입니다("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011). 다른 프로젝트의 코드는 한 줄도 가져오지 않았습니다.
