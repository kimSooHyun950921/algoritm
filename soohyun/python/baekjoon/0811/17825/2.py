NUM_HORSE = 4
class Horse:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f'[({self.row}, {self.col}):{self.value}]'

class Yutnole:
    def __init__(self, board, dice):
        self.board = board
        self.dice = dice

    def is_arrive(self, row, col):
        if len(self.board[row])-1 <= col:
            return True
        return False

    def is_change_direction(self, cur_row, cur_col):
        cdirection = {(0, 15), (3, 15)}
        if self.board[cur_row][cur_col] == 10:
            return True 
        if self.board[cur_row][cur_col] == 20:
            return True
        if self.board[cur_row][cur_col] == 30 and (cur_row, cur_col) in cdirection:
            return True
        return False
            
    def calc_nextloc(self, cur_row, cur_col):
        #도착하고 넘어가는 경우
        if self.is_arrive(cur_row, cur_col):
            return cur_row, len(self.board[cur_row])-1
        # 윷놀이 위치를 꺾어야하는경우
        elif self.is_change_direction(cur_row, cur_col):
                return self.board[cur_row][cur_col] // 10, cur_col
        # 그밖의 경우
        else:
            return cur_row, cur_col

    def is_horse_exist(self, row, col, horse_list):
        if not self.is_arrive(row, col):
            for horse in horse_list:
                if horse.row == row and horse.col == col:
                    return True
                if horse.row == 0:
                    if row == 1:
                        if col <= 5 and horse.col == col:
                            return True
                    if row == 2:
                        if col <= 10 and horse.col == col:
                            return True
                    if row == 3:
                        if col <= 15 and horse.col == col:
                            return True
                if row == 0:
                    if horse.row == 1:
                        if horse.col <= 5 and horse.col == col:
                            return True
                    if horse.row == 2:
                        if horse.col <= 10 and horse.col == col:
                            return True
                    if horse.row == 3:
                        if horse.col <= 15 and horse.col == col:
                            return True
                if horse.row == 1:
                    if row == 2:
                        if horse.col >= 9 and col >= 13:
                            if horse.col - 9 ==  col - 13:
                                return True
                    if row == 3:
                        if horse.col >= 9 and col >= 19:
                            if horse.col - 9 == col - 19:
                                return True
                if row == 1:
                    if horse.row == 2:
                        if col >= 9 and horse.col >= 13:
                            if col - 9 == horse.col - 13:
                                return True
                    if horse.row == 3:
                        if col >= 9 and horse.col >= 19:
                            if col - 9 == horse.col - 19:
                                return True
                if horse.row == 2:
                    if row == 3:
                        if horse.col >= 13 and col >= 19:
                            if horse.col - 13 == col - 19:
                                return True
                if row == 2:
                    if horse.row == 3:
                        if col >= 13 and horse.col >= 19:
                            if col - 13 == horse.col - 19:
                                return True
                if self.board[row][col] == 40 and self.board[horse.row][horse.col] == 40:
                    return True

        return False

    def print_horse_list(self, horse_list):
        for horse in horse_list:
            print(horse, end=", ")
        print("")

    def start_game(self, turn, horse_list):
        if turn >= 10:
            return 0
        max_value = 0
        dice_num = self.dice[turn]
        # 기존의 말들을 이동한다
        for horse_idx in range(len(horse_list)):
            cur_row, cur_col = horse_list[horse_idx].row, horse_list[horse_idx].col
            cur_value = horse_list[horse_idx].value   
            if not self.is_arrive(cur_row, cur_col):
                n_row, n_col = self.calc_nextloc(cur_row, cur_col + dice_num)
                if not self.is_horse_exist(n_row, n_col, horse_list):
                    # 위치 및 값 변경
                    horse_list[horse_idx].row, horse_list[horse_idx].col = n_row, n_col
                    horse_list[horse_idx].value = self.board[n_row][n_col]

                    cur_loop_value = self.start_game(turn+1, horse_list) + horse_list[horse_idx].value
                    max_value = max(max_value, cur_loop_value)

                    # 위치 및 값 원복 
                    horse_list[horse_idx].row, horse_list[horse_idx].col = cur_row, cur_col
                    horse_list[horse_idx].value = cur_value
         
        # 새롭게 놓는다.
        n_row, n_col = self.calc_nextloc(0, 0+dice_num)
        value = self.board[n_row][n_col]
        if not self.is_horse_exist(n_row, n_col, horse_list) and len(horse_list) < 4:
            horse_list.append(Horse(n_row, n_col, value))
            max_value = max(self.start_game(turn+1, horse_list) +  horse_list[-1].value, max_value)
            horse_list.pop()  

        return max_value
                      


def make_board():
    board = [list(), list(), list(), list()]
    for i in range(len(board)):
        if i == 0:
            board[i] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
        else:
            board[i].extend([value for value in board[0][0:5*i+1]])
    board[1].extend([13, 16, 19, 25, 30, 35, 40, 0])
    board[2].extend([22, 24, 25, 30, 35, 40, 0])
    board[3].extend([28, 27, 26, 25, 30, 35, 40, 0])
    return board

def main():
    board = make_board()
    for row in board:
        print(*row)
    #dice = list(map(int, input().rstrip().split(" ")))
    #game = Yutnole(board, dice)
    #print(game.start_game(0, []))

if __name__ == "__main__":
    main()