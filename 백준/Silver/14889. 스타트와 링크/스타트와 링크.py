import sys
from itertools import combinations
input = sys.stdin.readline


def solve(diff, team_A, team_B, N):
    total_A, total_B = 0, 0
    for i in range(N//2):
        for j in range(N//2):
            total_A += data[team_A[i]][team_A[j]]
            total_B += data[team_B[i]][team_B[j]]

    return min(diff, abs(total_A - total_B))


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

teams = list(combinations(list(range(N)), N//2))
team_A = teams[:len(teams)//2]
team_B = teams[-1:len(teams)//2-1:-1]

diff = 10e9
for t in range(len(teams)//2):
    diff = solve(diff, team_A[t], team_B[t], N)
print(diff)
