# 3시간 16분
import sys
from collections import defaultdict, deque
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

def eat_fertilizer(tree, board):
    for i in range(len(board)):
        for j in range(len(board)):
            new_tree = deque([])
            dead_tree = 0
            while tree[i][j]:
                year = tree[i][j].popleft()
                if  board[i][j] - year >= 0:
                    board[i][j] -= year
                    new_tree.append(year+1)
                else:
                    dead_tree += year // 2
            tree[i][j]= new_tree
            board[i][j] += dead_tree


def change_fertilizer(loc, dead_tree, board):
    for year in dead_tree:
        board[loc[0]][loc[1]] += year//2


def propagate(board_size, board, tree):
    for i in range(board_size):
        for j in range(board_size):
            for idx in range(len(tree[i][j])):
                if tree[i][j][idx] % 5 == 0:
                    for dr, dc in zip([-1, 0, 1, 0, -1, 1, -1, 1], [0, -1, 0, 1, 1, -1, -1, 1]):
                        nr, nc = i + dr, j + dc
                        if 0 <= nr < board_size and 0 <= nc < board_size:
                            tree[nr][nc].appendleft(1)


def add_fertilizer(board_size, fertilizer, board):
    for i in range(board_size):
        for j in range(board_size):
            board[i][j] += fertilizer[i][j]


def count_live_tree(tree):
    count = 0
    for row in tree:
        for col in row:
            count += len(col)
    return count


def start_finance(board_size, year, fertilizer, tree, board):
    for _ in range(year):
        # 양분먹기 & 죽은 나무의 양분변화 
        eat_fertilizer(tree, board)
        # 나무번식
        propagate(board_size, board, tree)
        # 양분추가
        add_fertilizer(board_size, fertilizer, board)
    # 살아있는 나무 세기
    print(count_live_tree(tree))


def main():
    board_size, num_of_tree, year = map(int, input().rstrip().split(" "))
    fertilizer = [list(map(int, input().rstrip().split(" "))) for _ in range(board_size)]
    tree = [[deque([]) for _ in range(board_size)] for _ in range(board_size)]
    board = [[5 for _ in range(board_size)] for _ in range(board_size)]
    for _ in range(num_of_tree):
        x, y, old = map(int, input().rstrip().split(" "))
        tree[x-1][y-1].append(old)

    start_finance(board_size, year, fertilizer, tree, board)


if __name__ == "__main__":
    main()