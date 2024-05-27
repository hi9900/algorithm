from collections import deque


def bfs(start):
    global v

    q = deque([])
    q.append((0, *start))
    v[start[0]][start[1]] = 0

    while q:
        d, ii, jj = q.popleft()

        for di, dj in dij:
            ni, nj = ii + di, jj + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == -1:
                # 갈 수 있는 땅
                if board[ni][nj] == 1:
                    v[ni][nj] = d + 1
                    q.append((d + 1, ni, nj))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
v = [[-1] * m for _ in range(n)]
dij = ((-1, 0), (1, 0), (0, -1), (0, 1))

# 목표 지점(2) 찾기
target = (-1, -1)
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            target = (i, j)
        if board[i][j] == 0:
            v[i][j] = 0

# 목표 지점 에서 bfs
bfs(target)

for i in v:
    print(*i)
