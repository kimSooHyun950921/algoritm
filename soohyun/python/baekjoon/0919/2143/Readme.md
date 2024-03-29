# 문제의 핵심
- dp
- (시간초과) dfs

# 자료구조
- memory, cost: 1차원 배열
- dp: 행 0부터 N까지, 열 0부터 sum(cost)까지 담을 수 있는 2차원 배열

# 풀이방법
```
    정리할 수 있는 최대 메모리가 M 이상인것중에 최소 cost를 반환
```
- dp 정리
    - dp 공식(점화식)
        - cost j보다 현재 앱의 cost가 작거나 같은경우:
            - dp[i][j] = max(현재 앱을 정리하지 않을경우의 메모리, 현재 앱을 정리할경우의 메모리)
        - cost j보다 현재 앱의 cost가 큰경우
            - dp[i][j-1]에서 가져옴
- dp의 원소의 의미
    - dp의 행(i)의 의미: memory 순서대로 i개까지 메모리를 정리했을때 최대로 정리할 수 있는 메모리
    - dp의 열(j)의 의미: 메모리정리할때 드는 cost수
    - dp의 각원소(행,열(i, j))의 의미: cost j를 만족하면서 memory 순서대로 i개까지 정리 했을때 정리할 수 있는 최대 메모리 
- 문제 예시
    - 주어진 정보
        |        | 0  | 1  | 2  | 3  | 4  |
        |--------|----|----|----|----|----|
        | cost   | 3  | 0  | 3  | 5  | 4  |
        | memory | 30 | 10 | 20 | 35 | 40 |
    - dp 결과
    
        | cost | memory/cost |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 |  10 |  11 |  12 |  13 |  14 |  15 |
        |:----:|:-----------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|:---:|:---:|:---:|
        |   3  |      30     |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |  0 |   0 |   0 |   0 |   0 |   0 |   0 |
        |   0  |      10     |  0 |  0 |  0 | 30 | 30 | 30 | 30 | 30 | 30 | 30 |  30 |  30 |  30 |  30 |  30 |  30 |
        |   3  |      20     | 10 | 10 | 10 | 40 | 40 | 40 | 60 | 60 | 60 | 60 |  60 |  60 |  60 |  60 |  60 |  60 |
        |   5  |      35     | 10 | 10 | 10 | 40 | 40 | 45 | 60 | 60 | 75 | 75 |  75 |  95 |  95 |  95 |  95 |  95 |
        |   4  |      40     | 10 | 10 | 10 | 40 | 50 | 50 | 60 | 80 | 80 | 85 | 100 | 100 | 115 | 115 | 115 | 135 |



# knapsack 문제
- knapsack문제의 점화식
    ```
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]) if ci > c \
             = dp[i][j-1] else
    ```
    - 최대 넣을 수 있는 무게(weight) j보다 현재 물건의 (weight)가 작거나 같은경우:
        - 새롭게 넣을 수 있음
        - dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + value[i])
        - max(i-1개의 보석들을 가지고 구한 전 단계의 최적값, i번째 보석을 위해 i번째 보석만큼의 무게를 비웠을 때의 최적값에 i번째 보석의 가격을 더한 값 )
    - 그렇지 않은경우
        - 새롭게 넣을 수 없으므로 i번째 보석을 뺀 i-1개의 보석들을 가지고 구한 전 단계의 최적값을 그대로 가져온다
        - dp[i][j-1]에서 가져옴

# code snippet 
```python
dp = [[0 for _ in range(j_len+1)] for _ in range(N+1)]
j_len = sum(cost)
for i in range(1, N+1):# 1부터 시작해야함
        for j in range(0, j_len+1): # 15까지 해야하므로  j_len +1 로 끝내야함
            if cost[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][j] >= M:
                result = min(result, j)
```

# 복기
- index 문제 
    - 언제시작하고, 언제끝나는지 확인할것 이것때문에 틀렸음
        - 0부터 N까지 모두 돌아야하니 코드는 **0~N+1**로 작성
        - 0부터 전체 cost합 까지 돌아야하니 열의 코드는 **0~j_len+1**로 작성