# 문제의 핵심
- 에라토스테네스의 체
- 투포인터

# 알고리즘
- 에라토스테네스의 체를 구한다.
- 에라토스테네스의 체를 이용하여 멈춤 조건까지 투포인터 알고리즘을 돌린다.
    ```
    - 초기화
        - start, end, value = 0, 1, prime[start] + prime[end]
    - 멈춤조건일때까지 돌림
        - 멈춤조건: start>end, start와 end의 값이 N보다 커질때 
        - 만약 현재 값이 입력값 N보다 크다면
        - start를 증가시켜주고 value에 prime숫자를 하나 뺀다.
        - 만약 현재 값이 입력값 N보다 작다면
        - end를 증가시켜주고 value에 prime 숫자를 하나 더한다.
        - 입력값과 현재값이 같다면
            - start는 현재 start 다음, end 는 start 바로 다음으로 초기화
            - count 를 하나 증가시켜줌
    ```

# Code Snippet
1. 에라토스테네스의 체
    - 내가 만든 코드
        ```python
            # 어차피 짝수는 제외하므로 홀수부터 시작
            # limit은 입력값에다 100을 더한값
            # (근거: 4000000 다음의 소수가 필요함 )
            raw = list(range(3, limit+100, 2)) 
            # 실제 소수는 2부터 시작하므로 2를 넣어주고 초기화
            prime = [2]
            # raw 길이 만큼 반복
            for i in range(len(raw)):
                # 현재 숫자가 0이면 소수가아니므로 넘어감
                number = raw[i]
                if number == 0:
                    continue
                # 시작은 i부터, number만큼 띄운다. 
                # 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23
                # 3일경우 세번째 후부터 3의 배수가 나옴
                # 5일경우 다섯번째 후부터 5의 배수가 나옴
                # 7일경우 일곱번째 후부터 7의 배수가 나옴
                for j in range(i, len(raw), number):
                    # 첫숫자가 다른숫자의 배수는 아니면(raw[i]>0)
                    # 무조건 소수
                    if j == i and raw[i] > 0:
                        prime.append(raw[j])
                    # 첫숫자가 아닌것은 첫숫자의 배수이므로
                    # 소수가 아님
                    else:
                        raw[j] = 0

        ```
    - 다른 사람 코드: (출처: https://mygumi.tistory.com/66 [마이구미의 HelloWorld])
        ```java
        int rootSqrt = (int) Math.sqrt(n);
        // 2부터 시작
        for(int i=2;i<=rootSqrt;i++) {
            // 현재 숫자가 True이면 소수가 아니므로 넘어감
            if (array[i]) {
                continue;
            }
            // 시작 숫자는 i의 2의 부터 ~
            // i만큼 띄어넘으며 모두 소수가 아닌것으로 체크
            // 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            // 2는 4부터 6, 8, 10, 12, 14, 16
            // 3은 6부터 6, 9, 12, 15, 18, 21는 소수가 아님
            for(int j=i+i;j<=1000000;j+=i) {
                array[j] = true;//소수가 아닌것으로 체크하는것
            }
        }
        ```
2. 투포인터 코드
    ```python
        # 시작, 끝 value, count 초기화
        start, end =0,  1
        value = prime[start] + prime[end]
        count = 0
        # 끝나는조건이 아니라면
        while stop_condition(start, end, prime, N):
            # value가 입력값보다 작다면
            if value > N:
                # 먼저 현재 숫자를 빼줘야함
                # 왜? 이미 value 부터 현재숫자가 더해져있으므로
                value -= prime[start]
                # start 인덱스 증가
                start += 1
            # value가 입력값보다 크다면
            elif value < N:
                # 인덱스를 먼저 늘리고
                # value를 더해줌
                # 이미 value가 더해져있으므로 value를 먼저 더해버리면 
                # 중복으로 더해지므로
                end += 1
                value += prime[end]
            # 동일하다면
            else:
                # 갯수를 증가시키고
                count += 1
                # 인덱스들 초기화
                start = start + 1
                end = start + 1
                value = prime[start] + prime[end]
    ```

# 복기할것
- 에라토스테네스의 체 구하는것이 생각보다오래 걸림
    - 처음엔 시간이 오래걸림
    - 공식을 아예 외워둘것
- start, end가 언제 더해지고 언제 빼지는지 순서를 처리하는것이 중요함
- 언제끝나는지도 중요함
    - start<=end 일때까지는 계속 돌아야 숫자가 N으로 일치할때도 count를 늘릴 수 있음
- 소수 2는 내 알고리즘으로 잡지 못함 따라서 예외처리 필요