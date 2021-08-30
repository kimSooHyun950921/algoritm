def multiple_minus(current, remember):
    return current * current - remember * remember

def is_end(current, remember, G):
    if multiple_minus(current, remember) > G:
        if current - remember == 1:
            return True
    return False

def solution(G):
    current = 1
    remember = 1
    is_print = False
    while not is_end(current, remember, G):
        #print(remember, current)
        if multiple_minus(current, remember) > G:
            remember += 1
        else:
            if multiple_minus(current, remember) == G:
                is_print = True
                print(current)
            current += 1
    return is_print



def main():
    G = int(input())
    if not solution(G):
        print(-1)

if __name__ == "__main__":
    main()