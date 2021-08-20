import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

def eat_fertilizer(tree, board):
    for loc in list(tree.keys()):
        new_tree = []
        while tree[loc]:
            year = heappop(tree[loc])
            if  board[loc[0]][loc[1]] - year >= 0:
                board[loc[0]][loc[1]] -= year
                heappush(new_tree, year+1)
            else:
                heappush(tree[loc],year)
                break
        # 죽은나무 양분변화
        change_fertilizer(loc, tree[loc], board)  
        tree[loc] = new_tree


def change_fertilizer(loc, dead_tree, board):
    for year in dead_tree:
        board[loc[0]][loc[1]] += year//2


def propagate(board_size, board, tree):
    for loc in list(tree.keys()):
        for idx in range(len(tree[loc])):
            if tree[loc][idx] % 5 == 0:
                for dr, dc in zip([-1, 0, 1, 0, -1, 1, -1, 1], [0, -1, 0, 1, 1, -1, -1, 1]):
                    nr, nc = loc[0] + dr, loc[1] + dc
                    if 0 <= nr < board_size and 0 <= nc < board_size:
                        heappush(tree[(nr, nc)], 1)


def add_fertilizer(board_size, fertilizer, board):
    for i in range(board_size):
        for j in range(board_size):
            board[i][j] += fertilizer[i][j]


def count_live_tree(tree):
    count = 0
    for _, cur_loc_tree in tree.items():
        count += len(cur_loc_tree)
    return count


def start_finance(board_size, year, fertilizer, tree, board):
    for _ in range(year):
        # 양분먹기
        #print("before")
        #print(tree) 
        #print(board)
        #print("=========")
        eat_fertilizer(tree, board)
        #print("after")
        #print(tree)
        #print(board)
        #print(dead_tree)
        #print("===========")
        # 죽은 나무의 양분변화 
        #print("change fertilizer")
        #print(dead_tree)
        #print(board)
        #print("============")
        # 나무번식
        propagate(board_size, board, tree)
        #print("propgate")
        #print(board)
        #print(tree)
        #print("=============")
        # 양분추가
        add_fertilizer(board_size, fertilizer, board)
        #print("add", board)
        #print("============")
    # 살아있는 나무 세기
    print(count_live_tree(tree))



def main():
    """
    - 변수: 
        1. N: 나무가 있는 NxN 보드 크기
        2. M: 나무의 개수
        3. K: K년 후
        4. A[r][c]: 매년마다 추가할 양분의 양
        5. tree: (x, y):나무위치  z: 나무나이
    - 초기상태: NxN에 양분 5
    - 과정
        - 나이가 어린 나무부터 자신의 나이만큼 양분을 먹음
            - 양분을 먹지 못하면 죽음
            -> dict를 돌면서 진행
            -> 양분을 먹으면 + 해줌
            -> 비료를 가진것은 나이만큼 제거해줌
            -> 못먹으면 -로 바꾸고 죽은 나무를 저장하는 배열에 넣음
        - 죽은나무가 양분으로 변함
            - 현재 나이의//2
            -> 죽은나무리스트를 돌면서 현재비료에 더해줌
        - 나무번식
            - 인접한 8개에 나이가 1인 나무 생김
            - 번식가능한 나무나이 5배수
            -> 나무리스트를 상하좌우8군대 돌면서 나무나이가 5배수라면 하나씩 추가해줌
        -  양분추가
            -A[r][c] 만큼 양분추가
            -> 비료에 더하기해줌
    -필요한 자료구조
        - 나무 dict (좌표):[나이, 나이, ...]
            - 나무를 죽이면 음수로변함
        - 죽은 나무를 저장하는 배열[[좌표]:[나이, 나이]]
        - 비료를 가지고 있는 NxN 2차원 배열
        - A를 저장하는 2차원 배열
    """
    board_size, num_of_tree, year = map(int, input().rstrip().split(" "))
    fertilizer = [list(map(int, input().rstrip().split(" "))) for _ in range(board_size)]
    tree = defaultdict(list)
    board = [[5 for _ in range(board_size)] for _ in range(board_size)]
    for _ in range(num_of_tree):
        x, y, old = map(int, input().rstrip().split(" "))
        heappush(tree[(x-1,y-1)], old)
    start_finance(board_size, year, fertilizer, tree, board)


if __name__ == "__main__":
    main()