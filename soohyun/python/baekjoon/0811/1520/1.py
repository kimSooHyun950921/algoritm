import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def print_board(board):
    for row in board:
        print(*row)
    print("")

def solution(N, M):
    def search(row, col, board):
        if row == N-1 and col == M - 1:
            board[row][col][1] = 1
            return 1
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                if board[row][col][0] > board[nr][nc][0]:
                    if board[nr][nc][2]:
                        board[row][col][1] += board[nr][nc][1]
                    else:
                        board[nr][nc][2] = True
                        board[row][col][1] += search(nr, nc, board)              
        return board[row][col][1]
    return search

def main():
    N, M = map(int, input().rstrip().split(" "))
    board = [[[value, 0, False] for value in list(map(int, input().rstrip().split(" ")))] for _ in range(N)]
    board[0][0][2] = True
    print(solution(N, M)(0, 0, board))

if __name__ == "__main__":
    main()