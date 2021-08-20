import math
def get_odd_leddar(board):
    odd_leddar = []
    for i, row in enumerate(board):
        sum_row = sum(row)
        if sum_row == 0 or sum_row % 2 != 0:
            odd_leddar.append(i)
    return odd_leddar

def leddaring(board, row, col):
    for i in range(row):
        current_position = i
        for j in range(col):
            if board[current_position][j] == 1:
                current_position = current_position + 1
            elif current_position > 0 and board[current_position-1][j] == 1:
                current_position = current_position - 1
        if i != current_position:
            return False
    return True

def init_game(board, row, col, count):
    def put_leddar(row_start, cur_count):
        min_leddar = 4
        if leddaring(board, row, col):   
            min_leddar = min(min_leddar, cur_count)
            return min_leddar
        if cur_count >= 3:
            return min_leddar
        for r in range(row_start, row):
            for c in range(col):
                if board[r][c] == 0:
                    if (r > 0 and board[r-1][c] == 1) or board[r+1][c] == 1:
                        continue
                    board[r][c] = 1
                    min_leddar = min(min_leddar, put_leddar(row_start+1, cur_count+1))
                    board[r][c] = 0
        return min_leddar
    return put_leddar


def main():
    row, col, count = map(int, input().rstrip().split(" "))
    board = [[0 for _ in range(count)] for _ in range(row)]
    for _ in range(col):
        c, r = map(int, input().rstrip().split(" "))
        board[r-1][c-1] = 1
    odd_leddar = get_odd_leddar(board)
    put_leddar = init_game(board, row-1, count, col, odd_leddar)
    answer = put_leddar(0, 0)
    #print(answer)
    if answer == math.inf or answer > 3:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    main()