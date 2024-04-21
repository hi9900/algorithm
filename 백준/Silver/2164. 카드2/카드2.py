from collections import deque

import sys
input = sys.stdin.readline

N = int(input())
q = deque(range(1, N+1))

while q:
    result = q.popleft()
    q.rotate(-1)

print(result)