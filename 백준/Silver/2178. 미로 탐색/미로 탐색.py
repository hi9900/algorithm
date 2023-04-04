import sys
# input = sys.stdin.readline


def bfs():
    q = []
    v = set()

    q.append((0, 0))
    v.add((0, 0))

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1),):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if (ni, nj) not in v and data[ni][nj] == 1:
                    data[ni][nj] += data[ci][cj]
                    q.append((ni, nj))
                    v.add((ni, nj))
    return


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

bfs()
print(data[N-1][M-1])
