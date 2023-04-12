import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = deque(data)
    cnt = 0
    star = max(p)
    while p:
        if p[0] == star:
            p.popleft()
            cnt += 1
            if M == 0:
                print(cnt)
                break
            M -= 1
            star = max(p)

        elif p[0] < star:
            p.rotate(-1)
            if M == 0:
                M = len(p)-1
            else:
                M -= 1
