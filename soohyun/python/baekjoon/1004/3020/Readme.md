#  1. 문제의 핵심
## 1.1 문제요약
    - 동굴높이 H, 돌갯수 N과 석순(아래에서 위로)과 종유석(위에서 아래로)가 차례로 주어질때, 개똥벌레가 최소한의 돌을 뚫고 지나는 방법의 수
## 1.2 문제 알고리즘
    - 누적합(내가 푼방식)
    - 이분탐색


# 2. 자료구조 및 알고리즘
## 1.1 자료구조
    - 갯수가 각각 height인 석순과 종유석을 저장하는 리스트 각 2개
## 1.2 알고리즘
1. 입력받기 및 전처리
    1. i번째 입력이 짝수번째 일때는 석순리스트에 갯수 저장
    2. i번째 입력이 홀수번째 일때는 종유석리스트에 갯수 저장
2. 누적합
    1. 두 리스트를 끝부터 누적해서저장
        ```
        A[i] = A[i+1]+A[i]
        ```
4. 결과 확인
    1. i부터 모든 길이 순회
    2. 석순[시작] + 종유석[끝]의 크기를 비교
    3. 크기가 가장 작은것과 그 갯수를 세서 출력
5. 복기할것
    - 이분탐색으로 푸는 방법?
    