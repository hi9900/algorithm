import sys
input = sys.stdin.readline

dij = ((-1, 0), (0, 1), (1, 0), (0, -1),)

C, R = map(int, input().split())
data = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

K = int(input())
result = (0,)

si, sj = R-1, 0
num = 1
data[si][sj] = num
visited[si][sj] = 1

while not result:
    if K > C * R:
        result = (0,)
        break
    if K == 1:
        result = (1, 1)
        break
        ??????????????

    for di, dj in dij:
        while 1:
            ni, nj = si+di, sj+dj
            if 0 <= ni < R and 0 <= nj < C:
                if visited[ni][nj]:
                    break
                elif visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    num += 1
                    data[ni][nj] = num
                    si, sj = ni, nj
                    if num == K:
                        result = (sj + 1, R - si)
                        break
            else:
                break
        if result:
            break

print(*result)