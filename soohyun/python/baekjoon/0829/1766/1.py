from heapq import heappush, heappop
from collections import defaultdict

def start_solve(next_problem, solve_order):
    queue = list()
    cur_order = 1
    visited = [False for _ in range(len(solve_order))]
    answer = []
    for problem, order in enumerate(solve_order):
        if order == 0:
            heappush(queue, problem)
            visited[problem] = True
    while queue:
        cur_problem = heappop(queue)
        answer.append(cur_problem+1)
        for np in next_problem[cur_problem]:
            solve_order[np] -= 1

        for problem, order in enumerate(solve_order):
            if order == 0 and not visited[problem]:
                heappush(queue, problem)
                visited[problem] = True
    return answer


def main():
    num_of_problem, num_of_order = map(int, input().rstrip().split(" "))
    next_problem = defaultdict(list)
    solve_order = [0 for _ in range(num_of_problem)]
    
    for _ in range(num_of_order):
        first, second = map(int, input().rstrip().split(" "))
        next_problem[first-1].append(second-1)
        solve_order[second-1] += 1
    print(' '.join(map(str, start_solve(next_problem, solve_order))))


if __name__ == "__main__":
    main()