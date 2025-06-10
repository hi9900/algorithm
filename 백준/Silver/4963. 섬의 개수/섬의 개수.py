import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(x, y, visited):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited[x][y] = 1

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny, visited)


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                dfs(i, j, v)
                cnt += 1

    print(cnt)
