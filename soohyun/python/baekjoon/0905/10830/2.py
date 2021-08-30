def matmul(A, B):
    #A의 내려가는 행
    result = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        # B에서 열
        for k in range(len(A)):
            # 한열에서 내려가는것
            value = 0
            for j in range(len(A[i])):
                value += A[i][j] * B[j][k]%1000
            result[i][k] = value % 1000
    return result

def print_matrix(matrix):
    for row in matrix:
        print(*row)


def multiple(num, matrix_data):
    if num == 0:
        return matrix_data[0]
    elif num == 1:
        return matrix_data[1]
    if matrix_data.get(num, None) is not None:
        return matrix_data[num]
    else:
        if num % 2 == 0:
            matrix_data[num] = matmul(multiple(num//2, matrix_data), multiple(num//2, matrix_data))
        else:
            matrix_data[num] = matmul(multiple(num//2, matrix_data), multiple(num-num//2, matrix_data))
        return matrix_data[num]

def unit_maxtrix(N):
    return [[1 if i==j else 0 for j in range(N)] for i in range(N)]

def mod_int(num):
    return int(num) % 1000

def main():
    N, B = map(int, input().rstrip().split(" "))
    matrix = [list(map(mod_int, input().rstrip().split(" "))) for _ in range(N)]
    matrix_data = dict()
    matrix_data[0] = unit_maxtrix(N)
    matrix_data[1] = matrix
    print_matrix(multiple(B, matrix_data))


if __name__ == "__main__":
    main()