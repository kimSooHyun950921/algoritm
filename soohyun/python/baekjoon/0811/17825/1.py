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
        self.horse_list = [Horse(0, 0, self.board[0][0]) for _ in range(4)]

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

    def is_horse_exist(self, row, col):
        if not self.is_arrive(row, col):
            for horse in self.horse_list:
                if horse.row == row and horse.col == col:
                    return True
        return False

    def print_horse_list(self):
        for horse in self.horse_list:
            print(horse, end=", ")
        print("")

    def start_game(self, turn):
        if turn == len(self.dice):
            return 0
        max_value = 0
        dice_num = self.dice[turn]
        for horse_idx in range(len(self.horse_list)):
            # dice 만큼 이동함
            cur_row, cur_col = self.horse_list[horse_idx].row, self.horse_list[horse_idx].col
            cur_value = self.horse_list[horse_idx].value
            if not self.is_arrive(cur_row, cur_col):
                n_row, n_col = self.calc_nextloc(cur_row, cur_col + dice_num)
                if not self.is_horse_exist(n_row, n_col):
                    # 위치 및 값 변경
                    self.horse_list[horse_idx].row, self.horse_list[horse_idx].col = n_row, n_col
                    self.horse_list[horse_idx].value = self.board[n_row][n_col]
                    #print(horse_idx, end=" ")

                    #self.print_horse_list()
                    cur_loop_value = self.start_game(turn+1) + self.horse_list[horse_idx].value
                    max_value = max(max_value, cur_loop_value)

                    # 위치 및 값 원복
                    self.horse_list[horse_idx].row, self.horse_list[horse_idx].col = cur_row, cur_col
                    self.horse_list[horse_idx].value = cur_value
        # 4개말중 가장 큰 값을 반환
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
    board[3].extend([32, 34, 36, 38, 40, 0])
    return board

def main():
    board = make_board()
    dice = list(map(int, input().rstrip().split(" ")))
    game = Yutnole(board, dice)
    print(game.start_game(0))


if __name__ == "__main__":
    main()