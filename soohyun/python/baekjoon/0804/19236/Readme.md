# 문제의 핵심
- dfs

# 복기할것
- dfs가 돌아오면 어떤 상태인지 확인해야함
  - 재귀 안으로 들어갔을때 그래프가 어떤 상태로 변경되었고, 다시 원복하려면 어떻게 해야하는지 고려해야함 (90번째줄)
- 주소 복사는 값을 그대로 가지고 있음 따라서 **새로 객체를 생성해서 거기에 넣어주던가, deepcopy해야함**  (70번째줄)
- 물고기가 있을때와 없을때 고려할것
- 꼼꼼하게 미리 계획할것
- 재귀 상태변화를 공부할 수 있어서 좋았음