DIRECTION = {0:(0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}
ATTACK = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}


class Solution():
    """ 얼음파편공격
    1. 초기화
    자료구조: 
    - loc_num: key는 좌표, value는인덱스를 가지고 있는 dict
    - 숫자리스트: value
    2. 얼음파편 공격 및 구슬 이동
        - 인덱스를 따라가 하니씩 지움(del 사용)
        - 주의해야할것) 하나씩 사라질때마다 앞으로 당겨지므로 -i해주어야함
    3. 4개이상 연속하는것 없애기
        - 새로운 리스트 하나 생성
        - 연속되지 않으면 추가 연속된다면 넘어감
    5. 분화(구슬개수/구슬번호)
        - 리스트하나 생성으로 갯수세고 추가
    """
    def __init__(self, num_list, N):
        self.score = 0
        self.N = N
        self.loc_num = self.make_dict()
        self.marble_list = self.make_list(num_list)


    def make_dict(self):
        idx = 0
        loc = (self.N>>1, self.N>>1)
        cur_direction = 0 
        loc_dict = {loc:idx}
        for i in range(2, self.N+1):
            repeat = 2 if i < self.N else 3
            for _ in range(repeat):
                for j in range(i):
                    if j == 0:
                        continue
                    idx += 1
                    row = loc[0]+DIRECTION[cur_direction][0]
                    col = loc[1]+DIRECTION[cur_direction][1]
                    loc = (row, col)
                    loc_dict[loc] = idx
                cur_direction = (cur_direction + 1) % 4
        return loc_dict


    def padding(self):
        if len(self.marble_list) > self.N*self.N:
            self.marble_list = self.marble_list[0:self.N*self.N]
        else:
            self.marble_list.extend([0]*(self.N*self.N - len(self.marble_list)))


    def make_list(self, num_list):
        result = list()
        for row, col in self.loc_num.keys():
            result.append(num_list[row][col])
        return result


    def bomb(self, marble_list):
        is_bomb = True
        while is_bomb:
            is_bomb = False
            new_marble_list = [marble_list[0]]
            previous_marble = marble_list[1]
            repeat = 0
            for marble in marble_list[2:]:
                if previous_marble == marble:
                    repeat += 1
                else:
                    if repeat >= 3:
                        self.score += previous_marble * (repeat+1)
                        is_bomb = True
                    else:
                        for _ in range(repeat+1):
                            new_marble_list.append(previous_marble)
                    repeat = 0
                previous_marble = marble
            if repeat < 3:    
                for _ in range(repeat+1):
                    new_marble_list.append(previous_marble)
            else:
                self.score += previous_marble * (repeat+1)
            marble_list = new_marble_list
        return marble_list
        

    def start_magic(self, attack_direction, attack_distance):
        # 구슬 공격
        start = (self.N>>1, self.N>>1)
        for i in range(attack_distance):
            attack_row = start[0] + ATTACK[attack_direction][0]
            attack_col = start[1] + ATTACK[attack_direction][1]
            if 0 <= attack_row < self.N and 0 <= attack_col < self.N:
                remove_idx = self.loc_num[(attack_row), (attack_col)]
                start = (attack_row, attack_col)
                del self.marble_list[remove_idx - i]
        self.padding()
        # 4개이상 구슬 폭발
        self.marble_list = self.bomb(self.marble_list)
        # 구슬 분화
        self.padding()
        extended_marble = [self.marble_list[0]]
        previous_marble = self.marble_list[1]
        repeat = 0
        for marble in self.marble_list[2:]:
            if previous_marble == marble:
                repeat += 1
            else:
                if previous_marble > 0:
                    extended_marble.append(repeat+1)
                    extended_marble.append(previous_marble)
                repeat = 0
            previous_marble = marble
        if previous_marble > 0:
            extended_marble.append(repeat+1)
            extended_marble.append(previous_marble)
        self.marble_list = extended_marble
        self.padding()
    
def main():
    N, cmd = map(int, input().rstrip().split(" "))
    marble_list = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    solution = Solution(marble_list, N)
    for _ in range(cmd):
        direction, distance = map(int, input().rstrip().split(" "))
        solution.start_magic(direction, distance)
    print(solution.score)

if __name__ == "__main__":
    main()