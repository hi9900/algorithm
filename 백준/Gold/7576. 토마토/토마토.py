import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 1 익은토마토 / 0 안익은토마토 / -1 빈 칸
dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
tomato = deque()
d = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tomato.append((i, j, 0))

while tomato:
    i, j, d = tomato.popleft()
    for di, dj in dij:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            tomato.append((ni, nj, d+1))
            board[ni][nj] = 1

for i in board:
    if 0 in i:
        print(-1)
        break

else: print(d)
