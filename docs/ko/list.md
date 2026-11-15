---
title: "맵 찾기: list"
nav_order: 2
lang: ko
source: list.md
source_hash: "334e2f7ab2b2"
nav_exclude: true
search_exclude: true
---
# 맵 찾기: `list` {#finding-theatres-list}

```text
heat3d-dcs-maps list [--dcs FOLDER]
```

명령줄이 처음입니까? 먼저 [시작하기 전에](before-you-start.md)를 읽으세요.

1. 한 번만 설치하세요: `git clone https://github.com/Holdi601/3DHeat-Ext-DCS`, 그 폴더에서 터미널을 열고 `python -m pip install -e .`를 실행합니다 (Python 3.10 이상. numpy가 함께 설치되며, `.parquet` 파일에 대한 `fit`을 위해 pyarrow도 설치됩니다).
2. `heat3d-dcs-maps list`를 실행하세요.
3. 설치된 맵마다 한 줄이 출력됩니다. 줄에는 폴더 이름(다른 명령이 받는 이름), 지면 파일의 크기, 타일과 꼭짓점 수, 위도/경도 투영을 알고 있는지, 그리고 읽을 수 있는지가 나옵니다. 각 줄의 끝은 `readable`이어야 합니다.

![가상 설치본에 대한 list](../assets/img/list.svg)

그림은 테스트가 만든 설치본(`tests/synth.py`)에서 실행한 결과이며, 게임에서 실행한 것이 아닙니다.

## 설치 위치를 찾는 방법 {#where-the-install-is-found}

`--dcs <folder>`(`Mods\terrains`를 담고 있는 폴더)를 주거나 `DCS_PATH` 환경 변수를 씁니다. 그러지 않으면 레지스트리, Steam 라이브러리, 그리고 흔한 폴더들을 찾아봅니다.

| 옵션 | 하는 일 |
|---|---|
| `--dcs FOLDER` | DCS World 폴더, `Mods\terrains`를 담고 있는 폴더 |

종료 상태: 0은 완료, 2는 설치본이나 맵을 찾지 못함입니다.
