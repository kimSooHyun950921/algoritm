# 문제의 핵심
- dp
- dfs

# 자료구조
- board: 3차원 배열(행, 열 값, 방문개수, 방문여부)
```
[50, 3, True] [45, 2, True] [37, 2, True] [32, 2, True] [30, 1, True]
[35, 1, True] [50, 0, False] [40, 0, False] [20, 1, True] [25, 1, True]
[30, 1, True] [30, 0, False] [25, 0, False] [17, 1, True] [28, 0, False]
[27, 1, True] [24, 1, True] [22, 1, True] [15, 1, True] [10, 1, True]
```
# 알고리즘
- 0행 0부터 상하좌우로 돌며 이동할곳 탐색
    - 다음 위치가 범위내에 있고,
    - 현재위치보다 다음위치가 작다면
    - 이미 방문한경우는 다음위치 + 현재위치해서 현재위치 갱신
    - 방문하지 않은경우는 새롭게 재귀로 탐색
- 행, 열의 끝까지 간경우 1을 반환

# 복기할것, 실수한것
- 방문표시를 제대로 안하는 경우 방문한후 0이된 경우 방문을 안했다고 간주하여 시간이 더 오래 걸릴 수 있음(원소 값에 세번째 원소 True False를 추가한 이유)
