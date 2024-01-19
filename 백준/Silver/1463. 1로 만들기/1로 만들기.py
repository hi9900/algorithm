from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
q.append((0, N))
v = [0] * (N+1)
while q:
    cnt, n = q.popleft()
    if n == 1:
        print(cnt)
        break

    if v[n] == 1:
        continue
    v[n] += 1

    if n % 3 == 0:
        q.append((cnt+1, n//3))
    if n % 2 == 0:
        q.append((cnt+1, n//2))
    q.append((cnt+1, n-1))
