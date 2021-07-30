# 문제의 핵심
```
    - 시뮬레이션
    - bfs(하나의 visited를 공유하기)
    - dfs 
```

# 알고리즘
1. dfs를통해 모든 세울 수 있는 벽의 모든 경우의수 만들어주기
2. 만들어진 모든 경우의 수를 통해 벽 세우기
3. bfs를통해 바이러스 전파시키기
4. bfs를 통해 남는 모든 안전 구역 세기

# 복기할것
- 급하게 풀지말고 천천히 풀것
- 빨리 푼사람 코드 찾아볼것

# 빨리푼사람 코드(출처: 백준아이디  jintak0401)
```python
from sys import stdin

input = stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d2 = [(-1, -1), (1, 1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]


def solve():
    N, M = map(int, input().split())
    board = []
    virus = []
    safeArea = []

    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(len(board[i])):
            if board[i][j] == 2:
                virus.append((i, j))
            elif board[i][j] == 0:
                safeArea.append((i, j))

    def nearWall(_x, _y, _board):
        l, r, u, d = False, False, False, False
        for dx, dy in d2:
            x, y = _x + dx, _y + dy
            if x < 0 or (x < _x and 0 <= y < M and _board[x][y] == 1):
                u = True
            elif x >= N or (x > _x and 0 <= y < M and _board[x][y] == 1):
                d = True
            if y < 0 or (y < _y and 0 <= x < N and _board[x][y] == 1):
                l = True
            elif y >= M or (y > _y and 0 <= x < N and _board[x][y] == 1):
                r = True
            if (l and r) or (u and d):
                return True

        return False

    def countSafeCell(a, b, c):
        _board = [[*board[i]] for i in range(len(board))]
        _board[a[0]][a[1]] = 1
        _board[b[0]][b[1]] = 1
        _board[c[0]][c[1]] = 1

        countSafeArea = len(safeArea) - 3
        if (nearWall(*a, _board) and nearWall(*b, _board) and nearWall(*c, _board)):

            q = [*virus]
            idx = 0
            while idx != len(q):
                _x, _y = q[idx]
                idx += 1
                for dx, dy in d:
                    x, y = _x + dx, _y + dy
                    if 0 <= x < N and 0 <= y < M and _board[x][y] == 0:
                        q.append((x, y))
                        _board[x][y] = 2
                        countSafeArea -= 1
            return countSafeArea

        return 0

    def buildWall():
        _ans = 0
        for i in range(len(safeArea)):
            for j in range(i + 1, len(safeArea)):
                for k in range(j + 1, len(safeArea)):
                    _ans = max(_ans, countSafeCell(safeArea[i], safeArea[j], safeArea[k]))
        return _ans

    return buildWall()


print(solve())

```