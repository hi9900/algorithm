import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

xij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(v, i, j, N, h):
    v[i][j] = 1
    for (xi, xj) in xij:
        ni, nj = i + xi, j + xj

        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] > h and v[ni][nj] == 0:
                dfs(v, ni, nj, N, h)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1
max_h = 0
for i in range(N):
    max_h = max(max_h, max(arr[i]))

for h in range(1, max_h):
    v = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and v[i][j] == 0:
                cnt += 1
                dfs(v, i, j, N, h)
    ans = max(ans, cnt)

print(ans)
