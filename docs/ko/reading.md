---
title: "파일을 읽는 방법"
nav_order: 7
lang: ko
source: reading.md
source_hash: "51a7963aff87"
nav_exclude: true
search_exclude: true
---
# 파일을 읽는 방법 {#how-the-files-are-read}

읽는 것은 `Mods/terrains/<theatre>/surface/*.surface5`(지면 메시), `Scenes/*.scn5`(물체가 서 있는 곳과 각 모델의 상자), `AirfieldsTaxiways/*.rn4`, 그리고 `map/towns.lua`(지명, 텍스트로만 읽으며 실행하지 않음)뿐입니다. 암호화된 `terrain.cfg.lua.pak.crypt`, `manifest.bin`, 그리고 프로그램의 어떤 것도 읽지 않습니다.

`.surface5` 형식은 문서화되어 있지 않습니다. 파일에서 읽어 낸 구조는 [`heat3d_ext_dcs/surface5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/surface5.py)에 적혀 있습니다.
요약하면: 타일 기록들의 색인(변환, 경계, 형식이 있는 바이트 스트림 목록. 각 목록 뒤에는 그것을 그릴 셰이더와 재질이 옵니다), 그다음 원본 데이터입니다. 압축도, 암호화도 되어 있지 않습니다. 타일의 `Pbase` 스트림에 꼭짓점이 들어 있습니다. `Land`로 그려지는 그룹에는 삼각형과 삼각형마다의 `TRITYPE`이 있으며, 그 최하위 비트가 바다를 표시합니다. 다른 그룹들은 위에서 본 종류들을 주는 덧칠입니다.

## 검증한 내용 {#verified}

- `list`는 설치된 모든 지도의 색인을 읽었습니다(지도마다 지면 꼭짓점이 수백만에서 수천만 개). 샘플링한 모든 타일이 그럴듯한 미터 값으로 해석되었습니다.
- 두 지도의 영역에서, `towns.lua`의 마을들은 지면 꼭짓점에서 몇 미터 안에 떨어졌고, 모두 육지 위에 있었으며(N of N), 가장 높은 지면은 실제 정상과 10m 이내로 일치했습니다. 비행장, 강, 마을, 도로가 각자의 종류로 나타났습니다. 두 레벨 모두 뷰어에서 불러와졌고, 같은 DCS 미터의 마을 표시가 지면 위에 놓였습니다.
- 한 장면 영역에서, 건물 배치는 자기 지면 위에 놓였습니다. 활주로 조명은 게임의 활주로를 따라갔고, 객차와 벽 조각은 해석한 방향에 맞게 늘어섰습니다. 전부 그랬습니다.
- `tests/`는 같은 구조의 `.surface5` 파일을 만들므로 여기에는 게임 데이터가 들어 있지 않습니다. `tests/test_real_install.py`는 테스트를 실행하는 컴퓨터에 있는 설치본에서 돌며, 설치본이 없으면 건너뜁니다.

**확인하지 않은 것:** 큰 지도 전체를 레벨 하나로 만드는 것(위의 크기 제한이 이유가 있어서 있습니다), 그리고 시도한 것 말고 다른 버전의 DCS.

## 읽지 않는 것 {#not-read}

- **모양으로서의 건물** (모델은 `Models/` 안의 `.edm`입니다): 의도적으로 상자만 씁니다. 그 구조와 장면의 구조는 [`heat3d_ext_dcs/scene5.py`](https://github.com/Holdi601/3DHeat-Ext-DCS/blob/main/heat3d_ext_dcs/scene5.py)에 적혀 있으며, 설치된 모든 지도가 읽힙니다(구버전 두 지도는 이 리더가 아는 변형 구조로 읽힙니다).
- 나무, 조명 등 장면의 다른 물체: 읽지만 그리지는 않습니다.
- **도로망을 그래프로** (`roads/*.rn4`): 해석하지 않습니다.
- 텍스처, 나무, 바다의 파도, 지형의 더 낮은 상세 단계.
