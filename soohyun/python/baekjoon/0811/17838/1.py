from collections import deque
import sys
input = sys.stdin.readline

DIRECTION = {1: (0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
class Horse():
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction

    def __str__(self):
        return f'[loc: ({self.row}, {self.col}), d:{self.direction}]'


def change_direction(num):
    if num == 1:
        return 2
    elif num == 2:
        return 1
    elif num == 3:
        return 4
    else:
        return 3

def get_horse_list(horse_board, horse, target):
    horse_list = []
    while True:
        current_horse = horse_board[horse.row][horse.col].pop()
        horse_list.append(current_horse)
        if current_horse == target:
            break
    return horse_list

def move(nr, nc, board, horse_list, horse_board, horse_loc):
    for j in range(len(horse_list)):
        if board[nr][nc] == 1:
            stacked_horse = horse_list[j]
            horse_board[nr][nc].append(stacked_horse)
        else:
            stacked_horse = horse_list[len(horse_list) - j - 1]
            horse_board[nr][nc].append(stacked_horse)
        horse_loc[stacked_horse].row = nr
        horse_loc[stacked_horse].col = nc

def is_over_four(K, horse_loc, horse_board):
    for i in range(K):
        row, col = horse_loc[i].row, horse_loc[i].col 
        if len(horse_board[row][col]) >= 4:
            return True
    return False

def print_board(board):
    print("=====")
    for row in board:
        print(*row)
    print("=====")

def print_horse(horse_loc):
    for i in horse_loc:
        print(i, end=", ")
    print("")

def solution(N, K, horse_board, board, horse_loc):
    turn = 1
    while turn <= 1000:
        #print("TURN", turn)
        # 0번 말부터 K-1 번말까지 움직임
        for i in range(K):
            # i 번 말의 다음 위치로 이동
            nr = horse_loc[i].row + DIRECTION[horse_loc[i].direction][0]
            nc = horse_loc[i].col + DIRECTION[horse_loc[i].direction][1]  
            #print("current horse:", i, horse_loc[i], (nr, nc))
              
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] < 2:
                horse_list = get_horse_list(horse_board, horse_loc[i], i)
                move(nr, nc, board, horse_list, horse_board, horse_loc)
                if  len(horse_board[nr][nc]) >= 4:
                        break  
            else:
                horse_loc[i].direction = change_direction(horse_loc[i].direction)
                nr = horse_loc[i].row + DIRECTION[horse_loc[i].direction][0]
                nc = horse_loc[i].col + DIRECTION[horse_loc[i].direction][1]
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] < 2:
                    horse_list = get_horse_list(horse_board,horse_loc[i], i)
                    move(nr, nc, board, horse_list, horse_board, horse_loc)     
                    if  len(horse_board[nr][nc]) >= 4:
                        break    
            #print_board(horse_board)
            #print_horse(horse_loc)
            

        if is_over_four(K, horse_loc, horse_board):
            break
        turn += 1
    turn = turn if turn <= 1000 else -1
    return turn


def main():
    N, K = map(int, input().rstrip().split(" "))
    horse = [[deque() for _ in range(N)] for _ in range(N)]
    board = [ list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    horse_loc = list()
    for i in range(K):
        r, c, d = map(int, input().rstrip().split(" "))
        horse_loc.append(Horse(r-1, c-1, d))
        horse[r-1][c-1].appendleft(i)
    #print_board(horse)
    #print_horse(horse_loc)

    print(solution(N, K, horse, board, horse_loc))

if __name__ == "__main__":
    main()