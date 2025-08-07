import sys
from collections import deque
input = sys.stdin.readline

dij = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(v, si, sj, n, h, arr):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ii, jj = q.popleft()
        for di, dj in dij:
            ni, nj = ii + di, jj + dj
            if 0 <= ni < n and 0 <= nj < n:
                if v[ni][nj] == 0 and arr[ni][nj] > h:
                    v[ni][nj] = 1
                    q.append((ni, nj))
    return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# 잠기는 높이 h = 1 -> max_h-1
max_h = 0
for i in range(n):
    max_h = max(max(arr[i]), max_h)

# 안전영역 safe
safe = 1
for h in range(1, max_h):
    v = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and v[i][j] == 0:
                cnt += 1
                bfs(v, i, j, n, h, arr)
        safe = max(safe, cnt)

print(safe)