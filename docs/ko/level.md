---
title: "레벨 만들기: level"
nav_order: 3
lang: ko
source: level.md
source_hash: "4035671e5fed"
nav_exclude: true
search_exclude: true
---
# 레벨 만들기: `level` {#building-a-level-level}

```text
heat3d-dcs-maps level <theatre> -o <folder> [--dcs FOLDER] [--name NAME]
                      [--around LAT LON KM | --bounds X0 Z0 X1 Z1] [--cell M]
                      [--seabed] [--no-water] [--no-buildings] [--force]
                      [--projection LON0 FE FN]
```

## 단계별 안내 {#step-by-step}

명령줄이 처음이신가요? 먼저 [시작하기 전에](before-you-start.md)를 읽으세요.

1. [`list`](list.md)로 지도의 폴더 이름을 찾으세요.
2. 작은 지도라면 전체를 만드세요: `heat3d-dcs-maps level <theatre> -o levels`.
3. 큰 지도라면 영역을 고르세요: `--around <lat> <lon> <km>`(한 점의 양옆 그 km만큼의 정사각형), 또는 DCS 미터 단위의 `--bounds X0 Z0 X1 Z1`. `--name`으로 이름을 붙이세요.
4. 명령은 타일을 읽는 대로 출력하고, 삼각형 수, 쓴 파일, 그리고 지도의 마을 중 몇 개가 지면 위에 놓이는지를 보여 줍니다. 이 값은 투영이 맞는지 보는 검사이며, "N of N"(N개 중 N개)이어야 합니다.
5. 뷰어의 배경 / 레벨 패널에서 `<folder>/<name>.glb`를 불러오고, **캡처한 색**을 켜서 지면 종류를 보세요.

![가상 설치본의 레벨](../assets/img/level.svg)

같은 가상 지도의 한 영역을 DCS 미터 단위로 잡은 그림:

![--bounds와 --name을 쓴 레벨](../assets/img/level-bounds.svg)

## 옵션 {#options}

| 옵션 | 기본값 | 하는 일 |
|---|---|---|
| `theatre` | - | `Mods\terrains` 아래의 폴더 이름. `list`가 출력하는 그대로 (대소문자 무관) |
| `-o`, `--out` | 필수 | `<name>.glb`와 `<name>.json`을 쓸 폴더 |
| `--dcs FOLDER` | 자동으로 찾음 | DCS World 폴더 ([어디서 찾는지](list.md#where-the-install-is-found)) |
| `--name NAME` | 지도의 이름 | 레벨의 이름과 그 파일들의 이름 |
| `--around LAT LON KM` | - | 한 점의 양옆 이 km만큼의 정사각형만 |
| `--bounds X0 Z0 X1 Z1` | - | DCS 미터 단위의 이 상자 안만 (x는 북쪽, z는 동쪽) |
| `--cell M` | `0` | 메시를 성기게 함: *M* 미터 안의 모든 꼭짓점이 하나가 됩니다 (0: 게임 자체의 삼각형) |
| `--seabed` | 꺼짐 | 바다 밑바닥을 지면으로 남김 (기본값은 뺍니다) |
| `--no-water` | 꺼짐 | 평평한 바다를 뺌 |
| `--no-buildings` | 꺼짐 | 지도 장면의 건물을 뺌 |
| `--force` | 꺼짐 | 아주 큰 맵을 전체, 최고 상세도로 내보냄 |
| `--projection LON0 FE FN` | 지도의 것 | 이 도구가 모르는 지도의 횡메르카토르 상수 ([fit](fit.md)) |

프로그램이 출력하는 모든 옵션: [명령 참조](../cli-reference.md).

## 크기 {#size}

게임의 메시는 적응형입니다. 열린 바다는 수 킬로미터짜리 삼각형으로, 해안과 도로는 몇 미터짜리 삼각형으로 되어 있습니다. 작은 지도는 수백만 개의 삼각형이고, 큰 지도는 수천만 개의 꼭짓점입니다. 읽어야 할 꼭짓점이 3천만 개를 넘으면 `level`은 멈추고(종료 상태 1), 영역을 고르거나, 더 성긴 메시(`--cell 50`)를 쓰거나, `--force`를 쓰라고 알립니다.

종료 상태: 0은 완료, 1은 실패 또는 너무 큼, 2는 설치본이나 지도를 찾지 못함입니다(찾은 지도 목록을 보여 줍니다).

## 예시 {#examples}

```bash
heat3d-dcs-maps level <theatre> -o levels                                       # 전체, 최고 상세도
heat3d-dcs-maps level <theatre> --around <lat> <lon> 12 -o levels --name Part   # 24km 정사각형
heat3d-dcs-maps level <theatre> --bounds 1000 2000 1390 2390 -o levels          # DCS 미터 단위의 상자
heat3d-dcs-maps level <theatre> --cell 50 -o levels                             # 전체, 50m로 성기게
heat3d-dcs-maps level <theatre> --no-buildings --no-water -o levels             # 지면만
```

파일에 무엇이 들어 있는지: [레벨 파일](output.md).
