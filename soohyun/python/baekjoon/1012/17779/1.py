import math
def calc(region, N):
    for r in range(N):
        for c in range(N):
            for d1 in range(N-2):
                for d2 in range(N-2):
                    max_region = 0
                    min_region = math.inf
                    if is_inrange(d1, d2, r, c):
                        region_1 = get_sum(1, r+d1, 1, c)
                        region_2 = get_sum(1, r+d2, c+1, N)
                        region_3 = get_sum(r+d1, N, 1, c-d1+d2-1)
                        region_4 = get_sum(r+d2+1, N, c-d1+d2, N)



def main():
    N = int(input())
    region = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    calc(region, N)
        

if __name__ == "__main__":
    main()