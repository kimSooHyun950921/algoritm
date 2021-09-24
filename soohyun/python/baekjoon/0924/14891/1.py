from collections import deque
MOVEINFO = {0:(2, 6), 1:(2, 6), 2:(2, 6)}   

def can_move(nidx, idx, didx, wheels):
    if didx == -1:
        return wheels[idx][6] != wheels[nidx][2]
    else:
        return wheels[idx][2] != wheels[nidx][6]

def get_move_wheel(visited, moved, idx, direction, wheels):
    moved[idx] = direction
    for didx in [-1, 1]:
        nidx = idx + didx
        if 0 <= nidx < 4 and not visited[nidx] and can_move(nidx, idx, didx, wheels):
            visited[nidx] = 1
            moved = get_move_wheel(visited, moved, nidx, -direction, wheels)
    return moved

def move_wheel(moved, wheels):
    for idx, move in enumerate(moved):
        for _ in range(abs(move)):
            if move < 0:
                num = wheels[idx].popleft()
                wheels[idx].append(num)
            else:
                num = wheels[idx].pop()
                wheels[idx].appendleft(num)

def calc_score(wheels):
    score = 0
    for idx, value in enumerate(wheels):
        score += ((2**idx) * value[0])
    return score

def debug_wheel(wheels):
    for wheel in wheels:
        print("wheels", wheel)

def main():
    wheels = list()
    for _ in range(4):
        wheels.append(deque(list(map(int, list(input().rstrip())))))
    count = int(input().rstrip())

    for _ in range(count):
        visited = [0 for _ in range(4)]
        moved = [0 for _ in range(4)]
        idx, direction = map(int, input().rstrip().split(" "))
        visited[idx-1] = 1 
        moved[idx-1] = direction
        moved = get_move_wheel(visited, moved, idx-1, direction, wheels)
        move_wheel(moved, wheels)


    result = calc_score(wheels)
    print(result)

if __name__ == "__main__":
    main()