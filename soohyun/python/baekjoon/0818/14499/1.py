def game(row, col, cmds, board):
    dice = [0, 1, 2, 3, 4, 5, 6]
    number = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    def change_dice(num):
        if num == 1:
            num_1 = dice[1]
            num_3 = dice[3]
            dice[1] = dice[4]
            dice[3] = num_1
            dice[4] = dice[6]
            dice[6] = num_3
        elif num == 2:
            num_1 = dice[1]
            num_4 = dice[4]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[4] = num_1
            dice[6] = num_4
        elif num == 3:
            num_1 = dice[1]
            num_5 = dice[5]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[5] = num_1
            dice[6] = num_5
        elif num == 4:
            num_1 = dice[1]
            num_2 = dice[2]
            dice[1] = dice[5]
            dice[2] = num_1
            dice[5] = dice[6]
            dice[6] = num_2

    def play(start_r, start_c):
        cur_head = 1
        r, c = start_r, start_c
        cur_bottom = 7 - cur_head
        for cmd in cmds:
            dr, dc = direction[cmd-1]
            nr, nc = r + dr, c+ dc
            if 0 <= nr < row and 0 <= nc < col:
                change_dice(cmd)
                cur_head = dice[1]
                cur_bottom = 7 - cur_head
                if board[nr][nc] == 0:
                    board[nr][nc] = number[cur_bottom]
                else:
                    number[cur_bottom] = board[nr][nc]
                    board[nr][nc] = 0
                r, c = nr, nc
                yield number[cur_head]

    return play


def main():
    row, col, start_r, start_c, _ = map(int, input().rstrip().split(" "))
    board = [list(map(int, input().rstrip().split(" "))) for _ in range(row)]
    cmds = list(map(int, input().rstrip().split(" ")))
    play = game(row, col, cmds, board)
    for value in play(start_r, start_c):
        print(value)

if __name__ == "__main__":
    main()