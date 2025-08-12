import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dij = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
def dfs(ii, jj):
    global visited, w, h

    for di, dj in dij:
        ni, nj = ii + di, jj + dj
        if 0 <= ni < h and 0 <= nj < w:
            if visited[ni][nj] == 0 and data[ni][nj] == 1:
                visited[ni][nj] = 1
                dfs(ni, nj)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j)

    print(cnt)