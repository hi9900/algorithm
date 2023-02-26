import sys
sys.stdin = open("input.txt")

T = 10
for _ in range(T):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    result = 0
    for i in range(16):
        for j in range(16):
            if data[i][j] == 2:
                si, sj = i, j

    dij = ((-1, 0), (0, -1), (1, 0), (0, 1))
    visited = [[0] * 16 for _ in range(16)]
    stack = [(si, sj)]
    ii, jj = si, sj
    while stack:
        visited[ii][jj] += 1
        for di, dj in dij:
            ni, nj = ii+di, jj+dj
            if data[ni][nj] == 3:
                result = 1
                break
            if data[ni][nj] + visited[ni][nj] == 0:
                stack.append((ni, nj))
        else:
            ii, jj = stack.pop()
        if result == 1:
            break

    print(f"#{tc}", result)
