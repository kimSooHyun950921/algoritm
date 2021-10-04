import math
def main():
    N, height = map(int, input().rstrip().split(" "))
    s2e = [0 for _ in range(height+1)]
    e2s = [0 for _ in range(height+1)]
    min_value = math.inf
    min_count = 0

    # preprocessing
    for i in range(N):
        num = int(input())
        if i % 2 == 0:
            s2e[num] += 1
        else:
            e2s[num] += 1

    # add cumulative
    for i in range(height-1, 0, -1):
        s2e[i] = s2e[i+1] + s2e[i]
        e2s[i] = e2s[i+1] + e2s[i]

    # search
    for i in range(1, height+1):
        #print(s2e[i], e2s[height+1-i])
        value = s2e[i] + e2s[height+1-i]
        if value < min_value:
            min_value = value
            min_count = 1
        elif value == min_value:
            min_count += 1
    
    return min_value, min_count

if __name__ == "__main__":
    min_value, min_count = main()
    print(min_value, min_count)