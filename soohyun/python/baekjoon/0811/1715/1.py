from collections import deque
from heapq import heappush, heappop

def solution(array):
    answer = 0
    while len(array) > 1:
        print("answer:", answer, array)
        val1 = heappop(array)
        val2 = heappop(array)
        heappush(array,val1+val2)
        answer += (val1+val2)
    return answer

def main():
    array = list()
    N = int(input())
    for _ in range(N):
        heappush(array, int(input()))
    print(solution(array))

if __name__ == "__main__":
    main()