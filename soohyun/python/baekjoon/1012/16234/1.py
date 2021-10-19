# bfs를 통하여 차이가나는 인접한것 모두 찾기
# 자료구조: 셋안에 튜플
# 방문하지 않는것에 한해서 계속 찾기
# 변경하지 않았다면 False를 반환
from collections import deque
def bfs(visited, board, start, L, R, size):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    move_list = [start]
    person_list = [board[start[0]][start[1]]]
    while queue:
        row, col = queue.popleft()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size:
                if not visited[nr][nc]:
                    if L <= abs(board[nr][nc] - board[row][col]) <= R:
                        queue.append((nr, nc))
                        move_list.append((nr, nc))
                        person_list.append(board[nr][nc])
                        visited[nr][nc] = True
    return move_list, person_list

def print_board(board):
    print()
    for row in board:
        print(*row)

def solution(board, L, R, size):
    # 인접한것 찾기
    days = 0
    while True:
        visited = [[0 for _ in range(size)] for _ in range(size)]
        move_list = list()
        person_list = list()
        for i in range(size):
            for j in range(size):
                if not visited[i][j]:
                    move, person = bfs(visited, board, (i, j), L, R, size)
                    move_list.append(move)
                    person_list.append(person)
        #print_board(move_list)
        #print_board(board)
        if len(move_list) == size*size:
            break
        for i, move in enumerate(move_list):
            people = sum(person_list[i])//len(move)
            for row,  col in move:
                board[row][col] = people
        days += 1
    return days

def main():
    size, L, R = map(int, input().rstrip().split(" "))
    board = []
    for _ in range(size):
        board.append(list(map(int, input().rstrip().split(" "))))
    print(solution(board, L, R, size))

if __name__ == "__main__":
    main()
