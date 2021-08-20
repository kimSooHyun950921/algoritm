# 문제의 핵심
- 구현
- deque

# 걸린시간
- 3시간 16분
# 사용 자료구조
- 나무 2차원 배열:deque()
- 비료를 가지고 있는 NxN 2차원 배열
- A를 저장하는 2차원 배열

# 알고리즘
- 나이가 어린 나무부터 자신의 나이만큼 양분을 먹음
    - 2차원 행열배열을 돌면서 진행
        - 현재 행/열의 새로운 나무리스트를 선언
        - **현재 행/열의 나무리스트를 하나씩 *앞* 에서 부터 뺀다(작은것부터 빼기위해서)**
        - 현재 양분을 줄 수 있는 여유가되면 현재나무의 연도수에 +1 해주고 새로운 나무리스트에 새롭게 추가해준다. 
        - 비료는(board) 가진것은 board나이만큼 제거해줌
        - 죽은 나무는 현재나이의 //2를 해서 계속 더해줌
    -2차원 행열의 원소를 도는것을 끝나면 현재 위치의 비료에 죽은나무를 더해준다.
- 나무번식
    - 인접한 8개에 나이가 1인 나무 생김
    - 번식가능한 나무나이 5배수
    - 나무리스트를 상하좌우8군대 돌면서 나무나이가 5배수라면 하나씩 *앞에서부터*추가해줌
-  양분추가
    - A[r][c] 만큼 양분추가
    - 비료에 더하기해줌
- 현재 나무 세기

# code snippet
    ```python
    def eat_fertilizer(tree, board):
        for i in range(len(board)):
            for j in range(len(board)):
                new_tree = deque([])# 데크추가
                dead_tree = 0 # 죽은나무의 비료들을 저장하기 위한것
                while tree[i][j]: # 현재 위치를 돌면서
                    year = tree[i][j].popleft() # 작은것들부터 제거
                    if  board[i][j] - year >= 0: # 비료를 줄 수 있으면
                        board[i][j] -= year # 비료를 제거하고
                        new_tree.append(year+1) #새로운 나무리스트에 추가해줌
                    else:
                        dead_tree += year // 2 # 비료를 줄 수 없으면 나무는 죽으므로
                                            # 죽은나무에 비료 추가
                tree[i][j]= new_tree # 새로운 나무들을 넣어줌
                board[i][j] += dead_tree # 죽은나무들의 비료의 총합은 비료에 추가해줌
    ```
2. 입력받는부분
    ```python
    board_size, num_of_tree, year = map(int, input().rstrip().split(" "))
    fertilizer = [list(map(int, input().rstrip().split(" "))) for _ in range(board_size)] # 비료 2차원배열
    tree = [[deque([]) for _ in range(board_size)] for _ in range(board_size)] # 트리는 2차원배열과 데크로 구성
    board = [[5 for _ in range(board_size)] for _ in range(board_size)] # 보드는 2차원배열의 5로초기화되기 구성
    for _ in range(num_of_tree):
        x, y, old = map(int, input().rstrip().split(" "))
        tree[x-1][y-1].append(old) #나이는 작은순서대로 들어온다고 가정
    ```
3. 전파하는 부분
```python
def propagate(board_size, board, tree):
    for i in range(board_size):
        for j in range(board_size):
            for idx in range(len(tree[i][j])):
                if tree[i][j][idx] % 5 == 0:
                    for dr, dc in zip([-1, 0, 1, 0, -1, 1, -1, 1], [0, -1, 0, 1, 1, -1, -1, 1]):
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < board_size and 0 <= nc < board_size:
                            tree[nr][nc].appendleft(1) # 앞에서부터 추가
```
# 복기할것
- 첫번째 버전: 
    - heappush로 구성
    - 비료먹기(봄), 죽인나무비료되기(여름), 전파(가을), 인공적으로 비료추가(겨울)로구성
    - 시간초과/틀림 ==> 정렬이 제대로 안되어있어서 틀림
- 두번째 버전
    - heap으로 구성
    - 비료먹기&죽인나무비료되기, 전파, 인공적비료추가 3개로 구성
        -죽인나무는 비료먹을때 list로 받아 없앰
        -heapify 추가로 정렬
    - 시간초과
- 세번째 버전 3과 동일
    - heapify 제거
    - 시간초과
- 네번째 버전
    - heap구성
    - 죽인나무 비료될때는 list로 받지 않고 int형 변수를 두어 값을 계속 저장하고있고 마지막에 한번에 빼줌
    - 시간초과
- 다섯번째 버전
    - deque로 변경
        - 입력받을때는 순서대로 들어온다가정(정렬된 상태로 들어온다 가정)
        - 뺄때는 작은것부터 뺌(popleft)
        - 넣을때는 순서대로 넣음
        - propagation시 앞에서부터 넣음(작은것으로 정렬해서 넣어야하므로)
    - 2차원 배열로 변경
        - 시간차이는 얼마 안날듯함
    - 통과
    - 근거
        - heappush는 log(n), deque는 log(1)
        - 별차이 안날줄알았는데 크게나서 놀람

