import sys
import math
input = sys.stdin.readline
def solution(N, M, memory, cost):
    j_len = sum(cost)
    dp = [[0 for _ in range(j_len+1)] for _ in range(N+1)]
    result = math.inf
    for i in range(1, N+1):
        for j in range(0, j_len+1):
            if cost[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])
            dp[i][j] = max(dp[i-1][j], dp[i][j])
            if dp[i][j] >= M:
                result = min(result, j)

    if result != 0:
        return result
    return 0


def main():
    N, M = map(int, input().rstrip().split(" "))
    memory = list(map(int, input().rstrip().split(" ")))
    cost = list(map(int, input().rstrip().split(" ")))
    result = solution(N, M, memory, cost)
    print(result)

if __name__ == "__main__":
    main()
