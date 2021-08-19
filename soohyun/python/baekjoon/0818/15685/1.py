DIRECTION = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def rotation(curve, gen):
    new = list()
    for i in range(len(curve)):
        new.append((curve[i][1], (1<<gen)-curve[i][0]-1))
    return new


def match_end(new_curve, original_curve, dragon_curve):
    r = original_curve[-1][0] - new_curve[-1][0]
    c = original_curve[-1][1] - new_curve[-1][1]
    for i in range(len(new_curve)-2, -1, -1):
        change_r, change_c = new_curve[i][0]+r, new_curve[i][1]+c
        original_curve.append((change_r, change_c))
        dragon_curve[change_r][change_c] = 1


def check_original_curve(curve, dragon_curve):
    for r, c in curve:
        dragon_curve[r][c] = 1

def make_dragon_curve(col, row, direction,
                      generation, dragon_curve):
    original_curve = [(row, col), 
                     (row+DIRECTION[direction][0], 
                      col+DIRECTION[direction][1])]
    check_original_curve(original_curve, dragon_curve)
    for c_gen in range(0, generation):
        # rotation
        new_curve = rotation(original_curve, c_gen)
        # 끝맞추기
        match_end(new_curve, original_curve, dragon_curve)


def count_square(dragon_curve):
    square = [(0, 0), (0, 1), (1, 0), (1, 1)]
    count_square = 0
    for i in range(0, 100):
        for j in range(0, 100):
            is_square = True
            for square_r, square_c in square:
                if not dragon_curve[square_r+i][square_c+j]:
                    is_square = False
            if is_square:
                count_square += 1
    return count_square
            

def main():
    dragon_curve = [[0 for _ in range(101)] for _ in range(101)]
    for _ in range(int(input().rstrip())):
        col, row, direction, generation = \
            map(int, input().rstrip().split(" "))
        make_dragon_curve(col, row, direction, 
                          generation, dragon_curve)
    print(count_square(dragon_curve))


if __name__ == "__main__":
    main()
