import sys
import math
from collections import defaultdict
input = sys.stdin.readline

def make_word_dict(words):
    word_dict = defaultdict(list)
    for idx, word in enumerate(words):
        word_dict[word].append(idx)
    return word_dict


def solution(check_word, word_dict, N):
    min_value = math.inf
    max_value = 0
    for word in check_word:
        loc_list = word_dict[word]
        for i in range(0, len(loc_list)-N+1):
            start_idx = i
            end_idx = i + N - 1
            min_value = min(abs(loc_list[start_idx] - loc_list[end_idx])+1, min_value) 
            max_value = max(abs(loc_list[start_idx] - loc_list[end_idx])+1, max_value) 
            
    return min_value , max_value


def main():
    for _ in range(int(input().rstrip())):
        word_dict = make_word_dict(input().rstrip())
        N = int(input().rstrip())
        check_word = list()
        for key in word_dict.keys():
            if len(word_dict[key]) >= N:
                check_word.append(key)
        if len(check_word) > 0:
            min_value, max_value = solution(check_word, word_dict, N)
            print(min_value, max_value)
        else:
            print(-1)

if __name__ == "__main__":
    main()