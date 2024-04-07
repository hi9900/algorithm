import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj):
    dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque([(si, sj)])
    area = 1

    while q:
        ii, jj = q.popleft()
        for di, dj in dij:
            ni, nj = ii+di, jj+dj
            if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 0:
                q.append((ni, nj))
                board[ni][nj] = 1
                area += 1
    return area


M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] += 1

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            board[i][j] += 1
            cnt += 1
            result.append(bfs(i, j))

print(cnt)
print(*sorted(result))