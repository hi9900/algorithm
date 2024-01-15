import sys
input = sys.stdin.readline

# k층 n호 = k-1층 n호 + k층 n-1호
build = [list(range(15))] + [[0, 1] + [0] * 13 for _ in range(14)]

for i in range(1, 15):
    for j in range(1, 15):
        build[i][j] = build[i-1][j] + build[i][j-1]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    print(build[k][n])
