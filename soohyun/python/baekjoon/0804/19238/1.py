import sys
from collections import deque
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def bfs_start(N, taxi_loc, board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi_loc[0]][taxi_loc[1]] = True
    queue = deque([(taxi_loc, 0)])
    same = list()
    while queue:
        cur_loc, cur_engine = queue.popleft()
        if board[cur_loc[0]][cur_loc[1]] > 1:
            heappush(same, (cur_engine, cur_loc[0], cur_loc[1]))
        for dr, dc in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
            r, c = cur_loc[0] + dr, cur_loc[1] + dc
            if 0 <= r < N and 0 <= c < N:
                if board[r][c] != 1 and not visited[r][c]:
                    visited[r][c] = True
                    if board[r][c] > 1:
                        heappush(same, (cur_engine+1, r, c))
                    queue.append(((r, c), cur_engine+1))
        if same:
            heapify(same)
            cur_engine, r, c= heappop(same)
            return (r, c), cur_engine
    return (0, 0), -1


def bfs_end(N, taxi_loc, end_loc ,board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[taxi_loc[0]][taxi_loc[1]] = True
    queue = deque([(taxi_loc, 0)])
    while queue:
        cur_loc, cur_engine = queue.popleft()
        if cur_loc == end_loc:
            return cur_loc, cur_engine
        for dr, dc in zip([-1, 0, 0, 1], [0, -1, 1, 0]):
            r, c = cur_loc[0] + dr, cur_loc[1] + dc
            if 0 <= r < N and 0 <= c < N:
                if board[r][c] != 1 and not visited[r][c]:
                    visited[r][c] = True
                    if (r, c) == end_loc:
                        return (r, c), cur_engine + 1
                    queue.append(((r, c), cur_engine+1))
    return (0, 0), -1


def solution(N, M, engine, taxi_loc, board, end):
    for _ in range(M):
        if engine >= 0:
            taxi_loc, used_engine = bfs_start(N, taxi_loc, board)
            
            if used_engine < 0:
                return -1
            engine -= used_engine
        else:
            return -1
        if engine >= 0:
            board[taxi_loc[0]][taxi_loc[1]] = 0
            taxi_loc, used_engine = bfs_end(N, taxi_loc, end[taxi_loc], board)
            
            if used_engine < 0:
                return -1
            engine -= used_engine
            if engine < 0:
                return -1
            engine += used_engine*2
        else:
            return -1
    return engine

def print_board(board):
    print("=====")
    for i in board:
        print(*i)
    print("======")

def main():
    N, M, engine = map(int, input().rstrip().split(" "))
    board = [ list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    taxi_loc = tuple(map(int, input().rstrip().split(" ")))
    taxi_loc = taxi_loc[0] - 1 ,taxi_loc[1] - 1
    end = dict()
    for i in range(M):
        s_r, s_c, e_r, e_c = map(int, input().rstrip().split(" "))
        board[s_r-1][s_c-1] = i + 2     
        end[(s_r-1, s_c-1)] = (e_r-1, e_c-1)
    print(solution(N, M, engine, taxi_loc, board, end))
if __name__ == "__main__":
    main()