def print_board(removed_one):
    board = [[1 if (i, j) in removed_one else 0 for j in range(10)] for i in range(10)]
    print("")
    for row in board:
        print(*row)
    print("")

def make_set(row, col, size):
    paper = set()
    for r in range(0, size):
        for c in range(0, size):
            if r+row < 10 and c+col < 10:
                paper.add((r+row, c+col))
            else:
                return {}
    return paper

def solution():
    global count
    remain_paper = [0, 5, 5, 5, 5, 5]
    count = 25
    def dfs(row, col, one):
        global count
        if count < 25 - sum(remain_paper):
            return count
        if len(one) <= 0:
            return 25 - sum(remain_paper)
        for i in range(row, 10):
            next_col = col if i == row else 0
            for j in range(next_col, 10):
                if (i, j) in one:
                    for k in range(5, 0, -1):
                        paper = make_set(i, j, k)
                        if paper:
                            #print("paper", paper)
                            # 원상복구
                            removed_one = one-paper
                            if remain_paper[k] > 0 and len(removed_one) == (len(one) - len(paper)):
                                    remain_paper[k] -= 1
                                    print_board(removed_one)
                                    if count > 25-sum(remain_paper):
                                        result = dfs(i, j+1, removed_one)
                                        print(result, count)
                                        count = min(result, count)
                                    print("count", count)
                                    remain_paper[k] += 1
                    #print("count", count, "result", result)
        print("result", count)
        return count
    return dfs

def main():
    one = set()
    for r in range(0, 10):
        for idx, c in enumerate(input().rstrip().split(" ")):
            if c == '1':
                one.add((r, idx))
    #print(one)
    result = solution()(0, 0, one)
    print(result) if result < 25 else print(-1)
        


if __name__ == "__main__":
    main()