# import sys
# input = sys.stdin.readline

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

data = [list(input().rstrip()) for _ in range(N)]
v = [[0] * N for _ in range(N)]

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
cnt = 0
q = deque()
result = []
for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and v[i][j] == 0:
            cnt += 1
            q.append((i, j, cnt))
            v[i][j] = cnt
            r = 0
            while q:
                x, y, c = q.popleft()
                r += 1
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == '1' and v[nx][ny] == 0:
                        q.append((nx, ny, c))
                        v[nx][ny] = c

            result.append(r)
result.sort()
print(cnt)
print(*result, sep="\n")
