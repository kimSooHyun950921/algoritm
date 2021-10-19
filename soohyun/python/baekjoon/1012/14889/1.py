import math

def get_ab(team, ability):
    total_ability = 0
    for i in team:
        for j in team:
            total_ability += ability[i][j]
    return total_ability

def dfs(N, ability, person):
    def recursive(start_team, start):
        answer = math.inf
        if len(start_team) == N//2:
            link_team = person - start_team
            start_ab = get_ab(list(start_team), ability)
            link_ab = get_ab(list(link_team), ability)
            return min(answer, abs(start_ab - link_ab))
        for i in range(start, N):
            add_set = set()
            add_set.add(i)
            answer = min(answer, recursive(start_team.union(add_set), i+1))
        return answer
    return recursive

def main():
    N = int(input())
    ability = list()
    person = set([i for i in range(N)])
    for _ in range(N):
        row = list(map(int, input().rstrip().split()))
        ability.append(row)

    value = dfs(N, ability, person)(set(), 0)
    print(value)

if __name__ == "__main__":
    main()