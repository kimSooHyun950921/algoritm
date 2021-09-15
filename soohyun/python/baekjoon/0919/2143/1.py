import sys
import math
input = sys.stdin.readline
def solution(N, M, app):
    def dfs(debug, sum_memory, sum_weight,visited):
        print(debug, sum_memory, sum_weight,  visited)
        result = math.inf
        if sum_memory >= M:
            return sum_weight
        else:
            #for idx in range(start, N):
            #    min_result = math.inf
                #print(idx)
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
                #visited = [False for _ in range(N)]
                #debug = []
                #sum_memory = 0
                #sum_weight = 0
                #result = min(min_result, result)
            return result
    return dfs([], 0, 0, [False for _ in range(N))
                


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
