import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
V = [0] * 100_001

q = deque()
q.append((N, 0))
time = 0
while q:
    X, time = q.popleft()
    if X < 0 or X > 100_000:
        continue
    if X == K:
        print(time)
        break
    if V[X]:
        continue

    V[X] += 1
    q.append((X-1, time+1))
    q.append((X+1, time+1))
    q.append((2*X, time+1))