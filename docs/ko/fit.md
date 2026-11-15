---
title: "투영: fit"
nav_order: 6
lang: "ko"
source: fit.md
source_hash: "eb9303fc94ef"
nav_exclude: true
search_exclude: true
---
# 투영: `fit` {#projections-fit}

```text
heat3d-dcs-maps fit <recording>
```

모든 맵(theatre)은 각자 고유한 상수를 가진 횡메르카토르 투영입니다. 이 도구는 검사를 거친 맵들의 상수를 알고 있습니다. 모르는 맵은, 위도/경도와 DCS 미터 값을 모두 담은 기록이라면 무엇에서든 `fit`이 그 상수를 찾아냅니다. 예를 들어 한 비행에 대한 3DHeat Watcher 세션이 그런 기록입니다.

1. 3DHeat Watcher로 그 맵에서 비행을 기록하세요 (또는 `lat`, `lon`, `x`, `z` 열이 있고 DCS 미터 단위인 기록이면 무엇이든 괜찮습니다. x는 북쪽으로의 미터, z는 동쪽으로의 미터이며, DCS 전체에서 이 규칙을 따릅니다).
2. `heat3d-dcs-maps fit "<session>/heat.parquet"`를 실행하세요 (또는 `.jsonl`이나 `.csv` 파일).
3. 맞춘 투영을 JSON으로, 점들에 대한 평균 제곱근 오차, 그리고 쓸 `--projection` 인수를 출력합니다.
4. 이 값으로 레벨을 만드세요:
   `heat3d-dcs-maps level <theatre> --projection <LON0> <FE> <FN> -o levels`.

![가상 기록에 대한 fit](../assets/img/fit.svg)

그림의 기록은 알려진 투영으로 만든 점 아홉 개이며, `fit`은 이것을 밀리미터 단위까지 정확히 되찾습니다.

| 인수 | 하는 일 |
|---|---|
| `recording` | `lat`, `lon`, `x`, `z` 열(DCS 미터)이 있는 `.parquet`, `.jsonl` 또는 `.csv`. 읽히지 않는 행은 건너뜁니다 |

이 투영은 C. F. F. Karney가 제시한 Krüger 급수입니다("Transverse Mercator with an accuracy of a few nanometers", Journal of Geodesy 85, 2011).

종료 상태: 0은 좋은 맞춤(평균 제곱근 오차 5m 미만), 1은 나쁜 맞춤이거나 쓸 수 있는 행이 셋보다 적음, 2는 파일을 찾지 못함입니다.
