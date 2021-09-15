import sys
import math
input = sys.stdin.readline
def solution(N, M, memory, cost):
    j_len = sum(cost)
    dp = [[0 for _ in range(j_len)] for _ in range(N+1)]
    cost_sum = 0
    for i in range(0, N):
        cost_sum += cost[i]
        for j in range(0, j_len):
            if cost[i] <= j:
                dp[i+1][j] = max(dp[i][j], dp[i][j-cost[i]] + memory[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    #for row in dp:
    #    print(*row)
    
    for idx, value in enumerate(dp[N]):
        if value >= M:
            return idx
    return -1


def main():
    N, M = map(int, input().rstrip().split(" "))
    memory = list(map(int, input().rstrip().split(" ")))
    cost = list(map(int, input().rstrip().split(" ")))
    result = solution(N, M, memory, cost)
    print(result)

if __name__ == "__main__":
    main()
