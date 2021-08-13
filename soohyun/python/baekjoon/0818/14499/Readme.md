# 문제의 핵심
- 시뮬레이션
- 주사위굴릴때 바뀌는 방향

# 사용 자료구조
- 주사위 굴리는것: 1차원 배열
- 주사위 값: 1차원 배열

# 알고리즘
1. 주사위를 굴린다.
2. 굴린후 보드의 값이 0이면 주사위 바닥을 보드에 복사
    굴린후 보드의 값이 0이아니면 보드값을 주사위에 복사, 보드는 0으로 바꿈
3. 굴린후 주사위가 천장을 바라보는쪽을 출력

# Code Snippet
1. 주사위 굴리는 코드
```python
def change_dice(num):
    if num == 1:
        num_1 = dice[1]
        num_3 = dice[3]
        dice[1] = dice[4]
        dice[3] = num_1
        dice[4] = dice[6]
        dice[6] = num_3
    elif num == 2:
        num_1 = dice[1]
        num_4 = dice[4]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[4] = num_1
        dice[6] = num_4
    elif num == 3:
        num_1 = dice[1]
        num_5 = dice[5]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[5] = num_1
        dice[6] = num_5
    elif num == 4:
        num_1 = dice[1]
        num_2 = dice[2]
        dice[1] = dice[5]
        dice[2] = num_1
        dice[5] = dice[6]
        dice[6] = num_2
```
# 복기할것
    1. 알고리즘 자체는 어렵지 않음
    2. 주사위 굴리는 방향으로 계속 바꿔줘야한다는것을 생각하지 못함 처음에는 무조건 그방향으로 가도록 설계
        - 2차원 배열을 만듦
            - 예를들면, 앞면이 4일때 상하좌우는 2, 5, 6, 1로 고정일것으로 착각 
            - 만약 상하로 굴리면 늘 동일하겠지만 좌우로 돌리면 앞면이 4일때 상하좌우도 바뀔 수 있음
        - 아예 계속 정육면체 도면의 숫자를 바꿔주어야 그 숫자들이 통일을 유지함