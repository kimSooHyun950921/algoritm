# 1. 문제의 핵심
## 1.1. 문제 요약
```
   N극과 S극이 있는 4개의 톱니바퀴를 회전시키기
   N극과 S극이 맞닿아 있는경우 인접한 톱니바퀴는 회전하는 톱니와 반대방향으로 회전한다. 
```
## 1.2. 알고리즘
- 재귀
- 구현


# 2. 구현 방법
## 2.1. 자료구조 
- 4개의 바퀴(wheels): 2차원 배열(배열안에 deque로 구성하도록함)
## 2.2. 알고리즘
```
규칙: N의 2번째와 N+1의 6번째바퀴가 인접
      N의 6번째와 N-1의 2번째바퀴가 인접
```
```python
while 회전할 톱니바퀴 입력수
    1. 돌릴 톱니바퀴 찾기(재귀)
        - 현재톱니바퀴(N번째)를 회전하는곳에 체크
        - 인접한 톱니바퀴(N-1, N+1)가 아래 조건을 만족하면 똑같이 반복
            - 인접한 톱니바퀴 범위를 넘어가지 않고
            - 방문한 톱니바퀴가 아니고
            - 앞으로 방문할 톱니바퀴가 서로 다른 극일경우
    2. 톱니바퀴 돌리기
        - 톱니바퀴 횟수만큼
        - 반시계방향이면 앞에서 빼고 뒤로 넣는 방법
        - 시계방향이면 뒤에서 빼고 앞으로 넣는 방법이용
3. 계산
```

# 3. Code Snippet
## 3.1. 돌릴 톱니바퀴 찾기
```python
def can_move(nidx, idx, didx, wheels):
    if didx == -1: # 숫자가 작아지는 바퀴로가면
        return wheels[idx][6] != wheels[nidx][2]
    else:
        return wheels[idx][2] != wheels[nidx][6]

def get_move_wheel(visited, moved, idx, direction, wheels):
    moved[idx] = direction # 현재 바퀴는 움직여야하므로 제크
    for didx in [-1, 1]:
        nidx = idx + didx
        # 범위 안에 있고, 방문했고, 인접한곳이 움직일수있는것이면
        if 0 <= nidx < 4 and not visited[nidx] and can_move(nidx, idx, didx, wheels):
            # 방문표시후
            visited[nidx] = 1
            # 다음 바퀴를 회전시킬수있는지 여부룰 확인한다.
            moved = get_move_wheel(visited, moved, nidx, -direction, wheels)
    return moved
```

# 4. 복기할것
1. 걸린시간: 2시간 45분
2. 재귀로 인접한곳을 찾는곳이 오래걸림
    - 회전이 안되는 N인경우 N+1, N-1도 회전이 안됨
    - 재귀를 만들때는 N과 N-1, N+1의 관계로 생각하는게 편할것같다.