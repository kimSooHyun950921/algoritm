def sorting_col(r, c, arr):
    max_len = 0
    for j in range(c):
        num_dict = dict()
        # 갯수 세기
        for i in range(r):
            if arr[i][j] > 0:
                num_dict[arr[i][j]] = num_dict.get(arr[i][j], 0) + 1
        # 정렬하기
        num_arr = [(key, value) for key, value in num_dict.items()]
        num_arr = sorted(num_arr, key=lambda value: value[0])
        num_arr = sorted(num_arr, key=lambda value: value[1])
        # 숫자 다시 넣기
        i = 0
        for num, num_count in num_arr:
            if i >= 101:
                break
            arr[i][j] = num
            arr[i+1][j] = num_count
            i += 2
        for k in range(i, 101):
            arr[k][j] = 0
        max_len = max(max_len, i)
    return max_len

def sorting_row(r, c, arr):
    max_len = 0
    for i in range(r):
        num_dict = dict()
        # 갯수 세기
        for j in range(c):
            if arr[i][j] > 0:
                num_dict[arr[i][j]] = num_dict.get(arr[i][j], 0) + 1
        # 정렬하기
        num_arr = [(key, value) for key, value in num_dict.items()]
        num_arr = sorted(num_arr, key=lambda value: value[0])
        num_arr = sorted(num_arr, key=lambda value: value[1])
        # 숫자 다시 넣기
        j = 0
        for num, num_count in num_arr:
            if j > 101:
                break
            arr[i][j] = num
            arr[i][j+1] = num_count
            j += 2
        for k in range(j, 101):
            arr[i][k] = 0
        max_len = max(max_len, j)
    return max_len


def print_arr(arr, r, c):
    print()
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=" ")
        print()
    print()


def solution(tr, tc, tval, arr):
    count = 1
    rcount = 3
    ccount = 3

    while count <= 100:
        if rcount >= ccount:
            ccount = sorting_row(rcount, ccount, arr)
        else:
            rcount = sorting_col(rcount, ccount, arr)
        #print_arr(arr, rcount, ccount)
        if arr[tr][tc] == tval:
            return count
        count += 1
    return -1

def main():
    r, c, target = map(int, input().rstrip().split(" "))
    arr = [[0 for _ in range(101)] for _ in range(101)]
    is_answer = False
    for i in range(3):
        row = list(map(int, input().rstrip().split(" ")))
        for j, value in enumerate(row):
            if i == r-1 and j == c-1 and value == target:
                is_answer = True
            arr[i][j] = value
    if not is_answer:
        result = solution(r-1, c-1, target, arr)
    else:
        result = 0
    print(result)
            

if __name__ == "__main__":
    main()