import sys
input = sys.stdin.readline
def game(board, N, start_N):
    min_value = 2100000000
    # 1<<1 == 2**1, 1<<2== 2**2 
    # 2 ** N과 동일
    for i in range(1<<N):
        sum_value = 0
        for c in range(N):
            value = 0
            for r in range(N):
                state = (board[r] & (1 << c)) >> c
                if (1<<r) & i != 0:
                    state = ~state & 1
                if state == 1:
                    value += 1
            sum_value += min(value, N-value)
        min_value = min(min_value, sum_value)
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