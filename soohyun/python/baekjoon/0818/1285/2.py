import sys
import math
sys.setrecursionlimit(100000000)
def s2i(character):
    if character == 'H':
        return 0
    else:
        return 1

def reverse(num):
    if num == 0:
        return 1
    else:
        return 0

def game(board, N, start_N):
    # 열을 뒤집음
    min_value = math.inf
    sum_value = 0
    for c in range(N, -1, -1):
        value = 0
        maximum = 1<<c
        for r in range(N):
            value += (board[r] & maximum) >> c
        sum_value += min(value, N-value, min_value)
    min_value = min(min_value, sum_value)
    # 행을 뒤집음
    original_board = [row for row in board]
    maximum = (1<<N)-1
    for r in range(start_N, N):
        board[r] = ~board[r] & maximum
        min_value = min(min_value, game(board, N, r+1))
        board =  [row for row in original_board]
    return min_value

def main():
    N = int(input().rstrip())
    board = list()
    for _ in range(N):
        row = 0
        for idx, j in enumerate(input()):
            if j == 'H':
                row += (1 << N-idx-1) & 0
            if j == 'T':
                row += (1 << N-idx-1)
        board.append(row)
    print(game(board, N, 0))

if __name__ == "__main__":
    main()