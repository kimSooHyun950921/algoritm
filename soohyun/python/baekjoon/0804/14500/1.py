TETROMINO = {1:{'row':3, 'col':2, 'value':[(0,0),(1,0),(2,0),(2,1)]},
             2:{'row':3, 'col':2, 'value':[(0,0),(1,0),(1,1),(2,1)]},
             3:{'row':2, 'col':3, 'value':[(0,0),(0,1),(0,2),(1,1)]},
             4:{'row':3, 'col':2, 'value':[(0,1),(1,1),(2,1),(2,0)]},
             5:{'row':3, 'col':2, 'value':[(0,1),(1,1),(1,0),(2,0)]},
             6:{'row':4, 'col':0, 'value':[(0,0),(1,0),(2,0),(3,0)]},
             7:{'row':2, 'col':2, 'value':[(0,0),(1,0),(0,1),(1,1)]}}


def sum_value(N, M, board, i, j, key):
    sum_tet = 0 
    new_list = []
    for dr, dc in TETROMINO[key]['value']:
        r, c = i + dr, j + dc
        new_list.append((r, c))
        if 0 <= r < N and 0 <= c < M:
            sum_tet += board[r][c]
        else:
            #print(key, new_list)
            return 0
    #print(key, new_list)
    return sum_tet


def rotation(key):
    new_value = []
    row, col = TETROMINO[key]['row'], TETROMINO[key]['col']
    for dr, dc in TETROMINO[key]['value']:
        r, c = row - dr - 1, dc
        r, c = c, r
        new_value.append((r, c))
    TETROMINO[key]['row'], TETROMINO[key]['col'] = col, row
    TETROMINO[key]['value'] = new_value

        
def flip(key):
    new_value = []
    for dr, dc in TETROMINO[key]['value']:
        new_value.append((dr, -dc))
    TETROMINO[key]['value'] = new_value


def solution(N, M, board):
    max_value = 0
    for i in range(N):
        for j in range(M):
            for key in TETROMINO.keys():
                sum_tet = 0
                for _ in range(4):
                    sum_tet = sum_value(N, M, board, i, j, key)
                    max_value = max(sum_tet, max_value)
                    if key == 7:
                        break
                    rotation(key)
                    #print(key, TETROMINO[key]['value'])
                #if key == 2 or key == 1:
                #    flip(key)
                    #print("flip", key, TETROMINO[key]['value'])
                #    for _ in range(4):
                #        sum_tet = sum_value(N, M, board, i, j, key)
                #        max_value = max(sum_tet, max_value)
                #        rotation(key)
                        #print("flip rotation", key, TETROMINO[key]['value'])

                #    flip(key)
                    #print("flip", key, TETROMINO[key]['value'])

    return max_value


def main():
    N, M = map(int, input().rstrip().split(" "))
    board = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    print(solution(N, M, board))
    

if __name__ == "__main__":
    main()
