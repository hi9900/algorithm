import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

check = [0] * (100_001)

q = deque()
q.append((N, 0))
min_time = 100_001

while q:
    now, time = q.popleft()
    check[now] = time

    if now == K:
        print(time)
        break

    else:
        if 0 <= now+1 <= 100_000 and check[now+1] == 0:
            q.append((now+1, time+1))

        if 0 <= now-1 <= 100_000 and check[now-1] == 0:
            q.append((now-1, time+1))

        if 0 <= now*2 <= 100_000 and check[now * 2] == 0:
            q.append((now*2, time+1))
