import sys
input = sys.stdin.readline
BLOCK = {1: [(0, 0)], 2: [(0, 0), (0, 1)], 3:[(0, 0), (1, 0)]}
ISECTION = [(0, 4, 3, 5), (4, 0, 5, 3)]

def is_block(row, col, board):
    if row == 0:
        for i in range(0, 4):
            if board[i][col] == 1:
                return False
        return True
    elif col == 0:
        for i in range(0, 4):
            if board[row][i] == 1:
                return False
        return True
    return False


def print_board(str, board):
    print("===",str,"===")
    for row in board:
        print(*row)
    print("=============")
 
def main():
    board = [[0]*10 for _ in range(10)]
    N = int(input())
    score = 0
    for _ in range(N):
        t, r, c = map(int, input().rstrip().split(" "))
        blocks = list()
        for loc in BLOCK[t]:
            blocks.append((r+loc[0], c+loc[1]))

        # 블록 이동
        # 우측이동
        new_block = list()
        for block in blocks:
            row, col = block[0], block[1] + 1
            while col < 10 and row < 10 and board[row][col] == 0 :
                col += 1
            new_block.append([row, col-1])
        if t == 3:
            new_block[0][1] = min(new_block[0][1], new_block[1][1])
            new_block[1][1] = min(new_block[0][1], new_block[1][1])
        if t == 2:
            new_block[0][1] = new_block[1][1] - 1
        
        for block in new_block:
            board[block[0]][block[1]] = 1

        # 하측 이동
        new_block = list()
        for block in blocks:
            row, col = block[0] + 1, block[1]
            while col < 10 and row < 10 and board[row][col] == 0:
                row += 1
            new_block.append([row-1, col])
        if t == 2:
            new_block[0][0] = min(new_block[0][0], new_block[1][0])
            new_block[1][0] = min(new_block[0][0], new_block[1][0])
        if t == 3:
            new_block[0][0] = new_block[1][0] - 1
        
        for block in new_block:
            board[block[0]][block[1]] = 1
        

        # 행이 채워지는지 확인
        blue_col = []
        for bcol in range(6, 10):
            is_full = True
            for brow in range(0, 4):
                if board[brow][bcol] == 0:
                    is_full = False
                    break
            if is_full:
                score += 1
                blue_col.append(bcol)
                for brow in range(0, 4):
                    board[brow][bcol] = 0

        # 열이 채워지는지 확인
        green_row = []
        for brow in range(6, 10):
            is_full = True
            for bcol in range(0, 4):
                if board[brow][bcol] == 0:
                    is_full = False
                    break
            if is_full:
                score += 1
                green_row.append(brow)
                for bcol in range(0, 4):
                    board[brow][bcol] = 0

        # 없앤후 블록이동
        # 파란색 이동(행 이동)
        if blue_col:
            rcol = blue_col.pop()
            for mcol in range(rcol-1, 3, -1):
                block_col = mcol + 1
                while block_col < 10 and is_block(0, block_col, board):
                    block_col += 1
                for mrow in range(0, 4):
                    board[mrow][block_col-1] = board[mrow][mcol]  
                    board[mrow][mcol] = 0
        # 초록색 이동(열이동)
        if green_row:
            rrow = green_row.pop()
            for mrow in range(rrow-1, 3, -1):
                block_row = mrow + 1
                while block_row < 10 and is_block(block_row, 0, board):
                    block_row += 1
                for mcol in range(0, 4):
                    board[block_row - 1][mcol] = board[mrow][mcol]  
                    board[mrow][mcol] = 0

        # 임계영역 마주치는지 확인
        # 파란색 영역
        count = 0
        for section_col in range(4, 6):
            for section_row in range(0, 4):
                if board[section_row][section_col] == 1:
                    count += 1
                    break

        for i in range(count):
            col = 9 - i
            for row in range(0, 4):
                board[row][col] = 0

        if count > 0:
            for mcol in range(8, 3, -1):
                block_col = mcol + 1
                while block_col < 10 and is_block(0, block_col, board):
                    block_col += 1
                for mrow in range(0, 4):
                    board[mrow][block_col-1] = board[mrow][mcol]  
                    board[mrow][mcol] = 0

        # 초록색 영역
        count = 0
        for section_row in range(4, 6):
            for section_col in range(0, 4):
                if board[section_row][section_col] == 1:
                    count += 1
                    break

        for i in range(count):
            row = 9 - i
            for col in range(0, 4):
                board[row][col] = 0

        if count > 0:
            for mrow in range(8, 3, -1):
                block_row = mrow + 1
                while block_row < 10 and is_block(block_row, 0, board):
                    block_row += 1
                for mcol in range(0, 4):
                    board[block_row - 1][mcol] = board[mrow][mcol]   
                    board[mrow][mcol] = 0
    # 남은 타일 세기
    # 파란색
    blue = 0
    for col in range(6, 10):
        for row in range(0, 4):
            if board[row][col] == 1:
                blue += 1

    green = 0
    for row in range(6, 10):
        for col in range(0, 4):
            if board[row][col] == 1:
                green += 1
    
    print(score)
    print(blue + green)   




if __name__ == "__main__":
    main()