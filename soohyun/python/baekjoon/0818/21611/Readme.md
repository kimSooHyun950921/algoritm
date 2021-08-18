# 문제의 핵심
- 시뮬레이션
# 자료구조
- loc_num: key는 좌표, value는인덱스를 가지고 있는 dict
- marble_list: value
# 알고리즘
1. 얼음파편 공격 및 구슬 이동
    - 인덱스를 따라가 하니씩 지움(del 사용)
    - 주의해야할것) 하나씩 사라질때마다 앞으로 당겨지므로 -i해주어야함
2. 4개이상 연속하는것 없애기
    - 새로운 리스트 하나 생성
    - 연속되지 않으면 추가 연속된다면 넘어감
3. 분화(구슬개수/구슬번호)
    - 리스트하나 생성으로 갯수세고 추가
# Code Snippet
- blizzard 위치에 맞는 인덱스를 잡아주는 코드
    ```python
            idx = 0
            loc = (self.N>>1, self.N>>1)
            cur_direction = 0 
            loc_dict = {loc:idx}
            # 2부터 N까지 반복
            for i in range(2, self.N+1):
                # 두번씩 반복
                repeat = 2 if i < self.N else 3
                for _ in range(repeat):
                    # i번씩 숫자를 만들어줘야함
                    for j in range(i):
                        # 처음은 무시(반복되므로)
                        if j == 0:
                            continue
                        #처음이 아니면 방향을 바꿔서 인덱스를 넣아줌
                        idx += 1
                        row = loc[0]+DIRECTION[cur_direction][0]
                        col = loc[1]+DIRECTION[cur_direction][1]
                        loc = (row, col)
                        loc_dict[loc] = idx
                    cur_direction = (cur_direction + 1) % 4
            return loc_dict
    ```
- 구슬 공격
    ```python
    start = (self.N>>1, self.N>>1)
    for i in range(attack_distance):
        attack_row = start[0] + ATTACK[attack_direction][0]
        attack_col = start[1] + ATTACK[attack_direction][1]
        if 0 <= attack_row < self.N and 0 <= attack_col < self.N:
            remove_idx = self.loc_num[(attack_row), (attack_col)]
            start = (attack_row, attack_col)
            del self.marble_list[remove_idx - i]
    ```

```python
def bomb(self, marble_list):
    is_bomb = True
    # 구슬이 폭파될때까지 반복
    while is_bomb:
        is_bomb = False
        new_marble_list = [marble_list[0]]
        previous_marble = marble_list[1]
        repeat = 0
        # marble2부터 시작
        for marble in marble_list[2:]:
            # 이전것과동일하다면
            if previous_marble == marble:
                # 반복을 하나 늘려줌
                repeat += 1
            else:
                # 동일하지 않다면
                # 4개 (처음 숫자는 안세므로 3)이상이면 
                if repeat >= 3:
                    # 폭발해야함
                    self.score += previous_marble * (repeat+1)
                    is_bomb = True
                else:
                    # 아니면 이전것을 합쳐줌
                    for _ in range(repeat+1):
                        new_marble_list.append(previous_marble)
                repeat = 0
            # 이전 marble을 갱신
            previous_marble = marble
        # previous만 넣어줬으므로 현재 marble 도 넣어줘야함
        if repeat < 3:    
            for _ in range(repeat+1):
                new_marble_list.append(previous_marble)
        else:
            self.score += previous_marble * (repeat+1)
        marble_list = new_marble_list
    return marble_list
```

# 복기할것
- 한번 더 푸니까 좀더 쉽게 풀었음
- new_marble_list의 previous index가 기존의 marble_list의 1부터 시작하는데 모두 폭발해서 0번째 원소밖에 없는경우를 생각해주어야함 
    - padding을 통해 해결