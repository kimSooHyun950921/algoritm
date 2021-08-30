# 문제의 핵심
- 분할정복
- dp

# 자료구조
- dp: dictionary
- matrix: 2차원 배열 

# 알고리즘
1. num==0 이면 단위 행렬반환
2. num==1 이면 가장 기본 행렬 반환
3. 현재 dp에 있으면 제곱된 결과가 있으면 그결과반환
4. 그렇지 않으면
    - 짝수이면 num//2*num//2로 나눔
    - 홀수이면 num*(num-num//2)로 나누어 그 값을 저장

# Code Snippet
1. 배열곱
```python
def matmul(A, B):
    #A의 내려가는 행
    result = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for i in range(len(A)):
        # B에서 열
        for k in range(len(A)):
            # 한열에서 내려가는것
            value = 0
            for j in range(len(A[i])):
                value += A[i][j] * B[j][k]
            result[i][k] = value
    return result
```

# 복기할것
- 이미 결과는 dp가 가지고 있다는것을 가정하기때문에, 
```matrix_data[num] = matmul(matrix_data[num//2], matrix_data[num//2]``` 이렇게 쓰지 않고 
```matrix_data[num] = matmul(multiple(num//2, matrix_data), multiple(num//2, matrix_data))``` 와 같이 써도 두번 연산을 안하게된다. 
- 메모리에러:
    - dp의 자료구조를 리스트를 썼더니 메모리 에러남 사용하지 않는 숫자도 메모리에 할당해서 그런가보다
- 틀렸습니다
    - 입력값을 나머지 연산한 형태롤 받아야한다. 1000을 받으면 이미 없애서 연산해야하나보다.
