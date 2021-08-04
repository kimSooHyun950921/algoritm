# 문제의 핵심
- 스택(deque)
- 시뮬레이션

# 알고리즘
1. turn을 1000번 이하까지 아래를 반복
    - 말개수만큼 아래를 반복
        - 현재말의 다음위치를 계산
        - 다음위치가 범위안에 있거나 파란색(2보다 작음) 인경우 현재말위에 있는 모든 말들을 현재말과 함께 이동(move)
            - 이동한곳이 빨간색이면 반전
            - 아니면 그대로 넣음
        - 이동한곳이 4이상이면 멈춤
        - 범위밖에있거나 파란색(2)인경우 방향을 바꾼후 현재 말 위에 있는 말들을 현재말과 함께이동 (move)
            - 이동한곳이 빨간색이면 반전
            - 아니면 그대로 넣음
        - 이동한 곳이 4이상이면 멈춤
2. turn이 1000넘으면 -1, 그렇지 않으면 turn 수를 반환

# 자료구조
- board
    - 빨,파,흰의 정보를 담고있는 보드
    - 2차원 배열
- horse_board
    - 말들의 정보를 담고 있는 보드
    - 2차원배열안 deque
        ```
        deque([0]) deque([]) deque([]) deque([8]) deque([]) deque([])
        deque([1]) deque([]) deque([]) deque([]) deque([]) deque([6])
        deque([]) deque([]) deque([]) deque([]) deque([]) deque([])
        deque([]) deque([]) deque([]) deque([]) deque([]) deque([])
        deque([]) deque([9, 4]) deque([3, 2]) deque([]) deque([]) deque([])
        deque([7]) deque([]) deque([]) deque([]) deque([]) deque([5])
        ```
- horse_loc
    - 말들의 번호와, 행렬, 위치를 담고있는 리스트
    - 1차원 배열안 class 
    ```
    [loc: (0, 0), d:2], [loc: (1, 0), d:1], [loc: (4, 2), d:3], [loc: (4, 2), d:1], [loc: (4, 1), d:4], [loc: (5, 5), d:1], [loc: (1, 5), d:3], [loc: (5, 0), d:1], [loc: (0, 3), d:3], [loc: (4, 1), d:2], 
    ```

# Code Snippet
1. 현재말위의 모든 말 가져오는 코드
```python
def get_horse_list(horse_board, horse, target):
    horse_list = []
    while True:
        # 현재말을 마주칠때까지 계속 pop함
        current_horse = horse_board[horse.row][horse.col].pop()
        # horse_list에 차례로 담아줌(거꾸로 저장됨)
        horse_list.append(current_horse)
        # 현재 말이 마주치면 멈춘다.
        if current_horse == target:
            break
    return horse_list
```
2. 말을 이동하는 코드
```python
def move(nr, nc, board, horse_list, horse_board, horse_loc):
    for j in range(len(horse_list)):
        #빨간색인경우
        if board[nr][nc] == 1:
            stacked_horse = horse_list[j]
            # 반대로 저장된것 그대로 넣는다.
            horse_board[nr][nc].append(stacked_horse)
        else:
            # 반대로 저장된것을 거꾸로해서 넣는다.
            stacked_horse = horse_list[len(horse_list) - j - 1]
            horse_board[nr][nc].append(stacked_horse)
        horse_loc[stacked_horse].row = nr
        horse_loc[stacked_horse].col = nc
```


# 복기할것
- 저장순서 확인할것
    - <-안쪽--------바깥쪽-->\
      [0, 1, 2, 3, 4, 5, 6, 7]
    - 바깥쪽에서 빼는경우: pop을 통해 뺀다
    - 그대로 넣어줘야하는경우: append를 통해 넣는다.(단, 뺀것의 반대로 넣어주어야한다.)
    - 반대로 넣어줘야하는경우: append를 통해 그대로 놓는다.
- 문제 이해
    - 4개 이상되는순간 멈춘다.