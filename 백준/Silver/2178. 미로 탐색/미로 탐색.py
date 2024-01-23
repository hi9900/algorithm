from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [['0']*(M+2)] + [['0'] + list(input().rstrip()) + ['0'] for _ in range(N)] + [['0']*(M+2)]
v = [[0] * (M+2) for _ in range(N+2)]

dxy = ((-1, 0), (1, 0), (0, -1), (0, 1),)
q = deque()
# start: 1, 1 // end: N, M
# x, y, cnt
q.append((1, 1, 1))
v[1][1] = 1
while q:
    x, y, c = q.popleft()
    if x == N and y == M:
        print(c)
        break

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if maze[nx][ny] == '1' and v[nx][ny] == 0:
            q.append((nx, ny, c+1))
            v[nx][ny] = 1
