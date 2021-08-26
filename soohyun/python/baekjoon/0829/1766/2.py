from heapq import heappush, heappop
from collections import defaultdict

def start_solve(next_problem, solve_order):
    queue = list()
    answer = []

    for problem, order in enumerate(solve_order):
        if order == 0:
            heappush(queue, problem)
    while queue:
        cur_problem = heappop(queue)
        print(cur_problem+1, end=" ")
        answer.append(cur_problem+1)
        for problem in next_problem[cur_problem]:
            solve_order[problem] -= 1
            if solve_order[problem] == 0:
                heappush(queue, problem)
    return answer


def main():
    num_of_problem, num_of_order = map(int, input().rstrip().split(" "))
    next_problem = defaultdict(list)
    solve_order = [0 for _ in range(num_of_problem)]
    
    for _ in range(num_of_order):
        first, second = map(int, input().rstrip().split(" "))
        next_problem[first-1].append(second-1)
        solve_order[second-1] += 1
    start_solve(next_problem, solve_order)
    #print(' '.join(map(str, start_solve(next_problem, solve_order))))


if __name__ == "__main__":
    main()