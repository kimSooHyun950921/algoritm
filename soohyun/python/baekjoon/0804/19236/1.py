# 복사 위치를 잘 알아야함
import sys
sys.setrecursionlimit(1000000000)
rotation = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
WIDTH = 4
def move_fish(board, shark, fish_num):
    for i in range(1, WIDTH*WIDTH+1):
        if fish_num.get(i) is not None:
            row, col = fish_num[i]
            current_d = board[row][col][1]
            
            for i in range(len(rotation)):
                direction = rotation[current_d]
                dr, dc = direction[0], direction[1]
                nr, nc = row + dr, col + dc
                if 0 <= nr < WIDTH and 0 <= nc < WIDTH:
                    if (nr, nc) != shark:
                        board[row][col][1] = current_d
                        # 0일때나 0이 아닐때나 바꾸어야함
                        if board[nr][nc][0] == 0: #여기서 틀렸음
                            board[nr][nc][0], board[row][col][0] = \
                                board[row][col][0], board[nr][nc][0]
                            board[nr][nc][1], board[row][col][1] = \
                                board[row][col][1], board[nr][nc][1]      
                            fish_num[board[nr][nc][0]] = (nr, nc)  # 여기서 틀렸음
                        else:
                            board[nr][nc][0], board[row][col][0] = \
                                board[row][col][0], board[nr][nc][0]
                            board[nr][nc][1], board[row][col][1] = \
                                board[row][col][1], board[nr][nc][1]      
                            fish_num[board[nr][nc][0]] = (nr, nc)   
                            fish_num[board[row][col][0]] = (row, col)    
                        break
                current_d = (current_d + 1) % len(rotation)

def can_eat(board, shark):
    result = []
    row, col = shark[0], shark[1]
    dr, dc = rotation[board[shark[0]][shark[1]][1]]
    for _ in range(1, 5):
        nr, nc = row+ dr, col + dc
        if 0 <= nr < WIDTH and 0 <= nc < WIDTH and board[nr][nc][0] > 0:
           result.append((nr, nc))
        row, col = nr, nc
    return result

def print_board(board):
    print("======start======")
    for i in board:
        print(*i)
    print("======send======")

def solution(board, fish_num, shark):
    # 현재 위치물고기를 상어가 먹음
    eat = board[shark[0]][shark[1]][0]
    max_eat = eat
    fish_num.pop(board[shark[0]][shark[1]][0])  
    board[shark[0]][shark[1]][0] = 0

    # 물고기를 움직임
    move_fish(board, shark, fish_num) 
    # 움직인 물고기 저장 ==> 다시 돌아오기 위해서 
    copy_board = [[[board[i][j][0], board[i][j][1]] for j in range(WIDTH)] for i in range(WIDTH)]
    copy_fish_num = dict()
    for key in fish_num.keys():
        copy_fish_num[key] = fish_num[key]
    # 상어움직임
    can_eat_list = can_eat(board, shark)
    for nr, nc in can_eat_list:
        max_eat = max(max_eat, solution(board, fish_num, (nr, nc)) + eat)
        # 복사해둔 board 다시 복사 (여기서 틀렸음)
        board = [[[copy_board[i][j][0], copy_board[i][j][1]] for j in range(WIDTH)] for i in range(WIDTH)]
        fish_num = dict()
        for key in copy_fish_num.keys():
            fish_num[key] = copy_fish_num[key]
    # 먹은것 원상복귀
    board[shark[0]][shark[1]][0] = eat   
    fish_num[board[shark[0]][shark[1]][0]] = shark        
    return max_eat
    


def main():
    board = [[[0, 0] for _ in range(4)] for _ in range(4)]
    fish_num = dict()
    for i in range(4):
        for idx, value in enumerate( list(map(int, input().rstrip().split(" ")))):
            if idx % 2 == 0:
                board[i][idx//2][0] = value
                fish_num[value] = (i, idx//2)
            else:
                board[i][idx//2][1] = value - 1
    print(solution(board, fish_num, (0, 0)))


if __name__ == "__main__":
    main()