import sys
from collections import deque
input = sys.stdin.readline


def move(X, c):
    q = deque()
    v = [0] * 100001
    q.append((X, c))
    v[X] += 1

    if X == K:
        return 0

    while q:
        c = q.popleft()
        if c[0] == K:
            return c[1]
        for d in (1, -1, c[0]):
            m = c[0] + d
            if m < 0 or m > 100000:
                continue
            if not v[m]:
                q.append((m, c[1]+1))
                v[m] += 1


N, K = map(int, input().split())
print(move(N, 0))

