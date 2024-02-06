import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    data = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        data[Y][X] += 1

    dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
    cnt = 0
    stack = []
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and v[i][j] == 0:
                cnt += 1
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    v[x][y] = 1
                    for dx, dy in dxy:
                        ni, nj = x + dx, y + dy
                        if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 1 and v[ni][nj] == 0:
                            stack.append((ni, nj))

    print(cnt)
