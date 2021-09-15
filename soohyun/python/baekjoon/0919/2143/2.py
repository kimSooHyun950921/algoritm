import sys
import math
input = sys.stdin.readline
def solution(N, M, app):
    def dfs(debug, sum_memory, sum_weight,visited):
        result = math.inf
        if sum_memory >= M:
            return sum_weight
        else:
            for i in range(N):
                if not visited[i]:
                    if len(debug) == 0 or (len(debug) > 0 and debug[-1] < i):
                        visited[i] = True
                        sum_memory += app[0][i]
                        sum_weight += app[1][i]
                        debug.append(i)
                        result = min(dfs(debug, sum_memory, sum_weight, visited), result)
                        debug.pop()
                        visited[i] = False
                        sum_memory -= app[0][i]
                        sum_weight -= app[1][i]
            return result
    return dfs([], 0, 0, [False for _ in range(N)])
                


def main():
    N, M = map(int, input().rstrip().split(" "))
    app = []
    for _ in range(2):
        app.append(list(map(int, input().rstrip().split(" "))))
    print(app)
    result = solution(N, M, app)
    print(result)

if __name__ == "__main__":
    main()
