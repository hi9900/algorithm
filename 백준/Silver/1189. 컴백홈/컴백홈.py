def dfs(s, e, d):
    global result, v
    si, sj = s

    if (si, sj) == e and d == K:
        result += 1
        return

    if d >= K:
        return

    for di, dj in dij:
        ni, nj = si + di, sj + dj
        if 0 <= ni < R and 0 <= nj < C and v[ni][nj] == 0 and board[ni][nj] != 'T':
            v[ni][nj] = 1
            dfs((ni, nj), e, d+1)
            v[ni][nj] = 0


R, C, K = map(int, input().split())
board = [input() for _ in range(R)]
v = [[0] * C for _ in range(R)]
dij = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = 0
v[R-1][0] = 1

dfs((R-1, 0), (0, C-1), 1)
print(result)