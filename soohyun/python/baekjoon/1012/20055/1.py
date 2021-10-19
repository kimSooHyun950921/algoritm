from collections import deque

#시간 효율성을위해 zero_strength 변수를 하나 저장하고 있으면 좋음!

class Component:
    def __init__(self, strength, is_robot):
        self.strength = strength
        self.is_robot = is_robot
    
    def __str__(self):
        return f'({self.strength}, {self.is_robot})'

def get_strength(belt):
    zero_strength = 0
    for comp in belt:
        if comp.strength == 0:
            zero_strength += 1
    return zero_strength

def down_robot(upper):
    if upper[-1].is_robot == True:
        upper[-1].is_robot = False

def rotation_belt(upper, lower):
    comp = upper.pop()
    lower.append(comp)
    comp = lower.popleft()
    upper.appendleft(comp)
    down_robot(upper)

def get_next_belt(i, upper, lower, N):
    if i == N-1:
        return lower[N-1]
    return upper[i+1]

def move_robot(upper, lower, N):
    for i in range(N-1, -1, -1):
        next_robot = get_next_belt(i, upper, lower, N)
        if upper[i].is_robot and not next_robot.is_robot:
            if next_robot.strength > 0:
                upper[i].is_robot = False
                next_robot.is_robot = True
                next_robot.strength -= 1
    down_robot(upper)

def load_robot(upper):
    if not upper[0].is_robot and upper[0].strength > 0:
        upper[0].is_robot = True
        upper[0].strength -= 1

def solution(N, upper, lower, K):
    level = 1
    while get_strength(upper) + get_strength(lower) < K:
        rotation_belt(upper, lower)
        move_robot(upper, lower, N)
        load_robot(upper)
        level += 1
    return level-1

def main():
    N, K = map(int, input().rstrip().split())
    upper = deque([])
    lower = deque([])
    for idx, value in enumerate(map(int, input().rstrip().split())):
        if idx < N:
            upper.append(Component(value, False))
        else:
            lower.appendleft(Component(value, False))

    result = solution(N, upper, lower, K)
    print(result)
        

if __name__ == "__main__":
    main()