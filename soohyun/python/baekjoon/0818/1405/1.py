def solution(N, e, w, s, n):
    direction_percentage = [e, w, s, n]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def start_move(count, r, c, visited):
        percentage = 0
        if count < N:
            for i, direct in enumerate(direction):
                nr, nc = r + direct[0], c + direct[1]
                if visited.get((nr, nc)) is not None:
                    continue
                else:
                    visited[(nr, nc)] = True
                    current_percentage = direction_percentage[i] / 100
                    current_percentage = current_percentage*start_move(count+1, nr, nc, visited)
                    percentage += current_percentage
                    visited.pop((nr, nc))
        else:
            percentage = 1
        return percentage
    return start_move

def main():
    N, e, w, s, n = map(int, input().rstrip().split(" "))
    # 동동/ 서서/ 남남/ 북북/ 동서/ 남북/ 서동/ 북남/ 서남/ 동남/ 남서/ 남동/ 
    # 전체경우의수: 4**N
    start_move = solution(N, e, w, s, n)
    print(start_move(0, 0, 0, {(0,0):True}))

if __name__ == "__main__":
    main()