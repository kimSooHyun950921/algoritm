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
    for c in range(N):
        value = 0
        for r in range(N):
            value += board[r][c]
        sum_value += min(value, N-value, min_value)
    min_value = min(min_value, sum_value)
    # 행을 뒤집음
    original_board = [[col for col in row] for row in board]
    for r in range(start_N, N):
        board[r] = list(map(reverse, board[r]))
        min_value = min(min_value, game(board, N, r+1))
        board =  [[col for col in row] for row in original_board]
    return min_value

def main():
    N = int(input().rstrip())
    board = [list(map(s2i, input())) for _ in range(N)]
    print(game(board, N, 0))

if __name__ == "__main__":
    main()