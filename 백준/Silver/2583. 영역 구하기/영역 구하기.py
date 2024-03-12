import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())

board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 사각형 영역 1로 채우기
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] += 1

dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
V = [[0] * N for _ in range(M)]
q = deque()
answer = []
# 영역 확인
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and V[i][j] == 0:
            q.append((i, j))
            V[i][j] = 1
            cnt = 0
            while q:
                ii, jj = q.popleft()
                cnt += 1
                for di, dj in dij:
                    ni, nj = ii+di, jj+dj
                    if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 0 and V[ni][nj] == 0:
                        q.append((ni, nj))
                        V[ni][nj] = 1

            answer.append(cnt)

print(len(answer))
print(*sorted(answer))