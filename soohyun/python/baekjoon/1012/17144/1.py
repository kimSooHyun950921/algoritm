CWISE = [(0, 1), (-1, 0), (0, -1), (1, 0)]
CCWISE =  [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_board(board):
    print()
    for row in board:
        print(*row)
    print()

def blow(board, r, c):
    new_board = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                count = 0
                for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < r and 0 <= nc < c:
                        if board[nr][nc] == -1:
                            continue
                        count += 1
                        new_board[nr][nc] += board[i][j] // 5
                board[i][j] -= (board[i][j] // 5) * count
    #print_board(new_board)
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                continue
            board[i][j] += new_board[i][j]
                

def fresh(aircond, board, row, col, dirs):
    # clockwise
    nr, nc = aircond
    idx = 0
    pdust = -1
    while idx < len(dirs):
        #print("new", nr, nc, idx, len(dirs), pdust)
        dr, dc = dirs[idx][0], dirs[idx][1]
        if pdust != -1:
            nr, nc = nr - dirs[idx-1][0], nc - dirs[idx-1][1]
        #if pdust == -1:
        nr, nc = nr + dr, nc + dc
        while 0 <= nr < row and 0 <= nc < col and board[nr][nc] >= 0:
            #print("nr, nc", nr, nc)
            dust = board[nr][nc]
            if pdust == -1:
                board[nr][nc] = 0
            else:
                board[nr][nc] = pdust
            pdust = dust
            nr, nc = nr + dr, nc + dc
            
        idx += 1


def main():
    row, col, time = map(int, input().rstrip().split(" "))
    aircond = []
    board = []
    for i in range(row):
        r = list(map(int, input().rstrip().split(" ")))
        board.append(r)
        for j, c in enumerate(r):
            if c == -1:
                aircond.append((i, j))
    for _ in range(time):
        blow(board, row, col)
        #print("after blow")
        #print_board(board)
        fresh(aircond[0], board, row, col, CWISE)
        #print("after upper cond")
        #print_board(board)
        fresh(aircond[1], board, row, col, CCWISE)
        #print("after lower cond")
        #print_board(board)

    answer = 0
    for row in board:
        answer += sum(row)
    print(answer+2)

if __name__ == "__main__":
    main()