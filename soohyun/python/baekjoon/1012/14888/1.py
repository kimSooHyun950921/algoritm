import math

def calc_num(op, num1, num2):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    elif op == 3:
        if num1 == 0:
            buoho = 1
        else:
            buoho = num1 // abs(num1)
        return buoho * (abs(num1) // num2)
    return None

def calc(op_list, number):
    answer = number[0]
    for idx, op in enumerate(op_list):
        answer = calc_num(op, answer, number[idx+1])
        #print(answer, number[idx+1], op)

    return answer


def dfs(num_op, number):
    def recursive(op, op_list):
        min_value = math.inf
        max_value = -math.inf
        if len(op_list) == num_op:
            value = calc(op_list, number)
            min_value = min(min_value, value)
            max_value = max(max_value, value)
            return min_value, max_value
        for i in range(0, 4):
            if op[i] > 0:
                op[i] -= 1
                op_list.append(i)
                value = recursive(op, op_list)
                op_list.pop()
                op[i] += 1
                min_value = min(min_value, value[0])
                max_value = max(max_value, value[1])
        return min_value, max_value
    return recursive


def main():
    num_op = int(input().rstrip()) - 1
    number = list(map(int, input().rstrip().split(" ")))
    op = list(map(int, input().rstrip().split(" ")))
    min_val, max_val = dfs(num_op, number)(op, [])
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()