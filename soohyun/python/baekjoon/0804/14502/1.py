import sys
from collections import deque
input = sys.stdin.readline

def dfs(N, cur_size, visited, numbers):
    result = []
    visited = [False] * N
    if cur_size == 3:
        result.append(tuple(numbers))
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                if cur_size == 0 or numbers[-1] < i:
                    numbers.append(i)
                    cur_size += 1
                    result.extend(dfs(N, cur_size, visited, numbers))
                    visited[i] = False
                    numbers.pop()
                    cur_size -= 1
    return result

def bfs(start, board, height, width, visited):
    queue = deque([start])
    count = 0
    while queue:
        row, col = queue.popleft()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < height and 0 <= nc < width:
                if board[nr][nc] == 0 and visited[nr][nc] == 0:
                    visited[nr][nc] = 3
                    count += 1
                    queue.append((nr, nc))
    return count

def virus_bfs(virus, board, virus_visited):
    queue = deque([virus])
    while queue:
        row, col = queue.popleft()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if virus_visited[nr][nc] == 0 and (board[nr][nc] == 0 or board[nr][nc] == 2):
                    virus_visited[nr][nc] = 2
                    queue.append((nr, nc))
    

def print_board(board):
    print("==========")
    for row in board:
        print(*row)
    print("==========")


def solution(height, width, board, blank_list, virus_list):
    wall_list = dfs(len(blank_list), 0, [False]*len(blank_list), [])
    max_safe_zone = 0
    for wall in wall_list:
        safe_zone = 0
        #wall_set = {blank_list[w1], blank_list[w2], blank_list[w3]}
        visited = [[0 for _ in range(width)] for _ in range(height)]
        for w in wall:
            visited[blank_list[w][0]][blank_list[w][1]] = 1
        for virus in virus_list:
            if not visited[virus[0]][virus[1]] == 2:
                visited[virus[0]][virus[1]] = 2
                virus_bfs(virus, board, visited)

        for r in range(height):
            for c in range(width):
                if board[r][c] == 0 and visited[r][c]==0 and (r, c):
                    visited[r][c] = 3
                    safe_zone += 1
                    safe_zone += bfs((r, c), board, height, width, visited)
        #if safe_zone > 23:
        #    print_board(visited)
        #    print(safe_zone, max_safe_zone)
        max_safe_zone = max(max_safe_zone, safe_zone)
    return max_safe_zone

def main():
    height, width = map(int, input().rstrip().split(" "))
    blank_list = []
    virus_list = []
    board = list()
    for r in range(height):
        row = list()
        for c, value in enumerate(map(int, input().rstrip().split(" "))):
            if value == 0:
                blank_list.append((r, c))
            elif value == 2:
                virus_list.append((r, c))
            row.append(value)
        board.append(row)
    print(solution(height, width, board, blank_list, virus_list))

if __name__ == "__main__":
    main()