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

def bfs(board, chosen_chick, house):
    city_dist = 0
    chosen_board= [[0 for c, val in enumerate(board[r])] for r in range(len(board))]
    for i, j in chosen_chick:
        chosen_board[i][j] = 2
    
    #print_board(chosen_board)
    for start in house:
        queue = deque([(start, 0)])
        visited = [[False for _ in range(len(board[i]))] for i in range(len(board))]
        chick_dist = 0
        while queue:
            (r, c), count = queue.popleft()
            if chosen_board[r][c] == 2:
                chick_dist += count
                break
            for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board):
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append(((nr, nc), count+1))   
        if chick_dist == 0:
            chick_dist = math.inf
        city_dist += chick_dist
    return city_dist 
           

def dfs(chick, board, house):
    def recursive(chosen, start, end):
        answer = math.inf
        if chosen:
            chosen_chick = [chick[j] for j in chosen]
            answer = bfs(board, chosen_chick, house)
        if len(chosen) < end:
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
