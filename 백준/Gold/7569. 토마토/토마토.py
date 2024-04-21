import sys
from collections import deque
input = sys.stdin.readline

def solve_day(data, day):
    for h in data:
        for i in h:
            if 0 in i:
                return -1
    return day


q = deque()
# 가로칸 M, 세로칸 N, 높이 H
M, N, H = map(int, input().split())
data = [[[] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for i in range(N):
        data[h][i] = list(map(int, input().split()))
        for j in range(M):
            if data[h][i][j] == 1:
                q.append((h, i, j, 0))

# 6방향: 상 하 좌 우 위층 아래층
dhij = ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0))
day = 0
while q:
    h, i, j, day = q.popleft()

    for dh, di, dj in dhij:
        nh, ni, nj = h+dh, i+di, j+dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and data[nh][ni][nj] == 0:
            data[nh][ni][nj] = 1
            q.append((nh, ni, nj, day+1))

# 안 익은 토마토가 남아 있으면,
print(solve_day(data, day))
