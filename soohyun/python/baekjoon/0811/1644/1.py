LIMIT = 4000100
def stop_condition(start, end, prime, N):
    if start <= end:
        if start < len(prime) and end < len(prime):
            if prime[start] <= N and prime[end] <= N:
                return True
    return False

def solution(prime, N):
    start = 0
    end = 1
    value = prime[start] + prime[end]
    count = 0
    while stop_condition(start, end, prime, N):
        if value > N:
            value -= prime[start]
            start += 1
        elif value < N:
            end += 1
            value += prime[end]
        else:
            count += 1
            start = start + 1
            end = start + 1
            value = prime[start] + prime[end]
    return count


def make_prime_number(limit):
    raw = list(range(3, limit+100, 2))
    prime = [2]
    for i in range(len(raw)):
        number = raw[i]
        if number == 0:
            continue
        for j in range(i, len(raw), number):
            if j == i and raw[i] > 0:
                prime.append(raw[j])
            else:
                raw[j] = 0
    return prime

def main():
    N = int(input().rstrip())
    prime_number = make_prime_number(N)

    if N == 2:
        print(1)
    else:
        print(solution(prime_number, N))

if __name__ == "__main__":
    main()