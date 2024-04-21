import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

V = [0] * 1_000_001
q = deque([(S, 0)])
V[S] = 1
while q:
    i, c = q.popleft()
    if i == G:
        print(c)
        break

    for di in (U, -D):
        ni = i + di
        if 0 < ni <= F and V[ni] == 0:
            V[ni] = 1
            q.append((ni, c+1))

else:
    print('use the stairs')
