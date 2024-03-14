import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
data = [input() for _ in range(M)]
V = [[0] * N for _ in range(M)]

# 맨 위(밖)의 0의 위치
start = []
for i in range(N):
    if data[0][i] == '0':
        start.append(i)

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque()

for y in start:
    q.append((0, y))
    V[0][y] = 1
    while q:
        ii,jj = q.popleft()
        for di, dj in dxy:
            ni, nj = ii+di, jj+dj

            if 0 <= ni < M and 0 <= nj < N and data[ni][nj] == '0' and V[ni][nj] == 0:
                q.append((ni, nj))
                V[ni][nj] = 1

print('YES') if 1 in V[-1] else print('NO')

