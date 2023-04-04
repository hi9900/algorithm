import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while q:
        ci, cj, d = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if not v[ni][nj] and data[ni][nj] == 0:
                    data[ni][nj] += data[ci][cj] + 1
                    q.append((ni, nj, d+1))
                    v[ni][nj] = 1
    return d


M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
q = deque()
v = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            q.append((i, j, 0))

if len(q) == 0:
    result = -1
else:
    result = bfs()

# print(data)
for i in data:
    if 0 in i:
        result = -1
        break

print(result)