# 계획: 알고리즘 dfs
# 카메라의 위치를 받는다.
# 5번을 받으면 board에 무조건 위치를 체크해놓는다.
# 각각의 카메라가 가능한 위치는 리스트에 넣어 놓는다.
# dfs를 돌려서 카메라가 있는 위치를 바꾼다
# 한번 바꾼후 사각지대를 계산한다.
import math
CAM = [[[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]], 
       [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]], 
       [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(1, 0), (0, 1)]], 
       [[(-1, 0), (0, 1), (0, -1)], [(1, 0), (0, 1), (0, -1)], [(0, -1), (1, 0), (-1, 0)], [(0, 1), (1, 0), (-1, 0)]]]


def get_cam(camera_num, camera_loc, camera_dir, r, c, info):
    show = set()
    for i in range(len(camera_num)):
        show.add(camera_loc[i])
        crow, ccol = camera_loc[i][0], camera_loc[i][1]
        #print(crow, ccol)
        #print(camera_num[i])
        for dr, dc in CAM[camera_num[i]-1][camera_dir[i]]:
            nr, nc = crow + dr, ccol + dc
            while 0 <= nr < r and 0 <= nc < c and info[nr][nc] != 6:
                show.add((nr, nc))
                nr, nc = nr + dr, nc + dc
    return show


def check_upper(camera_dir, camera_num):
    for i in range(len(camera_dir)-1, 0, -1):
        if camera_dir[i] >= len(CAM[camera_num[i]-1]):
            camera_dir[i] = 0
            camera_dir[i-1] += 1
        else:
            break


def dfs(board, camera_num, camera_loc, camera_dir, r, c, info):
    answer = math.inf
    idx = len(camera_num) - 1
    while True:
        if camera_dir[0] >= len(CAM[camera_num[0]-1]):
            break
        #print(camera_dir, idx)
        show = get_cam(camera_num, camera_loc, camera_dir, r, c, info)
        #print_board(board-show, r, c, cam_num=camera_num,cam_loc = camera_loc)
        answer = min(answer, len(board - show))
        camera_dir[idx] += 1
        check_upper(camera_dir, camera_num)
    return answer

def print_board(board,r,c, cam_num=None, cam_loc=None):
    maps = [[0 for i in range(c)] for _ in range(r)]
    bl = list(board) 
    for cr, cc, in bl:
        maps[cr][cc] = '#'
    if cam_num:
        for i, cam in enumerate(cam_num):
            maps[cam_loc[i][0]][cam_loc[i][1]] = cam
    for row in maps:
        print(*row)

def main():
    r, c = map(int, input().rstrip().split(" "))
    board = set()
    info = [[0 for _ in range(c)] for _ in range(r)]
    camera_num = list()
    camera_loc = list()
    camera_dir = list()
    bidirection_cam = list()
    for i in range(r):
        for j, value in enumerate(list(map(int, input().rstrip().split(" ")))):
            info[i][j] = value
            if value == 0:
                board.add((i, j))
            elif 1 <= value <= 4:
                camera_num.append(value)
                camera_loc.append((i,j))
                camera_dir.append(0)
            elif value == 5:
                bidirection_cam.append((i, j))

    # 5번카메라 제외
    for cam in bidirection_cam:
        crow, ccol = cam
        board = board - {crow, ccol}
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = crow + dr, ccol + dc
            while 0 <= nr < r and 0 <= nc < c and info[nr][nc] != 6:
                #print(f"({dr}, {dc}): {nr}, {nc}")
                board = board - {(nr, nc)}
                nr, nc = nr + dr, nc + dc
                

    #print(camera_num)
    #print(camera_loc)
    #print(camera_dir)
    #print_board(board, r, c)
    # dfs 돌리기
    result = len(board)
    if camera_num:
        result = dfs(board, camera_num, camera_loc, camera_dir, r, c, info)
    print(result)


if __name__ == "__main__":
    main()
