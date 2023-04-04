import sys
from collections import deque
input = sys.stdin.readline


def bfs_f():
    v = set()

    while f:
        ci, cj, t = f.popleft()
        v.add((ci, cj))
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if (ni, nj) not in v and data[ni][nj] != "#":
                    fire[ni][nj] += t+1
                    f.append((ni, nj, t+1))
                    v.add((ni, nj))


def bfs_j(si, sj):
    q = deque()
    q.append((si, sj, 0))
    v = set()
    v.add((si, sj))

    while q:
        ci, cj, t = q.popleft()
        if ci == 0 or ci == N-1 or cj == 0 or cj == M-1:
            return t+1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if (ni, nj) not in v and data[ni][nj] == ".":
                    if fire[ni][nj] > t+1 or fire[ni][nj] == 0:
                        move[ni][nj] = t+1
                        q.append((ni, nj, t+1))
                        v.add((ni, nj))
    return "IMPOSSIBLE"


N, M = map(int, input().split())
data = [list(input().rstrip()) for _ in range(N)]
fire = [[0] * M for _ in range(N)]
move = [[0] * M for _ in range(N)]
f = deque()

for i in range(N):
    for j in range(M):
        if data[i][j] == "J":
            si, sj = i, j

        if data[i][j] == "F":
            f.append((i, j, 0))
            fire[i][j] = -1

bfs_f()
print(bfs_j(si, sj))