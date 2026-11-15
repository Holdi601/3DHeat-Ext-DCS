---
title: "지명: towns"
nav_order: 5
lang: "ko"
source: towns.md
source_hash: "80a352aef3e8"
nav_exclude: true
search_exclude: true
---
# 지명: `towns` {#place-names-towns}

```text
heat3d-dcs-maps towns <theatre> [--dcs FOLDER]
```

맵의 지명을 `map/towns.lua`에서 찾아 JSON으로 출력합니다(텍스트로만 읽으며 실행하지 않습니다). 각 마을의 이름, 위도와 경도, 그리고 맵의 투영을 거친 DCS `x`(북쪽)와 `z`(동쪽) 미터 값을 담습니다.

1. [`list`](list.md)로 맵의 폴더 이름을 찾으세요.
2. `heat3d-dcs-maps towns <theatre> > towns.json`을 실행하세요.
3. `x`/`z` 값으로 레벨에 이름표를 달거나, 기록의 위치를 확인하세요.

![가상 설치본의 마을들](../assets/img/towns.svg)

| 옵션 | 하는 일 |
|---|---|
| `theatre` | `Mods\terrains` 아래의 폴더 이름 |
| `--dcs FOLDER` | DCS World 폴더 |

레벨 영역 안의 마을들은 `<name>.json`에도 들어 있으며, 각 마을 아래 지면의 높이도 함께 있습니다 ([레벨 파일](output.md)).
