import math

def print_board(board):
    print()
    for row in board:
        print(*row)
    print()

def coloring_last(fstart, fend, r, new_board):
    if fstart >= 0 and fend >= 0:
        for c in range(fstart, fend):
            new_board[r][c] = 5

def divide_section(d1, d2, x, y, new_board, N):
    for r in range(N):
        fstart, fend = -1, -1
        for c in range(N):
            if new_board[r][c] == 5:
                if fstart == -1:
                    fstart = c
                else:
                    fend = c
            else:
                if 0 <= r < x+d1 and 0 <= c <= y:
                    new_board[r][c] = 1
                elif 0 <= r <= x+d2 and y-1 < c <= N-1:
                    new_board[r][c] = 2
                elif x+d1-1 <= r <= N-1 and 0 <= c <= y-d1+d2-1:
                    new_board[r][c] = 3
                elif x+d2 < r <= N-1 and y-d1+d2 <= c <= N-1:
                    new_board[r][c] = 4
        coloring_last(fstart, fend, r, new_board)

def make_section_line(limit, dr, dc, x, y, new_board):
    for l in range(0, limit):
        cdr, cdc = dr*l, dc*l
        nr, nc = x + cdr, y + cdc
        new_board[nr][nc] = 5

def calc(new_board, board):
    section_sum = [0, 0, 0, 0, 0]
    for i, row in enumerate(new_board):
        for j, value in enumerate(row):
            section_sum[value-1] += board[i][j]
    return section_sum

def find_section(x, y, board, N):
    answer = math.inf
    for d1 in range(1, N):
        for d2 in range(1, N):
            if x + d1 + d2 < N and y - d1 >= 0 and y + d2 < N:
                new_board = [[0 for _ in range(N)] for _ in range(N)]

                make_section_line(d1+1, 1, -1, x, y, new_board)
                make_section_line(d2+1, 1, 1, x, y, new_board)
                make_section_line(d2+1, 1, 1, x+d1, y-d1, new_board)
                make_section_line(d1+1, 1, -1, x+d2, y+d2, new_board)
                
                divide_section(d1, d2, x, y, new_board, N)
                section_sum = calc(new_board, board)
                answer = min(max(section_sum) - min(section_sum), answer)
    return answer

def solution(board, N):
    answer = math.inf
    for r in range(N):
        for c in range(N):
            answer = min(answer, find_section(r, c, board, N))
    return answer

def main():
    N = int(input().rstrip())
    board = list()
    for i in range(N):
        row = list(map(int, input().rstrip().split(" ")))
        board.append(row)
    result = solution(board, N)
    print(result)

if __name__ == "__main__":
    main()
