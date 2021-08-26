def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

def longest_palindrome_ex(word):
    longest_word = 0
    if len(word) <= 1:
        return 0
    if not is_palindrome(word):
        return len(word)
    else:
        longest_word = max(longest_word, longest_palindrome_ex(word[1:]))
        longest_word = max(longest_word, longest_palindrome_ex(word[:-1]))
    return longest_word
#aabbaa
#ababa

def is_all_same(word):
    previous_word = word[0]
    for i in range(len(word)//2+1):
        if word[i] == word[len(word)-i-1]:
            if word[i] != previous_word:
                return False
        else:
            return False
    return True

def longest_palindrome(word):
    if is_palindrome(word):
        if is_all_same(word):
            return 0
        else:
            return len(word[1:])
    else:
        return len(word)


def main():
    result = longest_palindrome(input())
    if result == 0:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()