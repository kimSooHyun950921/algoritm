# 문제의 핵심
- 문자열처리
- 슬라이딩 윈도우
# 자료구조
- 각 알파벳 출현 인덱스를 가진 변수(word_dict): 딕셔너리
    - 키: 문자, 밸류: 리스트
  ```
  {'a':[1,2]}
  ```
- 출현횟수 이상을 가진 리스트(check_word): 리스트

# 알고리즘
- 문자의 출현 인덱스들의 리스트를 가지고 있는 딕셔너리(word_dict) 제작
- word_dict가 출현횟수(N)보다 같거나 큰 문자를 찾아 저장(check_list)
- check_list의 출현횟수(N)만큼의 길이만큼 시작/끝 값의 최소/최대값 반환

# 복기할것
- 반복문을 돌때 한번은 무조건돌려아햐므로 마지막은 len(loc_list)-N **+1**을 해야함
