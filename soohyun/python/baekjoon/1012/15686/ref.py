# 자료구조
# 1차원 배열: 치킨위치가 담긴 리스트
# 2차원 배열: board
# 1차원 배열: 집위치가 담긴 배열
# 알고리즘
# dfs를 통해 0부터 치킨집개수만큼 dfs를 돌린다.
# 한번 넣어있을때마다 bfs를 통해 bfs 거리를 모두 구한다
# 이때의 최소값을 구한다.
from collections import deque
import math

def print_board(board):
    for row in board:
        print(*row)
    print()

def bfs(chosen_chick, house):
    dist = 0
    for hr, hc in house:
        min_value = math.inf
        for ccr, ccc in chosen_chick:
            min_value = min(min_value, abs(hr - ccr) + abs(hc - ccc))
        dist += min_value
    return dist
           

def dfs(chick, board, house):
    def recursive(chosen, start, end):
        answer = math.inf
        if len(chosen) == end:
            #print(chosen)
            chosen_chick = [chick[j] for j in chosen]
            answer = bfs(chosen_chick, house)
            return answer
        #print(len(chosen), start, end, chosen)
        for i in range(start, len(chick)):
            #print("i", i)
            chosen.append(i)
            answer = min(answer, recursive(chosen, i+1, end))
            chosen.pop()
        return answer
    return recursive

def main():
    r, m = map(int, input().rstrip().split(" "))
    board = [[0 for _ in range(r)] for _ in range(r)]
    chick = []
    house = []
    for i in range(r):
        for j, value in enumerate(list(map(int, input().rstrip().split(" ")))):
            board[i][j] = value
            if value == 1:
                house.append((i, j))
            elif value == 2:
                board[i][j] = 0
                chick.append((i,j))
    result = dfs(chick, board, house)([], 0, m)
    print(result)

if __name__ == "__main__":
    main()
