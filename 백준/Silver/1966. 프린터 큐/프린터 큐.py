import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append((data[i], i))

    cnt = 0
    while q:
        # q의 max 우선순위
        max_q = max(q)[0]

        if q[0][0] < max_q:
            q.rotate(-1)
        else:
            a, b = q.popleft()
            cnt += 1
            if b == M:
                print(cnt)
                break
