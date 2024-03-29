# 문제의 핵심
- 재귀
- 브루트포스

# 사용 자료구조
- 보드(board): 2차원 리스트(동일 값을 가지진 않음)
    ```
    0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 0
    0 2 4 6 8 10 13 16 19 25 30 35 40 0
    0 2 4 6 8 10 12 14 16 18 20 22 24 25 30 35 40 0
    0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 28 27 26 25 30 35 40 0
    ```
- 10개턴 주사위(dice): 1차원리스트(입력값과 동일)
    ```
    1 2 3 4 1 2 3 4 1 2
    ```
- 현재 움직이는 말 모음(horse_list): 1차원 리스트안에 Horse라는 객체
    ```
    [Horse(row, col, direction)]
    [(1, 13):0], [(1, 13):0], [(1, 10):30], [(1, 5):10]
    ```
# 알고리즘
- 10 턴이 될때까지 아래를 반복
    ```
    1. 윷놀이 판위에 있는 말들을 이동
        - 윷놀이 판위의 말들을 하나씩 다음을 반복
        - 말이 도착한것이 아니라면
            - 말의 다음위치로 변경
        - 다음에 놓을곳에 말이 없다면
            - 현재 말을 다음위치로 변경
            - 턴을 증가시켜주고 재귀로 들어감
            - 변경했던 위치 및 값을 원상복귀
    2. 새롭게 말을 윷놀이 판에 놓음
        - 0, 0 위치에서 턴에따른 다음위치 이동
        - 다음갈위치에 말이 없다면 새롭게 말을 놓는다
        - 턴을 증가시켜주고 재귀로 들어감
        - 추가했던 말을 삭제
    ```
- 복기할것
    - 실제 윷판과 윷판을 구현한 보드가 다름
        - board에서 동일한 위치가 다르게 표현된 경우가 있음 이를 일일 히 바꿔줘야함
    - 초반에 4개의 말을 모두 경우의수로 생각해서 너무 시간이 많이듦
        - 말을 새롭게 놓는경우/있는말을 돌리는경우로 바꿈 