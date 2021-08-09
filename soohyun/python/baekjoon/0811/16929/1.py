from collections import deque
def recursive(visited, start, board, row, col,prev, count):
    is_cycle = False
    alpha = board[start[0]][start[1]]
    for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        nr, nc = start[0] + dr, start[1] + dc
        if 0 <= nr < row and 0 <= nc < col:
            if board[nr][nc] == alpha:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    if recursive(visited, start, board, row, col, prev, count+1):
                       return True
                    visited[nr][nc] = False 
                else:
                    if count >= 4 and prev != (nr, nc):
                        return True
    return is_cycle


def bfs(visited, start, board, row, col):
    queue = deque([(start, start, 1, {start})])
    alpha = board[start[0]][start[1]]
    while queue:
        prev_loc, loc, count, cycle_set = queue.popleft()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = loc[0] + dr, loc[1] + dc
            if 0 <= nr < row and 0 <= nc < col:
                if board[nr][nc] == alpha:
                    visited[nr][nc] = True
                    if (nr, nc) not in cycle_set:
                        new_set = set()
                        new_set = new_set.union(cycle_set)
                        new_set.add((nr, nc))
                        queue.append((loc, (nr, nc), count+1, new_set))
                    else:
                        if count >= 4 and (nr, nc) in cycle_set:#nr == start[0] and nc == start[1]:
                            if prev_loc != (nr, nc):
                                return True


def dfs(visited, start, board, row, col):
    queue = deque([(start, start, 1, {start})])
    alpha = board[start[0]][start[1]]
    while queue:
        prev_loc, loc, count, cycle_set = queue.pop()
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = loc[0] + dr, loc[1] + dc
            if 0 <= nr < row and 0 <= nc < col:
                if board[nr][nc] == alpha:
                    visited[nr][nc] = True
                    if (nr, nc) not in cycle_set:
                        new_set = set()
                        new_set = new_set.union(cycle_set)
                        new_set.add((nr, nc))
                        queue.append((loc, (nr, nc), count+1, new_set))
                    else:
                        if count >= 4 and (nr, nc) in cycle_set:#nr == start[0] and nc == start[1]:
                            if prev_loc != (nr, nc):
                                return True
    return False


def solution(row, col, board):
    visited = [[False for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if not visited[i][j]:
                visited[i][j] = True
                #cycle = bfs(visited, (i, j), board, row, col)   
                #cycle = bfs(visited, (i, j), board, row, col)  
                cycle = recursive(visited, (i, j), board, row, col, (i, j), 0)  
                if cycle:
                    return 1
    return -1

def main():
    row, col = map(int, input().rstrip().split(" "))
    board = [list(input().rstrip()) for _ in range(row)]
    result = solution(row, col, board)
    if result == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()