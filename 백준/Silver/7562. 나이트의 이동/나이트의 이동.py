import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    dxy = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2),)
    board = [[0] * N for _ in range(N)]

    q = deque([(0, *start)])
    board[start[0]][start[1]] = 1
    
    while q:
        c, x, y = q.popleft()

        if (x, y) == end:
            print(c)
            break

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                q.append((c+1, nx, ny))
                board[nx][ny] = 1
