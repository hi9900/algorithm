import sys
from collections import deque
input = sys.stdin.readline


def rgb(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = color[data[x][y]]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not check[ni][nj]:
                    if data[ci][cj] == data[ni][nj]:
                        check[ni][nj] = color[data[ci][cj]]
                        q.append((ni, nj))

def rb(x, y):
    q = deque()
    q.append((x, y))
    check_r[x][y] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if not check_r[ni][nj]:
                    if check[ci][cj] == check[ni][nj]:
                        check_r[ni][nj] = 1
                        q.append((ni, nj))

N = int(input())
data = [list(input().rstrip()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
color = {
    'R': 1,
    'G': 1,
    'B': 3,
}
cnt = 0
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            rgb(i, j)
            cnt += 1


check_r = [[0]*N for _ in range(N)]
cx = 0
for i in range(N):
    for j in range(N):
        if not check_r[i][j]:
            rb(i, j)
            cx += 1

print(cnt, cx)