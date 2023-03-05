import sys
from pprint import pprint

N, M = map(int, sys.stdin.readline().split())

data = [[0] * (M+2)] + [[0] + list(map(int, sys.stdin.readline().rstrip())) + [0] for _ in range(N)] + [[0] * (M+2)]
visited = [[0] * (M+2) for _ in range(N+2)]
dij = ((1, 0), (0, 1), (-1, 0), (0, -1))
i, j = 1, 1
stack = [(i, j)]
visited[i][j] += 1

result = 1
while stack:
    i, j = stack.pop()
    if (i, j) == (N, M):
        continue

    for di, dj in dij:
        ni, nj = i + di, j + dj
        if not visited[ni][nj] and data[ni][nj]:
            stack.append((ni, nj))
            if data[ni][nj] != 1 and data[ni][nj] <= data[i][j] + 1:
                continue
            else:
                data[ni][nj] = data[i][j] + 1
                visited[ni][nj] += 1

            if (ni, nj) == (N, M):
                visited[ni][nj] = 0

print(data[N][M])