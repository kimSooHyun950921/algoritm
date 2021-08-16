# 문제의 핵심
- 시뮬레이션

# 자료구조
- 보드: 2차원 배열
    - 행: 세로 사다리 갯수
    - 열: 가로 놓을수있는 사다릴 갯수(count)
    - 단, 1에서 2로가는 사다리는 board[1][1]=1으로 표현한다.

# 알고리즘
- 최소사다리는 4로 초기화
- 현재 사다리탔을때 조건을 만족하면(i가 i로 도착하면) 반환
- 조건을 만족하지 않고 3이상이라면 무조건 -1(왜? 맨앞에 사다리 타기 조건을 만족할것이므로)
- 3미만이면 행을 바꿔가면서 사다리를 하나씩 추가한다.

# Code Snippet
```python
# 사다리 타기
def leddaring(board, row, col):
    for i in range(row):
        #현 위치를 i로 지정
        current_position = i
        for j in range(col):
            # 만약 현재위치에 사다리가 있으면
            if board[current_position][j] == 1:
                # 다음행으로 넘어간다.
                current_position = current_position + 1
            # 이전 위치에 사다리가 있으면
            elif current_position > 0 and board[current_position-1][j] == 1:
                # 이전위치로 넘어간다.
                current_position = current_position - 1
        # 사다리 탄결과 현재위치와 이전위치가 다르다면
        if i != current_position:
            # False로 넘어감
            return False
    return True
```
```python
def init_game(board, row, col, count):
    def put_leddar(row_start, cur_count):
        min_leddar = 4
        if leddaring(board, row, col):   
            min_leddar = min(min_leddar, cur_count)
            return min_leddar
        if cur_count >= 3:
            return min_leddar
        for r in range(row_start, row):
            for c in range(col):
                if board[r][c] == 0:
                    # 같은 열을가지는 가로 사다리는 있을수없다
                    #|-|-|-|  ==> 안됨
                    #|-| | | 
                    if (r > 0 and board[r-1][c] == 1) or board[r+1][c] == 1:
                        continue
                    board[r][c] = 1
                    min_leddar = min(min_leddar, put_leddar(row_start+1, cur_count+1))
                    board[r][c] = 0
        return min_leddar
    return put_leddar

```

# 복기할것
- 수많은 시간초과, 수많은 틀렸습니다가 난무
- 알고리즘 문제
    - 3초과가 아닌 3이상일때로 제한 조건을 건다.
        - 3초과가 나면 시간초과: 사다리를 4개까지 놓고 확인하기때문
    - 위치우선순위: 사다리타는것을 먼저 확인하고 3이상인지 확인한다.
        - 그래야 정답이 -1일때와 3일때를 구분할 수 있음
    - 한번 재귀를 돌릴때 다음 사다리부터 시작하도록 한다.
        - 이유는 정확히 모르지만 그위치에 한번 더 놓는다하더라도 다시 돌아올 수 없기때문
    - odd 사다리만 했더니 틀렸음 모든 경우의 수를 생각해줘야함
        - 아마 0일때 생각을 안해준것같다.